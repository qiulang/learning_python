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

https://roadmap.sh/python

dunder methods  [Difference between len() and .__len__()?](https://stackoverflow.com/questions/2481421/difference-between-len-and-len)



## 2.15

`ag --js "xxx"` 当前目录下， 没有直接对应grep,大致是 `grep -r "xxx" *` 没有简单方法指定文件类型

http://conqueringthecommandline.com/book/frontmatter

用 ag 查了 我在这个问题单里写的代码 https://github.com/nodejs/node/issues/38339  而且也试了node 17.5 确实没有改进



## 3.16

### color term

以前用 https://pypi.org/project/termcolor/  很多人推荐，但是这个项目好像不更新了。 https://github.com/matthewdeanmartin/termcolor 自称  This is the successor to `termcolor`  但目前只有一颗星。

https://pypi.org/project/colorful/ 目前最多星，但是19年后来没更新 

[How to print colored text to the terminal](https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal) 很多答复，选了其中的 https://github.com/bluenote10/yachalk 他提到基于npm的chalk是我选一个原因。

另个看着太复杂，没时间研究 https://click.palletsprojects.com/en/8.0.x/

今天用m1 macOS 12.2 自带 python 3.8 执行之前脚本一直没结果，从 https://www.python.org/ 下3.10 第一次执行也很久，才发现可能是网络问题导致  `git remote add` 需要很长时间，再次执行就好了。所以可能和 3.8也没关系。



### Nullsafe operator

Python 没有，php 8 也开始支持， nodejs 14开始支持 refer to https://wiki.php.net/rfc/nullsafe_operator
