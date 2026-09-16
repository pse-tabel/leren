/* Leren Neglet - offline cache voor de startpagina.
   Belangrijk: deze service worker blijft van de submappen af. Elk vak heeft
   zijn eigen sw.js met een eigen cache; als deze de submappen ook zou
   afhandelen, zou de startpagina onder hun sleutel belanden. */
var CACHE = "leren-neglet-v1";
var ASSETS = ["./", "./index.html", "./manifest.webmanifest", "./icon-180.png", "./icon-512.png"];

function eigenPagina(url) {
  var basis = new URL(self.registration.scope).pathname;
  var pad = new URL(url).pathname;
  return pad === basis || pad === basis + "index.html";
}

self.addEventListener("install", function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(ASSETS); })
    .then(function () { return self.skipWaiting(); }));
});

self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.map(function (k) { return k === CACHE ? null : caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

self.addEventListener("fetch", function (e) {
  if (e.request.method !== "GET") return;

  if (e.request.mode === "navigate") {
    if (!eigenPagina(e.request.url)) return;      /* submap: niet aanraken */
    e.respondWith(fetch(e.request).then(function (res) {
      var copy = res.clone();
      caches.open(CACHE).then(function (c) { c.put("./index.html", copy); }).catch(function () {});
      return res;
    }).catch(function () {
      return caches.match("./index.html").then(function (hit) { return hit || caches.match("./"); });
    }));
    return;
  }

  e.respondWith(caches.match(e.request).then(function (hit) {
    if (hit) return hit;
    return fetch(e.request).then(function (res) {
      var copy = res.clone();
      caches.open(CACHE).then(function (c) { c.put(e.request, copy); }).catch(function () {});
      return res;
    });
  }));
});
