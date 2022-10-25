#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
作  者    : 孙振光 light22@126.com
创建时间  : 2022-08-22 20:55:26
最后编辑  : 2022-10-22 19:44:26
编辑人    : 孙振光
'''
import PySimpleGUI as sg

layout = [
    [sg.Frame('请选择功能', [
        [sg.FileBrowse(button_text='选择文件', target='-IP-', size=9),
         sg.In(key='-IP-'), sg.B('复制文件路径', key='-CP-', size=12)],
        [sg.FolderBrowse(button_text='选择文件夹', target='-IF-', size=9),
         sg.In(key='-IF-'), sg.B('复制文件夹路径', key='-CF-', size=12)],
        [sg.ColorChooserButton(button_text='选择颜色', target='-IC-', size=9),
         sg.In(key='-IC-'), sg.B('复制颜色代码', key='-CC-', size=12)],
        [sg.CalendarButton(button_text='选择日期', target='-ID-', size=9, format='%Y-%m-%d'),
         sg.In(key='-ID-'), sg.B('复制日期', key='-CD-', size=12)],
    ])],
    [sg.T('by:', font=('黑体', 12), text_color='red', size=48,
          justification='right'), sg.T('北极星光', font=('黑体', 12), text_color='red')],
    [sg.T('E-mail:', font=('黑体', 12), text_color='red', size=48, justification='right'),
     sg.T('light22@126.com', font=('黑体', 12), text_color='red')]
]
window = sg.Window('常用代码复制器', layout)
while True:
    event, values = window.read()
    if event == None:
        break
    if event == '-CP-':
        sg.popup('代码已选中，请按<Ctrl+C>复制', title='提示')
        window['-IP-'].SetFocus()
        window['-IP-'].update(select=True)
    if event == '-CF-':
        sg.popup('代码已选中，请按<Ctrl+C>复制', title='提示')
        window['-IF-'].SetFocus()
        window['-IF-'].update(select=True)
    if event == '-CC-':
        sg.popup('代码已选中，请按<Ctrl+C>复制', title='提示')
        window['-IC-'].SetFocus()
        window['-IC-'].update(select=True)
    if event == '-CD-':
        sg.popup('代码已选中，请按<Ctrl+C>复制', title='提示')
        window['-ID-'].SetFocus()
        window['-ID-'].update(select=True)
window.close()
