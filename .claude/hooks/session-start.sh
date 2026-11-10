#!/bin/bash
# Installe l'atelier motion-design-claude-code (HyperFrames 0.8.82 + skills HeyGen audités)
# au démarrage de chaque session Claude Code cloud. Idempotent : ne réinstalle que ce qui manque.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

MD="$HOME/motion-design-claude-code"
HOOK="${CLAUDE_PROJECT_DIR:-$(pwd)}/.claude/hooks/session-start.sh"
export HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_UPDATE_CHECK=1

# 1. Le dépôt de l'atelier
if [ ! -d "$MD/.git" ]; then
  git clone --quiet https://github.com/cblain100-prog/motion-design-claude-code "$MD"
fi
cd "$MD"

# 2. Le .env vide voulu (ne jamais le supprimer ni y écrire de clé)
test -f .env || cp .env.example .env

# 2b. Les projets de film enregistrés dans ce dépôt (motion-projects/<nom>) : copiés dans l'atelier s'ils manquent
PROJ="${CLAUDE_PROJECT_DIR:-$OLDPWD}/motion-projects"
if [ -d "$PROJ" ]; then
  for p in "$PROJ"/*/; do
    n="$(basename "$p")"
    [ -d "$MD/$n" ] || cp -r "$p" "$MD/$n"
  done
fi

# 3. HyperFrames figé par package-lock.json
hashes=node_modules/.session-start.sha256
if ! sha256sum --check --status "$hashes" 2>/dev/null; then
  rm -f "$hashes"
  npm ci --no-audit --no-fund --loglevel=error
  npx hyperframes telemetry disable >/dev/null
  sha256sum package-lock.json "$HOOK" > "$hashes"
fi

# 4. Paquets Python (whisper pour le calage des mots, playwright pour les styleframes)
pyhashes="$(python3 -I -c 'import sysconfig; print(sysconfig.get_path("purelib"))')/.session-start-motion.sha256"
if ! sha256sum --check --status "$pyhashes" 2>/dev/null || ! python3 -I -c "import whisper, playwright" 2>/dev/null; then
  rm -f "$pyhashes"
  python3 -m pip install -q --root-user-action=ignore openai-whisper playwright
  sha256sum "$HOOK" > "$pyhashes"
fi

# 5. Navigateur de rendu HyperFrames (rapide s'il est déjà en cache)
if ! compgen -G "$HOME/.cache/hyperframes/chrome/chrome-headless-shell/*/*/chrome-headless-shell" >/dev/null; then
  npx hyperframes browser ensure >/dev/null
fi

# 6. Préfixe anti-télémétrie pour toutes les commandes npx hyperframes de la session
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo 'export HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_UPDATE_CHECK=1' >> "$CLAUDE_ENV_FILE"
fi

echo "Atelier motion design prêt : $MD"
