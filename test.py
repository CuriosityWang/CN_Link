import msvcrt
import os
import sys
import subprocess
import time
import rsa
import requests as re

url = "http://192.168.255.195:8080/Control"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-CN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Length": "52",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.3"
}

data = {"id": 2000, "strAccount": None, "strPassword": None}


def create_keys():  # 生成公钥和私钥
    if not os.path.exists("./yourdata"):
        os.mkdir("./yourdata")

    (pubkey, privkey) = rsa.newkeys(1024)
    pub = pubkey.save_pkcs1()
    with open('yourdata/AWF97iID.pem', 'wb+')as f:
        f.write(pub)

    pri = privkey.save_pkcs1()
    with open('yourdata/FdrMX7qBO5L.pem', 'wb+')as f:
        f.write(pri)


def encrypt(original_text):  # 用公钥加密
    with open('yourdata/AWF97iID.pem', 'rb') as AWF97iIDkfile:
        p = AWF97iIDkfile.read()
    pubkey = rsa.PublicKey.load_pkcs1(p)
    original_text = original_text.encode('utf8')
    crypt_text = rsa.encrypt(original_text, pubkey)
    f = open('./yourdata/FdrMX7q.data', 'wb')
    f.write(crypt_text)
    f.close()


def decrypt():  # 用私钥解密
    with open('yourdata/FdrMX7qBO5L.pem', 'rb') as FdrMX7qBO5Lfile:
        p = FdrMX7qBO5Lfile.read()
    privkey = rsa.PrivateKey.load_pkcs1(p)
    f = open('yourdata/FdrMX7q.data', 'rb')
    crypt_text = f.read()
    lase_text = rsa.decrypt(crypt_text, privkey).decode()  # 注意，这里如果结果是bytes类型，就需要进行decode()转化为str

    f.close()
    return lase_text


def pwd_input():
    print("请输入您的校园网密码:")
    chars = []
    while True:
        try:
            newChar = msvcrt.getch().decode(encoding="utf-8")
        except:
            return input("你很可能不是在cmd命令行下运行，密码输入将不能隐藏:")
        if newChar in '\r\n':  # 如果是换行，则输入结束
            break
        elif newChar == '\b':  # 如果是退格，则删除密码末尾一位并且删除一个星号
            if chars:
                del chars[-1]
                msvcrt.putch('\b'.encode(encoding='utf-8'))  # 光标回退一格
                msvcrt.putch(' '.encode(encoding='utf-8'))  # 输出一个空格覆盖原来的星号
                msvcrt.putch('\b'.encode(encoding='utf-8'))  # 光标回退一格准备接受新的输入
        else:
            chars.append(newChar)
            msvcrt.putch('*'.encode(encoding='utf-8'))  # 显示为星号
    return (''.join(chars))


def test1():
    flag = os.system('ping 8.8.8.8')
    if flag:
        sys.stdout.write('ping fail')
        os.system('msdt.exe /id NetworkDiagnosticsNetworkAdapter')  # 调用系统网络诊断
    else:
        sys.stdout.write('ping ok')


def test2():
    fnull = open(os.devnull, 'w')
    return1 = subprocess.call('ping 8.8.8.8', shell=True, stdout=fnull, stderr=fnull)
    if return1:
        return False

    else:
        fnull.close()
        return True


def Str_acc_pass(acc, password):
    # 判断输入的数据有无特殊字符
    # 有 返回 False
    # 无 返回 True
    if acc.isdigit() and password.isdigit():
        return True
    return False


def connect():
    try:
        re.post(url, data, headers=header)
    except:
        return False
    # 测试网络状态
    if test2():
        return True
    else:
        return False


def judge_local():
    # 判断本地有无已经存储的正确的账号密码
    file_list = os.listdir("./")
    if "yourdata" in file_list and (len(os.listdir("./yourdata")) == 3):
        return True
    return False


def have_data():

    data = eval(decrypt())
    sys.stdout.write("正在登录")
    re.post(url, data, headers=header)

    for i in range(3):
        time.sleep(0.5)
        sys.stdout.write(".")

    sys.stdout.write("\n登录成功, 程序将在2s后关闭\n")
    time.sleep(2)


def no_data():

    acc = input("请输入您的校园网账号:\n")
    password = pwd_input()

    # 检测账号密码是否是纯数字
    flag = Str_acc_pass(acc, password)

    # 判断输入的数据有无特殊字符
    while not flag:

        acc = input("\n您输入的账号或密码有误,请重新输入\n请输入您的校园网账号:\n")
        password = pwd_input()
        flag = Str_acc_pass(acc, password)

    data["strAccount"] = int(acc)
    data["strPassword"] = int(password)

    sys.stdout.write("\n正在尝试登录...")

    if connect():
        sys.stdout.write("\n连接成功,正在保存您的账户信息...\n")
        # 将字典转换成字符串加密保存在本地
        # 账号 密码加密存储
        create_keys()
        encrypt(str(data))
    else:
        sys.stdout.write("\n连接失败,这可能与您输入的账号密码或者当前网络环境有关\n")


if __name__ == '__main__':

    sys.stdout.write("这是一个自动登陆山师校园网的小程序,请在连接sdnu后使用\n")

    Flag = judge_local()
    if Flag:
        have_data()
        os.system("pause")
    else:
        no_data()
        os.system("pause")

