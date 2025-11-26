import sqlite3
db=sqlite3.Connection("n.db")#数据库连接文件名叫n.db的文件，如果有就打开，没有就自动创建一个
db.execute("DROP table numsss")
db.execute("CREATE TABLE numsss AS SELECT 2 UNION SELECT 3;")
db.execute("INSERT INTO numsss VALUES (?),(?),(?)",(2,4,4))
db.commit()
cursor=db.execute("select * from numsss")
print(cursor.fetchall())