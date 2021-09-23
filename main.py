import paramiko

class PythonSSH():
    def __init__(self):
        pass

    """
    实现ssh执行命令
    """
    def exec(self):
        client = paramiko.SSHClient()

        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

        client.connect(hostname="39.106.12.136",port=22,username='root',password='hp2012..')

        stdin,stdout,stderr = client.exec_command("ls -al")

        print(stdout.read().decode("utf-8"))

    """
    实现ssh上传下载命令
    """
    def upload_down(self):
        transport = paramiko.Transport(("39.106.12.136",22))
        transport.connect(username="root",password='hp2012..')
        # private = paramiko.RSAKey.from_private_key_file("")
        # transport.connect(username="root",pkey=private)
        sftp = paramiko.SFTPClient.from_transport(transport)

        localpath = ""
        remotepath = ""

        sftp.put(localpath,remotepath)

        sftp.get(remotepath,localpath)

        transport.close()
    """
    实现ssh端口转发
    """
    def forward_port(self):
        pass

if __name__ == '__main__':
    PythonSSH().exec()