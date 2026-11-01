#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""换站点地址：一行命令改完全站出口与 UTM，再自动重建 README。

用法：
    python3 scripts/set_site.py https://你的域名
    python3 scripts/set_site.py https://你的域名 --label "看在线演示"
    python3 scripts/set_site.py --show

改的是 data/videos.json 的 site 字段，README 由它生成，所以只有这一处需要改。
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "videos.json")


def main():
    args = [a for a in sys.argv[1:]]
    with open(DATA, encoding="utf-8") as f:
        data = json.load(f)
    site = data["site"]

    if not args or args[0] in ("--show", "-s"):
        print(f"当前地址：{site['url']}")
        print(f"按钮文案：{site['label']}")
        print(f"UTM     ：{site['utm']}")
        return

    url = args[0].rstrip("/")
    if not url.startswith(("http://", "https://")):
        sys.exit("地址必须以 http:// 或 https:// 开头")

    site["url"] = url
    if "--label" in args:
        i = args.index("--label")
        if i + 1 < len(args):
            site["label"] = args[i + 1]

    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build_readme.py")], check=True)
    print(f"已切换到 {url}")


if __name__ == "__main__":
    main()
