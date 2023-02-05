from os import path
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
STATIC_FILES_DIR = path.join(ROOT_DIR, 'static')
STATIC_URL = '/static/'

CONTENT_TYPES_MAP = {
        ".css": "text/css",
        ".htm": "text/html",
        ".html": "text/html",
        ".js": "text/javascript",
        ".png": "image/png",
        ".svg": "image/svg+xml",
}
