import pymysql

db = pymysql.connect(
    host="106.53.250.56",
    user="root",
    password="XuBFt1DE0d18u3Fw",
    db="shopip"
)
cur = db.cursor()
def sql_delete():
    sql_del = "DELETE FROM de_user WHERE mobile='14259739812';"
    cur.execute(sql_del)
    db.commit()
    db.close()


if __name__ == '__main__':
    sql_delete()