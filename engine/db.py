import sqlite3

con = sqlite3.connect("Nova.db")

cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'OneDrive','C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\OneDrive.exe')"
#cursor.execute(query)
#con.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null,'OneDrive','C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\OneDrive.exe')"
cursor.execute(query)
con.commit()