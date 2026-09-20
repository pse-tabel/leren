# -*- coding: utf-8 -*-
"""Het themasysteem van Leren Neglet.

Elke app deelt negen neutrale kleuren (--ink tot --muted2) en heeft daarnaast
zijn eigen accenten: Frans gebruikt --voc/--gram/--werkw/--zin, chemie --cyan en
--paars, Duits --goud. Een thema herschrijft allebei, dus het uiterlijk
verandert echt en niet alleen de achtergrond.

Twee dingen blijven met rust, omdat hun kleur betekenis draagt en niet bij de
smaak van een thema hoort:
  · der / die / das in Duits — de kleuren uit de les
  · --pos en --neg in chemie — positief en negatief oxidatiegetal

De keuze staat in localStorage onder één sleutel. Alle apps staan in dezelfde
map (…/leren/) en delen die opslag, dus een thema kiezen in Frans verandert ook
chemie en het hoofdmenu.

bouw_alles.py roept zet_erin() aan voor elke pagina die het kopieert.
"""

# Welke accentnaam in welke app hetzelfde vakje is.
ALIAS = {
    "prim": ["hub", "cyan", "voc", "metaal", "goud", "vak1"],
    "twee": ["paars", "gram", "nietmetaal", "vak2"],
    "drie": ["werkw", "edelgas", "vak3"],
    "vier": ["zin"],
    "ok": ["ok"],
    "bad": ["bad"],
}

NEUTRAAL = ["ink", "ink2", "surface", "surface2", "line", "line2",
            "text", "muted", "muted2"]

