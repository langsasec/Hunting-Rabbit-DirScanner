# Hunting-Rabbit-DirScanner

A fast and easy-to-use directory scanning tool.

## Usage

```
Hunting-Rabbit-DirScanner author: Langsa

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Target URL
  -w THREADS, --threads THREADS
                        Number of threads, default is 150
  -d DICT, --dict DICT  Specify the dictionaries to use, multiple dictionaries can be separated by commas, default is
                        all
  -t TIMEOUT, --timeout TIMEOUT
                        Request timeout in seconds, default is 1.5
  -c STATUS_CODE, --status-code STATUS_CODE
                        Filter specific status codes, default is 200
  -rua, --random-ua     Randomly select User-Agent
```

## Examples

Default scan (using all dictionaries, 150 threads, return only 200 status code):

```
python Hunting-Rabbit-DirScanner.py -u https://www.baidu.com
```

Save results for 403 and 302 status codes:

```
python Hunting-Rabbit-DirScanner.py -u https://www.baidu.com -c 403,302
```

Scan with specific dictionaries:

```
python Hunting-Rabbit-DirScanner.py -u https://www.baidu.com -d jsp,api
```

## Help

1. Duplicates in dictionaries are automatically removed. The tool will not scan the same path multiple times.

2. Scan with custom headers (paste the headers from Burp Suite or browser).

3. Having too many threads or a short timeout duration may result in reduced output.

4. You can customize your own dictionaries and put them in the `dict` directory.

5. After the scan is completed, the recorded URLs will be saved in the `log` directory.

6. List of available dictionaries:

   ```
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
