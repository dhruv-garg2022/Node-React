from Services.IAM import create_user_initial
from Services.DB import store_user
from Services.EC2 import create_instance 
from Services.EC2 import show_instances
from Services.EC2 import stop_instance
from Services.EC2 import start_instance
from Services.EC2 import terminate_instance
from Services.S3 import create_bucket
from Services.S3 import list_bucket
from Services.S3 import delete_bucket
from Services.IAM import create_user
from Services.IAM import list_user
from Services.IAM import delete_user
from Services.IAM import generate_key
from Services.IAM import fetch_userid
from Services.DB import data_insertion
from Services.DB import data_deletion
from Services.DB import data_fetch
from Services.DB import fetch_instance
from Services.DB import fetch_buckets
from Services.DB import fetch_users
from Services.DB import insert_key
from Services.DB import generate_bill
from Services.DB import price
from Services.DB import payment
from Services.DB import get_database
from flask import *
app= Flask(__name__)
app.secret_key='mayur-innovaccer'

main_access_id = "AKIA32ULZ2HXATMGKYO7"
main_secret_key = "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"
access_id=""
secret_key=""
region = "us-east-1"

#home routes 


#for integration
@app.route('/yo')
def yo():
    userid = '123'
    return redirect('http://127.0.0.1:5001/newroute?userid={0}'.format(userid,))

@app.route('/newroute')
def newroute():
    userid=request.args.get('userid')
    print("\n\n\n\n",userid,"\n\n\n\n")
    return redirect('http://127.0.0.1:5001/')

#back to ecom
@app.route('/shop')
def shop():
    return redirect('http://0.0.0.0:5000/')

#home route
@app.route("/")
def index():
    # if session['userid']=='' or session['userName']=='':
    #     return redirect('http://127.0.0.1/')
    return render_template('index.html')

#create user at the time of registration
@app.route('/load')
def load():
    return render_template('take_info.html')

@app.route('/infotaken',methods=["POST"])
def infotaken():
    # global userid, userName
    if request.method == "POST":
        userid=request.form['userid']
        userName = request.form['userName']
        session['userid'] = userid
        session['userName'] = userName
        iamid = create_user_initial.create(userName,userid, main_access_id, main_secret_key, region)
        store_user.insert(userid,userName,iamid,"ecom_user")
        session['group']='ecom_user'
    return redirect(url_for('index'))

#bill generation
@app.route('/generatebill')
def bill():
    # global userName, userid
    servicesused = generate_bill.generate(session['userid'],session['userName'])
    prices=price.fetch()
    prices_dict={}
    for data in prices:
        prices_dict[data[0]]=float(data[1])
    return render_template('bill.html', services= servicesused, price=prices_dict)

#payment
@app.route('/pay')
def pay():
    services = session['list']
    payment.delete(services, session['userid'], session['userName'])
    return redirect(url_for('index'))

#login
@app.route('/login')
def login_aws_page():
    return render_template('login.html')

#save accessid and secretkey
@app.route('/setcreds', methods=["POST"])
def creds():
    if request.method == "POST":
        # global access_id, secret_key
        access_id = request.form['aci']
        secret_key = request.form['sak']
        session['access_id']=access_id
        session['secret_key'] = secret_key
        return redirect(url_for('index'))

#exist user
@app.route('/existuser')
def existuser():
    return render_template('existing_user.html')

#store userid and username of existing user
@app.route('/checkexistinguser', methods=["POST"])
def checkexistuser():
    if request.method == "POST":
        userid=request.form['userid']
        userName = request.form['userName']
        session['userid'] = userid
        session['userName'] = userName
        session['group']='ecom_user'
        return redirect(url_for('index'))

@app.route('/database')
def database():
    return render_template('database.html')
    # service = fetch_database.service()
    # access = fetch_database.access()
    # user = fetch_database.user()

@app.route('/access')
def access():
    access = get_database.access()
    return render_template('access.html',access=access)

