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

# ȫ�ֱ���
save_path = ''


# ���ύ���У��
class fileForm(Form):
    file = FileField(validators=[FileRequired(), FileAllowed(['mat'])])


# �ӿڼ�Ȩ
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = request.headers.get(
        'Origin') or 'http://127.0.0.1:5000' or 'http://localhost:8080/'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE'
    response.headers[
        'Access-Control-Allow-Headers'] = 'Content-Type, Authorization, Accept, Origin, Referer, User-Agent'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response


# ��ʼ��flaskʵ��
app = Flask(__name__)
app.after_request(after_request)

cors = CORS(app, resources={r"/getMsg": {"origins": "*"}})


# ���Է�������ͨ
@app.route('/')
def hello_world():
    print(111)
    return 'Hello World!'


# ����ǰ��˿�ͨ��
@app.route('/getMsg', methods=['GET', 'POST'])
def home():
    response = {
        'msg': 'Hello, Python !'
    }
    return jsonify(response)


# ��ȡע�����󼰴���
@app.route('/register', methods=['GET', 'POST'])
def getRigistRequest():
    # �������ݿ�,��ǰ�����ݿ��д������ݿ�flask
    db = pymysql.connect(
        user='root',
        password='root',
        # MySQL��Ĭ�϶˿�Ϊ3306
        port=3306,
        # ������ַΪ127.0.0.1��localhost
        host='localhost',
        # ָ��ʹ�õ����ݿ�
        database='geerwheel'
    )

    print("���ӳɹ�")
    # ʹ��cursor()������ȡ�����α�
    cursor = db.cursor()

    data = request.get_json()
    print(data)

    username = data.get('username')
    password = data.get('password')
    password2 = data.get('password2')
    truename = data.get('truename')
    idcardnum = data.get('idcardnum')

    # �ж��������������Ƿ�һ�£�һ������ת����¼���棬��һ���򵯳����棬Ҫ���û���������
    if password == password2:
        # SQL �������
        sql_0 = "INSERT INTO users(username, password,truename,idcardnum) VALUES (%s,%s,%s,%s)"
        sql = sql_0 % (repr(username), repr(password), repr(truename), repr(idcardnum))
        try:
            # ִ��sql���
            cursor.execute(sql)
            # �ύ�����ݿ�ִ��
            db.commit()
            return 'ע��ɹ�'
        except:
            # �׳�������Ϣ
            traceback.print_exc()
            # �������������ع�
            db.rollback()
            return 'ע��ʧ��'
        # �ر����ݿ�����
        db.close()
    else:
        return 'ע��ɹ�'


# ��ȡ��¼����������
@app.route('/login', methods=['GET', 'POST'])
def getLoginRequest():
    # ��ѯ�û����������Ƿ�ƥ�估����
    # �������ݿ�,��ǰ�����ݿ��д������ݿ�TESTDB
    db = pymysql.connect(host="localhost", user="root", password="root", database="geerwheel", charset="utf8")
    # ʹ��cursor()������ȡ�����α�
    cursor = db.cursor()

    username = request.get_json().get('username')
    password = request.get_json().get('password')
    # SQL ��ѯ���
    sql_0 = "select * from users where username= %s and password= %s"
    sql = sql_0 % (repr(username), repr(password))

    try:
        # ִ��sql���
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(len(results))
        print(results)
        if len(results) == 1:
            return '��¼�ɹ�'  # ������Ҫ��ת��ҳ�����Ҫ��ʾ���ַ���
        else:
            return '�û��������벻��ȷ'
        # �ύ�����ݿ�ִ��
        db.commit()
    except:
        # �������������ع�
        traceback.print_exc()
        db.rollback()
    # �ر����ݿ�����
    db.close()


# չʾ���ݼ�
@app.route('/showDataset', methods=['GET', 'POST'])
def showDataset():
    db = pymysql.connect(host="localhost", user="root", password="root", database="geerwheel", charset="utf8")
    # ʹ��cursor()������ȡ�����α�
    cursor = db.cursor()
    sql = "select * from dataset"

    try:
        # ִ��sql���
        cursor.execute(sql)
        results = cursor.fetchall()

        print('result��', results)
        list = []
        for row in results:
            dic = {'id': row[0], 'name': row[1], 'region': row[2], 'contact': row[3], 'description': row[4],
                   'ischoosed': row[5]}
            list.append(dic)
        print(list)
        return jsonify(list)
        # �ύ�����ݿ�ִ��
        db.commit()
    except:
        # �������������ع�
        traceback.print_exc()
        db.rollback()
        # �ر����ݿ�����
    db.close()
    return


