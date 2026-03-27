from pathlib import Path

from docx import Document


def fill_report(template_path: Path, output_path: Path) -> None:
    doc = Document(str(template_path))
    table = doc.tables[0]

    row0 = table.rows[0].cells
    row0[0].text = "学号：202300130066"
    row0[1].text = "姓名：林子逸"
    row0[3].text = "班级：23级泰山学堂"

    row2 = table.rows[2].cells
    row2[0].text = "实验学时：2"
    row2[2].text = "实验日期：3 月 26 日"

    table.rows[4].cells[0].text = "硬件环境：\n联网的计算机一台"
    table.rows[5].cells[0].text = "软件环境：\nWindows\nNode.js v20\nPython 3"

    steps = """实验步骤与内容：
1. 环境构建：在本地 Windows 环境中准备 Node.js 与 Python，作为静态页面开发和本地调试工具链。
2. 网站设计：创建 blog-site 目录，采用“首页 + 文章页 + 样式 + 部署配置”结构，保证内容和部署分离。
3. 页面开发：实现 index.html 与 posts/lab2-report.html，将实验报告正文转为可直接访问的博客文章。
4. 样式优化：编写 styles.css，统一排版、配色和响应式布局，保证桌面端与移动端阅读体验。
5. 本地验证：执行 python -m http.server 8080，访问首页与博文页，检查链接、样式和内容完整性。
6. 服务器部署：将 blog-site 上传至 Linux 云服务器（ECS/CVM），安装并配置 Nginx 托管 /var/www/personal-blog。
7. 域名接入：在 DNS 控制台添加 A 记录指向服务器公网 IP，并通过 certbot 配置 HTTPS 证书。
8. 上线确认：通过域名和公网 IP 双路径访问站点，确认博客页面可稳定打开且证书有效。"""
    table.rows[6].cells[0].text = steps

    conclusion = """结论分析与体会：
本实验完成了从环境构建、网站开发、本地验证到服务器部署和域名接入的完整流程，达成课程实验目标。
静态博客方案具备实现快、部署简单、成本低和维护门槛低的特点，适合课程作业与个人技术展示场景。
通过 Nginx 托管与 HTTPS 证书配置，可以将本地成果平滑迁移到公网环境，提高网站可访问性与安全性。
后续可结合 CI/CD 自动发布、日志监控和备份策略，进一步提升博客系统的工程化与可维护性。"""
    table.rows[7].cells[0].text = conclusion

    doc.save(str(output_path))


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parents[1]
    template = base_dir / "实验报告2_模板.docx"
    output = base_dir / "实验报告2_完成版.docx"

    if not template.exists():
        raise FileNotFoundError(f"未找到模板文件: {template}")

    try:
        fill_report(template, output)
        print(f"已生成: {output}")
    except PermissionError:
        fallback_output = base_dir / "实验报告2_完成版_更新版.docx"
        fill_report(template, fallback_output)
        print(f"目标文件被占用，已生成: {fallback_output}")
