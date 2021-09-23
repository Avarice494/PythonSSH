import queue

import paramiko
from fileoperation import FileOperation
class PythonSSH():

    """
    hostname:主机ip
    port:主机端口
    username:用户名称
    password:用户密码
    """
    def __init__(self):
        self.hostname = ""
        self.port = 0
        self.usename = ""
        self.password = ""

        """
        在实例化里调用函数
        """
        self.get_base_information_from_file()
    """
    使用FileOperation操作文件
    接收FileOperation.line
    FileOperation.line是一个队列，应对其使用队列的操作(多线程或while True)
    """
    def get_base_information_from_file(self):
        FileOperation(name="C:\\Users\\340\\Desktop\\user.txt")
        que = FileOperation.line
        line = que.get()
        self.hostname,self.port,self.usename,self.password = line.split(":")

    """
    实现ssh执行命令:
    1.创建SSHClient对象
    2.使用非密钥链接方式
    3.建立连接
    4.执行命令并返回结果
    5.输出结果
    """
    def exec(self):
        """1"""
        client = paramiko.SSHClient()
        """2"""
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        """3"""
        client.connect(hostname=self.hostname,port=int(self.port),username=self.usename,password=self.password)
        """4"""
        stdin,stdout,stderr = client.exec_command("ls -al")
        """5"""
        print(stdout.read().decode("utf-8"))

    """
    实现ssh上传下载命令:
    1.建立通道对象
    2.使用通道对象
    3.使用sftp客户端处理对象使其建立一个sftp链接
    4.使用put或get方式上传或下载文件
    """
    def upload_down(self):
        """1"""
        transport = paramiko.Transport((self.hostname,int(self.port)))
        """2"""
        transport.connect(username=self.usename,password=self.password)
        # private = paramiko.RSAKey.from_private_key_file("")
        # transport.connect(username="root",pkey=private)
        """3"""
        sftp = paramiko.SFTPClient.from_transport(transport)

        localpath = ""
        remotepath = ""
        """4"""
        sftp.put(localpath,remotepath)
        sftp.get(remotepath,localpath)

        transport.close()
    """
    实现ssh端口转发
    """
    def forward_port(self):
        pass

if __name__ == '__main__':
    PythonSSH().get_base_information_from_file()