# Pack Exos Jour 1 - Clean Code Java

Ce dossier remplace les exercices Jour 1 trop légers par un pack autonome,
plus complet et directement exploitable en formation.

Tous les scénarios sont fictifs. Ils servent uniquement à l'apprentissage du
Clean Code Java dans un contexte DSI assurance / protection sociale. Ils ne
décrivent aucune règle interne, aucune donnée réelle et aucune architecture
réelle PRO BTP.

## Organisation

- `01_exercices/` : fiches à donner aux apprenants.
- `02_corriges/` : corrigés détaillés pour le formateur, avec tests, code final,
  critères de réussite et variantes.
- `03_outils_pedagogiques/` : grilles, checklists, lexique, aide TDD et guide
  de revue pour accompagner les élèves pendant les exercices.

## Progression pédagogique proposée

| Moment | Fiche | Intention |
|---|---|---|
| 09:00-09:30 | `00_MODE_EMPLOI_JOUR_1.md` | Cadrage, règles de travail, prudence métier |
| 11:00-12:00 | `EX-J1-01_CONTRAT_COLLECTIF_ACTIF.md` | Lire, nommer, extraire un objet de valeur |
| 13:30-14:45 | `EX-J1-02_TDD_REMBOURSEMENT_SANTE.md` | Ecrire des tests AAA et pratiquer TDD |
| 14:45-15:30 | `EX-J1-03_COTISATION_PMSS.md` | Eviter PMSS/BRSS, nommer des seuils et constantes |
| 15:45-16:30 | `EX-J1-04_RESTE_A_CHARGE.md` | Refactorer une méthode longue sans changer le comportement |
| 16:30-17:00 | `EX-J1-05_REVUE_CODE_SANTE.md` | Mener une revue courte, actionnable, reliée au risque métier |

## Pré-requis techniques suggérés

- Java 17 ou plus.
- JUnit 5.
- Aucun framework métier.
- Pas de Spring dans ces exercices : l'objectif Jour 1 est le coeur Java,
  le nommage, les tests et le refactoring progressif.

## Comment utiliser ce pack

Pour un groupe débutant en Clean Code, ne distribuer pas seulement l'énoncé.
Distribuer aussi :

- `03_outils_pedagogiques/01_GRILLE_LECTURE_CODE.md` avant le premier exercice ;
- `03_outils_pedagogiques/02_MEMO_TESTS_JUNIT_TDD.md` avant l'exercice TDD ;
- `03_outils_pedagogiques/03_CHECKLIST_REFACTORING.md` avant les exercices 3 et 4 ;
- `03_outils_pedagogiques/04_GUIDE_REVUE_CODE.md` avant l'exercice 5 ;
- `03_outils_pedagogiques/05_GLOSSAIRE_JOUR_1.md` en support permanent.

Le formateur peut utiliser les corrigés comme script d'animation : chaque
corrigé contient maintenant les étapes de facilitation, les indices à donner
sans révéler la solution et les critères de correction.
