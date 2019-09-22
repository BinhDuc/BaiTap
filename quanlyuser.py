import os

danhsachuser=[]
def load_user_luckhoidong():
    files = os.listdir("danhsach")
    if "user.csv" not in files:
        return

    with open('danhsach/user.csv' , 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                user = {}
                user["id"] = str_to_reads[0]
                user["username"] = str_to_reads[1]
                password = str_to_reads[2]
                if password.endswith('\n'):
                    password = password[0:len(password)-1]
                user['pass'] = password
                danhsachuser.append(user)
            line=f.readline()
    print("danhsachuser:",danhsachuser)

load_user_luckhoidong()
def xem_user(id=None):
    if id is None:
        id = input("xin moi nhap id user : ")
    for user in danhsachuser:
        if user["id"] == id:
            print(user)
            return user

def tao_user():
    user={}
    while True:
        id = input("xin moi nhap id user : ")
        tim_id_daco = xem_user(id)
        if tim_id_daco is not None:
           print("da ton tai user nay.xin moi ban thuc hien chuc nang khac")
           return

        user["id"]=id
        user["username"]=input("username: ")
        password = input("password : ")
        confirmpassword = input("confirm password : ")
        if password==confirmpassword:
            user["pass"]=password
            danhsachuser.append(user)
            str_to_save = user["id"] + "#" + user["username"] + user['pass'] + '\n'
            with open('danhmuc/user.csv', 'a') as f:
                data = f.write(str_to_save)
            return data
        else:
            print("khong khop voi password")

def delete_user(id=None):
    if id is None:
        id = input("xin moi nhap id user : ")
    for i in range(len(danhsachuser)):
        if id == danhsachuser[i]['id']:
            del danhsachuser[i]

            return
def login_user():
    timthay = False
    while timthay is False:
        username = input("username: ")
        password = input("password: ")
        for user in danhsachuser:
            if username == user['username'] and password == user['pass']:
                print("Dang nhap thanh cong")
                timthay = True
