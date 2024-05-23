from tkinter import filedialog


def open_file():
    # root = tk.Tk()
    # root.withdraw()  # 隐藏主窗口
    file_path = filedialog.askopenfilename()
    print("Selected file path:", file_path)
    # 处理用户选择的文件
    return file_path


# open_file()

def open_folder():
    file_path = filedialog.askdirectory()
    print("Selected folder path:", file_path)
    return file_path
