# 初识Python - For 循环
Python for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。

## for 循环语句（先看上一行字）
「说人话！」  
首先，for循环的一般格式如下：  
<pre id="description-code-editor" style="height: 70px;">
for &lt;variable&gt; in &lt;sequence&gt;:
    &lt;statements&gt;
else:  # if there isn't anything in sequence
    &lt;statements&gt;</pre>
<script>
window.dce1 = ace.edit("description-code-editor", {
    mode: "ace/mode/python",
    selectionStyle: "text",
    readOnly: true,
    fontSize: "15px",
    theme: "ace/theme/chrome"
})
</script>

## for ... in range()语句
`range(n)`是一个神奇的函数。当你输入1时，它会给你0；当你输入3时，它会返回`[0, 1, 2]`。  
即：输入n，返回0到n（不含n）的所有数。
`range(a, n)`也类似，不过是返回a（默认为0）到n（不含n）的所有数。
`range(a, n, step)`也类似，不过是返回a到n（不含n）的所有数，且步长为step（默认为1）。

利用这个函数，我们可以快速实现一段计次循环（如指定循环n次）。  
<pre id="description-code-editor2" style="height: 50px;">
for i in range(10):
    &lt;statements&gt;  # 此处的代码将会被执行10次
</pre>
<script>
window.dce2 = ace.edit("description-code-editor2", {
    mode: "ace/mode/python",
    selectionStyle: "text",
    readOnly: true,
    fontSize: "15px",
    theme: "ace/theme/chrome"
})
</script>

#### 如果你学过c/c++，也可以看看：
 - 上述代码等同于：  
<pre id="description-code-editor3" style="height: 130px;">
#include &lt;_mingw.h&gt;
using namespace std;
int main(int argc, const char* argv) {
    for (int i = 0; i &lt; 10; i ++) {
        &lt;statements&gt;  // 此处的代码将会被执行10次
    }
}
</pre>
<script>
window.dce3 = ace.edit("description-code-editor3", {
    mode: "ace/mode/c_cpp",
    selectionStyle: "text",
    readOnly: true,
    fontSize: "15px",
    theme: "ace/theme/chrome"
})
</script>

###### 是不是非常的简单呢？

## 任务目标
小明同学准备了一个数，认为这个数是个质数。但是旁边的小日月同学认为，这个数一定是个合数。请你帮<span title="想不到吧，我故意的">小明和小明同学</span>看看，这个数是不是质数？  

 - 任务有一定难度。  
 - 请不要使用多线程模块。（使用了会报错）  
 - 首先输入一个数，然后判断这个数是否为质数。如果这个数为质数则输出1，否则输出0  
