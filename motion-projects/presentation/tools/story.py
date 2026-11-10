import pathlib, re
FRAMES = [
 dict(n=1, id='01-hook', title="Pourquoi les vidéos se font quitter", a=0.00, b=3.98, type='hook', bp='camera-journey', rules='depth-of-field-blur, svg-path-draw',
  voice="Pourquoi certaines vidéos te gardent jusqu'à la fin ? Et d'autres non.",
  focal="le post « @createur » (photo du créateur qui se filme, encadrée), puis la courbe de rétention vert-bleu qui tient jusqu'à la fin",
  scene="Un post « @createur » arrive très grand et flou et se pose ; une carte de courbes naît par-dessus : la courbe vert-bleu tient jusqu'au bout, la courbe grise des autres s'effondre ; le fil monte d'un cran sur « non »",
  hin="aucun (ouverture du film) ; première image = papier clair, règle de temps avec la tête de lecture à 00:00, le post « @createur » déjà posé en très grand (échelle 2,3) et flou 14 px au centre de la zone de contenu",
  hout="HS1 : fil en défilement vers le haut à −2200 u/s, flou vertical 10 px ; le post « @video.en.cours » (média « CINEMA », 900 u de large, sommet à y 700) entre par le bas, centré x 540 ; tête de lecture à 3.98 s (x 172) ; aucune notification, aucun sous-titre ; papier clair, grain 14 %",
  cues="Pourquoi@0.00 certaines@0.30 vidéos@0.70 te@1.10 gardent@1.30 jusqu'à@1.64 la@2.06 fin@2.16 Et@2.98 d'autres@3.06 non@3.26",
  scenes=[
  ("0.00 à 1.10", 1, "le post « @createur » se pose sous le flou",
   "TEXTE ÉCRAN : « Pourquoi certaines vidéos » (0.00, 0.30, 0.70) ; écart synchro.",
   "IMAGE DE DÉPART : papier clair, règle de temps vide, le post « @createur » énorme (échelle 2,3) et flou 14 px, centré.",
   "ÉTAPES : 0.00 le rail de la règle se remplit de 0 à 172 px (linéaire, toute la séquence) ; 0.04 le post « @createur » se pose (échelle 2,3 → 1, flou 14 → 0, expo.out 0.4 s) ; 0.30 le grand « ? » vert-bleu fantôme paraît derrière le post (opacité 0 → 0.2, 0.2 s) ; 0.55 les 3 icônes du post (cœur, bulle, envoi) s'allument une à une (0.12 s d'écart) ; 0.80 la puce de temps « 00:00 » passe à « 00:01 ».",
   "PISTE CAMÉRA : dérive linéaire du fil de 0 à +30 u/s vers le haut ; 0.04 à 0.44 atterrissage du post (zoom arrière expo.out).",
   "COUCHES ET PROFONDEUR : avant-plan le grand « ? » flou ; sujet le post net ; fond papier et post « suivant » flou qui dépasse en bas (y 1640) ; 3 couches.",
   "OBJET-PONT ET VECTEUR : le post « @createur » reste ; la carte de courbes naît sur son bord bas-droit.",
   "SON : whoosh court à 0.04 (le post se pose).", "IMAGE CLÉ : 0.70 : le post net, le « ? » en filigrane, la tête de lecture à 00:00."),
  ("1.10 à 2.98", 2, "la carte de courbes tient jusqu'à la fin",
   "TEXTE ÉCRAN : « te gardent [boîte : jusqu'à la fin] ? » (1.10 à 2.38) ; [trait : aucun] ; écart avance de 0.08 s.",
   "IMAGE DE DÉPART : le post net, le « ? » fantôme, la règle à 1.10 s.",
   "ÉTAPES : 1.02 la boîte vert-bleu se trace sous « jusqu'à la fin » (scaleX 0 → 1, 0.16 s) ; 1.30 la carte « courbes » (430 × 310, inclinée 4°) arrive trop grande et floue du bas-droit (échelle 1,6 → 1, flou 12 → 0, expo.out 0.35 s) ; 1.60 la courbe grise pointillée « LES AUTRES » se dessine et plonge (svg-path-draw 0.7 s) ; 1.90 la courbe vert-bleu « JUSQU'À LA FIN » se dessine, tient haut (0.5 s) ; 2.38 le point vert-bleu au bout pulse une fois (échelle 1 → 1,6 → 1, 0.3 s) ; 2.55 les 2 barres grises du post glissent (x 0 → −30).",
   "PISTE CAMÉRA : dérive +30 u/s ; 1.30 à 1.50 petit cran vers la carte (échelle 1 → 1,06, expo.out).",
   "COUCHES ET PROFONDEUR : avant-plan la carte courbes qui arrive floue ; sujet le post ; fond « ? » et post suivant flou ; 3 couches.",
   "OBJET-PONT ET VECTEUR : la courbe vert-bleu monte vers la droite : vecteur de sortie vers le haut-droite, repris par le défilement de la couture.",
   "SON : ping à 1.30 (la carte arrive), pop à 2.38 (le point).", "IMAGE CLÉ : 2.30 : les deux courbes tracées, la vert-bleu en haut, le sous-titre avec sa boîte."),
  ("2.98 à 3.98", 3, "« non » : le fil monte d'un cran",
   "TEXTE ÉCRAN : « Et d'autres non. » (2.98, 3.06, 3.26) ; [boîte : non] ; écart synchro.",
   "IMAGE DE DÉPART : le post, la carte courbes, la règle à 2.98 s.",
   "ÉTAPES : 2.98 le sous-titre précédent part (opacité 1 → 0, flou 6, 0.14 s) puis « Et d'autres non. » entre mot à mot ; 3.26 la courbe grise tombe d'un coup au plancher (0.15 s) ; 3.40 la carte courbes et le post montent et rétrécissent vers le haut (y −220, échelle 0,92, flou 6 → 12, power3.in 0.3 s) ; 3.55 le post « @video.en.cours » monte du bas en flou vertical ; 3.80 le fil prend sa vitesse (−2200 u/s).",
   "PISTE CAMÉRA : 3.40 à 3.98 défilement expo.in vers le haut, flou vertical 10 px au sommet de la couture.",
   "COUCHES ET PROFONDEUR : avant-plan le nouveau post flou ; sujet l'ancien post qui sort ; fond papier ; 2 couches.",
   "OBJET-PONT ET VECTEUR : le post « @video.en.cours » est l'objet de la séquence 2 ; vecteur de sortie : vers le haut, −2200 u/s, expo.in.",
   "SON : whoosh à 3.55 (le fil monte).", "IMAGE CLÉ : 3.70 : le fil en défilement flou, le post CINEMA qui entre par le bas.")]),
 dict(n=2, id='02-crush', title="Le crush écrit, tu ignores", a=3.98, b=9.58, type='pain_point', bp='camera-journey', rules='motion-blur-streak, depth-of-field-blur',
  voice="Tu sais, celles où ton crush t'écrit enfin, mais tu l'ignores, pour finir d'abord la vidéo.",
  focal="le post « @video.en.cours » (vidéo CINEMA à 55 % puis 92 %), puis la notification « Crush » qui tombe dessus",
  scene="La vidéo CINEMA joue dans son post ; une notification « Crush » tombe dessus ; elle est balayée à gauche (traînée) pendant que la barre de lecture atteint 92 % ; le post recule",
  hin="HS1 : fil en défilement vers le haut à −2200 u/s, flou vertical 10 px ; le post « @video.en.cours » (média « CINEMA », 900 u de large, sommet à y 700) entre par le bas, centré x 540 ; tête de lecture à 3.98 s (x 172) ; aucune notification, aucun sous-titre ; papier clair, grain 14 %",
  hout="HS2 : flou 12 px ; le post « @video.en.cours » (barre à 92 %) recule au centre, échelle 0,5, x 540, y 760 ; la notification « Crush » a quitté le cadre à gauche (traînée floue) ; papier clair, grand « ? » fantôme centré à 70 % d'opacité ; tête de lecture à 9.58 s (x 316) ; aucun sous-titre ; grain 14 %",
  cues="Tu@0.00 sais@0.14 celles@0.88 où@1.16 ton@1.28 crush@1.42 t'écrit@1.68 enfin@2.06 mais@2.94 tu@3.10 l'ignores@3.24 pour@4.02 finir@4.10 d'abord@4.40 la@4.68 vidéo@4.82",
  scenes=[
  ("0.00 à 0.88", 1, "le post CINEMA se pose, « Tu sais, »",
   "TEXTE ÉCRAN : « Tu sais, » (0.00, 0.14) ; écart synchro.",
   "IMAGE DE DÉPART : handoff_in : le post « @video.en.cours » en flou vertical, qui entre par le bas.",
   "ÉTAPES : 0.00 le post finit sa montée (flou 10 → 0, expo.out 0.3 s) ; 0.14 la barre de lecture blanche paraît dans le média (scaleX 0 → 1 en 0.2 s) ; 0.30 son remplissage vert-bleu avance de 0 à 55 % (linéaire jusqu'à 1.9 s) ; 0.60 le coup de chapeau du curseur de temps : la puce passe à « 00:04 ».",
   "PISTE CAMÉRA : dérive +30 u/s vers le haut ; 0.00 à 0.30 atterrissage du fil.",
   "COUCHES ET PROFONDEUR : avant-plan rien ; sujet le post net ; fond papier, post suivant flou en bas ; 2 couches.",
   "OBJET-PONT ET VECTEUR : la vidéo CINEMA et sa barre restent jusqu'à la séquence 3.",
   "SON : aucun (silence de 0.42 s : « sais, » → « celles »).", "IMAGE CLÉ : 0.50 : le post CINEMA net, la barre à 10 %."),
  ("0.88 à 3.24", 2, "la notification tombe sur la vidéo",
   "TEXTE ÉCRAN : « ton crush [boîte : t'écrit] enfin, » (0.88 à 2.2) ; écart avance de 0.1 s.",
   "IMAGE DE DÉPART : le post CINEMA, barre à 25 %.",
   "ÉTAPES : 0.78 la boîte se trace sous « t'écrit » ; 1.30 l'ombre de la notification paraît en haut (flou 14) ; 1.42 la notification « Crush » tombe du haut, trop grande (échelle 1,14 → 1, flou 10 → 0, expo.out 0.3 s) en recouvrant l'en-tête du post ; 1.60 le point vert-bleu clair pulse deux fois ; 2.10 la notification vibre de 6 px (3 allers-retours de 0.04 s) ; 2.80 le mot « ignores » arrive et le curseur vert-bleu « ← IGNORER » paraît sur le bord du média.",
   "PISTE CAMÉRA : dérive +30 u/s ; 1.42 à 1.70 cran vers la notification (échelle 1 → 1,05, expo.out).",
   "COUCHES ET PROFONDEUR : avant-plan la notification en chute, floue ; sujet la notification posée ; fond le post CINEMA ; 3 couches.",
   "OBJET-PONT ET VECTEUR : la notification est balayée vers la gauche dans le plan suivant : vecteur de sortie vers la gauche, expo.in.",
   "SON : notification à 1.42 (elle tombe).", "IMAGE CLÉ : 1.90 : la notification posée sur le post CINEMA, barre à 45 %."),
  ("3.24 à 4.40", 3, "« mais tu l'ignores » : balayée à gauche",
   "TEXTE ÉCRAN : « mais tu l'[boîte : ignores] » (2.94 à 3.7) + [trait : ignores] ; écart synchro.",
   "IMAGE DE DÉPART : la notification posée sur le post, barre à 60 %.",
   "ÉTAPES : 3.24 la notification glisse à gauche (x 0 → −420, flou 0 → 10, power3.in 0.22 s) en laissant 2 copies fantômes (opacité .28 et .13) ; 3.40 elle sort du cadre ; 3.50 la barre de lecture saute à 92 % (power2.out 0.5 s) ; 3.50 le trait vert-bleu se dessine sous « ignores » (scaleX 0 → 1, 0.4 s) ; 3.90 le point de la barre brille (lueur).",
   "PISTE CAMÉRA : 3.24 à 3.46 petit cran à gauche (x +40, expo.out) pour suivre la notification ; puis dérive +30 u/s.",
   "COUCHES ET PROFONDEUR : avant-plan les copies fantômes floues ; sujet le post CINEMA qui reste ; fond papier ; 3 couches.",
   "OBJET-PONT ET VECTEUR : le post CINEMA devient le « post à 92 % » du pivot.",
   "SON : whoosh court à 3.24 (balayage).", "IMAGE CLÉ : 3.50 : la notification en fuite à gauche (traînée), le trait vert-bleu sous « ignores »."),
  ("4.40 à 5.60", 4, "« pour finir d'abord la vidéo », le post recule",
   "TEXTE ÉCRAN : « pour finir [boîte : d'abord] la vidéo. » (4.02 à 5.4) ; écart synchro.",
   "IMAGE DE DÉPART : le post CINEMA seul, barre à 92 %.",
   "ÉTAPES : 4.10 le sous-titre précédent part, « pour finir… » entre mot à mot ; 4.40 le grand « ? » vert-bleu fantôme paraît derrière (opacité 0 → .7, 0.3 s) ; 4.82 la barre de lecture atteint 95 % puis 92 % (frémissement) ; 5.00 le post recule et rétrécit (échelle 1 → 0,5, flou 0 → 12, power3.in 0.45 s) ; 5.30 la puce de temps passe à « 00:09 ».",
   "PISTE CAMÉRA : 5.00 à 5.60 recul expo.in jusqu'à échelle 0,5 ; flou 12 px au sommet de la couture.",
   "COUCHES ET PROFONDEUR : avant-plan le « ? » flou ; sujet le post qui recule ; fond papier ; 3 couches.",
   "OBJET-PONT ET VECTEUR : le post CINEMA devient le petit post du pivot (échelle 0,5) qui laisse place à la carte avant/après.",
   "SON : riser de 4.40 à 5.60 (il monte vers le pivot).", "IMAGE CLÉ : 5.40 : le post à 92 % qui recule, le « ? » énorme derrière.")]),
 dict(n=3, id='03-pivot', title="Le pivot : qu'est-ce qu'elles ont de plus ? Moi, c'est James", a=9.58, b=14.16, type='pivot', bp='titlecard-reveal', rules='ambient-glow-bloom, card-morph-anchor',
  voice="Alors, qu'est-ce qu'elles ont de plus ? Moi, c'est James, monteur vidéo.",
  focal="la carte avant/après d'étalonnage « LOG ▸ ÉTALONNÉ », puis le portrait rond de James et son mot-symbole",
  scene="La carte « COLOR GRADING » (avant/après) se pose en grand sur le « ? » ; sur « Moi, c'est James » la tête de lecture s'arrête, la carte devient l'avatar rond de James et le mot-symbole FRAMØTION se compose",
  hin="HS2 : flou 12 px ; le post « @video.en.cours » (barre à 92 %) recule au centre, échelle 0,5, x 540, y 760 ; la notification « Crush » a quitté le cadre à gauche (traînée floue) ; papier clair, grand « ? » fantôme centré à 70 % d'opacité ; tête de lecture à 9.58 s (x 316) ; aucun sous-titre ; grain 14 %",
  hout="HS3 : avatar rond de James (480 u, anneau vert-bleu) centré x 540, y 470, mot-symbole FRAMØTION sous lui ; tout le groupe en défilement vers le bas à −1500 u/s, flou vertical 10 px ; tête de lecture à 14.16 s (x 433) ; aucun sous-titre ; papier clair, grain 14 %",
  cues="Alors@0.00 qu'est-ce@0.70 qu'elles@0.96 ont@1.08 de@1.24 plus@1.34 Moi@2.16 c'est@2.68 James@2.76 monteur@3.54 vidéo@3.82",
  scenes=[
  ("0.00 à 1.40", 1, "« Alors, » puis la carte avant/après se pose",
   "TEXTE ÉCRAN : « Alors, » (0.00) puis « qu'est-ce qu'elles ont [boîte : de plus] ? » (0.70 à 1.5) ; écart synchro ; silence de 0.44 s (« Alors, » → « qu'est-ce ») : action muette = la carte arrive.",
   "IMAGE DE DÉPART : handoff_in : le post CINEMA petit au centre, le « ? » fantôme.",
   "ÉTAPES : 0.00 le post CINEMA se replie en un point au centre (échelle 0,5 → 0,05, flou 12, power3.in 0.18 s) ; 0.10 la carte « COLOR GRADING » (860 × 484, liseré vert-bleu 8 px) naît du même point, trop grande et floue (échelle 1,5 → 1, flou 12 → 0, expo.out 0.4 s) ; 0.50 la puce « LOG ▸ ÉTALONNÉ » paraît sous la carte ; 0.62 la boîte se trace sous « de plus » ; 0.80 le trait de séparation avant/après de la carte glisse de gauche à droite (0.5 s) en révélant les couleurs.",
   "PISTE CAMÉRA : 0.00 à 0.40 atterrissage expo.out ; dérive +30 u/s.",
   "COUCHES ET PROFONDEUR : avant-plan 2 cartes floues (créateur, cadreur) qui dépassent à gauche et à droite ; sujet la carte avant/après nette ; fond le « ? » géant ; 3 couches.",
   "OBJET-PONT ET VECTEUR : la carte avant/après devient l'avatar rond de James en séquence 3 (même centre).",
   "SON : impact grave à 0.10 (la carte arrive).", "IMAGE CLÉ : 1.00 : la carte avant/après nette, la puce « LOG ▸ ÉTALONNÉ », le « ? » géant derrière."),
  ("1.40 à 2.68", 2, "« Moi, » : silence, la tête de lecture ralentit",
   "TEXTE ÉCRAN : « Moi, » (2.16) ; écart synchro ; silence de 1.04 s après « plus ? » : action muette = la carte se resserre.",
   "IMAGE DE DÉPART : la carte avant/après nette, séparation à droite.",
   "ÉTAPES : 1.40 le sous-titre précédent part ; 1.50 les 2 cartes floues sortent du cadre (x ∓300, 0.3 s) ; 1.70 la carte se resserre en carré (860 × 484 → 480 × 480, expo.inOut 0.45 s) ; 2.10 son liseré devient un cercle (border-radius 12 → 240 px, 0.3 s) ; 2.16 « Moi, » apparaît ; 2.40 la lueur vert-bleu clair s'allume derrière (ambient-glow-bloom).",
   "PISTE CAMÉRA : dérive +30 u/s ; 1.70 à 2.15 cran vers le centre (échelle 1 → 1,08, expo.out).",
   "COUCHES ET PROFONDEUR : avant-plan rien ; sujet la carte qui devient un cercle ; fond le « ? » qui s'efface (opacité .7 → .2) ; 2 couches.",
   "OBJET-PONT ET VECTEUR : la carte devient le cercle de l'avatar ; le centre ne bouge pas.",
   "SON : aucun (silence).", "IMAGE CLÉ : 2.20 : la carte en train de devenir un cercle, « Moi, » en sous-titre."),
  ("2.68 à 4.58", 3, "« c'est James, monteur vidéo » : le nom arrive, la tête de lecture s'arrête",
   "TEXTE ÉCRAN : « c'est [boîte : James], » (2.68 à 3.3) + [trait : James] puis « monteur vidéo. » (3.54 à 4.2) ; écart synchro ; silence de 0.5 s (« James, » → « monteur ») : action muette = le mot-symbole se compose.",
   "IMAGE DE DÉPART : le cercle de l'avatar (la photo de James encore en couleur étalonnée de la carte), « Moi, » à l'écran.",
   "ÉTAPES : 2.60 la photo du cercle passe de la carte d'avatar au portrait de James (fondu croisé 0.18 s, même cadre) ; 2.68 la boîte se trace sous « James » ; 2.76 l'anneau vert-bleu tourne d'un tour (0.5 s expo.out) ; 2.76 la tête de lecture de la règle s'arrête (elle gelait 0.4 s) puis reprend ; 3.05 « JAMES » (espacé) paraît au-dessus du mot-symbole ; 3.15 FRAMØTION se compose : chaque lettre arrive des deux côtés (convergence 0.5 s), le Ø reçoit sa barre vert-bleu (rotation 0 → 28°, 0.25 s) ; 3.54 @jamesframotion s'écrit sous le mot-symbole ; 3.60 les 3 vignettes de travaux (timeline, grading, cinéma) montent d'en bas, une à une (0.1 s d'écart) ; 4.20 tenue vivante : l'anneau tourne lentement.",
   "PISTE CAMÉRA : dérive +30 u/s ; 2.60 à 2.90 cran vers le portrait (échelle 1,08 → 1,0, expo.out) ; 4.20 à 4.58 défilement vers le bas −1500 u/s (couture).",
   "COUCHES ET PROFONDEUR : avant-plan les vignettes qui montent, floues au départ ; sujet le portrait et le nom ; fond halo vert-bleu clair ; 3 couches.",
   "OBJET-PONT ET VECTEUR : le portrait rond et le mot-symbole descendent (vecteur vers le bas) : la séquence 4 monte le panneau de montage par le haut-bas.",
   "SON : impact grave à 2.68 (le nom), ping à 3.15 (le mot-symbole), pop à 3.60 (vignettes).", "IMAGE CLÉ : 3.60 : le portrait à anneau, JAMES / FRAMØTION en points, @jamesframotion, le sous-titre « monteur vidéo. »")]),
 dict(n=4, id='04-skills', title="Les outils posés sur une timeline", a=14.16, b=19.36, type='demo', bp='cursor-ui-demo', rules='waterfall-entry, svg-path-draw',
  voice="Hook visuel, étalonnage, transition, sound design, mask, VFX.",
  focal="le panneau de montage avec ses 6 clips (un par compétence), puis la capture Premiere Pro encadrée",
  scene="Un panneau de montage (3 pistes, 3 puces d'outils) se remplit clip par clip au rythme des 6 mots ; la tête de lecture du panneau suit la voix ; la capture Premiere Pro se pose dessous",
  hin="HS3 : avatar rond de James (480 u, anneau vert-bleu) centré x 540, y 470, mot-symbole FRAMØTION sous lui ; tout le groupe en défilement vers le bas à −1500 u/s, flou vertical 10 px ; tête de lecture à 14.16 s (x 433) ; aucun sous-titre ; papier clair, grain 14 %",
  hout="HS4 : flou 10 px ; le panneau de montage (carte blanche 900 u, sommet y 260) glisse vers le haut et sort à 40 % ; la capture Premiere Pro encadrée (600 × 420) est restée centrée en bas de zone ; tête de lecture à 19.36 s (x 566) ; aucun sous-titre ; papier clair, grain 14 %",
  cues="Hook@0.00 visuel@0.16 étalonnage@0.92 transition@1.72 sound@2.54 design@2.74 mask@3.44 VFX@4.06",
  scenes=[
  ("0.00 à 1.70", 1, "le panneau arrive, « Hook visuel » puis « étalonnage »",
   "TEXTE ÉCRAN : « Hook visuel, étalonnage, » (0.00, 0.16, 0.92) ; puces d'outils « Premiere Pro », « CapCut », « DaVinci » ; écart synchro.",
   "IMAGE DE DÉPART : handoff_in : l'avatar et le mot-symbole qui descendent, en flou vertical.",
   "ÉTAPES : 0.00 le groupe avatar sort vers le bas (y +1100, flou 10, expo.in 0.25 s) ; 0.05 le panneau de montage entre par le haut, trop grand (échelle 1,3 → 1, flou 10 → 0, expo.out 0.35 s) ; 0.30 les 3 puces d'outils paraissent une à une (0.1 s d'écart, échelle .8 → 1) ; 0.00 le clip « HOOK VISUEL » se pose sur la piste V2 (x −300 → 0, flou 8 → 0, 0.25 s) ; 0.92 le clip « ÉTALONNAGE » se pose sur la piste V1 (même geste) ; 1.40 la tête de lecture du panneau (trait clair vertical) glisse de x 60 à x 330.",
   "PISTE CAMÉRA : dérive +30 u/s ; 0.05 à 0.40 atterrissage du panneau.",
   "COUCHES ET PROFONDEUR : avant-plan le panneau qui arrive flou ; sujet les clips nets ; fond mini carte floue (PC) à droite ; 3 couches.",
   "OBJET-PONT ET VECTEUR : la tête de lecture du panneau continue dans les scènes suivantes.",
   "SON : whoosh à 0.05 (le panneau), clic à 0.00 et à 0.92 (chaque clip se pose).", "IMAGE CLÉ : 1.00 : le panneau avec 2 clips posés, les 3 puces, « Hook visuel, étalonnage, »."),
  ("1.70 à 2.54", 2, "« transition »",
   "TEXTE ÉCRAN : « transition, » (1.72) ; écart synchro.",
   "IMAGE DE DÉPART : le panneau avec 2 clips, la tête de lecture à x 330.",
   "ÉTAPES : 1.72 le clip « TRANSITION » se pose sur V2 (même geste) ; 1.90 un trait de coupe vertical blanc traverse le clip (0.12 s) ; 2.10 la tête de lecture saute de x 330 à x 470 ; 2.30 la puce de temps générale passe à « 00:16 ».",
   "PISTE CAMÉRA : dérive +30 u/s ; 1.72 à 1.95 petit cran vers le clip (échelle 1 → 1,04).",
   "COUCHES ET PROFONDEUR : avant-plan rien ; sujet le panneau ; fond cartes floues ; 2 couches.",
   "OBJET-PONT ET VECTEUR : le trait de coupe prépare le silence du plan suivant.",
   "SON : clic à 1.72, whoosh court à 1.90.", "IMAGE CLÉ : 2.00 : 3 clips posés, le trait de coupe dans « TRANSITION »."),
  ("2.54 à 3.44", 3, "« sound design » : la piste son et sa forme d'onde",
   "TEXTE ÉCRAN : « [boîte : sound design], » (2.54 à 3.3) ; écart avance de 0.1 s ; silence de 0.52 s avant (16.18 à 16.70 global) : action muette = la piste A1 s'ouvre.",
   "IMAGE DE DÉPART : le panneau avec 3 clips.",
   "ÉTAPES : 2.04 la piste A1 se déroule (scaleY 0 → 1, 0.2 s) ; 2.44 la boîte se trace sous « sound design » ; 2.54 le clip « SOUND DESIGN » se pose sur A1 ; 2.70 la forme d'onde (40 barres) s'allume de gauche à droite (0.5 s) ; 2.90 la tête de lecture saute à x 400 et le trait s'allume en vert-bleu clair.",
   "PISTE CAMÉRA : dérive +30 u/s ; 2.50 à 2.80 cran vers A1 (y +60, expo.out).",
   "COUCHES ET PROFONDEUR : avant-plan rien ; sujet la piste A1 ; fond le panneau ; 2 couches.",
   "OBJET-PONT ET VECTEUR : la forme d'onde glisse vers le haut dans le plan suivant.",
   "SON : bruit de piste (ping) à 2.54.", "IMAGE CLÉ : 3.00 : la piste A1 avec la forme d'onde, le sous-titre « sound design » en boîte."),
  ("3.44 à 5.20", 4, "« mask », « VFX » et la capture Premiere Pro se pose",
   "TEXTE ÉCRAN : « mask, VFX. » (3.44, 4.06) ; écart synchro ; [trait : VFX].",
   "IMAGE DE DÉPART : le panneau avec 4 clips et la forme d'onde.",
   "ÉTAPES : 3.44 le clip « MASK » se pose sur V2 ; 4.06 le clip « VFX » se pose sur V1 ; 4.10 le trait vert-bleu se dessine sous « VFX » (0.4 s) ; 4.30 la capture Premiere Pro (600 × 420, cadre blanc) monte du bas, très flou au départ (y +300, flou 12 → 0, expo.out 0.35 s) ; 4.60 la tête de lecture du panneau atteint la fin ; 4.90 le panneau et la capture montent d'un cran (couture).",
   "PISTE CAMÉRA : dérive +30 u/s ; 4.90 à 5.20 défilement vers le haut expo.in, flou vertical 10 px.",
   "COUCHES ET PROFONDEUR : avant-plan la capture qui monte floue ; sujet les clips ; fond cartes floues ; 3 couches.",
   "OBJET-PONT ET VECTEUR : la capture Premiere Pro devient le cadre de « détail » de la séquence 5.",
   "SON : clic à 3.44 et 4.06, pop à 4.30.", "IMAGE CLÉ : 4.60 : le panneau à 6 clips, la capture Premiere Pro encadrée dessous.")]),
 dict(n=5, id='05-detail', title="Chaque détail est pensé", a=19.36, b=22.90, type='payoff', bp='zoom-out-workspace-reveal', rules='coordinate-target-zoom, depth-of-field-blur',
  voice="Chaque détail est pensé pour capter et garder l'attention.",
  focal="la loupe vert-bleu qui agrandit un détail de la timeline",
  scene="Une carte timeline (vignette de montage) apparaît ; une loupe vert-bleu plonge sur un détail et le grossit ; la loupe rétrécit en un point à la couture",
  hin="HS4 : flou 10 px ; le panneau de montage (carte blanche 900 u, sommet y 260) glisse vers le haut et sort à 40 % ; la capture Premiere Pro encadrée (600 × 420) est restée centrée en bas de zone ; tête de lecture à 19.36 s (x 566) ; aucun sous-titre ; papier clair, grain 14 %",
  hout="HS5 : flou 10 px ; la loupe (cercle vert-bleu, 560 u de diamètre) rétrécit vers un point au centre (x 540, y 760) ; la carte timeline reste en arrière, inclinée à −2°, échelle 0,8 ; tête de lecture à 22.90 s (x 657) ; aucun sous-titre ; papier clair, grain 14 %",
  cues="Chaque@0.00 détail@0.32 est@0.62 pensé@0.78 pour@1.12 capter@1.28 et@1.76 garder@2.18 l'attention@2.54",
  scenes=[
  ("0.00 à 1.12", 1, "« Chaque détail est pensé », la carte timeline",
   "TEXTE ÉCRAN : « Chaque [boîte : détail] est pensé » (0.00 à 1.0) ; écart synchro.",
   "IMAGE DE DÉPART : handoff_in : le panneau qui sort vers le haut, la capture en bas.",
   "ÉTAPES : 0.00 le panneau sort (y −500, flou 10, expo.in 0.2 s) ; 0.10 la carte timeline (780 × 455, inclinée −2°) arrive trop grande et floue (échelle 1,4 → 1, flou 12 → 0, expo.out 0.35 s) ; 0.22 la boîte se trace sous « détail » ; 0.50 le trait vert-bleu de visée (ligne oblique) se dessine de la carte vers le bas (0.3 s) ; 0.85 le cercle de la loupe naît au bout du trait (échelle 0 → 1, 0.25 s expo.out).",
   "PISTE CAMÉRA : dérive +30 u/s ; 0.10 à 0.45 atterrissage de la carte.",
   "COUCHES ET PROFONDEUR : avant-plan la carte qui arrive floue ; sujet la carte nette puis la loupe ; fond mini carte floue à droite ; 3 couches.",
   "OBJET-PONT ET VECTEUR : la loupe reste jusqu'à la couture.",
   "SON : whoosh à 0.10, pop à 0.85 (la loupe naît).", "IMAGE CLÉ : 1.00 : la carte timeline nette, le trait de visée, la loupe qui naît."),
  ("1.12 à 3.54", 2, "la loupe plonge sur le détail, puis se replie",
   "TEXTE ÉCRAN : « pour capter et garder [trait : l'attention]. » (1.12 à 3.3) ; écart synchro.",
   "IMAGE DE DÉPART : la carte, le trait de visée, la loupe vide (sans grossissement).",
   "ÉTAPES : 1.12 la loupe se remplit : le détail de la timeline grossit ×3 dedans (scale 1 → 3 de l'image intérieure, expo.out 0.4 s) ; 1.28 le sous-titre « pour capter… » entre mot à mot ; 1.60 le détail glisse de gauche à droite dans la loupe (x −60, 1.0 s linéaire) pour montrer les clips ; 2.18 le trait vert-bleu se dessine sous « l'attention » (0.4 s) ; 2.60 la poignée de la loupe tourne de −10° (0.3 s) ; 3.10 la loupe rétrécit vers un point au centre (échelle 1 → 0,05, flou 0 → 10, power3.in 0.3 s) ; 3.30 la carte timeline recule (échelle 0,8, x −30).",
   "PISTE CAMÉRA : 1.12 à 1.50 cran vers la loupe (échelle 1 → 1,1, expo.out) ; dérive +30 u/s ; 3.10 à 3.54 recul expo.in, flou 10 px au sommet.",
   "COUCHES ET PROFONDEUR : avant-plan la loupe nette ; sujet le détail grossi ; fond la carte timeline floue ; 3 couches.",
   "OBJET-PONT ET VECTEUR : la loupe rétrécie devient le point central de la grille de la séquence 6.",
   "SON : riser doux 3.0 → 3.5.", "IMAGE CLÉ : 2.00 : la loupe grossissant un détail de la timeline, « garder l'attention » avec son trait.")]),
 dict(n=6, id='06-services', title="Les services de James", a=22.90, b=28.76, type='payoff', bp='grid-card-assemble', rules='waterfall-entry, spring-pop-entrance',
  voice="Publicité, vidéo marketing, documentaire, clip musical, podcast, sketch, sous-titres animés.",
  focal="la grille des 8 tuiles du profil @jamesframotion, une tuile en surbrillance à chaque service",
  scene="Le profil @jamesframotion se déplie ; chaque service est une tuile qui se pose et s'éclaire quand la voix le dit (publicité, vidéo marketing, documentaire, clip musical, podcast, sketch, sous-titres animés)",
  hin="HS5 : flou 10 px ; la loupe (cercle vert-bleu, 560 u de diamètre) rétrécit vers un point au centre (x 540, y 760) ; la carte timeline reste en arrière, inclinée à −2°, échelle 0,8 ; tête de lecture à 22.90 s (x 657) ; aucun sous-titre ; papier clair, grain 14 %",
  hout="HS6 : flou 10 px ; la carte du profil @jamesframotion (grille 4 × 2) recule à l'échelle 0,55, centrée x 540, y 700 ; la tuile « SOUS-TITRES ANIMÉS » (vert-bleu) est au centre de la carte ; tête de lecture à 28.76 s (x 807) ; aucun sous-titre ; papier clair, grain 14 %",
  cues="Publicité@0.00 vidéo@0.86 marketing@1.10 documentaire@2.02 clip@2.92 musical@3.00 podcast@3.78 sketch@4.60 sous-titres@5.24 animés@5.52",
  scenes=[
  ("0.00 à 2.02", 1, "la carte du profil se déplie, publicité puis vidéo marketing",
   "TEXTE ÉCRAN : « Publicité, vidéo marketing, » (0.00, 0.86, 1.10) ; écart synchro.",
   "IMAGE DE DÉPART : handoff_in : le point de la loupe au centre.",
   "ÉTAPES : 0.00 le point se déplie en la carte du profil (échelle 0,05 → 1, flou 10 → 0, expo.out 0.35 s) avec son en-tête « @jamesframotion · monteur vidéo » ; 0.10 la tuile PUBLICITÉ se pose (flou 10 → 0, y +60 → 0, 0.2 s) ; 0.86 la tuile VIDÉO MARKETING se pose ; chaque étiquette de tuile s'écrit en mono sous sa tuile (0.1 s) ; 1.40 la tuile en cours reçoit le liseré vert-bleu (0.12 s).",
   "PISTE CAMÉRA : dérive +30 u/s ; 0.00 à 0.35 atterrissage de la carte.",
   "COUCHES ET PROFONDEUR : avant-plan mini carte floue (grading) à droite ; sujet la grille ; fond papier ; 3 couches.",
   "OBJET-PONT ET VECTEUR : la grille persiste jusqu'à la couture.",
   "SON : pop à 0.10 et 0.86 (chaque tuile), ping à 0.00.", "IMAGE CLÉ : 1.30 : la carte du profil, 2 tuiles posées, « Publicité, vidéo marketing, »."),
  ("2.02 à 3.78", 2, "documentaire, clip musical",
   "TEXTE ÉCRAN : « documentaire, [boîte : clip musical], » (2.02 à 3.5) ; écart synchro ; silence 0.54 s (« marketing, » → « documentaire ») : action muette = la tuile DOCUMENTAIRE se pose.",
   "IMAGE DE DÉPART : la grille avec 2 tuiles.",
   "ÉTAPES : 1.62 la tuile DOCUMENTAIRE se pose ; 2.02 le liseré passe sur DOCUMENTAIRE ; 2.82 la boîte se trace sous « clip musical » ; 2.92 la tuile CLIP MUSICAL se pose et prend le liseré vert-bleu épais avec lueur, échelle 1 → 1,07 (0.2 s) ; 3.40 la lueur retombe.",
   "PISTE CAMÉRA : dérive +30 u/s ; 2.92 à 3.12 cran vers la tuile (échelle 1 → 1,05).",
   "COUCHES ET PROFONDEUR : avant-plan rien ; sujet la tuile en cours ; fond la grille ; 2 couches.",
   "OBJET-PONT ET VECTEUR : le liseré se déplace d'une tuile à la suivante : c'est le fil conducteur.",
   "SON : pop à 1.62 et 2.92.", "IMAGE CLÉ : 3.00 : 4 tuiles, CLIP MUSICAL en surbrillance épaisse."),
  ("3.78 à 5.86", 3, "podcast, sketch, sous-titres animés",
   "TEXTE ÉCRAN : « podcast, sketch, » (3.78, 4.60) puis « sous-titres animés. » (5.24, 5.52) + [trait : animés] ; écart synchro ; silences de 0.42 et 0.42 s : actions muettes = les tuiles se posent.",
   "IMAGE DE DÉPART : la grille avec 4 tuiles.",
   "ÉTAPES : 3.78 la tuile PODCAST se pose et prend le liseré ; 4.60 la tuile SKETCH ; 5.24 la tuile SOUS-TITRES ANIMÉS (tuile pleine vert-bleu, texte « Aa … » blanc) ; 5.52 le trait vert-bleu se dessine sous « animés » (0.3 s) ; 5.20 la 8e tuile (portrait de James, petit) se pose ; 5.30 la carte du profil recule (échelle 1 → 0,55, flou 0 → 10, power3.in 0.5 s).",
   "PISTE CAMÉRA : dérive +30 u/s ; 5.30 à 5.86 recul expo.in, flou 10 px au sommet de la couture.",
   "COUCHES ET PROFONDEUR : avant-plan la tuile qui se pose, floue au départ ; sujet la grille ; fond papier ; 3 couches.",
   "OBJET-PONT ET VECTEUR : la tuile SOUS-TITRES ANIMÉS vert-bleu reste au centre de la carte qui recule : elle devient « une histoire » en séquence 7.",
   "SON : pop à 3.78, 4.60, 5.24 ; whoosh à 5.30.", "IMAGE CLÉ : 5.00 : la grille presque complète, SKETCH en liseré.")]),
 dict(n=7, id='07-histoire', title="Tu as les images ? J'en fais une histoire", a=28.76, b=32.06, type='payoff', bp='kinetic-type-beats', rules='kinetic-beat-slam, scale-swap-transition',
  voice="Tu as les images ? Moi, j'en fais une histoire.",
  focal="la tuile vert-bleu centrale qui devient la phrase « une histoire »",
  scene="La grille recule jusqu'à la tuile vert-bleu qui remplit le cadre ; une rangée de 3 images brutes (vignettes) s'aligne sur « tu as les images » puis la tuile les rassemble en une séquence : « j'en fais une histoire »",
  hin="HS6 : flou 10 px ; la carte du profil @jamesframotion (grille 4 × 2) recule à l'échelle 0,55, centrée x 540, y 700 ; la tuile « SOUS-TITRES ANIMÉS » (vert-bleu) est au centre de la carte ; tête de lecture à 28.76 s (x 807) ; aucun sous-titre ; papier clair, grain 14 %",
  hout="HS7 : flou 8 px ; l'avatar rond de James (240 u, anneau vert-bleu) au centre haut, x 540, y 350, échelle 1,15 ; rien d'autre sauf le papier ; tête de lecture à 32.06 s (x 892) ; aucun sous-titre ; papier clair, grain 14 %",
  cues="Tu@0.00 as@0.54 les@0.62 images@0.76 Moi@1.54 j'en@2.08 fais@2.14 une@2.36 histoire@2.50",
  scenes=[
  ("0.00 à 1.40", 1, "« Tu as les images ? » : 3 images brutes",
   "TEXTE ÉCRAN : « Tu as les [boîte : images] ? » (0.00 à 1.0) ; écart synchro.",
   "IMAGE DE DÉPART : handoff_in : la grille qui recule, la tuile vert-bleu au centre.",
   "ÉTAPES : 0.00 la grille s'efface par le haut (opacité 1 → 0, y −120, 0.2 s) ; 0.10 3 vignettes grises (cadreur, créateur, PC, en gris LOG) arrivent trop grandes et floues l'une après l'autre (0.18 s d'écart, échelle 1,5 → 1) et s'alignent en rangée (3 × 290 u, marges égales) ; 0.62 la boîte se trace sous « images » ; 1.00 les vignettes s'écartent légèrement (gap 24 → 60, 0.3 s).",
   "PISTE CAMÉRA : dérive +30 u/s ; 0.10 à 0.40 cran vers la rangée.",
   "COUCHES ET PROFONDEUR : avant-plan vignette qui arrive floue ; sujet les 3 images ; fond papier ; 3 couches.",
   "OBJET-PONT ET VECTEUR : la rangée devient la séquence « montée » dans la scène suivante.",
   "SON : pop à 0.10, 0.28, 0.46 (chaque image).", "IMAGE CLÉ : 1.20 : les 3 images brutes en gris, « Tu as les images ? »."),
  ("1.40 à 3.30", 2, "« Moi, j'en fais une histoire » : les images se rassemblent",
   "TEXTE ÉCRAN : « Moi, j'en fais une [boîte : histoire]. » (1.54 à 3.0) + [trait : histoire] ; écart synchro ; silence 0.4 s (« images ? » → « Moi, ») : action muette = les images attendent.",
   "IMAGE DE DÉPART : les 3 images en gris, écartées.",
   "ÉTAPES : 1.40 les images frémissent (x ±4 px, 0.2 s) ; 1.54 « Moi, » apparaît ; 2.08 les 3 images passent en couleur étalonnée de gauche à droite (filtre gris → couleur, 0.15 s chacune) ; 2.36 elles se rassemblent en une seule bande de film horizontale (gap 60 → 0, 0.3 s expo.out) ; 2.50 la boîte se trace sous « histoire » ; 2.80 le trait vert-bleu se dessine ; 3.00 la bande rétrécit dans l'avatar rond de James qui monte du centre (échelle 0,2 → 1,15, 0.3 s) ; 3.20 le fil prend la vitesse de la couture.",
   "PISTE CAMÉRA : dérive +30 u/s ; 3.00 à 3.30 cran vers l'avatar (échelle 1 → 1,15, expo.out).",
   "COUCHES ET PROFONDEUR : avant-plan rien ; sujet la bande puis l'avatar ; fond le papier ; 2 couches.",
   "OBJET-PONT ET VECTEUR : la bande de 3 images devient l'avatar de James (centre haut), qui ouvre la carte de fin.",
   "SON : whoosh à 2.36 (elles se rassemblent), ping à 3.00 (l'avatar).", "IMAGE CLÉ : 2.60 : les 3 images en couleur qui se rassemblent en bande, « une histoire » avec son trait.")]),
 dict(n=8, id='08-fin', title="James Framotion, ton monteur vidéo. Écris-moi.", a=32.06, b=36.68, type='cta', bp='cta-morph-press', rules='cursor-click-ripple, ambient-glow-bloom',
  voice="James Framotion, ton monteur vidéo. Écris-moi en DM et abonne-toi !",
  focal="le mot-symbole FRAMØTION, puis la carte « Écris-moi… » et le bouton « S'abonner »",
  scene="L'avatar pose le mot-symbole FRAMØTION ; la carte de message « Écris-moi… » se déplie (la rime de la notification du début) ; un curseur clique « S'abonner » ; les 4 réseaux s'allument ; tenue vivante",
  hin="HS7 : flou 8 px ; l'avatar rond de James (240 u, anneau vert-bleu) au centre haut, x 540, y 350, échelle 1,15 ; rien d'autre sauf le papier ; tête de lecture à 32.06 s (x 892) ; aucun sous-titre ; papier clair, grain 14 %",
  hout="aucun (fin du film : tenue vivante jusqu'à 36.68, la tête de lecture arrive au bout de la règle)",
  cues="James@0.00 Framotion@0.24 ton@1.26 monteur@1.38 vidéo@1.76 Écris-moi@2.64 en@2.98 DM@3.06 et@3.24 abonne-toi@3.86",
  scenes=[
  ("0.00 à 2.64", 1, "« James Framotion, ton monteur vidéo. » : le mot-symbole",
   "TEXTE ÉCRAN : « James Framotion, » (0.00, 0.24) puis « ton monteur vidéo. » (1.26, 1.38, 1.76) ; [boîte : Framotion] ; écart synchro ; silences de 0.42 s (« Framotion, » → « ton ») et 0.54 s (« vidéo. » → « Écris-moi ») : actions muettes = le mot-symbole se compose puis la carte se prépare.",
   "IMAGE DE DÉPART : handoff_in : l'avatar rond au centre haut, flou 8 px.",
   "ÉTAPES : 0.00 l'avatar se pose (flou 8 → 0, échelle 1,15 → 1, expo.out 0.25 s) ; 0.24 la boîte se trace sous « Framotion » ; 0.40 FRAMØTION (92 px) se compose sous l'avatar : les lettres arrivent des deux côtés (0.5 s), le Ø reçoit sa barre (0.25 s) ; 0.90 @jamesframotion s'écrit ; 1.26 le sous-titre suivant entre ; 1.80 les 4 icônes des réseaux (TikTok, Instagram, Facebook, YouTube) montent une à une (0.1 s d'écart) ; 2.30 la carte de message « Hey 😍 tu fais quoi ce soir ? » (bulle grise) se déplie sous le mot-symbole.",
   "PISTE CAMÉRA : dérive +30 u/s ; 0.40 à 0.80 petit cran vers le mot-symbole.",
   "COUCHES ET PROFONDEUR : avant-plan icônes qui montent, floues au départ ; sujet l'avatar et le mot ; fond halo vert-bleu clair ; 3 couches.",
   "OBJET-PONT ET VECTEUR : la bulle grise « Hey 😍 … » est la notification du début, rejouée dans la carte.",
   "SON : impact grave à 0.00, ping à 0.40, pop à 1.80, 1.90, 2.00, 2.10 (les icônes).", "IMAGE CLÉ : 1.80 : l'avatar, FRAMØTION, @jamesframotion, les icônes qui montent."),
  ("2.64 à 4.62", 2, "« Écris-moi en DM et abonne-toi ! » : le clic",
   "TEXTE ÉCRAN : « Écris-moi en [boîte : DM] et abonne-toi ! » (2.64 à 4.4) + [trait : abonne-toi] ; écart synchro.",
   "IMAGE DE DÉPART : la carte de message avec la bulle grise, les icônes alignées.",
   "ÉTAPES : 2.64 le champ « Écris-moi… » (contour vert-bleu) se déplie (scaleX 0 → 1, 0.3 s) ; 3.06 la boîte se trace sous « DM » ; 3.10 le bouton d'envoi rond vert-bleu pulse (échelle 1 → 1,12 → 1, 0.25 s) ; 3.30 le bouton « 🔔 S'abonner » (vert-bleu) monte sous la carte (flou 10 → 0, expo.out 0.3 s) ; 3.86 le curseur arrive d'un seul mouvement courbe (0.45 s power3.out) de la droite du cadre ; 4.20 clic direct sur « S'abonner » (échelle .92, 0.06 s) + onde vert-bleu qui s'étend et s'efface ; 4.25 le trait vert-bleu se dessine sous « abonne-toi » ; 4.30 le bouton devient « Abonné ✓ » (swap 0.15 s) ; 4.30 à 4.62 tenue vivante : l'onde finit, la tête de lecture arrive au bout de la règle.",
   "PISTE CAMÉRA : dérive +30 u/s ; 3.30 à 3.60 cran vers le bouton (échelle 1 → 1,06, expo.out) ; 4.20 à 4.62 dérive lente seulement.",
   "COUCHES ET PROFONDEUR : avant-plan le curseur et l'onde ; sujet la carte et le bouton ; fond le mot-symbole et le halo ; 3 couches.",
   "OBJET-PONT ET VECTEUR : fin du film : le bouton « Abonné ✓ » est le dernier état ; rime : la notification du début devient la carte « Écris-moi… ».",
   "SON : ping à 2.64, pop à 3.30, clic à 4.20.", "IMAGE CLÉ : 4.30 : la carte « Écris-moi… », le bouton « Abonné ✓ », l'onde, @jamesframotion, la règle arrivée au bout.")]),
]
def f(x): return f"{x:.2f}"
total = round(sum(fr['b']-fr['a'] for fr in FRAMES), 2)
head = f'''---
format: 1080x1920
duration: "{total}s"
message: "James Framotion, monteur vidéo, rend ta vidéo irrésistible : écris-lui en DM et abonne-toi."
arc: Hook → Problem → Pivot → Turn → Demo → Payoff → CTA
audience: "créateurs, marques et entrepreneurs qui veulent des vidéos que les gens regardent jusqu'à la fin (francophones, Kinshasa et ailleurs)"
mode: autonomous
captions: disabled
music: "pre-mixed with voice and SFX in assets/audio/mix.wav (mounted at root by the orchestrator)"
direction: "B « Le feed » mêlée à A « La timeline », accent vert-bleu #0C7F8F (DIRECTIONS.md)"
styleframes: "styleframes/png/B1.png (1.6 s), B2.png (4.9 s), B3.png (6.9 s), B4.png (9.6 s), B5.png (12.3 s), B6.png (15.6 s), B7.png (20 s), B8.png (25.2 s), B9.png (34.7 s)"
patterns: ../patterns/STORYBOARD-CRAFT.md, ../patterns/PATTERNS.md
---

## Video direction

- **Un seul monde** (frame.md) : le fil, un réseau social vertical vu de l'intérieur, avec la règle de temps d'un logiciel de montage en haut du cadre. Séquences 1-2 = la douleur (une vidéo à 92 % et un message qui tombe dessus) ; séquence 3 = le pivot ; séquences 4-7 = la solution (les outils, le détail, les services, l'histoire) ; séquence 8 = la carte de fin. Tout est en monde clair (papier #F1EEE7) : pas de flash ni d'iris, la continuité est faite par le défilement. Chaque séquence peint son propre sol sur un calque `class="clip"` de toute sa durée.
- **Coutures invisibles** : toutes les séquences s'enchaînent en `cut` ; la continuité est faite par la caméra : chaque couture tombe au sommet du flou d'un défilement du fil et le `handoff_out` de la séquence N est recopié à l'identique dans le `handoff_in` de la séquence N+1. Exceptions voulues : aucune coupe franche.
- **Texte** (lisible sans le son) : chaque phrase de la voix est un sous-titre bas-centre (zone y 1380 à 1560, rien d'autre dedans) qui arrive MOT PAR MOT sur les temps donnés dans chaque séquence (`mot@secondes`, temps locaux). Un seul mot ou groupe par phrase dans la boîte d'accent (nommé [boîte : …] dans les lignes Scene). Aucun autre texte coloré ou lumineux. Moments typographiques (la phrase EST l'image, centrée, 84 px au plus) : aucun, le sous-titre suffit sur ce film court.
- **Pics** : seulement les 5 pics nommés [trait : …] (ignores, James, VFX, l'attention, animés, histoire, abonne-toi) : un trait vert-bleu fin sous LE mot clé. Jamais un mot géant ni une grosse boîte.
- **Une seule chose à regarder** : à chaque plan la caméra isole le sujet de la phrase ; un défilement vers le haut ou le bas, jamais d'aller-retour ; mises en page côte à côte aux marges égales de 90 ; zéro décor sans sens, aucune ligne qui traverse une phrase.
- **Vraies interfaces** : notifications et fil dessinés à la main (aucune marque tierce) ; les photos de James et ses montages sont toujours petits et encadrés (posts, mini cartes, avatar rond, panneau) ; les noms Premiere Pro, CapCut et DaVinci sont des puces de texte tant que les logos ne sont pas fournis.
- **Grammaire de mouvement** : deux vitesses, gestes de 1 à 6 images (expo.out) et dérive linéaire de +30 u/s qui ne s'arrête jamais ; la zone 0.3 à 0.9 s est réservée à la caméra ; éléments qui arrivent trop grands et flous puis se posent, jamais un fondu à leur taille finale ; aucune tenue figée (chaque tenue nomme sa couche vivante) ; aucune transition « effet ».
- **Texte visible** : exactement le texte cité dans les lignes Scene, rien d'autre.
- **Négatifs** : diaporama (tout à t = 0), écran de veille, objet dédoublé, texte coloré à la place de la boîte, grand mot, grosse boîte, symbole abstrait, curseur hésitant, orange, photo en plein écran, plusieurs objets qui bougent pendant une couture.

**MONDE**
- Acte 1 (0.00 à 9.58) : le fil, post « @createur » puis post « @video.en.cours » ; fond papier clair, halo blanc cassé, grain (rend la dérive visible) ; règle de temps en haut.
- Acte 2 (9.58 à 14.16) : la carte avant/après d'étalonnage, puis le profil de James ; même fond papier.
- Acte 3 (14.16 à 28.76) : le panneau de montage, la loupe, la grille des services ; même fond.
- Acte 4 (28.76 à 36.68) : l'avatar, le mot-symbole, la carte « Écris-moi… » ; même fond.
- Couleurs de rôle : accent = ce qui compte (le mot clé, la tête de lecture, la courbe qui tient, le liseré de la tuile en cours) ; négatif = gris (la courbe des autres, les images LOG, la notification qu'on ignore reste sombre).

**SIGNATURES**
- Mécanisme 1 « Le défilement » : 3.40, 5.00, 14.0, 19.0, 22.9, 28.7, 32.0 (le fil monte ou descend d'un cran avec flou vertical, une fois par idée).
- Mécanisme 2 « La tuile en liseré » : 25.8, 26.7, 27.5, 28.1 (le liseré vert-bleu saute d'un service au suivant, une fois par mot).
- Registres de texte : sous-titre mot à mot = flou 6 → 0 et montée de 10 px en 0.14 s ; boîte = se trace de gauche à droite en 0.16 s ; trait = se dessine de gauche à droite en 0.3 à 0.5 s ; moment typographique = aucun.
- Rimes : la notification « Crush » du début (4.9 s) revient dans la carte « Écris-moi… » de la fin (35 s) ; la tête de lecture, partie de 00:00, arrive au bout de la règle à 36.68 s ; la courbe vert-bleu du début « tient jusqu'à la fin » comme le film.

**PARTITION CAMÉRA** (temps globaux) : 0.04 atterrissage du post · 1.30 cran vers la courbe · 3.40 défilement vers le haut · 5.00 recul · 9.68 atterrissage de la carte avant/après · 11.28 cran vers le centre · 12.18 cran vers le portrait · 14.16 sortie par le bas · 14.21 entrée du panneau · 19.36 sortie par le haut · 22.90 recul · 28.76 recul · 31.2 cran vers l'avatar · 35.3 cran vers le bouton · dérive linéaire +30 u/s vers le haut toute la durée sauf les 2 dernières secondes (tenue vivante lente).

**VOIX** : minutage dans `assets/audio/voix-mots.json` ; silences de plus de 0,4 s, chacun écrit comme un plan : 4.40 à 4.86 (la notification se prépare) · 9.84 à 10.28 (la carte avant/après arrive) · 12.62 à 13.12 (le mot-symbole se compose) · 13.72 à 14.16 (le portrait se tient) · 16.18 à 16.70 (la piste A1 s'ouvre) · 24.38 à 24.92 (la tuile DOCUMENTAIRE) · 26.26 à 26.68 (la tuile PODCAST) · 27.06 à 27.50 (la tuile SKETCH) · 27.72 à 28.14 (la tuile SOUS-TITRES ANIMÉS) · 32.90 à 33.32 (le mot-symbole) · 34.16 à 34.70 (la carte se prépare).

**COUPES** (quota narrative : 0 à 4) : 0 coupe franche ; les 7 coutures sont des défilements du fil.

**RYTHME** : douleur (0 à 9.58) 6 plans en 9.58 s (6,3 / 10 s) ; solution (9.58 à 36.68) 18 plans en 27.1 s (6,6 / 10 s).

**SON** (temps globaux, calé sur les gestes, pas sur les mots) : whoosh 0.04 · ping 1.30 · pop 2.38 · whoosh 3.55 · riser 9.0 à 9.58 · notification 5.40 · whoosh 7.22 · impact grave 9.68 · impact grave 12.26 · ping 12.73 · pop 13.18 · clic 14.16 · riser 22.0 à 22.9 · pop 23.0, 24.0, 24.5, 25.8, 26.7, 27.5, 28.1 · notification 34.70 · clic 36.26 · pas de musique générée (CC0 fournie par James).
'''
out = [head]
for fr in FRAMES:
    out.append(f"## Frame {fr['n']} : {fr['title']} · {f(fr['a'])} → {f(fr['b'])}\n")
    d = round(fr['b']-fr['a'], 2)
    out.append(f"- scene: {fr['scene']}")
    out.append(f"- duration: {d}s")
    out.append("- transition_in: cut")
    out.append("- status: outline")
    out.append(f"- src: compositions/frames/{fr['id']}.html")
    out.append(f"- voiceover: \"{fr['voice']}\"")
    out.append(f"- type: {fr['type']}")
    out.append(f"- blueprint: {fr['bp']} (Adapt)")
    out.append(f"- focal: {fr['focal']}")
    out.append(f"- rules: {fr['rules']}")
    out.append("- world: light")
    out.append(f"- handoff_in: à 0.00 : {fr['hin']}")
    out.append(f"- handoff_out: à {d} : {fr['hout']}\n")
    out.append("Word cues: " + fr['cues'] + "\n")
    for (rng, k, title, texte, depart, etapes, cam, couches, pont, son, cle) in fr['scenes']:
        a, b = rng.split(' à ')
        out.append(f"Scene {k} ({a} à {b} s) : P{k}, {title}")
        for line in (texte, depart, etapes, cam, couches, pont, son, cle):
            out.append("  " + line)
        out.append("")
pathlib.Path.home().joinpath('motion-design-claude-code/presentation/STORYBOARD.md').write_text("\n".join(out), encoding='utf-8')
print("total", total, "frames", len(FRAMES))
