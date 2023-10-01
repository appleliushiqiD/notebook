# 笔记：Git 和 Github 的方法与使用

内容采于***《Github入门与实践》***

### Git

- `git inint` : 初始化仓库  
  - 该命令用于在本地中创建仓库，用于与远程一个空仓库进行联系  
  - 命令会在目录中创建`.git`文件夹，用于跟踪仓库的变化  
  - 目录内容被称为“附属于该仓库的工作树”  
- `git status` : 查看仓库状态  
- `git add <fn/dir>` : 向暂存区添加文件  
  - 暂存区（Stage或Index）是提交之前的一个临时区域  
- `git commit` : 保存仓库的历史记录  
  - `-m <m>` : 添加提交的概述  
  - 将当前暂存区的文件实际保存到仓库的历史记录中  
  - 通过记录，我们可以在工作树中复原文件  
  - 没有使用概述会启动编辑器，编辑更为详细的提交说明  
    提交信息的格式  
    - 第一行：用一行文字简述提交的更改信息  
    - 第二行：空行  
    - 第三行以后：记述更改的原因和详细信息  
    以 # 开始的内容为注释  
    - 留空内容关闭编辑器以终止提交  
- `git log` : 查看提交日志  
  - `--pretty=short` : 只显示一行提交信息  
  - `<fn/dir>` : 只显示目标文件或目录的相关日志  
  - `-p` : 显示文件的改动  
- `git diff` : 查看当前工作树与暂存区的差别  
  - `HEAD` : 查看最新提交与上次提交的差异，`HEAD` 是指向当前分支中最新一次提交的指针  
  - 区别：在修改内容后而没有添加文件到暂存区，使用`git diif`查看差异；未`commit`使用`HEAD`查看差异  

#### 分支

不同分支中，可以进行完全不同的作业，作业完成后，可以合并分支  
**应当保持主分支（master）内容完整，以此创建特新（topic）分支，分支完成后进行合并**  

- `git branch` : 显示分支，其中 * 标记未当前所在分支  
- `git checkout <bn>` : 切换分支  
  - `-b <bn>` : 以当前分支为基础创建新分支，并切换到新分支  
    等同于  
    ```
    git branch <bn>
    git checkout <bn>
    ```
  - `-` : 切换回上一分支  
- `git merge <bn>` : 合并分支  
  - 合并前切换回主分支，启动编辑器编辑合提交的信息（默认信息会包含合并的相关内容）    
  - `--no-ff` : 取消快进式合并，减少分支中提交记录的对主分支的影响  
  - 合并默认`-ff`（如果分支能回到主分支状态则简单移动指针到分支上）  
- `git log --graph` : 图表形式查看分支  

#### 版本控制

- `git reset` : 回溯历史版本  
  - `--hard` : 仓库`HEAD`、暂存区、当前工作树回溯到指定状态  
- `git reflog` : 查看当前仓库的操作记录  
  - `git log`只能查看以当前状态为终点的历史日志   
  - 查找回溯前的状态哈希值，用于“推进”历史  
  - 哈希值只要输入4位以上就可以执行  

