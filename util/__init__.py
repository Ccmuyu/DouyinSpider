import os


def create_dir_if_nt(path):
    """
    如果文件夹不存在, 创建文件夹
    :param path:
    :return:
    """
    # 带文件名的路径, 只创建文件夹
    if '.' in path:
        path = os.path.dirname(path)
    if not os.path.exists(path):
        os.makedirs(path)
