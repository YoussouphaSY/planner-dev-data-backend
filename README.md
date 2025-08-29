//  Gestion des Utilisateurs et Plannings

[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/) 
[![Django](https://img.shields.io/badge/django-5.2-green)](https://www.djangoproject.com/) 
[![DRF](https://img.shields.io/badge/DjangoRESTFramework-3.16.0-blueviolet)](https://www.django-rest-framework.org/) 
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Une application Django REST pour gérer les utilisateurs et leurs plannings, avec authentification JWT et base de données PostgreSQL. Elle permet de gérer facilement les utilisateurs selon leur filière et de suivre leurs plannings via une API sécurisée.



 Fonctionnalités principales

- Gestion des utilisateurs :
  - Email unique
  - Prénom et nom
  - Filière (Data, Dev-Web, Ref-Dig, Aws, Hackeuse)
- Authentification sécurisée via JWT
- Gestion des plannings liés aux utilisateurs
- API REST CRUD complète pour utilisateurs et plannings
- Compatible PostgreSQL
- Supporte la configuration via .env pour la sécurité des clés

---

// Technologies utilisées

- Python 3.8
- Django 5.2.4
- Django REST Framework
- Django CORS Headers
- Simple JWT
- PostgreSQL
- psycopg2-binary
- python-decouple

---

// Installation

1. Cloner le projet :

~bash: 
git clone https://github.com/ton-utilisateur/ton-projet.git
cd ton-projet

//Creer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


//installer les dependances
pip install -r requirements.txt

//Configuerer la base PostgresSQL dans .env
DB_NAME=nom_de_la_base
DB_USER=utilisateur
DB_PASSWORD=motdepasse
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=ta_clef_secrète

//Appliquer les migrations
python manage.py migrate

//Creer un utilisateur
python manage.py migrate


//Creer un super Utilisateur
python manage.py migrate

//Lancer le serveur
python manage.py runserver

Structure du projet
daily_360/
│-- plannnings/               # Application pour les plannings
|   |--init.py               # Permet la configuration de l'interface d'adiministration Django
|   |--amdin.py              # importation des modules
│   │--models.py             # Modèles  Planning pour creer les taches
│   │--views.py              # Vues / API:Contient la logique métier et la réponse aux requêtes HTTP
|   |--urls.py:               # Définit les routes de l’application, c’est-à-dire les URL accessibles.
|   |--test.py               #Contient les tests unitaires pour vérifier que l’app fonctionne correctement.
|   |--urls.py:              #Définit les routes de l’application, c’est-à-dire les URL accessibles.  
│   │--serializers.py        # Convertit les modèles Django en JSON et inversement.
|   |--apps.py                # Définit la configuration de l’application (nom, label, etc.).
│-- requirements.txt          # Toutes les modules utilises et leur depandances
|
|
|-- users/
|   |--Migrations/
|   |--_pycache
|   |--init.py               # Permet la configuration de l'interface d'adiministration Django
|   |--amdin.py              # importation des modules
│   │--models.py             # Modèles  Planning pour creer les taches
│   │--views.py              # Vues / API:Contient la logique métier et la réponse aux requêtes HTTP
|   |--urls.py:               # Définit les routes de l’application, c’est-à-dire les URL accessibles.
|   |--test.py               #Contient les tests unitaires pour vérifier que l’app fonctionne correctement.
|   |--urls.py:              #Définit les routes de l’application, c’est-à-dire les URL accessibles.  
│   │--serializers.py        # Convertit les modèles Django en JSON et inversement.
|   |--apps.py                # Définit la configuration de l’application (nom, label, etc.).
│-- requirements.txt          # Toutes les modules utilises et leur depandances
│-- manage.py
│-- README.md
│-- .env


Documentation

pour les utilisateurs

| Méthode | Endpoint         | Description                  |
| ------- | ---------------- | ---------------------------- |
| POST    | /api/register/   | Créer un utilisateur         |
| POST    | /api/login/      | Obtenir un token JWT         |
| GET     | /api/users/      | Liste des utilisateurs       |
| GET     | /api/users/<id>/ | Détails d’un utilisateur     |
| PUT     | /api/users/<id>/ | Mettre à jour un utilisateur |
| DELETE  | /api/users/<id>/ | Supprimer un utilisateur     |


pour les plannings

| Méthode | Endpoint             | Description               |
| ------- | -------------------- | ------------------------- |
| GET     | /api/plannings/      | Liste des plannings       |
| POST    | /api/plannings/      | Créer un planning         |
| GET     | /api/plannings/<id>/ | Détails d’un planning     |
| PUT     | /api/plannings/<id>/ | Mettre à jour un planning |
| DELETE  | /api/plannings/<id>/ | Supprimer un planning     |

pour les periodes de planning

| Champ       | Type    | Description                                                          |
| ----------- | ------- | -------------------------------------------------------------------- |
| date\_debut | Date    | Date de début du planning                                            |
| date\_fin   | Date    | Date de fin du planning (calculée automatiquement si non renseignée) |
| est\_expire | Booléen | True si la période est dépassée et le planning n’est pas terminé     |


⚠️ À adapter selon tes routes réelles dans Django REST Framework

1-Fork le projet

1-Créer une branche : git checkout -b feature/nouvelle-fonctionnalite

2-Commit tes changements : git commit -m 'Ajout fonctionnalité'

3-Push la branche : git push origin feature/nouvelle-fonctionnalite

5-Créer une Pull Request

📌 Notes

Utiliser .env pour protéger les informations sensibles

Vérifier que PostgreSQL est installé et configuré avant de lancer le projet

Les endpoints peuvent être testés via Postman ou tout autre outil REST