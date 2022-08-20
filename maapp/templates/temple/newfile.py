import pyrebase

config = {
    "apiKey": "AIzaSyCOld5rYqF6uE9iXO8tNdE-PUcRVrsIVEU",
    "authDomain": "teste-c3fba.firebaseapp.com",
    "databaseURL": "https://teste-c3fba-default-rtdb.firebaseio.com",
    "projectId": "teste-c3fba",
    "storageBucket": "teste-c3fba.appspot.com",
    "messagingSenderId": "1080131592865",
    "appId": "1:1080131592865:web:655c3752e9765500ce06e0",
    "measurementId": "G-YLWSX8DVM0",
    "serviceAccount": "serviceAccount.json"
}

firebase = pyrebase.initialize_app(config)