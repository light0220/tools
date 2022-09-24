# -*- encoding: utf-8 -*-
'''
@File    :   喵了个喵.py
@Author  :   北极星光 
@Contact :   light22@126.com
'''
import random


class MiaoMiao:
    space_l = [[], [], [], [], [], [], []]

    def __init__(self) -> None:
        self.generate()
        self.check()

    def generate(self):
        '''
        生成牌局'''

        cat_pool = ['白猫', '黑猫', '黄猫', '蓝猫', '花猫', '粉猫', '大猫', '小猫']

        self.l1 = [random.choices(cat_pool) for i in range(9)]
        self.l2 = [random.choices(cat_pool) for i in range(9)]
        self.l3 = [random.choices(cat_pool) for i in range(9)]
        self.l4 = [random.choices(cat_pool) for i in range(9)]
        self.l5 = [random.choices(cat_pool) for i in range(9)]
        self.l6 = [random.choices(cat_pool) for i in range(9)]
        self.l7 = [random.choices(cat_pool) for i in range(9)]
        self.l8 = [random.choices(cat_pool) for i in range(9)]
        self.l9 = [random.choices(cat_pool) for i in range(9)]

    def check(self):
        '''判断：如果出现无解的情况则重新洗牌'''
        x = True
        while x:
            x = False
            sum_l = self.l1 + self.l2 + self.l3 + self.l4 + \
                self.l5 + self.l6 + self.l7 + self.l8 + self.l9
            for i in sum_l:
                if sum_l.count(i) % 3 != 0:
                    x = True
                    self.generate()
                    break

    def select(self, l: list):
        if len(l) == 0:
            print('当前位置已经没有猫了，请重新选择！')
            return
        tmp_l = l.pop()
        if tmp_l not in self.space_l:
            self.space_l[self.space_l.index([])] = tmp_l
        else:
            self.space_l.insert(self.space_l.index(tmp_l), tmp_l)
            self.space_l.pop()
        if self.space_l.count(tmp_l) == 3:
            for i in range(3):
                self.space_l.remove(tmp_l)
                self.space_l.append([])

    def play(self):
        while True:
            lay = f'''
            欢迎游玩《喵了个喵》
            ====================
            1.{self.l1[-1] if len(self.l1) != 0 else '[      ]'}\t 2.{self.l2[-1] if len(self.l2) != 0 else '[      ]'}\t 3.{self.l3[-1] if len(self.l3) != 0 else '[      ]'}
            4.{self.l4[-1] if len(self.l4) != 0 else '[      ]'}\t 5.{self.l5[-1] if len(self.l5) != 0 else '[      ]'}\t 6.{self.l6[-1] if len(self.l6) != 0 else '[      ]'}
            7.{self.l7[-1] if len(self.l7) != 0 else '[      ]'}\t 8.{self.l8[-1] if len(self.l8) != 0 else '[      ]'}\t 9.{self.l9[-1] if len(self.l9) != 0 else '[      ]'}
            ====================
            空槽位：{self.space_l}
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
    miao = MiaoMiao()
    miao.play()
