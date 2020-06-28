import os
# 需要在命令行输入 pip install baidu-aip（什么？你不懂什么是命令行？建议百度。）
from aip import AipSpeech

# 在风空原代码的基础上加入了百度的语音合成SDK，实现终极自动化流水线
voice_flag=1 # 语音合成开关 1为开启 0为关闭
# 你的 APPID AK SK 建议自己去百度云平台申请，当然用我的也没关系（但保不准哪天我就关掉了）
APP_ID = '20355681'
API_KEY = '6gI2piIaG0DzRMTgDE6XN4S6'
SECRET_KEY = 'yARGOWrKDHDSDIkkD1ngFNKvjvhvBWdX'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 打开输入文件，整理后的log。log.txt需要是utf-8编码并且和自动脚本for renpy.py放在一个目录下面
fobj = open('log.txt',mode='r',encoding='utf-8')
# 创建用于复制进renpy的输出文件
file_rpy = open('script.rpy',mode='w',encoding='utf-8')


# 列出log.txt里所有出现的kp、骰子、pl及npc的角色名字
char_list=["【Kira】","【博良】","【雨声】","【安德森】","【墨非白】"]

# 列出每个角色对应的音色，顺序请与上面的char_list保持一致
'''
spd：语速，取值0-9，默认为5中语速
pit：音调，取值0-9，默认为5中语调
vol：音量，取值0-15，默认为5中音量
per：发音人选择, 0为女声，1为男声，3为感情男，4为感情女，默认为0
'''
char_voice_list=[ 
	{
    'vol': 5,
    'per': 3,
    'pit': 6,
    },
    {
    'vol': 5,
    'per': 3,
    'pit': 4,
    },
    {
    'vol': 5,
    'per': 4,
    'pit': 7,
    },
    {
    'vol': 5,
    'per': 3,
    'pit': 5,
    },
    {
    'vol': 5,
    'per': 4,
    'pit': 6,
    },
    ]

#立绘x的自定义显示宽度，顺序请与上面的char_list保持一致，单位为像素
char_x=["500","500", "500", "500", "500", "500"]

#立绘y的自定义显示高度，顺序请与上面的char_list保持一致，单位为像素
char_y=["800","800", "800", "800", "800", "800"]

#每个角色立绘位置。顺序请与上面的char_list保持一致
location_list=["left","right", "right", "right", "right", "right"]

#骰子的名字。注意骰子的名字同样应该在char_list出现
dice_tag="【bot-drsink】"

#是否自动处理骰子。1为自动，0为直接显示投掷发言那一行
dice_flag=1

#骰子音效文件名。如果选择自动处理骰子，需要设置以下部分
rolling_se="manydice.mp3"#投掷音效
suc_se="suc_se.mp3"#成功音效
crit_suc_se="crit_suc_se.mp3"#大成功音效
fail_se="fail_se.mp3"#失败音效
fumble_fail_se="fumble_fail_se.wav"#大失败音效


##################################################################以上为需要修改的部分
#set the initial value#tag初始化。不要改动
char_tag="【null】"
previous_char_tag="【null】"

#number of the voice files#全局语音编号。不要改动
global global_voice_num
global_voice_num=0

#声明全局变量
global rolling_text


def para_init():
    global rolling_text
    rolling_text=""

para_init()


