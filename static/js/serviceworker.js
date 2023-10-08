
var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    'static/images/logo.png',
    '/static/css/bootstrap.css',
    '/static/css/bootstrap.min.css',
    '/static/css/main.css',
    '/static/css/login.css',
    
];
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/');
            })
    )
});

self.addEventListener('beforeinstallprompt', (e) => {
    // Evita que el navegador muestre su propio mensaje
    e.preventDefault();

    // Muestra tu propio mensaje personalizado o un botón "Instalar" aquí
    // Puedes utilizar una notificación o una interfaz personalizada
    // e.userChoice.then(choiceResult => {
    //     if (choiceResult.outcome === 'dismissed') {
    //         console.log('El usuario canceló la instalación');
    //     } else {
    //         console.log('La aplicación se ha instalado');
    //     }
    // });
});