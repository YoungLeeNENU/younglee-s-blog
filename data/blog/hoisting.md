# 变量提升
## 变量提升的基础
首先我们要知道，js 编译器对于变量定义和变量声明是分开进行的。声明和赋值要像编译器一样分开考虑，不能作为一个表达式处理。
而变量提升的意思是，和顺序执行代码不通，编译器会先处理作用域中的声明，后处理赋值。于是我们有

```javascript
a = 2;
var a;
console.log( a );
```

和

```javascript
var a;
a = 2;
console.log( a );
```

等价，打印 2 而不是 undefined。
又有

```javascript
console.log( a );
var a = 2;
```

和

```javascript
var a;
console.log( a );
a = 2;
```

等价，打印 undefined 而不是 2。

### 函数在变量提升中的次序
变量提升中，先提升函数，后提升变量。

```javascript
foo(); // 1
var foo;
function foo() {
	console.log( 1 );
}
foo = function() {
	console.log( 2 );
};
```

代码会打印 1 而不是打印 2。代码会按照下述的顺序执行

```javascript
function foo() {
	console.log( 1 );
}
foo(); // 1
foo = function() {
	console.log( 2 );
};
```

这里重复定义的 var foo; 被忽略掉了

## 关于重复用 var 定义的一个误区
我之前一直认为，对于变量声明和赋值，在编译器进行 LHS 声明变量之后，会去进行 RHS 对变量进行赋值，如果 RHS 有找到对应的值，那么变量赋值成功，否则赋值 undefined，如果是这样，那么下列代码会打印 2。

```javascript
foo(); // 3

function foo() {
	console.log( 1 );
}

var foo = function() {
	console.log( 2 );
};

function foo() {
	console.log( 3 );
}
```

实际情况是对于 var 的重复定义，编译器是会自定忽略重复的定义的。所以上述代码执行结果是 3。

## 在块作用域内提升 var 变量和函数变量的不同
在块作用域内，对于函数和 var 变量的提升是不同的，对于函数，会突破块作用域提升到块作用域之外的相邻作用域，而对于变量的提升，到块作用域顶端为止。这种在块作用域中定义函数的做法，是不推荐的。

```
foo();    // "b"

console.log(a);    // undefined

{
    a = true;
    
    var a;
    
    console.log(a);    // true
    
    if (a) {
        function foo() { console.log("a"); }
    }
    else {
        function foo() { console.log("b"); }
    }
}
```