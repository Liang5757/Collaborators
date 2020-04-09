# 四则运算生成 (Python)

English

> **开发者**：[ZeongPaang](https://github.com/P4XL/) / [w1036933220](https://github.com/P4XL/Collaborators)

----

## 1.  实现功能

- 使用 -n 参数控制生成题目的个数
- 使用 -r 参数控制题目中数值的范围（自然数、真分数和真分数分母）
- 生成的题目中计算过程不能产生负数
- 生成的题目中如果存在形如e1÷ e2的子表达式，那么其结果应是真分数
- 每道题目中出现的运算符个数不超过3个
- 程序一次运行生成的题目不能重复
- 在生成题目的同时，计算出所有题目的答案，并存入执行程序的当前目录下的Answers.txt文件
- 程序应能支持一万道题目的生成.
- 程序支持对给定的题目文件和答案文件，判定答案中的对错并进行数量统计，输出到文件Grade.txt
- ~~用户图形界面~~

----
## 2.  使用用法

```
$ Python main.py [-args|-args]
```

> $ args
> ├─ -h --help	# 输出帮助信息
>    ├─ -n			  # 指定生成表达式数量，默认100
>    ├─ -r 			  # 指定生成表达式各个数字的取值范围，默认100
>    ├─ -a 			 # 需和-e参数共同使用进行批改，指定答案文件
>    └─ -e 			 # 需和-a参数共同使用进行批改，指定练习文件

例子 ：

> Generate 100 subjects whose domain is in range from 0 to 100
>
> 生成100道值域从0到100的四则运算
>
> ```python
> python -n 100 -r 100
> ```

> 检查答案，需要指定习题文件 以及 答案文件
>
> ```python
> python -e ./docs/Exercise.txt -a ./docs/Answer.txt
> ```

默认环境下，目录结果应该如下所示：

```
Collaborators/
│ .gitingore
│ main.py
├─utils
│  │  Arithmetic.py
│  │  Calculate.py
│  │  constant.py
│  │  Fraction.py
│  │  Generator.py
│  │  Generatorold.py
│  │  Operation.py
│  └─  paser.py
└─views
    │  config.json
    │  GUI.py
    └─ MainWindow.py
```

----

## 3.  Bugs

> 未完成用户图形界面
>

----

## 4.  Cnblog 链接 🚀

- **[四则运算生成命令行程序 (Python)](https://www.cnblogs.com/green--hand/p/12665616.html)**

> [作者 :  [张鹏](https://github.com/P4XL/) / [郑靓](https://www.cnblogs.com/green--hand/) ]
>
> [时间:  二零二零年,  四月九日, 星期四]