#处理骰子
def rolling_identifier():
    global rolling_text

    
    if line[-3:]==" 成功":
        para_init()
        rolling_result=line[-3:]
        rolling_text1="\\n"+line[:len(line)-2-len(line.split(" ")[-2])-1]
        file_rpy.write("    play sound" +  " \"" + rolling_se + "\"\n")
        file_rpy.write("    " + char_tag + " \"" + rolling_text1 + "{size=+10} {/size}\"\n")
        

        para_init()
        rolling_text2=" "+line.split(" ")[-2]+" "+"{size=+10}{color=#32CD32}成功{/color}{/size}"
        file_rpy.write("    play sound" +  " \"" + suc_se + "\"\n")
        file_rpy.write("    " + char_tag + " \"" + rolling_text1+rolling_text2 + "\"\n")



    elif line[-3:]=="大成功":
        para_init()
        rolling_result=line[-3:]
        rolling_text1="\\n"+line[:len(line)-3-len(line.split(" ")[-2])-1]
        file_rpy.write("    play sound" +  " \"" + rolling_se + "\"\n")
        file_rpy.write("    " + char_tag + " \"" + rolling_text1 + "{size=+10} {/size}\"\n")
        


        para_init()
        rolling_text2=" "+line.split(" ")[-2]+" "+"{size=+10}{color=#FDFF00}大成功{/color}{/size}"
        file_rpy.write("    play sound" +  " \"" + crit_suc_se + "\"\n")
        file_rpy.write("    " + char_tag + " \"" + rolling_text1+rolling_text2 + "\"\n")        

    elif line[-5:]==" 普通成功":
        para_init()
        rolling_result=line[-5:]
        rolling_text1="\\n"+line[:len(line)-5-len(line.split(" ")[-2])-1]
        file_rpy.write("    play sound" +  " \"" + rolling_se + "\"\n")
        file_rpy.write("    " + char_tag + " \"" + rolling_text1 + "{size=+10} {/size}\"\n")        

        para_init()
        rolling_text2=" "+line.split(" ")[-2]+" "+"{size=+10}{color=#32CD32}普通成功{/color}{/size}"
        file_rpy.write("    play sound" +  " \"" + suc_se + "\"\n")
        file_rpy.write("    " + char_tag + " \"" + rolling_text1+rolling_text2 + "\"\n")    



        
    elif line[-5:]==" 困难成功":
        para_init()
        rolling_result=line[-5:]
        rolling_text1="\\n"+line[:len(line)-5-len(line.split(" ")[-2])-1]
        file_rpy.write("    play sound" +  " \"" + rolling_se + "\"\n")
        file_rpy.write("    " + char_tag + " \"" + rolling_text1 + "{size=+10} {/size}\"\n")        

        para_init()
        rolling_text2=" "+line.split(" ")[-2]+" "+"{size=+10}{color=#32CD32}困难成功{/color}{/size}"
        file_rpy.write("    play sound" +  " \"" + suc_se + "\"\n")
        file_rpy.write("    " + char_tag + " \"" + rolling_text1+rolling_text2 + "\"\n")  



    elif line[-5:]==" 极难成功":
        para_init()
        rolling_result=line[-5:]
        rolling_text1="\\n"+line[:len(line)-5-len(line.split(" ")[-2])-1]
        file_rpy.write("    play sound" +  " \"" + rolling_se + "\"\n")
        file_rpy.write("    " + char_tag + " \"" + rolling_text1 + "{size=+10} {/size}\"\n")        

        para_init()
        rolling_text2=" "+line.split(" ")[-2]+" "+"{size=+10}{color=#32CD32}极难成功{/color}{/size}"
        file_rpy.write("    play sound" +  " \"" + suc_se + "\"\n")
        file_rpy.write("    " + char_tag + " \"" + rolling_text1+rolling_text2 + "\"\n")  


    elif line[-3:]==" 失败":
        para_init()
        rolling_result=line[-3:]
        rolling_text1="\\n"+line[:len(line)-2-len(line.split(" ")[-2])-1]
        file_rpy.write("    play sound" +  " \"" + rolling_se + "\"\n")
        file_rpy.write("    " + char_tag + " \"" + rolling_text1 + "{size=+10} {/size}\"\n")        

        para_init()
        rolling_text2=" "+line.split(" ")[-2]+" "+"{size=+10}{color=#FF0000}失败{/color}{/size}"
        file_rpy.write("    play sound" +  " \"" + fail_se + "\"\n")
        file_rpy.write("    " + char_tag + " \"" + rolling_text1+rolling_text2 + "\"\n")  


    elif line[-3:]=="大失败":
        para_init()
        rolling_result=line[-3:]
        rolling_text1="\\n"+line[:len(line)-3-len(line.split(" ")[-2])-1]
        file_rpy.write("    play sound" +  " \"" + rolling_se + "\"\n")
        file_rpy.write("    " + char_tag + " \"" + rolling_text1 + "{size=+10} {/size}\"\n")        

        para_init()
        rolling_text2=" "+line.split(" ")[-2]+" "+"{size=+10}{color=#FF0000}大失败{/color}{/size}"
        file_rpy.write("    play sound" +  " \"" + fumble_fail_se + "\"\n")
        file_rpy.write("    " + char_tag + " \"" + rolling_text1+rolling_text2 + "\"\n")  

    else:
        print("骰子的结果不是成功等级!!!直接播放骰子音效并显示整行!")
        print("这一行的内容为： "+line)
        file_rpy.write("    play sound" +  " \"" + rolling_se + "\"\n")
        file_rpy.write("    " + char_tag + " \"" + line + "{size=+10} {/size}\"\n")
        para_init()
    para_init()

