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
    以`#`开始的内容为注释  
    - 留空内容关闭编辑器以终止提交  
  - `git commit -amend` : 修改上一次的提交信息（上一次提交历史被覆盖）  
- `git commit -am <m>` : 合并`add`与`commit`的命令，完成两步操作  
- `git log` : 查看提交日志  
  - `--pretty=short` : 只显示一行提交信息  
  - `<fn/dir>` : 只显示目标文件或目录的相关日志  
  - `-p` : 显示文件的改动  
- `git diff` : 查看当前工作树与暂存区的差别  
  - `HEAD` : 查看最新提交与上次提交的差异，`HEAD` 是指向当前分支中最新一次提交的指针  
  - 区别：在修改内容后而没有添加文件到暂存区，使用`git diff`查看差异；未`commit`使用`HEAD`查看差异  
- `git remote add` : 添加远程仓库  
  - `origin <repository url>` : 将远程仓库的名称设置位`origin`（标识符）  
  - 将本地仓库设置为远程仓库的本地仓库时，保证远程仓库内容不会冲突（可以生成一个没有初始化的远程空仓库）  
- `git push` : 推送至远程仓库  
  - `-u origin master` : 当前分支内容推送给远程仓库`origin`的`master`分支  
  - `-u` : 推送的同时，将`origin`仓库的`master`分支设置为本地仓库当前分支的 upstream （上游），`pull`时该分支可以直接从`master`分支获取内容 
- `git clone` : 获取远程仓库  
  - 命令后我们会默认处于`master`分支下（只会 clone `master` 分支），同时系统将`origin`设为远程仓库的标识符  
  - `git branch -a` : 查看当前分支信息，并可以显示本地仓库和远程仓库的分支信息  
  - `git checkout -b <local feature> <origin/feature>` : 从名为`origin`的仓库 clone `repname`分支  
- `git pull` : 获取最新的远程仓库分支  
  - `origin <feature>` : 从 origin 仓库拉取`feature`分支  

#### 分支

不同分支中，可以进行完全不同的作业，作业完成后，可以合并分支  
**应当保持主分支（ master ）内容完整，以此创建特新（ topic ）分支，分支完成后进行合并**  

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
  - 合并前切换回主分支，启动编辑器编辑合提交的信息（默认信息会包含合并的相关内容，使用中并没有出现编辑器用于编辑合并信息）  
  - `--no-ff` : 取消快进式合并，减少分支中提交记录的对主分支的影响  
  - 合并默认`-ff`（如果分支能回到主分支状态则简单移动指针到分支上）  
- `git log --graph` : 图表形式查看分支  
- `git commit -amend` : 修改上一次的提交信息（上一次提交历史被覆盖）  



#### 版本控制

- `git reset` : 回溯历史版本  
  - `--hard` : 仓库`HEAD`、暂存区、当前工作树回溯到指定状态  
- `git reflog` : 查看当前仓库的操作记录  
  - `git log`只能查看以当前状态为终点的历史日志   
  - 查找回溯前的状态哈希值，用于“推进”历史  
  - 哈希值只要输入4位以上就可以执行  
- `git rebase -i` : 压缩历史  
  - `HEAD~2` : 选定当前分支中包含HEAD（最新提交）在内的两个最新历史为对象  
  - 将需要被压缩的历史对象的`pick`改为 `fixup`（`pick`项的 message 会成为新历史的 message ，历史的哈希值会改变）  

#### 帮助深入理解Git

- [Pro Git](http://git-scm.com)（请在主页的 Documentation/Book 下找到相关的内容）  
  ***Pro Git*** 由就职于 GIthub 公司的 Scott Chacon 执笔，是一部零基础的 Git 学习资料。（摘于原书）  
- [LearnGitBranching](https://learngitbranching.js.org)（原书链接跳转结果）  
  - LearnGitBranching 是学习 Git 基本操作的网站。注重树形结构的学习方式非常适合初学者（摘于原书）  
  - 该网站有相关 Git 命令的演示动画和相关命令的执行任务，适合理解命令的意义，不过内容过于简单  
- [tryGit](http://try.github.io)  
  - 通过 tryGit 我们可以在 Web 上一边操作一边学习 Git 的基本功能，很可惜该教程只有英文版。（摘于原书）  


### GitHub


