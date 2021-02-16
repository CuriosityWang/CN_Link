# CN_Link
### 一键登录校园网源码讲解

![](https://i.loli.net/2021/01/23/tWG7825gKdQmyfX.png)

#### 为什么要做这个程序

一般在我们连接上校园网后,浏览器会自动弹出校园网的登录页面,要进入多步点击的过程,输入账号密码,还有点击登录.但是如果,在我连接上校园网之后,只需要简简单单的双击某个程序就能登录,岂不美哉!

##### 核心代码

```python
import requests as re

url = "http://192.168.255.195:8080/Control" # 校园网登录网址
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-CN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Length": "52",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.3"
}
data = {"id": 2000, "strAccount": 1548465556, "strPassword": 123123}
re.post(url, data, headers=header)
```

#### 完善的功能

用户的账号密码需要加密保存在本地,因此需要使用一定的加密解密算法

用户在控制台输入账号密码,密码应该是*显示

保证保存在本地的用户的账号和密码是正确的,因此也需要是否联网的判断


#### 基本思路

由于我已经回家,所以没法使用学校的校园网进行讲解了,故使用路由器的管理员登录页面进行说明.

**路由器管理员登录页面和校园网登录页面基本思想是一致的!!!**

更多请看https://www.bilibili.com/video/BV1XX4y1P7LN

