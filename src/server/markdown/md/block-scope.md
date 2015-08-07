# 创建块作用域
## with
`见第二章读书笔记`
## try/catch
try/catch 会在 catch 中创建新的块作用域，例如

```javascript
// "use strict";

try {
	undefined();
} catch(error) {
	console.log(error);    // error 只存于 catch 创建的块作用域中
}

console.log(err);    // err 不存在在当前的全局作用域中，找不到 err 会抛出 ReferenceError
```
虽然这个行为在标准的 js 环境中是被允许的，但是对于一个作用域内的多个 catch ，有些语法检查器会提示警告的情况，那么可以把 catch 的 error 命名为 err1, err2, ...
## let 
`ES6 的新语法`
let 会在当前所在得块 { ... } 内创建块作用域，用法是在希望的块作用域上直接写上 {}
```javascript
var foo = true;

if (foo) {
	{    // 明显的块作用域
		let bar = foo * 2;
		bar = something(bar);
		console.log(bar);
	}
}

console.log(bar);    // ReferenceError
```
使用 let 我们就可以明确的声明块作用域了。
### let 的一些特性
1. let 不会在块作用域内产生变量提升
```javascript
{
	console.log(a);
	let a = 1;
}
```
2. 主动垃圾回收
{ let ... } 创建的块作用域能够在块作用域代码运行完后主动触发垃圾回收，而不会受闭包的影响。
```javascirpt
function process(data) {
	// do something interesting
}
var someReallyBigData = { ... };
process( someReallyBigData );    // 因为 click 的回调有一个全局的闭包，所以运行到这里不能回收 someReallyBigData

{    // 显式块作用域触发主动垃圾回收
	let var someReallyBigData = { ... };
	process( someReallyBigData );
}

var btn = document.getElementById("my_button");

btn.addEventListener("click", function click(evt) {
	console.log("button clicked");
},    /*capturingPhase=*/false );
```
3. let 的循环绑定
```
for (let i = 0; i < 10; i++) {
	console.log(i);    // 每次遍历都会重复绑定
}
// 和下面的代码是一致的
{
	let j;
	for (j=0; j<10; j++) {
		let i = j;    // 每次遍历都会重复绑定
		console.log( i );
	}
}
```
## const
`ES6 的新语法`
作用和 let 相似，但是 const 定义的是常量，而不是变量，不能在定以后进行值的修改
