# CS 3050 Warmup Project
# Admin Program
# Load data from JSON file to datastore
import sys
import pandas as pd
from json import loads, dumps
import authentication

# loading the csv file from the command line and then reading the provided csv file
file_path = sys.argv[1]

# must be vgsales.csv file for program to work
if file_path == 'vgsales.csv':
    df = pd.read_csv(file_path)
    # making the year an int not a double
    df['year'] = df['year'].astype(int)

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
        db.collection('video_games').document(str(i['rank'])).set(i)
else:
    print("Incorrect file! Make sure you're entering vgsales.csv as your filename")



