import csv

with open("victimes_synthetiques.csv", encoding="utf-8-sig") as fichier:
    victimes = list(csv.DictReader(fichier))

with open("hebergements_synthetiques.csv", encoding="utf-8-sig") as fichier:
    hebergements = list(csv.DictReader(fichier))

with open("lieux_prise_en_charge_synthetiques.csv", encoding="utf-8-sig") as fichier:
    lieux = list(csv.DictReader(fichier))

for victime in victimes:

    if victime["victime_id"] == "V001":

        for hebergement in hebergements:

            if int(hebergement["places_disponibles"]) == 0:
                continue

            if victime["accompagnee_enfant"] == "Oui" and hebergement["enfant_accepte"] == "Non":
                continue

            if victime["prise_en_charge_nocturne"] == "Oui" and hebergement["accueil_nuit"] == "Non":
                continue

            print(victime["victime_id"], hebergement["hebergement_id"], "compatible")
