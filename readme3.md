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

