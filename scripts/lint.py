#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""数据校验：字段完整性、ID 唯一、文件存在、prompt 质量线。CI 与本地都会跑。"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "videos.json")

REQUIRED = ["id", "title", "category", "tags", "difficulty", "duration", "summary", "prompt_file"]
# 这些词出现在 prompt 里说明写得不够具体
VAGUE = ["适当调整", "等等", "类似地", "酌情", "随便", "大概就"]
MIN_PROMPT_CHARS = 120


def main():
    errors, warns = [], []
    with open(DATA, encoding="utf-8") as f:
        data = json.load(f)

    cats = {c["id"] for c in data["categories"]}
    seen = set()

    for i, it in enumerate(data.get("items", [])):
        tag = it.get("id", f"#{i}")
        for k in REQUIRED:
            if not it.get(k):
                errors.append(f"[{tag}] 缺字段 {k}")
        if it.get("id") in seen:
            errors.append(f"[{tag}] ID 重复")
        seen.add(it.get("id"))
        if it.get("category") not in cats:
            errors.append(f"[{tag}] 分类 {it.get('category')} 不在 categories 里")
        if not isinstance(it.get("difficulty"), int) or not 1 <= it["difficulty"] <= 4:
            errors.append(f"[{tag}] difficulty 必须是 1-4 的整数")

        pf = os.path.join(ROOT, it.get("prompt_file", ""))
        if not os.path.exists(pf):
            errors.append(f"[{tag}] prompt_file 不存在：{it.get('prompt_file')}")
            continue
        text = open(pf, encoding="utf-8").read()
        body = re.search(r"```\n(.*?)\n```", text, re.S)
        if not body:
            errors.append(f"[{tag}] 没找到 ``` 包裹的 Prompt 代码块")
            continue
        p = body.group(1)
        if len(p) < MIN_PROMPT_CHARS:
            errors.append(f"[{tag}] prompt 过短（{len(p)} 字符，下限 {MIN_PROMPT_CHARS}）")
        for w in VAGUE:
            if w in p:
                warns.append(f"[{tag}] prompt 出现模糊措辞「{w}」，建议改成具体数值")

    for c in data["categories"]:
        n = sum(1 for it in data["items"] if it["category"] == c["id"])
        if n == 0:
            warns.append(f"分类 {c['name']} 下没有任何条目")

    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\n{len(data.get('items', []))} 条 / {len(errors)} 错误 / {len(warns)} 警告")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
