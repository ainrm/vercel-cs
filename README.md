## cobalt strike后台隐藏 - vercel



### 0x01 简介

这是一个cs后台隐藏项目，由[vercel官方模版](https://github.com/vercel/examples/tree/main/python/flask)改编而来，原理类似云函数，设置cs的上线地址为一个指定域名，该域名解析后的ip归属于`vercel`，从而实现真实ip隐藏

![ainrm@20230426182017](./tu/ainrm@20230426182017.webp)

### 0x02 部署

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?s=https://github.com/ainrm/vercel-cs&env=C2&repository-name=vercel-cs)


1. 创建vercel项目

![ainrm@20230505205915](./tu/ainrm@20230505205915.webp)

2. 绑定域名

![ainrm@20230505210549](./tu/ainrm@20230505210549.webp)

### 0x03 测试

1. 生成`https beacon`马

![ainrm@20230505211028](./tu/ainrm@20230505211028.webp)

2. dns请求，解析出cs服务器ip为[76.76.21.9](https://x.threatbook.com/v5/ip/76.76.21.9)

![ainrm@20230505211421](./tu/ainrm@20230505211421.webp)

3. 上线，执行命令

![ainrm@20230505211435](./tu/ainrm@20230505211435.webp)
