"""把 Taku新手图文手册.md 生成为 index.html。

用法：python3 tools/build.py（需要 pip install markdown）
"""
import html
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "Taku新手图文手册.md"
TEMPLATE = ROOT / "tools" / "template.html"
OUT = ROOT / "index.html"


def slug(text):
    return "section-" + "-".join(re.findall(r"[0-9A-Za-z一-鿿]+", text))


def main():
    md = SRC.read_text(encoding="utf-8")
    title, rest = md.split("\n", 1)
    assert title.startswith("# ")
    subtitle, rest = rest.strip().split("\n", 1)

    body = markdown.markdown(rest, extensions=["tables", "fenced_code"])

    chapters = []

    def h2(m):
        text = m.group(1)
        num = re.match(r"(\d+)\.\s*(.*)", html.unescape(text))
        chapters.append((num.group(1), num.group(2)))
        return f'<h2 id="chapter-{num.group(1)}">{text}</h2>'

    body = re.sub(r"<h2>(.*?)</h2>", h2, body)
    body = re.sub(r"<h3>(.*?)</h3>",
                  lambda m: f'<h3 id="{slug(html.unescape(re.sub("<.*?>", "", m.group(1))))}">{m.group(1)}</h3>', body)
    body = body.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    body = re.sub(r"<pre><code([^>]*)>", r'<div class="code-wrap"><button class="copy" type="button">复制</button><pre><code\1>', body)
    body = body.replace("</code></pre>", "</code></pre></div>")

    first = True

    def img(m):
        nonlocal first
        src, alt = m.group(1), m.group(2)
        name = Path(src).stem
        load = 'loading="eager" fetchpriority="high"' if first else 'loading="lazy"'
        first = False
        return (f'<picture><source srcset="screenshots/web/{name}.webp" type="image/webp">'
                f'<img src="{src}" alt="{alt}" width="2400" height="1600" {load} decoding="async"></picture>')

    body = re.sub(r'<img src="(screenshots/[^"]+\.png)" alt="([^"]*)"[^>]*>', img, body)

    links = "".join(
        f'<a href="#chapter-{n}"><span>{int(n):02d}</span>{html.escape(t)}</a>' for n, t in chapters)
    head = (f'<h1 id="top">{html.escape(title[2:])}</h1>'
            f'<details class="mobile-toc"><summary>展开章节目录</summary><nav>{links}</nav></details>'
            f'<p>{html.escape(subtitle)}</p>\n')

    page = TEMPLATE.read_text(encoding="utf-8")
    page = (page.replace("{{NAV}}", links)
                .replace("{{COUNT}}", str(len(chapters)))
                .replace("{{BODY}}", head + body))
    OUT.write_text(page, encoding="utf-8")
    print(f"index.html：{len(chapters)} 个章节，{body.count('<picture>')} 张图")


if __name__ == "__main__":
    main()
