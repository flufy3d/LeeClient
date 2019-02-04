# -*- coding: utf-8 -*-

import os

class LeePath:
    def __init__(self):
        pass
    
    def __withmark(self, val, withmark = True):
        if os.path.isfile(val):
            return val
        return val if not withmark else val + os.sep

    def utility(self, relpath = '', withmark = True):
        # 之所以需要 .. 是应为当前脚本在 PyLibs 目录下
        # 只有切换到上级目录才是 LeeClientAgent.py 的目录, 即: Utility
        path = os.path.join(os.path.split(os.path.realpath(__file__))[0], '..')
        path = os.path.join(path, relpath)
        return self.__withmark(os.path.abspath(path), withmark)
    
    def client(self, relpath = '', withmark = True):
        path = self.utility('..', withmark)
        path = os.path.join(path, relpath)
        return self.__withmark(os.path.abspath(path), withmark)
    
    def bin(self, relpath = '', withmark = True):
        path = self.utility('Bin', withmark)
        path = os.path.join(path, relpath)
        return self.__withmark(os.path.abspath(path), withmark)
    
    def imports(self, relpath = '', withmark = True):
        path = self.utility('Import', withmark)
        path = os.path.join(path, relpath)
        return self.__withmark(os.path.abspath(path), withmark)
    
    def patches(self, relpath = '', withmark = True):
        path = self.utility('Patches', withmark)
        path = os.path.join(path, relpath)
        return self.__withmark(os.path.abspath(path), withmark)
    
    def resources(self, relpath = '', withmark = True):
        path = self.utility('Resources', withmark)
        path = os.path.join(path, relpath)
        return self.__withmark(os.path.abspath(path), withmark)
    
    def reports(self, relpath = '', withmark = True):
        path = self.utility('Reports', withmark)
        path = os.path.join(path, relpath)
        return self.__withmark(os.path.abspath(path), withmark)

    # beforePatches
    # afterPatches

    # clientOrigin
    # clientTranslate
    # clientImport
