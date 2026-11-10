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

- Étape 1 (script), 2 (voix), 3 (directions, fiche de style `frame.md`, storyboard `STORYBOARD.md` de 8 séquences, contrôle
  `STORYBOARD-CHECK.md`) : faites et validées.
- Étape 4 (animation) : séquence pilote `compositions/frames/01-hook.html` construite ; les séquences 2 à 8 restent à faire.
- Outils : `tools/story.py` régénère `STORYBOARD.md` ; `tools/frame01.py` génère la séquence 1 ; `tools/patch_assemble.py`
  fait lire GSAP depuis `assets/vendor/gsap-3.14.2.min.js` (réseau fermé : `npm pack gsap@3.14.2`, fichier `package/dist/gsap.min.js`).
- Polices : Inter (Medium, SemiBold, Bold, ExtraBold) et JetBrains Mono (Bold, ExtraBold), copiées depuis `/usr/share/fonts` dans `assets/fonts/`.