THEMAS = [
    dict(id="standaard", naam="Neon", uitleg="zoals de app bedoeld is",
         licht=False, bol="#0b0d18", stip="#b9c3ff", kleuren=None),

    dict(id="synthwave", naam="Synthwave", uitleg="neon roze en cyaan op paars",
         licht=False, bol="#0d0420", stip="#ff2e97", kleuren=dict(
             ink="#0d0420", ink2="#140a2e", surface="#1c1040", surface2="#241553",
             line="#33206b", line2="#4a2f91",
             text="#f7e9ff", muted="#b49ad6", muted2="#7f6aa3",
             prim="#ff2e97", twee="#b14bff", drie="#23e0ff", vier="#ffd23f",
             ok="#2bf5a0", bad="#ff3b5c")),

    dict(id="neonijs", naam="Neon ijs", uitleg="fel cyaan op diepblauw",
         licht=False, bol="#020813", stip="#22e6ff", kleuren=dict(
             ink="#020813", ink2="#05101f", surface="#0a1a2e", surface2="#0f2340",
             line="#163455", line2="#204a78",
             text="#e6f6ff", muted="#86b6d6", muted2="#5d859f",
             prim="#22e6ff", twee="#63b3ff", drie="#9df0ff", vier="#c6a8ff",
             ok="#3df5c0", bad="#ff5c7a")),

    dict(id="gifgroen", naam="Gifgroen", uitleg="fel limoen op zwart",
         licht=False, bol="#060a04", stip="#aaff1a", kleuren=dict(
             ink="#060a04", ink2="#0b1207", surface="#111c0c", surface2="#182611",
             line="#21351a", line2="#304c26",
             text="#eaffd9", muted="#9dc27e", muted2="#6d8c56",
             prim="#aaff1a", twee="#4fe3ff", drie="#ffe83d", vier="#c77dff",
             ok="#3dff88", bad="#ff4d4d")),

    dict(id="magenta", naam="Magenta", uitleg="neon roze en violet",
         licht=False, bol="#0f0413", stip="#ff3df0", kleuren=dict(
             ink="#0f0413", ink2="#17081d", surface="#200c2a", surface2="#2a1136",
             line="#3a1a4a", line2="#532768",
             text="#ffe9fb", muted="#c898d6", muted2="#8f6b9d",
             prim="#ff3df0", twee="#a24bff", drie="#ff8ac0", vier="#63e8ff",
             ok="#38f5b0", bad="#ff4f6e")),

    dict(id="vuur", naam="Vuur", uitleg="neon oranje en rood",
         licht=False, bol="#120503", stip="#ff6a1a", kleuren=dict(
             ink="#120503", ink2="#1a0906", surface="#260d08", surface2="#32120c",
             line="#451a12", line2="#62281b",
             text="#ffece2", muted="#d1a091", muted2="#9c7365",
             prim="#ff6a1a", twee="#ff3d9e", drie="#ffc53d", vier="#ffa06b",
             ok="#4ade80", bad="#ff2e2e")),

    dict(id="terminal", naam="Terminal", uitleg="zwart met groen, zoals een shell",
         licht=False, bol="#000000", stip="#39ff5f", kleuren=dict(
             ink="#000000", ink2="#050a05", surface="#0a120a", surface2="#0f1a0f",
             line="#1b2e1b", line2="#2c452c",
             text="#b9ffb9", muted="#5fa85f", muted2="#3d6f3d",
             prim="#39ff5f", twee="#8affa8", drie="#00e6c3", vier="#c8ff3f",
             ok="#00ffa0", bad="#ff5f56")),

    # ---- vanaf hier zonder gloed: gewone kleuren, geen neon ----

    dict(id="middernacht", naam="Middernacht", uitleg="diep zwart, rustig",
         licht=False, bol="#000000", stip="#8ab4ff", kleuren=dict(
             ink="#000000", ink2="#0a0a0c", surface="#131317", surface2="#1a1b20",
             line="#27272e", line2="#3b3b46",
             text="#ededf1", muted="#8f8f99", muted2="#62626d",
             prim="#8ab4ff", twee="#c79bff", drie="#6fe3c4", vier="#ffb86b",
             ok="#4ade80", bad="#ff6b6b")),

    dict(id="leisteen", naam="Leisteen", uitleg="donkergrijs, gedempte kleuren",
         licht=False, bol="#14171c", stip="#6f9bc9", kleuren=dict(
             ink="#14171c", ink2="#191d24", surface="#21262f", surface2="#29303a",
             line="#343c48", line2="#47515f",
             text="#e4e8ee", muted="#97a1af", muted2="#6c7683",
             prim="#6f9bc9", twee="#a08cc0", drie="#79b09a", vier="#c9a37a",
             ok="#6aab7e", bad="#cc7b7b")),

    dict(id="indigo", naam="Indigo", uitleg="licht en strak, blauwpaars",
         licht=True, bol="#f6f7fb", stip="#4255ff", kleuren=dict(
             ink="#f6f7fb", ink2="#eceef6", surface="#ffffff", surface2="#fafbfd",
             line="#dde1ed", line2="#bfc7db",
             text="#0a092d", muted="#565f7e", muted2="#7c86a0",
             prim="#4255ff", twee="#9333ea", drie="#0d9488", vier="#db2777",
             ok="#15a163", bad="#dc2626")),

    dict(id="indigonacht", naam="Indigo nacht", uitleg="hetzelfde, maar donker",
         licht=False, bol="#0a092d", stip="#6b7bff", kleuren=dict(
             ink="#0a092d", ink2="#111038", surface="#1a1947", surface2="#232159",
             line="#2f2d6b", line2="#423f8c",
             text="#f2f3fb", muted="#a2a5cc", muted2="#7477a3",
             prim="#6b7bff", twee="#b566ff", drie="#22d3c5", vier="#ff6fae",
             ok="#34d399", bad="#ff5a5a")),

    dict(id="mist", naam="Mist", uitleg="licht grijsblauw, heel rustig",
         licht=True, bol="#eef1f4", stip="#3f6d99", kleuren=dict(
             ink="#eef1f4", ink2="#e5e9ee", surface="#ffffff", surface2="#f7f9fb",
             line="#d7dde4", line2="#b6c0cb",
             text="#1f242b", muted="#5d6773", muted2="#838e9b",
             prim="#3f6d99", twee="#7a5f9e", drie="#3f8a72", vier="#9a6b3a",
             ok="#2f7d52", bad="#b04242")),

    dict(id="grasgroen", naam="Grasgroen", uitleg="licht en vrolijk, groen",
         licht=True, bol="#ffffff", stip="#58cc02", kleuren=dict(
             ink="#ffffff", ink2="#f7f7f7", surface="#ffffff", surface2="#fbfbfb",
             line="#e5e5e5", line2="#cfcfcf",
             text="#3c3c3c", muted="#777777", muted2="#a3a3a3",
             prim="#58a700", twee="#1899d6", drie="#8549ba", vier="#e07b00",
             ok="#17803d", bad="#ea2b2b")),

    dict(id="notitieblok", naam="Notitieblok", uitleg="papier met balpen",
         licht=True, bol="#f7f3e8", stip="#2d5bd7", kleuren=dict(
             ink="#f7f3e8", ink2="#efe9da", surface="#fffdf7", surface2="#f8f4ea",
             line="#ded5c0", line2="#bfb49b",
             text="#2b2a26", muted="#6d6659", muted2="#938a78",
             prim="#2d5bd7", twee="#8e44ad", drie="#0e7490", vier="#b7791f",
             ok="#1f7a4d", bad="#c0392b")),

    dict(id="sepia", naam="Sepia", uitleg="oud papier, gedempt warm",
         licht=True, bol="#ece3d6", stip="#96591f", kleuren=dict(
             ink="#ece3d6", ink2="#e3d8c7", surface="#f7f1e6", surface2="#efe7d9",
             line="#d4c7b0", line2="#b6a68b",
             text="#2f2920", muted="#6f6350", muted2="#948570",
             prim="#96591f", twee="#7d4f6b", drie="#3f6b63", vier="#8a6f2c",
             ok="#4a7a4a", bad="#a8452f")),

    dict(id="zonsopgang", naam="Zonsopgang", uitleg="warm licht, oranje",
         licht=True, bol="#fff6ee", stip="#e2571d", kleuren=dict(
             ink="#fff6ee", ink2="#fbe9da", surface="#ffffff", surface2="#fffaf5",
             line="#f0dbc8", line2="#d8bda4",
             text="#2a1f18", muted="#7a6455", muted2="#a08b79",
             prim="#d24d14", twee="#b02a5f", drie="#0f7b8a", vier="#8a5cd6",
             ok="#157f4f", bad="#c0281e")),

]

