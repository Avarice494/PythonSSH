import queue
"""
对txt文件的读写操作
1.按行读取txt文件
"""


class FileOperation():
    """
    line:文件行的队列
    """
    line = queue.Queue(100)
    def __init__(self,name="mode.txt",method = "r"):
        self.name = name
        self.method = method
        self.txt_read_into_queue()
    def txt_read_into_queue(self):
        fl = True
        file = open(self.name, self.method)
        while fl:
            fl = file.readline()
            self.line.put(fl)
            print(self.line.qsize())

if __name__ == '__main__':
    FileOperation()
