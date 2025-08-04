"""
Django settings for redBookBackend project - Production Environment
"""

import os
from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# 生产环境允许的主机
ALLOWED_HOSTS = ['your-domain.com', 'your-ip-address', 'localhost']

# 静态文件配置
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 安全设置
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# 数据库配置（生产环境建议使用更安全的配置）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'red_book_backend',
        'USER': 'agy',
        'PASSWORD': '123456',
        'HOST': '1.12.253.202',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
} 