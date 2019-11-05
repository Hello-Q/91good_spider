# import pymysql
# db = pymysql.connect('localhost', 'root', 'ZYQ1994zyq', 'pt')
# # 获取游标
# cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
# # 数据列名
# school_date = {'name': '1', 'img_url': '2'}
# cols = ', '.join('`{}`'.format(k) for k in school_date.keys())
# # 数据值
# val_cols = ', '.join('%({})s'.format(k) for k in school_date.keys())
# # sql语句
# sql = "insert into school(%s) values(%s)"
# res_sql = sql % (cols, val_cols)
# # res_sql = 'insert into school(name)  values(1)'
# print(res_sql)
# cursor.execute(res_sql, school_date)
# db.commit()
# db.close()
#
#
# a = {'a': 1, 'b': 2, 'c': 3}
#
# del a['d'] , a['b']
#
# print(a)
#
# a = {'a': 1, 'b': 3}
# a = str(a)
# print(a, type(a))
#
# import requests
# for i in range(30):
# 	r = requests.get('http://api.ip.data5u.com/dynamic/get.html?order=8cf43b65ecaff2784a14c00006094c34&json=1&sep=3')
#
# 	print(r.text)
# import json
# with open('LessonInfoItem.json', 'r') as f:
# 	file = f.read()
# 	file = '[' + file + ']'
# 	lesson_dict = json.loads(file)
# 	print(lesson_dict)

# a = '123.00'
# b = float(a)
# print(b)

import xlrd
# import xlwt
# import json
#
# with open('/home/zhangyanqing/python/work/91good_spider/file/city.json', 'r') as f:
#     citys = json.load(f)
# print(citys)
#
# excel = xlwt.Workbook(encoding='utf-8')
# sheet = excel.add_sheet('test', cell_overwrite_ok=True)
# print(len(citys))
# sheet.write(0, 0, '城市')
# sheet.write(0, 1, '简称')
# row = 1
# col = 0
# for k, v in citys.items():
#     sheet.write(row, col, k)
#     sheet.write(row, col+1, v)
#     row += 1
# excel.save('test.xls')
# import json
#
# a = [{'w': 1, 'q': 2}, {'w': 4, 'q': 5}]
# r = json.dumps(a)
# print(r)

import cv2
import numpy as np

path = '8229.jpg'
img = cv2.imread(path)
height, width = img.shape[0:2]
thresh = cv2.inRange(img, np.array([0, 0, 0]), np.array([192, 192, 192]))
scan = np.ones((3, 3), np.uint8)
cor = cv2.dilate(thresh, scan, iterations=1)
specular = cv2.inpaint(img, cor, 5, flags=cv2.INPAINT_TELEA)
# 操作结束，下面开始是输出图片的代码
cv2.namedWindow("image", 0)
cv2.resizedWindow("image", int(width/2), int(height/2))
cv2.imshow("image", img)

cv2.namedWindow("modified", 0)
cv2.resizeWindow("modified", int(width/2), int(height/2))
cv2.imshow("modified", specular)

cv2.waitKey(0)
cv2.destroyAllWindows()
