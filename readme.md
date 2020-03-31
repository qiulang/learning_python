## 学习 Python

### 4.6 更新

#### ”A Whirlwind Tour“

对照着这本书 [A Whirlwind Tour of Python](<https://jakevdp.github.io/WhirlwindTourOfPython/>) 来学习Python

但环境设置碰到一点小麻烦，首先从 www.python.org 下载Python安装，有两个应用， Python Launcher做什么？[在SO论坛提问](<https://apple.stackexchange.com/questions/356243/what-does-python-launcher-do>) , 不过自己现在 <https://docs.python.org/3.7/using/mac.html> 找到答案，原来是为了在 finder里启动Python脚本用的。

A Whirlwind Tour 建议用 MiniConda/AnaConda 自然就引发一个新问题，MiniConda 到底是干什么的，和python/pip又是什么关系 ? 看到这两篇 1. [What is the difference between pip and conda?](https://stackoverflow.com/questions/20994716/what-is-the-difference-between-pip-and-conda)  2. [Understanding Conda and Pip](https://www.anaconda.com/understanding-conda-and-pip/)  简单的说，是不是做科学计算的时候我需要Conda,目前学习阶段还不是必须？

安装 MiniConda 碰到问题两个问题：

1. 没法安装在 ~ 目录下，装在 `/miniconda3` 下。
2. 虽然用Python 3 的版本，但是再安装iPython还是用 Python 2，[给它开了一个问题单](https://github.com/conda/conda/issues/8513)，不知道会不会有人理?  能看到的明显问题是 它装的iPython 是 5.X版本

改用 pip3 install iPython 是7的版本，用的就是 Python 3！ 同时发现要想直到pip到底把包装在哪里就用 pip3 show xxx, 比如



```bash
pip3 show ipython
Name: ipython
Version: 7.4.0
Summary: IPython: Productive Interactive Computing
Home-page: https://ipython.org
Author: The IPython Development Team
Author-email: ipython-dev@python.org
License: BSD
Location: /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages
Requires: traitlets, jedi, appnope, setuptools, decorator, prompt-toolkit, pexpect, pygments, backcall, pickleshare
Required-by:
```

测试发现安装 AnaConda 带的安装包iPython没这个问题。

决定先卸载MiniConda，发现也没有简单的卸载方法，google 也没太好结果，[这里说直接删了](http://deeplearning.lipingyang.org/2018/12/24/install-miniconda-on-mac/)



### 4.16 更新

#### Anaconda

uninstall就是直接删，rm -fr <https://docs.anaconda.com/anaconda/install/uninstall/>

更新 .bash_profile 去掉 anaconda部分

<https://github.com/conda/conda/issues/8513>



### 10.8 更新

。。。 搁置了半年！！！

暂不使用 Anaconda

#### [Python's 3 main applications](https://www.freecodecamp.org/news/what-can-you-do-with-python-the-3-main-applications-518db9a68a78/)

两个Python 脚本

1. 取翻译结果 https://automatetheboringstuff.com/chapter11/
2. [Bashing the Bash — Replacing Shell Scripts with Python](https://medium.com/capital-one-tech/bashing-the-bash-replacing-shell-scripts-with-python-d8d201bc0989)

[What Can I Do With Python?](https://realpython.com/what-can-i-do-with-python/)

#### python & pip 版本问题

首先为什么macOS建议  `#!/usr/bin/env python3` 

  [Why is it better to use “#!/usr/bin/env NAME” instead of “#!/path/to/NAME” as my shebang?](https://unix.stackexchange.com/questions/29608/why-is-it-better-to-use-usr-bin-env-name-instead-of-path-to-name-as-my) 

[pip or pip3 to install packages for Python 3?](https://stackoverflow.com/questions/40832533/pip-or-pip3-to-install-packages-for-python-3)

查看brew 安装的具体信息 `brew info python` 我的pip不是指向pip3的软连接，所以安装包要用pip3

`pip list` 和`pip3 list` 显示结果不一样

安装提示 运行 不知道装在哪了！！

```shell
You are using pip version 19.0.3, however version 19.2.3 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
~ ➤ pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/30/db/9e38760b32e3e7f40cce46dd5fb107b8c73840df38f0046d8e6514e675a1/pip-19.2.3-py2.py3-none-any.whl (1.4MB)
    100% |████████████████████████████████| 1.4MB 9.8kB/s
Installing collected packages: pip
  Found existing installation: pip 10.0.1
    Uninstalling pip-10.0.1:
      Successfully uninstalled pip-10.0.1
Successfully installed pip-19.2.3
~ ➤ which pip
/usr/local/bin/pip
~ ➤ ls -al /usr/local/bin/pip
lrwxr-xr-x  1 qiulang  admin  35 Jul  5  2018 /usr/local/bin/pip -> ../Cellar/python@2/2.7.15_1/bin/pip
~ ➤ which pip3
/usr/local/bin/pip3
~ ➤ ls -al /usr/local/bin/pip3
lrwxrwxr-x  1 root  admin  66 Apr 11 13:31 /usr/local/bin/pip3 -> ../../../Library/Frameworks/Python.framework/Versions/3.7/bin/pip3 /* 这是通过Python的官网安装包*/
```



这才发现原因

```shell
~ ➤ brew uninstall python@2
Error: Refusing to uninstall /usr/local/Cellar/python@2/2.7.15_1
because it is required by gobject-introspection and mongodb, which are currently installed.
You can override this and force removal with:
  brew uninstall --ignore-dependencies python@2
```



但是这之后

```
~ ➤ pip list
zsh: command not found: pip
~ ➤ which pip
pip not found
~ ➤ brew install python
Updating Homebrew...
==> Auto-updated Homebrew!
Updated 1 tap (homebrew/cask).
No changes to formulae.

Warning: python 3.7.2_1 is already installed, it's just not linked
You can use `brew link python` to link this version.
~ ➤ brew link python
Linking /usr/local/Cellar/python/3.7.2_1...
Error: Could not symlink bin/2to3
Target /usr/local/bin/2to3
already exists. You may want to remove it:
  rm '/usr/local/bin/2to3'

To force the link and overwrite all conflicting files:
  brew link --overwrite python

To list all files that would be deleted:
  brew link --overwrite --dry-run python
~ ➤ brew link --overwrite python
Linking /usr/local/Cellar/python/3.7.2_1... 24 symlinks created
~ ➤ pip list
zsh: command not found: pip
~ ➤ which pip
pip not found
```



只好重装

```shell
~ ➤ brew uninstall python
Uninstalling /usr/local/Cellar/python/3.7.2_1... (8,437 files, 118MB)
~ ➤ brew install python
Python has been installed as
  /usr/local/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /usr/local/opt/python/libexec/bin

If you need Homebrew's Python 2.7 run
  brew install python@2

You can install Python packages with
  pip3 install <package>
They will install into the site-package directory
  /usr/local/lib/python3.7/site-packages
```



pip 还是没有

```shell
~ ➤ which pip
pip not found
~ ➤ which pip3
/usr/local/bin/pip3
~ ➤ pip3 list
Package           Version
----------------- -------
astroid           2.2.5
isort             4.3.17
lazy-object-proxy 1.3.1
mccabe            0.6.1
pip               18.1
pylint            2.3.1
setuptools        40.6.3
six               1.12.0
typed-ast         1.3.1
wheel             0.32.3
wrapt             1.11.1
~ ➤ pip3 install --upgrade pip
Collecting pip
  Using cached https://files.pythonhosted.org/packages/30/db/9e38760b32e3e7f40cce46dd5fb107b8c73840df38f0046d8e6514e675a1/pip-19.2.3-py2.py3-none-any.whl
Installing collected packages: pip
  Found existing installation: pip 18.1
    Uninstalling pip-18.1:
      Successfully uninstalled pip-18.1
Successfully installed pip-19.2.3
~ ➤ pip list
Package           Version
----------------- -------
astroid           2.2.5
isort             4.3.17
lazy-object-proxy 1.3.1
mccabe            0.6.1
pip               19.2.3
pylint            2.3.1
setuptools        40.6.3
six               1.12.0
typed-ast         1.3.1
wheel             0.32.3
wrapt             1.11.1
~ ➤ which pip
/usr/local/bin/pip
~ ➤ pip --version
pip 19.2.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)

python3 也指对了

~ ➤ which python3
/usr/local/bin/python3
~ ➤ ls -al /usr/local/bin/python3
lrwxr-xr-x  1 qiulang  admin  36 Oct  8 17:53 /usr/local/bin/python3 -> ../Cellar/python/3.7.2_1/bin/python3


但是pip 和 pip3不是同一个

~ ➤ which pip
/usr/local/bin/pip
~ ➤ which pip3
/usr/local/bin/pip3
~ ➤ ls -al /usr/local/bin/pip
-rwxr-xr-x  1 qiulang  admin  235 Oct  8 17:58 /usr/local/bin/pip
~ ➤ ls -al /usr/local/bin/pip3
lrwxr-xr-x  1 qiulang  admin  33 Oct  8 17:53 /usr/local/bin/pip3 -> ../Cellar/python/3.7.2_1/bin/pip3
~ ➤ pip --version
pip 19.2.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
~ ➤ pip3 --version
pip 19.2.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)

```



教训，不要同时用 python官网安装包和 brew install python安装



### 10.11 更新

#### “Automate the Boring Stuff with Python”  -- Web Scraping

练习 “Automate the Boring Stuff with Python”   Chapter 11 – Web Scraping 的第一个例子，打开搜索结果，就碰到不少问题，首先程序运行完没有任何结果。

断点调试第一步，如何输入参数，还好vscode 是统一的，和nodejs调试一样

其次仔细检查返回结果发现 用页面打开和用代码发的返回内容不一样， 代码返回 class="kCrYT"，而且 `soup.select('.kCrYT > a')` 也得不到正确结果，[SO提到别的答案](https://stackoverflow.com/questions/56664934/soup-select-r-a-in-fhttps-google-com-searchq-query-brings-back-empty)也不行



注， https://github.com/IFinners/automate-the-boring-stuff-projects 代码或许可以参考，跑下载图片例子不成功。



### 10.12 更新

#### selenium

1. 下载图片例子完成

2. pip -U 解释

   `-U` means `--update` and it will update the library (`pytest` in your case) to the latest version available (5.0.1 right now)

   If you don't use `-U` / `--update` and you have the library already installed, `pip` will not install the latest version.

3. 安装 selenium 包失败，估计是被墙，**设置国内代理**

   `pip install -U selenium -i https://pypi.tuna.tsinghua.edu.cn/simple` 马上成功

   所以设置全局   https://mirror.tuna.tsinghua.edu.cn/help/pypi/

   ```
   pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
   ```
   
4. 运行 selenium 打开浏览器失败，因为没装 driver


   ```shell
   FileNotFoundError: [Errno 2] No such file or directory: 'geckodriver': 'geckodriver'
   selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
   ```

   https://pypi.org/project/selenium/ 其实写了

   Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires [geckodriver](https://github.com/mozilla/geckodriver/releases), which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

   下载完还要放到PATH里

   下载 [geckodriver v0.25.0](https://github.com/mozilla/geckodriver/releases/tag/v0.25.0) 因为v0.26还是 Pre-release ，运行发生错误 `selenium.common.exceptions.WebDriverException: Message: invalid argument: can't kill an exited process`

   [SO解答](https://stackoverflow.com/questions/52534658/webdriverexception-message-invalid-argument-cant-kill-an-exited-process-with)  [*GeckoDriver*, *Selenium* and *Firefox Browser* compatibility chart](https://firefox-source-docs.mozilla.org/testing/geckodriver/geckodriver/Support.html)

   更新到 v0.26就好了  模拟点击事件 。


5. google translate 初步例子可以

   [list join要用 string](https://stackoverflow.com/questions/493819/why-is-it-string-joinlist-instead-of-list-joinstring) 

   但有时候会找不到翻译结果的元素  target = browser.find_element_by_class_name('translation')， 还不知道为啥？
  
6. 周末把 [Bashing the Bash — Replacing Shell Scripts with Python](https://medium.com/capital-one-tech/bashing-the-bash-replacing-shell-scripts-with-python-d8d201bc0989) 也练习下。

#### with & lamda

1. with & lambda 用法 (“匿名函数？”) 
2. map, filter lamda

lambda *arguments* : *expression*

```
x = lambda a : a + 10
x = lambda a, b : a * b
```





### 10.14 更新

#### string , path



```python
list(map())
any(list) & all(list)
foldername.split(os.sep)
zip文件写不写目录名好像没啥区别
backupZip.write(foldername)
abspath
```



Jupyter Notebook 到底干什么

https://www.infoworld.com/article/3347406/what-is-jupyter-notebook-data-analysis-made-easier.html

`if __name__ == "__main__":`  https://stackoverflow.com/questions/419163/what-does-if-name-main-do

type hint



Pathlib vs os.path

https://www.linuxjournal.com/content/easier-python-paths-pathlib

>  / is a Python operator

[Python String Formatting Best Practices](https://realpython.com/python-string-formatting/) 

1. % Operator
2. [f-Strings](https://realpython.com/python-f-strings/) **3.6 才有！**



### 10.15 更新

#### variable scope

[What's the scope of a variable initialized in an if statement?](https://stackoverflow.com/questions/2829528/whats-the-scope-of-a-variable-initialized-in-an-if-statement) 没有block level的scope



### 10.17 更新

#### thread

1. 多线程下载例子，The regular arguments can be passed as a list to the `args` keyword argument in `threading.Thread()`. The keyword argument can be specified as a dictionary to the `kwargs` keyword argument in `threading.Thread()`.

2. 彩色命令行输出，因为node.js的debug很好用，所以查查Python有没有类似的。发现有几个，试了 `termcolor`  https://pypi.org/project/termcolor/ 但要注意，因为我的item用了zsh,所以 attrs 的属性像 *concealed* 和 *blink* 没效果。

3. tuple vs list 

   1. https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples

   2. https://stackoverflow.com/questions/1708510/list-vs-tuple-when-to-use-each

   3. [Could we always use the list type as the function parameter when the tuple type parameter is expected?](https://stackoverflow.com/questions/48038883/could-we-always-use-the-list-type-as-the-function-parameter-when-the-tuple-type)

4. pathlib 练习 https://stackabuse.com/introduction-to-the-python-pathlib-module/



### 10.18 更新

#### pathlib

pathlib 练习续，`files = Path('./removeCsvHeader/').glob("*.csv")` 或者 `files = Path('.').glob("removeCsvHeader/*.csv")` 都可以.



但是[如何用pathlib打开文件写](https://stackoverflow.com/questions/58443632/how-do-i-use-pathlib-csv-module-to-write)是个问题 ! 原因也简单，但要注意用 pathlib 读写文件（不涉及csv模块）方法。

pathlib 有自己的读写方法 ["Reading and Writing Files using Pathlib"](https://stackabuse.com/introduction-to-the-python-pathlib-module/)

但需要把open的返回值，File object传给csv ，这点其实和build-in open 方法是一样的。



json 数据例子，返回数据最好判断类型 `isinstance` 



### 10.20 更新

#### venv

[虚拟环境 venv 学习](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments), 

> Please note that `venv` does not permit creating virtual environments with other versions of Python. For that, install and use the `virtualenv` [package](https://pypi.python.org/pypi/virtualenv).

[Python 包管理一些基本概念](https://www.datacamp.com/community/tutorials/pip-python-package-manager), 比如科学计算为啥要用 Anaconda，比如要是用pip安装，https://www.scipy.org/install.html

`python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose`



查看包缺省安装目录 `pip show `  在哪个 `site-packages`

```shell
pip show selenium                                                                               git:master
Name: selenium
Version: 3.141.0
Summary: Python bindings for Selenium
Home-page: https://github.com/SeleniumHQ/selenium/
Author: UNKNOWN
Author-email: UNKNOWN
License: Apache 2.0
Location: /usr/local/lib/python3.7/site-packages
Requires: urllib3
Required-by:
...
pip3 install --user pandas
...
pip3 show pandas                                                                                git:master
Name: pandas
Version: 0.25.2
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /Users/qiulang/Library/Python/3.7/lib/python/site-packages
Requires: numpy, python-dateutil, pytz
Required-by:
```

关于 [python package]((https://hackernoon.com/pip-install-abra-cadabra-or-python-packages-for-beginners-33a989834975)) ， 暂时没时间看

关于 [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/) 暂时没时间看, **10.23练习！**



**练习 venv**

1. pyvenv.cfg 文件 `include-system-site-packages = false` 缺省是false，练习时候图方便改true

2. [bs4 如何使用不同parser](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser) 如果装了`lxml` 但是调用`bs4.BeautifulSoup()` 没写 lxml 会用lxml但是会有警告信息，所以还是写明好。

3. 单位的 vscode 不知道是激活什么脚本，也能正确取到venv设置 , 新打开一个shell是不行。晚上在我的macbook再试试。

4. [生成 requirement.txt](https://pip.pypa.io/en/latest/user_guide/#requirements-files)

5. pip install bs4

   > This is a dummy package managed by the developer of Beautiful Soup to prevent name squatting. The official name of PyPI’s Beautiful Soup Python package is [beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4). This package ensures that if you type pip install bs4 by mistake you will end up with Beautiful Soup.



### 10.22 更新

#### 学习 [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) 和 [Pipenv](https://pipenv.kennethreitz.org/en/latest/install/#installing-pipenv)

[virtualenv 激活目的](https://virtualenv.pypa.io/en/stable/userguide/#activate-script)  <1> 改 path

> This will change your `$PATH` so its first entry is the virtualenv’s `bin/` directory. (You have to use `source` because it changes your shell environment in-place.) This is all it does; it’s purely a convenience.

<2> venv 激活能使该环境安装的pip 包可用。

`source ./bin/activate` 后在shell 里敲 `deactivate` 就退出了，这时候虚拟环境安装的包又不可用了。

 virtualenv激活作用相同。  pipenv 试了 `deactivate` 命令好像可行, 但怎么[这里说不行](https://github.com/pypa/pipenv/issues/84)



[pipenv 映射 virtualenv 的方法](https://pipenv.kennethreitz.org/en/latest/install/#virtualenv-mapping-caveat)

> The virtualenv is stored globally with the name of the project’s root directory plus the hash of the full path to the project’s root (e.g., `my_project-a3de50`).



[Why you should use pyenv + Pipenv for your Python projects](https://hackernoon.com/reaching-python-development-nirvana-bb5692adf30c)



#### 练习 pipenv

pipenv 安装时候没有国内代理, 必须要修改 `Pipfile`

```python
[[source]] 
name = "pypi"
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
verify_ssl = true
```



根据 pipenv的官网介绍，我尝试用brew，但失败了, 因为brew安装的python和我用python 官网安装包安装的冲突

```shell
==> Installing pipenv dependency: python
==> Downloading https://homebrew.bintray.com/bottles/python-3.7.4_1.mojave.bottle.1.tar.gz
==> Downloading from https://akamai.bintray.com/38/387e32b735f3273bee16e8d8d20686ac40bd81e642a7e3d13cd21966698a4b77?__gda__=exp=1571747686~
######################################################################## 100.0%
==> Pouring python-3.7.4_1.mojave.bottle.1.tar.gz
Error: The `brew link` step did not complete successfully
The formula built, but is not symlinked into /usr/local
Could not symlink bin/2to3
...
Error: Permission denied @ dir_s_mkdir - /usr/local/Frameworks

bash-3.2$ brew info pipenv
pipenv: stable 2018.11.26 (bottled)
Python dependency management tool
https://docs.pipenv.org/
Not installed
From: https://github.com/Homebrew/homebrew-core/blob/master/Formula/pipenv.rb
==> Dependencies
Required: python ✔
==> Analytics
install: 11,449 (30 days), 32,674 (90 days), 155,686 (365 days)
install_on_request: 11,406 (30 days), 32,535 (90 days), 154,856 (365 days)
build_error: 0 (30 days)
```

同时还发现我的brew太慢了，没法简单设置国内镜像。[尝试问个问题](https://stackoverflow.com/questions/58505555/is-there-an-easy-way-to-change-homebrews-origins) 但后来觉得肯定是没有，给brew开了一个 [feature request](https://github.com/Homebrew/brew/issues/6640)，被接受了！

pip & npm 设置国内镜像


```shell
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
npm config set registry https://registry.npm.taobao.org
```

[Alpine Linux 镜像源](https://yq.aliyun.com/articles/695874)

中科大镜像 https://mirrors.ustc.edu.cn/help/alpine.html

pip & npm 各项设置

```shell
☁  Dev  pip3 config list -v
For variant 'global', will try loading '/Library/Application Support/pip/pip.conf'
For variant 'user', will try loading '/Users/langqiu/.pip/pip.conf'
For variant 'user', will try loading '/Users/langqiu/.config/pip/pip.conf'
For variant 'site', will try loading '/Library/Frameworks/Python.framework/Versions/3.7/pip.conf'
global.index-url='https://pypi.tuna.tsinghua.edu.cn/simple'
☁  Dev  ls /Users/langqiu/.config/pip/pip.conf
/Users/langqiu/.config/pip/pip.conf
☁  Dev  ls /Users/langqiu/.pip/pip.conf
ls: /Users/langqiu/.pip/pip.conf: No such file or directory
☁  Dev  cat /Users/langqiu/.config/pip/pip.conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

☁  Dev  npm config list
; cli configs
metrics-registry = "https://registry.npm.taobao.org/"
scope = ""
user-agent = "npm/6.4.1 node/v10.12.0 darwin x64"

; userconfig /Users/langqiu/.npmrc
prefix = "/Users/langqiu/.nvm/versions/node/v8.14.0"
registry = "https://registry.npm.taobao.org/"

; node bin location = /usr/local/bin/node
; cwd = /Users/langqiu/Dev
; HOME = /Users/langqiu
; "npm config ls -l" to show all defaults.

☁  Dev  brew --config
HOMEBREW_VERSION: 2.1.15
ORIGIN: https://github.com/Homebrew/brew
HEAD: 2bf8015bc44878d432fb9da4f11e1d8abcef8f32
Last commit: 6 days ago
Core tap ORIGIN: https://github.com/Homebrew/homebrew-core
Core tap HEAD: 29c7cfb92c0efed7fdb303f069bb3d2830fed636
Core tap last commit: 5 hours ago
HOMEBREW_PREFIX: /usr/local
CPU: quad-core 64-bit skylake
Homebrew Ruby: 2.6.3 => /usr/local/Homebrew/Library/Homebrew/vendor/portable-ruby/2.6.3/bin/ruby
Clang: 10.0 build 1001
Git: 2.20.1 => /Library/Developer/CommandLineTools/usr/bin/git
Curl: 7.54.0 => /usr/bin/curl
macOS: 10.14.6-x86_64
CLT: 10.3.0.0.1.1562985497
Xcode: N/A
CLT headers: 10.3.0.0.1.1562985497
```



### 10.23 更新

#### pipenv 镜像源

[pipenv 更新镜像源，不直接修改pipfile修改](https://pipenv-fork.readthedocs.io/en/latest/advanced.html#using-a-pypi-mirror)

列出安装包 pipenv graph



### 10.24 更新

#### main.py vs init.py

[What is __main__.py?](https://stackoverflow.com/questions/4042905/what-is-main-py)

[What is __init__.py for?](https://stackoverflow.com/questions/448271/what-is-init-py-for) 相当于[nodejs的index.js](https://stackoverflow.com/questions/43812514/javascript-equivalent-to-python-init-py) , https://alligator.io/react/index-js-public-interfaces/



OO Python ？？

https://docs.python-guide.org/writing/structure/#object-oriented-programming 



### 10.25 更新

#### init.py

`__init__.py`

https://pythontips.com/2013/08/01/packaging-and-distributing-your-python-libraries/

https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html

> It allows you to treat a directory as if it was a python module



### 10.27 更新

#### redis

写 redis的 pubsub例子

redis nodejs 客户端我们用ioredis,  https://github.com/NodeRedis/node_redis 上一次更新半年前，这里提到[pub/sub问题](https://cnodejs.org/topic/56835f18b9de25e81e01c211) 我们又恰好要用[pubsub](https://github.com/luin/ioredis#pubsub)



### 10.28 更新

#### generator 什么概念？

[What does the “yield” keyword do?](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)

[pubsub 使用](https://pypi.org/project/redis/) "There are three different strategies for reading messages." ... "If your application doesn’t need to do anything else but receive and act on messages received from redis, listen() is an easy way to get up an running."

[Python & Redis PUB/SUB](https://medium.com/@johngrant/python-redis-pub-sub-6e26b483b3f7)

[b string](https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal)



### 11.24

#### subprocess.Popen vs subprocess.run

这几个SO问题对连接它们很有帮助

1. [Running shell command and capturing the output](https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output)
2. 但使用 subprocess.run 问题是必须等到执行shell命令执行结束才输出，对于执行时间长的命令很不友好，所以查看了这个 Q&A  [Constantly print Subprocess output while process is running](https://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running) 但是它的答复太多，简单试了几个好像不生效。
3. [Read streaming input from subprocess.communicate()](https://stackoverflow.com/questions/2715847/read-streaming-input-from-subprocess-communicate) 终于找到能生效方法，但难道是必须用Popen？
4. [What is the difference between subprocess.popen and subprocess.run](https://stackoverflow.com/questions/39187886/what-is-the-difference-between-subprocess-popen-and-subprocess-run) 如果要看到命令执行过程输出，必须Popen
5. [What is the difference between using universal_newlines=True (with bufsize=1) and using default arguments with Popen](https://stackoverflow.com/questions/38181494/what-is-the-difference-between-using-universal-newlines-true-with-bufsize-1-an) 进一步解释 这两个参数作用

#### argparse

1. [argparse 比起自己写方法分享命令行输入方便多了](https://docs.python.org/2/howto/argparse.html)
2. 如果添加多余一个 position paramter 还没细研究，[或许可以参考](https://docs.python.org/2/library/argparse.html) 
3. https://mkaz.blog/code/python-argparse-cookbook/ 明天练习



### 11.25

#### Pexpect

https://pexpect.readthedocs.io/en/stable/index.html

但没机会尝试！



### 11.29 

#### argparse 总结

argparse 对照 cookbook 文章接着做修改。

Dictionary https://realpython.com/iterate-through-dictionary-python/

[How to Run Your Python Scripts](https://realpython.com/run-python-scripts/)

argparse 这个包其实和 npm包 yargs 作用相同，用nodejs写脚本可以参见[阮一峰这篇](http://www.ruanyifeng.com/blog/2015/05/command-line-with-node.html) 



### 12.1

#### 各种环境管理的总结

[An Effective Python Environment: Making Yourself at Home](https://realpython.com/effective-python-environment/) 各种环境管理的总结



### 12.3

#### null vs None

[null object in Python?](https://stackoverflow.com/questions/3289601/null-object-in-python)

[Ternary Operators](https://book.pythontips.com/en/latest/ternary_operators.html)



### 12.13

in operator, [不只是list](https://data-flair.training/blogs/python-operator/) string，tuple 也可以。

check_output

#### 暂停一段 python学习，学习 vue

vue  plugin vs mixin, plugin用来增加全局变量

[plugin 一个很简单例子](https://dev.to/nkoik/writing-a-very-simple-plugin-in-vuejs---example-8g8) 

[Understanding Mixins in Vue JS](https://blog.bitsrc.io/understanding-mixins-in-vue-js-bdcf9e02a7c1)

[Directives](https://vuejs.org/v2/guide/syntax.html#Directives) `v-bind = : , v-on = @ , v-if`  注意 directive是用来修改 dom元素

[v-for 遍历 数组或object](https://vuejs.org/v2/guide/list.html)

[mixin, directive, filter用在一起的一个简单例子](https://blog.logrocket.com/mixins-and-custom-functions-to-enhance-your-vue-applications-693caa7ae76a/)

css framework 重新评估后还是暂时选 [bulma](https://bulma.io/) , 这个比较可以看下 [Evaluating CSS Frameworks — Bootstrap vs Bulma vs Foundation vs Milligram vs Pure vs Semantic vs UIKit](https://codeburst.io/evaluating-css-frameworks-bulma-vs-foundation-vs-milligram-vs-pure-vs-semantic-vs-uikit-503883bd25a3) 



### 12.17

#### pyenv

用 pipenv 定位 3.5.2的问题

首先使用 pyenv 安装不同版本python:

1. 10.22做过 [Why you should use pyenv + Pipenv for your Python projects](https://hackernoon.com/reaching-python-development-nirvana-bb5692adf30c)
2. https://realpython.com/intro-to-pyenv/
3. https://weknowinc.com/blog/running-multiple-python-versions-mac-osx



发现我的脚本 iph.py在3.5.2运行错误原因是 正则匹配组的时候，3.5.2必须要再调用 group()才能得到匹配的组

[具体参见](https://github.com/YumaInaura/YumaInaura/issues/1281)

安装 3.5.2 时候编译出错，因为

```shell
zlib is keg-only, which means it was not symlinked into /usr/local,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

For compilers to find zlib you may need to set:
  export LDFLAGS="-L/usr/local/opt/zlib/lib"
  export CPPFLAGS="-I/usr/local/opt/zlib/include"
```



编译完还是没法改变版本，[在SO问](https://stackoverflow.com/questions/59377288/my-pyenv-can-not-switch-python-version-what-did-i-do-wrong) 无果，[给他开问题单](https://github.com/pyenv/pyenv/issues/1492) 很不客气的关了，说你就是没有设置 `eval "$(pyenv init -)"`  一开始我确实没有，但后来设置了。所以我才奇怪。但是经他这么一说，我突然想起来最新的macOS 15.2 已经把缺省shell从bash改成zsh，一试，果然是这个原因！

注意：安装一个python版本, pyenv会从下载源代码开始，然后编译，还是很耗时间，编译过程可能碰到的问题参见[这里](https://github.com/pyenv/pyenv/wiki/Common-build-problems)

pyenv是根据每个目录设置python版本，

```shell
learning_python ➤ ./re_test.py 
Traceback (most recent call last):
  File "./re_test.py", line 5, in <module>
    image_id = group[1]
TypeError: '_sre.SRE_Match' object is not subscriptable
learning_python ➤ re35/re_test.py /*两个文件完全一样*/
qiulang

learning_python ➤ pyenv version
3.5.3 (set by /Users/qiulang/Dev/learning_python/.python-version)
learning_python ➤ cd re35
re35 ➤ pyenv version
system (set by /Users/qiulang/Dev/learning_python/re35/.python-version)
```



### 12.24 

#### **

[What does ** (double star/asterisk) and * (star/asterisk) do for parameters?](https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters)

[Python : How to check if a key exists in dictionary ?](https://thispointer.com/python-how-to-check-if-a-key-exists-in-dictionary/)  `dict.get(key[, default])` 

[How do I let preinstalled python 2.7 access pip installed modules?](https://apple.stackexchange.com/questions/378272/how-do-i-let-preinstalled-python-2-7-access-pip-installed-modules)



### 12.25

#### 写处理 mysql脚本:

1. 参照 [Python Select from MySQL Table](https://pynative.com/python-mysql-select-query-to-fetch-data/) . 注意一点, google 搜索第一位的 [w3school 文章](https://www.w3schools.com/python/python_mysql_getstarted.asp) 使用的驱动 [mysql-connector](https://pypi.org/project/mysql-connector/) 已经Deprecated

2. 关于参数化查询，使用tuple的注意事项 [tuple](https://www.tutorialspoint.com/python/python_tuples.htm) :  To write a tuple containing a single value you have to include a comma, even though there is only one value `tup1 = (50,);` 

3. finally 一定会被掉用，即便有exit https://docs.python.org/2.5/whatsnew/pep-341.html



因为使用 python2 把 Popen 和 run,call区别又看了一遍，同时也熟悉 python2 下 如何实时读取子进程输出。

1. [What's the difference between subprocess Popen and call (how can I use them)?](https://stackoverflow.com/questions/7681715/whats-the-difference-between-subprocess-popen-and-call-how-can-i-use-them)

2. [What's the difference between Python's subprocess.call and subprocess.run](https://stackoverflow.com/questions/40697583/whats-the-difference-between-pythons-subprocess-call-and-subprocess-run)

3. [Realtime output from a shell command in Python](https://zaiste.net/realtime_output_from_shell_command_in_python/) : `process.communicate()` that blocks till given command is completed.



### 12.27



#### OO

OO ？ [A real life examples of object-oriented Python script? 这个问题始终是个困惑](https://softwareengineering.stackexchange.com/questions/403001/a-real-life-examples-of-object-oriented-python-script) 不幸真的被删，不过还是得到一个回答还，我觉得还可以

> A single script that is written to replace a bash script often does not require OO modeling, so this kind of scripts is often not a good example. Most of these scripts are designed to perform a single task in a mostly linear run, so a couple of loops and task specific logic is sufficient.
>
> OO design has its strengths when data has complex structure and lifetime, and when generalizations and specializations of classes are needed in a problem domain. For example, a script that should be able to deal with various media file formats might benefit from a hierarchy of file type handlers.
>
> The libraries used by scripts are the main places where objects happen, so you might have a look at the source code of packages from a domain that you're familiar with.
>
> Applications with a GUI or web interface might also be suitable examples, although probably less so than the library packages.



### 1.3

#### OOP again

第一次在reddit 提问 [A real life examples of object-oriented Python script?](https://www.reddit.com/r/learnpython/comments/ej9eh4/a_real_life_examples_of_objectoriented_python/)

一些 OOP 的文章

1. [Improve Your Python: Python Classes and Object Oriented Programming](https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)

2. [Object-Oriented Programming in Python vs Java](https://realpython.com/oop-in-python-vs-java/)

3. [Object-Oriented Programming in Python](https://python-textbok.readthedocs.io/en/1.0/#object-oriented-programming-in-python)

   

### 1.8

#### self

[What is the purpose of the word 'self', in Python?](https://stackoverflow.com/questions/2709821/what-is-the-purpose-of-the-word-self-in-python) 有几个答案值得看

1. https://stackoverflow.com/a/2725996/301513 基本复述了 ["Why explicit self has to stay" by Guido van Rossum](https://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html) 给类添加一个方法，复用一个def
2. https://stackoverflow.com/a/6433556/301513 模拟没用 class的实现
3. https://stackoverflow.com/a/2709857/301513 调用基类



[Adding Support for User-defined Classes](https://python-history.blogspot.com/2009/02/adding-support-for-user-defined-classes.html) 关于历史，有点长，说明了为啥要self



#### 结巴分词分析

1. https://blog.csdn.net/daniel_ustc/article/details/48195287

2. 结巴的模型数据来源 https://github.com/fxsjy/jieba/issues/7

   
  
### 1.9

#### setup.py

https://stackoverflow.com/questions/1471994/what-is-setup-py



### 1.17

#### generator & yield

[How to Use Generators and yield in Python](https://realpython.com/introduction-to-python-generators/)

[What does the “yield” keyword do?](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)

和 JavaScript应该一样的东西



#### relative import

1. [What does a . in an import statement in Python mean?](https://stackoverflow.com/questions/7279810/what-does-a-in-an-import-statement-in-python-mean)
2. https://www.python.org/dev/peps/pep-0328/#guido-s-decision



#### _compat.py

1. [Best Practices for Compatible Python 2 and 3 Code](https://pybit.es/python-porting.html)

2. https://chromium.googlesource.com/external/github.com/giampaolo/psutil/+/master/psutil/_compat.py

3. [Porting to Python 3 Redux](https://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/) 长，没看

4. [The key differences between Python 2.7.x and Python 3.x with examples](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html#the-__future__-module)

   

#### `__init__`

1. [What’s __init__ for me?](https://towardsdatascience.com/whats-init-for-me-d70a312da583)
2. ...



### 2.6

#### `__main__`

[Defining Main Functions in Python](https://realpython.com/python-main-function/)

#### `setup.py`
[A Practical Guide to Using Setup.py](https://blog.godatadriven.com/setup-py)

如何能执行 jieba 的test 代码？

[How to run tests without installing package?](https://stackoverflow.com/questions/23984973/how-to-run-tests-without-installing-package)



### 2.9

####执行 jieba 的test 代码

测试目录和代码目录同级. `pip3 install pytest` 但 `collected 0 items`  因为它没用pytest

看了下测试代码都有，所以其实直接进到test目录执行就行

```python
import sys
sys.path.append('../')
```



[Good Integration Practices](https://docs.pytest.org/en/latest/goodpractices.html#tests-outside-application-code)

### Tests outside application code

> Putting tests into an extra directory outside your actual application code might be useful if you have many functional tests or for other reasons want to keep tests separate from actual application code (often a good idea):

```python
setup.py
mypkg/
    __init__.py
    app.py
    view.py
tests/
    test_app.py
    test_view.py
    ...
```

[Python | end parameter in print()](https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/) 为了不换行



### 2.12

#### vscode format on save

发现一个[bug](https://github.com/microsoft/vscode-python/issues/10069)，vscode会修改import语句顺序，所以结巴的test代码一保存就出错了。注：见2.13 结果

关于import 语句顺序， [pep8](https://www.python.org/dev/peps/pep-0008/)

> Imports should be grouped in the following order:
>
> 1. Standard library imports.
> 2. Related third party imports.
> 3. Local application/library specific imports.
>
> You should put a blank line between each group of imports.
>

两个SO 讨论

1. [Python Import Order](https://softwareengineering.stackexchange.com/questions/341001/python-import-order)
2. [What's the correct way to sort Python `import x` and `from x import y` statements?](https://stackoverflow.com/questions/20762662/whats-the-correct-way-to-sort-python-import-x-and-from-x-import-y-statement)



#### 召回率与精确率

[如何解释召回率与精确率？](https://www.zhihu.com/question/19645541)

`recall = TP/All P `   & `precision = TP / All count` (分母是我的理解)

正确写法

`recall = TP/TP+FN`  & `precision = TP/TP+FP` 

[Beyond Accuracy: Precision and Recall](https://towardsdatascience.com/beyond-accuracy-precision-and-recall-3da06bea9f6c) 长，只看了前一小段，但是对于 [Imbalanced Classification Problems in machine learning](https://www.analyticsvidhya.com/blog/2017/03/imbalanced-classification-problem/) 怎么破？ 100人里有 5个坏人，坏人 recall 和 precision 容易理解，但是如果是计算好人，我把100人全归为好人，这时的 recall 和 precision 怎么理解 ？这是不是现实中 innocent unless proove otherwise ? 



#### jieba分析文章

[jieba分词学习笔记 一](https://segmentfault.com/a/1190000004061791)  Prefix Set是怎么要学习下 https://github.com/fxsjy/jieba/pull/187
[jieba分词学习笔记 二](https://segmentfault.com/a/1190000004065927?utm_source=tag-newest) DAG要学习下
[jieba分词学习笔记 三](https://segmentfault.com/a/1190000004085949?utm_source=tag-newest) 讲解DAG

一篇旧闻 [一篇文章总结语言处理中的分词问题](https://www.infoq.cn/article/nlp-word-segmentation/)



另外一组分析结巴的文章

https://blog.csdn.net/daniel_ustc/article/details/48195287 

https://blog.csdn.net/John_xyz/article/details/54645527

https://github.com/howl-anderson/MicroTokenizer



### 2.13

#### vscode format on save 

autopep8 

关于 [format on save的bug](https://github.com/microsoft/vscode-python/issues/10069) 对不需要格式化的行加 `# NOQA`



### 2.20

#### REST API test script

函数定义放在哪好 [Declare function at end of file in Python](https://stackoverflow.com/questions/3754240/declare-function-at-end-of-file-in-python) 对照2.6号关于main的文章

> The Pythonic way to write code is to divide your program into modules that define classes and functions, and a single "main module" that imports all the others and runs.
>
> For simple throw-away scripts get used to placing the "executable portion" at the end, or better yet, learn to use an interactive Python shell.

长串多行显示，而且没有多余字符 [Pythonic way to create a long multi-line string](https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string)



timeit 没法测试带输入参数的函数[how to pass parameters of a function when using timeit.Timer()](https://stackoverflow.com/questions/5086430/how-to-pass-parameters-of-a-function-when-using-timeit-timer)

> The code snippets must be self-contained - they cannot make external references. You must define your values in the statement-string or setup-string



[Python: variables scope and profile.run](https://stackoverflow.com/questions/8682716/python-variables-scope-and-profile-run)

> Instead of using `run()` use `runctx()` which allows you to supply locals and globals. 



还是简单用时间差吧 https://stackoverflow.com/questions/5478351/python-time-measure-function

[fstring 的各种格式](http://zetcode.com/python/fstring/) 



如何并行执行函数？

1.  [Running same function for multiple files in parallel in python](https://stackoverflow.com/questions/25889268/running-same-function-for-multiple-files-in-parallel-in-python)
2.  [Python: How can I run python functions in parallel?](https://stackoverflow.com/questions/7207309/python-how-can-i-run-python-functions-in-parallel)



找时间读 [Setting Up Python for Machine Learning on Windows](https://realpython.com/python-windows-machine-learning-setup/)


### 2.21

[What is the syntax rule for having trailing commas in tuple definitions?](https://stackoverflow.com/questions/7992559/what-is-the-syntax-rule-for-having-trailing-commas-in-tuple-definitions)

python 函数调用不可以给多的参数，这和[javascript 不一样](https://stackoverflow.com/questions/12694031/what-happens-if-i-call-a-js-method-with-more-parameters-than-it-is-defined-to-ac)



### 2.24

#### timeit

[Python Timeit Module (With Examples)](https://www.pylenin.com/blogs/python-timeit-module/)

有时间看他的[blog](https://www.pylenin.com/blogs/)



### 3.1

#### SO pyton 问题排名

[SO python 问题排名](https://stackoverflow.com/questions/tagged/python?tab=votes&page=1&pagesize=50)

比如访问环境变量 `os.environ`  [How to access environment variable values?](https://stackoverflow.com/questions/4906977/how-to-access-environment-variable-values)

[How do I check if a variable exists?](https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists) `in locals()` & `in globals()`

`in`操作符 可以检查 字符串是否包含某个子字符串，可以检查list 是否含某个元素

[How to use glob() to find files recursively?](https://stackoverflow.com/questions/2186525/how-to-use-glob-to-find-files-recursively) 才用上

[Calling a function of a module by using its name (a string)](https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string) 我用map



### 3.13

#### trie

https://www.hackerearth.com/zh/practice/data-structures/advanced-data-structures/trie-keyword-tree/tutorial/ 

https://brilliant.org/wiki/tries/

[Applications Of Trie Data Structure](http://blog.xebia.in/index.php/2015/09/28/applications-of-trie-data-structure/)

以上三篇大致看了，了解trie一些使用场景

[How Do I Choose Between a Hash Table and a Trie (Prefix Tree)?](https://stackoverflow.com/questions/245878/how-do-i-choose-between-a-hash-table-and-a-trie-prefix-tree)

[How to create a trie in Python](https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python)

这两个SO没看，要动手完成一个实际问题



#### autocomplete 

[Auto-complete feature using Trie](https://www.geeksforgeeks.org/auto-complete-feature-using-trie/)  练习

> For example if the Trie store {“abc”, “abcd”, “aa”, “abbbaba”} and the User types in “ab” then he must be shown {“abc”, “abcd”, “abbbaba”}.



[Trie autocomplete](https://medium.com/@daetam/trie-autocomplete-8dd23ddd3846) 更实际一点例子

[Implementing a Trie to support autocomplete in Python](https://stackoverflow.com/questions/46038694/implementing-a-trie-to-support-autocomplete-in-python)  SO 例子

```python
from collections import defaultdict
_trie = lambda: defaultdict(_trie)
trie = _trie()
for s in ["cat", "bat", "rat", "cam"]:
    curr = trie
    for c in s:
        curr = curr[c]
    curr.setdefault("_end")
    ...
```

以及 [Implementing a Trie in Python (in less than 100 lines of code)](https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1)



#### defaultdict

[How does collections.defaultdict work?](https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work)

```python
from collections import defaultdict

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1

d.items()
[('i', 4), ('p', 2), ('s', 4), ('m', 1)]

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

d.items()
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```



### 3.16

结巴代码先放一边，把 trie 和 DAG 先搞清楚

https://github.com/howl-anderson/MicroTokenizer



#### recursive

递归调用得到`none` 

[Why does my recursive function return None?](https://stackoverflow.com/questions/17778372/why-does-my-recursive-function-return-none)

[Python recursion with list returns None [duplicate]](https://stackoverflow.com/questions/2599149/python-recursion-with-list-returns-none)



#### class first attemp

用类方法实现tries



### 3.17 



#### 引入类练习

这个答案 3.16那两个更好结束为什么递归处理不当会得到None https://stackoverflow.com/questions/11356168/return-in-recursive-function



同一目录下不用relative import,[Creating and Importing Modules in Python](https://stackabuse.com/creating-and-importing-modules-in-python/)

同级目录引入用 relative import , 而且**直接运行**反而报错。 

1. [ModuleNotFoundError: What does it mean __main__ is not a package?](https://stackoverflow.com/questions/41816973/modulenotfounderror-what-does-it-mean-main-is-not-a-package)
2. [ModuleNotFoundError: No module named '__main__.xxxx'; '__main__' is not a package](https://stackoverflow.com/questions/45446418/modulenotfounderror-no-module-named-main-xxxx-main-is-not-a-packag)



没空看  [The Definitive Guide to Python import Statements](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html#absolute-vs-relative-import)

 `dict.get(key) vs dict[key]`   [Return None if Dictionary key is not available](https://stackoverflow.com/questions/6130768/return-none-if-dictionary-key-is-not-available)

#### 递归练习 

[Recursive merge sort in python](https://codereview.stackexchange.com/questions/154135/recursive-merge-sort-in-python)

[merge sort/recursion in python](https://stackoverflow.com/questions/47124512/merge-sort-recursion-in-python)



#### 练习

1. 完成 autocomplete 第一个练习。
2. 再找时间做另外两个练习
3. 先完成递归例子



### 3.20

#### divide & conquer

1. merge sort
2. binary search
3. 如何坚持数组是否排序了
4. quick sort



#### list comprehension &  Generator Expressions

[List Comprehensions in Python](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)

`new_list = [expression for member in iterable]` 

[Python List Comprehensions vs Generator Expressions](https://www.geeksforgeeks.org/python-list-comprehensions-vs-generator-expressions/)

`all(l[i] <= l[i+1] for i in range(len(l)-1))` 

长没看 https://realpython.com/list-comprehension-python/



### 3.22

#### quick_sort

https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/overview-of-quicksort

> The way that quicksort uses divide-and-conquer is a little different from how merge sort does. In merge sort, the divide step does hardly anything, and all the real work happens in the combine step. Quicksort is the opposite: all the real work happens in the divide step. In fact, the combine step in quicksort does absolutely nothing.

第一次尝试 quick_sort 不成功，没找到 divide 这部要怎么做好。



### 3.24 

quick_sort 进一步尝试，经过提示 divide 分出 partition方法，它返回pivot的index

vscode 大bug！！！

debugger 没法启动！ https://github.com/microsoft/vscode-python/issues/10684



### 3.26

####  vscode

vscode 没法启动python  debugger 居然是因为没有设置LANG环境变量！

1. https://github.com/microsoft/vscode-python/issues/10684
2. https://github.com/microsoft/debugpy/issues/87
3. https://apple.stackexchange.com/questions/385240/where-does-zsh-get-the-values-of-lang-lc-ctype-if-it-is-not-in-zshrc



### 3.27

#### jupyter

jupyter https://realpython.com/jupyter-notebook-introduction/ 了解下

[Getting Started to Work With Jupyter Notebooks in Visual Studio Code](https://towardsdatascience.com/getting-started-with-jupyter-notebooks-in-visual-studio-code-5dcccb3f739b)

https://code.visualstudio.com/docs/python/jupyter-support "[Jupyter](http://jupyter-notebook.readthedocs.io/en/latest/) (formerly IPython Notebook) is an open-source project that lets you easily combine Markdown text and executable Python source code on one canvas called a **notebook**."

https://www.quora.com/What-are-benefits-of-Jupyter-notebook-over-PyCharm-like-IDE



#### brew

想起我给brew开的feature request已经解决但到底怎么做到，查了下 [2.2.3](https://github.com/Homebrew/brew/packages/29947?version=2.2.3) 解决

[brew 的术语](https://docs.brew.sh/Formula-Cookbook)

https://docs.brew.sh/Manpage 这里提到改变源的几个变量

`HOMEBREW_BOTTLE_DOMAIN` `HOMEBREW_BREW_GIT_REMOTE` ``HOMEBREW_CORE_GIT_REMOTE`



#### quick_sort

第一次尝试成功，接下来优化



### 3.30

判断list是不是空，不用len(), 直接 if list ,因为 empty sequences and collections 就是 false , https://docs.python.org/3/library/stdtypes.html#truth-value-testing  

[In-place Quicksort, using the Hoare Partitioning scheme](https://stackoverflow.com/a/41211360/301513) In this scheme, the pivot's final location is not necessarily at the index that was returned, and the next two segments that the main algorithm recurs on are (lo..p) and (p+1..hi) as opposed to (lo..p-1) and (p+1..hi) as in Lomuto's scheme. However, the partitioning algorithm guarantees lo ≤ p < hi

> Quicksort is not very practical in Python since our builtin [timsort](https://en.wikipedia.org/wiki/Timsort) algorithm is quite efficient, and we have recursion limits. We would expect to sort lists in-place with [`list.sort`](https://docs.python.org/3/library/stdtypes.html#list.sort) or create new sorted lists with [`sorted`](https://docs.python.org/library/functions.html#sorted) - both of which take a `key` and `reverse` argument.

碰到问题改示例 pivot 为最末尾一个就报错

[Quicksort using Hoare Partitioning, how I chose pivot affects my python implement](https://stackoverflow.com/questions/60925885/quicksort-using-hoare-partitioning-how-i-chose-pivot-affects-my-python-implemen)

[Hoare partitioning falls into infinite loop](https://stackoverflow.com/questions/12520555/hoare-partitioning-falls-into-infinite-loop)

[Hoare partitioning scheme in Quicksort](https://cs.stackexchange.com/questions/97727/hoare-partitioning-scheme-in-quicksort)  解释了原因，晚点再仔细看下。

有就会再看 [A sort of quick guide to quicksort and Hoare’s partitioning scheme in Javascript](https://itnext.io/a-sort-of-quick-guide-to-quicksort-and-hoares-partitioning-scheme-in-javascript-7792112c6d1)



### 3.31

[Quicksort using Hoare Partitioning, how I chose pivot affects my python implement](https://stackoverflow.com/questions/60925885/quicksort-using-hoare-partitioning-how-i-chose-pivot-affects-my-python-implemen) 解答很清晰！

