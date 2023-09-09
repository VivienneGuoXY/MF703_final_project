# MF703_final_project

## Git tutorial
先建一个文件夹
>mkdir -p desktop/<文件夹名>

>cd desktop/<文件夹名>

Clone this project to your
>git clone https://github.com/ShenghengLi/MF703_final_project.git

or by SSH. Note: you might need to setup your public key. Refer to online tutorials.

基础设定（方便查看修改者）
>git config pull.rebase false

>git config --global user.name "<填入名字>"

>git config --global user.email "<填入email>"

>git config --global init.default branch main

>git config --global credential.helper store


查看修改记录
>git log

>git log --oneline

查看local和github上文件的区别
>git status

>git status -u

创造自己的branch（不要直接修改main）
>git checkout -b <branch_name>

>git branch

删除自己的branch
>git push -d origin <branch_name>

Checkout ("switch") to a new branch
>git fetch origin

>git checkout <target_branch_name>

更新自己的本地文件
>git pull

添加新文件（修改完之后也要再add一遍)
>git add <文件名>

>git commit -m "<填入关于修改的说明（必须有东西）>"

>git push

删除文件
>git rm <文件名>

>git commit -m "<填入关于修改的说明（必须有东西）>"

Push your change to remote.
>git pull

>git merge

>git push
