import matplotlib.pyplot as plt
import numpy as np
import json
import sqlite3
from Crawler import change_name
SERVERS=['Apache', 'IIS', 'nginx']

def load_database(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    conn.row_factory = sqlite3.Row

    get_data = '''
    SELECT server FROM websites
    '''
    res = cursor.execute(get_data)
    
    elems = res.fetchall()
    
    jsoned = {
            'Apache': 0,
            'IIS': 0,
            'nginx': 0,
            'other': 0
            }

    for elem in elems:
        jsoned[change_name(tuple(elem)[0])] += 1

    return jsoned

def load_json(filename):
    fl = open(filename)
    jsoned = json.load(fl)
    fl.close()
    return jsoned

def get_elems_number(jsoned):
    total_cnt = 0
    for elem in jsoned.keys():
        total_cnt += jsoned[elem]
    return total_cnt

def get_servers(total_cnt, jsoned):
    servers = []
    for i in range(3):
        if SERVERS[i] in jsoned.keys():
            servers.append(jsoned[SERVERS[i]]/total_cnt)
        else:
            servers.append(0)
        print(servers)
    servers.append(1 - sum(servers))
    return servers

def plot(filename):
    #jsoned = load_json(filename)
    jsoned = load_database(filename)
    labels = 'Apache', 'IIS', 'nginx', 'other'
    total_cnt = get_elems_number(jsoned)

    all_ser = get_servers(total_cnt, jsoned)

    sizes = [all_ser[0], all_ser[1], all_ser[2], all_ser[3]]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')

    plt.show()
