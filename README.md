# 🎮 Clean Architecture Pong (Python & Pygame)

A professional, decoupled implementation of the classic Pong game using Hexagonal Architecture (Ports & Adapters), built inside a fully containerized Docker Devcontainer environment.

Une implémentation professionnelle et découplée du jeu classique Pong, utilisant l'Architecture Hexagonale (Ports & Adaptateurs) et conçue au sein d'un environnement de développement conteneurisé via Docker Devcontainer.

---

## 📌 Table of Contents / Table des Matières

* [🇬🇧 English Version](#-english-version)
    * [Key Features](#key-features)
    * [Architectural Design](#architectural-design)
* [🇫🇷 Version Française](#-version-française)
    * [Fonctionnalités Clés](#fonctionnalités-clés)
    * [Conception Architecturale](#conception-architecturale)
* [📂 File Structure / Structure des Fichiers](#-file-structure--structure-des-fichiers)
* [🕹️ Controls / Contrôles](#️-controls--contrôles)
* [🚀 Installation & Run / Installation & Exécution](#-installation--run--installation--exécution)

---

## 🇬🇧 English Version

### Key Features

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Domain Engine** | Python OOP & Dataclasses | Core business logic, interfaces (Ports), and service orchestrator. |
| **UI / Graphics** | Pygame | Graphical adapter implementing the game port. |
| **Environment** | Docker & Compose | Debian Trixie workspace isolated with permissions matching the host. |

### Architectural Design

This project implements the **Ports & Adapters (Hexagonal) Pattern**:

* **Domain (Inside):** Houses the `RunnerPongGamePort` interface and the `RunnerService` controller. The domain is completely decoupled and does not know how the game is rendered or handled.
* **Infrastructure (Outside):** The `PygameRunnerPongGameAdapter` implements the port, handling screen drawing, clock ticking, key inputs, and physics logic. This makes it trivial to swap Pygame with another engine (like Arcade, Kivy, or even a CLI mode) without touching the domain.

---

## 🇫🇷 Version Française

### Fonctionnalités Clés

| Composant | Technologie | Rôle |
| :--- | :--- | :--- |
| **Moteur Métier** | Python POO & Dataclasses | Logique métier pure, interfaces (Ports), et orchestrateur de services. |
| **Interface / Graphisme** | Pygame | Adaptateur graphique qui implémente le port du jeu. |
| **Environnement** | Docker & Compose | Espace de travail Debian Trixie isolé avec gestion des permissions hôte. |

### Conception Architecturale

Ce projet implémente le modèle **Ports & Adaptateurs (Architecture Hexagonale)** :

* **Domaine (Intérieur) :** Héberge l'interface `RunnerPongGamePort` et le contrôleur `RunnerService`. Le domaine est complètement découplé et ignore la manière dont le jeu est rendu.
* **Infrastructure (Extérieur) :** L'adaptateur `PygameRunnerPongGameAdapter` implémente le port, gérant l'affichage de l'écran, le rafraîchissement (*clock ticking*), les entrées clavier et la physique du jeu. Cela permet de remplacer facilement Pygame par un autre moteur (Arcade, Kivy, ou même un mode CLI) sans altérer le domaine.

---

## 📂 File Structure / Structure des Fichiers

```text
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