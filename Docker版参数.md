示例

```bash
docker run -itd -e debug="True" -e webhook_url="https://oapi.dingtalk.com/robot/send?access_token=123456" -e token="来自心爱酱的提醒" -p 22119:22119/udp --name=cocoapush luckykeeper/cocoapush
```

参数

| 参数                | 选项                 | 默认值                              | 说明                                             |
| ------------------- | -------------------- | ----------------------------------- | ------------------------------------------------ |
| debug               | 可选                 | False                               | 调试模式                                         |
| webhook_url         | 必选                 | 无                                  | 钉钉 Webhook URL                                 |
| token               | 必选                 | 无                                  | 钉钉关键词                                       |
| CocoaServer_port    | 可选                 | 22119                               | CocoaServer服务端口                              |
| py_dingpusher_token | 可选（强烈推荐传参） | KxA0ubjN8DMZCKrhS19uhKB2EYYnpNm60S3 | CocoaServer客户端验证key，生产环境请生成一个使用 |

