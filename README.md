## 简介|Introductions

<div>
    <img flex="left" src="https://img.shields.io/badge/python-%3E%3D3.3.0-3776AB"/>
    <img flex="left" src="https://img.shields.io/badge/Sublime%20Text-FF9800?style=flat&logo=Sublime%20Text&logoColor=white"/>
    <img flex="left" src="https://img.shields.io/github/license/caoxiemeihao/electron-vite-vue?style=flat"/>
</div>

日常编写代码的环境中，一码代码一边查资料，一边聊天一边码代码：`英文输入`>`中文输入`>`英文输入`>`...`这样的场景来来回回，每次切换场景总会要手动切换一下输入法，非常不优雅。

首先类似功能的插件网上已经存在， 非本人原创，但是代码稍有改动，更符合本人自己维护的习惯，打包成本项目代码。

> - 本系列插件均为团队内部定制打造，不对外更新负责，
> - 2023年了，前端coder建议采用**VSCode**。



## 功能|Feature

![image-20221113235730390](/screenshot/sublimeTextPlugs/cps-auto-switch-language/cps-auto-switch-language11.gif)

![cps-auto-switch-language1](http://localhost:45462/image/cps-auto-switch-language1.gif)

![image-20221113235730390](/screenshot/sublimeTextPlugs/cps-auto-switch-language/cps-auto-switch-language12.gif)

![cps-auto-switch-language2](http://localhost:45462/image/cps-auto-switch-language2.gif)



## 安装|Install

```bash
# 打开 SublimeText3的插件目录，并在该目录下打开shell
菜单栏 > Preferences > Browse Packages...

# 在插件目录运行shell，下载插件
# gitee
git clone --depth=1 git@gitee.com:Capsion-ST-PLugins/auto-switch-language.git auto-switch-language
# or github
git clone --depth=1 git@github.com:Capsion-ST-PLugins/auto-switch-language.git auto-switch-language

# 系统中添加英文输入环境

```



## 使用|Usage

每次激活Sublime Text时，系统自动切换为英文输入环境（不是输入法）。因为切换的不是输入法，是系统语言环境，所以使用前需要添加一个英文的语言环境



## 插件配置|Configure

![image-20230413160541763](http://localhost:45462/image/image-20230413160541763.png)

因为在sublime的`on_activated_async`钩子（编辑器被激活时的钩子）时，触发一个切换语言的系统调用，将当前系统语言切换成英语，所以本插件的前置

系统设置 > 语言页面 中可以看到除了`中文（简体，中国）`，还带了一个`英语（美国）`，这个`英语（美国）`就是一个纯英文的系统语言。

![image-20221113235730390](http://localhost:45462/image/image-20221113235730390.png)![image-20221113235811245](/screenshot/sublimeTextPlugs/cps-auto-switch-language/image-20221113235811245.png)





## 项目架构|Tree

```ini
DIR:cps-auto-switch-language                             # 
   |-- .sublime/                                         # 
   |   `-- Context.sublime-menu                          # 
   |-- Pywin32/                                          # 「Pywin32」核心依赖：离线版的Pywin32
   |-- screenshot/                                       # 「screenshot」
   |   |-- 使用演示2.gif                                   # 
   |   |-- 使用演示1.gif                                   # 
   |   |-- image-20221113235811245.png                   # 
   |   `-- image-20221113235730390.png                   # 
   |-- README.md                                         # 
   |-- main.py                                           # 核心代码
   `-- .gitignore                                        # 

```



## 联系方式|Contact

- **373704015 (qq、wechat、email)**
