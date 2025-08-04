# Gunicorn配置文件

# 绑定的IP和端口
bind = "0.0.0.0:8000"

# 工作进程数
workers = 4

# 工作进程类型
worker_class = "sync"

# 最大请求数
max_requests = 1000
max_requests_jitter = 100

# 超时设置
timeout = 30
keepalive = 2

# 日志设置
accesslog = "logs/gunicorn_access.log"
errorlog = "logs/gunicorn_error.log"
loglevel = "info"

# 进程名称
proc_name = "redbook_backend"

# 用户和组（生产环境建议设置）
# user = "www-data"
# group = "www-data" 