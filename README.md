## zhangqy的博客
### 使用工具
本项目利用django + rest_framework实现，django保留了models（M），而views（C）和urls（C）则采用rest_framework，分发api之后，
将利用vuejs实现前端界面，从而达到前后端分离，分别进行开发的目的
### api说明
1. 分为文章列表、用户列表、类目列表、标签列表等，均以超链接形式展示，便于点击查看，提高api之间的聚合度
2. 为上传图片采用uuid重新命名，防止图片重名（虽然没什么卵用），以统一格式命名图片
### todos
1. 在admin后台增加markdown编辑功能
2. 图片防盗链
3. 部署到服务器
4. 增加博客评论、注册功能
### 部署到服务器
前端后端部署到同一台服务器，前端url正常访问，后端url形如www.mydomain.com/api/...，多了个api，访问之，得到后端发送的json格式的数据。
1. 后端利用Nginx+PostgreSQL+Gunicorn+Virtualenv+Supervisor配置，部署在digitalOcean主机上
2. 前端利用vuejs编写，Nginx部署