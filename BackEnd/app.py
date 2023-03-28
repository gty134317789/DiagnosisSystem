from flask import Flask
from flask import jsonify
from flask import request
from flask import redirect
from flask_cors import CORS
import pymysql
import traceback


def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = request.headers.get(
        'Origin') or 'http://127.0.0.1:5000' or 'http://localhost:8080/'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE'
    response.headers[
        'Access-Control-Allow-Headers'] = 'Content-Type, Authorization, Accept, Origin, Referer, User-Agent'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response




app = Flask(__name__)
app.after_request(after_request)
cors = CORS(app, resources={r"/getMsg": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getMsg', methods=['GET', 'POST'])
def home():
    response = {
        'msg': 'Hello, Python !'
    }
    return jsonify(response)


#获取注册请求及处理
@app.route('/register',methods=['GET','POST'])
def getRigistRequest():
    #连接数据库,此前在数据库中创建数据库flask
    db= pymysql.connect(
    user = 'root',
    password = 'root',
    # MySQL的默认端口为3306
    port = 3306,
    # 本机地址为127.0.0.1或localhost
    host = 'localhost',
    # 指定使用的数据库
    database = 'geerwheel'
)

    print("连接成功")
    #使用cursor()方法获取操作游标
    cursor = db.cursor()

    data=request.get_json()
    print(data)



    username=data.get('username')
    password=data.get('password')
    password2=data.get('password2')
    truename=data.get('truename')
    idcardnum=data.get('idcardnum')


    print(username)
    print(password)
    print(password2)
    print(truename)
    print(idcardnum)
    #判断两次输入密码是否一致，一致则跳转到登录界面，不一致则弹出警告，要求用户重新输入
    if password==password2:
        # SQL 插入语句
        sql_0 = "INSERT INTO users(username, password,truename,idcardnum) VALUES (%s,%s,%s,%s)"
        sql = sql_0 % (repr(username), repr(password), repr(truename), repr(idcardnum))
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            return '注册成功'
        except:
            #抛出错误信息
            traceback.print_exc()
            # 如果发生错误则回滚
            db.rollback()
            return '注册失败'
        # 关闭数据库连接
        db.close()
    else:
        return '注册成功'

# 获取登录参数及处理
@app.route('/login',methods=['GET','POST'])
def getLoginRequest():
    # 查询用户名及密码是否匹配及存在
    # 连接数据库,此前在数据库中创建数据库TESTDB
    db = pymysql.connect(host="localhost", user="root", password="root", database="geerwheel",charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    username = request.get_json().get('username')
    password = request.get_json().get('password')
    # SQL 查询语句
    sql_0 = "select * from users where username= %s and password= %s"
    sql = sql_0 % (repr(username),repr(password))

    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(len(results))
        print(results)
        if len(results) == 1:
            return '登录成功'      #返回需要跳转的页面或需要显示的字符串
        else:
            return '用户名或密码不正确'
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
    # 关闭数据库连接
    db.close()


#分页查询方法
@app.route('/showDataset',methods=['GET','POST'])
def showDataset():
    db = pymysql.connect(host="localhost", user="root", password="root", database="geerwheel", charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql="select * from dataset"
    # post_data=request.get_json()
    # print('传过来的参数是',post_data)
    # pagesize=post_data.get('pagesize')
    # page=post_data.get('page')
    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        print('result是',results)
        list=[]
        for row in results:
            dic={'id':row[0],'name':row[1],'region':row[2],'contact':row[3],'description':row[4],'ischoosed':row[5]}
            list.append(dic)
        print(list)
        return jsonify(list)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
        # 关闭数据库连接
    db.close()
    return


# 启动运行
if __name__ == '__main__':
    app.run()   # 这样子会直接运行在本地服务器，也即是 localhost:5000
   # app.run(host='your_ip_address') # 这里可通过 host 指定在公网IP上运行