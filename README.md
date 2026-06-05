🎮 Clean Architecture Pong (Python & Pygame)

A professional, decoupled implementation of the classic Pong game using Hexagonal Architecture (Ports & Adapters) and built inside a fully containerized Docker Devcontainer environment.

Une implémentation professionnelle et découplée du jeu classique Pong, utilisant l'Architecture Hexagonale (Ports & Adaptateurs) et conçue au sein d'un environnement de développement conteneurisé via Docker Devcontainer.

📌 Table of Contents / Table des Matières

🇬🇧 English Version

Key Features

Architectural Design

File Structure

Controls

Installation & Run

🇫🇷 Version Française

Fonctionnalités Clés

Conception Architecturale

Structure des Fichiers

Contrôles

Installation & Exécution

🇬🇧 English

Key Features

Component

Technology

Role

Domain Engine

Python OOP & Dataclasses

Core business logic, interfaces (Ports), and service orchestrator.

UI / Graphics

Pygame

Graphical adapter implementing the game port.

Environment

Docker & Compose

Debian Trixie workspace isolated with permissions matching the host.

Architectural Design

This project implements the Ports & Adapters (Hexagonal) Pattern:

Domain (Inside): Houses the RunnerPongGamePort interface and the RunnerService controller. The domain is completely decoupled and does not know how the game is rendered or handled.

Infrastructure (Outside): The PygameRunnerPongGameAdapter implements the port, handling screen drawing, clock ticking, key inputs, and physics logic. This makes it trivial to swap Pygame with another engine (like Arcade, Kivy, or even a CLI mode) without touching the domain.

🇫🇷 Français

Fonctionnalités Clés

Composant

Technologie

Rôle

Moteur Métier

Python POO & Dataclasses

Logique métier pure, interfaces (Ports), et orchestrateur de services.

Interface / Graphisme

Pygame

Adaptateur graphique qui implémente le port du jeu.

Environnement

Docker & Compose

Espace de travail Debian Trixie isolé avec gestion des permissions hôte.

Conception Architecturale

Ce projet implémente le modèle Ports & Adaptateurs (Hexagonal) :

Domaine (Intérieur) : Héberge l'interface RunnerPongGamePort et le contrôleur RunnerService. Le domaine est complètement découplé et ignore comment le jeu est rendu.

Infrastructure (Extérieur) : L'adaptateur PygameRunnerPongGameAdapter implémente le port, gérant l'affichage de l'écran, le rafraîchissement, les entrées clavier et la physique du jeu. Cela permet de remplacer facilement Pygame par un autre moteur (Arcade, Kivy, ou même un mode CLI) sans altérer le domaine.

📂 File Structure / Structure des Fichiers

.
├── domaine/
│   └── ports/
│       └── RunnerPongGamePort.py      # Abstract interface (Port)
├── infrastructure/
│   └── adapters/
│       └── PygameRunnerPongGame.py    # Pygame implementation (Adapter)
├── services/
│   └── RunnerService.py               # Domain Service orchestrator
├── Dockerfile                         # Container setup (Debian Trixie)
├── docker-compose.yml                 # Service & volume mounts
└── README.md                          # Documentation


🕹️ Controls / Contrôles

Player / Joueur

Up / Monter

Down / Descendre

Screen Side / Côté

Player 1 (Right / Droite)

▲ (Up Arrow)

▼ (Down Arrow)

Right / Droite

Player 2 (Left / Gauche)

M

S

Left / Gauche

🚀 Installation & Run / Installation & Exécution

🇬🇧 English: Running with Docker Compose

To run inside the isolated Devcontainer and avoid dependency conflicts:

Configure environment variables (or set them directly in your shell):

export USERNAME=$(whoami)
export USERID=$(id -u)
export GROUPNAME=$(whoami)
export GROUPID=$(id -g)


Build and launch the container:

docker compose up -d --build


Enter the container:

docker compose exec devcontainer bash


Run the game (Ensure your X11 server is shared with Docker if you want to display Pygame windows on your host screen):

python3 main.py


🇫🇷 Français : Exécution avec Docker Compose

Pour exécuter le projet dans le conteneur isolé et éviter les conflits de dépendances :

Configurer les variables d'environnement (ou exportez-les directement dans votre terminal) :

export USERNAME=$(whoami)
export USERID=$(id -u)
export GROUPNAME=$(whoami)
export GROUPID=$(id -g)


Construire et démarrer le conteneur :

docker compose up -d --build


Accéder au conteneur :

docker compose exec devcontainer bash


Lancer le jeu (Assurez-vous que votre serveur X11 est partagé avec Docker pour afficher la fenêtre Pygame sur votre écran hôte) :

python3 main.py
