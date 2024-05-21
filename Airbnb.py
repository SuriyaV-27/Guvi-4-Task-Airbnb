import pymongo
import pandas as pd

mongo_uri = "mongodb+srv://suriyav:Suriya27@cluster0.us35cad.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_uri)

db = client.Airbnb_data
collection = db.Airbnb

neighborhood = "Downtown"
query = {"neighbourhood": neighborhood}
results = collection.find(query)

cleaned_data = []

for listing in results:
    try:
        price = listing['price']
    except KeyError:
        price = None    

    cleaned_data.append({
        'price': price,
    })

df = pd.DataFrame(cleaned_data)

df['price'].fillna(0, inplace=True)  

df.drop_duplicates(subset='name', inplace=True)

df['price'] = df['price'].astype(float)

print(df.head())
