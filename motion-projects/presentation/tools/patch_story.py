import pathlib, re
p = pathlib.Path('/tmp/gen/story.py'); s = p.read_text()
# 1. le texte des puces d'outils devient les 3 logos fournis
s = s.replace("les 3 puces d'outils « Premiere Pro », « CapCut », « DaVinci »", "les 3 logos d'outils fournis (assets/logos/premiere.png, capcut.png, davinci.jpg) dans des tuiles blanches de 88 u aux angles arrondis, avec le nom « Premiere Pro », « CapCut », « DaVinci » en mono sous chaque tuile")
s = s.replace("0.30 les 3 puces d'outils paraissent une à une (0.1 s d'écart, échelle .8 → 1)", "0.30 les 3 tuiles-logos (Premiere Pro, CapCut, DaVinci, fichiers de assets/logos) paraissent une à une (0.1 s d'écart, échelle .8 → 1)")
s = s.replace("les 3 puces, « Hook visuel, étalonnage, ».", "les 3 logos d'outils, « Hook visuel, étalonnage, ».")
# 2. fin : tenue de 2 s + iris vers la séquence logo
s = s.replace("b=36.68, type='cta'", "b=38.68, type='cta'")
s = s.replace("hout=\"aucun (fin du film : tenue vivante jusqu'à 36.68, la tête de lecture arrive au bout de la règle)\"",
  "hout=\"HS8 : iris vert-bleu : un cercle (rayon 0 → 2492 u) s'ouvre depuis le bouton « Abonné ✓ » (centre x 540, y 1215) à 38.63 s ; la carte de fin est figée dans son dernier état (bouton « Abonné ✓ », les 4 réseaux allumés, la règle arrivée au bout x 1010) ; aucun sous-titre ; papier clair, grain 14 %\"")
s = s.replace("scenes=[\n  (\"0.00 à 2.64\", 1, \"« James Framotion, ton monteur vidéo. » : le mot-symbole\"", "scenes=[\n  (\"0.00 à 2.64\", 1, \"« James Framotion, ton monteur vidéo. » : le mot-symbole\"")
s = s.replace("4.30 à 4.62 tenue vivante : l'onde finit, la tête de lecture arrive au bout de la règle.", "4.30 l'onde finit ; la tête de lecture est arrivée au bout de la règle (x 1010 à 4.62).")
s = s.replace("(\"2.64 à 4.62\", 2, \"« Écris-moi en DM et abonne-toi ! » : le clic\"", "(\"2.64 à 4.62\", 2, \"« Écris-moi en DM et abonne-toi ! » : le clic\"")
# scène 3 de la séquence 8 : tenue vivante de 2 s (ajoutée avant le crochet fermant de la séquence)
old = "\"SON : ping à 2.64, pop à 3.30, clic à 4.20.\", \"IMAGE CLÉ : 4.30 : la carte « Écris-moi… », le bouton « Abonné ✓ », l'onde, @jamesframotion, la règle arrivée au bout.\")]),\n]"
assert old in s
new = ("\"SON : ping à 2.64, pop à 3.30, clic à 4.20.\", \"IMAGE CLÉ : 4.30 : la carte « Écris-moi… », le bouton « Abonné ✓ », l'onde, @jamesframotion, la règle arrivée au bout.\"),\n"
 "  (\"4.62 à 6.62\", 3, \"tenue vivante : les réseaux s'allument un à un, le bouton prépare l'iris\",\n"
 "   \"TEXTE ÉCRAN : aucun sous-titre (la voix est finie à 4.58) ; le sous-titre « Écris-moi en DM et abonne-toi ! » part à 4.62 ; écart aucun texte.\",\n"
 "   \"IMAGE DE DÉPART : la carte « Écris-moi… », le bouton « Abonné ✓ », les 4 réseaux, @jamesframotion, la règle arrivée au bout.\",\n"
 "   \"ÉTAPES : 4.62 le sous-titre part (opacité 1 → 0, flou 6) ; 4.80 les 4 icônes des réseaux s'allument à tour de rôle (TikTok 4.80, Instagram 5.05, Facebook 5.30, YouTube 5.55 ; échelle 1 → 1,15 → 1, lueur vert-bleu clair, 0.25 s chacune) ; 5.10 un deuxième anneau vert-bleu part du bouton et s'élargit (échelle 1 → 3, opacité .5 → 0, 0.7 s) ; 5.70 le bouton « Abonné ✓ » respire une fois (échelle 1 → 1,05 → 1, 0.4 s) ; 6.10 la bulle grise « Hey 😍 … » et le champ « Écris-moi… » glissent de 12 u vers le haut (dérive lente) ; 6.30 le bouton se centre à l'image pour l'iris (immobile).\",\n"
 "   \"PISTE CAMÉRA : dérive linéaire seulement (+12 u/s vers le haut, plus lente que le reste du film) ; aucun cran ; la séquence reste montée jusqu'à 7.37 s sous l'iris.\",\n"
 "   \"COUCHES ET PROFONDEUR : avant-plan l'anneau qui s'élargit ; sujet le bouton et les réseaux ; fond le mot-symbole et le halo ; 3 couches.\",\n"
 "   \"OBJET-PONT ET VECTEUR : le bouton « Abonné ✓ » est le centre de l'iris (x 540, y 1215) : le cercle de la séquence 9 en sort.\",\n"
 "   \"SON : ping à 4.80, 5.05, 5.30, 5.55 (un par réseau) ; riser de 5.9 à 6.6 (avant l'iris) ; impact grave à 6.57 (l'iris s'ouvre).\", \"IMAGE CLÉ : 5.30 : les 4 réseaux dont Facebook allumé, le deuxième anneau qui part du bouton.\")]),\n"
 " dict(n=9, id='09-logo', title=\"Le logo animé de James\", a=38.68, b=44.68, type='cta', bp='logo-assemble-lockup', rules='ambient-glow-bloom',\n"
 "  voice=\"(aucune voix : musique et bruitages seuls)\",\n"
 "  focal=\"la vidéo du logo animé de James (fichier fourni, 1080 × 1920, 6.00 s), en plein cadre\",\n"
 "  scene=\"L'iris vert-bleu s'ouvre sur le fond sombre de la marque et le logo animé fourni joue en plein cadre (trait, cercle, Ø barré, JAMES FRAMØTION, réseaux, @jamesframotion) ; aucune voix\",\n"
 "  hin=\"HS8 : iris vert-bleu : un cercle (rayon 0 → 2492 u) s'ouvre depuis le bouton « Abonné ✓ » (centre x 540, y 1215) à 38.63 s ; la carte de fin est figée dans son dernier état (bouton « Abonné ✓ », les 4 réseaux allumés, la règle arrivée au bout x 1010) ; aucun sous-titre ; papier clair, grain 14 %\",\n"
 "  hout=\"aucun (fin du film : le logo tient sa dernière image jusqu'à 44.68, puis noir)\",\n"
 "  cues=\"\",\n"
 "  scenes=[(\"0.00 à 6.00\", 1, \"le logo animé fourni joue en plein cadre\",\n"
 "   \"TEXTE ÉCRAN : aucun texte ajouté (les textes JAMES, FRAMØTION et @jamesframotion sont dans la vidéo fournie) ; écart aucun texte.\",\n"
 "   \"IMAGE DE DÉPART : handoff_in : le cercle d'iris qui s'ouvre sur le fond sombre #030B10.\",\n"
 "   \"ÉTAPES : 0.00 la vidéo assets/video/james-framotion-reveal-9x16.mp4 démarre (6.00 s, 1080 × 1920, sans son) ; la suite (trait, cercle blanc à rayons, Ø barré, mot-symbole, réseaux, poignée) est celle de la vidéo ; 5.00 à 6.00 tenue de la dernière image.\",\n"
 "   \"PISTE CAMÉRA : celle de la vidéo fournie (aucune caméra ajoutée).\",\n"
 "   \"COUCHES ET PROFONDEUR : une couche : la vidéo sur le sol sombre.\",\n"
 "   \"OBJET-PONT ET VECTEUR : le cercle d'iris de la séquence 8 devient le cercle blanc du logo.\",\n"
 "   \"SON : musique seule, impact grave à 0.00, whoosh à 0.30, ping à 1.2 (le cercle), pop à 2.3 (le Ø), shimmer à 3.2 (le mot-symbole), pop à 4.0 (les réseaux), aucune voix.\", \"IMAGE CLÉ : 3.60 : JAMES FRAMØTION net sur le fond vert-bleu sombre, les 4 réseaux qui s'allument.\")]),\n]")
