# Hunting-Rabbit-DirScanner(猎兔目录扫描器)

一款快速易上手的目录扫描工具。

进入 [英文文档](https://github.com/langsasec/Hunting-Rabbit-DirScanner/blob/main/README_EN.md)

## 使用方法

```sh
Hunting-Rabbit-DirScanner 作者：浪飒

参数选项：
  -h, --help            显示帮助信息并退出
  -u URL, --url URL     目标URL
  -w THREADS, --threads THREADS
                        线程数，默认为150
  -d DICT, --dict DICT  指定要使用的字典，可以使用逗号分隔多个字典， 默认为全部
  -t TIMEOUT, --timeout TIMEOUT
                        请求超时时间（秒），默认为1.5
  -c STATUS_CODE, --status-code STATUS_CODE
                        过滤特定的状态码，默认为200
  -rua, --random-ua     随机选择User-Agent
```

## 示例

默认扫描（使用所有字典，150个线程，仅返回状态码为200的结果）：

```sh
python Hunting-Rabbit-DirScanner.py -u https://www.baidu.com
```

保存403和302状态码的结果：

```sh
python Hunting-Rabbit-DirScanner.py -u https://www.baidu.com -c 403,302
```

指定字典进行扫描：

```sh
python Hunting-Rabbit-DirScanner.py -u https://www.baidu.com -d jsp,api
```

## 帮助

1. 字典会自动去重，不会重复扫描相同的路径。

2. 可自定义请求头，可选择从burpsuite或浏览器中粘贴请求头。

3. 线程太多或超时时间太短会导致输出结果减少。

4. 可以自定义字典并将其放入`dict`目录中。

5. 扫描完毕后会将所记录url记录到`log`目录中。

6. 可用字典列表：

   ```sh
   apache.txt
api.txt
ASP.TXT
aspx.txt
axis.txt
cgis.txt
coldfusion.txt
ctf.txt
DIR.txt
domino.txt
editor.txt
espcms.txt
fatwire.txt
fatwire_pagenames.txt
FCKeditor编辑器.txt
frontpage.txt
gn2023.txt
hpsmh.txt
hyperion.txt
iis.txt
iplanet.txt
jboss.txt
jersey.txt
JoekoeCMS.txt
jrun.txt
jsp.txt
MDB.txt
netware.txt
oracle.txt
php.txt
phpcms.txt
phpweb.txt
ror.txt
S2命令执行.txt
sap.txt
sharepoint.txt
shopex.txt
spring.txt
sunas.txt
tests.txt
ThinkPHP.txt
tomcat.txt
top7000.txt
ueditor.txt
vignette.txt
weblogic.txt
websphere.txt
wordpress.txt
Z-BLOG.txt
乔客.txt
其他CMS.txt
动力.txt
动易.txt
动网.txt
千博.txt
南方数据.txt
夏茂OA.txt
天天团购.txt
汇成cms.txt
科讯.txt
织梦.txt
西部商务.txt
迪科.txt
逐浪cms.txt
风讯.txt
风讯foosunCMS.txt
   ```
