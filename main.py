from . import PythonSSH
import config
"""
实现多个ssh命令和文件的使用场景（该模块将更具需求逐步跟新）
"""
class scenario:
    PythonSSH = PythonSSH(userfile=config.userfile,command=config.command)
    def __init__(self):
        pass
    """
    场景一：上传一个bash脚本，执行这个bash脚不，返回这个bash脚本内容
    """
    def scenario_one(self):
        self.PythonSSH.upload()
        self.PythonSSH.exec()
        self.PythonSSH.down()
