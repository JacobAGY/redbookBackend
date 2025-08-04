# Docker部署指南

## 前置要求

1. 安装Docker Desktop (Mac/Windows) 或 Docker Engine (Linux)
2. 安装Docker Compose

## 快速部署

### 1. 克隆项目
```bash
git clone <your-repo-url>
cd redbookBackend
```

### 2. 运行部署脚本
```bash
chmod +x docker-deploy.sh
./docker-deploy.sh
```

### 3. 手动部署（可选）
```bash
# 构建并启动所有服务
docker-compose up --build -d

# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f
```

## 服务说明

### 应用服务 (web)
- **端口**: 8000
- **功能**: Django应用服务器
- **技术栈**: Python + Gunicorn

### 数据库服务 (db)
- **端口**: 3306
- **功能**: MySQL数据库
- **数据持久化**: mysql_data卷

### 反向代理 (nginx)
- **端口**: 80
- **功能**: 静态文件服务和反向代理
- **缓存**: 静态文件30天缓存

## 常用命令

### 服务管理
```bash
# 启动服务
docker-compose up -d

# 停止服务
docker-compose down

# 重启服务
docker-compose restart

# 查看服务状态
docker-compose ps
```

### 日志查看
```bash
# 查看所有服务日志
docker-compose logs -f

# 查看特定服务日志
docker-compose logs -f web
docker-compose logs -f db
docker-compose logs -f nginx
```

### 数据库操作
```bash
# 进入数据库容器
docker-compose exec db mysql -u agy -p red_book_backend

# 执行Django迁移
docker-compose exec web python manage.py migrate

# 创建超级用户
docker-compose exec web python manage.py createsuperuser
```

### 文件操作
```bash
# 进入应用容器
docker-compose exec web bash

# 收集静态文件
docker-compose exec web python manage.py collectstatic

# 备份数据库
docker-compose exec db mysqldump -u agy -p red_book_backend > backup.sql
```

## 环境配置

### 修改数据库配置
编辑 `docker-compose.yml` 中的数据库环境变量：
```yaml
environment:
  MYSQL_DATABASE: red_book_backend
  MYSQL_USER: agy
  MYSQL_PASSWORD: 123456
  MYSQL_ROOT_PASSWORD: rootpassword
```

### 修改Django设置
编辑 `redBookBackend/settings_production.py`：
```python
ALLOWED_HOSTS = ['your-domain.com', 'your-ip-address', 'localhost']
```

## 生产环境优化

### 1. 安全配置
- 修改 `SECRET_KEY`
- 设置强密码
- 配置防火墙
- 启用HTTPS

### 2. 性能优化
- 增加Gunicorn工作进程数
- 配置Redis缓存
- 优化数据库查询
- 使用CDN

### 3. 监控和日志
- 配置日志轮转
- 设置监控告警
- 定期备份数据

## 故障排除

### 常见问题

1. **端口冲突**
   ```bash
   # 修改docker-compose.yml中的端口映射
   ports:
     - "8080:8000"  # 改为8080端口
   ```

2. **数据库连接失败**
   ```bash
   # 检查数据库服务状态
   docker-compose logs db
   
   # 重启数据库服务
   docker-compose restart db
   ```

3. **静态文件404**
   ```bash
   # 重新收集静态文件
   docker-compose exec web python manage.py collectstatic --noinput
   ```

4. **权限问题**
   ```bash
   # 修改文件权限
   sudo chown -R $USER:$USER .
   ```

## 备份和恢复

### 备份数据库
```bash
docker-compose exec db mysqldump -u agy -p red_book_backend > backup_$(date +%Y%m%d_%H%M%S).sql
```

### 恢复数据库
```bash
docker-compose exec -T db mysql -u agy -p red_book_backend < backup.sql
```

### 备份媒体文件
```bash
tar -czf media_backup_$(date +%Y%m%d_%H%M%S).tar.gz media/
```

## 更新部署

### 代码更新
```bash
# 拉取最新代码
git pull

# 重新构建并部署
docker-compose up --build -d
```

### 配置更新
```bash
# 重启服务
docker-compose restart
``` 