s = s.replace(old, new)
# 3. en-tête
s = s.replace("total = round(sum(fr['b']-fr['a'] for fr in FRAMES), 2)", "total = round(sum(fr['b']-fr['a'] for fr in FRAMES), 2)  # 36.68 de voix + 2.00 de tenue + 6.00 de logo = 44.68")
s = s.replace("(« Écris-moi… » (35 s) ;", "(« Écris-moi… » (35 s) ;")
s = s.replace("séquence 8 = la carte de fin. Tout est en monde clair (papier #F1EEE7) : pas de flash ni d'iris, la continuité est faite par le défilement.", "séquence 8 = la carte de fin ; séquence 9 = le logo animé de James sur fond sombre. Tout est en monde clair (papier #F1EEE7) jusqu'à la séquence 8 : un seul iris vert-bleu (38.63 s) ouvre le logo sombre ; la continuité est faite par le défilement.")
s = s.replace("- Acte 4 (28.76 à 36.68) : l'avatar, le mot-symbole, la carte « Écris-moi… » ; même fond.", "- Acte 4 (28.76 à 38.68) : l'avatar, le mot-symbole, la carte « Écris-moi… » (2 s de tenue vivante après la voix) ; même fond.\\n- Acte 5 (38.68 à 44.68) : le logo animé fourni (assets/video), fond sombre #030B10, aucune voix ; l'iris vert-bleu l'ouvre depuis le bouton « Abonné ✓ ».")
s = s.replace("**COUPES** (quota narrative : 0 à 4) : 0 coupe franche ; les 7 coutures sont des défilements du fil.", "**COUPES** (quota narrative : 0 à 4) : 0 coupe franche ; 7 coutures sont des défilements du fil et la huitième est l'iris vert-bleu (38.63 s).")
s = s.replace("notification 34.70 · clic 36.26 · pas de musique générée (CC0 fournie par James).", "notification 34.70 · clic 36.26 · pings 36.5 à 38.2 · riser 37.9 à 38.6 · impact grave 38.68 · logo : whoosh 39.0, ping 39.9, pop 41.0, shimmer 41.9, pop 42.7 · pas de musique générée (CC0 fournie par James) · aucune voix après 36.64.")
p.write_text(s)
print('ok')
