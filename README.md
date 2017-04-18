## zhangqy的博客
### 使用工具
本项目利用django + rest_framework实现，django保留了models（M），而views（C）和urls（C）则采用rest_framework，分发api之后，
将利用vuejs实现前端界面。
### api说明
× 分为文章列表、用户列表、类目列表、标签列表等，均以超链接形式展示，便于点击查看，提高api之间的聚合度
× 为上传图片采用uuid重新命名，防止图片重名（虽然没什么卵用），以统一格式命名图片
## todos
× 在admin后台增加markdown编辑功能
× 图片防盗链
× 部署到服务器