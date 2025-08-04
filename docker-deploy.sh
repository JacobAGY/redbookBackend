#!/bin/bash

# Docker部署脚本

echo "开始Docker部署..."

# 检查Docker是否安装
if ! command -v docker &> /dev/null; then
    echo "错误: Docker未安装，请先安装Docker"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "错误: Docker Compose未安装，请先安装Docker Compose"
    exit 1
fi

# 停止现有容器
echo "停止现有容器..."
docker-compose down

# 删除旧镜像（可选）
echo "清理旧镜像..."
docker system prune -f

# 构建并启动服务
echo "构建并启动服务..."
docker-compose up --build -d

# 等待服务启动
echo "等待服务启动..."
sleep 10

# 检查服务状态
echo "检查服务状态..."
docker-compose ps

# 查看日志
echo "查看应用日志..."
docker-compose logs web

echo "部署完成！"
echo "应用访问地址: http://localhost"
echo "管理后台: http://localhost/admin"
echo ""
echo "常用命令:"
echo "查看日志: docker-compose logs -f"
echo "停止服务: docker-compose down"
echo "重启服务: docker-compose restart" 