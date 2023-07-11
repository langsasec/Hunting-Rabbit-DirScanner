# -*- coding: UTF-8 -*-
# @Time:  21:57
# @Author: 浪飒
# @File: Hunting-Rabbit-DirScanner.py
# @Software: PyCharm


import argparse
import random
import threading
import signal
import sys
import requests
import glob

# 读取字典
import urllib3
from jinja2 import Template


def read_dir(url, dict_name):
    words = []
    if dict_name == "all":
        # 获取所有符合条件的文件路径
        file_paths = glob.glob("dict/*.txt")
        # 逐个打开并读取文件内容
        for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if url is not None:
                    words.extend([url + x.strip() for x in lines])
    else:
        dict_name = dict_name.split(',')
        for name in dict_name:
            with open(f"dict/{name}.txt", 'r', encoding="utf-8") as f:
                lines = f.readlines()
                if url is not None:
                    words.extend([url + x.strip() for x in lines])
    return words


# 随机UA
def Random_UserAgents():
    UserAgents = [

        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",

        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",

        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",

        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",

        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",

        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",

        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",

        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",

        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CL",

        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",

        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",

        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",

        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",

        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",

        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",

        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",

        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",

        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",

        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",

        "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",

        "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",

        "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12",

        "Opera/9.27 (Windows NT 5.2; U; zh-cn)",

        "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13",

        "Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 ",

        "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 ",

        "Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; F-01D Build/F0001) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 ",

        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; ja-jp) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7",

        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; da-dk) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5 ",

        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9 ",

        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",

        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",

        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36",

        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",

        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"

    ]
    UserAgent = random.choice(UserAgents)
    return UserAgent


def execute_threads(thread_num, worker):
    threads = []
    for i in range(thread_num):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def dir_scan(url, use_random_ua, timeout, status_code_filter="200"):
    headers = {}
    with open('header.config', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                key, value = line.split(': ', 1)
                headers[key] = value
    if use_random_ua:
        headers["User-Agent"] = Random_UserAgents()
    else:
        headers[
            "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    red = "\033[31m"
    green = "\033[32m"
    try:
        # ssl证书禁用警告
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # 发包
        req = requests.get(url, headers=headers, timeout=timeout, verify=False, allow_redirects=False)
        status_code = req.status_code
        # 如果状态码符合条件，则打印结果
        status_code_list = status_code_filter.split(",")
        status_code_list.append("200")
        if str(status_code) in status_code_list:
            print(green + f"[+] {url} - Status code: {status_code}")
            return url
    except:
        print(red + f"[-] {url} - Request encountered an exception")
        pass


def scan_log(name, links):
    name = name.replace("://", "-")
    name = name.replace("/", "-")
    log_file = f"log/{name}.html"
    template_str = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>目录扫描结果</title>
<style>
body {
  font-family: Arial, sans-serif;
  margin: 20px;
}

h1 {
  text-align: center;
}

.list-container {
  margin-top: 30px;
}

table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
}

th, td {
  padding: 8px;
  border-bottom: 1px solid #ddd;
  text-align: center;
  word-wrap: break-word;
}

th:nth-child(2),
td:nth-child(2) {
  position: relative;
}

th:nth-child(2)::after,
td:nth-child(2)::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 100%;
  transform: translateY(-50%);
  height: 80%;
  width: 1px;
  background-color: #ddd;
}

th:first-child,
td:first-child {
  width: 20%;
}

th:last-child,
td:last-child {
  width: 80%;
}

tr:hover {
  background-color: #f5f5f5;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

/* 增加垂直分割线 */
td:not(:first-child)::before {
  content: '';
  display: block;
  height: 100%;
  width: 1px;
  background-color: #ddd;
  position: absolute;
  left: 0;
  top: 0;
}

/* 增加水平分割线 */
tr:not(:first-child) td {
  border-top: 1px solid #ddd;
}

.footer {
  margin-top: 30px;
  text-align: center;
  font-size: 12px;
  color: #888;
}
</style>
</head>
<body>
<h1>目录扫描结果</h1>
<div class="list-container">
  <table>
    <tr>
      <th>序号</th>
      <th>URL地址</th>
    </tr>
    {% for link in links %}
    <tr>
      <td>{{ loop.index }}</td>
      <td><a href="{{ link }}" target="_blank">{{ link }}</a></td>
    </tr>
    {% endfor %}
  </table>
</div>
<div class="footer">
  &copy; 2023 Hunting-Rabbit-DirScanner. All rights reserved. <a href="https://github.com/langsasec/Hunting-Rabbit-DirScanner">Github</a>
</div>
</body>
</html>

"""

    template = Template(template_str)
    output = template.render(links=links)

    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(output)


# main
def main():
    parser = argparse.ArgumentParser(description="Hunting-Rabbit-DirScanner  author: 浪飒")
    parser.add_argument("-u", "--url", type=str, required=True, help="Target URL")
    parser.add_argument("-w", "--threads", type=int, default=200, help="Number of threads, default is 200")
    parser.add_argument("-d", "--dict", type=str, default="all",
                        help="Specify the dictionaries to use, multiple dictionaries can be separated by commas, default is all")
    parser.add_argument("-t", "--timeout", type=float, default=1.5, help="Request timeout in seconds, default is 1.5")
    parser.add_argument("-c", "--status-code", type=str, default="200",
                        help="Filter specific status codes, default is 200")
    parser.add_argument("-rua", "--random-ua", action="store_true", help="Randomly select User-Agent")

    args = parser.parse_args()
    url = args.url
    thread_num = args.threads
    dict_name = args.dict
    timeout = args.timeout
    status_code_filter = args.status_code
    use_random_ua = args.random_ua

    words = read_dir(url, dict_name)
    result = []

    def worker(i):
        global is_paused
        while words:
            word = words.pop()
            url = dir_scan(word, use_random_ua, timeout, status_code_filter)
            if url is None:
                pass
            else:
                result.append(url)
            while is_paused:
                while is_paused:
                    sys.exit(0)

    execute_threads(thread_num, worker)

    if result==[]:
        print("[-] No result!")
    else:
        scan_log(url, result)
    reset = "\033[0m"
    print(
        reset + "[Hunting-Rabbit-DirScanner]: Directory scan completed. Scan results have been saved to the 'log' folder.")


if __name__ == '__main__':
    is_paused = False


    # 定义一个信号处理函数
    def signal_handler(sig, frame):
        global is_paused
        if is_paused:
            print("继续执行线程")
            is_paused = False
        else:
            print("暂停线程")
            is_paused = True


    # 注册信号处理函数
    signal.signal(signal.SIGINT, signal_handler)
    main()
