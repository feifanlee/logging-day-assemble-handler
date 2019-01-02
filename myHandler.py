import logging
from logging import handlers
import os
import shutil

class AdHandler(handlers.TimedRotatingFileHandler):
    def __init__(self,filename,when='h',interval=1,backupCount=0,encoding=None,delay=False,utc=False):
        super(AdHandler,self).__init__(filename,when,interval,1,encoding,delay,utc)
    def getFilesToDelete(self):
        rst = super(AdHandler,self).getFilesToDelete()
        #only 1 or 0 in rst
        for f in rst:
            dirName,baseName = os.path.split(self.baseFilename)
            prelen=len(self.baseFilename+'.')
            suf=f[prelen:]
            if len(suf)>10:
                suf = suf[:10]
            timeDirName = os.path.join(dirName,suf)
            if not os.path.exists(timeDirName):
                os.mkdir(timeDirName)
            shutil.copy(f,timeDirName)
        return rst
    pass