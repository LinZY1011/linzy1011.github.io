# 个人博客（实验二）

本目录为《云计算技术》实验二交付代码，包含一个可直接运行的静态博客站点，并将实验报告发布为博客文章。

## 目录结构

```text
blog-site/
├─ index.html
├─ styles.css
├─ posts/
│  └─ lab2-report.html
└─ deploy/
   └─ nginx-site.conf
```

## 本地运行

```bash
cd blog-site
python -m http.server 8080
```

浏览器访问：`http://localhost:8080`

## 云服务器部署（Nginx）

1. 将 `blog-site` 目录上传至云服务器，例如 `/var/www/personal-blog`。
2. 安装 Nginx 并启用站点配置：

```bash
sudo cp deploy/nginx-site.conf /etc/nginx/sites-available/personal-blog.conf
sudo ln -s /etc/nginx/sites-available/personal-blog.conf /etc/nginx/sites-enabled/personal-blog.conf
sudo nginx -t
sudo systemctl reload nginx
```

3. 通过服务器公网 IP 或域名访问博客首页。

## 域名解析与 HTTPS

1. 在域名服务商控制台添加 A 记录：
   - `@` -> 服务器公网 IP
   - `www` -> 服务器公网 IP
2. 在服务器安装证书工具并自动配置 HTTPS：

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
sudo certbot renew --dry-run
```

3. 验证 `https://your-domain.com` 可访问。
