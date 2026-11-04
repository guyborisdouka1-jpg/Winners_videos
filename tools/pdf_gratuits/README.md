# PDF gratuits « Commente INTÉRESSÉ » – Winners' English Center

Chaque jour, une publication Facebook (12 h 30, Africa/Abidjan, via Metricool, marque 7212387) propose un PDF gratuit.
Les gens commentent « INTÉRESSÉ » → une automatisation Meta Business Suite (réponse aux commentaires, globale) leur envoie
en privé le lien **winnersenglishcenter.com/cadeau**. Cette page lit `test/cadeau/pdfs.js` et affiche le PDF dont la date
est la plus récente ≤ aujourd'hui, + la bibliothèque des précédents. Le lien ne change jamais.

## Ajouter une semaine
1. Dans `content.py`, ajouter 7 entrées `D.append(dict(slug, date, title, sub, emoji, tip, p1, p2))` (formats variés :
   phrases, erreurs, vocabulaire, mini-leçon + exercice, dialogue, verbes, expressions, quiz…). **2 pages max**
   (p1 = page 1, p2 = page 2 ; l'encadré promo est ajouté automatiquement en bas de la page 2).
   Règles : prononciation écrite « à la française » (pas d'audio), noms/lieux uniquement du monde anglophone (jamais africains).
2. `python3 make.py` → `<slug>.pdf` (vérifier que rien ne déborde) ; puis
   `for s in …; do pdftoppm -r 80 -f 1 -l 1 -singlefile -jpeg $s.pdf cov-$s; done`
3. Ajouter les slugs dans le dict `B` de `vis.py` (titre, sous-titre, 4 puces) → `python3 vis.py` → `visuel-<slug>.jpg`.
4. Copier `<slug>.pdf`, `cov-<slug>.jpg` (renommé `<slug>.jpg`) et `visuel-<slug>.jpg` dans `test/cadeau/pdf/`
   **et** dans `cadeau/pdf/` de la branche `gh-pages` ; régénérer `pdfs.js` (window.PDFS = liste {slug,date,title,sub,emoji})
   dans les deux. Commit + push des deux branches.
5. Programmer les 7 publications Facebook (12 h 30, sans premier commentaire, texte en gras Unicode, signé Coach Winner,
   se terminant par « Commente « INTÉRESSÉ » … en privé 📩 »), image = https://winnersenglishcenter.com/cadeau/pdf/visuel-<slug>.jpg
