import pandas as pd
import sqlite3

# Read csv file.
df = pd.read_csv("44.7k_new.csv")
print(df.head(1))
# Connect to (create) database.
database = "db.sqlite3"
conn = sqlite3.connect(database)
dtype={
    "country" : "CharField",
    "description" : "TextField",
    "designation" : "CharField",
    "points" : "IntegerField",
    "price" : "IntegerField",
    "province" : "CharField",
    "taster_name" : "CharField",
    "title" : "CharField",
    "variety" : "CharField",
    "winery" : "CharField",
    "year" :"IntegerField",
    "grade" : "IntegerField"
}
df.to_sql(name='wine_data', con=conn, if_exists='replace', dtype=dtype, index=True, index_label="id")
conn.close()
print(df.head(2))