#用于存放log.txt中不应该出现的字符。不要改动
illegal_list=["?",":", "<", ">", "*", "\"", "/", "\\", "[", "]"]


#在当前目录生成用于存放txt的文件夹。不要改动
if not os.path.exists("voice"): os.makedirs("voice")
for i in range(len(char_list)):
    if not os.path.exists("voice\\"+char_list[i]):
        os.makedirs("voice\\"+char_list[i])

#写入renpy的头文件，定义角色
for i in range(0, len(char_list)):
	file_rpy.write("define " + char_list[i] + " = Character(\"" + char_list[i] + "\")\n")


#写入renpy的头文件，缩放角色立绘
for i in range(0, len(char_list)):
	file_rpy.write("image " + char_list[i] + "_resized" + " = im.Scale(\"" + char_list[i] + ".png\"" + ", "+char_x[i]+","+ char_y[i]+")\n")
file_rpy.write("\n")

file_rpy.write("label start:\n\n")

file_rpy.write("    scene bg room\n\n")

for l in fobj:
    line=l.strip();#line is the content of current line
    if len(line)>0:#only deal with non empty lines
        if line[0]=="【":#which means that line is a tag line
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

#####dice
        if line!=char_tag:#which means line is a content line
            if char_tag==dice_tag:#这个标识后面跟着的一行是投掷内容，不需要挂语音
                #####first, turn off any halves
                if dice_flag==1:
                    file_rpy.write("    hide " + previous_char_tag + "\n\n")
                    rolling_identifier()
                else:
                    file_rpy.write("    " + char_tag + " \"" + line + "\"\n")

#####

#####PC and KP
            elif char_tag!="【null】":
                for i in range(len(illegal_list)):
                    if l.find(illegal_list[i])!=-1:
                        print("警告！不可用作文件名或renpy不支持的符号：")
                        print(illegal_list[i])
                        print("请修改后再使用本脚本！")
                        print("所在行的完整内容为：")
                        print(l)
                #语音txt文件拆分部分
                global_voice_num=global_voice_num+1
                if voice_flag:
                    file_name="voice\\"+char_tag+"\\"+str(global_voice_num).zfill(3)+char_tag+" "+line+".mp3"#mp3文件的路径
                    file_temp = open(file_name,mode='wb')
                    file_temp.write(client.synthesis(line,'zh', 1,char_voice_list[char_list.index(char_tag)]))
                else:
                    file_name="voice\\"+char_tag+"\\"+str(global_voice_num).zfill(3)+char_tag+" "+line+".txt"#txt文件的路径
                    file_temp = open(file_name,mode='w',encoding='utf-8')
                    file_temp.write(line)#写入文件
#               file_batch.write(batch_line)				
                #生成renpy文件的部分         
                if char_tag!=previous_char_tag and previous_char_tag!="【null】":#first, clear halves
                    file_rpy.write("    hide " + previous_char_tag +"_resized" + "\n\n")
                if char_tag!=previous_char_tag:
                    file_rpy.write("    show " + char_tag +"_resized"+ " at "+location_list[char_list.index(char_tag)]+"\n")
                ####then deal with dialog
                file_name_voice=char_tag+"/"+str(global_voice_num).zfill(3)+char_tag+" "+line+".mp3"#语音文件的路径
                file_rpy.write("    voice \"../voice/" + file_name_voice + "\"\n")
                file_rpy.write("    " + char_tag + " \"" + line + "\"\n")

file_rpy.write("    return")

file_temp.close()   
file_rpy.close()
print("finished!")
os.system("pause")
