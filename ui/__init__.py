import os.path
import time
import tkinter as tk
import re

import cmd
import v2
from ui import file


class App(object):
    def __init__(self):
        # 初始化窗口
        app = tk.Tk()
        app.title('抖音作品下载器')
        app.geometry('600x300')
        app.iconphoto(False, tk.PhotoImage(file='./image/icon.png'))
        # app.iconbitmap('./favicon.ico')
        self.app = app
        self.save_dir = ''
        self.douyin_url = 'https://www.douyin.com'

        label1 = tk.Label(self.app, text='主页地址:')
        entry1 = tk.Entry(self.app, width=25)  # 输入框
        self.download_entry = entry1

        btn1 = tk.Button(self.app, text='检查', bg='red', command=self.check_input_douyin_user_url)
        label_check_url = tk.Label(self.app, text='请检查地址是否有误')
        self.label_check_url = label_check_url

        label2 = tk.Label(self.app, text='保存地址：')
        btn_open_dir = tk.Button(self.app, text='打开', bg='red', command=self.open_dir)
        label_dir = tk.Label(self.app)  # 输入框

        self.label_dir = label_dir

        # label1.pack(side=tk.TOP, anchor=tk.W)
        # label1.grid(row=0, column=0)

        label1.place(x=0.5, y=0.5)
        entry1.place(x=75, y=0.5)
        btn1.place(x=320, y=0.5)
        label_check_url.place(x=400, y=2)

        label2.place(x=0.5, y=50)
        btn_open_dir.place(x=75, y=50)
        label_dir.place(x=150, y=50)

        label_ready = tk.Label(self.app, text='准备就绪：')
        start_btn = tk.Button(self.app, text='开始下载', command=self.start_download)
        label_found_videos = tk.Label(self.app, foreground='blue')
        self.label_found_videos = label_found_videos
        label_ready.place(x=0.5, y=95)
        start_btn.place(x=75, y=95)
        label_found_videos.place(x=170, y=98)

    def clear_label(self):
        self.label_found_videos.config(text='')
        self.label_check_url.config(text='')

    def check_input_douyin_user_url(self):
        url = self.download_entry.get()
        if re.match(r'https://www.douyin.com/user/[\w-]+', url) is None:
            self.label_check_url.config(text='抖音主页地址错误', foreground='red')
        else:
            self.label_check_url.config(text='check url ok', foreground='green')

    def run(self):
        # app 入口
        self.app.mainloop()

    def open_dir(self):
        # 选择文件夹
        self.save_dir = file.open_folder()
        print("open_dir:", self.save_dir)
        self.label_dir.config(text=self.save_dir)

    def start_download(self):
        # 下载入口
        url = self.download_entry.get()
        path = self.save_dir
        if path is None or path == "":
            print("path is none......")
            path = cmd.user_home() + os.path.sep + '/Documents/dy_download'
        print("start download,url: \n", url, "\n", path)
        self.clear_label()
        self.app.update()

        self.label_found_videos.config(text='正在下载中...')
        time.sleep(0.5)
        v2.app_run(url, path)
        print("视频已保存：\n", self.save_dir)
        self.label_found_videos.config(text='下载完成！')


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
