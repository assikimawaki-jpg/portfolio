"""Configuration Gunicorn pour Railway."""
import os

bind = f"0.0.0.0:{os.environ.get('PORT', '8080')}"
workers = 1
worker_class = "sync"
timeout = 120
