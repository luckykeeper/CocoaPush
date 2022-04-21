# CocoaServer 心爱酱钉钉推送机器人——服务端
# Author:Luckykeeper <luckykeeper@luckykeeper.site>|https://luckykeeper.site>
# last modified:2022-04-21
# 服务端依赖：DingtalkChatbot

# 心爱酱 Cocoa : https://github.com/luckykeeper/LOVE69_renpy_remaster
###############################################################################
# 基础设置

# WebHook URL 填自己的钉钉机器人 webhook 回调地址
WebHook_URL = "https://oapi.dingtalk.com/robot/send?access_token=123456"
# 关键词 机器人安全设置选择关键词，填在这里（Token）
Token = "来自心爱酱的提醒"
# 调试模式
debug = True
# 监听端口(UDP)，listenHOST 不需要改，Port看情况
listenHOST = '0.0.0.0'
listenPort = int(22119)
# 其它机器使用本服务的 token （这里是随机生成，自己使用时请务必再去随机生成一个放在这里）
py_dingpusher_token = "KxA0ubjN8DMZCKrhS19uhKB2EYYnpNm60S3"

# 钉钉推送
from dingtalkchatbot.chatbot import DingtalkChatbot
# UDP 监听
import socketserver

# 初始化心爱酱
LuckyCocoa = DingtalkChatbot(WebHook_URL)

# # 测试 Markdown ，需要发送 Markdown 像下面这样
# LuckyCocoa.send_markdown(title=Token, text='#### 奶糖苹果被抢走了~~~\n'
#                        '> 呜欸欸欸欸欸欸——\n')

# 定义 CocoaServerUDPHandler 类
class CocoaServerUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        orgData = bytes.decode(self.request[0].strip())  # 读取数据
        if debug == True:
            print("原始数据:",orgData) # Debug:输出接收的数据
            # print(type(orgData)) # type class 'str'
            print("—————————————————————————————————————————————————————————————————————————————")

        # 校验 py_dingpusher_token ，正确了才能发送消息，否则忽略
        pre_check_dingpusher_token = orgData.split(";msg:")[0]
        check_dingpusher_token = pre_check_dingpusher_token.split("token:")[1]
        if py_dingpusher_token == check_dingpusher_token:
            if debug:
                print("token 校验成功，王大队长，是自己人!")

            msg = orgData.split(";msg:")[1]
            if debug:
                print("将让心爱酱传达以下消息:\n ",msg)
            LuckyCocoa.send_markdown(title=Token, text=msg)

        else:
            if debug:
                print("如果你真没下毒，你就把这碗鸡汤喝了!")
            pass

# 初始化监听服务器
try:
    server = socketserver.UDPServer((listenHOST, listenPort), CocoaServerUDPHandler)  # 绑定本地地址，端口和CocoaServer处理方法
    print("CocoaServer By Luckykeeper Service Started And Ready to Handle Push Data!!!")
    print("CocoaServer Server listening on:",listenHOST,listenPort,"(udp)")
    if debug == False:
        print("Debug Mode:OFF!")
    else:
        print("Debug Mode:ON!")
    print("—————————————————————————————————————————————————————————————————————————————")
    server.serve_forever(poll_interval=0.5)  # 运行服务器，轮询间隔0.5

except (IOError, SystemExit): # 崩溃处理
    raise