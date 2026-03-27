# LinZY1011 Nginx 云服务器博客

这是一个使用 Nginx 部署到云服务器上的静态个人博客站点，当前只保留：

- 首页简介
- 实验报告博文

## 目录结构

```text
linzy1011.github.io/
├─ index.html
├─ styles.css
├─ README.md
├─ .nojekyll
└─ posts/
   └─ lab2-report.html
```

## 本地预览

在仓库根目录运行：

```bash
python -m http.server 8080
```

然后访问 [http://localhost:8080/](http://localhost:8080/)。

## 云服务器部署

将站点文件复制到云服务器目录后，由 Nginx 托管：

```bash
sudo mkdir -p /var/www/linzy1011.github.io
sudo cp -r index.html styles.css posts .nojekyll /var/www/linzy1011.github.io/
sudo systemctl reload nginx
```
