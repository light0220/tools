#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
作  者    : 孙振光 light22@126.com
创建时间  : 2022-10-16 17:50:12
最后编辑  : 2022-10-16 18:32:19
编辑人    : 孙振光
'''
from 喵了个喵 import MiaoMiao
from colorama import Fore, Back, Style
import random


class ColorMiao(MiaoMiao):
    def __init__(self) -> None:
        super().__init__()

    def generate(self):
        '''
        生成牌局'''

        cat_pool = [f'{Fore.LIGHTCYAN_EX}白猫{Fore.RESET}', f'{Fore.BLACK}黑猫{Fore.RESET}', f'{Fore.YELLOW}黄猫{Fore.RESET}', f'{Fore.BLUE}蓝猫{Fore.RESET}',
                    f'{Fore.LIGHTGREEN_EX}花猫{Fore.RESET}', f'{Fore.MAGENTA}粉猫{Fore.RESET}', f'{Fore.RED}大猫{Fore.RESET}', f'{Fore.CYAN}小猫{Fore.RESET}']

        self.l1 = [random.choices(cat_pool) for i in range(9)]
        self.l2 = [random.choices(cat_pool) for i in range(9)]
        self.l3 = [random.choices(cat_pool) for i in range(9)]
        self.l4 = [random.choices(cat_pool) for i in range(9)]
        self.l5 = [random.choices(cat_pool) for i in range(9)]
        self.l6 = [random.choices(cat_pool) for i in range(9)]
        self.l7 = [random.choices(cat_pool) for i in range(9)]
        self.l8 = [random.choices(cat_pool) for i in range(9)]
        self.l9 = [random.choices(cat_pool) for i in range(9)]

    def play(self):
        while True:
            lay = f'''
            欢迎游玩《喵了个喵》
            ====================
            1.[{self.l1[-1][0] if len(self.l1) != 0 else '    '}]\t 2.[{self.l2[-1][0] if len(self.l2) != 0 else '    '}]\t 3.[{self.l3[-1][0] if len(self.l3) != 0 else '    '}]
            4.[{self.l4[-1][0] if len(self.l4) != 0 else '    '}]\t 5.[{self.l5[-1][0] if len(self.l5) != 0 else '    '}]\t 6.[{self.l6[-1][0] if len(self.l6) != 0 else '    '}]
            7.[{self.l7[-1][0] if len(self.l7) != 0 else '    '}]\t 8.[{self.l8[-1][0] if len(self.l8) != 0 else '    '}]\t 9.[{self.l9[-1][0] if len(self.l9) != 0 else '    '}]
            ====================
            空槽位：[{self.space_l[0][0] if len(self.space_l[0]) != 0 else '    '}] [{self.space_l[1][0] if len(self.space_l[1]) != 0 else '    '}] [{self.space_l[2][0] if len(self.space_l[2]) != 0 else '    '}] [{self.space_l[3][0] if len(self.space_l[3]) != 0 else '    '}] [{self.space_l[4][0] if len(self.space_l[4]) != 0 else '    '}] [{self.space_l[5][0] if len(self.space_l[5]) != 0 else '    '}] [{self.space_l[6][0] if len(self.space_l[6]) != 0 else '    '}]
            ====================
            请输入1~9将相应的猫放入空槽位：
            '''
            ch = input(lay)
            if ch == '1':
                self.select(self.l1)
            elif ch == '2':
                self.select(self.l2)
            elif ch == '3':
                self.select(self.l3)
            elif ch == '4':
                self.select(self.l4)
            elif ch == '5':
                self.select(self.l5)
            elif ch == '6':
                self.select(self.l6)
            elif ch == '7':
                self.select(self.l7)
            elif ch == '8':
                self.select(self.l8)
            elif ch == '9':
                self.select(self.l9)
            else:
                print('输入有误，请重新输入')

            if [] not in self.space_l:
                print('游戏结束！！！')
                break
            if len(self.l1) + len(self.l2)+len(self.l3)+len(self.l4)+len(self.l5)+len(self.l6)+len(self.l7)+len(self.l8)+len(self.l9) == 0:
                print('恭喜通关！！！')
                break


if __name__ == '__main__':
    miao = ColorMiao()
    miao.play()
