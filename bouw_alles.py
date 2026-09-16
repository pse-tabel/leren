# -*- coding: utf-8 -*-
"""Zet de gebouwde apps in de studie-map.

Elk vak staat in zijn eigen bronmap; dit script kopieert alleen wat online
hoort. Een vak bijzetten: voeg een regel toe aan VAKKEN en zet de map erbij
in index.html.
"""
import os, shutil

HIER = os.path.dirname(os.path.abspath(__file__))
BRON = os.path.dirname(HIER)

VAKKEN = [
    ("chemie",           os.path.join(BRON, "chemie-menu")),
    ("chemie/elementen", os.path.join(BRON, "neon-elementen")),
    ("chemie/toets",     os.path.join(BRON, "chemie-toets")),
    ("frans",            os.path.join(BRON, "frans")),
    ("duits",            os.path.join(BRON, "duits")),
]

BESTANDEN = ["index.html", "manifest.webmanifest", "sw.js", "icon-180.png", "icon-512.png"]

for map_naam, bronmap in VAKKEN:
    doel = os.path.join(HIER, map_naam)
    os.makedirs(doel, exist_ok=True)
    print("%s  <-  %s" % (map_naam, bronmap))
    for naam in BESTANDEN:
        van = os.path.join(bronmap, naam)
        if not os.path.exists(van):
            print("   ONTBREEKT: " + naam)
            continue
        shutil.copy2(van, os.path.join(doel, naam))
        print("   %-24s %7d bytes" % (naam, os.path.getsize(van)))

print("\nklaar. Wat online gaat:")
for pad, _, namen in os.walk(HIER):
    if "__pycache__" in pad:
        continue
    rel = os.path.relpath(pad, HIER)
    for n in sorted(namen):
        if n.endswith(".py"):
            continue
        p = os.path.join(pad, n)
        print("  %-34s %8d bytes" % (os.path.join("" if rel == "." else rel, n),
                                     os.path.getsize(p)))
