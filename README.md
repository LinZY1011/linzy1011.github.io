# LinZY1011 GitHub Pages 博客

这是一个直接部署到 `https://linzy1011.github.io/` 的静态个人博客站点。本次实验已经完成：

- 个人博客首页搭建
- 实验报告整理为独立博文
- GitHub Pages 发布准备

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

## 发布方式

提交并推送根目录文件：

```bash
git add index.html styles.css posts/lab2-report.html README.md .nojekyll
git commit -m "feat: launch personal blog on GitHub Pages"
git push origin main
```

如果仓库没有自动发布，可在 GitHub 仓库的 `Settings -> Pages` 中确认发布源指向默认分支根目录。

## 首篇博文

- 实验报告：`/posts/lab2-report.html`
