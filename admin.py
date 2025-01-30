# CS 3050 Warmup Project
# Admin Program
# Load data from JSON file to datastore
import importlib
import pandas as pd
from json import loads, dumps
import authentication

# load the original CSV file
file_path = "vgsales.csv"
df = pd.read_csv(file_path)

# creating json file to store in firebase
result = df.to_json(orient='records')
parsed = loads(result)
dumps(parsed)

# calling the init_db function in authentication, which returns a reference to the data base
db = authentication.init_db()

# deleting everything from firebase
docs = db.collection('video_games').list_documents()
for doc in docs:
    doc.delete()

# adding everything back to firebase
for i in parsed:
    db.collection('video_games').document(str(i['Rank'])).set(i)

# # displaying json file
# print(dumps(parsed))