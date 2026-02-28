# 2025 

2024下半年 开始 RAG、 大模型部署（e.g. vllm）的学习
4 月份开始 Xinference 的学习

## 4.23

### Xinference

读[Xinference: Making Large Model Serving Easy](Xinference-intro.pdf)

中文 [Xinference：企业级大模型推理和部署平台](https://www.53ai.com/news/LargeLanguageModel/2025010401745.html)

### MCP

https://huggingface.co/blog/Kseniase/mcp



## 4.27

### sglang vs vllm

https://github.com/qiulang/vllm-sglang-perf

别人做的 https://github.com/build-ai-applications/SgLang-vs-vLLM

https://buildaiapplications.com/blogs/sglang-vs.-vllm-vs.-lit-gpt-the-ultimate-llm-inference-evaluation/

https://www.cerebrium.ai/blog/benchmarking-vllm-sglang-tensorrt-for-llama-3-1-api

小模型评估

https://buildaiapplications.com/blogs/evaluating-small-language-models-a-deep-dive/



发现sglang 问题   https://github.com/qiulang/vllm-sglang-perf

https://github.com/sgl-project/sglang/issues/4245

https://github.com/sgl-project/sglang/issues/4245



## 12.10

### 一些 python 概念重新复习

#### Zero-based numbering

https://www.cs.utexas.edu/~EWD/transcriptions/EWD08xx/EWD831.html

https://cseducators.stackexchange.com/questions/5023/why-do-we-count-starting-from-zero

#### @dataclass

1. https://realpython.com/python-data-classes/  dataclass 更新了好几次
2. [The Evolution of Data Classes in Python: From namedtuple to @dataclass](https://medium.com/@tihomir.manushev/the-evolution-of-data-classes-in-python-from-namedtuple-to-dataclass-adedc2b13d83) 上一篇太长。这篇短点

 

#### pydantic

1. https://www.datacamp.com/tutorial/pydantic 文章里也提到 如何选择data class 和 **Pydantic**

>- **Use dataclasses** for internal data structures, configuration objects, or when performance is critical and you trust your data sources
>- **Use Pydantic** for API endpoints, user input, external data parsing, or when you need JSON serialization



2. 我自己和 claude 的讨论 https://claude.ai/chat/c41b32bd-bed1-4c21-8275-4d98feced9b5



## 12.29

### KV cache

1. https://ngrok.com/blog/prompt-caching/

2. https://poloclub.github.io/transformer-explainer/

3. https://grok.com/c/912bb617-3766-4a73-a215-29e2d282a1c4?rid=aafae2fd-51bd-4e2d-8604-03ec9f6fb7c1

4. https://gemini.google.com/app/e0c88b24c1f7ad7c

   

## 2026.1.28

### CLAUDE.md

1. https://claude.com/blog/using-claude-md-files
2. https://medium.com/@pankaj_pandey/claude-md-stop-explaining-the-same-stuff-to-claude-code-15c5f0ec85a1



## 2026.2.3

### 总结 python 学习手册

从 2019年4月份开始，学习python居然已经6年了！借助claude写了一份python手册（改了4版）。同时把每年记录的学习内容又会看了一遍。发现从一开我就对python虚拟环境的管理花了很多时间. 

手册里对 空list和 *args和**kwargs详解 我自己其实也没深入。

2020 5月找到一段话还是有意义，Bill Karwin的回答：

> To me, both Python and Ruby are basically like Perl, but with fixes for a bunch of the things that made Perl hard to use.
>
> The developers who drove Ruby popularity back in 2005 were always the kind of programmers who wanted to try new and shiny toys instead of proven and mature, so perhaps former Ruby users are trying out new languages.

还有另外一个有趣回复

> Python, perhaps simply through dumb luck (or not), was picked up by a lot of old Unix/C hackers in the late '90s and early aughts. It was also picked up by a lot of scientists. This lead to the creation of a lot of high-performance C libraries for Python for a very wide variety of tasks. Outside of maybe Java and C++, Python has more best-in-class libraries than almost any language out there, and the standard library is both deep and wide. Outside of libraries for web (and possibly devops), Ruby really can't compete in terms of library support.

https://www.nicholashairs.com/posts/major-changes-between-python-versions/

https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/

https://blog.jetbrains.com/pycharm/2024/12/the-state-of-python/



## 2026.2.10

### 学习材料

[The Car That Would Not Stop](https://levelup.gitconnected.com/the-car-that-would-not-stop-f9eea9d35ae0)

https://datawhalechina.github.io/hello-agents/

https://blog.algomaster.io/p/scaling-a-system-from-0-to-10-million-users



## 2026.2.27

### 学习材料

1. 如果要学 css https://frontendmasters.com/blog/what-you-need-to-know-about-modern-css-2025-edition/
2. https://allenpike.com/2026/a-broken-heart/
3. https://www.clientserver.dev/p/war-story-the-hardest-bug-i-ever 绝对值的实现 bug
4. https://claude.com/blog/using-claude-md-files
5. https://www.newyorker.com/culture/rabbit-holes/the-uncanny-failures-of-ai-generated-hands
6. https://nodesource.com/blog/worker-threads-nodejs-multithreading-in-javascript



学习智能体

https://datawhalechina.github.io/
