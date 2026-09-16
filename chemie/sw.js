/* Neon Elementen - offline cache */
var CACHE = "neon-elementen-v3";
var ASSETS = ["./", "./index.html", "./manifest.webmanifest", "./icon-180.png", "./icon-512.png"];

self.addEventListener("install", function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(ASSETS); }).then(function () { return self.skipWaiting(); }));
});

self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.map(function (k) { return k === CACHE ? null : caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

self.addEventListener("fetch", function (e) {
  if (e.request.method !== "GET") return;

  /* De pagina zelf: eerst het netwerk proberen, zodat een nieuwe versie meteen
     doorkomt. Lukt dat niet (offline), dan de opgeslagen versie tonen. */
  if (e.request.mode === "navigate") {
    e.respondWith(
      fetch(e.request).then(function (res) {
        var copy = res.clone();
        caches.open(CACHE).then(function (c) { c.put("./index.html", copy); }).catch(function () {});
        return res;
      }).catch(function () {
        return caches.match("./index.html").then(function (hit) { return hit || caches.match("./"); });
      })
    );
    return;
  }

  /* Alle overige bestanden (icoon, lettertypes): eerst uit de cache, dat is sneller. */
  e.respondWith(
    caches.match(e.request).then(function (hit) {
      if (hit) return hit;
      return fetch(e.request).then(function (res) {
        var copy = res.clone();
        caches.open(CACHE).then(function (c) { c.put(e.request, copy); }).catch(function () {});
        return res;
      });
    })
  );
});
