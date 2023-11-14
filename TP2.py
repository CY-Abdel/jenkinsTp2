from datetime import datetime

# Obtenir la date et l'heure actuelles
now = datetime.now()

# Extraire les composants de la date et de l'heure
mm = now.month
dd = now.day
yyyy = now.year
hour = now.hour
mi = now.minute
ss = now.second

# Afficher les informations dans un seul print
print(f"Date et heure actuelles: {mm}/{dd}/{yyyy} {hour}:{mi}:{ss} !")
