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
> `pipenv` is currently the recommended dependency manager for collaborative projects by Python. It uses `pip` and `virtualenv` under the hood.

2. [Pipenv: A Guide to the New Python Packaging Tool](https://realpython.com/pipenv-guide/)
3. [How are Pipfile and Pipfile.lock used?](https://stackoverflow.com/questions/46330327/how-are-pipfile-and-pipfile-lock-used)
4. 还有pipenv https://pipenv-fork.readthedocs.io/en/latest/index.html

写和rabbitmq通信的简单例子



### 7.1

#### pipreqs

`pip3 freeze >requirements.txt` 就是把当前安装所有pip包都列出了，安装 pipreqs 然后执行 `pipreqs ./` 才能正确生成 `requirements.txt`



### 7.9

#### pyenv

1. https://realpython.com/pipenv-guide/ 读完，需要做相应练习

2. https://blog.windrunner.me/python/pip.html 中文简述  pip 与 Pipfile

3. [python package](https://hackernoon.com/pip-install-abra-cadabra-or-python-packages-for-beginners-33a989834975) 又看了一遍，再次理解一下package和setup.py 但wheel到底是个什么概念没讲透

4. [How to create a Pure-Python wheel](https://stackoverflow.com/questions/31573107/how-to-create-a-pure-python-wheel) 帮助理解 wheel



### 7.10

#### bpython

[bpython原来是有一个python shell](https://stackoverflow.com/questions/4232923/what-are-the-differences-between-ipython-and-bpython)，但是有了ipyhton就没必要再试它了



### 9.7

#### ssl module

又断了两个月！



```python
learning_python ➤ pip3 install pexpect                                           
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
```

[pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available](https://stackoverflow.com/questions/45954528/pip-is-configured-with-locations-that-require-tls-ssl-however-the-ssl-module-in) 

安装最新 3.8.5解决

> **Certificate verification and OpenSSL**
>
> 
>
> This package includes its own private copy of OpenSSL 1.1.1.  The trust certificates in system and user keychains managed by the *Keychain Access* application and the *security* command line utility are not used as defaults by the Python ssl module. A sample command script is included in /Applications/Python 3.8 to install a curated bundle of default root certificates from the third-party certifi package (https://pypi.org/project/certifi/). Double-click on Install Certificates to run it.
>
> 
>
> The bundled pip has its own default certificate store for verifying download connections.



https://gist.github.com/grzhan/77222b1a737e1ad9cb00b28e025ec1e2

跟我基本一样的代码，不知道哪里出了问题! 运行了 child.expect('Password:')  就控制台不出`Password`



### 9.8

#### pexpect

对比 expect 才知道是 pexpect吃掉了匹配的字符串，但是有没有可能把那些字符串完全打出？

[Is it possbile to achieve the expect script output ?](https://github.com/pexpect/pexpect/issues/658)



### 9.10

#### main()

把 [Defining Main Functions in Python](https://realpython.com/python-main-function/#a-basic-python-main) 又复习了一遍；同时复现 [global variables in a function](https://stackoverflow.com/questions/423379/using-global-variables-in-a-function)

```python
def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__ == "__main__":
    main()
```



pexpect 吃掉匹配字符串的问题解决，但又碰到新问题 [Is it possbile to let pexpect output the texts it matches?](https://stackoverflow.com/questions/63825774/is-it-possbile-to-let-pexpect-output-the-texts-it-matches)



### 9.11

#### pexpect cont.

pexpect 吃掉匹配字符串的问题，因为加了 `interact` 后更复杂，放弃了，我就是需要一个简单ssh登录脚本，不想这么麻烦。

[How to see the output in pexpect?](https://stackoverflow.com/questions/45989975/how-to-see-the-output-in-pexpect) 提到的 `logfile_read` 解决不了。

但我自己终于把它解决！ https://stackoverflow.com/questions/63825774/is-it-possbile-to-let-pexpect-output-the-texts-it-matches

注意两点:

1. 不能调用 `child.expect(pexpect.EOF)` 没深究。
2. `child.expect('Last login')` 不能调用，不然 `: Fri Sep 11 11:44:19 2020 from 10.0.0.132` 这串会重复打印。
3. `child.expect('.*')` 完美解决



#### Pathlib

复习使用 Pathlib , 比如重载 `/ `运算符 需要仔细把这篇文档再读下 https://realpython.com/python-pathlib/   （还没有！）

[How do I list all files of a directory?](https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory)

[How to get file creation & modification date/times in Python?](https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python)

[From stat().st_mtime to datetime?](https://stackoverflow.com/questions/39359245/from-stat-st-mtime-to-datetime)

https://github.com/chris1610/pbpython/blob/master/extras/Pathlib-Cheatsheet.pdf



### 9.14

#### python2

macOS 自带python2 的注意事项，mac自带 python 2.7.16 在 `/usr/bin/python` 但应该是不带pip ，只有 `easy_install` , 参见 https://ahmadawais.com/install-pip-macos-os-x-python/ 和 [How do I install pip on macOS or OS X?](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x) 所以会经常看到大家推荐用brew安装python2

但python2现在运行也有错误`ERROR:root:code for hash md5 was not found.` （和python3一样），直接卸了 brew uninstall python@2 不折腾了。

[The right and wrong way to set Python 3 as default on a Mac](https://opensource.com/article/19/5/python-3-default-mac) 没空看



#### datetime

1. datatime 可以减， 只用 days, seconds 记录差别， divmod 除以秒数取余

2. [How do I find the time difference between two datetime objects in python?](https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python)



### 9.16

google  <u>improve python skill to the next level</u>

https://stackabuse.com/the-best-python-books-for-all-skill-levels/



### 9.17

#### decorator

[Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/) decorator 概念在每个语言中都会碰到； python 中的应用可以再深入学习下，这篇文章有点长。

https://www.programiz.com/python-programming/decorator 这篇长度合适，看了

[@property decorator](https://www.programiz.com/python-programming/property)

[What are some common uses for Python decorators?](https://stackoverflow.com/questions/489720/what-are-some-common-uses-for-python-decorators)



#### closure

[Python closure vs javascript closure](https://stackoverflow.com/questions/18502095/python-closure-vs-javascript-closure)

同时回顾 "Python assumes that all variables in a function are local. "



#### slice notation

https://stackoverflow.com/questions/509211/understanding-slice-notation

```python
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
```



### 9.21

[Everything About Python — Beginner To Advanced](https://medium.com/fintechexplained/everything-about-python-from-beginner-to-advance-level-227d52ef32d2) 列举25点，以下三点稍微注意下

1. package  `__init__.py`

2. zip

3. Decorators



#### PyTorch ?


#### yield
[What does the “yield” keyword do?](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)



### 9.27

#### pexpect

npm publish脚本 404原因知道了。跑了 expect脚本一样 404，在`npm logout` 提示 `Not logged in to` 所以没有调用`interact` 只是在那个子进程npm login，父进程没登录 npm publish 就提示404了



### 10.9

#### python 3.8

[Cool New Features in Python 3.8](https://realpython.com/python38-new-features/)

https://deepsource.io/blog/python-3-8-whats-new/ 发现这个更清晰 ,顺带熟悉了 unpack



#### python 3.9

https://realpython.com/python39-new-features/

[Python 3.9](https://towardsdatascience.com/python-3-9-9c2ce1332eb4)



#### type hint

[What are type hints in Python 3.5?](https://stackoverflow.com/questions/32557920/what-are-type-hints-in-python-3-5)

[Python Type Hinting](https://medium.com/depurr/python-type-hinting-a7afe4a5637e)



#### logging

[Logging in Python](https://realpython.com/python-logging/)



### 10.10

#### log & color log

[Python之日志处理（logging模块）](https://www.cnblogs.com/yyds/p/6901864.html) 基本就是翻译 https://docs.python.org/3/howto/logging.html

[How can I color Python logging output?](https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output)



碰到奇怪问题  https://stackoverflow.com/questions/64292033/why-set-logging-level-for-each-module-wont-work-here

按说 https://stackoverflow.com/questions/48787538/how-to-set-logging-level-for-the-module-only-in-python 很简单就是这么做

SO很强大！马上得到答案，而且还解答另一个问题， `logging.basicConfig()` 创建一个handler, `coloredlogs` 也会创建handler，难怪看到两个打印。



`coloredlogs.install` 加一个在root就可以。



暂时没时间看

#### python-dotenv

https://pypi.org/project/python-dotenv/

[What is the use of python-dotenv?](https://stackoverflow.com/questions/41546883/what-is-the-use-of-python-dotenv)



复习这些基本概念

https://docs.python-guide.org/writing/structure/#structure-of-code-is-key

https://docs.python-guide.org/dev/virtualenvs/



### 10.12

[Why do /usr and /tmp directories for Linux miss vowels in their spellings?](https://unix.stackexchange.com/questions/8677/why-do-usr-and-tmp-directories-for-linux-miss-vowels-in-their-spellings) 就为了少打两个字母

https://docs.python.org/3/library/subprocess.html#subprocess.run

*args* should be a sequence of program arguments or else a single string or [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object). By default, the program to execute is the first item in *args* if *args* is a sequence. If *args* is a string, the interpretation is platform-dependent and described below. See the *shell* and *executable* arguments for additional differences from the default behavior. Unless otherwise stated, it is recommended to pass *args* as a sequence.

An example of passing some arguments to an external program as a sequence is:

```
Popen(["/usr/bin/git", "commit", "-m", "Fixes a bug."])
```

On POSIX, if *args* is a string, the string is interpreted as the name or path of the program to execute. However, this can only be done if not passing arguments to the program.



[How can I color Python logging output?](https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output) 如何实现

