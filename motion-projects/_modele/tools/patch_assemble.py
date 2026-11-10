import pathlib
p = pathlib.Path.home()/'motion-design-claude-code/presentation/assemble.sh'
s = p.read_text()
marker = "python3 - <<'EOF'\nimport os, re\n\nenv = os.environ"
assert marker in s
patch = r"""# Réseau fermé : GSAP vient du fichier local assets/vendor/ (même version 3.14.2) au lieu du CDN.
python3 - <<'EOF'
import re
p = "index.html"
s = open(p, encoding="utf-8").read()
s = re.sub(r'<script src="https://cdn\.jsdelivr\.net/npm/gsap@3\.14\.2/dist/gsap\.min\.js"[^>]*></script>',
           '<script src="assets/vendor/gsap-3.14.2.min.js"></script>', s)
open(p, "w", encoding="utf-8").write(s)
EOF

"""
if "assets/vendor/gsap" not in s:
    s = s.replace(marker, patch + marker, 1)
    p.write_text(s)
print("ok")
