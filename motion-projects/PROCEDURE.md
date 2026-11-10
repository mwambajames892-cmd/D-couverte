# Procédure motion design de James : de la voix et des photos au film MP4

Écrite à la fin du premier film (« présentation James Framotion », 44,7 s, 9:16, 9 séquences, 3 jours de travail réduits à quelques heures).
Elle sert à refaire un film **différent** (autre script, autre durée, autre contexte) en ne demandant à James presque que les fichiers.
Le film de référence vit dans `motion-projects/presentation/` (texte et code seulement). Les modèles réutilisables sont dans `motion-projects/_modele/`.

## 0. Contexte de James (à ne pas redemander)

- Monteur vidéo à Kinshasa (RDC), supporter du Barça, passionné de cinéma. Outils : Premiere Pro, CapCut, DaVinci (étalonnage), After Effects.
  Quand il parle de **montage**, penser Premiere Pro ; de **motion design**, penser After Effects.
- **Il n'a pas de PC** : tout se fait depuis son téléphone Android, par la conversation, le Google Drive et GitHub.
- **Forfait mobile limité** (environ 1 Go) : envoyer des aperçus légers (planches JPEG de 3 images, vidéos de 2 à 3 Mo en 720p),
  le fichier final en HD (pas de 4K sauf demande explicite, il a choisi la HD pour économiser), jamais de fichier de plusieurs centaines de Mo.
