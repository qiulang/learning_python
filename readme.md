## 2021 4.22 开始第三个年头

### timeit

node.js 没有类似 python timeit的包，https://www.npmjs.com/package/timeit 七年前，太老了，能不能自己给它改改

首先把python timeit 再好好熟悉下 [How to use timeit module](https://stackoverflow.com/questions/8220801/how-to-use-timeit-module) 起因是发现node16的async/await 性能还不如 node 12

1. [Simple practical example to see faster async functions and promises from node 10 to node 12, and up](https://stackoverflow.com/questions/64886560/simple-practical-example-to-see-faster-async-functions-and-promises-from-node-10)
2. [with node16 I see performance of async/await is worse than node 12](https://github.com/nodejs/node/issues/38339)
3. [How do I measure the execution time of JavaScript code with callbacks?](https://stackoverflow.com/questions/10617070/how-do-i-measure-the-execution-time-of-javascript-code-with-callbacks)
4. [How to measure time taken by a function to execute](https://stackoverflow.com/questions/313893/how-to-measure-time-taken-by-a-function-to-execute)
5. https://fibjs.org/en/docs/guide/about.md.html [Embrace high energy] section



### git 问题

[git push failed to push to github, but git push -vv can](https://stackoverflow.com/questions/67210965/git-push-failed-to-push-to-github-but-git-push-vv-can) 碰到好几次

显示一个commit 改动过的文件 `git show --stat --name-only  <commit-hash>` 

[git subtree pull --squash bug if the pulled codes rebase before?](https://stackoverflow.com/questions/67264736/git-subtree-pull-squash-bug-if-the-pulled-codes-rebase-before)



### 4.26

#### Pragmatic Programmer

The Pragmatic Programmer: 20th Anniversary Edition， 第一版我当年应该还是有些收货，第二版有什么更新有点好奇

1. https://www.endpoint.com/blog/2020/10/16/the-pragmatic-programmer-20th-anniversary-edition

2. [5 Essential Takeaways From “The Pragmatic Programmer”](https://betterprogramming.pub/5-essential-takeaways-from-the-pragmatic-programmer-6bb3db986294)

   

### 5.6

http://neuralnetworksanddeeplearning.com/chap1.html

[brew install httpie will install python too instead of using my existing pyhton](https://github.com/httpie/httpie/issues/1051)

[What is a shim?](https://medium.com/@ujjawal.dixit/what-is-a-shim-72d9ac5d8620) 其实就是改路径

[How do I mitigate the situation when Redia has not cached an expensive DB query?](https://stackoverflow.com/questions/67411387/how-do-i-mitigate-the-situation-when-redia-has-not-cached-an-expensive-db-query)



#### Cache Stampede

1. https://kkc.github.io/2020/03/27/cache-note/

2. [What is Cache Stampede ?](https://medium.com/@vaibhav0109/cache-stampede-problem-5eba782a1a4f)

   1. Locking.

   2. External Computation. 就是另外起一个服务器不停算

   3. Internal Computation using Probabilistic early expiration. 过期前再算一下
   
3. https://engineering.convertkit.com/2019/10/29/we-built-our-own-cache.html 也是列以上三条。关于锁的做法

   > If another request comes in and encounters a cache miss with a global lock for a key it will wait for 2 seconds (this value is configurable as well) trying to fetch a value from cache and then will bypass cache completely retrieving the value from underlying applications and will return a response.

4. https://pypi.org/project/python-redis-lock/

5. [How a Cache Stampede Caused One of Facebook’s Biggest Outages](https://betterprogramming.pub/how-a-cache-stampede-caused-one-of-facebooks-biggest-outages-dbb964ffc8ed) [对应的中文翻译](https://www.infoq.cn/article/bb2yc0yhvsz4qvwdgzmo) 里面提到 Instagram 用的一个方法，缓存promise,所以其他请求都得到同一个promise，最终得到结果。

6. [Thundering Herds & Promises](https://instagram-engineering.com/thundering-herds-promises-82191c8af57d) 讲缓存promise

7. https://redis.io/commands/setnx 设置锁有问题，所以建议 https://redis.io/topics/distlock

8. https://redislabs.com/blog/caches-promises-locks/ 没时间再看了



### 5.7

#### 安装python

`.zprofile`  & `PATH="/usr/local/bin:$PATH"`  

[Install python3 from Homebrew vs the installer from https://www.python.org/?](https://apple.stackexchange.com/questions/403041/install-python3-from-homebrew-vs-the-installer-from-https-www-python-org) 补充下我以前问的这个问题

brew 安装文档里没找到  `PATH="/usr/local/bin:$PATH"`  的说明，但说了 [Amending PATH so that /usr/local/bin is ahead of /usr/bin](https://apple.stackexchange.com/questions/49389/amending-path-so-that-usr-local-bin-is-ahead-of-usr-bin)  （`brew doctor`可以看到）

但是安装文档提到了我看到问题单，设置镜像源  https://docs.brew.sh/Installation#git-remote-mirroring 



### 5.10

#### Two-Factor Authentication code

[Two factor Auth code sent to same device](https://apple.stackexchange.com/questions/285597/two-factor-auth-code-sent-to-same-device)  "something you know" vs  "something you have"

[Does iCloud Two-factor authentication send a code to the same device as a log in request?](https://apple.stackexchange.com/questions/278839/does-icloud-two-factor-authentication-send-a-code-to-the-same-device-as-a-log-in) 发送到你信赖的设置，而且是通知，不是阻止。



### 5.18

#### nested list comprehensions

去年 [12.20](./readme2.md) 接触过一次，”the order of for loop inside the list comprehension is based on the order in which they appear in traditional loop approach. Outer most loop comes first, and then the inner loops subsequently.“ 

进一步理解两个常用使用场景，1. [把matrix 拉平](https://spapas.github.io/2016/04/27/python-nested-list-comprehensions/)

```python
non_flat = [ [1,2,3], [4,5,6], [7,8] ]
[y for x in non_flat for y in x]
[1, 2, 3, 4, 5, 6, 7, 8]

# https://stackoverflow.com/questions/18551458/how-to-frame-two-for-loops-in-list-comprehension-python
result = []

for tag in tags:
    for entry in entries:
        if tag in entry:
            result.extend(entry)
# 改成            
[entry for tag in tags for entry in entries if tag in entry]
```



2. 不是拉平，而是保持原来matrix shape, [List comprehension on a nested list?](https://stackoverflow.com/questions/18072759/list-comprehension-on-a-nested-list) 

两个答案，但是还是保持loop的好记

```python
l = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], ['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], ['100', '100', '100', '100']]
newList = []
for x in l:
  for y in x:
    newList.append(float(y))
#两个做法    
[[float(y) for y in x] for x in l]
#或者 这样好记好理解
[float(y) for x in l for y in x]
```



#### numpy和pandas中 axis(軸)的概念

 [numpy axis概念整理筆記](http://changtw-blog.logdown.com/posts/895468-python-numpy-axis-concept-organize-notes)

0是Y轴 ， 1 是 X轴 所以 以下例子, https://numpy.org/doc/stable/reference/generated/numpy.apply_along_axis.html

```python
def my_func(a):
    """Average first and last element of a 1-D array"""
    return (a[0] + a[-1]) * 0.5
b = np.array([[1,2,3], [4,5,6], [7,8,9]])
np.apply_along_axis(my_func, 0, b)
array([4., 5., 6.])
np.apply_along_axis(my_func, 1, b)
array([2.,  5.,  8.])
```



### 5.19

#### apline DNS problem

[What is the difference between alpine docker image and busybox docker image?](https://stackoverflow.com/questions/67529042/what-is-the-difference-between-alpine-docker-image-and-busybox-docker-image)

[musl-libc - Alpine's Greatest Weakness](https://www.linkedin.com/pulse/musl-libc-alpines-greatest-weakness-rogan-lynch/?trackingId=FsMR%2BhJfQqyOH9e1MIN0jw%3D%3D) 描述DNS失败问题

[Solving DNS lookup failures in Kubernetes](https://tech.findmypast.com/k8s-dns-lookup/) 没细看

https://github.com/gliderlabs/docker-alpine/blob/master/docs/caveats.md#dns 提到用 "it can help to run a local caching DNS server such as dnsmasq, that can be used for both caching and search path routing" 就是这次我们加的，但是 dnsmasq具体怎么用没细研究。

[Does Alpine have known DNS issue within Kubernetes?](https://stackoverflow.com/questions/65181012/does-alpine-have-known-dns-issue-within-kubernetes)

[I thought I understood Docker until I saw the BusyBox docker image](https://stackoverflow.com/questions/33291458/i-thought-i-understood-docker-until-i-saw-the-busybox-docker-image) 找一个回答者回答了我的问题



### 5.20

#### pandas for DB 

2019.12 第一次写sql 相关脚本，但是当然没想到可以用pandas，这是当时学习文章 [Python Select from MySQL Table](https://pynative.com/python-mysql-select-query-to-fetch-data/)

这次根据 [Working with SQLite Databases using Python and Pandas](https://www.dataquest.io/blog/python-pandas-databases/)

- It doesn’t require us to create a `Cursor` object or call `fetchall` at the end.
- It automatically reads in the names of the headers from the table.
- It creates a DataFrame, so we can quickly explore the data.

[What's the difference between lists enclosed by square brackets and parentheses in Python?](https://stackoverflow.com/questions/8900166/whats-the-difference-between-lists-enclosed-by-square-brackets-and-parentheses)

[Python List vs. Array - when to use?](https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use)



https://realpython.com/pandas-dataframe/ 在看

Pandas uses the attribute `john.name`, which is the value `17`, to specify the label for the new row.

```
>>> john = pd.Series(data=['John', 'Boston', 34, 79],
...                  index=df.columns, name=17)
df = df.append(john)
df = df.drop(labels=[17])
```



### 5.21

#### pandas

[10 Amazing Applications of Pandas – Which Industry Segment is Using Python Pandas?](https://data-flair.training/blogs/applications-of-pandas/)

https://realpython.com/pandas-dataframe/ 已看完 https://realpython.com/pandas-python-explore-dataset/ 周末看

[What is the difference between using squared brackets or dot to access a column?](https://stackoverflow.com/questions/41130255/what-is-the-difference-between-using-squared-brackets-or-dot-to-access-a-column) 

”There are several ways to index a Pandas DataFrame. One of the easiest ways to do this is by using square bracket notation.“



### 5.31

#### SELECT ... FOR UPDATE NOWAIT

[`SELECT ... FOR UPDATE`](https://dev.mysql.com/doc/refman/8.0/en/select.html) 8.0 引入 `NOWAIT` ， 5.7 没有，问了 [How do I Implement select … for update NOWAIT (sort of) for mysql 5.7 in python?](https://stackoverflow.com/questions/67770407/how-do-i-implement-select-for-update-nowait-sort-of-for-mysql-5-7-in-pytho)

这个没细看 [mysql python concurrent access on same table column](https://stackoverflow.com/questions/15351074/mysql-python-concurrent-access-on-same-table-column) 从 [Bill Karwin](https://stackoverflow.com/users/20860/bill-karwin) 答复知道 `select .. for update`

起因是 [Post-Upgrade Scripting for Containers in Kubernetes](https://stackoverflow.com/questions/46924181/post-upgrade-scripting-for-containers-in-kubernetes) 知道了[`PostStart`](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/)

[WL#3597: Implement NOWAIT and SKIP LOCKED](https://dev.mysql.com/worklog/task/?id=3597)



### 6.1 

#### `nowait` cont.

[How do I make sure a task run only once in a dockerized environment?](https://softwareengineering.stackexchange.com/questions/426902/how-do-i-make-sure-a-task-run-only-once-in-a-dockerized-environment)

```sql
UPDATE your_table
SET running_update = 1
WHERE running_update = 0

// check the count of rows updated, 实际更新的返回1 ，没更新的返回0
```



### 6.2

#### crash question

一个相关问题 [When a thread/process crashes on acquired DB locks, how does DB detects that and releases the lock?](https://dba.stackexchange.com/questions/292592/when-a-thread-process-crashes-on-acquired-db-locks-how-does-db-detects-that-and)

搜到两个相关问题，他们答复是说要等 `[wait_timeout](http://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_wait_timeout)` 确实8小时！

[Setting a time limit for a transaction in MySQL/InnoDB](https://serverfault.com/questions/241823/setting-a-time-limit-for-a-transaction-in-mysql-innodb)

[MySQL rollback on transaction with lost/disconnected connection](https://stackoverflow.com/questions/9936699/mysql-rollback-on-transaction-with-lost-disconnected-connection)

[effective innodb_lock_wait_timeout value check](https://stackoverflow.com/questions/16960261/effective-innodb-lock-wait-timeout-value-check)

```
show variables like 'innodb_lock_wait_timeout';
```



### 6.7

#### MySQL driver

https://pypi.org/project/mysql-connector-python/ 这是应该用的mysql驱动 ，这篇 https://pynative.com/python-mysql-database-connection/  （在2019时候也是看这篇） **Updated on: March 9, 2021**  也提到用这个启动，其他的驱动安装都是错的

```python
pip3 install mysql-connector
pip3 install mysql
pip3 install MySQL-python
# 这才是正确的
pip3 install mysql-connector-python
```



有 `for update` 就是串行，执行效果明显



#### pipreqs vs pigar

[mysql_connector_repackaged==0.3.1 is totally wrong](https://github.com/bndr/pipreqs/issues/261) 大bug，[pigar](https://github.com/Damnever/pigar) 是对的，pigar来源于 [Automatically create requirements.txt](https://stackoverflow.com/questions/31684375/automatically-create-requirements-txt)

SO 问类似问题不少，比如 [List dependencies in Python](https://stackoverflow.com/questions/42237072/list-dependencies-in-python) "Scan your `import` statements."是正解，因为没想到pipreqs居然会搞错。

创建 mysql driver 名字错误可能原因 [What are the differences between mysql-connector-python, mysql-connector-python-rf and mysql-connector-repackaged?](https://stackoverflow.com/questions/34168651/what-are-the-differences-between-mysql-connector-python-mysql-connector-python)

但是在单位安装 pigar总是报错，回家了就好了，又是网络问题。

想要google pipreqs 和 pigar的比较 发现这个 https://pypi.org/project/rqmts/ 当然我不会用它，但他说的理由可以看看，但是反对pigar 理由莫名其妙

  > Why re-invent the wheel
  >
  > - **pipreqs** fails on many occasions *(see - [pipreqs/issues](https://github.com/bndr/pipreqs/issues))*
  > - **pigar** queries pypi servers, big no-no. Ideally, it should be local, on fallback? then maybe. Other than that, **pigar** recommends using Pipenv ([pipenv has serious issues](https://news.ycombinator.com/item?id=18612590))
  > - **poetry** quotes "Be aware, however, that it will also install poetry's dependencies which might cause conflicts."
  > - Sheer curiousity. *"can I create a project that has potential of collecting thosands of stars and most importantly, hundreds of contributors?"*



#### python-dotenv

https://github.com/theskumar/python-dotenv   注意  [Profile specific environment variable](https://github.com/theskumar/python-dotenv/issues/73) : `load_dotenv('.env.local')`

#### class name

[If the convention in Python is to capitalize classes, why then is list() not capitalized? Is it not a class?](https://stackoverflow.com/questions/14973963/if-the-convention-in-python-is-to-capitalize-classes-why-then-is-list-not-cap)



### 6.8

#### mysql-connector

[MySQL Connector/Python: How to use the start_transaction() method?](https://stackoverflow.com/questions/52723251/mysql-connector-python-how-to-use-the-start-transaction-method)

> autocommit is disabled by default and the first SQL statement will implicitly begin a transaction... must call [`connection.commit`](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-commit.html) to commit the transaction.



https://github.com/qiulang/mysql  总结我发现问题，mysql总是能马上发现一个process 没有close connection 然后让另一个再等这个锁的进程获得锁, 到底是如果做到的？



### 6.10

#### mysql

https://pynative.com/python-database-connection-pooling-with-mysql/  这个网站 google mysql python 排名靠前，还有这个 https://overiq.com/mysql-connector-python-101/ 但没法解答我目前碰到的问题。而且基本步骤就是这7步



1. Create connection
2. Create cursor
3. Create Query string
4. Execute the query
5. Commit to the query
6. Close the cursor
7. Close the connection



[Pythonic way to create a long multi-line string](https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string) 以前解决过

> triple quotes  ... anything between the starting and ending quotes becomes part of the string, so this example has a leading blank and newlines.
>
> This will **not** include any extra blanks or newlines

```python
 s = ("this is a very"
      "long string too"
      "for sure ..."
     )
```



[When a process holds an exclusive row lock return without commit or close the connection, how does MySQL Connector/Python detect that?](https://stackoverflow.com/questions/67915122/when-a-process-holds-an-exclusive-row-lock-return-without-commit-or-close-the-co)



### 6.17

#### pipreqs 问题

[Pipreqs generate incorrect requiremnets for Hydra](https://stackoverflow.com/questions/67022499/pipreqs-generate-incorrect-requiremnets-for-hydra) pipreqs 还是错，pigar是对的

[Pip freeze for only project requirements](https://stackoverflow.com/questions/32390291/pip-freeze-for-only-project-requirements) "I have tried both `pipreqs` and `pigar` and found `pigar` is better because it also generates information about where it is used, it also has more options."

[Find which version of package is installed with pip](https://stackoverflow.com/questions/10214827/find-which-version-of-package-is-installed-with-pip) `pip show`  https://pip.pypa.io/en/stable/cli/pip_show/



### 6.21

#### 安装 tensorflow

deep learning 第二章最后几节看得有点囫囵吞枣，今天直接跳到 3.1.3 但是下单买了中文版，想看看跳过地方翻译是不是做得不错。

比如 3.1.3 stochastic gradient descent (SGD) 到底翻译成什么？

`pip install tensorflow` 总是失败，即便连的是清华的源

[Can pip.conf specify two index-url at the same time?](https://stackoverflow.com/questions/30889494/can-pip-conf-specify-two-index-url-at-the-same-time) 


```shell
缺省的源是  https://pypi.python.org/simple/
我已经改成  pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
设置vpn 然后运行 pip install tensorflow -i https://pypi.python.org/simple/ 
还是碰到 pip._vendor.urllib3.exceptions.ReadTimeoutError ，延长超时值终于成功
pip install tensorflow -i https://pypi.python.org/simple/ --default-timeout=100
```



### 6.23

#### 数据库脚本

因为讨论php 的 mysql代码，把pyton的 mysql 流程又复习一遍 https://realpython.com/python-mysql/

一个以前没注意的几点

1. The **Python Database API** (DB-API) defines the standard interface with which all Python database drivers must comply. These details are documented in [PEP 249](https://www.python.org/dev/peps/pep-0249/). All Python database drivers, such as [sqlite3](https://docs.python.org/3/library/sqlite3.html) for SQLite, [psycopg](https://www.psycopg.org/docs/) for PostgreSQL, and [MySQL Connector/Python](https://github.com/mysql/mysql-connector-python) for MySQL, follow these implementation rules.
2. Using `.executemany()`  ， A query that contains placeholders for the records that need to be inserted；A list that contains all records that you wish to insert
3. **`.fetchmany()`**  以前只是简单用 `.fetchall()`  实际获取结果，对应 php 的 [生成器](https://www.php.net/manual/zh/language.generators.overview.php)
4. **SQL injection attack** the %s placeholders are no longer in string quotes.  cursor.execute() makes sure that the values in the tuple received as argument are of the required data type.  `cursor.execute(update_query, val_tuple, multi=True):` 
5. other connector
6. ORM like [SQLAlchemy](https://docs.sqlalchemy.org/en/13/index.html) 



Asterisks(*) in tuple unpacking and Asterisks in list literals  [Asterisks in Python: what they are and how to use them](https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/)

https://realpython.com/python-data-engineer/



### 6.29

#### k8s 基本概念

1.  https://feisky.gitbooks.io/kubernetes/content/

2. pod/server(clusterIP,NodePort)

3. deployment/statefulset [K8s: Deployments vs StatefulSets vs DaemonSets](https://medium.com/stakater/k8s-deployments-vs-statefulsets-vs-daemonsets-60582f0c62d4) 
4. pod 什么时候需要自己的yaml ？

####  js the first 20 years

1. 21.1.5 One JavaScript.

2. the difference between expressions and statements.
3. [Javascript: difference between a statement and an expression?](https://stackoverflow.com/questions/12703214/javascript-difference-between-a-statement-and-an-expression)

[How do I detect what is changing file ownership on Linux?](https://serverfault.com/questions/619722/how-do-i-detect-what-is-changing-file-ownership-on-linux) & https://wiki.alpinelinux.org/wiki/Inotifyd



### 6.30

#### watchdog

https://pypi.org/project/watchdog/  跨平台，统一接口的python脚本确实是python的一大应用

- Linux 2.6 (inotify)
- Mac OS X (FSEvents, kqueue)
- FreeBSD/BSD (kqueue)
- Windows (ReadDirectoryChangesW with I/O completion ports; ReadDirectoryChangesW worker threads)
- OS-independent (polling the disk for directory snapshots and comparing them periodically; slow and not recommended)



### 7.15

#### numpy

https://realpython.com/what-can-i-do-with-python/ 很详细总结，之前应该也有类似的

https://realpython.com/numpy-scipy-pandas-correlation-python/ 读读没特别有用。

https://realpython.com/numpy-array-programming/



### 7.19

#### 考虑买M1

https://ayushirawat.com/python-39-all-you-need-to-know

MacBook Air M1 for ML ?



### 7.21

#### try/catch

[Are nested Try/Catch blocks a bad idea?](https://stackoverflow.com/questions/4799758/are-nested-try-catch-blocks-a-bad-idea)

> There are certain circumstances where they're a good idea, e.g. one try/catch for the whole method and another inside a loop as you want to handle the exception and continue processing the rest of a collection.
>
> Really the only reason to do it is if you want to skip the bit that errored and carry on, instead of unwinding the stack and losing context. Opening multiple files in an editor is one example.

[Is it good to use try catch within a try catch?](https://stackoverflow.com/questions/13759759/is-it-good-to-use-try-catch-within-a-try-catch)

另一种情况是 [Exception handling try catch inside catch](https://stackoverflow.com/questions/3526167/exception-handling-try-catch-inside-catch)



### 7.22

#### torch

和Tensorflow 一样，清华源装不上， `pip3 install torch torchvision torchaudio -i https://pypi.python.org/simple/` 

[Why you should use `python -m pip`](https://snarky.ca/why-you-should-use-python-m-pip/) 

[What's the difference between “pip install” and “python -m pip install”?](https://stackoverflow.com/questions/25749621/whats-the-difference-between-pip-install-and-python-m-pip-install)

都是说有不同python版本时候可以知道哪个python执行了pip，也就可以进一步知道包是安装在是哪个版本的 `site-packages` 目录下

https://techwithtech.com/python-pip-vs-pip3/ 解释得不错

```
pip show pip
pip --version
pip3.9 install package_name //pip具体的版本号
pip install pip-autoremove
pip-autoremove somepackage -y
```

[Does uninstalling a package with “pip” also remove the dependent packages?](https://stackoverflow.com/questions/7915998/does-uninstalling-a-package-with-pip-also-remove-the-dependent-packages) 不会，可以用 `pip-autoremove`

最终是我一直在考虑的 [Update: Setting up Python, numpy, and PyTorch natively on Apple M1](https://hendrik-erz.de/post/update-setting-up-python-numpy-and-pytorch-natively-on-apple-m1)



### 8.19

#### css framework

工作原因 又花了点时间研究css framework，[2019年 12月时候](readme.md)花了点时间，选了 Bulma 这次 查了觉得如果需要还是选它 [Evaluating CSS frameworks](https://jesperhoy.dev/p44/evaluating-css-frameworks) Bulma/Buefy combo

[CSS Utility Classes and "Separation of Concerns"](https://adamwathan.me/css-utility-classes-and-separation-of-concerns/) [Tailwind CSS](https://tailwindcss.com/) 作者总结  https://tailwindchina.com/ 中文版

> **What if we needed to add \*a new type of content\* that also needed the same styling?**
>
> Using a "semantic" approach, we'd need to write the new HTML, add some content-specific classes as styling "hooks", open up our stylesheet, create a new CSS component for the new content type, and apply the shared styles, either through duplication or using `@extend` or a mixin.
>
> Using our content-agnostic `.media-card` class, all we'd need to write is the new HTML; we wouldn't have to open the stylesheet at all.
>
> ...
>
> CSS Zen Garden takes the first approach, while UI frameworks like [Bootstrap](http://v4-alpha.getbootstrap.com/) or [Bulma](http://bulma.io/) take the second approach. For the project you're working on, what would be more valuable: restyleable HTML, or reusable CSS?
>
> 
>
> Phase 5: Utility-first CSS
>
> Once this clicked for me, it wasn't long before I had built out a whole suite of utility classes for common visual tweaks I needed. The amazing thing about this is that before you know it, you can build entirely new UI components without writing any new CSS.
>
> Want to mute some dark text a little? Add the `.text-dark-soft` class. Need to make the font size a little smaller? Use the `.text-sm` class. When everyone on a project is choosing their styles from a curated set of limited options, your CSS stops growing linearly with your project size, and you get consistency for free.
>
> One of the areas where my opinion differs a bit from some of the really die-hard functional CSS advocates is that I don't think you should build things out of utilities *only.* The reason I call the approach I take to CSS utility-*first* is because I try to build everything I can out of utilities, and **only extract repeating patterns as they emerge.**



[A Year of Utility Classes](https://css-irl.info/a-year-of-utility-classes/) 

> Utility classes are CSS class names that serve one particular purpose, and are named as such.

https://www.smashingmagazine.com/2013/10/challenging-css-best-practices-atomic-approach/ 类似 utility class, 快速阅读

https://frontstuff.io/in-defense-of-utility-first-css   太长，到25号才看完。

https://css-tricks.com/growing-popularity-atomic-css/ 8.26看完



### 8.24

#### team management ?

[How To Manage a Software Development Team](https://www.wrike.com/blog/non-techies-can-successfully-manage-development-team/#How-to-manage-a-software-development-team-with-project-management-software)

如何把这个问题问好 https://softwareengineering.stackexchange.com/questions/431284/whats-the-people-managements-job-responsibility-on-a-self-organizing-team  之前类似的问题已经几次失败，删帖。

从 https://www.scrum.org/resources/blog/scrum-team-self-managing 到 https://textexpander.com/blog/team-management-in-software-development

做吸取些素材来修改：

1. https://www.pluralsight.com/blog/teams/7-tips-for-managing-software-developers-effectively
2. https://textexpander.com/blog/how-to-manage-a-software-development-team-17-tips-for-success
3. https://www.scrum.org/resources/blog/how-lead-self-managing-teams-3-practical-tips
4. https://www.atlassian.com/agile/software-development/dev-managers-vs-scrum-masters
5. https://www.devnetwork.com/what-is-a-dev-manager/
6. https://www.infoq.com/articles/development-manager-role/
7. https://www.atlassian.com/agile/kanban/kanban-vs-scrum

SO 上问题一改再改，觉得已经是最完整描述了

在这里呼吁  [Is there any way we can encourage people to leave a comment when they cast delete votes?](https://meta.stackexchange.com/questions/368995/is-there-any-way-we-can-encourage-people-to-leave-a-comment-when-they-cast-delet) 居然已经一再被down-vote

https://softwareengineering.stackexchange.com/questions/419122/does-oop-overemphasize-the-importance-of-noun-and-thus-put-action-verb-in-the-le 



### 8.31

#### 议题比较杂

证实vscode 1.5.9 cpp工具没法读取和输出到stdio https://github.com/microsoft/vscode-cpptools/issues/8075 承认是bug，而且修复了也只能用 `externalConsole`

[Native JSON support in MYSQL 5.7 : what are the pros and cons of JSON data type in MYSQL?](https://stackoverflow.com/questions/33660866/native-json-support-in-mysql-5-7-what-are-the-pros-and-cons-of-json-data-type)

[Testing in the Twenties](https://www.tbray.org/ongoing/When/202x/2021/05/15/Testing-in-2021)

https://web.dev/off-main-thread/

#### css utility library

https://www.smashingmagazine.com/2013/10/challenging-css-best-practices-atomic-approach/

https://blog.logrocket.com/css-utility-classes-library-extendable-styles/

https://css-tricks.com/need-css-utility-library/ 和 logrocket文章类似，各种 utility-library的比较

#### autoplay

https://developer.chrome.com/blog/autoplay/

> Autoplay with sound is allowed if:
>
> - The user has interacted with the domain (click, tap, etc.).

https://stackoverflow.com/questions/57455849/chrome-autoplay-policy-chrome-76 还可以参见 https://github.com/Hugo22O/chrome-autoplay

重刷页面处理还要再设计，可参考：

1. [How to pop up an alert box when the browser's refresh button is clicked?](https://stackoverflow.com/questions/3221161/how-to-pop-up-an-alert-box-when-the-browsers-refresh-button-is-clicked)
2. [Check if page gets reloaded or refreshed in JavaScript](https://stackoverflow.com/questions/5004978/check-if-page-gets-reloaded-or-refreshed-in-javascript)



### 9.1

#### RabbitMQ vs Redis 实现queue

[Publish/Subscribe reliable messaging: Redis VS RabbitMQ](https://stackoverflow.com/questions/43777807/publish-subscribe-reliable-messaging-redis-vs-rabbitmq)

https://blog.tuleap.org/how-we-replaced-rabbitmq-redis/

关于laravel queue 两篇文章 https://proxify.io/articles/laravel-redis 和 https://learnku.com/articles/3729/use-laravel-queue-to-understand-the-knowledge

#### RabbitMQ vs kafka

https://www.cloudamqp.com/blog/when-to-use-rabbitmq-or-apache-kafka.html

https://tanzu.vmware.com/developer/blog/understanding-the-differences-between-rabbitmq-vs-kafka/

### 9.2

#### 杂项

[yapi](https://hellosean1025.github.io/yapi/index.html) vs [apizza](https://www.apizza.net/) [常见的API接口管理工具](http://blog.cxiangnet.cn/2019/03/26/%E5%B8%B8%E8%A7%81%E7%9A%84api%E6%8E%A5%E5%8F%A3%E7%AE%A1%E7%90%86%E5%B7%A5%E5%85%B7/)

https://lumen.laravel.com/ 了解



### 9.3

#### 爬虫

通过爬虫看看别人怎么写一个简单规范的脚本，还没看

1. https://www.zenrows.com/blog/mastering-web-scraping-in-python-crawling-from-scratch
2. https://www.zenrows.com/blog/stealth-web-scraping-in-python-avoid-blocking-like-a-ninja



### 9.10

github action?



### 9.17

#### nologin

`/sbin/nologin` 

```
su - www-data -c xxx
This account is currently not available.
```

原因 [Would su, sudo or ssh honor /sbin/nologin?](https://manjusri.ucsc.edu/2017/09/15/su-sudo-ssh/)

["This account is currently not available" error when trying to ssh](https://askubuntu.com/questions/486346/this-account-is-currently-not-available-error-when-trying-to-ssh) "it's a special user/group used by the web server, not intended for regular shell use."

[How to run command as user who has /usr/sbin/nologin as Shell?](https://serverfault.com/questions/351046/how-to-run-command-as-user-who-has-usr-sbin-nologin-as-shell)



### 9.29

#### docstring vs comments

[Docstrings vs Comments](https://stackoverflow.com/questions/19074745/docstrings-vs-comments) docstring for your user, comments for yourself 

https://realpython.com/how-long-does-it-take-to-learn-python/



### 10.8

#### su -

`su - usr` vs `su usr`

[What's the difference between "su" with and without hyphen?](https://superuser.com/questions/453988/whats-the-difference-between-su-with-and-without-hyphen)  "The difference between "-" and "no hyphen" is that the latter *keeps* your existing environment (variables, etc); the former creates a new environment (with the settings of the actual user, not your own)."

原来 `su - www-data -s /bin/sh -c "/usr/local/bin/php /var/www/html/artisan cm:upgrade"` 报错 "Server connection error: 403, message: ACCESS_REFUSED - Login was refused using authentication mechanism PLAIN." [应该就是最普通的用户名密码错](https://stackoverflow.com/questions/26811924/spring-amqp-rabbitmq-3-3-5-access-refused-login-was-refused-using-authentica)。

改成 `su www-data -s /bin/sh -c "/usr/local/bin/php /var/www/html/artisan cm:upgrade"` 就可以



[Any difference between su -www-data vs sudo -u www-data?](https://stackoverflow.com/questions/69493317/any-difference-between-su-www-data-vs-sudo-u-www-data) 不知道会不会被关，参考 [BASH Scripting, su to www-data for single command](https://serverfault.com/questions/388016/bash-scripting-su-to-www-data-for-single-command) 和 [Cannot run command as www-data using su](https://unix.stackexchange.com/questions/327436/cannot-run-command-as-www-data-using-su)



### 10.12

#### m1

[A Python Data Scientist’s Guide to the Apple Silicon Transition](https://www.anaconda.com/blog/apple-silicon-transition) 2021 7.15 ”For general usage, the performance is excellent, but these systems are not aimed at the data science and scientific computing user yet. If you want an M1 for other reasons, and intend to do some light data science, they are perfectly adequate. For more intense usage, **you’ll want to stick with Intel Macs for now**, but keep an eye on both software development as compatibility improves and future ARM64 Mac hardware, which likely will remove some of the constraints we see today.“



### 10.13

#### Async

https://realpython.com/python-async-features/

The reason why `Task Two` outputs its total first is that it’s only counting to 10, while `Task One` is counting to 15. `Task Two` simply arrives at its total first, so it gets to print its output to the console before `Task One`.

https://stackoverflow.com/questions/14413969/why-does-next-raise-a-stopiteration-but-for-do-a-normal-return



The event loop is at the heart of the Python async system. It runs all the code, including `main()`. When task code is executing, the CPU is busy doing work. When the `await` keyword is reached, a context switch occurs, and control passes back to the event loop. The event loop looks at all the tasks waiting for an event (in this case, an `asyncio.sleep(delay)` timeout) and passes control to a task with an event that’s ready.

```python
        "https://baidu.com",
        "https://www.taobao.com/",
        "https://www.apple.com",
        "https://www.microsoft.com",
        "https://qq.com/"
        
        request能正确解析
        await response.text()都报错 UnicodeDecodeError: 'gb2312' codec can't decode byte
        await response.text(encoding='utf-8') 只剩下qq报错 UnicodeDecodeError: 'utf-8' codec can't decode byte
        正想通过取出 Content-Type: text/html;charset=utf-8 的 charset来解析结果突然又不出错！

按理说自动查编码格式是最基本的，不知道怎么第一次出了 If encoding is None content encoding is autocalculated using Content-Type HTTP header and chardet tool if the header is not provided by server.
```



随手回答了 https://stackoverflow.com/questions/55499511/unable-to-get-webpage-using-aiohttp-clientsession



### 10.14

#### Aysnc cont.

https://www.ruanyifeng.com/blog/2019/11/python-asyncio.html 阮一峰文章 主要是引出 https://realpython.com/async-io-python/

长，有几点跳着看

>  Python’s async model is built around concepts such as callbacks, events, transports, protocols, and futures... At the heart of async IO are coroutines. A coroutine is a specialized version of a Python generator function...
>
> It is less common (and only recently legal in Python) to use `yield` in an `async def` block. 
>
> Most programs will contain small, modular coroutines and one wrapper function that serves to chain each of the smaller coroutines together. [`main()`](https://realpython.com/python-main-function/) is then used to gather tasks (futures) by mapping the central coroutine across some iterable or pool.
>
> Python’s `requests` package isn’t compatible with async IO
>
> Use `aiohttp` for the requests, and `aiofiles` for the file-appends. These are two primary examples of IO that are well-suited for the async IO model.

文章结尾有个简单列表  [aio-libs](https://github.com/aio-libs)

几个注意点：

1. `asyncio.create_task`
2. If you need to get the **return value** of these async functions, then `gather` is useful. 

[Simplest async/await example possible in Python](https://stackoverflow.com/questions/50757497/simplest-async-await-example-possible-in-python) 这里的问题和解答在看完两篇  https://realpython.com/ 就基本明白

[Intro to Async Concurrency in Python vs. Node.js](https://medium.com/@interfacer/intro-to-async-concurrency-in-python-and-node-js-69315b1e3e36) 比较阅读，另 [Async patterns in Node.js: only 5+ different ways to do it!](https://codeburst.io/async-patterns-in-node-js-only-4-different-ways-to-do-it-70186ee83250) 我们都经历过

> In practice you’ll likely have an `async def main(): …` that you’ll run at end of your code with `asyncio.run(main())`. Note that it’s **not** `**asyncio.run(main)**`**, but** `**asyncio.run(main())**` — we don’t pass the main function as a callback to `asyncio.run`, but the coroutine object returned by the called `main()`.
>
> If you were to call a function like `fetch_url` above (sometimes called a “**coroutine function**”) *directly*, what you’d get back will surprise you: it will not be the result of the function, but a **coroutine object**:
>
> 这就是下面generator提到的

 `await asyncio.wait(tasks)`   [Asyncio.gather vs asyncio.wait](https://stackoverflow.com/questions/42231161/asyncio-gather-vs-asyncio-wait)

python async 的一个问题接口和使用规范还在变化，不像nodejs已经很稳定.

####  genarator

http://www.dabeaz.com/generators/Generators.pdf 长，没都看

>  Calling a generator function creates an generator object. However, it does not start running the function. A generator is a one-time operation. You can iterate over the generated data once, but if you want to do it again, you have to call the generator function again.

文章里的例子有点像nodejs的stream

> The generator solution was based on the concept of pipelining data between different components
>
> Generators decouple iteration from the code that uses the results of the iteration

```python
with open("access-log") as wwwlog:
   bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog)
   bytes_sent = (int(x) for x in bytecolumn if x != '-')
   print("Total", sum(bytes_sent))
```

https://www.geeksforgeeks.org/python-list-comprehensions-vs-generator-expressions/



小知识点

[Python try-else](https://stackoverflow.com/questions/855759/python-try-else) "The statements in the `else` block are executed if execution falls off the bottom of the `try` - if there was no exception. Honestly, I've never found a need."





### 10.26

#### python generator cont.

https://realpython.com/introduction-to-python-generators/ 提供一个pipeline的例子实际动手试试，还有加深理解`generator expression` 或者叫 `generator comprehension` （对比 `list comprehensions`）

[Javascript ES6 yield vs yield in python](https://stackoverflow.com/questions/33161964/javascript-es6-yield-vs-yield-in-python)



### 11.1

#### lua script

https://www.lua.org/pil/contents.html

> Tables are the main (in fact, the only) data structuring mechanism in Lua, and a powerful one. We use tables to represent ordinary arrays, symbol tables, sets, records, queues, and other data structures, in a simple, uniform, and efficient way. 



[Learn Lua in 15 Minutes](http://tylerneylon.com/a/learn-lua/)

#### lua in redis

[A Speed Guide To Redis Lua Scripting](https://www.compose.com/articles/a-quick-guide-to-redis-lua-scripting/)

> Run lua script using redis-cli
> Now our script needs keys and arguments. The keys come first and redis-cli counts them for us; each command line argument is a key, right up to the comma. What comes after the comma are arguments.

```lua
eval 'for _,key in ipairs(redis.call("lrange", KEYS[1], 0,-1)) do redis.call("INCR",key) end' 1 region:one
```

The redis [documentation](http://redis.io/commands/eval#available-libraries) lists the ones that are loaded; [base](https://www.lua.org/manual/5.1/manual.html#5.1), [table](https://www.lua.org/manual/5.1/manual.html#5.5), [string](https://www.lua.org/manual/5.1/manual.html#5.4), [math](https://www.lua.org/manual/5.1/manual.html#5.6), [struct](http://www.inf.puc-rio.br/~roberto/struct/), [cjson](http://www.kyne.com.au/~mark/software/lua-cjson-manual.html), [cmsgpack](https://github.com/antirez/lua-cmsgpack), [bitop](http://bitop.luajit.org/), redis.sha1hex, ref

https://developpaper.com/redis-how-to-use-lua-script-instance-tutorial/  讲解好像更清楚

[A quick guide to Redis Lua scripting](https://www.freecodecamp.org/news/a-quick-guide-to-redis-lua-scripting/)

[What is the difference of pairs() vs. ipairs() in Lua?](https://stackoverflow.com/questions/55108794/what-is-the-difference-of-pairs-vs-ipairs-in-lua)

[What does # mean in Lua?](https://stackoverflow.com/questions/17974622/what-does-mean-in-lua) 所以 `eval "return #redis.pcall('keys', 'abc:*')" 0` 参见 https://stackoverflow.com/questions/20418529/how-to-count-the-number-of-keys-matching-a-pattern

#### 实际例子

https://github.com/alexanderscott/redis-lua-samples



### 11.2

#### redis lua script cont.

```
redis> eval "return #redis.pcall('keys', 'cc-cm:recoding_finish:*')" 0
654
redis> eval "return #redis.pcall('keys', 'cc-cm:preview_task_customer:*')" 0
367
redis> eval "return #redis.call('keys','cc-cm:'..KEYS[1]..':*')" 1 preview_task_customer
367
redis> eval "return #redis.call('keys','cc-cm:'..KEYS[1]..':*')" 1 recoding_finish
654

redis> eval "for _,k in ipairs(redis.call('keys','cc-cm:'..KEYS[1]..':*')) do redis.call('del',k) end" 1 recoding_finish
null --没有显式return 所以就返回null
redis> eval "return #redis.call('keys','cc-cm:'..KEYS[1]..':*')" 1 recoding_finish
0
redis> eval "for _,k in ipairs(redis.call('keys','cc-cm:'..KEYS[1]..':*')) do redis.call('del',k) end" 1 preview_task_customer
null
redis> eval "return #redis.call('keys','cc-cm:'..KEYS[1]..':*')" 1 preview_task_customer
0

redis> eval "return #redis.call('hgetall','websocket:socket_user')" 0
2044
```



### 11.3

#### generator comprehension cont.

https://realpython.com/introduction-to-python-generators/  提到两点，这里进一步阐述 Python Like You Mean It

1. [Chaining comprehensions](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Generators_and_Comprehensions.html#Chaining-comprehensions)
2. [Using generator comprehensions on the fly](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Generators_and_Comprehensions.html#Using-generator-comprehensions-on-the-fly)  "generator comprehensions can be fed *directly* into functions that operate on iterables. "

[Generator expressions vs. list comprehensions](https://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehensions) 参考 我们代码用了 https://realpython.com/python-enumerate/ 但注意

```
TypeError: 'enumerate' object is not subscriptable
```

[Usage of Asterisks in Python](https://www.datacamp.com/community/tutorials/usage-asterisks-python) 又有点忘

https://github.com/redis/redis-py##getting-started 比如是 `delete` 而不是`del`

https://realpython.com/python-redis/#using-redis-py-redis-in-python



### 11.16

#### 关于dict 一些复习

the keys can be added or removed from a dictionary by converting the view returned by `.keys()` into a `list` object:

```
>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> for key in list(prices.keys()):  # Use a list instead of a view
...     if key == 'orange':
...         del prices[key]  # Delete a key from prices
...
>>> prices
{'apple': 0.4, 'banana': 0.25}
不能直接删 for key in prices.keys():
```



[Python is 'key in dict' different/faster than 'key in dict.keys()'](https://stackoverflow.com/questions/31738912/python-is-key-in-dict-different-faster-than-key-in-dict-keys)

```
>>> for key in a_dict:
...     print(key, '->', a_dict[key])

>>> for key in a_dict.keys():
...     print(key)
```

[Why use dict.keys?](https://stackoverflow.com/questions/17634177/why-use-dict-keys) 历史原因，python3 可以做集合操作



dictionary comprehension

```
>>> a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
>>> new_dict = {value: key for key, value in a_dict.items()}
>>> new_dict
{1: 'one', 2: 'two', 3: 'thee', 4: 'four'}

>>> a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
>>> new_dict = {k: v for k, v in a_dict.items() if v <= 2}
>>> new_dict
{'one': 1, 'two': 2}

>>> incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
>>> total_income = sum([value for value in incomes.values()])
>>> total_income

>>> total_income = sum(value for value in incomes.values())
>>> total_income
14100.0

>>> total_income = sum(incomes.values())
>>> total_income
```

[7 Handy Use Cases Of Dictionary Comprehensions In Python](https://towardsdatascience.com/7-handy-use-cases-of-dictionary-comprehensions-in-python-f7c37e462d92)



### 11.29

#### regex: 2 catch groups  

```python
re.search('Successfully built (.*)|writing image sha256:(.*)', test).groups()
image_id = image_ids[0] if image_ids[1] == None else image_ids[1]
# 如果直接 group(1) 或者 group(2) 可能的None
```

[Python Regexes - findall, search, and match](https://howchoo.com/python/python-regexes-findall-search-and-match) match只从头开始找， search返回第一个，findall 所有



### 11.30

#### log on std.err by default

我的脚本突然没法再获取`docker-compose build`的输出，还给他开了问题单 [Can't get docker-compose(mac version) build output with python Popen anymore](https://github.com/docker/compose/issues/8975) 然后突然意识到这是因为`docker-compose build`把它的输出改到 `std.err` 了

想起debugjs也是输出到std.err,当初还困惑一下。所以为什么有的应用把输出log写到std.err，有的写到std.out ？ 觉得在SO问这种问题估计会被close，但查了一下 确实有这样问题，比如：

1. [Should I log messages to stderr or stdout?](https://stackoverflow.com/questions/4919093/should-i-log-messages-to-stderr-or-stdout) 回复很好
2. [Why Python logging writes to stderr by default?](https://stackoverflow.com/questions/58971197/why-python-logging-writes-to-stderr-by-default) “stderr is meant to be an output for all messages that are just some internal and/or debugging program information like logs and errors, rather than actual output, the result of the program.” ... “one for monitoring (logging and errors): stderr.” 
3. https://github.com/log4js-node/log4js-node/issues/66 "It's more typical for console logs to go to stderr than stdout, to avoid interfering with "real" output from (for example) a command-line tool." 但也有人不同意 “ Node will output all `console.log` messages to `stdout`.”
4. https://github.com/rs/zerolog/issues/96 “The default behaviour of the logger is to log to `stderr` rather than `stdout`. ”
5. https://github.com/denoland/deno/issues/4256 “Request: Separate console functions from Standard Output, In the web browser, [console](https://developer.mozilla.org/en-US/docs/Web/API/Console) was always meant to be a developer's debugging tool, not a way to show output to the end user. " 但讨论里也有不同意的。
6. https://github.com/pypa/pip/issues/6758 ”Log debug and informational messages to stderr only“
7. https://www.postgresql.org/docs/9.1/runtime-config-logging.html ”PostgreSQL supports several methods for logging server messages, including stderr, csvlog and syslog.  The default is to log to stderr only. “



### 12.6

#### generator

原来 [10.14](#10.14) 就看过，但这次完整看完。代码和文档都在 https://github.com/dabeaz/generators

它的例子比 https://realpython.com/introduction-to-python-generators/ (在 [10.26](#10.26) 和 [11.3](#11.3)  分别读过) 更深入一些。

同时又复习了一下 [What is the difference between declarative and imperative paradigm in programming?](https://stackoverflow.com/questions/1784664/what-is-the-difference-between-declarative-and-imperative-paradigm-in-programmin) 觉得declarative这种说法实在有点哗众取宠  the whole "what to do" vs "how to do it" is too vague and really doesn't explain。比如你可以写一些helper 方法（比如私有方法）做how 就是具体实现， 然后把他们再串在一起，解决what.

[The dream of declarative programming [closed\]](https://softwareengineering.stackexchange.com/questions/275680/the-dream-of-declarative-programming) 有几个回复跟我是一样观点：

1. "in practice for general purpose computing **you still have to think about the 'how'** and write all kinds of tricks while keeping in mind how this will be implemented... For some limited domains you can write systems that almost always do well in figuring out a good implementation, for example, SQL. For general purpose computing that doesn't work particularly well - you can write systems in, say, Prolog but you have to visualize how exactly your declarations will be converted to an imperative execution order in the end, and that loses much of the expected declarative programming benefits."
2. One could argue that most configuration files (.vimrc, .profile, .bashrc, .gitconfig) are using a domain-specific language that's largely declarative ... **Configuration files are declarative**, but certain configurations are hard to declare. 
3. Mostly the problem is how you model the data; and declarative programming isn't helping here. In imperative languages you already have tons of libraries that does lots of stuff for you, so you **only need to know what to call**. In a particular way one might consider this declarative programming

但是 [Python as a Declarative Programming Language](https://www.benfrederickson.com/python-as-a-declarative-programming-language/) 提到比较实际一点 “In practice this means avoiding expressions of control flow: **loops and conditional statements are removed** and replaced with higher level constructs..."

[Chapter 1. (Avoiding) Flow Control](https://www.oreilly.com/library/view/functional-programming-in/9781492048633/ch01.html) 也提到 Eliminating Loops & Generators 作为 declarative 编程的一个表现

declarative  vs imperative 讨论就此打住。



### 12.9

#### update case when

```sql
update `employee` set salary = (case when `manager_id` = 17 then salary+100 else salary end),
tax = (case when `manager_id` = 18 then tax+100 else tax end) where emp_id > 12
//或者两条sql语句
update `employee` set salary = salary+100 where emp_id > 12 and `manager_id` = 17 
update `employee` set taxt = tax+100 where emp_id > 12 and `manager_id` = 18 
```

 [MySQL: Update Query using If else](https://stackoverflow.com/questions/14580520/mysql-update-query-using-if-else)

```sql
UPDATE tablename
SET col1=(CASE WHEN col1 LIKE 'A' THEN col1='IA' ELSE col1 END),
col2=(CASE WHEN col1 LIKE 'A' THEN col2='XXX' ELSE col2 END),
col3=(CASE WHEN col3 LIKE 'A' THEN col3='IA' ELSE col3 END),
col3=(CASE WEHN col3 LIKE 'A' THEN col4='XXX' ELSE col4 END)
WHERE
(col1='A' AND col2='UNKNOWN') OR (col3='A' AND col4='UNKNOWN')
```

https://stackoverflow.com/questions/18449247/how-to-make-update-query-with-parameters-and-case-statement-in-laravel-4  laravel 的 `raw() ` 自己写case

[SQL 'case when' vs 'where' efficiency](https://stackoverflow.com/questions/56689364/sql-case-when-vs-where-efficiency) case 比where低效，因为没有用到索引，但是在我们这个特定情况 `!=` 查一次，`=` 查一次就一样了 

