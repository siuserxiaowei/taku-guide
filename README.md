# Taku 新手图文手册

**[在线阅读图文手册](https://siuserxiaowei.github.io/taku-guide/)** · [查看 Markdown](Taku新手图文手册.md)

根据 Taku 官网、官方 X、Publisher / Sites 文档与 macOS 客户端实机整理的中文参考手册，包含 **22 个章节（第 0—21 节）、21 张实机截图**。这是第三方使用参考，非 Taku 官方文档。

- 核对日期：2026-10-19
- 实机版本：Taku 3.1.123（macOS，中文界面）
- 内容：Taku 是什么与电脑要求、套餐与 credits、隐私与作品许可、创作者收益预期、版本速览、常见问题；以及现成 App、`@` 资源、Skill / API、创建与修改 App、任务管理、自动化、模型、集成、通知、Helper、Publisher、Sites 与常见排错。
- 已验证、官方流程和尚未端到端验证的部分，见手册第 21 节。

## 推荐阅读顺序

1. 第 0 节：Taku 是什么、你的电脑能不能装；第 16 节：要花多少钱。
2. 第 2 节：打开现成 App，验证一次交互。
3. 第 4、6 节：理解 `@` 菜单，创建自己的简单工具。
4. 第 11—13 节：带入 Codex / Claude 项目，以及新词雷达的迁移路线。

## 文件

- `index.html`：带目录、可放大截图、可复制提示词与打印样式的网页版。
- `Taku新手图文手册.md`：Markdown 原稿。
- `screenshots/`：21 张实机截图原图（PNG，2400×1600，Markdown 和网页放大图使用）。
- `screenshots/web/`：网页正文用的 WebP 压缩版（1600 宽，约 1.1 MB，原图约 6.2 MB）。
- `og-cover.jpg`：分享到微信、X 等平台时的封面图。
- `sitemap.xml`：给搜索引擎提交的站点地图。
- `.nojekyll`：按静态文件发布到 GitHub Pages。

## 修改内容

只改 `Taku新手图文手册.md`，然后生成网页：

```bash
pip install markdown
python3 tools/build.py
```

`tools/template.html` 是网页外壳（样式、目录、脚本），`build.py` 会把 Markdown 填进去，并自动生成目录和 WebP 图片引用。

## 本地预览

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

浏览器打开 `http://127.0.0.1:8000/`。在线版由 GitHub Pages 发布 `main` 分支根目录，更新文件后会自动重建。

## 官方资料

[Taku 官网](https://taku.ai/) · [官方更新记录](https://taku.ai/changelog) · [Marketplace](https://taku.ai/marketplace) · [官方 X](https://x.com/TheTakuAI) · [Publisher](https://github.com/Taku-OS/taku-publisher)

每节的具体来源见手册正文。截图中的账号状态和已有任务属于拍摄时示例，不能视为所有账号的默认状态。
