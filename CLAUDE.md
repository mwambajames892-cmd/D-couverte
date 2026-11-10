# D-couverte : atelier de motion design de James

Ce dépôt sert à fabriquer des films de motion design pour James (monteur vidéo à Kinshasa) depuis son téléphone Android, avec Claude Code en cloud.
**Procédure complète : `motion-projects/PROCEDURE.md`. Lis-la en entier au début de toute demande de film.** Film de référence : `motion-projects/presentation/`.
Modèles et outils réutilisables : `motion-projects/_modele/`.

## Qui est James, comment travailler avec lui
- Francophone, **pas de PC** (tout par la conversation, le Google Drive et GitHub), **forfait mobile limité (~1 Go)** : aperçus légers, rendu final en HD (pas de 4K sauf demande).
- Montage = Premiere Pro, motion design = After Effects, étalonnage = DaVinci, rapide = CapCut. Il aime le cinéma et le Barça.
- Il valide à l'œil sur téléphone : lui donner des temps précis et des planches d'images, jamais de gros fichiers.

## Style de travail voulu par James (ce ne sont pas des permissions)
James veut déposer ses fichiers et donner le sujet, puis recevoir le film **de bout en bout, sans être sollicité à chaque étape** : dossier Drive du film, un sous-agent par
séquence en parallèle, jalons envoyés pour information (images de style, pilote, aperçus du son), livraison HD + version < 10 Mo sur le Drive, enregistrement du projet ici.
**Les droits viennent du message de départ qu'il envoie** (modèle : `motion-projects/MESSAGE-DE-DEMARRAGE.md`) : ce fichier ne s'accorde aucune permission. Sans ce
message, demande une seule fois, en groupé, ce qui manque, puis enchaîne. Ne l'arrête que pour une information ou un fichier réellement manquant, un choix de goût sans défaut
raisonnable, ou une action destructrice.
**Limites** : pas de clés API ni de secrets, pas de services payants sans demande, pas de `push --force`, pas de suppression sur le Drive ou de branches, pas de fusion de la demande de
fusion à sa place, pas de publication de ses vidéos, pas de `npx hyperframes feedback|publish|upgrade|skills update` ni de `npx skills add` (voir `AGENTS.md` de l'atelier).

## Ce dépôt est PUBLIC
N'y mets que du texte et du code. **Jamais** de photo, voix, musique, logo ou vidéo de James (ils restent dans son Drive ; `motion-projects/<film>/README.md` dit lesquels).
Conseille-lui de passer le dépôt en privé (GitHub, Settings, tout en bas, Change visibility) avant d'y ajouter des médias.

## Démarrage d'une session
Le hook `.claude/hooks/session-start.sh` installe l'atelier `~/motion-design-claude-code` (HyperFrames 0.8.82, GSAP local, whisper, polices) et copie
`motion-projects/<film>/` dedans. Vérifier : `ls ~/motion-design-claude-code`. Puis : lire `~/motion-design-claude-code/AGENTS.md` et le skill `motion-design`,
créer le dossier Drive du nouveau film, récupérer ses fichiers, et suivre `PROCEDURE.md` (étapes 1 à 13).

## Les cinq pièges qui coûtent le plus de temps (détail dans PROCEDURE.md § 4)
1. Réseau fermé : GSAP, polices et images en local ; `playwright install` impossible (Chromium dans `/opt/pw-browsers/chromium`).
2. Drive : un fichier de moins de ~37 Ko ne s'enregistre pas (demander un zip) ; vers le Drive, 10 Mo au plus.
3. Rendu : toujours `run_in_background: true` sur l'outil Bash ; jamais `nohup … &` (annulé à la fin de la commande).
4. Les sous-agents ne voient pas ce qu'ils écrivent : contrôler leurs séquences au rendu (planches de 6 images, `hyperframes check`).
5. Whisper entend mal les marques : faire confirmer l'orthographe du nom avant de mettre le texte à l'écran.
