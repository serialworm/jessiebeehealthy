import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'blog/static/')
)

print(STATICFILES_DIRS)
