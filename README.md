# MF703_final_project

先建一个文件夹
>cd desktop/文件夹名
然后
>git clone https://github.com/ShenghengLi/MF703_final_project.git 

基础设定（方便查看修改者）
>git config --global user.name "..."
和
>git config --global user.email "..."
和
>git config --global init.default branch main

查看修改记录
>git log
或者
>git log --oneline

查看local和github上文件的区别
>git status

添加新文件（修改完之后也要再add一遍）
>git add <文件名>
然后
>git commit -a -m "<填入关于修改的说明（必须有东西）>"
然后
>git push 

删除文件
>git rm <文件名>
然后
>git commit -a -m "<填入关于修改的说明（必须有东西）>"
然后
>git push 这时候就已经改好了