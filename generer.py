# -*- coding: utf-8 -*-
"""Génère les pages légales HTML depuis poussededans/_contenu.py.

Usage : python generer.py

Pourquoi générer plutôt qu'écrire 10 fichiers à la main : deux documents
en cinq langues, c'est dix pages qui doivent rester structurellement
identiques. Écrites séparément, elles divergent — une langue garde une
vieille date, une autre perd une section ajoutée ailleurs. Ici la
structure est unique et seul le texte varie.

Les .html produits SONT committés (GitHub Pages sert des fichiers
statiques, il n'exécute rien) : ce script est la source, pas une étape
de build côté serveur.
"""
import io
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'poussededans'))
import _contenu as C  # noqa: E402

GABARIT = """<!DOCTYPE html>
<html lang="{langue}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titre} — {app}</title>
<style>
  body {{ font-family: -apple-system, Segoe UI, Roboto, Arial, sans-serif; max-width: 720px; margin: 40px auto; padding: 0 16px; line-height: 1.6; color: #222; }}
  h1 {{ font-size: 1.6em; margin-bottom: 0.2em; }}
  h2 {{ font-size: 1.2em; margin-top: 1.8em; border-bottom: 1px solid #ddd; padding-bottom: 4px; }}
  .maj {{ color: #666; font-size: 0.9em; margin-top: 0; }}
  .important {{ background: #fff3cd; border-left: 4px solid #e0a800; padding: 12px 16px; margin: 1.2em 0; }}
  a {{ color: #2e7d32; }}
  nav {{ margin-bottom: 2em; font-size: 0.9em; }}
  nav a {{ margin-right: 16px; }}
  footer {{ margin-top: 3em; font-size: 0.85em; color: #888; border-top: 1px solid #eee; padding-top: 16px; }}
</style>
</head>
<body>

<nav><a href="../../">{retour}</a><a href="{autre_fichier}">{autre_libelle}</a></nav>

<h1>{titre}</h1>
<p class="maj">{libelle_maj} : {maj}</p>

<p>{intro}</p>

{corps}

<footer>{app} — {editeur}</footer>
</body>
</html>
"""


def rendre(doc, langue, fichier_courant, autre_fichier, autre_libelle):
    """Une section dont le titre commence par '!' devient un encadré
    d'avertissement sans titre (les mises en garde légales se lisent mieux
    en bloc mis en valeur qu'en section numérotée parmi d'autres)."""
    morceaux = []
    numero = 0
    for titre, corps in doc["sections"]:
        if titre.startswith("!"):
            morceaux.append('<div class="important">{}</div>'.format(corps))
        else:
            numero += 1
            morceaux.append("<h2>{}. {}</h2>\n{}".format(numero, titre, corps))
    return GABARIT.format(
        langue=langue,
        app=C.APP,
        editeur=C.EDITEUR,
        titre=doc["titre"],
        intro=doc["intro"],
        maj=C.MAJ,
        libelle_maj=C.NAV[langue]["maj"],
        retour=C.NAV[langue]["retour"],
        autre_fichier=autre_fichier,
        autre_libelle=autre_libelle,
        corps="\n\n".join(morceaux),
    )


def main():
    racine = os.path.dirname(os.path.abspath(__file__))
    ecrits = []
    for langue in C.LANGUES:
        dossier = os.path.join(racine, "poussededans", langue)
        os.makedirs(dossier, exist_ok=True)

        pages = [
            ("politique-confidentialite.html", C.CONFIDENTIALITE[langue],
             "conditions-utilisation.html", C.NAV[langue]["autre"]),
            ("conditions-utilisation.html", C.CONDITIONS[langue],
             "politique-confidentialite.html", C.NAV_AUTRE_CONF[langue]),
        ]
        for fichier, doc, autre_fichier, autre_libelle in pages:
            chemin = os.path.join(dossier, fichier)
            io.open(chemin, "w", encoding="utf-8").write(
                rendre(doc, langue, fichier, autre_fichier, autre_libelle)
            )
            ecrits.append(os.path.relpath(chemin, racine).replace(os.sep, "/"))

    for f in ecrits:
        print("  " + f)
    print("{} pages generees".format(len(ecrits)))


if __name__ == "__main__":
    main()
