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


a = {'a': 1, 'b': 2, 'c': 3}

del a['d'] , a['b']

print(a)