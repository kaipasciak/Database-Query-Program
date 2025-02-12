# CS 3050 Warmup Project
# Connection and Authentication for Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# This function returns a reference to the firestore client for use in other places in the application.
# It should only be called one time in the rest of the program.
def init_db():
    # Using the private key file generated on the firebase console
    cred = credentials.Certificate("vgsales_query_cli_private_key.json")
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db
