const CACHE_NAME = 'son-vu-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/cam-nang/ban-tho-go-gu-cao-cap.html',
  '/cam-nang/van-khan.html'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => response || fetch(event.request))
  );
});
