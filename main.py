# -*- coding: utf-8 -*-

import sys, os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher


class MarkdownPreviewTest(FlowLauncher):

    def query(self, query):
        return [
            {
                "Title": "Always",
                "SubTitle": "PreviewVisibility: always",
                "IcoPath": "Images/app.png",
                "Preview": {
                    "ContentType": "markdown",
                    "Description": _preview_content()
                },
                "PreviewVisibility": "always"
            },
            {
                "Title": "Default",
                "SubTitle": "PreviewVisibility: default",
                "IcoPath": "Images/app.png",
                "Preview": {
                    "ContentType": "markdown",
                    "Description": _preview_content()
                },
                "PreviewVisibility": "default"
            },
            {
                "Title": "Never",
                "SubTitle": "PreviewVisibility: never",
                "IcoPath": "Images/app.png",
                "Preview": {
                    "ContentType": "markdown",
                    "Description": _preview_content()
                },
                "PreviewVisibility": "never"
            },
            {
                "Title": "None",
                "SubTitle": "Preview and PreviewVisibility are unset",
                "IcoPath": "Images/app.png",
            }
        ]

    def context_menu(self, data):
        return []


def _preview_content():
    return """## Test Preview

**bold** *italic* `code`

### Code Block

```python
# long line for horizontal scroll testing
def search(query): results = find(query); return [r for r in results if r.matches and r.is_valid and r.score > 0.5]











# vertical space test
```

### Long line outside code block

This is a deliberately long line of text outside any code block to test whether the markdown renderer handles line wrapping correctly for very long content that exceeds the width of the preview pane without forcing a horizontal scrollbar on the entire document.

### Blockquotes

> single blockquote

> first level
> > second level
> > > third level

### Lists

- item one
- item two

1. first
2. second

### Horizontal rule

---

### Table with long cell

| Short | Really Long Cell Content Here |
|-------|-------------------------------|
| x     | This cell has a very long line of text that should wrap or scroll depending on how the table rendering is handled in the markdown preview pane |


"""


if __name__ == "__main__":
    MarkdownPreviewTest()
