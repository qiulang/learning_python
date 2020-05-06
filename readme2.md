### 4.9 

学习已经一年，当然实际时间不到6个月，而且还是花在平时晚上或者周末一点零碎时间。

决定先把我在SO的这个问题解决了：18年问的到现在还一直在增粉，即便问题被关闭 [“Client network socket disconnected before secure TLS connection was established”, node 10 [closed\]](https://stackoverflow.com/questions/53593182/client-network-socket-disconnected-before-secure-tls-connection-was-established)

googleapis 也变了主页 https://github.com/googleapis/google-api-nodejs-client

我开的问题也被关闭了  https://github.com/googleapis/google-api-nodejs-client/issues/1471

nodejs 这个讨论也没人理 https://github.com/nodejs/node/issues/21088



但我重新试了下，发现我现在的vpn服务在命令行下都ping不通那个 google url，所以暂时没法试了。



### 4.26

一年又20天后，第一次写python

[UnboundLocalError: local variable 'x' referenced before assignment](https://stackoverflow.com/questions/9264763/dont-understand-why-unboundlocalerror-occurs-closure) 

> Python doesn't have variable declarations, so it has to figure out the [scope](http://docs.python.org/3.3/tutorial/classes.html#python-scopes-and-namespaces) of variables itself. It does so by a simple rule: If there is an assignment to a variable inside a function, that variable is considered local.[[1\]](http://docs.python.org/3.3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python)

> In Python, variables that are only referenced inside a function are implicitly global. 

一行长串， 各种方法 https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string，下面这样最简单

```python
 s = ("this is a very"
      "long string too"
      "for sure ..."
     )
 # 但下面这样可避免 query == "SELECT fooFROM barWHERE baz" 
 query = ' '.join((  # note double parens, join() takes an iterable
    "SELECT foo",
    "FROM bar",
    "WHERE baz",
  ))

```

对比 js

```javascript
var multiStr = "This is the first line" + 
	"This is the second line" + 
	"This is more...";
	
var multiStr = "This is the first line \
	This is the second line \
	This is more...";
```



### 4.30

解决使用 typora 一个长久的困惑，顺便给它开了一个 [bug](https://github.com/typora/typora-issues/issues/3467)： 

markdown number list 两种风格 tight & loose, 差别就是有没有多加一行(blank line) , 转成html时候是不是加 `<p>` https://github.github.com/gfm/#tight 这个在md的基本语法里没有提到 https://www.markdownguide.org/basic-syntax/ 

[Why are there even tight lists?](https://talk.commonmark.org/t/why-are-there-even-tight-lists/2301) 这里回答说是历史原因 

> It’s partly a backwards-compatibility issue, since Gruber’s original Markdown had a distinction between tight and loose lists that was realized this way (presence or absence of p tags). 

**[Jeff Atwood](https://meta.discourse.org/u/codinghorror)** 大牛也参与这类讨论 [Markdown nested lists have different vertical padding for different bullet depths](https://meta.discourse.org/t/markdown-nested-lists-have-different-vertical-padding-for-different-bullet-depths/106166)

[Extra lines appearing between list items in Github Markdown](https://stackoverflow.com/questions/43503528/extra-lines-appearing-between-list-items-in-github-markdown) 这个讨论没有详细看了



### 5.6

5.1假日看了下图和DAG，现在可以开始看结巴代码，以下几个连接是不是提供有用信息还不清楚：

1. [NLP之中文分词算法(DAG图)解析及实战](https://hadxu.github.io/2018/01/19/NLP之中文分词算法(DAG图)解析及实战/)

2. [jieba中文分词源码分析（三）](https://blog.csdn.net/daniel_ustc/article/details/48223135)

3. [jieba分词源码解读一](https://blog.csdn.net/shenxiaoming77/article/details/51511289)

4. [jieba分词流程及部分源码解读（一）](https://blog.csdn.net/Jameslvt/article/details/81118560)
