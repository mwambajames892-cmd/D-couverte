import pathlib, re
p = pathlib.Path.home()/'motion-design-claude-code/presentation/assemble.sh'
s = p.read_text()
# 1. réglage de la vidéo du logo
if 'LOGO_VIDEO=' not in s:
    s = s.replace('RUN_LINT="${RUN_LINT:-1}"', '# Vidéo du logo animé (séquence 9) : posée à la racine par l\'orchestrateur, ouverte par le même cercle que l\'iris.\nLOGO_VIDEO="assets/video/james-framotion-reveal-9x16.mp4"\nLOGO_DUR="6.00"\n\nRUN_LINT="${RUN_LINT:-1}"', 1)
    s = s.replace('export FIRST_FRAME END_CARD TOTAL AUDIO', 'export LOGO_VIDEO LOGO_DUR FIRST_FRAME END_CARD TOTAL AUDIO', 1)
# 2. anneau de l'iris à la taille du canevas portrait
s = s.replace('<svg width="1920" height="1080" viewBox="0 0 1920 1080" style="position:absolute;inset:0">', '<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0">')
# 3. la vidéo à la racine, juste avant les calques de l'iris
if 'id="logovid"' not in s:
    anchor = "    fx += f'''\n      <div id=\"fxiris\""
    assert anchor in s
    add = ("    if env.get(\"LOGO_VIDEO\"):\n"
           "        fx += f'''\n"
           "      <video id=\"logovid\" class=\"clip\" data-start=\"{round(iris_at + 0.05, 3)}\" data-duration=\"{env[\"LOGO_DUR\"]}\" data-track-index=\"14\" src=\"{env[\"LOGO_VIDEO\"]}\" muted playsinline style=\"position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover;z-index:58\"></video>'''\n")
    s = s.replace(anchor, add + anchor, 1)
# 4. le cercle d'ouverture s'applique aussi à la vidéo
tw = '        tl.fromTo("#fxiris-ring"'
assert tw in s
if '#logovid' not in s:
    s = s.replace(tw, '        tl.fromTo("#logovid", {{ clipPath: "circle(0% at {ix}px {iy}px)" }}, {{ clipPath: "circle(160% at {ix}px {iy}px)", duration: 0.75, ease: "power2.inOut", immediateRender: false }}, {t(0.05)});\n' + tw, 1)
p.write_text(s); print('ok')
