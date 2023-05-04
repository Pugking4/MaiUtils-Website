import sqlite3
import json
import os

def add_data_to_sqlite3_db(data=None):
    table_name = 'records_data'
    record_headers = [
    "title",
    "difficulty",
    "score",
    "deluxe_score",
    "type",
    "time",
    "track",
    "img_link",
    "combo",
    "sync",
    "place",
    "players",
    "new_record",
    "new_record_deluxe",
    "cp_taps",
    "p_taps",
    "gr_taps",
    "go_taps",
    "m_taps",
    "cp_holds",
    "p_holds",
    "gr_holds",
    "go_holds",
    "m_holds",
    "cp_slides",
    "p_slides",
    "gr_slides",
    "go_slides",
    "m_slides",
    "cp_touch",
    "p_touch",
    "gr_touch",
    "go_touch",
    "m_touch",
    "cp_breaks",
    "p_breaks",
    "gr_breaks",
    "go_breaks",
    "m_breaks",
    "player2",
    "max_combo",
    "max_sync",
    "rating_gain",
    "current_rating",
    "fast",
    "late"
    ]
   
    notes = [
    "cp_taps",
    "p_taps",
    "gr_taps",
    "go_taps",
    "m_taps",
    "cp_holds",
    "p_holds",
    "gr_holds",
    "go_holds",
    "m_holds",
    "cp_slides",
    "p_slides",
    "gr_slides",
    "go_slides",
    "m_slides",
    "cp_touch",
    "p_touch",
    "gr_touch",
    "go_touch",
    "m_touch",
    "cp_breaks",
    "p_breaks",
    "gr_breaks",
    "go_breaks",
    "m_breaks",
    ]

    bruh = {
        "cp": "critical_perfect",
        "p": "perfect",
        "gr": "great",
        "go": "good",
        "m": "miss"
    }

    json_data = []
    files = os.listdir(r'~/MaiUtils-Website/flask_app/records')
    for date in files:
        if date.endswith('.json'):
            with open(r'~/MaiUtils-Website/flask_app/records' + '/' + date, 'r') as f:
                    json_data.append(json.load(f))
    

    # Connect to the database
    conn = sqlite3.connect(r'~/MaiUtils-Website/flask_app/db/playdata.sqlite3')
    # Create a cursor
    c = conn.cursor()
    # Insert data into table
    c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    if c.fetchone() is None:
        c.execute(f"CREATE TABLE {table_name} (title str)")
        conn.commit()


    existing_columns = []
    for column in c.execute("PRAGMA table_info({})".format(table_name)):
        existing_columns.append(column[1])
        #c.execute(f'SELECT * FROM {table_name}')

    if len(existing_columns) != len(record_headers):
        for attribute in record_headers:
            if attribute not in existing_columns:
                c.execute(f"ALTER TABLE {{}} ADD COLUMN {attribute} datatype".format(table_name))
    
    conn.commit()

    c.execute(f"SELECT time FROM {table_name};")
    existing_data = c.fetchall()
    print(existing_data[1][0])
    print(existing_data[3][0])
    for day in json_data:
        for chart in day:
            if chart['time'] not in [data[0] for data in existing_data]:
                print(chart['time'])
                c.execute(f"INSERT INTO {table_name} (time) VALUES ('{chart['time']}');")
                conn.commit()
                for attribute in record_headers:
                    if attribute in notes:
                        c.execute(f"UPDATE {table_name} SET {attribute} = '{chart[attribute.split('_')[1]][bruh.get(attribute.split('_')[0])]}' WHERE time = '{chart['time']}';")
                        conn.commit()
                    else:
                        c.execute(f"UPDATE {table_name} SET {attribute} = ? WHERE time = ?", (chart[attribute], chart['time']))
                        conn.commit()
            else:
                    print('already exists')
                    '''
            
            else:
                for attribute in record_headers:
                    c.execute(f"UPDATE {table_name} SET {attribute} = '{chart[attribute]}' WHERE time = '{chart['time']}';")
                    conn.commit()
                    '''

#todo:
#1. add function to search for broken records
#2. add function to fix broken records by reinserting the data

add_data_to_sqlite3_db()