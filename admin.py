# CS 3050 Warmup Project
# Admin Program
# Load data from JSON file to datastore
import importlib
import pandas as pd
from json import loads, dumps

foobar = importlib.import_module("Database-Query-Program/authentication.py")

# load the original CSV file
file_path = "vgsales.csv"
df = pd.read_csv(file_path)

result = df.to_json(orient='records')

parsed = loads(result)
dumps(parsed)

print(dumps(parsed))