# �������ݼ�ѡ��״̬
@app.route('/updataDataset', methods=['GET', 'POST'])
def updateDataset():
    db = pymysql.connect(host="localhost", user="root", password="root", database="geerwheel", charset="utf8")
    cur = db.cursor()
    status = request.get_data(as_text=True)
    print('status ����')
    print(status)
    if (status == '1'):
        sql = "UPDATE dataset SET ischoosed='��' WHERE id=2"
    else:
        sql = "UPDATE dataset SET ischoosed='��' WHERE id=2"
    print(sql)
    cur.execute(sql)
    db.commit()
    cur.close()
    db.close()
    return '���ĳɹ�'


# ������ݼ�
@app.route('/uploadDataset', methods=['GET', 'POST'])
def uploadDataset():
    db = pymysql.connect(host="localhost", user="root", password="root", database="geerwheel", charset="utf8")
    cursor = db.cursor()
    data = request.get_json()
    print('data��')
    print(data)

    id = data.get('id')
    name = data.get('name')
    region = data.get('region')
    contact = data.get('contact')
    description = data.get('description')
    ischoosed = data.get('ischoosed')
    # SQL �������
    sql_0 = "INSERT INTO dataset(id,name,region,contact,description,ischoosed) VALUES (%s,%s,%s,%s,%s,%s)"
    sql = sql_0 % (repr(id), repr(name), repr(region), repr(contact), repr(description), repr(ischoosed))
    try:
        # ִ��sql���
        cursor.execute(sql)
        # �ύ�����ݿ�ִ��
        db.commit()
        return '��ӳɹ�'
    except:
        # �׳�������Ϣ
        traceback.print_exc()
        # �������������ع�
        db.rollback()
        return '���ʧ��'
    # �ر����ݿ�����
    db.close()


# �ϴ��ļ�
@app.route("/uploadDatafile", methods=['POST'])
def uploadDatafile():
    # print(data)
    # ��ʼ�����ض���
    file_form = fileForm(CombinedMultiDict([request.form, request.files]))
    if file_form.validate():
        # ��ȡ��Ŀ·��+�����ļ��У���ɷ��񱣴����·��
        # save_path = os.path.join(os.path.abspath(os.path.dirname(__file__)).split('DiagnosisSystem')[0],
        #                          'DiagnosisSystem/BackEnd/static/data')
        # print('�ѱ���')
        # ͨ�����ύ��form-data��ȡѡ���ϴ����ļ�
        attfile = request.files.get('file')
        # ���а�ȫ���Ƽ�鴦��
        file_name = secure_filename(attfile.filename)
        # �����ļ��ļ���
        attfile.save(os.path.join(save_path, file_name))
        print('����ɹ�')

        return jsonify({
            "code": 200,
            "message": "�ϴ�����ɹ�",
            "fileName": file_name
        })
    else:
        return jsonify({
            "code": 400,
            "message": "�ļ���ʽ������Ԥ��"
        }), 400


# �������ݼ��ļ���
@app.route("/makeDatadir", methods=['GET', 'POST'])
def makeDatadir():
    data = request.get_json()['name']
    print(data)
    name = data
    print(name)
    dir = os.path.dirname(__file__)
    print(dir)
    if (os.path.exists('{}/static/data/{}'.format(dir, name))) == False:
        print('��Ŀ¼�����ڣ�������Ŀ¼')
        os.mkdir('{}/static/data/{}'.format(dir, name))
        global save_path
        save_path = ('{}/static/data/{}'.format(dir, name))
        print(save_path)
        print('�����ɹ�')
        return jsonify({
            "code": 200,
            "message": save_path
        })
    else:
        return jsonify({
            "code": 400,
            "message": "·���Ѵ���"
        }), 400


# ����ѵ������
@app.route("/train", methods=['GET', 'POST'])
def train():
    data = request.get_json()
    print(data)

    from BackEnd.Algorithm.BackEnd.Algorithm import sign_cnn
    from BackEnd.Algorithm.BackEnd.Algorithm import sign_inception


    model=request.get_json()['model']

    import sys
    f = open('Algorithm/BackEnd/Algorithm/save_logs/{}.log'.format(model), 'a',encoding='utf-8')
    sys.stdout = f  # ����print���
    sys.stderr = f  # �����쳣�������Ϣ
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
        "message": "�ɹ�"
    })

#�鿴ѵ����־
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


# ��������
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)  # �����ӻ�ֱ�������ڱ��ط�������Ҳ���� localhost:5000
# app.run(host='your_ip_address') # �����ͨ�� host ָ���ڹ���IP������
