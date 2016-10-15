# Dispider

Based on elastic search

## 架构

![Dispider架构图.png](http://ww4.sinaimg.cn/large/72f96cbajw1f79aarhc4yj218s0tsmyx.jpg)

### Web Controller

- Project 信息创建与配置
- 支持 Nginx 负载均衡
- 支持 HTTP CALLBACK
- 支持监控任务
- 下发调度

### Spider


#### Scheduler ( Django Server )

- Redis 存储 links base
- URL 管理

#### Fetcher

- 下载 (&&渲染) html

#### Processor

- 处理 html
- 将新链 CALLBACK 回 Server , 等待新一轮调度
- 调用 Pipeline 持久化结果

#### Pipeline

- 持久化到数据库(elastic search)
