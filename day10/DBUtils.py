import pymysql

host = "localhost"
database = "银行数据库"
user = "root"
password = "root"


# 可以处理增，删，改的所有操作
def update(sql, param):
    con = pymysql.connect(host=host, database=database, user=user, password=password)
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()  # 提交数据
    cursor.close()
    con.close()


# 可以处理查询所有炒作
def select(sql, param, mode="many", size=0):
    con = pymysql.connect(host=host, database=database, user=user, password=password)
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()  # 提交数据
    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)
    cursor.close()
    con.close()
