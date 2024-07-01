## 2024 

2023 遗留不少事

1. 吴恩达的课 看到 61课就停了  ， 2023 年11月7号
1. 如何生产自己的pip包， 2023 年 10月 18号就停了
1. 继续使用各种模型，总结
   1.  https://start.chatgot.io/ 集合几个常见
   1.  https://www.chatpdf.com/
   1.  Moonshot AI  https://moonshot.feishu.cn/docx/RnkWdeFo8oQabzxYFVwcNg1Mn9g
   1.  清华智普 、 通义千问





### 1.29

### 发布自己的包

发布 pip 包 ，之前检索到的两篇没啥用的文章。 2023 10.18 号找的几篇文章也没有什么印象了。

1. https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
2. https://mathspp.com/blog/how-to-create-a-python-package-in-2022

重新 google  how to publish pip package 排名前几名文章，build 工具用最常见的 `setuptools`

1. https://builtin.com/data-science/how-to-publish-python-code-pypi 简单也比较清晰，但没有实际例子
1. https://www.turing.com/kb/how-to-create-pypi-packages `python setup.py sdist` 和 `setup.py`解释 参见 https://docs.python.org/3.10/distutils/introduction.html#distutils-simple-example 但这篇提到 `init.py`是不是必现？ 它也没提 `__init__.py`
1. 重读去年 第一篇 https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/

