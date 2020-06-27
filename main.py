import requests
from bs4 import BeautifulSoup
import random
import time
import ctypes

from translate import Translator

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12
path = "words.txt"
senPath = "sentenses.txt"

FOREGROUND_DARKBLUE = 0x01  # 暗蓝色
FOREGROUND_DARKGREEN = 0x02  # 暗绿色
FOREGROUND_DARKSKYBLUE = 0x03  # 暗天蓝色
FOREGROUND_DARKRED = 0x04  # 暗红色
FOREGROUND_DARKPINK = 0x05  # 暗粉红色
FOREGROUND_DARKYELLOW = 0x06  # 暗黄色
FOREGROUND_DARKWHITE = 0x07  # 暗白色
FOREGROUND_DARKGRAY = 0x08  # 暗灰色
FOREGROUND_BLUE = 0x09  # 蓝色
FOREGROUND_GREEN = 0x0a  # 绿色
FOREGROUND_SKYBLUE = 0x0b  # 天蓝色
FOREGROUND_RED = 0x0c  # 红色
FOREGROUND_PINK = 0x0d  # 粉红色
FOREGROUND_YELLOW = 0x0e  # 黄色
FOREGROUND_WHITE = 0x0f  # 白色

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool


def resetColor():
    set_cmd_text_color(FOREGROUND_DARKWHITE)


def cprint(mess, color):
    color_dict = {'暗蓝色': FOREGROUND_DARKBLUE,
                  '暗绿色': FOREGROUND_DARKGREEN,
                  '暗天蓝色': FOREGROUND_DARKSKYBLUE,
                  '暗红色': FOREGROUND_DARKRED,
                  '暗粉红色': FOREGROUND_DARKPINK,
                  '暗黄色': FOREGROUND_DARKYELLOW,
                  '暗白色': FOREGROUND_DARKWHITE,
                  '暗灰色': FOREGROUND_DARKGRAY,
                  '蓝色': FOREGROUND_BLUE,
                  '绿色': FOREGROUND_GREEN,
                  '天蓝色': FOREGROUND_SKYBLUE,
                  '红色': FOREGROUND_RED,
                  '粉红色': FOREGROUND_PINK,
                  '黄色': FOREGROUND_YELLOW,
                  '白色': FOREGROUND_WHITE
                  }
    set_cmd_text_color(color_dict[color])
    print(mess)
    resetColor()


def writeFile(path, text):
    with open(path, 'a+') as f:
        f.write(text + '\n')


def writeFileS(path, text):
    with open(path, 'a+') as f:
        f.write(text + '\n')


def main():
    color_list = ['暗绿色', '暗天蓝色', '暗红色', '暗粉红色', '暗黄色', '暗白色', \
                  '绿色', '天蓝色', '红色', '粉红色', '黄色', '白色']

    print('#' * 60)
    print('MingliangXu\'s dictionary:')
    print('#' * 60 + '\n')

    word = input("Enter a word/sentence:  \n")

    while word != 'q':
        try:
            r = requests.get(url='http://dict.youdao.com/w/%s/#keyfrom=dict2.top' % word)
            soup = BeautifulSoup(r.text, "lxml")
            s = soup.find(class_='trans-container')('ul')[0]('li')
            random.shuffle(color_list)
            writeFile(path, word)
            for item in s:
                if item.text:
                    cprint(item.text, color_list[0])
                    writeFile(path, item.text)
            writeFile(path, '\n')
            print('=' * 40 + '\n')
        except Exception:
            translator = Translator(from_lang="english", to_lang="chinese")
            translation = translator.translate(word)
            cprint(translation, color_list[0])
            writeFileS(senPath, word)
            writeFileS(senPath, translation)
            writeFileS(senPath, '\n')
            print('=' * 40 + '\n')
        finally:
            word = input("Enter a word/sentence:  \n")


if __name__ == "__main__":
    main()
