# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date:
# @Last Modified by: CPS
# @Last Modified time: 2021-08-13 22:12:57.599852
# @file_path "D:\CPS\IDE\sublime Text\sublime_text_4113.21_win64_patched\sublime_text\Data\Packages\testt_switch_language"
# @Filename "testt_switch_language.py"
# @Description: 每次激活sublime编辑器的时候，自动切换成英文输入，（需要添加一个英文语言，相当于直接切换成英文语言环境）
#


import sublime, sublime_plugin
import os, sys

if sys.platform != "win32":
    exit()

if int(sublime.version()) < 3176:
    raise ImportWarning("本插件不支持当前版本，请使用大于等于3176的sublime Text")


# 为了引入插件目录下的 pywin32模块 添加插件目录到环境变量
sys.path.append(os.path.join(sublime.packages_path(), __package__))

# 引入模块
import Pywin32.setup
from win32con import WM_INPUTLANGCHANGEREQUEST
import win32api, win32gui

# 设置语言
LANG = {"zh": 0x0804, "en": 0x0409}


def change_language(lang: str = "en") -> bool:

    global LANG
    HWND = win32gui.GetForegroundWindow()
    LANGUAGE_CODE = LANG[lang.lower()] or LANG["en"]

    res = win32api.PostMessage(HWND, WM_INPUTLANGCHANGEREQUEST, 0, LANGUAGE_CODE)
    return res


def check_system_language() -> str:
    """
    @Description 获取当前系统的语言
    """
    import ctypes

    dll_h = ctypes.windll.kernel32

    res = hex(dll_h.GetSystemDefaultUILanguage())
    return res


class CpsSwicthLanguageEventer(sublime_plugin.EventListener):
    def on_activated_async(self, view):
        """
        @Description 每当视图切换，都执行切换一次语言
        """
        change_language("en")


class CpsSwitchLanguageCommand(sublime_plugin.TextCommand):
    def run(self, view):
        change_language("en")
