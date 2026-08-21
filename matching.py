import csv

with open("victimes_synthetiques.csv", encoding="utf-8-sig") as fichier:
    victimes = list(csv.DictReader(fichier))

with open("hebergements_synthetiques.csv", encoding="utf-8-sig") as fichier:
    hebergements = list(csv.DictReader(fichier))

with open("lieux_prise_en_charge_synthetiques.csv", encoding="utf-8-sig") as fichier:
    lieux = list(csv.DictReader(fichier))

with open("distances_sante_synthetiques.csv", encoding="utf-8-sig") as fichier:
    distances_sante = list(csv.DictReader(fichier))

with open("etablissements_sante.csv", encoding="utf-8-sig") as fichier:
    etablissements_sante = list(csv.DictReader(fichier))

for victime in victimes:

    if victime["victime_id"] == "V001":
               
        if victime["examen_medical_necessaire"] == "Oui":

            distances_possibles = []

            for distance in distances_sante:

                if distance["lieu_id"] == victime["lieu_prise_en_charge_id"]:
                    distances_possibles.append(distance)

            print("Établissements conventionnés :")

            for distance in distances_possibles:
                print(distance["etablissement_id"], distance["distance_km"], "km")

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