- Il valide à l'œil sur son téléphone : donner des **temps précis** (« à 25 s ») pour les corrections.
- Langue : français. Voix des films : ElevenLabs (il la génère lui-même dans l'application web, jamais de clé API).

## 1. Style de travail voulu par James, et limites

James veut déposer ses fichiers et donner le sujet, puis recevoir le film : **de bout en bout, sans être sollicité à chaque étape**. Ce qu'il attend, pour chaque film :

- installer l'atelier et ses dépendances (le hook le fait), lire ses fichiers du Drive, créer le dossier du film, déposer les rendus à valider ;
- construire les séquences avec **un sous-agent par séquence, en parallèle** (méthode prévue ; il l'a demandée pour le premier film) ;
- lui envoyer les jalons (planches d'images de style, pilote, aperçus du son) **pour information**, sans bloquer dessus ;
- livrer le film final en HD (envoi dans la conversation + version de moins de 10 Mo sur le Drive) ;
- enregistrer le projet dans ce dépôt (texte et code seulement : le dépôt est public).

**Ce que ce fichier ne fait pas : il ne donne aucune permission.** Les droits (écrire sur le Drive, pousser sur GitHub, lancer des sous-agents) viennent du message que
James envoie au début de chaque film : il y a un modèle prêt à coller dans `motion-projects/MESSAGE-DE-DEMARRAGE.md`. Sans ce message, demander une seule fois, de façon
groupée, ce qui est nécessaire, puis enchaîner.

S'arrêter et demander seulement pour : un fichier ou une information réellement manquant (voix, format, appel à l'action, nom exact de la marque), un choix de goût sans
défaut raisonnable (la musique), ou une action destructrice. Valeurs par défaut raisonnables : format 9:16, une direction artistique recommandée, rendu HD, une seule version du
mixage sauf s'il y a plusieurs musiques.

Limites : pas de clé API ni de secret ; pas de service payant (voix, images, musique générées) sans demande ; pas de `push --force`, pas de suppression sur le Drive ou de
branches, pas de fusion de la demande de fusion à sa place, pas de publication de ses vidéos ; respecter `AGENTS.md` de l'atelier (`hyperframes feedback|publish|upgrade|skills update`
et `skills add` interdits). Les invites de sécurité de la plateforme (création d'environnement) ne s'approuvent pas depuis son téléphone : le hook du dépôt fait l'installation.

## 2. Ce que James dépose, et où

Dossier Drive : `Motion Design/<nom-du-film>/` avec
`1-voix` (voix ElevenLabs en .mp3 ou .wav), `2-captures-ecran` (photos, montages, images d'ambiance, captures, jpg/png/mp4),
`3-musique` (morceaux), `4-logo-et-marque` (logos, logo animé, couleurs), `5-rendus-a-valider` (c'est moi qui y dépose).
Informations utiles (les demander une seule fois, regroupées, et seulement ce qui manque) : sujet et public, format (9:16 ou 16:9), appel à l'action et lien
ou pseudo, nom exact de la marque (**faire confirmer l'orthographe : whisper entend mal les marques** — « Framotion » a été transcrit « from Ocean »),
couleur d'accent, source et licence de la musique, durée voulue de la tenue finale, logo animé de fin (durée réelle à vérifier avec ffprobe).

## 3. La méthode en étapes (commandes de la machine cloud)

Atelier : `~/motion-design-claude-code` (HyperFrames 0.8.82 figé, compétences HeyGen auditées). Le hook de `.claude/hooks/session-start.sh` l'installe à
chaque session et copie les projets de `motion-projects/<nom>/` dedans. Toutes les commandes `npx hyperframes` se lancent depuis l'atelier, avec
`HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_UPDATE_CHECK=1`.
Lire `AGENTS.md` et `.claude/skills/motion-design/SKILL.md` de l'atelier une fois par session.

1. **Dossier de projet** : `bash .claude/skills/motion-design/scripts/new-project.sh <nom> --fonts` (les polices ne se téléchargent pas : copier Inter et
   JetBrains Mono depuis `/usr/share/fonts` dans `<nom>/assets/fonts/`). Mettre à jour `meta.json` et `hyperframes.json` (largeur et hauteur : 1080 × 1920 en 9:16).
2. **Récupérer les fichiers du Drive** : `search_files` avec `parentId = '<id du dossier>'`, puis `download_file_content`. Le résultat de plus de ~37 Ko
   est enregistré dans un fichier JSON du dossier `tool-results` : `jq -r .content <fichier> | base64 -d > <destination>`. **Un fichier de moins de ~37 Ko
   revient dans la conversation et ne peut pas être enregistré** : demander à James de les regrouper dans un `.zip` (le zip est enregistré, l'extraire avec
   `python3 -I` et `zipfile`, après avoir refusé tout chemin absolu ou contenant `..`, dans un dossier vide). Regarder les images (`Read`) et les vidéos
   (planche ffmpeg `fps=1,tile`) pour savoir ce qu'on a ; les noms de fichiers mentent (captures d'écran de galerie, photos d'écran d'ordinateur).
3. **Voix** : `ffprobe`, mesure `ebur128` (la voix ElevenLabs sort très basse, vers -29 LUFS : +12,6 dB au mixage), `python3 .claude/skills/motion-design/scripts/mots.py
   <voix.wav> --model small --lang fr` (le modèle `small` est en cache ; `medium` demande un téléchargement). Convertir d'abord le .mp3 en wav 16 kHz mono.
   Sortie : `voix-mots.json` (mots avec temps) et la liste des silences de plus de 0,4 s, qui deviennent des plans. **Corriger les mots mal transcrits**
   (marques, termes de montage) avec James ou son script.
4. **Script** : si James fournit la voix, le script existe déjà (le transcrire dans `SCRIPT.md`). Sinon écrire deux versions (6 parties : accroche, gag muet,
   diagnostic, pivot, solution, marque + appel à l'action), 170 à 180 mots par minute.
5. **Directions et images de style** : trois directions de mise en scène vraiment différentes, neuf images (3 moments par direction) dessinées en HTML
   1080 × 1920 et rendues en PNG avec `motion-projects/_modele/tools/render.py` (il utilise `/opt/pw-browsers/chromium` : `playwright install` est bloqué par le réseau).
   Recadrer les photos (jamais en plein écran : petites et encadrées), puis envoyer **3 planches JPEG de 3 images** à James avec `SendUserFile` (un seul
   fichier par direction, ~250 Ko). Recommander une direction. S'il a déjà tout dit (direction, couleurs), ne pas refaire ce choix.
6. **Fiche de style `frame.md`**, **storyboard `STORYBOARD.md`** (générer avec un script comme `tools/story.py` : temps des mots → temps locaux,
   durées, passages de relais `handoff_out` = `handoff_in` vérifiés mot pour mot par script), **`STORYBOARD-CHECK.md`** (grille de 15 points).
   Puis `node .claude/skills/product-launch-video/scripts/frame-packets.mjs --project <nom> --storyboard <nom>/STORYBOARD.md`.
   Vérifier par script : somme des durées = durée du film, bornes des plans sans trou, coutures identiques.
7. **Séquence pilote** : la 1 à la main, avec GSAP **local** (voir pièges). `bash assemble.sh`, `npx hyperframes check`, `npx hyperframes snapshot --at ...`,
   rendu brouillon `npx hyperframes render --quality draft`. Envoyer le MP4 brouillon (1 Mo) et une planche à James comme jalon.
8. **Sous-agents** : un par séquence restante (`Agent`, type `general-purpose`, `run_in_background: true`), tous lancés dans le même message. Chaque prompt =
   le contexte de dispatch (frame_id, paquet, durée, début dans le film, positions de la règle de temps, image de style cible, lignes propres) + la
   consigne commune `WORKER-BRIEF.md` (modèle dans `_modele/`). Les agents **n'ont pas le droit de lancer `npx hyperframes`** : ils écrivent des fichiers que
   personne n'a vus s'afficher ; **contrôler soi-même** ensuite. Attendre leurs notifications sans interroger.
9. **Assemblage et relecture** : `bash assemble.sh` (réglages en tête de fichier : première et dernière séquence, durée totale, vidéo du logo, iris), puis
   `npx hyperframes check` (lint, exécution, mise en page, contraste), rendu brouillon complet, **planches de 6 images** extraites du MP4 (`ffmpeg -ss T -i ... | hstack`)
   aux coutures et aux moments clés ; corriger ce qui cloche (éléments encore visibles avant leur entrée, éléments sortants qui restent dans le cadre).
10. **Son** : `tools/mix.py` (voix à +12,6 dB, musique démarrée de façon que son « drop » tombe sur le moment fort, `sidechaincompress` sous la voix, montée à la fin
    si une séquence finale n'a pas de voix, bruitages du dossier `.claude/skills/media-use/audio/assets/sfx/` calés sur les gestes d'après les lignes `SON` du
    storyboard, `loudnorm -16 LUFS`, limiteur). Fabriquer A, B, C seulement s'il y a un vrai choix ; sinon une version. Aperçus 720p avec le son en `-c:v copy`.
    Mesurer : `ebur128=peak=true`, pic sous -1,5 dBTP.
11. **Rendu final** : `MIX=mix-X.wav bash assemble.sh` (insère l'`<audio>`), puis le rendu en **HD** (`npx hyperframes render --quality high --output renders/film.mp4`, environ
    3 min pour 45 s). **Toujours le lancer par l'outil Bash avec `run_in_background: true`, sans `nohup &` ni `sleep`** : un processus lancé en `&` est annulé à la fin
    de la commande (`render_cancelled_parent_exited`). Contrôler : `ffprobe` (flux vidéo et audio, durée), `ffmpeg -v error -i film.mp4 -f null -`, `blackdetect`,
    `freezedetect=n=-60dB:d=0.5`, `ebur128`. Voir les images à la couture.
12. **Livraison** : `SendUserFile` du MP4 HD (copié dans le dossier de travail de session, `display: attach`) ; sur le Drive : `create_file` avec `base64Content`
    de la forme `sha256:<hex>:<chemin dans le dossier de travail de session>` (limite **10 Mo** : y mettre un 720p `libx264 -crf 28`).
13. **Sauvegarde GitHub** : copier dans `motion-projects/<nom>/` le texte et le code (storyboard, frames HTML, outils, README d'avancement). **Aucun média.**
    Sur la branche de session, `git add`, `commit` avec les lignes d'attribution demandées, `git push -u origin <branche>` (pas de `--force` : repartir de
    `origin/main` quand la demande précédente est fusionnée), demande de fusion en brouillon.

## 4. Pièges connus (tous rencontrés)

- **Le réseau est fermé** : GSAP depuis le CDN échoue (`ERR_TUNNEL_CONNECTION_FAILED`, « gsap is not defined »). `npm pack gsap@3.14.2` dans un dossier de travail,
  extraire `package/dist/gsap.min.js` dans `<projet>/assets/vendor/gsap-3.14.2.min.js` et référencer ce fichier ; `assemble.sh` remplace le `<script>` du CDN dans `index.html`
  (patch dans `_modele/tools/patch_assemble.py`). Polices et images : toujours locales (`assets/...`).
- **L'assembleur récent** écrit `window.__timelines["main"] = gsap.timeline({ paused: true });` sans ancre `tl.to({}, …)` : `patch_assemble3.py`. L'anneau d'iris est
  en 1920 × 1080 par défaut : `patch_assemble2.py` le met à la taille du canevas portrait. Une vidéo (logo animé) ne peut pas être dans une séquence : la poser à la
  racine (même patch) et lui appliquer le même `clip-path` que l'iris.
- **Vidéo à images clés rares** (GOP de 6 s) : la ré-encoder `ffmpeg -r 30 -g 30 -keyint_min 30 -pix_fmt yuv420p -an` (« sparse keyframes »).
- **Cartes `.post` de 900 u** : mettre `box-sizing: border-box` (sinon elles font 968 u et se décalent).
- **Texte transparent ou contouré** (décor « ? », mot-symbole en points avec `background-clip:text`) : le contrôle `text_not_painted` le refuse ; dessiner en SVG.
- **Éléments animés par `fromTo` avec `immediateRender:false`** sont visibles tant que leur début n'est pas arrivé : leur mettre `opacity:0` au départ.
- **Un groupe qui « sort » doit sortir du cadre** (`y` supérieur à la hauteur du cadre).
- **Un sous-titre trop large** : 64 px, 52 caractères au plus ; le couper en deux morceaux ; `white-space: nowrap`.
- **Pas de fichier de moins de ~37 Ko depuis le Drive** (voir étape 2). Pas de téléchargement de plus de 10 Mo vers le Drive (étape 12).
- **`playwright install chromium` bloqué** : utiliser `/opt/pw-browsers/chromium` (`executable_path`, `args=['--no-sandbox']`).
- **Rendu 4K** : `--resolution portrait-4k` existe mais coûte 4 fois plus de temps et de poids ; les photos fournies restent à leur définition d'origine.
- **Les invites d'approbation de la plateforme** (création d'environnement) ne s'approuvent pas depuis un téléphone : passer par le hook du dépôt.
- **Les sous-agents rendent compte avec des écarts** : lire leurs « incertain » ; ils proposent parfois de corriger le pilote (le défaut `border-box` a été trouvé ainsi).
- Mesures utiles : tout le film se rend en ~3 min HD ; 9 séquences ~ 140 Ko de HTML ; 8 agents en parallèle ont tenu 2 à 9 minutes.

## 5. Ce que contient `_modele/`

`assemble.sh` (réglages 1080 × 1920, GSAP local, vidéo de logo, iris), `WORKER-BRIEF.md` (consigne commune des sous-agents, à adapter : palette, positions de la règle,
fichiers autorisés), `tools/render.py` (images de style en PNG), `tools/story.py` (générateur de `STORYBOARD.md`), `tools/b2.py` et `b2frames.py` (composants et neuf images de
style du premier film), `tools/frame01.py` (séquence pilote écrite par un script), `tools/mix.py` (mixage voix + musique + bruitages), `tools/patch_assemble*.py` (réparations de l'atelier).
Ce sont des **exemples à adapter**, pas des gabarits à remplir : le style, les mots et les temps changent à chaque film.
