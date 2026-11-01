<div align="center">

# Awesome AI 视频 Prompt · 中文首发

**给任意会写代码的 AI 一句中文描述，让它直接把动画写成 HTML / Canvas / SVG / Three.js，录屏即成片。**

不需要剪辑软件，不需要素材库，不需要建模。你需要的只是一段说得够具体的描述。

[![Stars](https://img.shields.io/github/stars/{{REPO}}?style=flat-square&color=C2662F&label=stars)](https://github.com/{{REPO}}/stargazers)
[![PRs](https://img.shields.io/badge/PRs-welcome-C2662F?style=flat-square)](../../pulls)
[![License](https://img.shields.io/badge/license-MIT-C2662F?style=flat-square)](LICENSE)
[![Prompts](https://img.shields.io/badge/prompts-{{COUNT}}-C2662F?style=flat-square)](prompts/)

### [▶ {{CTA_LABEL}}]({{CTA_URL}})

</div>

---

这里收录的是**「描述 → 代码 → 视频」**这条链路上真正跑得通的中文 prompt。

每一条都包含完整参数：画布尺寸、颜色值、缓动曲线、时长、性能约束。不是「做一个酷炫的粒子动画」这种说了等于没说的话——你复制过去，就能得到一个具体的东西。

{{COUNT}} 条起步，按品类持续收录中。

---

## 目录

{{TOC}}

---

## 这个库怎么用

**第一步 · 复制。** 点进任意一条，把「Prompt」代码块整段复制走。

**第二步 · 粘贴。** 丢给任何一个能写代码的模型（Claude / GPT / Gemini / DeepSeek 都行），要求它输出单个 HTML 文件。

**第三步 · 改。** 每条都附了「调参提示」，告诉你哪个数字动了会出什么效果。改文字、改配色、改时长，比从零写快一百倍。

**第四步 · 录。** 浏览器全屏打开，用系统录屏或 OBS 录下来。想要 4K 就把画布尺寸参数改掉再录。

> 为什么是「写代码」而不是「生成视频」？
> 因为代码生成的内容是**可无限微调**的：改一个颜色值不用重新抽卡，改一个时长不用重拍。这也是这类内容能复现的前提。

---

## 全部内容

{{GALLERY}}

---

## 收录标准

一条 prompt 要被收进来，必须同时满足：

| 标准 | 说明 |
|---|---|
| **可复现** | 复制过去就能跑出接近的效果，不是「概念演示」 |
| **参数完整** | 尺寸、颜色、时长、缓动都写死，不留「适当调整」这种话 |
| **无外部依赖** | 不依赖素材文件、不依赖付费 API、不依赖特定版本的库 |
| **性能可控** | 明确标注帧率要求和性能约束，能在普通笔记本上跑 |
| **中文可读** | 用中文写，且是中国人能看懂的中文，不是机翻 |

不符合的会直接关掉，别介意。

---

## 快速索引

| 我想做… | 去看 |
|---|---|
| 一个品牌 LOGO 开场 | [液态金属文字开场](prompts/m001-液态金属文字开场.md) · [粒子聚合成汉字](prompts/m002-粒子聚合成汉字.md) |
| 一个数据看板动效 | [数字滚动的数据看板](prompts/e002-数字滚动的数据看板.md) · [等距网格数据流](prompts/m003-等距网格数据流.md) |
| 讲清一个流程 / 概念 | [三步流程图生长](prompts/e001-三步流程图生长.md) · [时间轴演化](prompts/e003-时间轴演化.md) · [漏斗转化过程](prompts/e006-漏斗转化过程.md) |
| 一个科技感片头 | [悬浮芯片主视觉](prompts/s003-悬浮芯片主视觉.md) · [无限走廊穿梭](prompts/s002-无限走廊穿梭.md) · [地球数据弧线](prompts/s004-地球数据弧线.md) |
| 让用户愿意多玩两秒 | [点击爆破粒子](prompts/g003-点击爆破粒子.md) · [磁力场跟随](prompts/g005-磁力场跟随.md) |
| 直接能玩的小游戏 | [打砖块变体](prompts/g001-打砖块变体.md) · [极简贪吃蛇](prompts/g004-极简贪吃蛇.md) · [节奏点击](prompts/g006-节奏点击.md) |

---

## 贡献

有跑通的新 prompt？欢迎 PR。规则见 [CONTRIBUTING.md](CONTRIBUTING.md)，只改 `data/videos.json` 和 `prompts/` 两处，README 会自动重建。

发现某条已经跑不通了（模型行为变了、库升级了）？开 issue 说明现象，会比 PR 更受欢迎。

---

## 说明

- 本库所有 prompt 均为原创撰写并实测，采用 MIT 协议，可自由商用、改写、二次分发。
- 生成的成品归你，不需要署名（当然署了更好）。
- 如果你认为某条内容与你的作品雷同，见 [DISCLAIMER.md](DISCLAIMER.md)，提 issue 我们会处理。

<div align="center">

**[▶ {{CTA_LABEL}}]({{CTA_URL_FOOT}})**

<sub>最后更新：{{UPDATED}} · 由 <code>scripts/build_readme.py</code> 自动生成，请勿手改本文件</sub>

</div>
