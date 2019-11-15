# CrashCourse-Physics       

## 十分钟速成课 | 物理部分双语字幕 

[![](https://img.shields.io/badge/CrashCourse-xxk-yellow.svg?style=social&logo=youtube)](?)
[![](https://img.shields.io/badge/CrashCourse-xxk-yellow.svg?style=social&logo=twitter)](?)
[![](https://img.shields.io/badge/CrashCourse-xxk-yellow.svg?style=social&logo=facebook)](?)

### [原视频合集（生肉）](?)
### [b站双语合集链接（更新中）](https://www.bilibili.com/video/av49721651/跳转bilibili)

# Don't Forget To Be Awosome!

### 分集标题。。（待续）

### 工具（自用）：

- [ ]`ass2txt.py`推荐![](https://img.shields.io/badge/Python-v3.5-blue.svg)以上运行

- [x]打包后的`ass2txt.exe`(无需安装py，双击即可)

`.ass -> .txt`文本转换，去掉版本信息、字体信息和时间轴等无关内容，每句之间增加空行；并修改文件名增加可读性。
```
// 原始ass文件
Dialogue: 0,0:01:00.56,0:01:04.04,统计en,,0,0,0,,In the mid 19th century, a German physicist named Gustav Kirchhoff
Dialogue: 0,0:01:00.56,0:01:04.04,统计ch,,0,0,0,,19世纪中期 德国的物理学家Gustav Kirchhoff
Dialogue: 0,0:01:04.40,0:01:07.50,统计en,,0,0,0,,expanded on the principles of Ohm's law to improve our ability
Dialogue: 0,0:01:04.40,0:01:07.50,统计ch,,0,0,0,,拓展了欧姆定律
// 转换后的txt文件：
In the mid 19th century, a German physicist named Gustav Kirchhoff
19世纪中期 德国的物理学家Gustav Kirchhoff

expanded on the principles of Ohm's law to improve our ability
拓展了欧姆定律

// 原文件名 -> 转换后文件名：
Capacitors and Kirchhoff -  Crash Course Physics #31.ass
                            ↓
Crash Course Physics #31 Capacitors and Kirchhoff .txt
```

#### 用法：
1. `$ python ass2txt.py`；
2. 将`ass2txt.exe`放在字幕文件夹中，双击。
