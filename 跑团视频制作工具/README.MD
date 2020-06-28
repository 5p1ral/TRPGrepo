# 【教程】如何使用Renpy制作跑团视频

本教程基于风空Offical制作的跑团视频教程（《我们不用很麻烦很累就可以做跑团视频》共两期，如今已因不明原因删除），再加上本人一定程度的魔改而成。经过了一段时间的打磨，我认为此教程已经足够便利，完全可以实现流水线作业，故分享出来仅供参考。本方法制作出来的视频可能精细度不会很高，但是效率绝对数一数二（甚至你只要有整理好的跑团记录就可以一天之内做完）。

<font color=red>**还等什么，抛弃肝帝生活，换我茂密头发！**</font>

### 准备工作

#### 素材与软件清单

Win10/Win7 64位系统

跑团记录

立绘、场景等素材

跑团记录着色器（[溯洄版](https://logpainter.kokona.tech/)/[陈末版](http://trpg.maddestroyer.xyz/logpainter)）[关于这两个版本的区别之后会提到，至于凤羽版的，现在我上不去了...]

[Python3.X](https://www.python.org/)

[终极自动脚本for renpy](https://wwe.lanzous.com/iOiPldw7muj)（基于风空原代码的魔改版）

[Renpy](https://www.renpy.org/)

录屏软件：[OBS](https://obsproject.com/)/[Bandicam](https://www.bandicam.cn/)（貌似Win10可以使用Win+G录屏，不过我不推荐）

文字转语音软件：[朗读女](http://www.443w.com/tts/)（在本版本非必须）

剪辑软件：PR/Vegas/会声会影（非必须）

编辑器：[Atom](https://atom.io/)/[Vscode](https://code.visualstudio.com/)（非必须）

[懒人包](https://cloud.189.cn/t/fUzq2qf2EbMr)（包含Renpy、Python3安装包、自动脚本、朗读女以及简单示例）

#### 配置python环境

*本部分为无编程基础的读者准备，认为自己能力足够的读者可以直接跳过，阅读脚本源码即可。*

首先百度python，进入官网（或者点击上文的超链接），不用管那些英文，直接找到Download图标以及下面的**python3.X.X**，点击进入下载页面。

![](https://cdn.jsdelivr.net/gh/Spiral111/Img-Hosting@master/20200621093825.png)

接着进入下载页面，你可能会很懵逼，不过不要紧，直接往下拉，直到出现如下界面。

![](https://cdn.jsdelivr.net/gh/Spiral111/Img-Hosting@master/20200621094102.png)

点击下载如图所示的exe文件，打开安装即可（一般来说只需要一直点击下一步[Next]）。

需要注意的是，需要把`Add Python 3.X to PATH`的选项勾选上（图是老图请别介意）

![](https://cdn.jsdelivr.net/gh/Spiral111/Img-Hosting@master/20200621095851.png)

接着打开命令行（cmd），输入`pip install baidu-aip`，等待安装完成。

###  正式开工

#### 跑团Log处理

##### 如何导出跑团Log

**使用骰娘**

现在的骰娘（塔骰和溯洄骰，惠惠骰我不知道）一般都支持`.log on`命令，只要再开团使输入该命令，在结团的时候输入`.log off`，骰娘便会帮你自动保存骰娘记录。

（此类方法简单，但是毕竟记录保存在骰娘服务端，建议一定要找服务稳定的骰娘*[比如本人的骰娘三天两头重启，肯定就不靠谱]*，否则记录就全没了）

**使用QQ的消息管理器**

*仅限PC*

打开腾讯QQ的界面，你会看到左下角有个按钮，单击之后显示出的页面左上角便是我们需要的消息管理器。

进入消息管理器之后，在群聊板块找到自己用于跑团的群聊，右键导出成txt格式即可。

*（此方法导出的聊天记录需要经过手动筛选与着色，且容易出现部分文字离奇消失的灵异事件）*

##### 着色

打开QQ跑团记录着色器（[溯洄版](https://logpainter.kokona.tech/)/[陈末版](http://trpg.maddestroyer.xyz/logpainter)）。

![](https://cdn.jsdelivr.net/gh/Spiral111/Img-Hosting@master/20200621101003.png)

将已经准备好的跑团记录全选复制到着色器的输入框内。

将显示时间调为OFF，点击处理按钮。

![](https://cdn.jsdelivr.net/gh/Spiral111/Img-Hosting@master/20200621101018.png)

在出现PC名字区域将同一个人的群名片调成一致。

最后的结果如下图所示。

![](https://cdn.jsdelivr.net/gh/Spiral111/Img-Hosting@master/20200621101036.png)

全选预览区域的文件，复制粘贴到word中即可。

##### 简单格式处理

*本方法适用于使用溯洄版Logpainter或者使用塔骰进行记录的读者（使用我的着色器则可直接跳过）*

将已经着色好的跑团记录复制进word文档（塔骰省略这一步）。

接着打开word的替换面板，在查找栏输入`<`，替换栏输入`^p【`，全部替换。

![](https://cdn.jsdelivr.net/gh/Spiral111/Img-Hosting@master/20200621102614.png)

接着，将查找栏换成`>`，输入栏换成`】^p`，再一次全部替换。

最后的结果如下图所示。

![](https://cdn.jsdelivr.net/gh/Spiral111/Img-Hosting@master/20200621102736.png)

最后全选word文档，粘贴到txt文本文档中。

**<font color=red>建议手动检查一遍最终的记录，以防其中出现英文字符或其他不能作为文件名的字符。</font>**

#### 自动脚本的配置

##### 初步配置

直接看源代码的注释就行了，具体我就不再讲解。

```python
import os
# 需要在命令行输入 pip install baidu-aip（什么？你不懂什么是命令行？建议百度。）
from aip import AipSpeech

# 在风空原代码的基础上加入了百度的语音合成SDK，实现终极自动化流水线

voice_flag=1 # 语音合成开关 1为开启 0为关闭 网速慢的建议关闭

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
char_list=["【GM】","【黑桃3】","【黑桃6】","【梅花7】","【梅花4】"]

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
    'pit': 5,
    },
    {
    'vol': 5,
    'per': 1,
    'pit': 3,
    },
    {
    'vol': 5,
    'per': 0,
    'pit': 7,
    },
    {
    'vol': 5,
    'per': 3,
    'pit': 8,
    },
    {
    'vol': 5,
    'per': 4,
    'pit': 6,
    },
    ]

#立绘x的自定义显示宽度，顺序请与上面的char_list保持一致，单位为像素
char_x=["500","400", "400", "400", "400"]

#立绘y的自定义显示高度，顺序请与上面的char_list保持一致，单位为像素
char_y=["800","700", "700", "700", "700"]

#每个角色立绘位置。顺序请与上面的char_list保持一致
location_list=["left","right", "right", "right", "right"]

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
```

##### 运行脚本

将处理好的跑团记录命名为`log.txt`，双击脚本运行。

运行时请耐心等待，只要窗口没有消失就说明还在运行。

如果窗口上出现`finish!`则表示已经运行完成，如果出现其他文字则表示出现了问题，可以按照提示对跑团记录进行修改。

运行结束后根目录将会出现一个`script.rpy`文件以及一个`voice`文件夹。

*风空的原代码并不会自动生成语音，文件夹内放置的将会是拆分的文字，可通过朗读女将其批量转换成语音。*

#### Renpy的配置

##### 新建项目与初始化

下载好renpy，打开之后应该是这个界面。

![](https://cdn.jsdelivr.net/gh/Spiral111/Img-Hosting@master/20200621102036.png)

点击创建新工程，按照提示一步步来。

打开项目根目录的`game`文件夹。

将之前生成的`script.rpy`和`voice`文件夹粘贴进去。

新建`image`文件夹，将准备好的立绘按角色命好名（例如`【GM】.jpg`）、和场景一起粘贴到`image`文件夹。

##### 替换字体、 隐藏按钮与自动播放

**替换字体**

由于Renpy原生的字体对于中文的支持不是一般的差，所以我建议更换字体以获得更好的体验。

将你想要替换的字体文件粘贴到项目根目录的`game`文件夹下。

用记事本打开`gui.rpy`

```python
## 用于游戏内文本的字体。
define gui.text_font = "SourceHanSans-Light-Lite.ttf"

## 用于角色名称的字体。
define gui.name_text_font = "SourceHanSans-Light-Lite.ttf"
```
找到这一段语句，将其中的`SourceHanSans-Light-Lite.ttf`替换成你所要替换的字体即可

**隐藏按钮**

用记事本打开`gui.rpy`

```python
            textbutton _("回退") action Rollback()
            textbutton _("历史") action ShowMenu('history')
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("保存") action ShowMenu('save')
            textbutton _("快存") action QuickSave()
            textbutton _("快读") action QuickLoad()
            textbutton _("设置") action ShowMenu('preferences')
```
找到这些语句，在这些语句最前面加上`#`即可将其注释掉

**自动播放**

打开软件根目录下的`\renpy\common\00keymap.rpy`

```python
toggle_afm = ['z'],
```
修改括号内的字母即可修改对应的自动播放快捷键。

##### 简单的语法

假设有一个叫`bg room`的背景图片，想要让他显示出来，就要在`script.rpy`里编辑，在对应的位置输入

```python
scene bg room
```

切换场景时使用的也是此语句。

#### 录制与后期处理

打开Renpy，启动工程，进入游戏界面，暂时不动。

![](https://i.loli.net/2020/06/21/5qE9NSOKVxRTt2A.png)

打开录屏软件，调整好后再回到Renpy生成的游戏界面。

![](https://i.loli.net/2020/06/21/YaLBhcQJMA6t9GX.png)

开始游戏，在**英文输入法**状态下按下自动播放快捷键，耐心等待播放完成。

之后可以用剪辑软件对录制的视频进行一定程度的后期处理，当然也可不处理。

### 结语

以上便是我制作跑团视频的方法，再次申明，该方法不是最好的方法，只是为了效率牺牲了精细度。

~~（话说感觉专栏有点说不清楚，以后如果有空或许会出个视频）~~

从总体上来说，跑团视频制作并没有难度，现在各种教程都有，千万不要被开头的门槛吓退。

**<font color=red>记住，内容产出重要的是内容，制作的工具并没有优劣之分。</font>**

如果有疑问欢迎在评论区（指B站评论区）留言，祝各位都能将自己有趣的跑团经历做成视频，分享给别人。

**别人的Renpy跑团视频制作教程：**https://www.bilibili.com/video/BV1KT4y157Xr

**使用此方法制作的跑团视频：**https://www.bilibili.com/video/BV1sa4y1Y755

#### 此方法的优点

**没有版权问题：**Renpy、跑团记录着色器均采用MIT协议开源（当然如果你自己要用盗版美术素材我也没办法）

**模块化、流水线作业：**跑团记录的处理、文字转语音、语音转视频都是分工进行的，即使中间有一步出现了错误也可以快速纠正。

#### 此方法的缺点

**配音不够丰富：**经我改进后的自动脚本使用的是百度的文字转语音SDK（别问我为什么不用其他的，其他的要钱）其他所以只有4个音色，就算是分成高低两个声调，也只能够支撑八个角色。解决的方法关闭脚本的文字转语音开关，使用朗读女以获得更佳体验。

**不经过后期处理没有特殊效果：**比如战斗轮如果想要有血条的话就得自己动手做了。

**需要安装python以及baidu-aip模块：**万事开头难，有多少人懒得去做第一步，这我也没办法。

#### 其他方法的简单参考

**相关视频：**https://www.bilibili.com/video/BV1KT4y157Xr

##### 视频剪辑软件制作

这个方法其实没有什么好说的，大部分UP主属于纯手工制作，主要就是技术问题。你技术好，操作熟练的话效率就会高，技术不好的话可能一个月都搞不出来一期（不要认为这种速度很快，大部分up拖更的原因其实都不是因为技术问题，而是现实忙碌/面团需要耗费精力整理记录/想要更好的表现形式，如果你现实很闲的话这种效率真的不快）。至于用什么剪辑软件纯属个人喜好，没有必要深究。

**优点：**如果本身熟悉剪辑软件的话没有其他的学习成本、可以在制作过程中拥有更好的表现形式。

**缺点：**对低技术力人员不够友好、某些软件吃内存吃得太死，对低配电脑也不友好。

**相关视频：**https://www.bilibili.com/video/BV19t411775m

##### PPT制作

其实PPT制作法我的感觉是和PR制作法没有什么区别的，基本上也都是纯手工制作，不过会比PR友好一些（毕竟PPT不会吃你的内存，更不会突然就给你来个无法响应），学习成本也相对较低（会PPT的总比会PR的人多吧），算是对新手较为友好的方法了。

**优点：**学习成本较低，操作相对于剪辑软件有一定的简化。

**缺点：**惊了，我居然找不到缺点。

**相关视频：**https://www.bilibili.com/video/BV1it411Z7oU

##### 无双AVG引擎

*由于我没有进该引擎的QQ群，也没有实操过该软件，所以我只能通过视频中的内容进行一些评价，可靠度可能不是很高*

**优点：**与Renpy其实很类似，不过大部分语法都为中文，对国人友好一些。

**缺点：**up做的教程看得我头疼。

**相关视频：**https://www.bilibili.com/video/BV1cb411J7Jj

##### 橙光游戏

**优点：**学习成本低，操作也很简单。

**缺点：**橙光的美术素材实际上不能用于制作视频（用来做跑团视频算是擦边球）

**相关视频：**https://www.bilibili.com/video/BV1BW411J7zP

##### 活字引擎

现版本我不推荐使用，不够成熟。

**优点：**轻量化语法、原作者在线解答。

**缺点：**预加载资源导致开启缓慢、内置字体导致无法自定义、在线转语音无缓存导致调试困难。

**相关视频：**https://www.bilibili.com/video/BV1Ek4y1r7vw