# -*- converter to Sqlite -*-

import sqlite3
import pandas as pd
import src.cl as cl
import os

config = {
    "file_csv": "../data/data.csv",
    "outfile": "../data/data.db"
}

def convert():

    print(cl.yellow + "•" + cl.reset + " From File: " + cl.blue + config["file_csv"])
    print(cl.yellow + "•" + cl.reset + " Converting CSV to SQLite...")

    if not os.path.exists(config['file_csv']):
        print(cl.red + "•" + cl.reset + f"Missing {config["file_csv"]}")
        print(os.path.abspath(config["file_csv"]))
    else:
        conn = sqlite3.connect(config["outfile"])
        csv_file = config["file_csv"]
        chunk_size = 500000  

    for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
        chunk.to_sql("data_table", conn, if_exists="append", index=False)

    conn.execute("CREATE INDEX IF NOT EXISTS idx_column ON data_table (column_name);")
    conn.commit()
    conn.close()

    print(cl.green + "•" + cl.reset + " Conversion complete!")
