#!/bin/bash

# Django项目部署脚本

echo "开始部署Django项目..."

# 1. 安装依赖
echo "安装Python依赖..."
pip install -r requirements.txt

# 2. 收集静态文件
echo "收集静态文件..."
python manage.py collectstatic --noinput

# 3. 执行数据库迁移
echo "执行数据库迁移..."
python manage.py migrate

# 4. 创建日志目录
mkdir -p logs

echo "部署完成！" 