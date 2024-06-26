# Utiliser une image Python officielle comme image de base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

COPY . .

# EXPOSE 80

# Exécuter main.py
CMD ["python", "main.py"]
