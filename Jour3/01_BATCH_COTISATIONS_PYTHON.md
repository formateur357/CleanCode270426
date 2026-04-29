# Exercice 1 - Batch de cotisations et rapport d'anomalies

Durée conseillée : 60 à 70 minutes.

## Objectif pédagogique

Transformer un batch Python fragile en traitement lisible, testable et utile
pour une équipe support. Vous devez éviter qu'une seule ligne invalide bloque
tout le lot, tout en produisant un rapport assez précis pour comprendre ce qui
s'est passé.

Vous allez travailler :

- la distinction entre anomalie de ligne et erreur globale ;
- le remplacement d'un `print` par un résultat métier exploitable ;
- le nommage des règles de calcul ;
- les tests pytest sur un traitement de lot ;
- un scénario BDD orienté gestion.

## Contexte métier fictif

L'antenne de Cagnes-sur-Mer reçoit chaque nuit un fichier simplifié de bases
mensuelles de cotisation prévoyance. Chaque ligne correspond à une déclaration
d'entreprise adhérente.

Le support ne veut pas seulement savoir le total. Il doit pouvoir répondre à
des questions concrètes :

- combien de lignes ont été lues ?
- combien de lignes ont été effectivement traitées ?
- quelles lignes ont été rejetées ?
- pourquoi une ligne a-t-elle été rejetée ?
- le lot a-t-il continué après une anomalie ?

Dans cet exercice, on ne manipule volontairement que la base de cotisation pour
garder un terrain de jeu court. Vous pouvez toutefois nommer vos variables comme
si elles venaient d'un vrai lot mensuel.

## Code de départ

```python
def process(bases):
    total = 0
    for base in bases:
        if base is None or base < 0:
            raise ValueError("bad line")
        total += base * 8 // 100
    print("total=", total)
    return total
```

Ce code fonctionne sur un cas heureux, mais il mélange tout :

- parcours du lot ;
- validation de ligne ;
- calcul de cotisation ;
- arrêt brutal ;
- affichage console ;
- retour trop pauvre.

## Risque à traiter

Une base invalide peut arrêter tout le batch de nuit. Les lignes valides
suivantes ne sont alors pas traitées, et le support ne sait pas quelles données
ont été perdues ou ignorées.

Formulez ce risque avec vos mots avant de coder.

## Règles métier fictives

- Une base absente produit une anomalie de ligne.
- Une base négative produit une anomalie de ligne distincte.
- Une base à `0` est valide et produit une cotisation à `0`.
- Les lignes valides restent traitées même si une autre ligne est invalide.
- Le taux fictif de cotisation est de 8 %.
- Le calcul utilise une valeur entière pour rester simple dans l'exercice.
- Le rapport contient au minimum :
  - le total de cotisation ;
  - le nombre de lignes lues ;
  - le nombre de lignes valides traitées ;
  - la liste des anomalies ;
  - pour chaque anomalie : numéro de ligne et raison métier.

## Données d'exemple

| Ligne | Base entrante | Résultat attendu |
|---:|---:|---|
| 1 | 1000 | cotisation 80 |
| 2 | -1 | anomalie `base negative` |
| 3 | 500 | cotisation 40 |
| 4 | 0 | cotisation 0 |
| 5 | absence | anomalie `base absente` |

Pour le lot `[1000, -1, 500]`, le comportement attendu est :

- total : `120` ;
- lignes lues : `3` ;
- lignes traitées : `2` ;
- anomalies : une anomalie sur la ligne 2.

## Contraintes de conception

- Ne gardez pas le résultat uniquement dans la console.
- Ne levez pas une exception globale pour une anomalie de ligne récupérable.
- Ne cachez pas une ligne invalide.
- N'introduisez pas de lecture CSV réelle.
- N'écrivez pas un framework de batch.
- Gardez une fonction de calcul unitaire facile à tester ou à comprendre.

## Consignes progressives

1. Copiez le code de départ dans un fichier de travail.
2. Écrivez un premier test qui prouve que le batch continue après une ligne
   invalide.
3. Vérifiez que ce test échoue avec le code initial.
4. Nommez le taux de cotisation.
5. Remplacez le `print` par un rapport retourné.
6. Ajoutez une représentation explicite d'une anomalie de ligne.
7. Séparez le calcul d'une ligne valide de l'orchestration du lot.
8. Ajoutez le cas de base absente.
9. Ajoutez le cas de base à `0`.
10. Rédigez un BDD et une remarque de review.