另：[Difference between Module and Class in Python](https://stackoverflow.com/questions/43183244/difference-between-module-and-class-in-python)



## 1.31

### attention

Bard 推荐

1. [Visualizing A Neural Machine Translation Model (Mechanics of Seq2seq Models With Attention)](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)
2. https://jalammar.github.io/illustrated-transformer/



最新的书要读  https://udlbook.github.io/udlbook/



## 2.28

udl 看到第三章  shallow neural networks， 图 3.8 visualise a linear function of the two inputs 没彻底理解，接着看第四章

https://docs.wandb.ai/tutorials   Weights & Biases (W&B) is the AI developer platform, with tools for training models, fine-tuning models, and leveraging foundation models.

https://docs.wandb.ai/guides 试试



https://nlp.seas.harvard.edu/annotated-transformer/  要读还要试验，但是之前把transformer 再了解清楚

https://jalammar.github.io/illustrated-transformer/



## 3.12

### Requests 

https://realpython.com/python-requests/ 写代码用到又复习一下

[A Review: Pipenv vs. Poetry vs. PDM](https://dev.to/frostming/a-review-pipenv-vs-poetry-vs-pdm-39b4) 三个工具都能指定 python 版本

udl 看到第五章 Loss functions



## 3.19

### RAG

RAG & LangChain

[Advanced RAG Techniques: an Illustrated Overview](https://pub.towardsai.net/advanced-rag-techniques-an-illustrated-overview-04d193d8fec6) **在看**

[How to Improve LLMs with RAG](https://towardsdatascience.com/how-to-improve-llms-with-rag-abdc132f76ac)



### Transformer 学习材料

两篇简介

1. [Understanding Transformers and Attention](https://medium.com/@stefanbschneider/understanding-attention-and-transformers-d84b016cd352) 2023写的，标注7分钟读完。模型是简述了，但我也陆陆续续从别的地方知道了，现在是进一步深入了解，所以还要看别的

2. [Transformers: A Beginner’s Guide](https://medium.com/@nikitamalviya/transformers-a-beginners-guide-194a8ad70c4a) 作为入门介绍，这篇比上篇好

[Ketan Doshi](https://ketanhdoshi.medium.com/?source=post_page-----95a6dd460452--------------------------------) 系列

1. [Transformers Explained Visually (Part 1): Overview of Functionality](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452)

2. [Transformers Explained Visually (Part 2): How it works, step-by-step](https://towardsdatascience.com/transformers-explained-visually-part-2-how-it-works-step-by-step-b49fa4a64f34) **快看** mask 哪里没细看

3. [Transformers Explained Visually (Part 3): Multi-head Attention, deep dive](https://towardsdatascience.com/transformers-explained-visually-part-3-multi-head-attention-deep-dive-1c1ff1024853)  **Reshaping the Q, K, and V matrices** 没有理解好

4. [Transformers Explained Visually — Not Just How, but Why They Work So Well](https://towardsdatascience.com/transformers-explained-visually-not-just-how-but-why-they-work-so-well-d840bd61a9d3) 2021写的， **4.3 看完，较好理解**

[XQ](https://medium.com/@xq-is-here) 系列 有实际python 例子更容易理解

1. [Explained: Transformers for Everyone](https://medium.com/the-research-nest/explained-transformers-for-everyone-af01cbe600c5) 2024，15分钟 

2. [Explained: Tokens and Embeddings in LLMs](https://medium.com/the-research-nest/explained-tokens-and-embeddings-in-llms-69a16ba5db33) 读完，对 embedding 有一定了解

3. [Explained: Attention Mechanism in AI](https://medium.com/the-research-nest/explained-attention-mechanism-in-ai-e9bb6f0b0b4d) 代码用 notebook 试验 https://hex.tech/blog/beginners-guide-to-python-notebooks/  **4,1阅读完** 觉得有些概念没解释好，给他留言

4. [Explained: Hyperparameters in Deep Learning](https://medium.com/the-research-nest/explained-hyperparameters-in-deep-learning-9b1e0f3b9029) 4.1 读完，留言 loss function 到底怎么体现在transformer里？



**4.3 读完以上10篇** 和 https://opencv.org/blog/pytorch-vs-tensorflow/

-------

4.7 看完以下

[An Intuitive Explanation of ‘Attention Is All You Need’: The Paper That Revolutionized AI and Created Generative AI like ChatGPT](https://drlee.io/an-intuitive-explanation-of-attention-is-all-you-need-the-paper-that-revolutionized-ai-and-39aac5827411) 2023 9 分钟 看完，没什么有用的

[Understanding the Transformer Architecture in Simple English](https://medium.com/codex/understanding-the-transformer-architecture-in-simple-english-8ee30770a1e0) 2024, 8分钟 这篇比上一篇解释更清楚，作为入门了解。

[Self-Attention: A step-by-step guide to calculating the context vector](https://medium.com/@lovelyndavid/self-attention-a-step-by-step-guide-to-calculating-the-context-vector-3d4622600aac) 2023 7分钟 先看了，因为对vector 有点兴趣，但是浑沦吞枣，对理解好像没有太大帮助


[Mika.i Chak](https://medium.com/@m_chak?source=post_page-----9b46f4178b23--------------------------------) 系列8篇 还不错，短小精炼

[Transformers — In Plaintext. Part 1](https://medium.com/@m_chak/transformers-in-plaintext-part-1-4bb081135f0d) 乍一看好像还可以

[Transformers — Unknown Hero. Part 2](https://medium.com/@m_chak/transformers-unknown-hero-part-2-be2ac7afc640) 

[Transformers — In Deep Dive. Part 3](https://medium.com/@m_chak/transformers-in-deep-dive-part-3-c6fd1113f4c4)

[Transformers — does not exist without Input Processing. Part 4](https://medium.com/@m_chak/transformers-does-not-exist-without-input-processing-part-4-9b46f4178b23) 位置编码用sin/cos,解释 对于浮点数，sin/cos表示更有效

[Transformers — Is All About Attention. Part 5](https://medium.com/@m_chak/transformers-is-all-about-attention-part-5-d57cae854964) QKV 计算过程图形呈现

[Transformers — Multi-Head Attention. Part 6](https://medium.com/@m_chak/transformers-multi-head-attention-part-6-132624292959) 

[Transformers — Masked Multi-Head Attention. Part 7](https://medium.com/@m_chak/transformers-masked-multi-head-attention-part-7-5ac24517b355) 

[Transformers — Feed Forward and Output. Part 8](https://medium.com/@m_chak/transformers-feed-forward-and-output-part-8-1f959b9eca1e) 想到一个问题，整个过程怎么没看到loss function 的应用？

[The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)  读完 ， 2018年写的，但任然是信息量最全的


------

4.8 开始

[What are Query, Key, and Value in the Transformer Architecture and Why Are They Used?](https://towardsdatascience.com/what-are-query-key-and-value-in-the-transformer-architecture-and-why-are-they-used-acbe73f731f2) 2023,10分钟  **4.8 开始读**

[The Math Behind Neural Networks](https://towardsdatascience.com/the-math-behind-neural-networks-a34a51b93873) 长

[Jay Alammar](https://jalammar.github.io/) 系列

1. [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)  **读完**
2. [Visualizing A Neural Machine Translation Model (Mechanics of Seq2seq Models With Attention)](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/) 2018
3. https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/ 2018

[Roadmap to Learn AI in 2024](https://medium.com/bitgrit-data-science-publication/a-roadmap-to-learn-ai-in-2024-cc30c6aa6e16)

2.28记录的 https://nlp.seas.harvard.edu/annotated-transformer/   一定最后要试验，读完！！代码 https://github.com/harvardnlp/annotated-transformer/


[Why ChatGPT Uses Decoder-Only](https://medium.com/@row3no6/why-chatgpt-uses-decoder-only-eaf0223143e6) 

[ChatGPT's Architecture - Decoder Only? Or Encoder-Decoder?](https://datascience.stackexchange.com/questions/118260/chatgpts-architecture-decoder-only-or-encoder-decoder)


微信公众号各种文章

小插曲，被python list遍历坑了一下 [How slicing in Python works](https://stackoverflow.com/questions/509211/how-slicing-in-python-works) 比如 `::-1, ::2, for i in range(0, len(parts), 2)` 像 [Understanding string reversal via slicing](https://stackoverflow.com/questions/766141/understanding-string-reversal-via-slicing) 这里说的 You can omit one or more of the elements and it does "**the right thing**"

还有一个小教训要记牢：遍历数组元素的时候，如果一次要处理**一个以上元素**就不能用 `for in` 而是要index，而且 `for i in range `中 i 不会变，要让i变化，或者设置step(如果step固定,，比如 `for i in range(0, len(parts), 2)`)，或者就用 while 自己加 i 的step=



```
# 没有更简单的写法吗？
weighted_embeddings = {word: [weight * val for val in embedding]
                       for word, embedding in word_embeddings.items()
                       for word_weight, weight in attention_weights.items() if word == word_weight}
# 比如下面
weighted_embeddings = {word: [v * attention_weights[word] for v in word_embeddings[word]] 
                        for word in word_embeddings}
```



## 4.8 

### 位置编码实现

找到一个中文讲解  [Transformer 详解](https://wmathor.com/index.php/archives/1438/) 加代码学习, 

https://www.zhihu.com/question/347678607  位置编码

[Transformer 中的 Positional Encoding](https://wmathor.com/index.php/archives/1453/)

[Master Positional Encoding: Part I](https://towardsdatascience.com/master-positional-encoding-part-i-63c05d90a0c3)

### AI tools

[What's the difference between Cursor and the new version of Github Copilot?](https://github.com/getcursor/cursor/issues/1123)

[How to maximise the Copilot's context awareness?](https://github.com/orgs/community/discussions/51323)

尝试 https://codeium.com/ 老是报错，先放弃



## 4.16

### transformer cont.

[What are Query, Key, and Value in the Transformer Architecture and Why Are They Used?](https://towardsdatascience.com/what-are-query-key-and-value-in-the-transformer-architecture-and-why-are-they-used-acbe73f731f2) 读完，还是觉得v 矩阵多余，结果发现 [Simplified Transformer Block Architecture: Insights and Impact](https://www.e2enetworks.com/blog/simplified-transformer-block-architecture-insights-and-impact) 也说简化努力包括去掉 v 矩阵

[Transformer Architecture Simplified](https://medium.com/@tech-gumptions/transformer-architecture-simplified-3fb501d461c8) 本来以为是如何简化transformer，但其实简介

读完 [Chen Margalit](https://medium.com/@chenmargalit) 系列 没有太多新东西了

1. [Simplifying Transformers: State of the Art NLP Using Words You Understand — part 3— Attention](https://towardsdatascience.com/transformers-part-3-attention-7b95881714df) 有代码，读完！
2. [Simplifying Transformers: State of the Art NLP Using Words You Understand — part 2— Input](https://medium.com/towards-data-science/transformers-part-2-input-2a8c3a141c7d) 相关内容看过很多，快读
3. [Simplifying Transformers: State of the Art NLP Using Words You Understand — Part 4 — Feed-Forward- Layer](https://medium.com/towards-data-science/simplifying-transformers-state-of-the-art-nlp-using-words-you-understand-part-4-feed-foward-264bfee06d9)
4. [Simplifying Transformers: State of the Art NLP Using Words You Understand — Part 5 — Decoder and Final Output](https://towardsdatascience.com/simplifying-transformers-state-of-the-art-nlp-using-words-you-understand-part-5-decoder-and-cd2810c6ad40)

[What Is ChatGPT Doing … and Why Does It Work?](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/) 看完

[The Math Behind Neural Networks](https://towardsdatascience.com/the-math-behind-neural-networks-a34a51b93873)  草草读完，主要难点还是backpropagation，在 Grokking DP 看过，之前看到Chapter 12，这会在复习一下它关于 word embedding 的描述

还是回到 udl  接着从从第五章 loss function 但马上想到NLP的loss 要怎么算，会选哪些loss function



## 4.22

### loss function in NLP

读 [Cross Entropy in Large Language Models (LLMs)](https://medium.com/ai-assimilating-intelligence/cross-entropy-in-large-language-models-llms-4f1c842b5fca)

学习 langchain https://github.com/liaokongVFX/LangChain-Chinese-Getting-Started-Guide

[LangChain Agents: Unleashing the Power of Language Models for Real-World Automation](https://medium.com/@vinusebastianthomas/langchain-agents-unleashing-the-power-of-language-models-for-real-world-automation-d4a75845717f)





## 6.4

### LangChain && RAG

[Building a Document-based Question Answering System with LangChain using LLM model](https://medium.com/@nageshmashette32/building-a-document-based-question-answering-system-with-langchain-using-llm-model-fb22e47a965c)

[AI Chatbot with your Knowledge base](https://medium.com/databutton/ai-chatbot-with-your-knowledge-base-0390c8c6e5d8)

[Building Next-Gen Apps with AI Agents](https://medium.com/databutton/building-next-gen-apps-with-ai-agents-f18551c71218)

https://www.promptingguide.ai/research/llm-agents

[Intro to LLM Agents with LangChain: Beyond Simple Prompts](https://medium.com/@siladityaghosh/intro-to-llm-agents-with-langchain-beyond-simple-prompts-4ee1edd00225) 代码跑不过，从头开始看 https://python.langchain.com/v0.2/docs/introduction/

No good (or at all) reStructuredText editor   https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

https://github.com/liaokongVFX/LangChain-Chinese-Getting-Started-Guide

[How to Improve LLMs with RAG](https://towardsdatascience.com/how-to-improve-llms-with-rag-abdc132f76ac)

[What is an LLM Agent and how does it work?](https://medium.com/@aydinKerem/what-is-an-llm-agent-and-how-does-it-work-1d4d9e4381ca)

跑了第一个例子  [Build a Simple LLM Application with LCEL](https://python.langchain.com/v0.2/docs/tutorials/llm_chain/) 碰到问题是如何看 LangSmith trace
