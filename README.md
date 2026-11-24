# 🤖 Agent de service client avec LangGraph

## 📌 Présentation

Ce projet consiste à développer un agent intelligent de service client pour une boutique en ligne tunisienne.

L'agent utilise LangGraph pour orchestrer les interactions avec le modèle Gemini, interroger une base vectorielle ChromaDB et accéder aux données des commandes stockées dans SQLite.

Il intègre également un mécanisme Human-in-the-Loop (HITL) permettant de demander une validation humaine avant toute opération sensible.

## 🏗️ Architecture et technologies

- Python
- LangGraph
- LangChain
- Google Gemini
- ChromaDB
- RAG (Retrieval-Augmented Generation)
- SQLite
- Streamlit
- uv

## ✨ Fonctionnalités

- Répondre aux questions concernant la politique de la boutique.
- Rechercher des informations dans un document PDF avec RAG.
- Consulter l'état des commandes.
- Demander l'annulation d'une commande.
- Enregistrer une demande de retour.
- Demander une validation humaine avant une opération sensible.
- Conserver un journal des validations.
- Afficher une interface interactive avec Streamlit.

## 📂 Structure du projet

```text
agent-service-client-langgraph/
│
├── agent_boutique_state.py
├── app_streamlit_state.py
├── indexer.py
├── outils_base.py
├── politique_boutique.pdf
├── graphe_agent.png
├── pyproject.toml
├── uv.lock
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Prérequis

- Python 3.11+
- uv
- Une clé API Google Gemini

### 2. Cloner le projet

```bash
git clone https://github.com/TON-USERNAME/agent-service-client-langgraph.git
cd agent-service-client-langgraph
```

### 3. Installer les dépendances

```bash
uv sync
```

### 4. Configurer les variables d'environnement

Créer un fichier `.env` à la racine du projet :

```env
GOOGLE_API_KEY=your_google_api_key
MODELE=gemini-2.5-flash
EMBEDDINGS=gemini-embedding-001
```

Remplacer `your_google_api_key` par votre propre clé API.

### 5. Indexer le document PDF

```bash
uv run indexer.py
```

Cette étape permet de charger le document, de créer les embeddings et de stocker les données dans ChromaDB.

### 6. Lancer l'application

```bash
uv run streamlit run app_streamlit_state.py
```

## 🧪 Scénarios de test

Quelques questions pour tester l'agent :

- Quels sont les délais de livraison ?
- Où en est la commande 1002 ?
- Annule ma commande 1001.
- Je souhaite retourner la commande 1003.
- Je souhaite retourner la commande 1004.

## 🔐 Sécurité

Les opérations sensibles nécessitent une validation humaine.

La clé API doit rester dans le fichier `.env`, qui ne doit jamais être publié sur GitHub.

## 👩‍💻 Auteur

Projet académique réalisé dans le cadre d'un atelier sur les agents intelligents, LangGraph et le RAG.