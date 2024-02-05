# 日志收集服务

这是一个基于 FastAPI 的日志收集服务，它接收 HTTP POST 请求，并将日志信息持久化到服务器上的日志文件。

## 安装

首先，克隆这个仓库到你的本地机器上：

```bash
git clone https://github.com/lvguanjun/log-service.git
```

然后，进入到仓库的目录：

```bash
cd log-service
```

接着，安装所需的依赖：

```bash
pip install -r requirements.txt
```

## 配置

在项目的根目录下，复制 `.env.example` 创建一个 `.env` 文件，然后根据你的需求修改它。

```env
cp .env.example .env
```

- `API_KEY` 是你预设的 API 密钥，用于鉴权

## 运行

在项目的根目录下，使用以下命令启动服务：

```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

这将在本地启动一个 FastAPI 应用，你可以通过访问 `http://localhost:8000` 来访问它。

## 使用

你可以通过发送一个 POST 请求到`/logs`路径来创建一个新的日志条目。请求应该包含一个名为 `X-API-KEY` 的 header ，值是你在 `.env` 文件中定义的 API 密钥。请求的 body 应该是一个 JSON 对象，包含 `service` 和 `message` 两个字段。例如：

```json
{
    "service": "user-service",
    "message": "User logged in"
}
```

当接收到有效的请求时，应用将生成一个时间戳，然后将时间戳和消息一起格式化为一个字符串，并写入服务名对应的日志文件，即 `{service}.log`。

## 许可

此项目根据MIT许可证进行许可。