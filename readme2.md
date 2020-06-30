### 4.9 

#### 一年整

学习已经一年，当然实际时间不到6个月，而且还是花在平时晚上或者周末一点零碎时间。今天没有学习新东西就是记录下。

### 4.26

#### 长字符串

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

#### md tight list & loose list

解决使用 typora 一个长久的困惑，顺便给它开了一个 [bug](https://github.com/typora/typora-issues/issues/3467)： 

markdown number list 两种风格 tight & loose, 差别就是有没有多加一行(blank line) , 转成html时候是不是加 `<p>` https://github.github.com/gfm/#tight 这个在md的基本语法里没有提到 https://www.markdownguide.org/basic-syntax/ 

[Why are there even tight lists?](https://talk.commonmark.org/t/why-are-there-even-tight-lists/2301) 这里回答说是历史原因 

> It’s partly a backwards-compatibility issue, since Gruber’s original Markdown had a distinction between tight and loose lists that was realized this way (presence or absence of p tags). 

**[Jeff Atwood](https://meta.discourse.org/u/codinghorror)** 大牛也参与这类讨论 [Markdown nested lists have different vertical padding for different bullet depths](https://meta.discourse.org/t/markdown-nested-lists-have-different-vertical-padding-for-different-bullet-depths/106166)

[Extra lines appearing between list items in Github Markdown](https://stackoverflow.com/questions/43503528/extra-lines-appearing-between-list-items-in-github-markdown) 这个讨论没有详细看了



### 5.6

#### DAG

5.1假日看了下图和DAG，现在可以开始看结巴代码，以下几个连接是不是提供有用信息还不清楚：

1. [NLP之中文分词算法(DAG图)解析及实战](https://hadxu.github.io/2018/01/19/NLP之中文分词算法(DAG图)解析及实战/)

2. [jieba中文分词源码分析（三）](https://blog.csdn.net/daniel_ustc/article/details/48223135)

3. [jieba分词源码解读一](https://blog.csdn.net/shenxiaoming77/article/details/51511289)

4. [jieba分词流程及部分源码解读（一）](https://blog.csdn.net/Jameslvt/article/details/81118560)



### 5.11

#### 读结巴代码

```python
while i<N and frag in self.FREQ: # FREQ 对词的前缀都存，但是前缀值是0
		if self.FREQ[frag]:
			templist.append(i)
```



### 5.15

#### 很久以前 bill karwin 评价python

以前在quora关注的这个讨论终于又找到 [Which is better for a beginner, Python or Ruby?](https://www.quora.com/Which-is-better-for-a-beginner-Python-or-Ruby)

比如 Bill Karwin的回答：

> To me, both Python and Ruby are basically like Perl, but with fixes for a bunch of the things that made Perl hard to use.
>
> The developers who drove Ruby popularity back in 2005 were always the kind of programmers who wanted to try new and shiny toys instead of proven and mature, so perhaps former Ruby users are trying out new languages.

还有另外一个有趣回复

> Python, perhaps simply through dumb luck (or not), was picked up by a lot of old Unix/C hackers in the late '90s and early aughts. It was also picked up by a lot of scientists. This lead to the creation of a lot of high-performance C libraries for Python for a very wide variety of tasks. Outside of maybe Java and C++, Python has more best-in-class libraries than almost any language out there, and the standard library is both deep and wide. Outside of libraries for web (and possibly devops), Ruby really can't compete in terms of library support.



当年看ruby 第一困惑就是 Metaprogramming, 为什么只有rudy要提这个概念，没看到有别的语言提，而是这个概念被搞得很神秘：

> *Metaprogramming* is a technique by which you can write code that writes code by itself dynamically at runtime. 

我自己问的问题也被关闭 [Examples to explain what Ruby metaprogramming is closed](https://stackoverflow.com/questions/53776313/examples-to-explain-what-ruby-metaprogramming-is)

如果仔细搜索Metaprogramming 能找到比较实用一点文章 "using metaprogramming you can reopen and modify classes, catch methods that don’t exist and create them on the fly" 但我现在已经没精力看，只能是记录下。

1. [Ruby Metaprogramming by Example](https://buildingvts.com/ruby-metaprogramming-by-example-612526d0b72)
2. [Ruby Metaprogramming Is Even Cooler Than It Sounds](https://www.toptal.com/ruby/ruby-metaprogramming-cooler-than-it-sounds) 



### 5.17

#### 结巴DAG

继续结巴学习， DAG看明白，但是计算最大概率路径`def calc(self, sentence, DAG, route)`还不明白，继续查资料:

[中文分词原理理解+jieba分词详解（二）](https://zhuanlan.zhihu.com/p/66904318) 先搞清楚calc如何算在看 他写的入门资料 [中文分词原理理解+jieba分词详解（一）](https://zhuanlan.zhihu.com/p/65680803)  关于`Verterbi算法与分词` 描述。

[结巴的词性标注](https://gist.github.com/hscspring/c985355e0814f01437eaf8fd55fd7998) 以及其他分词库的[词性标注](https://gist.github.com/hscspring/e063662135f789c9f67321aceea9c155) 

然后注意到 [5.6](#5.6) 摘抄的第二篇文章也解释了`calc` 目前卡在下一步 ` __cut_DAG`  即如何得到『得到最大概率路径』



List comprehension

```python
new_list = [expression(i) for i in old_list if filter(i)]
# vs
new_list = []
for i in old_list:
    if filter(i):
        new_list.append(expressions(i))
```



[How to use Python’s min() and max() with nested lists](https://dbader.org/blog/python-min-max-and-nested-lists)

```python
nested_list = [['cherry', 7], ['apple', 100], ['anaconda', 1360]]
max(nested_list, key=lambda x: x[1]) # 缺省比的是第一个
```



理解`__cut_DAG` ！



### 6.30

#### pipfile & requirement.txt

再次复习 pipfile & requirement.txt

[requirement.txt](https://zhuanlan.zhihu.com/p/69058584) 简单，但是pipfile要再花时间看下

1. [Python HOW: Create requirements.txt Using pipenv](https://medium.com/@DrGabrielHarris/python-how-create-requirements-txt-using-pipenv-2c22bbb533af) 

2. [Pipenv: A Guide to the New Python Packaging Tool](https://realpython.com/pipenv-guide/)

3. [How are Pipfile and Pipfile.lock used?](https://stackoverflow.com/questions/46330327/how-are-pipfile-and-pipfile-lock-used)

4. 还有pipenv https://pipenv-fork.readthedocs.io/en/latest/index.html

   

   

