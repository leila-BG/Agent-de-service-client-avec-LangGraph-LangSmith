

"""Point d'entrée pour LangGraph Studio"""

from outils_base import creer_base
from agent_boutique_state import graphe

# Initialisation de la base de données
creer_base()

# Compilation du graphe
agent = graphe.compile()