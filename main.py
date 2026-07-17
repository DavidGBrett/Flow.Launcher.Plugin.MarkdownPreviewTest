# -*- coding: utf-8 -*-

import sys, os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher


class MarkdownPreviewTest(FlowLauncher):

    def query(self, query):
        preview = _preview_content(query)
        return [
            {
                "Title": "Always",
                "SubTitle": "PreviewVisibility: always",
                "IcoPath": "Images/app.png",
                "Preview": {
                    "ContentType": "markdown",
                    "Description": preview
                },
                "PreviewVisibility": "always"
            },
            {
                "Title": "Optional",
                "SubTitle": "PreviewVisibility: optional",
                "IcoPath": "Images/app.png",
                "Preview": {
                    "ContentType": "markdown",
                    "Description": preview
                },
                "PreviewVisibility": "optional"
            },
            {
                "Title": "Never",
                "SubTitle": "PreviewVisibility: never",
                "IcoPath": "Images/app.png",
                "Preview": {
                    "ContentType": "markdown",
                    "Description": preview
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


def _preview_content(query=""):
    raw = query.strip()
    if raw:
        preview = raw + "\n\n---\n\n" + _default_content()
    else:
        preview = _default_content()
    return preview


def _default_content():
    return """## Markdown Examples

**bold** *italic* `code`

### Links

- <https://github.com/Flow-Launcher/Flow.Launcher>
- [Flow Launcher](https://github.com/Flow-Launcher/Flow.Launcher)
- [named link with title](https://github.com/Flow-Launcher/Flow.Launcher "Flow Launcher")

### Code Blocks

```python
# long line for horizontal scroll testing
def search(query): results = find(query); return [r for r in results if r.matches and r.is_valid and r.score > 0.5]










# vertical space test
```

```xml
<note>
  <to>User</to>
  <from>Plugin</from>
  <body>XML rendering test</body>
</note>
```

```json
{
  "name": "test",
  "nested": {
    "array": [1, 2, 3],
    "enabled": true
  }
}
```

```diff
- old line
+ new line
 unchanged
```

```text
plain text block with no highlighting
```

### HTML

<p style="color: red;">Red paragraph text</p>
<p><b>Bold HTML</b> and <i>italic HTML</i> and <u>underlined</u></p>
<details><summary>Click to expand</summary>Hidden content</details>
<table border="1"><tr><td>Cell 1</td><td>Cell 2</td></tr></table>

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

### Images

![Flow Launcher](https://raw.githubusercontent.com/Flow-Launcher/Flow.Launcher/master/Flow.Launcher/Images/app.png)
"""


if __name__ == "__main__":
    MarkdownPreviewTest()
