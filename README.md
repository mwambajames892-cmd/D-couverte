# D-couverte
## Atelier motion design (sessions Claude Code cloud)

Au démarrage de chaque session cloud, `.claude/hooks/session-start.sh` installe automatiquement
l'atelier [motion-design-claude-code](https://github.com/cblain100-prog/motion-design-claude-code)
dans `~/motion-design-claude-code` : clone, `.env` vide, `npm ci` (HyperFrames 0.8.82),
openai-whisper et playwright, télémétrie HyperFrames désactivée, navigateur de rendu.
Il ne réinstalle que ce qui manque.
