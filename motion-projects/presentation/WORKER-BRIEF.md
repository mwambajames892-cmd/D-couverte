# Consigne commune aux sous-agents (une séquence chacun) : film « James Framotion », 1080 × 1920, 30 i/s

Tu construis UNE séquence d'un film de motion design en HTML + GSAP (HyperFrames). Tu ne vois pas la conversation :
ces fichiers sont ton monde. Chemins absolus, dossier du projet : `/root/motion-design-claude-code/presentation` (appelé PROJECT_DIR).

## À lire, dans cet ordre
1. `PROJECT_DIR/.hyperframes/frame-packets/_role.md` : le contrat du worker (sortie = un seul fragment `<template>…</template>`, auto-contrôles).
2. `PROJECT_DIR/.hyperframes/frame-packets/<frame_id>.md` : ton paquet (bloc du storyboard, blueprint, recettes). Les lignes `Scene` SONT le plan de montage.
3. `PROJECT_DIR/frame.md` : le style (couleurs, polices, composants, règles négatives).
4. **La séquence pilote validée** `PROJECT_DIR/compositions/frames/01-hook.html` : COPIE sa structure et son kit (voir plus bas). Le client l'a validée.
5. Les images de style validées `PROJECT_DIR/styleframes/png/B1.png` … `B9.png` (tu peux les ouvrir avec Read) et leurs sources `PROJECT_DIR/styleframes/B*.html` : ce sont les compositions cibles de chaque séquence (B2, B3 = séquence 2 ; B4, B5 = 3 ; B6 = 4 ; B7 = 5 ; B8 = 6 ; B9 = 8). La séquence 7 n'a pas d'image : fais-la dans le même langage.

