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

    motifs = []

    if int(hebergement["places_disponibles"]) == 0:
        motifs.append("aucune place disponible")

    if victime["accompagnee_enfant"] == "Oui" and hebergement["enfant_accepte"] == "Non":
        motifs.append("enfant non accepté")

    if victime["prise_en_charge_nocturne"] == "Oui" and hebergement["accueil_nuit"] == "Non":
        motifs.append("accueil de nuit indisponible")

    if not motifs:
        print(hebergement["hebergement_id"], "COMPATIBLE")
    else:
        print(hebergement["hebergement_id"], "INCOMPATIBLE", motifs)
