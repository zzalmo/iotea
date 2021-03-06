import pymysql.cursors

# 打开数据库连接
conn = pymysql.connect("localhost", "root", "1234", "iotea")
# 使用cursor()方法获取操作游标
cur = conn.cursor()


# SQL 插入语句
def insert(list):
	sql = "insert into iotea (time,air_temp,air_hum,pressure,co2,dust,illumination,o2,soil_temp,soil_hum,voltage,error)" \
		  " values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
		  %(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9],list[10],list[11])
	cur.execute(sql)
	conn.commit()



# SQL 查询语句
def readMax():
	sql="SELECT  * FROM iotea.iotea where id =(SELECT  max(id) FROM iotea.iotea)"
	cur.execute(sql)
	result = cur.fetchall()
	conn.commit()
	return result


