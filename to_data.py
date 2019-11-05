import pymysql

db = pymysql.connect('192.168.0.124', 'root', '123456', 'pt')
cursor = db.cursor()
sql = 'select tag_ids from lesson'
cursor.execute(sql)
data = cursor.fetchall()
tag0 = []
tag1 = []
tag2 = []
tag3 = []
tag4 = []
for i in data:
    tag = i[0].replace('[', '').replace(']', '').replace("'", '').replace(' ', '').split(',')
    tag0.append(tag[0])
    tag1.append(tag[1])
    tag2.append(tag[2])
    tag3.append(tag[3])
    tag4.append(tag[4])
print(set(tag0))
print(set(tag1))
print(set(tag2))
print(set(tag3))
print(set(tag4))

