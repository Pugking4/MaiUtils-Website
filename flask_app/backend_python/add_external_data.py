import sqlite3
import json
import os

class add_external_data:
    def __init__(self, sql_path: str):
        self.connection = sqlite3.connect(sql_path)
    
    def get_sql_data_intern(self) -> dict:
        parent_dict = []
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM SheetInternalLevels")
        tuple_data = cur.fetchall()
        for i in tuple_data:
            child_dict = {}
            child_dict['title'] = i[0]
            child_dict['type'] = i[1]
            child_dict['difficulty'] = i[2]
            child_dict['internal_level'] = i[3]
            parent_dict.append(child_dict)
        self.data = parent_dict
    
    def insert_sql_data_intern(self, date_requested: str):
        with open(os.path.expanduser(r'~/MaiUtils-Website/flask_app/records') + '/' + date_requested + '.json', 'r') as f:
            raw_data = json.load(f)
        #print(raw_data)
        #print('test')
        for i_raw in raw_data:
            for i_sql in self.data:
                if i_raw['title'].lower() == i_sql['title'].lower() and i_raw['type'].lower() == i_sql['type'].lower() and i_raw['difficulty'].lower() == i_sql['difficulty'].lower():
                    i_raw['internal_level'] = i_sql['internal_level']
                    break
                i_raw['internal_level'] = None
        with open(os.path.expanduser(r'~/MaiUtils-Website/flask_app/records') + '/' + date_requested + '.json', 'w') as f:
            json.dump(raw_data, f, indent=4)

    def get_sql_data_level(self) -> dict:
        parent_dict = []
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM Sheets")
        tuple_data = cur.fetchall()
        for i in tuple_data:
            child_dict = {}
            child_dict['songId'] = i[0]
            child_dict['type'] = i[1]
            child_dict['difficulty'] = i[2]
            child_dict['level'] = i[3]
            parent_dict.append(child_dict)
        self.data = parent_dict
        
    def insert_sql_data_level(self, date_requested: str):
        with open(os.path.expanduser(r'~/MaiUtils-Website/flask_app/records') + '/' + date_requested + '.json', 'r') as f:
            raw_data = json.load(f)
        for i_raw in raw_data:
            for i_sql in self.data:
                if i_raw['title'].lower() == i_sql['songId'].lower() and i_raw['type'].lower() == i_sql['type'].lower() and i_raw['difficulty'].lower() == i_sql['difficulty'].lower():
                    i_raw['level'] = i_sql['level']
                    break
                i_raw['level'] = None
        with open(os.path.expanduser(r'~/MaiUtils-Website/flask_app/records') + '/' + date_requested + '.json', 'w') as f:
            json.dump(raw_data, f, indent=4)
    
    def get_sql_data_genre_artist(self) -> dict:
        parent_dict = []
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM Songs")
        tuple_data = cur.fetchall()
        for i in tuple_data:
            child_dict = {}
            child_dict['title'] = i[2]
            child_dict['artist'] = i[3]
            child_dict['category'] = i[1]
            parent_dict.append(child_dict)
        self.data = parent_dict
    
    def insert_sql_data_genre_artist(self, date_requested: str):
        with open(os.path.expanduser(r'~/MaiUtils-Website/flask_app/records') + '/' + date_requested + '.json', 'r') as f:
            raw_data = json.load(f)
        for i_raw in raw_data:
            for i_sql in self.data:
                if i_raw['title'].lower() == i_sql['title'].lower():
                    i_raw['artist'] = i_sql['artist']
                    i_raw['genre'] = i_sql['category']
                    break
                i_raw['artist'] = None
                i_raw['genre'] = None
        with open(os.path.expanduser(r'~/MaiUtils-Website/flask_app/records') + '/' + date_requested + '.json', 'w') as f:
            json.dump(raw_data, f, indent=4)
        


#my_class = add_external_data(os.path.expanduser(r'~/MaiUtils-Website/flask_app/db/20230423db.sqlite3'))
#
#
#my_class.get_sql_data_intern()
#
#
#my_class.insert_sql_data_intern('2023-05-07')
#
#
#my_class.get_sql_data_level()
#
#
#my_class.insert_sql_data_level('2023-05-07')
#
#
#my_class.get_sql_data_genre_artist()
#
#
#my_class.insert_sql_data_genre_artist('2023-05-07')