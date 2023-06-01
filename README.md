## cobalt strike后台隐藏 - vercel



### 0x01 简介

这是一个cs后台隐藏项目，由[vercel官方模版](https://github.com/vercel/examples/tree/main/python/flask)改编而来，原理类似云函数，设置cs的上线地址为一个指定域名，该域名解析后的ip归属于`vercel`，从而实现真实ip隐藏，相关的过程记录【[在此](https://ainrm.cn/2023/vercel.html)】

![ainrm@20230426182017](./tu/ainrm@20230426182017.webp)

### 0x02 部署

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?s=https://github.com/ainrm/vercel-cs&env=C2&repository-name=vercel-cs)
