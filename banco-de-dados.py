import sqlite3
conn = sqlite3.connect('example.db')
cursor=conn.cursor()
cursor.execut('''
CREATE TABLE IF NOT EXISTS users
(id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
password TEXT
)''')
conn.commit()
conn.close()
print("Tabela criada com sucesso!")
    
    
    
    
    

