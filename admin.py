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

# creating json file
result = df.to_json(orient='records')

parsed = loads(result)
dumps(parsed)

db = authentication.init_db()

# deleting everything from firebase
docs = db.collection('video_games').list_documents()
for doc in docs:
    doc.delete()

# adding eveythign back to firebase
for i in parsed:
    db.collection('video_games').document(str(i['Rank'])).set(i)

# displaying json file
print(dumps(parsed))