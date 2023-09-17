# 笔记：Emacs 编辑器

***查看中文指南 `M-x help-with-tutorial-spec-language` / `C-u C-h t`***

### 命令基础

- `M-c` == `Esc c`  

| Key | Desc |
| :---: | :---: |
| `C` | `Ctrl` / `Ctl` |
| `M` | `Meta` / `Alt` / `Edit` |
| `C-c`| 按住 `Ctrl` 同时按住 `c` |
| `C-c c` | 使用 `Ctrl-c` 后按 `c` |
| `C-x C-c` | 退出 Emacs |
| `C-g` | 中断输入的命令 |
| `C-u ? <op>` | 重复命令 op ？次 |

### 光标移动

- 翻页  
  `C-v`: 下翻页，屏幕内容为一页  
  `M-v`: 上翻页，屏幕内容为一页  
  `C-l`: 重绘屏幕，光标所在行移动至屏幕中央  
- 上下左右  
  `C-p/n/b/f` ( previous/next/backward/forward )  
- 词句  
  `M-b/f` 光标向前 / 向后移动一个词的量  
  `M-a/e` 光标移动到句首 / 句尾  
- 行间  
  `C-a/e` 光标移动到行首 / 行尾  
- 内容  
  `M-</>` 光标移动到所有文字最开头 / 最末尾（ `<` 使用 `shift` 写出） == `M-shift-,/.`   
- 