@app.route('/service_used')
def service():
    services = get_database.service()
    return render_template('service.html',services=services)

@app.route('/user')
def user():
    users = get_database.user()
    return render_template('user.html',users=users)

#ec2 Routes

@app.route("/ec2")
def ec2():
    return render_template('ec2.html')

#creating an instance 
@app.route('/create')
def create():
    # global userid, userName
    id = create_instance.create_ec2instance(session['access_id'],session['secret_key'], region)
    data_insertion.insert(session['userid'],session['userName'], "EC2", id)
    return redirect(url_for('list'))

#show all instances
@app.route('/list')
def list():
    rows = fetch_instance.fetch(session['userid'], session['userName'])
    # print("\n\n\n\n\n\n\n",rows, "rows\n\n\n\n\n\n\n")
    instances=[]
    for instance in rows:
        instances.append(instance[0])
    # print("\n\n\n\n\n\n\n",instances, "instances\n\n\n\n\n\n\n")
    all_instances=[]
    response = show_instances.get_all_instances(session['access_id'],session['secret_key'], region)
    # print("\n\n\n\n\n\n\n",response, "response\n\n\n\n\n\n\n")
    check_instances=[]
    # print("Response",response)
    for reservation in response:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_state = instance['State']['Name']
            if instance_state == 'running':
                public_ip = instance["PublicIpAddress"]
                private_ip = instance["PrivateIpAddress"]
            else:
                public_ip = '-'
                private_ip = '-'
            check_instances.append(instance_id)
            if instance_id in instances:

                all_instances.append([instance_id,instance_state,public_ip,private_ip])
    # print("\n\n\n\n\n\n\n",check_instances, "check_instances\n\n\n\n\n\n\n")
    # print("\n\n\n\n\n\n\n",all_instances, "all_instances\n\n\n\n\n\n\n")
    return render_template('list_instance.html',instances=all_instances)

# @app.route('/stop')
# def stop():
#     return render_template('stop.html')

# @app.route('/stop_inst', methods=["POST"])
# def stop_inst():
#     if request.method=="POST":
#         id = request.form['id']
#         stop_instance.stop(id,access_id, secret_key ,region)
#         return redirect(url_for('list'))

# @app.route('/start')
# def start():
#     return render_template('start.html')

# @app.route('/start_inst', methods=["POST"])
# def start_inst():
#     if request.method=="POST":
#         id = request.form['id']
#         start_instance.start(id,access_id, secret_key, region)
#         return redirect(url_for('list'))

# @app.route('/terminate')
# def terminate():
#     return render_template('terminate.html')

# @app.route('/terminate_inst', methods=["POST"])
# def terminate_inst():
#     if request.method=="POST":
#         id = request.form['id']
#         terminate_instance.terminate(id,access_id, secret_key, region)
#         data_deletion.delete(userid,userName, "EC2", id)
#         return redirect(url_for('list'))

#stopinstance
@app.route('/stopinst/<id>')
def stopinst(id):
    stop_instance.stop(id,session['access_id'], session['secret_key'] ,region)
    return redirect(url_for('list'))

#start instance
@app.route('/startinst/<id>')
def startinst(id):
    start_instance.start(id,session['access_id'], session['secret_key'], region)
    return redirect(url_for('list'))  

#terminate instance
@app.route('/terminateinst/<id>')
def terminateinst(id):
    terminate_instance.terminate(id,session['access_id'], session['secret_key'], region)
    data_deletion.delete(session['userid'],session['userName'], "EC2", id)
    return redirect(url_for('list'))

#s3 Routes

@app.route("/s3bucket")
def s3bucket():
    return render_template('s3bucket.html')

#creating bucket
@app.route('/createbucket')
def createbucket():
    return render_template('createbucket.html')

#saving name of bucket and display
@app.route('/cbucket', methods=["POST"])
def cbucket():
    if request.method=="POST":
        name = request.form['bn']
        create_bucket.create(name, session['access_id'], session['secret_key'], region)
        data_insertion.insert(session['userid'],session['userName'], "s3", name)
        return redirect(url_for('listbucket'))

