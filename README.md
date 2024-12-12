# YouTube 视频下载器

一个基于 FastAPI + yt-dlp 的 YouTube 视频下载工具，支持高质量视频直接下载到本地。

## 功能特点

- ✨ 简洁优雅的用户界面
- 📊 实时下载进度显示
- 🚀 异步下载，不阻塞主线程
- 💾 直接下载到本地
- 📝 清晰的下载状态提示

## 技术栈

- 后端框架：FastAPI
- 模板引擎：Jinja2
- 下载工具：yt-dlp
- 前端样式：TailwindCSS
- 类型检查：Pydantic

## 项目结构

```bash
YouTube视频下载/
├── app/                    # 应用主目录
│   ├── __init__.py
│   ├── config.py          # 配置文件
│   ├── main.py           # 主程序入口
│   ├── core/             # 核心功能
│   │   ├── __init__.py
│   │   ├── downloader.py # 下载器
│   │   └── utils.py      # 工具函数
│   └── routers/          # 路由处理
│       ├── __init__.py
│       └── download.py   # 下载相关路由
├── static/               # 静态文件
│   └── videos/          # 临时下载目录
├── templates/           # 模板文件
│   └── index.html      # 主页面
└── requirements.txt    # 项目依赖
```

## 核心模块说明

### 1. 配置模块 (config.py)
- 项目基础配置
- 路径配置
- 下载参数配置

### 2. 下载器模块 (downloader.py)
- 视频下载核心逻辑
- 进度追踪
- 错误处理
- 文件路径管理

### 3. 路由模块 (download.py)
- HTTP 请求处理
- 下载任务管理
- 进度查询接口

## API 接口说明

### 1. 主页
- 路由：`GET /`
- 功能：显示下载界面

### 2. 下载视频
- 路由：`POST /download`
- 功能：开始下载视频
- 参数：
  - video_url: YouTube 视频链接
- 返回：
  ```json
  {
    "video_id": "下载任务ID"
  }
  ```

### 3. 获取下载进度
- 路由：`GET /progress/{video_id}`
- 功能：获取下载进度
- 返回：
  ```json
  {
    "status": "downloading|finished|error",
    "progress": "下载进度",
    "speed": "下载速度",
    "eta": "预计剩余时间",
    "file_path": "文件保存路径"
  }
  ```

## 安装和运行

1. 克隆项目：
```bash
git clone [项目地址]
cd YouTube视频下载
```

2. 创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 安装依赖��
```bash
pip install -r requirements.txt
```

4. 运行项目：
```bash
uvicorn app.main:app --reload
```

5. 访问网址：
打开浏览器访问 http://localhost:8000

## 使用说明

1. 在输入框中粘贴 YouTube 视频链接
2. 点击"下载"按钮开始下载
3. 等待下载完成，查看文件保存路径
4. 在本地文件夹中找到下载的视频

## 维护和升级指南

### 添加新功能
1. 在相应模块添加新代码
2. 更新路由和模板
3. 更新文档

### 常见维护任务
1. 更新依赖：
```bash
pip install -r requirements.txt --upgrade
```

2. 清理临时文件：
```bash
rm -rf static/videos/*
```

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 发起 Pull Request

## 许可证

MIT License

## 联系方式

如有问题或建议，请提交 Issue 或发送邮件至 qiaomu6666@gmail.com

## 分支管理

本项目包含以下分支：

- `main`: 主分支，保存稳定版本
- `local-version`: 本地运行版本，适合个人使用
- `deploy-version`: 在线部署版本，支持多人使用（开发中）

### 分支用途说明

- **local-version**：
  - 本地运行的稳定版本
  - 适合个人使用
  - 直接下载到本地存储

- **deploy-version**：
  - 支持在线部署
  - 多用户支持
  - 云存储支持
  - 用户认证功能