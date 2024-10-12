在使用 Sentence Transformer (sbert)的过程中我一直有这几个问题：

1. sbert 到底做了什么，使得它在句子嵌入（sentence embeddings）方面遥遥领先？
2. 除了 sbert，句子嵌入方法还有别的选择吗？尤其是中文句子的嵌入还有别的选择吗？
3. sbert 和实际使用的预训练模型是什么关系，为什么有那多预训练模型都通过 sbert加载。

我尝试在 SO 提问 “[What does SentenceTransformers provide to simplify sentence embedding?](https://stackoverflow.com/questions/79022351/what-does-sentencetransformers-provide-to-simplify-sentence-embedding)” 也没有人回复。随便说一句话，ML相关问题SO似乎还不是合适Q&A论坛，但我又没有找到哪里可以更合适发问。

我自己测试发现智源的“BAAI/bge-base-zh-v1.5" 模型对中文句子的文本嵌入表现最好，超过了 [sbert 提到的各种多语言模型](https://sbert.net/docs/sentence_transformer/pretrained_models.html#multilingual-models)。可是它不是用sentence bert 模型训练的，为什么可以用 Sentence Transformer 来加载？

在比较试用另一个中文RAG框架 [MaxKB](https://github.com/1Panel-dev/MaxKB) 我发现它用了另一个句子嵌入库[text2vec](https://github.com/shibing624/text2vec). text2vec 介绍了四种文本向量表示模型（他说的**文本向量**就是句子向量），包括sbert，text2vec 用其中的 [Cosine Sentence](https://github.com/shibing624/text2vec/blob/master/text2vec/cosent_model.py) 训练，自称比 sentence bert模型效果好，但是它也能通过 sbert加载。

如果进一步点开sbert 预训练模型在 hugging face的说明，以最常见的 [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) 为例，它们居然都提到模型既可以通过 Sentence-Transformers 加载，也可以不通过 Sentence-Transformers 直接用 HuggingFace Transformers 加载：

Without [sentence-transformers](https://www.sbert.net/), you can use the model like this: First, you pass your input through the transformer model, then you have to apply the right pooling-operation on-top of the contextualized word embeddings.

而且不用 sbert加载时候给的示例代码都一样，都需要通过 `mean_pooling 函数得到句子嵌入。这个mean_pooling到底做了什么？`

HuggingFace 还有一篇介绍embedding的入门文章[ Getting Started With Embeddings](https://huggingface.co/blog/getting-started-with-embeddings) 简单解释了嵌入，句子相似度（这些我都明白），但没能帮我理解我的三个疑问。不过在寻找答案的过程中我突然意识到一点：我们有很多种方法得到**词嵌入**，包括在transformer出现前的 Word2vec 和 doc2vec, 但是如何从词嵌入(word embedding) 得到句子嵌入(sentence embedding)？总不能把一个句子中的每一个词的词嵌入向量多叠加吧！

仔细翻看 text2vec 项目的文章，注意到 [文本向量表示方法](https://github.com/shibing624/text2vec/wiki/文本向量表示方法) 这篇短文，发现以下的话印证我的初步理解（如何从词向量得到句子向量），“*当通过平均词向量的方式计算句向量”*:

- BERT自身导出的句向量（不经过Fine-tune，**对所有词向量求平均**）质量较低，甚至比不上Glove的结果，因而难以反映出两个句子的语义相似度

> *主要原因是：*
>
> *1.BERT对所有的句子都倾向于编码到一个较小的空间区域内，这使得大多数的句子对都具有较高的相似度分数，即使是那些语义上完全无关的句子对。*
>
> *2.BERT句向量表示的聚集现象和句子中的高频词有关。具体来说，当通过平均词向量的方式计算句向量时，那些高频词的词向量将会主导句向量，使之难以体现其原本的语义。当计算句向量时去除若干高频词时，聚集现象可以在一定程度上得到缓解，但表征能力会下降。*

所以我抱着试试看的想法给 [sbert开了一个问题单](https://github.com/UKPLab/sentence-transformers/issues/2958)，询问 sbert到底做了什么，为什么这么多模型都可以通过sbert加载；而不用sbert加载直接用 hugging face transfomer计算句子的嵌入向量，为什么它们的代码都是类似的。没想到很快就得到答复，答复印证了我的思考，we use a pooling strategy to go **from token embeddings -> text embeddings**. Sentence Transformers just abstracts away this conversion.

为什么不用Sentence Transformers训练的模型也能通过 Sentence Transformers加载：

models not trained with Sentence Transformers, like the BGE models, can still be adapted to work in Sentence Transformers as long as the model 1) can be loaded with AutoModel and 2) produces token embeddings.

…

In short: Sentence Transformers is a wrapper around Transformers that 1) abstracts away common embedding model functionality such as pooling and normalization for easy 3-line usage (import; load; encode) and 2) implements a whole range of finetuning functionality that can help you get the best model on exactly your data.

答复还建议我要读读[sbert的论文](https://arxiv.org/pdf/1908.10084)，才能更清楚的了解它的原理，这是我一直逃避的事😂，觉得这把年纪读paper实在吃力了，不过既然他这么说，好歹把摘要看了 （看完就发现，不少中文文章在解释sbert就从摘要里摘出这两句）：“ 使用BERT在10,000个句子的集合中找到最相似的一对，需要大约5000万次推理计算（~65小时）。BERT的构造使其不适合语义相似性搜索以及聚类等无监督任务。我们介绍了 Sentence-BERT （SBERT），这是预训练 BERT 网络的修改版，将查找最相似对的工作量从 BERT / RoBERTa 的 65 小时减少到使用 SBERT 的约 5 秒，同时保持 BERT 的准确性。”

文章还解释计算句子迁入经常会碰到到几个术语，不如 mean pooling, CLS-token (我没看懂，贴在这里警示自己要努力)，但终于知道 **池化策略** 原来就是 **pooling strategy**

When trained with the regression objective function, we observe that the **pooling strategy** has a large impact. There, the MAX strategy perform significantly worse than MEAN or CLS-token strategy. This is in contrast to Conneau et al. ([2017](https://ar5iv.labs.arxiv.org/html/1908.10084?_immersive_translate_auto_translate=1#bib.bib10)), who found it beneficial for the BiLSTM-layer of InferSent to use MAX instead of MEAN pooling.

知道这些关键词我又进一步搜到这篇文章 [Sentence Embeddings. Introduction to Sentence Embeddings](https://osanseviero.github.io/hackerllama/blog/posts/sentence_embeddings/) 是我目前找到的关于句子迁入最全解释文章，但如果没有之前的背景知识，读起来也会不少困难。文章有一个章节专门解释了这些策略从词向量得到句子向量: `[CLS]` pooling, max pooling and mean pooling.

CLS token需要专门提一下，在BERT模型中，每个输入文本在被送入模型前会增加一个特殊的标记（token），即CLS（classification）标记。这个CLS标记放在输入序列的开头，其目的是为了在模型处理完输入文本后，能够从这个特定的标记上获得整个输入文本的表示。 [What is purpose of the [CLS\] token and why is its encoding output important?](https://datascience.stackexchange.com/questions/66207/what-is-purpose-of-the-cls-token-and-why-is-its-encoding-output-important) 我当然也是一知半解

在我的这段学习过程中，我也找到英文句子嵌入另外两个选择，参考 [Top 4 Sentence Embedding Techniques using Python](https://www.analyticsvidhya.com/blog/2020/08/top-4-sentence-embedding-techniques-using-python/)

1. facebook 的 InferSent ， 基于 [(Stanford Natural Language Inference) dataset](https://nlp.stanford.edu/projects/snli/) 但是这个项目还是关停，应该用的人不多，而且这个数据集应该不适合中文
2. google的 Universal Sentence Encoder， 用的人可能也不多，是 sbert 的问题单 [what’s the difference between USE and then SBERT?](https://github.com/UKPLab/sentence-transformers/issues/64) 简单答复 SBERT works much better

这就是我目前学习 sentence embedding 的总结心得。

