var staticCacheName = 'djangopwa-v1';

self.addEventListener('install', function(event) {
event.waitUntil(
  caches.open(staticCacheName).then(function(cache) {
  return cache.addAll([
    'blogs/',
    '',
    'mentalhealthspecialists/',
  ]);
  })
);
});

self.addEventListener('fetch', function(event) {

    event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
    );
  });
