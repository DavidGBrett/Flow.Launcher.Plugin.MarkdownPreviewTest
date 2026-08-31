# Markdown File Preview

This preview is loaded from a Markdown file in the plugin directory.

## File-backed content

- The path found using `__file__` and `os.path`.
- It remains valid when Flow Launcher runs the plugin from its installed location.

```python
def preview_from_file(path):
    return path
```