# Bij deze thema's hoort de neongloed: de waas achter de pagina, de halo's om
# knoppen en merken, en de lichtrand om grote woorden. Alle andere thema's
# krijgen gewone kleuren zonder die gloed — zie RUSTIG_CSS.
MET_GLOED = {"standaard", "synthwave", "neonijs", "gifgroen", "magenta",
             "vuur", "terminal"}

# De plekken waar in de apps een neonhalo of lichtrand staat.
HALO = [".mark", ".mark.tijdelijk", ".mark:hover", ".merk", ".bar", ".btn.pri",
        ".btn.ok", ".btn.bad", ".kklaar", ".knoop.nu", ".kroontjes i.aan",
        ".legend i", '.chip[aria-pressed="true"]', '.gear[aria-expanded="true"]',
        '.tab[aria-selected="true"]', ".mt.sel", ".opt.good", ".score",
        ".install", "input[type=text]:focus"]
LICHTRAND = [".sym", ".nm", ".woord", ".done h2"]


def rustig_css(kies):
    """Haalt de neongloed weg: de waas, de halo's en de lichtrand om tekst."""
    regels = ["%s .glow{display:none}" % kies,
              "%s .grid-bg{opacity:.12}" % kies]
    regels.append(",\n".join("%s %s" % (kies, s) for s in LICHTRAND)
                  + "{text-shadow:none}")
    regels.append(",\n".join("%s %s" % (kies, s) for s in HALO)
                  + "{box-shadow:none}")
    return "\n".join(regels)


