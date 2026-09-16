# -*- coding: utf-8 -*-
"""Zet de gebouwde apps in de studie-map.

Elk vak staat in zijn eigen bronmap; dit script kopieert alleen wat online
hoort. Een vak bijzetten: voeg een regel toe aan VAKKEN en zet de map erbij
in index.html.
"""
import io, os, re, shutil, datetime

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

MAANDEN = ["januari", "februari", "maart", "april", "mei", "juni", "juli",
           "augustus", "september", "oktober", "november", "december"]
NU = datetime.datetime.now()
STEMPEL = "%d %s %d · %02d:%02d" % (NU.day, MAANDEN[NU.month - 1], NU.year,
                                          NU.hour, NU.minute)


def stempel_erin(pad):
    """Zet de datum van nu in de 'laatst bijgewerkt'-regel onderaan de pagina."""
    tekst = io.open(pad, encoding="utf-8", newline="").read()
    nieuw, aantal = re.subn(r"(<b data-bijgewerkt>)[^<]*(</b>)",
                            r"\g<1>" + STEMPEL + r"\g<2>", tekst)
    if aantal:
        io.open(pad, "w", encoding="utf-8", newline="").write(nieuw)
    return aantal


for map_naam, bronmap in VAKKEN:
    doel = os.path.join(HIER, map_naam)
    os.makedirs(doel, exist_ok=True)
    print("%s  <-  %s" % (map_naam, bronmap))
    for naam in BESTANDEN:
        van = os.path.join(bronmap, naam)
        if not os.path.exists(van):
            print("   ONTBREEKT: " + naam)
            continue
        naar = os.path.join(doel, naam)
        shutil.copy2(van, naar)
        extra = ""
        if naam == "index.html":
            extra = "  (datum gezet)" if stempel_erin(naar) else "  (GEEN datumregel)"
        print("   %-24s %7d bytes%s" % (naam, os.path.getsize(naar), extra))

if stempel_erin(os.path.join(HIER, "index.html")):
    print("\nhoofdmenu: datum gezet op %s" % STEMPEL)

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
