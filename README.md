# projet_09

Ce projet LitReview est un MVP d'une application de partage de critiques et avis sur des livres et articles
L'utilisateur peut ainsi : 
  - demander un avis concernant un livre/article aux autres utilisateurs
  - poster son propre avis concerant un livre/article
  - suivre des utilisateurs afin que leurs publications (demandes et avis) s'affichent sur son flux personnel

Afin de faire fonctionner cette application en locale, veuillez suivres les indications suivantes

## Clônage du projet

Tout d'abord, clônez en local le dépôt distant

    $ git clone https://github.com/Benoitrenou/projet_09.git

## Création de l'environnement virtuel

Si vous êtes sur un OS hors Windows 

Depuis votre terminal de commande, effectuez les commandes suivantes 

### Sous Linux/ MAC OS

    $ python -m venv <environment_name>
    exemple : python -m venv envlitreview
    
### Sous Windows:
    
    $ virtualenv <environment_name>
    exemple : virtualenv envlitreview 
    
## Activation de l'environnement virtuel : 

### Sous Linux / MAC OS:

    $ source <environment_name>/bin/activate
    exemple : source envlitreview/bin/activate
   
### Sous Windows:

    $ source <environment_name>/Scripts/activate
    exemple : source envlitreview/Scripts/activate
    
## Installation des packages : 

    $ pip install -r requirements.txt
    
## Lancement de l'application

Dans le terminal depuis le répertoire du projet

    $ python manage.py runserver

Vous pouvez ensuite accéder au site via votre navigateur à l'[adresse suivante](http://127.0.0.1:8000/)

## Accès au site

Il existe un profil de démonstration auquel vous pouvez accéder en entrant les logins suivants:

  Nom d'utilisateur: userdemo
  
  Mot de passe: projet09
  
Vous accéderez ainsi à un flux déjà constitué de plusieurs publications
Vous pouvez également créer votre propre profil via la page d'inscription
