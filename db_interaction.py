import pymysql

def showTasks():
    sql= "SELECT ID, Description FROM tasks_list.tasks"
    conn= pymysql.connect(user='root', password='user', host='localhost', database='tasks_list')
    cur= conn.cursor()
    cur.execute(sql)
    res= cur.fetchall()
    cur.close()
    conn.close()
    return res

def showSpecificTasks(args):
    sql= "SELECT ID, Description FROM tasks_list.tasks WHERE id= (%s)"
    conn= pymysql.connect(user='root', password='user', host='localhost', database='tasks_list')
    cur= conn.cursor()
    cur.execute(sql, (args,))
    res= cur.fetchone()
    cur.close()
    conn.close()
    return res

def newTask(args, urgent):
    sql = "INSERT INTO tasks_list.tasks(Description, Urgent) VALUES (%s, %s)"
    conn = pymysql.connect(user='root', password='user', host='localhost', database='tasks_list')
    cur = conn.cursor()
    cur.execute(sql, (args, urgent,))
    conn.commit()
    cur.close()
    conn.close()
    return

def removeTask(args):
    sql = "DELETE FROM tasks_list.tasks WHERE id= (%s)"
    conn = pymysql.connect(user='root', password='user', host='localhost', database='tasks_list')
    cur = conn.cursor()
    cur.execute(sql, (args,))
    conn.commit()
    cur.close()
    conn.close()
    return

def updateTask(id, description, urgent):
    sql = "UPDATE tasks_list.tasks SET Description= (%s), Urgent= (%s) WHERE ID= (%s)"
    conn = pymysql.connect(user='root', password='user', host='localhost', database='tasks_list')
    cur = conn.cursor()
    cur.execute(sql, (description, urgent, id,))
    conn.commit()
    cur.close()
    conn.close()
    return