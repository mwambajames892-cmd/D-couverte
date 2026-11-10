---
version: 2
name: "James Framotion : film de présentation (9:16)"
description: >
  Frame spec du film de présentation de James Framotion, monteur vidéo (Kinshasa). Direction retenue : « Le feed »
  mêlée à « La timeline ». Le monde est un fil de réseau social vertical vu de l'intérieur ; la règle de temps d'un
  logiciel de montage court en haut du cadre et sa tête de lecture avance avec la voix. Un seul monde clair, une seule
  couleur d'accent, le vert-bleu de la marque (aucun orange). La phrase de la voix est un sous-titre bas-centre, mot par mot.
unit: 1080×1920
principle: lisible sans le son · une seule chose à regarder · une couleur d'accent, un mécanisme de mise en valeur · la voix déclenche chaque apparition · les photos de James sont toujours petites et encadrées, jamais en plein écran

colors:
  paper: "#F1EEE7"             # sol du film (monde clair unique)
  paper-2: "#E4DFD3"
  card: "#FFFFFF"              # cartes et posts
  ink: "#0B2229"               # texte, encre vert-bleu très sombre
  ink-soft: "#243F46"
  ink-mute: "#78898D"
  hairline: "#E8E4DA"
  track: "#D9E4E4"             # rail de la règle de temps
  accent: "#0C7F8F"            # LE vert-bleu de la marque (mot clé, trait, tête de lecture, Ø)
  accent-light: "#27B2C4"
  accent-deep: "#0B5560"
  accent-glow: "#9FDDE5"
  night: "#0B2229"             # notifications (carte sombre), même encre

fonts:
  Inter: { files: ["assets/fonts/Inter-Medium.otf (500)", "assets/fonts/Inter-SemiBold.otf (600)", "assets/fonts/Inter-Bold.otf (700)", "assets/fonts/Inter-ExtraBold.otf (800)"] }
  JetBrains Mono: { files: ["assets/fonts/JetBrainsMono-Bold.ttf (700)", "assets/fonts/JetBrainsMono-ExtraBold.ttf (800)"] }

typography:
  subtitle: { fontFamily: "Inter", px: 64, weight: 800, lineHeight: 77, tracking: "-0.01em", note: "la phrase de la voix en BAS CENTRE, haut du bloc à y 1420 (bande y 1380 à 1560 qui ne porte rien d'autre), 52 caractères au plus par morceau, un morceau remplace le précédent, mot par mot sur ses temps ; encre sur le papier ; jamais en haut" }
  type: { fontFamily: "Inter", px: 84, weight: 800, lineHeight: 1.1, tracking: "-0.02em", note: "moments typographiques uniquement (nommés au storyboard), centrés, 84 px au plus" }
  ui: { fontFamily: "Inter", px: 34, weight: 800, lineHeight: 1.2 }
  ui-small: { fontFamily: "Inter", px: 26, weight: 500, lineHeight: 1.2 }
  mono: { fontFamily: "JetBrains Mono", px: 24, weight: 700, tracking: "0.08em", note: "temps de la règle, puces, étiquettes" }
  wordmark-top: { fontFamily: "Inter", px: 38, weight: 700, tracking: "0.62em", note: "JAMES, au-dessus du mot-symbole" }
  wordmark: { fontFamily: "JetBrains Mono", px: 128, weight: 800, note: "FRAMØTION en points (trame de points d'encre), le Ø barré d'une barre vert-bleu inclinée à 28°" }

components:
  ground: "papier uni #F1EEE7 avec un halo radial blanc cassé (#FBF9F4) derrière le sujet et un grain de 14 % (multiply). Peint sur un calque class=\"clip\" de toute la durée du plan, jamais sur #root."
  timeline-header: "la règle de temps en haut (y 56 à 200) : rail #D9E4E4 de x 70 à 1010, une graduation par seconde (une grande toutes les 5 s avec son temps en mono), remplissage vert-bleu qui suit la tête de lecture, tête de lecture = trait vert-bleu de 4 px avec triangle, puce de temps « 00:SS » au-dessus. x(t) = 70 + 940 × t / 36.68. Elle avance en continu (linéaire) pendant tout le film."
  post: "carte blanche 900 u de large, rayon 44, ombre douce, en-tête (avatar rond à anneau vert-bleu + nom + « à l'instant »), média encadré (rayon 28, 560 u de haut), rangée d'icônes (cœur, bulle, envoi) et 2 barres grises. C'est le cadre de toutes les photos de James."
  mini: "petite carte encadrée (rayon 26, liseré blanc 6 px, ombre) pour une photo ou une vignette."
  notification: "carte sombre #0B2229, 930 × 200, rayon 44, avatar rond dégradé vert-bleu avec un cœur, « Crush » + « à l'instant », message « Hey 😍 tu fais quoi ce soir ? », point vert-bleu clair à droite."
  word-by-word: "chaque mot du sous-titre apparaît SUR son temps de voix : fromTo {opacity:0, y:10, filter:blur(6px)} → {opacity:1, y:0, blur(0)} en 0.14 s, immediateRender:false. Jamais la phrase d'un bloc. Avant une couture, le sous-titre part : opacité 1 → 0 et flou 0 → 6 px en 0.14 s."
  key-word-box: "UN seul par phrase : petit rectangle vert-bleu #0C7F8F (rayon 12 px), qui déborde le mot de 16 px de chaque côté, le mot devient blanc dedans. Il se trace de gauche à droite (scaleX 0 → 1, 0.16 s power3.out), 0 à 2 images avant le mot. Jamais un rectangle noir."
  peak-stroke: "trait vert-bleu de 9 px, extrémités rondes, légèrement incliné (−1.4°), sous LE mot clé seulement, qui se dessine de gauche à droite (scaleX 0 → 1, 0.3 à 0.5 s power2.out). 3 ou 4 fois dans le film."
  logo-lockup: "JAMES (Inter 700, espacé) sur FRAMØTION en points d'encre, barre du Ø vert-bleu avec lueur, puis @jamesframotion en mono ink-mute."
  photos: "les photos de James et ses montages (assets/img/...) ne sont JAMAIS en plein écran : toujours dans un post, une mini carte, un cercle (avatar) ou un panneau, à l'échelle 0.2 à 0.65 du cadre."

