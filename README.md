# Documentation

## Introduction
Cette application web utilise le micro-framework Flask et intéragit avec l'API Google Maps afin de pouvoir indiquer à l'utilisateur, où se situe l'adresse qu'il recherche. Elle intéragit également avec l'API Wikipédia qui permet de récupérer du contenu sur l'adresse récupérée pour ainsi, raconter une petite histoire à notre utilisateur. 
Cette application est créé avec le langage de programmation Python pour la partie serveur et JavaScript pour la partie client. Aucune base de données n'est nécessaire.

## Installation

Pour tester en local, il est nécessaire de posséder une clé API Google Maps.
Si vous possédez cette clé, aller dans le fichier config.py  et remplacer la variable suivante :

API_KEY_GOOGLE = os.environ['API_KEY_GOOGLE']

**par** API_KEY_GOOGLE = [VOTRE_CLÉ]

_Utiliser SSH_ : 

    git@github.com:eme-subteno-it/project7.git

_Ou utiliser HTTPS_ :

    https://github.com/eme-subteno-it/project7.git

_Installer les dépendances_ :

    pip install -r requirements.txt

_Pour l'ouvrir_ :

    python3 run.py

ou

    FLASK_APP=run.py

## Utilisation de l'application web
* **Poser votre question à notre GrandPy Bot dans le champ formulaire.**
    * Exemple : 'Connais-tu l'adresse d'OpenclassRooms ?'

* **Visualiser la réponse de notre GrandPy Bot**
    * GrandPy Bot vous donnera l'adresse accompagnée d'une carte Google Maps afin de pouvoir l'a situer.
    * Puis, il vous racontera une petite histoire sur cette adresse.

## Développement
L'application web a été conçu en orienté objet (côté backend) afin de pouvoir différencier la gestion de l'API Google Maps, le système de parsing pour les questions des utilisateurs et l'API de Wikipédia. Ces classes sont situés dans le dossier /models. À la racine de l'application, nous pouvons retrouver un fichier main.py qui gère les différentes routes de l'app. 