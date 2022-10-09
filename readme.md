## 2022.1.4

从2019.4月开始，拿课余时间学习python已经三年

[Python isn't just Java without the compile](https://bitworking.org/news/2006/08/python_isnt_java_without_the_compile/) 2006老文章，可以做个简单复习

[Some real practical example to teach object-oriented concepts and programming (in python)](https://cseducators.stackexchange.com/questions/6709/some-real-practical-example-to-teach-object-oriented-concepts-and-programming-i) 更新我的问题

[Object Oriented Software Engineering Project](https://cseducators.stackexchange.com/questions/7087/object-oriented-software-engineering-project) 参与讨论

https://www.lucidchart.com/blog/product-owner-roles-and-responsibilities

## 1.13

### controller vs service

[What is the difference between Controllers and Services in Node REST API's?](https://www.coreycleary.me/what-is-the-difference-between-controllers-and-services-in-node-rest-apis/)

[Why should you separate Controllers from Services in Node REST API's?](https://www.coreycleary.me/why-should-you-separate-controllers-from-services-in-node-rest-apis)

我根据这两篇给的给的一个回答 https://cseducators.stackexchange.com/questions/146/what-is-a-good-analogy-for-the-object-oriented-paradigm



## 1.14

### pause container

[What are the pause containers?](https://stackoverflow.com/questions/48651269/what-are-the-pause-containers)

[The Almighty Pause Container](https://www.ianlewis.org/en/almighty-pause-container)

[What is the use of a pause image in Kubernetes?](https://stackoverflow.com/questions/53258342/what-is-the-use-of-a-pause-image-in-kubernetes)

[4 Most Important Kubernetes Interview Questions](https://www.linkedin.com/pulse/4-most-important-kubernetes-interview-questions-raju-kumar-/)

[Using User Namespaces on Docker](https://coderwall.com/p/s_ydlq/using-user-namespaces-on-docker)



## 1.21

### roadmap

https://roadmap.sh/python

dunder methods  [Difference between len() and .__len__()?](https://stackoverflow.com/questions/2481421/difference-between-len-and-len)



## 2.15

### ag

`ag --js "xxx"` 当前目录下， 没有直接对应grep,大致是 `grep -r "xxx" *` 没有简单方法指定文件类型

http://conqueringthecommandline.com/book/frontmatter

用 ag 查了 我在这个问题单里写的代码 https://github.com/nodejs/node/issues/38339  而且也试了node 17.5 确实没有改进

ag 缺省是正则匹配，所以如果搜索函数调用有 `()` 需要  `-Q --literal Do not parse PATTERN as a regular expression. Try to match it literally.` 比如

`ag --js 'randomstring.generate(32)' -Q` 

`-w` 只搜索词 `-C` 指定多少上下文，缺省2行 ，例子 `ag --md -w "ag" -C 3`

比起grep 几大好处， ignore files https://beyondgrep.com/why-ack/

Easy filetype specifications

```
//ignore files
$ grep pattern $(find . -type f | grep -v '\.git')
$ ack pattern
//Easy filetype specifications
$ grep pattern $(find . -name '*.pl' -or -name '*.pm' -or -name '*.pod' | grep -v .git)
$ ack --perl pattern
```



## 3.16

### color term

以前用 https://pypi.org/project/termcolor/  很多人推荐，但是这个项目好像不更新了。 https://github.com/matthewdeanmartin/termcolor 自称  This is the successor to `termcolor`  但目前只有一颗星。

https://pypi.org/project/colorful/ 目前最多星，但是19年后来没更新 

[How to print colored text to the terminal](https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal) 很多答复，选了其中的 https://github.com/bluenote10/yachalk 他提到基于npm的chalk是我选一个原因。

另个看着太复杂，没时间研究 https://click.palletsprojects.com/en/8.0.x/

今天用m1 macOS 12.2 自带 python 3.8 执行之前脚本一直没结果，从 https://www.python.org/ 下3.10 第一次执行也很久，才发现可能是网络问题导致  `git remote add` 需要很长时间，再次执行就好了。所以可能和 3.8也没关系。



### Nullsafe operator

Python 没有，php 8 也开始支持， nodejs 14开始支持 refer to https://wiki.php.net/rfc/nullsafe_operator



## 6.18

### lost

有段时间不更新，不知道该把时间花在哪里，学点什么？

以前看过 https://pypi.org/project/watchdog/，现在注意到facebook 有一个 https://github.com/facebook/watchman



## 6.23

### docker

https://snyk.io/blog/best-practices-containerizing-python-docker/

几个问题， MULTI-STAGE BUILDS 里 python 如何知道pip的安装路径 ？怎么知道 venv 估计要再查下 virtualenv 文档 (见 6.28更新)

https://realpython.com/python-wheels/ 有兴趣就看，不是太重要 

WSGI Servers 的概念有兴趣就看看 https://www.fullstackpython.com/wsgi-servers.html

[Building Minimal Docker Containers for Python Applications](https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3) 对 MULTI-STAGE BUILDS 类似阐述， 注意 “It is important to note that by default Alpine uses musl instead of glibc by default. This means that some Python wheels won’t work without forcing a recompilation.” 

https://testdriven.io/blog/docker-best-practices/ 长 看完



## 6.28

### docker cont.

https://www.docker.com/blog/containerized-python-development-part-1/

> we relied on the *pip’s –user* option to install dependencies to the local user directory and copy that directory to the final image. There are however other solutions available such as virtualenv or building packages as wheels and copy and install them to the final image.

```
# first stage
FROM python:3.8 AS builder
COPY requirements.txt .

# install dependencies to the local user directory (eg. /root/.local)
RUN pip install --user -r requirements.txt

# second unnamed stage
FROM python:3.8-slim
WORKDIR /code

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.local /root/.local
COPY ./src .

# update PATH environment variable
ENV PATH=/root/.local:$PATH

CMD [ "python", "./server.py" ]
```

https://www.docker.com/blog/containerized-python-development-part-2/ 讲docker-compose 用处不很大



## 7.12

#### TOML

https://realpython.com/python-toml/

[Why not TOML?](https://dev.to/siddharthshyniben/why-not-toml-1fj9)

https://realpython.com/python-virtual-environments-a-primer/ 这篇文章更新了几次，比起2020看的时候好像删掉一些有用内容, 改成这句

> A Python virtual environment is just a folder structure. 



## 7.13

### Conda 

[New Release: Anaconda Distribution Now Supporting M1](https://www.anaconda.com/blog/new-release-anaconda-distribution-now-supporting-m1)



### TensorFlow

要使用 Keras 只有安装 tensorflow就可以

安装失败 https://www.tensorflow.org/install

[Could not find a version that satisfies the requirement tensorflow](https://stackoverflow.com/questions/48720833/could-not-find-a-version-that-satisfies-the-requirement-tensorflow) 里面的回答都不对，但`pip install tensorflow-macos` 试了居然可以

```
pip install tensorflow
ERROR: Could not find a version that satisfies the requirement tensorflow (from versions: none)
//但是这个可以
pip install tensorflow-macos 
```

[What is the proper way to install TensorFlow on Apple M1 as conda has supported M1](https://stackoverflow.com/questions/72964800/what-is-the-proper-way-to-install-tensorflow-on-apple-m1-as-conda-has-supported) 我完美总结

但其实 [How to Setup TensorFlow on Apple M1 Pro and M1 Max (works for M1 too)](https://www.mrdbourke.com/setup-apple-m1-pro-and-m1-max-for-machine-learning-and-data-science/) 是我列出四篇文章中最好的

> Let's start by installing various TensorFlow dependencies (TensorFlow is a large piece of software and *depends* on many other pieces of software).
>
> Rather than list these all out, Apple have setup a quick command so you can install almost everything TensorFlow needs in one line.
>
> Apple have created a fork (copy) of TensorFlow specifically for Apple Macs. It has all the features of TensorFlow with some extra functionality to make it work on Apple hardware.
>
> Now we've got base TensorFlow installed, it's time to install `tensorflow-metal`.
>
> Why?
>
> Machine learning models often benefit from GPU acceleration. And the M1, M1 Pro and M1 Max chips have quite powerful GPUs.
>
> TensorFlow allows for automatic GPU acceleration if the right software is installed.
>
> And Metal is Apple's framework for GPU computing.

[What is the difference between miniconda and miniforge?](https://stackoverflow.com/questions/60532678/what-is-the-difference-between-miniconda-and-miniforge) 讨论 mamba [Open Software Packaging for Science](https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23)

https://github.com/apple/tensorflow_macos

https://developer.apple.com/metal/tensorflow-plugin/

https://blog.tensorflow.org/2021/06/pluggabledevice-device-plugins-for-TensorFlow.html 

[Deep Learning on the M1 Pro with Apple Silicon](https://wandb.ai/tcapelle/apple_m1_pro/reports/Deep-Learning-on-the-M1-Pro-with-Apple-Silicon---VmlldzoxMjQ0NjY3) 性能上一些比较数据

[Installing PyTorch on Apple M1 chip with GPU Acceleration](https://towardsdatascience.com/installing-pytorch-on-apple-m1-chip-with-gpu-acceleration-3351dc44d67c) PyTorch就先放一边

## 7.14

### TensorFlow cont

继续验证tensorflow,  我也加了自己回答，再装一个环境试试。

安装好就需要 Run a Benchmark by training the **MNIST** dataset

https://venturebeat.com/2020/11/18/google-releases-new-version-of-tensorflow-optimized-for-macos/ 解释 `tensorflow-mac` 

*Deep Learning with Python, Second Edition* 看看这回能不能看下去

## 7.18

### pivot

[SQL query to pivot a column using CASE WHEN](https://stackoverflow.com/questions/5846007/sql-query-to-pivot-a-column-using-case-when) 和 https://learnsql.com/blog/case-when-with-sum/ 解释行转列，中文文章 [SQL行转列，列转行](https://zhuanlan.zhihu.com/p/66207434)

Pivot table basics: rows to columns  https://codingsight.com/pivot-tables-in-mysql/

[How to Optimize/Refactor MySQL Pivot Table Performance when using Where Clause](https://stackoverflow.com/questions/58229470/how-to-optimize-refactor-mysql-pivot-table-performance-when-using-where-clause)

[SQL query to pivot a column using CASE WHEN](https://stackoverflow.com/questions/5846007/sql-query-to-pivot-a-column-using-case-when)

[MySQL - Rows to Columns](https://stackoverflow.com/questions/1241178/mysql-rows-to-columns)

https://www.tarynpivots.com/post/how-to-rotate-rows-into-columns-in-mysql/ "MySQL does not have `PIVOT` function, so in order to rotate data from rows into columns you will have to use a `CASE` expression along with an aggregate function."

总结我的问题 [How to improve mysql query performance for the rows to columns pivot table?](https://stackoverflow.com/questions/73107377/how-to-improve-mysql-query-performance-for-the-rows-to-columns-pivot-table)

## 7.19

https://github.com/jeffheaton/t81_558_deep_learning

开始看 Deep Learning with Python, Second Edition, **chapter one**

### neural networks

[Neural Networks](https://www.ibm.com/cloud/learn/neural-networks) Each node, or artificial neuron, connects to another and has an associated **weight** and **threshold**. If the output of any individual node is above the specified threshold value, that node is **activated**, sending data to the next layer of the network. Otherwise, no data is passed along to the next layer of the network.



### SciKit Learn vs TensorFlow vs PyTorch

[Differences in SciKit Learn, Keras, or Pytorch](https://stackoverflow.com/questions/54527439/differences-in-scikit-learn-keras-or-pytorch) "SciKit Learn is not a neural network framework"

[Scikit-learn, TensorFlow, PyTorch, Keras… but where to begin?](https://towardsdatascience.com/scikit-learn-tensorflow-pytorch-keras-but-where-to-begin-9b499e2547d0) "if you want to predict the price of future NBA game tickets, then scikit-learn’s ability to **crunch structured data** is all you need." 就学一种，从简单开始

[What's the difference between scikit-learn and tensorflow? Is it possible to use them together?](https://stackoverflow.com/questions/61233004/whats-the-difference-between-scikit-learn-and-tensorflow-is-it-possible-to-use) 回答没有太多有用信息。

https://www.simplilearn.com/scikit-learn-vs-tensorflow-article scikit-learn能干什么没写出

https://www.simplilearn.com/keras-vs-tensorflow-vs-pytorch-article 帮助不大，因为我已经选定 keras

[Are The New M1 Macbooks Any Good for Data Science? Let’s Find Out](https://towardsdatascience.com/are-the-new-m1-macbooks-any-good-for-data-science-lets-find-out-e61a01e8cad1) 没细看，有机会再看

## 7.20

### keras chapter 2

翻看历史记录 2020.12.25 （圣诞！）看到这一章，一年半之后再次挑战！

[Are The New M1 Macbooks Any Good for Deep Learning? Let’s Find Out](https://towardsdatascience.com/are-the-new-m1-macbooks-any-good-for-deep-learning-lets-find-out-b475ad70dec2) 训练模型的基本代码步骤

[Top 5 Books to Learn Data Science in 2021](https://towardsdatascience.com/top-5-books-to-learn-data-science-in-2020-f43153851f14)

看看 hands-on 关于 MNIST的表述



## 7.21

### chapter 2

Gradient descent

4个系列视频

[Gradient descent, how neural networks learn | Chapter 2, Deep learning](https://www.youtube.com/watch?v=IHZwWFHWa-w) 视频里提到的材料，翻看历史记录2021.5.6 记录看了 http://neuralnetworksanddeeplearning.com/



## 7.26

### MNIST 学习

http://neuralnetworksanddeeplearning.com/chap1.html



## 7.29

### pexpect

翻看记录 2020.9.11研究过相同问题，这次其实又重新解决一次，不过好像也有点小进展

[Is it possbile to let pexpect output the texts it matches?](https://stackoverflow.com/questions/63825774/is-it-possbile-to-let-pexpect-output-the-texts-it-matches) 说明需要 `child.logfile_read = sys.stdout`
这次  [pexpect.interact(): TypeError: write() argument must be str, not bytes](https://stackoverflow.com/questions/73149936/pexpect-interact-typeerror-write-argument-must-be-str-not-bytes) 说明要设置 `child.logfile_read = None` 而且自己上次也提了！！

另外一点教训 `npm ERR! code EOTP` 就说OTP输错了，因为邮件太多看混了，以为脚本有问题。



## 8.15

### for...loop vs itertools

[You (Probably) Don’t Need For-Loops](https://medium.com/python-pandemonium/never-write-for-loops-again-91a5a4c84baf) 这个是一直都需要注意，文章提到 itertools 再学习一下

https://www.educative.io/answers/what-are-itertools-in-python

https://www.pythoncheatsheet.org/modules/itertools-module 另 https://www.pythoncheatsheet.org/ 对python 知识点分类比较清晰，但讲解不全面

开始没明白 `groupby` 看了 [itertools and functools : Two Python Lone Soldiers](https://towardsdatascience.com/itertools-and-functools-two-python-lone-soldiers-7d3400495c89) 没看全



> Every time the value of the key function changes, it creates a break or a new group. This is in contrast to SQL’s GROUP BY, which groups similar data irrespective of the order. So it is important to sort the data in the first place before passing it to itertools.groupby .

...

> *key* specifies a function of one argument that is used to extract a comparison key from each element in *iterable* (for example, `key=str.lower`).

https://realpython.com/python-itertools/ 也没看全

另外注意一点 [pythonic way to do something N times without an index variable](https://stackoverflow.com/questions/2970780/pythonic-way-to-do-something-n-times-without-an-index-variable) 和 https://www.delftstack.com/howto/python/python-repeat-n-times/ (它的howto 系列内容太多太杂了)

```
for _ in range(num): 
for _ in itertools.repeat(None, num):
```

The `itertools.repeat(val, num)` method is an infinite iterator, which means it will iterate infinitely till the `break` statement if the `num` value (which represents the number of iterations) is not provided. The `val` parameter of this method represents the value that will be printed on each iteration.

As we want to repeat the iteration N times, we will pass the value of N to the `num` argument and `None` value to the `val` argument since we do not need to print anything. The `itertools.repeat()` method is more efficient than the `range()` method, but the `itertools` module needs to be imported to use this method.



## 8.16

### pager

[Too many tags so `git tag` will stop with a colon for further input](https://stackoverflow.com/questions/73368830/too-many-tags-so-git-tag-will-stop-with-a-colon-for-further-input)

[What is a pager?](https://unix.stackexchange.com/questions/144016/what-is-a-pager) 和 [Git-Config: core.pager](https://medium.com/pragmatic-programmers/git-config-core-pager-807e17d64243)

`git --no-pager tag -l "v[123467].*"` -l 支持的pattern 是 The pattern is a shell wildcard (i.e., matched using [fnmatch](https://docs.python.org/3/library/fnmatch.html) , 4个模式 * ?, `[seq]` 和 `[!seq]` 以前没注意

[How to tell which commit a tag points to in Git?](https://stackoverflow.com/questions/1862423/how-to-tell-which-commit-a-tag-points-to-in-git) 发现`git show-ref --abbrev=7 --tags` 没用pager (看VonC更新答复)， `git rev-list -1` 找到tag对应的commit id



[subprocess wildcard usage](https://stackoverflow.com/questions/9997048/subprocess-wildcard-usage)

https://devconnected.com/how-to-delete-local-and-remote-tags-on-git/



[Problems with command using * wildcard in subprocess](https://stackoverflow.com/questions/12267774/problems-with-command-using-wildcard-in-subprocess)

[subprocess wildcard usage](https://stackoverflow.com/questions/9997048/subprocess-wildcard-usage)

```
qiulang@qiulangdeMacBook-Air wechat % git --no-pager tag -l [v]5.*
zsh: no matches found: [v]5.*
qiulang@qiulangdeMacBook-Air wechat % git --no-pager tag -l "[v]5.*"
v5.4.0
v5.5.0
v5.5.1
v5.6.0
v5.7.0
v5.7.1
v5.7.2

所以我的代码开始写

'git --no-pager tag -l "[v]5.*"'
result = run(command.split(), stdout=PIPE, stderr=PIPE) 执行没有结果，需要改成
result = run(command, shell=True, stdout=PIPE, stderr=PIPE)

突然意识我的命令不需要shell执行，所以其实是 [v]5.* 不需要引号
'git --no-pager tag -l [v]5.*'
result = run(command.split(), stdout=PIPE, stderr=PIPE)
```



## 8.17

### argparse bool

bool 参数好像没什么好办法，翻看以前记录也没有, [A Simple Guide To Command Line Arguments With ArgParse](https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3) 也没写

**flag 参数** ('-' 或'--' 开始) 设置缺省值是一个办法，不给就用缺省值 false,给了就true， **position 参数**不好，因为position参数导致必填（即便有缺省值），而必填值只有空串是false。而且position参数也不好记。



## 8.26

### keras chapter 2 cont.

继续 7.20记录 从 **2.4.1 What’s a derivative?** 再次开始

https://www.mathsisfun.com/gradient.html   gradient 即 slope 这个网站以前访问过 mathsisfun

https://www.mathsisfun.com/calculus/derivatives-introduction.html  derivative of a function

和书上写的正相反 "The slope a is called the *derivative* of f in p", 不过 “The derivative of a tensor operation (or tensor function) is called a *gradient*.



## 9.11

### chapter 5 "The mechanics of learning"

keras chapter 2.4 几次都翻不过去，开始觉得是书写得有问题了。所以换 "Deep learning with PyTorch2" chapter 5 "The mechanics of learning"

安装 pytorch 很简单 ，明天验证 https://pytorch.org/get-started/locally/

[What is the difference between pip and conda?](https://stackoverflow.com/questions/20994716/what-is-the-difference-between-pip-and-conda) 没空看

pytorch 的 MNIST 例子可以找时间看看 https://pytorch.org/tutorials/recipes/recipes/defining_a_neural_network.html#defining-a-neural-network-in-pytorch 

[Installing Tensorflow on Apple M1 With the New Metal Plugin](https://betterprogramming.pub/installing-tensorflow-on-apple-m1-with-new-metal-plugin-6d3cb9cb00ca) 提到验证 MNIST 层级和ts书里说的不一样有时间验证。



### conda commands

如何 [How do I prevent Conda from activating the base environment by default?](https://stackoverflow.com/questions/54429210/how-do-i-prevent-conda-from-activating-the-base-environment-by-default)

Conda cheatsheet 和 https://conda.io/projects/conda/en/latest/user-guide/getting-started.html



### python knowledge

https://realpython.com/python-strings/

https://www.runoob.com/python/att-string-center.html "字符串字符数为奇数时左侧字符会比右侧少 1，字符串字符数为偶数时左侧字符会比右侧多 1"

[How to implement center() by padding the extra character always on the left?](https://stackoverflow.com/questions/73699051/how-to-implement-center-by-padding-the-extra-character-always-on-the-left)



## 9.19

### Deep learning with PyTorch2

快速浏览完第五章（对应keras chapter 2.4 ），觉得应该从第三章重新看起。



## 10.1 假期

### pytorch chapter 3-5


[Pip vs Conda: an in-depth comparison of Python’s two packaging systems](https://pythonspeed.com/articles/conda-vs-pip)

Grokking Deep Learning-2019 chapter 4 -- chapter 6

OReilly.Hands-on.Machine.Learning.with.Scikit-Learn.Keras.and.TensorFlow.2nd.2019.9  **Gradient Descent**



### YouTube  [3Blue1Brown](https://www.youtube.com/c/3blue1brown)

1. [But what is a neural network? | Chapter 1, Deep learning](https://www.youtube.com/watch?v=aircAruvnKk)
2. [Gradient descent, how neural networks learn | Chapter 2, Deep learning](https://www.youtube.com/watch?v=IHZwWFHWa-w)
3. [What is backpropagation really doing? | Chapter 3, Deep learning](https://www.youtube.com/watch?v=Ilg3gGewQ5U)
4. [Backpropagation calculus | Chapter 4, Deep learning](https://www.youtube.com/watch?v=tIeHLnjs5U8&t=134s)

*Backpropagation* 需要再学习

翻看记录 [7.21](#7.21)都学习过，又过了三个月。这学习速度真的要提高
