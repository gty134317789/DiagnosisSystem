# -*- coding: gbk -*-
import pymysql
import traceback
import os
from wtforms import Form, FileField
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_wtf.file import FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict

# 全局变量
save_path = ''


# 表单提交相关校验
class fileForm(Form):
    file = FileField(validators=[FileRequired(), FileAllowed(['mat'])])


# 接口鉴权
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = request.headers.get(
        'Origin') or 'http://127.0.0.1:5000' or 'http://localhost:8080/'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE'
    response.headers[
        'Access-Control-Allow-Headers'] = 'Content-Type, Authorization, Accept, Origin, Referer, User-Agent'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response


# 初始化flask实例
app = Flask(__name__)
app.after_request(after_request)

cors = CORS(app, resources={r"/getMsg": {"origins": "*"}})


# 测试服务器连通
@app.route('/')
def hello_world():
    print(111)
    return 'Hello World!'


# 测试前后端可通信
@app.route('/getMsg', methods=['GET', 'POST'])
def home():
    response = {
        'msg': 'Hello, Python !'
    }
    return jsonify(response)


# 获取注册请求及处理
@app.route('/register', methods=['GET', 'POST'])
def getRigistRequest():
    # 连接数据库,此前在数据库中创建数据库flask
    db = pymysql.connect(
        user='root',
        password='root',
        # MySQL的默认端口为3306
        port=3306,
        # 本机地址为127.0.0.1或localhost
        host='localhost',
        # 指定使用的数据库
        database='geerwheel'
    )

    print("连接成功")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    data = request.get_json()
    print(data)

    username = data.get('username')
    password = data.get('password')
    password2 = data.get('password2')
    truename = data.get('truename')
    idcardnum = data.get('idcardnum')

    # 判断两次输入密码是否一致，一致则跳转到登录界面，不一致则弹出警告，要求用户重新输入
    if password == password2:
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
            # 抛出错误信息
            traceback.print_exc()
            # 如果发生错误则回滚
            db.rollback()
            return '注册失败'
        # 关闭数据库连接
        db.close()
    else:
        return '注册成功'