negative:
  - "Aucune couleur orange nulle part dans l'interface dessinée. Une seule teinte d'accent : le vert-bleu #0C7F8F (et ses variantes light, deep, glow). Le cœur rouge de l'emoji de la notification est la seule exception."
  - "Aucune photo en plein écran. Aucun logo de marque tierce redessiné de mémoire (les noms Premiere Pro, CapCut, DaVinci restent des puces de texte tant que James n'a pas fourni leurs logos)."
  - "Rien d'autre que le sous-titre dans la bande y 1380 à 1560 ; jamais de sous-titre en haut ; la tête de lecture et sa règle s'arrêtent à y 200."
  - "Une seule chose à regarder à la fois ; mises en page côte à côte aux marges égales ; aucune ligne du décor ne traverse une phrase."
  - "Pas de va-et-vient de caméra, pas de rebond ni d'élasticité (pas de back.out), pas de respiration en boucle, pas de repeat:-1."
  - "Aucun texte visible qui ne figure pas dans les lignes Scene d'une séquence (les étiquettes de composants ci-dessus sont permises)."
  - "Ne jamais animer letterSpacing."
---

# James Framotion : frame spec

Le film a un seul monde : **le fil** (clair), qui s'achève sur un **iris vert-bleu** ouvrant le logo animé de James sur fond sombre #030B10 (séquence 9, vidéo fournie, aucune voix). Le spectateur est dans un réseau social vertical, en haut défile la **règle de temps**
d'un logiciel de montage, et la caméra descend de post en post. La douleur est celle de la voix : une vidéo à 92 % et un
message qui tombe dessus. Le **pivot** (« qu'est-ce qu'elles ont de plus ? ») montre l'avant/après d'étalonnage de James.
La solution : son profil `@jamesframotion`, ses outils posés sur une timeline, la grille de ses services, puis la carte de fin
(message « Écris-moi… », bouton « S'abonner », réseaux).

## Géométrie du monde (1080 × 1920, unités = pixels)

- Cadre : 1080 × 1920. Colonne du fil : x centre 540, largeur 900 (marges égales de 90).
- Règle de temps : y 56 à 200 (puce de temps y 56 à 100, rail y 176 à 184, graduations y 150 à 176).
- Zone de contenu : y 230 à 1360. Bande de sous-titre : y 1380 à 1560 (réservée). Zone basse : y 1560 à 1920 (rien d'important : interface des plateformes ; un post flou « suivant » peut y dépasser).
- Défilement du fil : un seul vecteur, vers le haut ; un geste de caméra = un défilement de 800 à 1800 u en 0.12 à 0.4 s expo.out, flou vertical 8 à 14 px.
- Stations du fil : post « @createur » (sommet y 270), post « @video.en.cours » (sommet y 330), profil de James (avatar centre x 540, y 470), panneau de montage (sommet y 260), loupe (centre x 610, y 1040), grille des services (sommet y 270), carte de fin (avatar centre y 350).

## Mécanismes signature

- « Le défilement » : le fil monte d'un cran avec flou vertical à chaque nouvelle idée (4 à 8 fois).
- « La tête de lecture » : avance en continu sur la règle ; elle s'arrête une fois, sur « Moi, c'est James » (12.26 s), l'instant où le nom arrive.
- Rime : la notification « Crush » du début (4.9 s) rejoue à la fin dans la carte « Écris-moi… » (35 s).

## Références (images de style validées)

`styleframes/png/B1.png` à `B9.png` (1.6 · 4.9 · 6.9 · 9.6 · 12.3 · 15.6 · 20 · 25.2 · 34.7 s). Chaque séquence du storyboard part d'une de ces images.
