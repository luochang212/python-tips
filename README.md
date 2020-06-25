# python-tips

本文是博客[《我的Python不可能这么麻烦》](https://luochang212.github.io/posts/python_tips/)的代码示例。这篇博客前后更新了5个月，陪伴我从实习到正式工作，写到现在也告一段落了。本文主要介绍 Python 的异常处理、装饰器、画图库等基础知识，也包含少量的工程实践。

## 语言基础

- [列表](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/list.ipynb)

    - 创建
    - 获取
    - 修改
    - 添加
    - 插入
    - 删除
    - 排序
    - 逆序
    - 索引
    - 循环
    - 列表推导
    - 切片
    - 复制
    - 去重
    - 计数
    - 查找

- [字典](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/dict.ipynb)

    - 创建
    - 获取
    - 更新
    - 遍历
    - 排序
    - 删除
    - 字典与JSON
    - collections.defaultdict()
    - setdefault()

- [字符串](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/str.ipynb)

    - 基本操作
    - 格式化
    - 字符串方法

- [函数](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/func.ipynb)

    - 形参和实参
    - 位置实参
    - 关键字实参
    - 默认值
    - 位置实参和关键字实参的混用
    - 默认值、位置实参和关键字实参的混用
    - 传递任意数量的位置实参
    - 传递任意数量的关键字实参
    - 由字符串函数名生成可调用的函数

- [异常](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/exception.ipynb)

    - 引发异常
    - 捕捉异常
    - 捕捉多种异常
    - 捕捉所有异常
    - 输出异常
    - 使用 else
    - 手动触发异常
    - 使用 finally

- [闭包](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/closures.ipynb)

- [生成器](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/iter.ipynb)

    - 可迭代对象
    - 可迭代对象与迭代器的对比
    - 典型的迭代器
    - Sentence 类第3版: 生成器函数
    - Sentence 类第4版: 惰性实现
    - Sentence类第5版: 生成器表达式
    - 等差数列生成器
    - 标准库中的生成器函数
    - Python 3.3 中新出现的句法: yield from
    - 可迭代的归约函数
    - 深入分析iter函数

- [装饰器](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/decorator.ipynb)

    - 装饰器基础
    - 一个小练习
    - 使用 *args 和 **kwargs
    - 高阶装饰器
    - @functools.lru_cache()

- [内置函数](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/builtInFunction.ipynb)

## 常用库

- [NumPy](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/numpy.ipynb)

    - ndarray
    - 通用函数
    - 数组文件
    - 线性代数

- [pandas](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/pandas.ipynb)

    - 基本数据类型
    - 基本功能
    - 统计描述
    - 缺失数据
    - 层次化索引
    - 整数索引
    - 合并

- [datetime](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/datetime.ipynb)

    - timedelta 对象
    - date 对象
    - datetime 对象
    - time 对象
    - tzinfo 对象
    - timezone 对象

## 玩转 Python

- [画图](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/plot.ipynb)
  
    - Matplotlib
    - Seaborn
    - 自适应的时间轴
    - 动态更新

- [读写 CSV](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/csv.ipynb)

    - 读取 CSV 文件
    - 用 DataFrame 展示数据
    - 处理数据
    - 导出数据到 CSV 文件
    - 用 pandas 读 CSV 文件
    - 用 pandas 随机读取 CSV 文件

- [词云](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/wordCloud.ipynb)

    - 最简单的词云
    - 几何形状的词云
    - 以 png 图片作遮罩的词云
    - 中文词云

- [图像处理](https://nbviewer.jupyter.org/github/luochang212/python-tips/blob/master/image.ipynb)

    - PIL
    - Matplotlib
    - Numpy
    - SciPy
    - GIF图像处理