# 获取登录参数及处理
@app.route('/login', methods=['GET', 'POST'])
def getLoginRequest():
    # 查询用户名及密码是否匹配及存在
    # 连接数据库,此前在数据库中创建数据库TESTDB
    db = pymysql.connect(host="localhost", user="root", password="root", database="geerwheel", charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    username = request.get_json().get('username')
    password = request.get_json().get('password')
    # SQL 查询语句
    sql_0 = "select * from users where username= %s and password= %s"
    sql = sql_0 % (repr(username), repr(password))

    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(len(results))
        print(results)
        if len(results) == 1:
            return '登录成功'  # 返回需要跳转的页面或需要显示的字符串
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


# 展示数据集
@app.route('/showDataset', methods=['GET', 'POST'])
def showDataset():
    db = pymysql.connect(host="localhost", user="root", password="root", database="geerwheel", charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from dataset"

    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()

        print('result是', results)
        list = []
        for row in results:
            dic = {'id': row[0], 'name': row[1], 'region': row[2], 'contact': row[3], 'description': row[4],
                   'ischoosed': row[5]}
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


# 更改数据集选中状态
@app.route('/updataDataset', methods=['GET', 'POST'])
def updateDataset():
    db = pymysql.connect(host="localhost", user="root", password="root", database="geerwheel", charset="utf8")
    cur = db.cursor()
    status = request.get_data(as_text=True)
    print('status 如下')
    print(status)
    if (status == '1'):
        sql = "UPDATE dataset SET ischoosed='否' WHERE id=2"
    else:
        sql = "UPDATE dataset SET ischoosed='是' WHERE id=2"
    print(sql)
    cur.execute(sql)
    db.commit()
    cur.close()
    db.close()
    return '更改成功'


# 添加数据集
@app.route('/uploadDataset', methods=['GET', 'POST'])
def uploadDataset():
    db = pymysql.connect(host="localhost", user="root", password="root", database="geerwheel", charset="utf8")
    cursor = db.cursor()
    data = request.get_json()
    print('data是')
    print(data)

    id = data.get('id')
    name = data.get('name')
    region = data.get('region')
    contact = data.get('contact')
    description = data.get('description')
    ischoosed = data.get('ischoosed')
    # SQL 插入语句
    sql_0 = "INSERT INTO dataset(id,name,region,contact,description,ischoosed) VALUES (%s,%s,%s,%s,%s,%s)"
    sql = sql_0 % (repr(id), repr(name), repr(region), repr(contact), repr(description), repr(ischoosed))
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        return '添加成功'
    except:
        # 抛出错误信息
        traceback.print_exc()
        # 如果发生错误则回滚
        db.rollback()
        return '添加失败'
    # 关闭数据库连接
    db.close()


# 上传文件
@app.route("/uploadDatafile", methods=['POST'])
def uploadDatafile():
    # print(data)
    # 初始化返回对象
    file_form = fileForm(CombinedMultiDict([request.form, request.files]))
    if file_form.validate():
        # 获取项目路径+保存文件夹，组成服务保存绝对路径
        # save_path = os.path.join(os.path.abspath(os.path.dirname(__file__)).split('DiagnosisSystem')[0],
        #                          'DiagnosisSystem/BackEnd/static/data')
        # print('已保存')
        # 通过表单提交的form-data获取选择上传的文件
        attfile = request.files.get('file')
        # 进行安全名称检查处理
        file_name = secure_filename(attfile.filename)
        # 保存文件文件中
        attfile.save(os.path.join(save_path, file_name))
        print('保存成功')

        return jsonify({
            "code": 200,
            "message": "上传请求成功",
            "fileName": file_name
        })
    else:
        return jsonify({
            "code": 400,
            "message": "文件格式不符合预期"
        }), 400


# 创建数据集文件夹
@app.route("/makeDatadir", methods=['GET', 'POST'])
def makeDatadir():
    data = request.get_json()['name']
    print(data)
    name = data
    print(name)
    dir = os.path.dirname(__file__)
    print(dir)
    if (os.path.exists('{}/static/data/{}'.format(dir, name))) == False:
        print('根目录不存在，创建根目录')
        os.mkdir('{}/static/data/{}'.format(dir, name))
        global save_path
        save_path = ('{}/static/data/{}'.format(dir, name))
        print(save_path)
        print('创建成功')
        return jsonify({
            "code": 200,
            "message": save_path
        })
    else:
        return jsonify({
            "code": 400,
            "message": "路径已存在"
        }), 400


# 调用训练函数
@app.route("/train", methods=['GET', 'POST'])
def train():
    data = request.get_json()
    print(data)

    from BackEnd.Algorithm.BackEnd.Algorithm import sign_cnn
    from BackEnd.Algorithm.BackEnd.Algorithm import sign_inception


    model=request.get_json()['model']

    import sys
    f = open('Algorithm/BackEnd/Algorithm/save_logs/{}.log'.format(model), 'a',encoding='utf-8')
    sys.stdout = f  # 保存print输出
    sys.stderr = f  # 保存异常或错误信息
    if model=='CNN':
        sign_cnn.run_Algorithm()
        sign_cnn.num_classes = request.get_json()['num_classes']
        sign_cnn.epochs = request.get_json()['epochs']
        sign_cnn.train = request.get_json()['train']
        sign_cnn.valid = request.get_json()['valid']
        sign_cnn.test = request.get_json()['test']
    elif model=='INCEPTION':
        sign_inception.num_classes = request.get_json()['num_classes']
        sign_inception.epochs = request.get_json()['epochs']
        sign_inception.train = request.get_json()['train']
        sign_inception.valid = request.get_json()['valid']
        sign_inception.test = request.get_json()['test']
        sign_inception.run_Algorithm()

    return jsonify({
        "code": 200,
        "message": "成功"
    })

#查看训练日志
@app.route('/result', methods=['POST','GET'])
def read_file():
    file_path = 'E:\DiagnosisSystem\BackEnd\Algorithm\BackEnd\Algorithm\save_logs'
    model = request.get_json()['model']
    file_path=file_path+('\{}.log'.format(model))
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return jsonify({'content': content, 'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'})


# 启动运行
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)  # 这样子会直接运行在本地服务器，也即是 localhost:5000
# app.run(host='your_ip_address') # 这里可通过 host 指定在公网IP上运行