## Tests pytest attendus

Écrivez au moins ces tests, avec des noms proches :

- `test_batch_continue_apres_une_ligne_invalide`
- `test_batch_signale_une_base_absente`
- `test_base_zero_est_traitee_comme_valide`
- `test_lot_sans_anomalie_produit_un_rapport_sans_rejet`
- `test_rapport_distingue_lignes_lues_et_lignes_traitees`

Vous pouvez ajouter d'autres tests si cela vous aide, mais ne testez pas des
détails internes qui changeraient au premier renommage.

## Squelette possible, incomplet

Ce squelette sert à démarrer la réflexion. Il n'est pas une solution finale.

```python
from dataclasses import dataclass


CONTRIBUTION_RATE = 8


@dataclass
class LineAnomaly:
    line_number: int
    reason: str


@dataclass
class BatchReport:
    total_contribution: int
    read_lines: int
    processed_lines: int
    anomalies: list[LineAnomaly]


def process_contribution_batch(monthly_bases):
    raise NotImplementedError
```

Vous pouvez choisir une autre structure si vos tests restent lisibles.

## Déroulé guidé

### 0-8 min - Diagnostic

Répondez par écrit ou oralement :

- Quel comportement casse le plus fort ?
- Quelle information manque au support ?
- Quel nom du code initial est trop vague ?
- Quelle partie est un calcul pur ?

### 8-18 min - Premier test

Écrivez un test avec `[1000, -1, 500]`. Le test doit exprimer que :

- le total des lignes valides est conservé ;
- la ligne invalide est signalée ;
- le lot ne s'arrête pas.

### 18-32 min - Rapport minimal

Remplacez le retour `int` par un rapport. Ne cherchez pas encore la forme
parfaite : cherchez une forme testable.

### 32-45 min - Refactoring de nommage

Renommez ce qui reste trop technique :

- `process` ;
- `bases` si nécessaire ;
- `base` si le contexte devient ambigu ;
- `bad line`.

### 45-58 min - Cas limites

Ajoutez les cas :

- toutes les lignes sont valides ;
- base absente ;
- base à `0` ;
- plusieurs anomalies dans le même lot.

### 58-70 min - BDD, review, auto-évaluation

Rédigez votre scénario BDD et une remarque de review sur le code de départ.
Complétez ensuite l'auto-évaluation.

## BDD à rédiger

Complétez un scénario du type :

```gherkin
Scenario: le batch de cotisations continue malgré une ligne invalide
  Given ...
  When ...
  Then ...
  And ...
```

Votre scénario doit mentionner le résultat métier, pas le nom de vos fonctions.

## Indices progressifs

### Indice 1

Une anomalie de ligne est une donnée du rapport. Ce n'est pas forcément une
exception qui arrête tout.

### Indice 2

Le total seul est dangereux : il ne permet pas de savoir si une ligne a été
ignorée.

### Indice 3

Le numéro de ligne est souvent plus utile qu'un message long pour revenir au
fichier source.

### Indice 4

Une dataclass peut clarifier le rapport, mais elle ne remplacera pas une bonne
nomination des règles.

## Livrables

- Code Python refactoré.
- Tests pytest.
- Scénario BDD.
- Une remarque de review.
- Une courte note de limite, par exemple : "nous ne traitons pas encore les
  arrondis réglementaires ni le format CSV réel".

## Critères de réussite

- Le lot continue après une anomalie.
- Une ligne invalide est visible dans le rapport.
- Les lignes lues et traitées ne sont pas confondues.
- Le taux de 8 % est nommé.
- Le rapport est exploitable sans lire la console.
- Les noms `process`, `bad`, `x`, `res` ont disparu ou sont justifiés.

## Auto-évaluation

Cochez avant de passer à l'exercice suivant :

- Mon premier test échoue sur le code de départ.
- Je peux expliquer pourquoi une exception globale était un problème.
- Le rapport permet à un support de retrouver la ligne en erreur.
- Une base à `0` n'est pas traitée comme une anomalie.
- Je n'ai pas introduit de lecture de fichier inutile.
- Mon BDD est compréhensible sans connaître Python.

## Pièges fréquents

- Arrêter tout le batch à la première anomalie.
- Ignorer silencieusement la ligne invalide.
- Garder le rapport dans un `print`.
- Confondre lignes lues et lignes traitées.
- Mélanger le futur format CSV avec la règle métier.
- Appeler toutes les valeurs `data`.
- Construire une architecture trop lourde pour un batch aussi petit.
