import pathlib
p = pathlib.Path.home()/'motion-design-claude-code/presentation/assemble.sh'
s = p.read_text()
old = '''anchor = re.search(r"(?m)^[ \\t]*tl\\.to\\(\\{\\}, \\{ duration: [0-9.]+ \\}, 0\\);", s)
if not anchor:
    raise SystemExit("assemble: full-span anchor tl.to({}, { duration: N }, 0); not found in index.html")
s = s[:anchor.start()] + tl + s[anchor.start():]
'''
new = '''anchor = re.search(r"(?m)^[ \\t]*tl\\.to\\(\\{\\}, \\{ duration: [0-9.]+ \\}, 0\\);", s)
if anchor:
    s = s[:anchor.start()] + tl + s[anchor.start():]
else:
    # assembleur récent : la timeline principale est créée vide, sans variable `tl` ni ancre de durée
    m = re.search(r'window\\.__timelines\\["main"\\] = gsap\\.timeline\\(\\{ paused: true \\}\\);', s)
    if not m:
        raise SystemExit("assemble: main timeline registration not found in index.html")
    s = (s[:m.start()] + "var tl = gsap.timeline({ paused: true });\\n" + tl
         + f"        tl.to({{}}, {{ duration: {total} }}, 0);\\n        window.__timelines[\\"main\\"] = tl;" + s[m.end():])
'''
assert old in s
s = s.replace(old, new, 1)
p.write_text(s); print('ok')
