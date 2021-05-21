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

The Pragmatic Programmer: 20th Anniversary Edition， 第一版我当年应该还是有些收货，第二版有什么更新有点好奇

1. https://www.endpoint.com/blog/2020/10/16/the-pragmatic-programmer-20th-anniversary-edition

2. [5 Essential Takeaways From “The Pragmatic Programmer”](https://betterprogramming.pub/5-essential-takeaways-from-the-pragmatic-programmer-6bb3db986294)

   

### 5.6

http://neuralnetworksanddeeplearning.com/chap1.html

[brew install httpie will install python too instead of using my existing pyhton](https://github.com/httpie/httpie/issues/1051)

[What is a shim?](https://medium.com/@ujjawal.dixit/what-is-a-shim-72d9ac5d8620) 其实就是改路径

[How do I mitigate the situation when Redia has not cached an expensive DB query?](https://stackoverflow.com/questions/67411387/how-do-i-mitigate-the-situation-when-redia-has-not-cached-an-expensive-db-query)



### Cache Stampede

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

[10 Amazing Applications of Pandas – Which Industry Segment is Using Python Pandas?](https://data-flair.training/blogs/applications-of-pandas/)

https://realpython.com/pandas-dataframe/ 已看完 https://realpython.com/pandas-python-explore-dataset/ 周末看

[What is the difference between using squared brackets or dot to access a column?](https://stackoverflow.com/questions/41130255/what-is-the-difference-between-using-squared-brackets-or-dot-to-access-a-column) 

”There are several ways to index a Pandas DataFrame. One of the easiest ways to do this is by using square bracket notation.“