BALK_CSS = """
.themabalk{position:relative; z-index:1; max-width:760px; margin:0 auto;
  padding:18px 20px 4px; display:flex; flex-wrap:wrap; align-items:center;
  justify-content:center; gap:9px}
.themabalk .tlabel{font-family:var(--fm); font-size:10px; letter-spacing:.16em;
  text-transform:uppercase; color:var(--muted2); margin-right:3px}
.themaknop{width:28px; height:28px; padding:0; border-radius:50%; cursor:pointer;
  border:1px solid var(--line2); position:relative; overflow:hidden;
  transition:transform .16s ease; background:var(--tb)}
.themaknop::after{content:""; position:absolute; inset:0;
  background:linear-gradient(135deg,var(--ts) 0 48%,transparent 48%)}
.themaknop:hover{transform:scale(1.12)}
.themaknop[aria-pressed="true"]{outline:2px solid var(--text); outline-offset:2px}
.themaknop:focus-visible{outline:2px solid var(--text); outline-offset:2px}
.tsplit{width:1px; height:20px; background:var(--line2); opacity:.7; margin:0 2px}
.themanaam{font-family:var(--fm); font-size:10px; letter-spacing:.1em;
  text-transform:uppercase; color:var(--muted); min-width:104px; text-align:center}
.themabalk.inline{max-width:none; margin:0; padding:0; justify-content:flex-start;
  gap:10px}
.themabalk.inline .themanaam{min-width:0; margin-left:2px; text-align:left}
@media print{.themabalk{display:none}}"""


def css():
    regels = ["/* de thema's van de site: neutralen en accenten in één keer */"]
    for t in THEMAS:
        if not t["kleuren"]:
            continue
        k = t["kleuren"]
        kies = ':root[data-thema="%s"]' % t["id"]
        deel = ["  color-scheme:%s;" % ("light" if t["licht"] else "dark")]
        for naam in NEUTRAAL:
            deel.append("  --%s:%s;" % (naam, k[naam]))
        for vak, namen in ALIAS.items():
            for naam in namen:
                deel.append("  --%s:%s;" % (naam, k[vak]))
        regels.append("%s{\n%s\n}" % (kies, "\n".join(deel)))
        regels.append("%s body{background:var(--ink); color:var(--text)}" % kies)
        if t["id"] not in MET_GLOED:
            regels.append(rustig_css(kies))
    regels.append(BALK_CSS)
    return "\n".join(regels) + "\n"


def vroeg_script():
    """In de <head>, zodat de pagina nooit even in het verkeerde thema flitst."""
    return """<script>
/* Het thema staat in localStorage; alle apps op deze map delen die opslag. */
(function(){
  try{
    var t=localStorage.getItem("leren-thema");
    if(t&&t!=="standaard")document.documentElement.setAttribute("data-thema",t);
  }catch(e){}
})();
</script>
"""


def balk(inline=False):
    knoppen = []
    vorige = None
    for t in THEMAS:
        nu = t["id"] in MET_GLOED
        if vorige is not None and nu != vorige:
            knoppen.append('    <span class="tsplit" aria-hidden="true"></span>')
        vorige = nu
        knoppen.append(
            '    <button class="themaknop" type="button" data-thema="%s" '
            'style="--tb:%s; --ts:%s" title="%s — %s" aria-label="Thema %s">'
            "</button>"
            % (t["id"], t["bol"], t["stip"], t["naam"], t["uitleg"], t["naam"]))
    klasse = "themabalk inline" if inline else "themabalk"
    label = "" if inline else '    <span class="tlabel">Thema</span>\n'
    return ('<div class="%s" id="themabalk">\n' % klasse
            + label
            + "\n".join(knoppen) + "\n"
            '    <span class="themanaam" id="themanaam"></span>\n'
            "  </div>\n")


