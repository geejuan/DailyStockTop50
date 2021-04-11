# DailyStockTop50
![](https://img.shields.io/badge/Python-3.x-blue) ![](https://img.shields.io/badge/license-MIT-green)
![](https://img.shields.io/badge/%E5%8F%8D%E9%A6%88-geejuanxu%40gmail.com-red)

> 本项目为一时兴起而写，主要目的是检验近期学习成果，欢迎一切意见和指正。
* 本项目运行在python环境下
* [Python 3.9 Win版 官网下载地址](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe) 
* 默认你会安装和使用python，详细方法可自行搜索😝

## 实现了什么？

* 爬取每日A股资金流入Top50的个股数据
* 包括'代码', '名称', '最新价', '今日涨跌幅', '今日主力净流入', '今日主力占比', '今日超大单净流入', '今日超大单占比', '今日大单净流入', '今日大单占比','今日中单净流入', '今日中单占比', '今日小单净流入', '今日小单占比'
* 数据会被整理后写入以日期命名的csv文件中

![](https://github.com/geejuan/DailyStockTop50/blob/main/img/Screenshot%202021-04-11%20at%2011.52.18%20PM.png)

## 使用指南

**目录：**
* [0. 目录结构介绍](#menu)
* [1. 下载&安装](#f1)
* [2. 配置](#f2)
* [3. 开始使用](#f3)



### 目录介绍

```
├── README.md          使用说明，你当前看到的
├── config.ini         主要配置文件，需要修改这个
├── images             本文配图存放处
├── requirements.txt   Python依赖
└── stocktop50.py      入口文件，运行这个
```

### 下载&安装

```python
git clone https://github.com/geejuan/DailyStockTop50.git
cd DailyStockTop50
pip install -r requirements.txt
```


### 配置

编辑修改`config.ini`，按需填写字段即可
如何获得http请求头？ 请Google/Baidu/Bing
|必填| 配置项        | 代表含义 | 示例 |
|----| --------      | -----:   |-----:   | 
|✅| HEADER     |请求头信息 |Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3)…|

## 使用

执行`python stocktop50.py`即可完成一次爬取


## Release History 版本历史

* 0.0.1
    * Work in progress

## Authors 关于作者

* **Even** - *Initial work* - [Even](geejuanxu@gmail.com)

查看更多关于这个项目的贡献者，请阅读 [contributors](#) 

## License 授权协议

这个项目 MIT 协议， 请点击 [LICENSE.md](LICENSE.md) 了解更多细节。
