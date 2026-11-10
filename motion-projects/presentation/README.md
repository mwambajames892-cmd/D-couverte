# Projet « présentation » (film de présentation James Framotion, 9:16, ≈ 37 s)

Dépôt public : **aucune photo, voix ni musique n'est ici**. Elles sont dans le Google Drive de James,
dossier `Motion Design/premier-film/` :
`1-voix` (voix ElevenLabs), `2-captures-ecran` (photos, montages, images d'ambiance),
`3-musique`, `4-logo-et-marque` (logo animé Framotion).

Contenu : `SCRIPT.md` (texte et minutage mot à mot), `DIRECTIONS.md` (directions et choix : B « Le feed » mêlée à A
« La timeline », accent vert-bleu `#0C7F8F`), `styleframes/B1..B9.html` (les 9 images de style), `tools/`
(générateurs et rendu des images).

Pour reprendre : le hook de session copie ce dossier dans `~/motion-design-claude-code/presentation`, puis les
fichiers du Drive sont rapatriés dans `assets/` (voix, images, logo, musique).

## État d'avancement

- Étapes 1 à 3 (script, voix, storyboard) : faites et validées.
- Étape 4 (animation) : les 9 séquences sont écrites (`compositions/frames/01-hook.html` à `09-logo.html`) ; la 1 (pilote) et la 9 (logo animé,
  vidéo posée à la racine par `assemble.sh`) à la main, les séquences 2 à 8 par 7 sous-agents (`WORKER-BRIEF.md`), puis corrigées. Le film muet
  de 44,68 s se rend (36,68 s de voix + 2 s de tenue + 6 s de logo). Reste : étape 5 (musique, bruitages, mixage de la voix), contrôles, rendu final.
- Fichiers à rapatrier du Drive avant de rendre : voix (`assets/audio/voix.mp3`), images (`assets/img/fx/`, copies recadrées des photos), logos
  (`assets/logos/`), vidéo du logo (`assets/video/james-framotion-reveal-9x16.mp4`, puis `-gop30.mp4` : `ffmpeg -r 30 -g 30 -keyint_min 30`).
- Outils : `tools/story.py` (+ `patch_story.py`) génère `STORYBOARD.md` ; `tools/patch_assemble*.py` rendent `assemble.sh` compatible
  (GSAP local `assets/vendor/gsap-3.14.2.min.js`, vidéo du logo à la racine, assembleur récent) ; `tools/frame01.py` génère la séquence 1.
