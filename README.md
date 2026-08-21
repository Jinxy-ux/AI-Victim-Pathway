# AI-Victim-Pathway
How could artificial intelligence help ensure that every victim receives the right support, at the right time, rather than having to navigate a fragmented system alone?

## Summary

AI Victim Pathway is a prototype decision-support tool designed to assist professionals in orienting victims of domestic violence toward appropriate healthcare facilities and emergency accommodation.

The program uses victim-specific information and the location where the victim is being assisted to determine whether medical care is required. When necessary, it identifies conventioned healthcare facilities, compares their distances, and recommends the nearest one.

It then evaluates available accommodation facilities according to compatibility criteria such as availability, acceptance of accompanying children, and night-time reception. Incompatible facilities are excluded with an explicit reason.

The current project uses synthetic data and is intended as a proof of concept, not as an operational decision-making system.

## Le constat

Aujourd’hui, le parcours d'aide aux victimes est globalement construit autour des institutions : police, justice, associations, psychologues, intervenants sociaux, hôpitaux, hébergement, indemnisation…

La victime doit souvent passer d'un dispositif à l'autre, raconter, comprendre, chercher et parfois relancer elle-même les différents acteurs.

## L'idée

L'objectif d'**AI Victim Pathway** est d'explorer comment l'intelligence artificielle pourrait contribuer à construire le parcours d'aide autour de la victime et de ses besoins.

L'IA ne serait pas simplement un « chatbot d'aide aux victimes ». Elle jouerait le rôle d'un **orchestrateur de parcours**, sous le contrôle des professionnels.

Avec le consentement de la victime, un système pourrait analyser uniquement les informations nécessaires et identifier différents besoins : sécurité immédiate, logement, enfants, santé, soutien psychologique, ressources financières, transport, protection juridique ou démarches administratives.

Il pourrait ensuite proposer un parcours personnalisé et évolutif.

Par exemple :

**danger immédiat → hébergement disponible → transport nécessaire → accompagnement adapté**

ou :

**enfant victime → dispositif spécialisé → professionnel disponible → suivi**

## La question centrale

> **Peut-on utiliser l'IA pour faire en sorte qu'aucune victime identifiée ne reste avec un besoin essentiel sans solution proposée ?**

## Deux niveaux d'utilisation

### Pour la victime

Le système chercherait à mettre en relation ses besoins, sa situation et les ressources réellement disponibles afin d'aider les professionnels à proposer les solutions les plus adaptées.

### Pour les décideurs

L'analyse agrégée pourrait faire apparaître les besoins auxquels un territoire ne répond pas suffisamment : manque de psychologues disponibles, insuffisance des places d'hébergement, éloignement géographique de certains dispositifs ou absence de ressources spécialisées.

L'IA ne servirait donc pas seulement à orienter les victimes. Elle pourrait également permettre d'identifier les **besoins non couverts**.

## Une nouvelle mesure : le besoin résolu

Au lieu de mesurer uniquement l'activité des dispositifs — nombre de victimes reçues, nombre d'entretiens ou nombre d'orientations — le projet propose d'explorer une autre logique :

**besoin détecté → solution proposée → solution accessible → besoin effectivement résolu**

L'existence d'une ressource ne signifie pas nécessairement que le besoin est couvert. Une solution peut exister mais être indisponible, trop éloignée ou inaccessible à la victime.

## Comment l'IA pourrait intervenir

Le projet explorera plusieurs possibilités :

* classification des besoins ;
* recommandation et mise en relation entre besoins et ressources ;
* optimisation de l'utilisation des ressources disponibles ;
* détection ou prédiction des ruptures de parcours ;
* analyse territoriale des besoins non couverts.

Ces possibilités devront être étudiées en tenant compte de questions essentielles : confidentialité des données, consentement, biais algorithmiques, explicabilité des recommandations et maintien de la décision humaine.

L'objectif n'est pas de remplacer le professionnel par une intelligence artificielle, mais d'étudier comment l'IA pourrait l'aider à mettre en relation simultanément une multitude de besoins, de droits, de contraintes et de ressources disponibles.

## Prototype

Une première expérimentation pourra être réalisée à partir de **données entièrement fictives**, par exemple :

* 20 profils fictifs de victimes ;
* 30 ressources fictives ;
* différents besoins et contraintes ;
* un algorithme simple de mise en relation entre besoins et ressources.

Le prototype cherchera à montrer comment un système peut proposer des correspondances pertinentes tout en faisant apparaître les besoins pour lesquels aucune solution satisfaisante n'est disponible.

**Aucune donnée personnelle réelle concernant des victimes ne sera utilisée dans ce projet.**