## Écarts avec le contrat générique (ils l'emportent)
- **Canevas portrait 1080 × 1920**, `data-width="1080" data-height="1920"`, un seul monde clair (papier `#F1EEE7`). Aucun orange nulle part : l'accent est le vert-bleu `#0C7F8F` (light `#27B2C4`, deep `#0B5560`, glow `#9FDDE5`).
- **GSAP en local, jamais depuis un CDN** (le réseau est fermé) : `<script src="assets/vendor/gsap-3.14.2.min.js"></script>`.
- **Polices locales** par `@font-face` (comme le pilote) : Inter 500/700/800 (`assets/fonts/Inter-*.otf`), JetBrains Mono 700 (`assets/fonts/JetBrainsMono-Bold.ttf`). Rien d'autre.
- **Les sous-titres existent** (les « captions » génériques sont désactivées, la phrase de la voix EST un sous-titre) : bas centre, haut du bloc à `y = 1420`, 64 px, Inter 800, mot par mot sur les temps `Word cues` (copie le kit `.h1-sw`, `.h1-ink`, `.h1-inkbg` du pilote), un seul mot-clé par phrase dans la boîte vert-bleu (texte blanc dedans), trait vert-bleu seulement là où le storyboard écrit `[trait : …]`. **La bande y 1380 à 1560 ne contient RIEN d'autre que le sous-titre.** Aucun élément de décor dans cette bande à l'instant où un sous-titre y est affiché.
- **La règle de temps du haut** (y 56 à 200) est dans chaque séquence : copie le bloc `#h1-header` du pilote (rail, graduations, tête de lecture, puce « 00:SS ») et recalcule : la tête de lecture avance en LINÉAIRE de `x_début` à `x_fin` pendant ta séquence ; remplissage `scaleX` de `(x_début−70)/940` à `(x_fin−70)/940` ; la puce de temps change de valeur à chaque seconde du FILM (`00:SS`, secondes entières du film). Formule : `x(t) = 70 + 940 × t / 36.68` (t = temps du film, plafonné à 36.68 → x 1010). Valeurs : séq 2 : 172 → 316 (début 3.98 s) ; séq 3 : 316 → 433 (début 9.58) ; séq 4 : 433 → 566 (début 14.16) ; séq 5 : 566 → 657 (début 19.36) ; séq 6 : 657 → 807 (début 22.90) ; séq 7 : 807 → 892 (début 28.76) ; séq 8 : 892 → 1010 sur ses 4.62 premières secondes puis immobile (début 32.06). La règle est un calque au-dessus du monde (z-index 3) ; le monde défile dessous.
- **Photos de James : toujours petites et encadrées** (posts, mini cartes, avatar rond, panneau), jamais en plein écran. Fichiers autorisés (rien d'autre, ne fabrique aucune URL) :
  `assets/img/fx/createur.jpg` (créateur qui se filme, 900×506), `cinema.jpg` (montage « CINEMA », 900×450), `cadreur.jpg` (cadreur caméra, lumière bleue, 700×466), `pc.jpg` (poste de montage sombre, 900×676), `timeline.jpg` (gros plan d'une timeline colorée, 700×408), `grading.jpg` (avant/après d'étalonnage « COLOR GRADING », 900×506), `premiere.jpg` (capture de Premiere Pro, 900×826), `portrait.jpg` (James, veste en jean, 720×844), `portail.jpg` (James en chemise wax devant un portail, 640×920) ;
  logos d'outils : `assets/logos/premiere.png` (carré bleu nuit, 192 px), `assets/logos/capcut.png` (noir sur blanc, 512 px), `assets/logos/davinci.jpg` (carré arrondi coloré, 447 px).
- Les chemins d'images/polices/scripts sont relatifs à la RACINE du projet (`assets/...`), comme dans le pilote.
- **Les coutures** : chaque séquence est un `cut` ; ta première image est EXACTEMENT `handoff_in`, ta dernière EXACTEMENT `handoff_out` (mêmes positions, flous, échelle, objets, tête de lecture). Aucun objet ne naît ni ne meurt dans les 2 images autour d'une couture. Ne fais PAS de sortie en fondu : la sortie est le défilement écrit dans les `Scene` (c'est une animation d'objets, pas un fondu de la séquence).
- Aucune orange, aucun emoji hors celui de la notification (le ❤️ et le 😍 du texte « Hey 😍 tu fais quoi ce soir ? » sont écrits dans le storyboard).

## Le kit du pilote à reprendre (ne le réinvente pas)
- Structure : `<template>` → `<style>` → `<div id="root" data-composition-id="<frame_id>" data-width="1080" data-height="1920" data-duration="<D>">` → calques `class="clip"` pleine durée (sol, monde, règle, sous-titres, vignette, grain) avec `data-start="0" data-duration="<D>" data-track-index`, puis le `<script>` GSAP. Style du `#root` par son id, jamais par une classe ; sol plein cadre sur un calque `clip`, pas sur `#root`.
- Un seul `gsap.timeline({paused:true})`, enregistrée à `window.__timelines["<frame_id>"]`, avec `tl.set({}, {}, DUR)` à la fin pour fixer la durée. Aides du pilote : `ft` (fromTo avec rendu immédiat à t=0) et `fl` (fromTo avec `immediateRender:false` pour tout ce qui commence après t=0).
- Tout élément absent à t=0 démarre avec `opacity:0` en CSS ; ne tween que x, y, scale, rotation, opacity, filter, clip-path (circle/ellipse/inset) ; jamais top/left/width/height/letterSpacing ; jamais `backdrop-filter` ; jamais `style.visibility="visible"` (utilise `inherit`) ; pas de `repeat:-1`, pas d'animation CSS, pas de `Math.random`.
- Éléments du pilote : `.h1-post` (post blanc 900 u, en-tête, média encadré, icônes, 2 barres), `.h1-chart`, la notification (cf. `styleframes/B2.html`), la règle de temps, la dérive linéaire du monde (+30 u/s vers le haut), les sous-titres mot par mot, la boîte vert-bleu, le trait.
- Préfixe TOUS tes ids et classes par celui de ta séquence (`p2-`, `p3-`, …) : tout est assemblé dans une seule page.
- Décor purement graphique = formes SVG (pas du texte transparent ni contouré : le contrôle refuse un texte sans remplissage visible). Les textes doivent rester dans le cadre et contrastés (≥ 3:1). Ce qui sort volontairement du cadre pendant une animation : mets `data-layout-allow-overflow` sur l'élément.
- Écris une première version COMPLÈTE de ton fichier très tôt (toutes les scènes ébauchées, timeline enregistrée), puis affine : une coupure de session ne doit pas laisser un demi-fichier.

## Interdits
Lancer une commande `npx hyperframes`, éditer `STORYBOARD.md`, `frame.md`, `index.html`, `assemble.sh` ou le fichier d'une autre séquence, ajouter un `<audio>`, charger une police ou un script depuis le réseau, inventer un texte visible que les lignes Scene ne citent pas, mettre un `<template id>` interne hors de la racine, utiliser des rebonds (`back.out`, `elastic`).

## Ta dernière action
Écrire `PROJECT_DIR/compositions/frames/<frame_id>.html` (un seul `<template>…</template>`, premiers octets `<template`, derniers `</template>`). Réponds ensuite en trois lignes : le fichier, ce qui est fait, ce qui est incertain.
