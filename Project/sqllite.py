import sqlite3
import random
conn = sqlite3.connect('cancer.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS user_details(user_id integer primary key,name text,gender text,email_id text,password text,age int)")
    c.execute("CREATE TABLE IF NOT EXISTS records(user_id int ,clump_thickness int,uniformity_cell_size int,uniformity_cell_shape int,marginal_adhesion int,single_epithelial_cell_size int,bare_nuclei int,bland_chromatin int,normal_nucleoli int,mitoses int,date text,record_no integer primary key autoincrement,foreign key(user_id) references user_details(user_id))")
              

    conn.commit()
##    c.close()
##    conn.close()

create_table()

def entry_sign(name,gender,email,password,age):
    #print('in entry')
    us_id = random.randint(1,100000)
    c.execute("INSERT INTO user_details(user_id,name,gender,email_id,password,age) VALUES (?,?, ?, ?, ?, ?)",
          (us_id,name,gender,email,password,age))
    #print('bef commit')
    conn.commit()

def entry_ml(us_id, q,r,s,t,u,v,w,x,y,today,stat):

    c.execute("INSERT INTO records (user_id,clump_thickness,uniformity_cell_size,uniformity_cell_shape,marginal_adhesion,single_epithelial_cell_size,bare_nuclei,bland_chromatin,normal_nucleoli,mitoses,date,status) VALUES ( ?, ?, ?, ?,?,?, ?, ?, ?, ?,?,?)",
          (us_id,q,r,s,t,u,v,w,x,y,today,stat))

    conn.commit()
#entry_vars('t','t2', 12,'M', 20000)
def login_check(email, passw):
    c.execute('SELECT * FROM user_details')
    data = c.fetchall()
    for row in data:
        if email in row and passw in row:
            return row
    return False
#read_from_db()

