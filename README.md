# NotifTweets

Programme qui envoie une timeline twitter donnée sur discord via un webhook.

Il utilise l'api de twitter version 1.1, et l'api des webhooks discord.

## Statut

Pas terminé (~40%)

## Fait

### 03/01/2023
- Récupération de tous les tweets depuis un tweet choisi, avec toutes les informations nécessaires (arobase, tn, pp, contenu texte du tweet)
- Mise en forme du tweet pour intégrer sur discord en embed
- Récupère et envoie la première image du tweet

### 04/01/2023
- Fonctionne avec une liste d'arobases
- Sauvegarde du dernier tweet envoyé par arobase dans le fichier "derniers_tweets.csv" pour qu'il ne soient pas renvoyé à la prochaine exécution

### 11/01/2023
- Prise en compte des retweets : envoi du tweet retweeté avec, en plus, l'arobase de la personne qui l'a retweeté

## A faire

- Séparer le code en plusieurs fonctions pour le rendre plus propre
- Prendre en compte les tweets cités
- Récupérer toutes les images du tweet
- Passer les requêtes en asynchronisé pour avoir une timeline mélangée, et une exécution plus rapide