def script():
    namen = ", ".join('"%s":"%s"' % (t["id"], t["naam"]) for t in THEMAS)
    return """<script>
/* ---------- themakiezer ---------- */
(function(){
  var NAMEN={%s};
  var balk=document.getElementById("themabalk");
  if(!balk)return;
  var knoppen=[].slice.call(balk.querySelectorAll(".themaknop"));
  var naamvak=document.getElementById("themanaam");

  function huidig(){
    try{return localStorage.getItem("leren-thema")||"standaard"}catch(e){return "standaard"}
  }
  function toon(t){
    if(t==="standaard")document.documentElement.removeAttribute("data-thema");
    else document.documentElement.setAttribute("data-thema",t);
    var meta=document.querySelector('meta[name="theme-color"]');
    if(meta){
      var kleur=getComputedStyle(document.documentElement)
        .getPropertyValue("--ink").trim();
      if(kleur)meta.setAttribute("content",kleur);
    }
    knoppen.forEach(function(b){
      b.setAttribute("aria-pressed",String(b.dataset.thema===t));
    });
    if(naamvak)naamvak.textContent=NAMEN[t]||"";
  }
  function kies(t){
    try{localStorage.setItem("leren-thema",t)}catch(e){}
    toon(t);
  }
  knoppen.forEach(function(b){
    b.addEventListener("click",function(){kies(b.dataset.thema)});
  });
  /* een andere tab of app in dezelfde map heeft het thema gewijzigd */
  window.addEventListener("storage",function(e){
    if(e.key==="leren-thema")toon(huidig());
  });
  toon(huidig());
})();
</script>
""" % namen


MERKEN = [("/*thema-css-start*/", "/*thema-css-eind*/"),
          ("<!--thema-kop-start-->", "<!--thema-kop-eind-->"),
          ("<!--thema-balk-start-->", "<!--thema-balk-eind-->"),
          ("<!--thema-js-start-->", "<!--thema-js-eind-->")]


def schoon(tekst):
    """Haalt een eerder gezet themablok er weer uit, zodat opnieuw bouwen mag."""
    for open_merk, sluit_merk in MERKEN:
        while open_merk in tekst and sluit_merk in tekst:
            a = tekst.index(open_merk)
            b = tekst.index(sluit_merk, a) + len(sluit_merk)
            while b < len(tekst) and tekst[b] in "\r\n":
                b += 1
            tekst = tekst[:a] + tekst[b:]
    return tekst


def zet_erin(pad):
    """Zet de kleuren, het vroege script, de balk en de kiezer in één pagina.

    De balk gaat naar de plek waar je hem zoekt: in het instellingenpaneel als
    de app er een heeft, anders onderaan bij de voet.
    """
    import io
    tekst = schoon(io.open(pad, encoding="utf-8", newline="").read())
    nl = "\r\n" if "\r\n" in tekst else "\n"

    def stuk(merk, inhoud):
        heel = merk[0] + "\n" + inhoud.strip("\n") + "\n" + merk[1] + "\n"
        return heel.replace("\n", nl)

    snee = tekst.rindex("</style>")
    tekst = tekst[:snee] + stuk(MERKEN[0], css()) + tekst[snee:]

    snee = tekst.index("</head>")
    tekst = tekst[:snee] + stuk(MERKEN[1], vroeg_script()) + tekst[snee:]

    paneel = '<div class="panel" id="panel" hidden>'
    voetregel = '<p class="bijwerk">'
    losse_voet = '<div class="bijwerkvoet"'
    if paneel in tekst:
        snee = tekst.index(paneel) + len(paneel)
        blok = ('\n  <div class="fset">\n'
                '    <span class="flabel">Thema van de site</span>\n  '
                + balk(inline=True).rstrip("\n") + "\n  </div>\n")
        plek = "instellingen"
    elif voetregel in tekst:
        snee = tekst.index(voetregel)
        blok = balk(inline=True)
        plek = "voet"
    else:
        snee = (tekst.index(losse_voet) if losse_voet in tekst
                else tekst.rindex("</body>"))
        blok = balk()
        plek = "onderaan"
    tekst = tekst[:snee] + stuk(MERKEN[2], blok) + tekst[snee:]

    snee = tekst.rindex("</body>")
    tekst = tekst[:snee] + stuk(MERKEN[3], script()) + tekst[snee:]

    io.open(pad, "w", encoding="utf-8", newline="").write(tekst)
    return plek
