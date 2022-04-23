
echo "Welcome to use CocoaPush By Luckykeeper in Docker!!!"
echo "github: https://github.com/luckykeeper/CocoaPush"
echo "当前系统参数如下所示:"
echo "调试模式 = ${debug}"
echo "WebHook 地址 = ${webhook_url}"
echo "关键词 = ${token}"
echo "CocoaServer 服务端口 = ${CocoaServer_port}"
echo "token = ${py_dingpusher_token}"

echo " —————————————————程序开始运行！———————————————————————"
echo "Powered By Luckykeeper<luckykeeper.site|luckykeeper@luckykeeper.site>"
echo " —————————————————代码和人必有一个能润起来！———————————————————————"

python3 /usr/src/app/CocoaServer_Docker.py