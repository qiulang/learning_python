### AES 加密示例

使用 [crypto-js](https://www.npmjs.com/package/crypto-js)

代码示例

```javascript
var CryptoJS = require("crypto-js");
 
// Encrypt
var ciphertext = CryptoJS.AES.encrypt('my message', 'secret key 123').toString();
// 输入字符串的会被用作 passphrase,生成 256 bits 的实际key
// ciphertext.key 是根据输入passphrase实际生成的 key
// 参见 https://stackoverflow.com/questions/22875419/cryptojs-how-to-generate-aes-passphrase
 
// Decrypt
var bytes  = CryptoJS.AES.decrypt(ciphertext, 'secret key 123');
var originalText = bytes.toString(CryptoJS.enc.Utf8);
 
console.log(originalText); // 'my message'


```



和目前服务器算出来不一致 应该是因为这个处理造成

```java
SecureRandom secureRandom = SecureRandom.getInstance("SHA1PRNG");
```

java实现可以参照 https://blog.csdn.net/max229max/article/details/87639613

我们需要找到对应js实现'SHA1PRNG' 

`02adc2368daf44c1864b721cc684fb7f` 转换对应的 16 byte s数组 `[59, 106, 116, 80, -17, 27, -41, -39, -73, -102, 84, -33, 114, -117, -84, 124]`



AES 资料

[AES-GCM 加密简介](https://juejin.im/post/6844904122676690951)

[最佳安全实战：在 Java 和 Android 里用 AES 进行对称加密](https://cloud.tencent.com/developer/article/1161339)

[PKCS5Padding vs PKCS7Padding](https://stackoverflow.com/questions/20770072/aes-cbc-pkcs5padding-vs-aes-cbc-pkcs7padding-with-256-key-size-performance-java) 和 [What is the difference between PKCS#5 padding and PKCS#7 padding](https://crypto.stackexchange.com/questions/9043/what-is-the-difference-between-pkcs5-padding-and-pkcs7-padding) 就是一样

这个问题跟我们的类似 [What are the AES parameters used and steps performed internally by crypto-js while encrypting a message with a password?](https://stackoverflow.com/questions/27220297/what-are-the-aes-parameters-used-and-steps-performed-internally-by-crypto-js-whi) 和 [CryptoJS AES-128-ECB and PHP openssl_encrypt don't match](https://stackoverflow.com/questions/53894466/cryptojs-aes-128-ecb-and-php-openssl-encrypt-dont-match)

同样有人问 [what is the default AES config](https://github.com/brix/crypto-js/issues/122) 没有回答！

ECB & Salt [Surely No-one Uses ECB Mode in AES?](https://medium.com/asecuritysite-when-bob-met-alice/surely-no-one-uses-ecb-mode-in-aes-332ed90f29d0)

ECB mode 不用 iv [Is it possible to use AES with an IV in ECB mode?](https://stackoverflow.com/questions/1789709/is-it-possible-to-use-aes-with-an-iv-in-ecb-mode)

从 这个 [使用crypto-js进行128位AES/ECB/PKCS7Padding加密/解密](https://segmentfault.com/a/1190000011041123) 和 https://lijinya.xyz/qian-hou-duan-aesjia-jie-mi/ 受到一点启动

### 几个问题

encrypt 缺省设置

为什么java的 SHA1PRNG 对应 `CryptoJS.SHA1(CryptoJS.SHA1(key)).toString().substring(0, 32)`  这个 https://github.com/bombworm/SHA1PRNG 不可用

 [Can't decrypt using CryptoJS (works in Java, Python)](https://stackoverflow.com/questions/36185680/cant-decrypt-using-cryptojs-works-in-java-python)

URLSafeString 对应实现？



### SHA1PRNG

 [Use of “SHA1PRNG” in SecureRandom Class](https://stackoverflow.com/questions/12726434/use-of-sha1prng-in-securerandom-class)

> `"SHA1PRNG"` is the name of a pseudo random number generator (the PRNG in the name). That means that it uses the SHA1 hash function to generate a stream of random numbers. SHA1PRNG is a proprietary mechanism introduced by Sun at the time.
>
> ...
>
> The SHA1 hash function is to create the output of the RNG and to hash the seed information before it is used in the PRNG. 
>
> PRNG's are deterministic. That means that they will always generate the same stream of random numbers from the same input material (the "seed"). ... Note that implementations of SHA1PRNG may differ among JCA providers / different runtimes. The code on Android particularly is different and less stable than the SUN SHA1PRNG. 

 [SecureRandom with NativePRNG vs SHA1PRNG](https://stackoverflow.com/questions/27622625/securerandom-with-nativeprng-vs-sha1prng)  

> `"SHA1PRNG"` uses a hash function and a counter, together with a seed. The algorithm is relatively simple, but it hasn't been described well. Beware that `"SHA1PRNG"` is **not** an implementation requirement for Java SE. On most runtimes it will be present, but directly referencing it from code will make your code less portable.
>
> ...
>
> As a general warning I strongly advice against using the random number generator for anything other than random number generation. Even if you can seed it yourself and even if you choose Sun's SHA1PRNG, *don't count on being able to extract the same sequence of random numbers from the random number generator*. So do **not** use it for key derivation from passwords, to name one example. 就是现在众安的java实现

[Better way to create AES keys than seeding SecureRandom](https://stackoverflow.com/questions/24124091/better-way-to-create-aes-keys-than-seeding-securerandom)

> No, the whole idea that you should use a `SecureRandom` for key derivation from static data is rather bad:
>
> 1. `SecureRandom`'s main function is to generate random values, it should not be used as a generator for a key stream;
> 2. `SecureRandom`, when instantiated with `"SHA1PRNG"` does not implement a well defined algorithm, and the algorithm has actually be known to change, even from one Sun JDK to another;
> 3. The Oracle provided implementation of `"SHA1PRNG"` uses the initial seed as *only* seed, others may just *add* the seed to the random pool.
>
> Using `"SHA1PRNG"` as key derivation function has been known to produce issues on several versions of Android, and may fail on any other Java RE.