#show all buckets
@app.route('/listbucket')
def listbucket():
    response = list_bucket.list(session['access_id'], session['secret_key'], region)
    buckets = fetch_buckets.fetch(session['userid'], session['userName'])
    only_buckets = []
    for bucket in buckets:
        only_buckets.append(bucket[0])
    final_bucket = []
    for bucket in response["Buckets"]:
        if bucket["Name"] in only_buckets:
            final_bucket.append(bucket["Name"])
    return render_template('listbucket.html',response = final_bucket)
    # for bucket in response['Buckets']:
    #     print(bucket['Name'])

# @app.route('/deletebucket')
# def deletebucket():
#     return render_template('deletebucket.html')

# @app.route('/dbucket', methods=["POST"])
# def dbucket():
#     if request.method=="POST":
#         name = request.form['bn']
#         delete_bucket.delete(name, access_id, secret_key,region)
#         data_deletion.delete(userid,userName, "S3", name)
#         return redirect(url_for('listbucket')) 

#delete bucket
@app.route('/deletebucket/<name>')
def deletebucket(name):
    delete_bucket.delete(name, session['access_id'], session['secret_key'],region)
    data_deletion.delete(session['userid'],session['userName'], "s3", name)
    return redirect(url_for('listbucket')) 

# IAM routes

@app.route('/iam')
def iam():
    return render_template('iam.html')

#generation of accessid and secret key
@app.route('/generatekeys')
def generate_keys():
    # global userName, userid
    name = session['userName'] + session['userid']
    
    a_id = data_fetch.fetch(name)
    
    keys=generate_key.generate(name,a_id,main_access_id,main_secret_key,region)
    # print(keys, "\n\n\n\n\n\n\nkeys\n\n\n\n\n\n\n")
    insert_key.insert(name, keys[0])
    # print(keys, "\n\n\n\n\n\n\nkeys\n\n\n\n\n\n\n")
    return render_template('generate_key.html',keys=keys)

#create user
@app.route('/createuser')
def createuser():
    return render_template('create_user.html')

#passing details of user
@app.route('/createduser', methods=["POST"])
def cuser():
    # global userid, userName
    if request.method=="POST":
        name = request.form["username"]
        name=session['userName']+session['userid']+"-"+name
        print("\n\n\n",name,"\n\n\n")
        id = create_user.create(name,session['access_id'], session['secret_key'],region)
        data_insertion.insert(session['userid'],session['userName'], "iam", id)
        return redirect(url_for('listuser'))

# show users
@app.route('/listuser')
def listuser():
    users = list_user.list(session['access_id'], session['secret_key'],region)
    rows = fetch_users.fetch(session['userid'], session['userName'])
    final_rows = []
    for row in rows:
        final_rows.append(row[0])
    final_users = []
    for user in users:
        if user[1] in final_rows:
            final_users.append(user)
    return render_template('list_user.html',users=final_users)
    
# @app.route('/deleteuser')
# def deleteuser():
#     return render_template('delete_user.html')

# @app.route('/deleteduser', methods=["POST"])
# def duser():
#     if request.method=="POST":
#         name = request.form["username"]
#         id = fetch_userid.fetch_id(name,access_id, secret_key,region)
#         delete_user.delete(name,access_id, secret_key,region)
#         data_deletion.delete(userid,userName, "IAM", id)
#         return redirect(url_for('listuser'))


#delete user
@app.route('/deleteuser/<name>/<id>')
def deleteuser(name,id):
    
    delete_user.delete(name,session['access_id'], session['secret_key'],region)
    data_deletion.delete(session['userid'],session['userName'], "iam", id)
    return redirect(url_for('listuser'))

#progress routes

@app.route("/inprogress")
def progress():
    return render_template('inprogress.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port="5001")
    # app.run(host="",port="",debug=True)