#Prototype :
## Premier cas d'usage : mise à l'abri après des violences intrafamiliales

La première version du prototype se concentrera sur l'orientation vers un hébergement d'une victime de violences intrafamiliales nécessitant une mise à l'abri.

Le système devra prendre en compte plusieurs catégories d'informations.

### Données concernant la victime

Pour respecter le principe de minimisation des données, le moteur de recommandation n'a pas besoin de connaître l'identité de la victime. Un identifiant fictif suffit pour le prototype.

Les variables utiles pourront notamment être :

* âge ;
* type de violences ;
* nécessité éventuelle d'un examen médical préalable ;
* lieu de prise en charge ;
* mobilité ou besoin de transport ;
* présence et nombre d'enfants accompagnants ;
* heure de prise en charge ;
* besoin de mise à l'abri immédiate ;
* contraintes de sécurité.

### Données concernant les hébergements

Pour chaque lieu fictif :

* localisation ;
* disponibilité à l'instant considéré ;
* possibilité d'accueil nocturne et horaires d'admission ;
* possibilité d'accueillir des enfants ;
* conditions ou capacité d'accueil des enfants ;
* possibilités de transport ou de taxi ;
* distance et temps de trajet ;
* compatibilité avec les contraintes de sécurité.

### Logique de recommandation

Le système distinguera trois types de critères :

**1. Contraintes éliminatoires**

Une ressource incompatible est écartée. Il peut s'agir notamment de l'absence de place disponible, de l'impossibilité d'accueillir les enfants accompagnants, de l'absence d'accueil nocturne lorsque celui-ci est nécessaire ou d'une incompatibilité avec une contrainte de sécurité.

**2. Conditions modifiant le parcours**

Certaines informations ne conduisent pas nécessairement à éliminer un hébergement mais modifient les étapes nécessaires. Par exemple, la nécessité d'un examen médical peut conduire à proposer le parcours :

**prise en charge → hôpital → hébergement**

plutôt que :

**prise en charge → hébergement**

**3. Critères de classement**

Après élimination des solutions incompatibles, les ressources restantes pourront être classées selon différents critères, notamment le temps de trajet, la distance et les possibilités d'acheminement.

La recommandation finale restera une **aide à la décision** : le système proposera les solutions compatibles et expliquera les raisons de leur classement, mais la décision restera sous le contrôle du professionnel.

## Première logique de filtrage

La première version du prototype utilise des règles explicites pour éliminer les hébergements qui ne peuvent pas répondre à la situation de la victime.

```python
for hebergement in hebergements:

    if hebergement["places_disponibles"] == 0:
        continue

    if victime["accompagnee_enfant"] == "Oui" and hebergement["enfant_accepte"] == "Non":
        continue

    if victime["prise_en_charge_nocturne"] == "Oui" and hebergement["accueil_nuit"] == "Non":
        continue

    print(hebergement["hebergement_id"], "compatible")
```

"Évolution du prototype : orientation vers un établissement de santé

Le prototype intègre désormais une étape préalable d'orientation médicale lorsque la situation de la victime nécessite un examen médical.

À partir du lieu de prise en charge de la victime, le programme :

identifie les établissements de santé conventionnés ;
compare leurs distances ;
recommande l'établissement le plus proche ;
affiche les autres établissements disponibles afin de conserver une logique d'aide à la décision ;
poursuit ensuite la recherche d'un hébergement adapté.

Les distances utilisées dans cette version sont des données synthétiques. Une version opérationnelle nécessiterait l'utilisation de données réelles et actualisées.

Le parcours devient ainsi :

Victime
   ↓
Examen médical nécessaire ?
   │
   ├── OUI → établissement de santé conventionné le plus proche
   │                         ↓
   └── NON ──────────────────┤
                             ↓
                 recherche d'hébergement
                             ↓
              filtrage des incompatibilités
                             ↓
                 solutions compatibles

# Évolutions envisagées:

Une évolution ultérieure pourrait intégrer les données issues de l'évaluation du danger réalisée lors du dépôt de plainte, afin d'affiner les critères d'orientation. Les hébergements compatibles pourraient également être classés selon plusieurs critères pondérés, notamment la distance, les modalités de transport et les facteurs de sécurité. Le prototype pourrait enfin être connecté à des données réelles et actualisées concernant les capacités d'hébergement.

Dans cette première version, un hébergement est donc écarté lorsqu'il n'a aucune place disponible, lorsqu'il ne peut pas accueillir l'enfant accompagnant la victime ou lorsqu'une prise en charge nocturne est nécessaire mais impossible.

Les contraintes relatives à la distance de sécurité ne sont pas encore implémentées : les règles applicables doivent être vérifiées avant leur intégration au modèle.

