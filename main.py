# -*- data searcher -*-

import sqlite3
import src.cl as cl
import src.convert as convert
import os

config = {
    "outfile": "\\data\\data.db"
}

def Search(search_value):
    conn = sqlite3.connect(config["outfile"])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data_table WHERE column_name = ?", (search_value,))
    result = cursor.fetchall()
    conn.close()

    return result

def search_in_db(search_value):
    print(os.path.abspath(config["outfile"]))

    if not os.path.exists(config["outfile"]):
        print(cl.red + "•" + cl.reset + f" Database not found. Converting CSV to SQLite.")
        convert.convert()
        return Search(search_value)
        
    else:
        cm = input(cl.yellow + "•" + cl.reset + f' Do you want to replace "{config["outfile"]}" ? (y/n): ')
        if cm.lower() == 'y':
            os.remove(config["outfile"])
            print(cl.blue + "•" + cl.reset + " Replacing data.db")
            convert.convert()
            return Search(search_value) 
        elif cm.lower() == 'n':
            print(cl.red + "•" + cl.reset + " Database not removed.")
            cmm = input(cl.yellow + "•" + cl.reset + f' Do you want to search directly from: "{config["outfile"]}"? (y/n): ')
            if cmm.lower() == 'y':
                return Search(search_value) 
            else:
                print(cl.red + "•" + cl.reset + " Exiting...")
                exit()
                return None

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