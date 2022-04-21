# CocoaClient 心爱酱的分身，示例通过 ping\socket\request 探测服务状态，向本体回报信息
# Author:Luckykeeper <luckykeeper@luckykeeper.site>|https://luckykeeper.site>
# last modified:2022-04-32
# 依赖：ping3 requests

###############################################################################
# 基础设置

# 统一推送中心服务器 ip ，填 CocoaServer 地址
server = "192.168.0.1"

# 统一推送中心服务器端口（UDP），填 CocoaServer 的端口
port = int(22119)

# requests 超时时间
req_timeout = 10

# 其它机器使用本服务的 token （这里是随机生成，自己使用时请务必再去随机生成一个放在这里），填 CocoaServer 的 py_dingpusher_token
py_dingpusher_token = "KxA0ubjN8DMZCKrhS19uhKB2EYYnpNm60S3"

# 调试模式
debug = True

import socket,requests,datetime,time
from ping3 import ping

# 程序开始计时
start_time = time.time()
now_time = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

print ("心爱酱消息推送服务 By Luckykeeper 已经开始运行!")
print ("#####基础设定#####")
print ("统一推送中心地址： ",server,port)

print("—————————————————————————————————————————————————————————————————————————————")

# 定义发送消息方法
def send_msg(msg,udp_socket: socket.socket):

    message = "token:"+py_dingpusher_token+";msg:"+msg

    udp_socket.sendto(message.encode('utf-8'), (server, port))

# 初始化
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 获取本机ip
localip = str(socket.gethostbyname(socket.getfqdn(socket.gethostname())))

# 爬虫伪装
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    }

# 定义检测任务
def CocoaCheck():
    # 01 ping 方法检测示例

    device16811 = "192.168.1.1"
    ping16811_result = ping(device16811)
    if ping16811_result != None:
        ping16811 = "👌可 Ping 通，"
        if debug:
            print("可 Ping 通")
    else:
        if debug:
            print("不可 Ping 通")
        ping16811 = "😰不可 Ping 通，"

    # 02 requests 方法检测示例
    try:
        web16811_status =  requests.get(url="https://192.168.1.1/", headers=headers,timeout=req_timeout,verify=False) # 自签证书verify=False，正常证书或http不需要加这个参数
        if web16811_status.status_code == 200:
            if debug:
                print("WEB正常!")
            req16811 = "👍 web 管理正常，"
        else:
            if debug:
                print("WEB它寄了!")
            req16811 = "⚠ web 管理异常，"
    except:
        req16811 = "⚠ web 管理异常，"

    # 总结设备状态
    status16811 = ping16811+req16811

    # 03 socket 检测端口方法，此例检测 ssh 是否开放
    try:
        ssh_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssh_sock_result = ssh_sock.connect_ex(("192.168.1.1",22))
        if ssh_sock_result == 0:
            socks_ssh = "👍 ssh 服务正常\n"
        else:
            socks_ssh = "⚠ ssh 服务异常\n"
    except:
        socks_ssh = "⚠ ssh 服务异常\n"

    ssh = socks_ssh

    # 顺序返回
    return status16811,ssh

getmsg = CocoaCheck()

end_time = time.time()
total_time = str(end_time - start_time)
msg = "# LuckyCocoa 服务综合测试\n 检测时间："+now_time+\
        "\n> 网关设备状态："+getmsg[0]+\
        "\n> ssh状态："+getmsg[1]+\
        "\n 检测总用时："+total_time+"秒"
# 发送消息
try:
    send_msg(msg,udp_socket)
    if debug:
        print ("发送信息：",msg)
        print ("发送成功")
except:
    if debug:
        print ("发送失败")

    pass