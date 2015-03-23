# 自我介绍 #

这是知乎日报数据同步脚本, 用于同步知乎日报的数据, 配合[zhihudaily](https://github.com/isayme/zhihudaily)可实现网页版[知乎日报](http://zhihudaily.isayme.org)~

知乎日报数据API信息来自[知乎日报 API 分析](https://github.com/izzyleung/ZhihuDailyPurify/wiki/知乎日报-API-分析)一文.

文章中分析的是第4版的API, 我实际使用的是第2版, 原因是第2版的API中提供的日报图片的分辨率是`640*640`, 而第四版的是`150*150`的.

另外, 同步下来的数据可选择是否上传到[七牛云存储](http://www.qiniu.com/).

# 如何使用 #
如果需要同步数据至[七牛云存储](http://www.qiniu.com/), 请先阅读[Python SDK 使用指南](http://developer.qiniu.com/docs/v6/sdk/python-sdk.html), 安装SDK并在[开发者自助平台](https://portal.qiniu.com/setting/key)获得`Access Key`, `Secret Key`以及`Bucket Name`后更新`qnu.py`中对应的变量.

如果不需要同步数据至[七牛云存储](http://www.qiniu.com/), 直接修改`util.py`中函数`download`参数`upload`的默认值为`False`.

`cron.py`用于每天定时同步知乎日报最新数据. Linux环境`crontab -e`命令可方便添加定时任务, 为防止被知乎判定为spam, 定时时间不要太短(我是15分钟).

`sync.py`用于同步知乎日报历史数据.

# 联系我 #

`e-mail` isaymeorg # gmail.com
