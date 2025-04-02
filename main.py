# // Data Searcher - CSV File To SQLite Searcher

# -*- data searcher -*-
import sqlite3
import src.cl as cl
import src.convert as convert
import os

config = {
    "outfile": "/data/data.db"
}

def search_in_db(search_value):
    if not os.path.exists(config["outfile"]):
        convert.convert()
    else:
        cm = input(cl.yellow + "•" + cl.reset + f' Do you want to replace "{config["outfile"]}" ? (y/n): ')
        if cm.lower() == 'y':
            os.remove(config["outfile"])
            print(cl.blue + "•" + cl.reset + " Replacing data.db")
            convert.convert()
        elif cm.lower() == 'n':
            print(cl.red + "•" + cl.reset + " Database not removed.")
            return None

    conn = sqlite3.connect(config["outfile"])
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM data_table WHERE column_name = ?", (search_value,))
    
    result = cursor.fetchall()
    conn.close()
    
    return result

while True:
    try:
        search_value = input(cl.cyan + "•" + cl.reset + ' Search value: ')
        result = search_in_db(search_value)

        if result:
            print(result)
        else:
            print(cl.red + "•" + cl.reset + " No results found.")
    except Exception as e:
        print(cl.red + "• ERROR" + cl.reset + str(e))
