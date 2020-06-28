import os

#打开输入文件，整理后的log。log.txt需要是utf-8编码并且和自动脚本for renpy.py放在一个目录下面
fobj = open('log.txt',mode='r',encoding='utf-8')
#创建用于复制进活字引擎的输出文件
file_rpy = open('游戏剧本.txt',mode='w',encoding='utf-8')

#列出log.txt里所有出现的kp、骰子、pl及npc的角色名字
char_list=["【GM】","【梅花4】", "【梅花7】", "【黑桃3】", "【黑桃6】"]

##################################################################以上为需要修改的部分

#set the initial value#tag初始化。不要改动
char_tag="【null】"
previous_char_tag="【null】"

#用于存放log.txt中不应该出现的字符。不要改动
illegal_list=["?",":", "<", ">", "*", "\"", "/", "\\", "[", "]"]

file_rpy.write("#背景#测试背景A\n")

for l in fobj:
    line=l.strip();#line is the content of current line
    if len(line)>0:#只处理非空行
        if line[0]=="【":#检测是否为角色行
            IsValidTag=0
            for i in range(len(char_list)):
                if line==char_list[i]:#which means
                    previous_char_tag=char_tag#save the current one to previous
                    char_tag=line#change char tag if find a new one
                    IsValidTag=1
            if IsValidTag==0 and char_tag!="【null】":
                print("警告!存在未被定义的人物标识!")
                print("这一行将会被跳过!")
                print("为定义的人物标识为：")
                print(char_tag)
                print("该标识对应的完整句子为：")
                print(line)
                previous_char_tag=char_tag#save the current one to previous
                char_tag="【null】"#change char tag to null
        #end of tag identifier

        if line!=char_tag and char_tag!="【null】":
            for i in range(len(illegal_list)):
                if l.find(illegal_list[i])!=-1:
                    print("警告！不可用作文件名或renpy不支持的符号：")
                    print(illegal_list[i])
                    print("请修改后再使用本脚本！")
                    print("所在行的完整内容为：")
                    print(l)
            #生成renpy文件的部分         
            if char_tag!=previous_char_tag:
                file_rpy.write(char_tag +"：\n")
            ####then deal with dialog
            file_rpy.write(line + "\n")

file_rpy.close()
print("finished!")
