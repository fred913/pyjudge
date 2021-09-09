# 初识Python - 输入
You must know what "`if`" is in English. However, the same in Python has the same meaning.  

## 前情回顾
你还记得「思维导图」中的「输入、输出」吗？这回，我们将使用「输入」的函数「`input`」。  


## `input()`是什么？
`input(prompt)` 会从控制台读取一行字符串。  
`prompt` 参数（可选）可以使你在输入之前先输出一行文字，称为「提示符」。

#### 示例  
<pre id="description-code-editor" style="height: 50px;">
s = input("请输入：")
print("你输入了：", s)</pre>
我们输入123，则终端里显示：    
<pre>
请输入：123
你输入了： 123
</pre>
<script>
window.dce1 = ace.edit("description-code-editor", {
    mode: "ace/mode/python",
    selectionStyle: "text",
    readOnly: true,
    fontSize: "15px",
    theme: "ace/theme/chrome"
})

</script>

## 任务目标
 - 超级简单！   
 - 输入一行字，然后把这行字输出！
 - 不要有任何prompt（提示符）

