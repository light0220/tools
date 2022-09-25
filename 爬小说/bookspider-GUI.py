import requests,os,PySimpleGUI as sg,threading
from lxml import etree  #数据转换

class BookSpider:
    def __init__(self,url) -> None:
        self.url = url

    # 定义获取小说列表模块
    def get_booklist(self):
        #字典  请求头/伪装头  网景  火狐
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
        }

        #发起访问，获取数据
        response = requests.get(url=self.url,headers=self.headers)
        #print(response.text)

        #数据转换  xpath解析数据  RE
        data = etree.HTML(response.text)
        # # #
        #拿到所有的小说详情地址  //   @ 定位符  指定条件   <Element div at 0x212bb28ac88>
        book_info_list = data.xpath('//div[@class="item"]')
        # print(book_info_list)
        self.book_dict = {}
        for book_info in book_info_list:
            #解析出path
            page_id = book_info.xpath('div[@class="image"]/a/@href')[0]
            #print(page_id)
            #将每一部小说的路径拼接到主域名下面
            url = self.url[0:19] + page_id
            #print(url)
            #获取详情页面
            response = requests.get(url=url,headers=self.headers)
            info_page = etree.HTML(response.text)
            download_url = info_page.xpath('//div[@class="readbtn"]/a/@href')[2]
            # print(download_url)
            #拼接下载的链接
            download_url = url[0:19] + download_url
            #print(download_url)
            #拿到小说得名字
            book_name = download_url.split('=')[2]
            #print(book_name)
            self.book_dict[book_name] = download_url
        return self.book_dict

    # 定义写入模块
    def write_txt(self,book_path,book_name):
        self.path = book_path
        os.makedirs(self.path,exist_ok=True)
        #对下载的链接进行访问
        book_txt = requests.get(url=self.book_dict[book_name],headers=self.headers)
        #文件I/O读写
        with open(f'{self.path}/{book_name}.txt','w',encoding='utf-8') as f:
            f.write(book_txt.text)
        print('《%s》 下载完成！'%book_name)
    
    # 定义主程序
    def main(self,download_list,book_path):
        for book_name in self.book_dict:
            if book_name in download_list:
                self.write_txt(book_path,book_name)

# 定义图形界面
class WindowsGUI:
    def __init__(self,book_dict) -> None:
        self.book_dict = book_dict

    def gui(self):
        layout1 = [
            [sg.Listbox([i for i in self.book_dict],size=(50,15),key='-LISTBOX-',select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE)]
        ]
        layout2 = [
            [sg.ML(default_text='正在下载所选书籍，请稍等···\n',size=(50,15),disabled=True,reroute_stdout=True,autoscroll=True)]
        ]
        layout3 = [
            [sg.In(key='-FOLDER-',size=43),sg.FolderBrowse('浏览···')]
        ]
        layout = [
            [sg.Frame('请选择要下载的书籍',layout=layout1,key='-LIST-'),sg.Frame('提示',layout=layout2,key='-RESULT-',visible=False)],
            [sg.Frame('请指定书籍的保存目录',layout3,key='-PATH-')],
            [sg.Button('确定',key='-OK-',),sg.Button('继续',key='-GOON-',visible=False,disabled=True),sg.Button('取消',key='-CANCEL-'),sg.Button('退出',key='-EXIT-',visible=False,disabled=True)],
            [sg.T('by:',font=('黑体',12),text_color='red',size=28,justification='right'),sg.T('北极星光',font=('黑体',12),text_color='red')],
            [sg.T('E-mail:',font=('黑体',12),text_color='red',size=28,justification='right'),sg.T('light22@126.com',font=('黑体',12),text_color='red')]
        ]

        self.window = sg.Window('书籍下载',layout)
        while True:
            event,values = self.window.read()
            if event in [None,'-CANCEL-','-EXIT-']: break
            if event == '-OK-':
                if len(values['-LISTBOX-']) == 0:
                    sg.popup('请至少选择一本要下载的书籍')
                    continue
                if len(values['-FOLDER-']) == 0:
                    sg.popup('请指定书籍的保存目录')
                    continue
                self.window['-LIST-'].update(visible=False)
                self.window['-RESULT-'].update(visible=True)
                self.window['-PATH-'].update(visible=False)
                self.window['-OK-'].update(visible=False)
                self.window['-GOON-'].update(visible=True)
                self.window['-CANCEL-'].update(visible=False)
                self.window['-EXIT-'].update(visible=True)
                download_list = values['-LISTBOX-']
                book_path = values['-FOLDER-']
                self.t1 = threading.Thread(target=books.main,args=(download_list,book_path))
                self.t2 = threading.Thread(target=self.status_change)
                self.t1.start()
                self.t2.start()

            if event == '-GOON-':
                self.window['-LIST-'].update(visible=True)
                self.window['-RESULT-'].update(visible=False)
                self.window['-PATH-'].update(visible=True)
                self.window['-OK-'].update(visible=True)
                self.window['-GOON-'].update(visible=False)
                self.window['-CANCEL-'].update(visible=True)
                self.window['-EXIT-'].update(visible=False)      
        self.window.close()

    def status_change(self):
        while True:
            if self.t1.is_alive() == True:
                self.window['-GOON-'].update(disabled=True)
                self.window['-EXIT-'].update(disabled=True)
            if self.t1.is_alive() == False:
                self.window['-GOON-'].update(disabled=False)
                self.window['-EXIT-'].update(disabled=False)
                break


# 调试
if __name__ == '__main__':
    url = 'http://www.xqb5.org/rank/' #资源地址  第一个目的地
    books = BookSpider(url)
    sg.theme('BrightColors')
    sg.PopupNoButtons('正在获取书籍列表，请稍等···',font=('华文行楷',20),text_color='pink',no_titlebar=True,auto_close=True,auto_close_duration=2,non_blocking=True)
    book_dict = books.get_booklist()
    windows_gui = WindowsGUI(book_dict)
    # t_gui = threading.Thread(target=windows_gui.gui)
    # t_gui.setDaemon(True)
    # t_gui.start() 
    windows_gui.gui()
