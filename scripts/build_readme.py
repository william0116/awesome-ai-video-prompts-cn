#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 data/videos.json 生成 README.md 与 prompts 索引。

用法：
    python3 scripts/build_readme.py          # 生成 README.md
    python3 scripts/build_readme.py --check  # 只校验，不写文件

规则：
    - data/videos.json 是唯一事实来源，README 是产物，不要手改 README。
    - 站点地址与 UTM 只在这里和 data/videos.json 的 site 字段里出现，
      换域名只改一处，重跑即可全站生效。
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "videos.json")
OUT = os.path.join(ROOT, "README.md")
TPL = os.path.join(ROOT, "README.template.md")

REPO = "william0116/awesome-ai-video-prompts-cn"


def cta(site, content):
    """拼出带 UTM 的出口链接。content 用来区分区块，便于归因。"""
    base = site["url"].rstrip("/")
    utm = site["utm"]
    return f"{base}/?{utm}&utm_content={content}"


def build(data):
    site = data["site"]
    items = data["items"]
    cats = data["categories"]
    by_cat = {c["id"]: [] for c in cats}
    for it in items:
        by_cat[it["category"]].append(it)

    # ---- 统计 ----
    stats = [
        ("收录 Prompt", f"{len(items)} 条"),
        ("覆盖品类", f"{len(cats)} 类"),
        ("可直接复现", "全部（含完整参数）"),
        ("依赖", "无外部库、无素材文件"),
    ]
    stats_md = "\n".join(
        f"| **{k}** | {v} |" for k, v in stats
    )

    # ---- 目录 ----
    toc = "\n".join(
        f"- [{c['name']}](#{c['name'].lower().replace(' ', '-')})（{len(by_cat[c['id']])} 条）"
        for c in cats
    )

    # ---- 正文分区 ----
    # 只要全库有任何一条带封面图，该分类就自动切换成图墙模式；否则退回文本表格。
    # 补图时只需在 data/videos.json 里填 cover，重跑即可。
    sections = []
    for c in cats:
        group = by_cat[c["id"]]
        if any(it.get("cover") for it in group):
            cells = [
                f'<a href="{it["prompt_file"]}"><img src="{it.get("cover") or ""}" width="240" alt="{it["title"]}"></a>'
                f'<br><sub><b>{it["title"]}</b></sub>'
                for it in group
            ]
            rows = []
            for i in range(0, len(cells), 3):
                chunk = cells[i:i + 3]
                chunk += [""] * (3 - len(chunk))
                rows.append("| " + " | ".join(chunk) + " |")
            body = "| | | |\n|:--:|:--:|:--:|\n" + "\n".join(rows)
        else:
            lines = []
            for it in group:
                stars = "★" * it["difficulty"] + "☆" * (4 - it["difficulty"])
                lines.append(
                    f"| [`{it['title']}`]({it['prompt_file']}) | {it['summary']} | {stars} | {it['duration']} |"
                )
            body = "| 名称 | 效果 | 难度 | 时长 |\n|---|---|:--:|:--:|\n" + "\n".join(lines)
        sections.append(f"### {c['name']}\n\n{c['desc']}\n\n{body}")
    gallery = "\n\n".join(sections)

    return dict(
        STATS=stats_md,
        TOC=toc,
        GALLERY=gallery,
        COUNT=str(len(items)),
        CAT_COUNT=str(len(cats)),
        UPDATED=data["updated"],
        CTA_URL=cta(site, "hero"),
        CTA_URL_FOOT=cta(site, "footer"),
        CTA_LABEL=site["label"],
        REPO=REPO,
    )


def main():
    with open(DATA, encoding="utf-8") as f:
        data = json.load(f)
    with open(TPL, encoding="utf-8") as f:
        tpl = f.read()

    ctx = build(data)
    md = tpl
    for k, v in ctx.items():
        md = md.replace("{{" + k + "}}", v)

    left = [p for p in ("{{", "}}") if p in md]
    if left:
        print("模板占位符未全部替换：", left, file=sys.stderr)
        sys.exit(1)

    if "--check" in sys.argv:
        with open(OUT, encoding="utf-8") as f:
            if f.read() != md:
                print("README 与数据不一致，请运行 python3 scripts/build_readme.py", file=sys.stderr)
                sys.exit(1)
        print("README 一致。")
        return

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"已生成 README.md —— {ctx['COUNT']} 条 / {ctx['CAT_COUNT']} 类")


if __name__ == "__main__":
    main()
