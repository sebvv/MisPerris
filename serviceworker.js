var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    'formulario/',
    'mascotas/',
    'listar-mascotas/',
    'eliminar-mascotas/<id>/',
    'modificar-mascotas/<id>/',
    '/static/core/css/Estilos.css',
    '/static/core/img/Apolo.jpg',
    '/static/core/img/Bigotes.jpg',
    '/static/core/img/Chocolate.jpg',
    '/static/core/img/crowfunding.jpg',
    '/static/core/img/Duque.jpg',
    '/static/core/img/logo.png',
    '/static/core/img/Luna.jpg',
    '/static/core/img/Maya.jpg',
    '/static/core/img/Oso.jpg',
    '/static/core/img/perro.png',
    '/static/core/img/Pexel.jpg',
    '/static/core/img/rescate.jpg',
    '/static/core/img/social-inst.png',
    '/static/core/img/social-twitter.png',
    '/static/core/img/socialfacebook.png',
    '/static/core/img/socialplus.png',
    '/static/core/img/Tom.jpg',
    '/static/core/img/Wifi.jpg',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.3.5/jquery.fancybox.min.css',
    'https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.3.5/jquery.fancybox.min.js',
    '/static/core/js/jquery.validate.min.js',
    '/static/core/js/validaciones.js',
    '/static/core/js/inicializacion.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/images/controls.png'
    

];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
            if(response) {
                return response;
            }

            return fetch(event.request);
        })
    );
});


importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var config = {
    apiKey: "AIzaSyDEaPMZ38uq2DwIhEpsOXDSRZ737XvsN1Q",
    authDomain: "automotora-43afc.firebaseapp.com",
    databaseURL: "https://automotora-43afc.firebaseio.com",
    projectId: "automotora-43afc",
    storageBucket: "automotora-43afc.appspot.com",
    messagingSenderId: "393993915876"
};
firebase.initializeApp(config);

const messaging = firebase.messaging();

//programamos una funcion que estara escuchando cuando llegue una
//notificacion desde firebase

messaging.setBackgroundMessageHandler(function(payload) {

    //el payload contendrá el mensaje destinado al usuario
    var title = "notificacion"
    var options = {
        body:"este es el cuerpo del mensaje"
    }

    //mostramos la notificacion al usuario
    return self.registration.showNotification(title, options);

})
