import os

def readIphone():
    '''获取手机配置信息，返回手机adb号与安卓版本'''
    rootPath=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    filePath=os.path.join(rootPath + "/data/confData/")
    os.chdir(filePath)
    f=open("confData.yaml","r",encoding="utf-8")
    iphoneDataSet=f.readlines()
    return iphoneDataSet
    #iphoneData=eval(iphoneDataSet[0])
    #w=iphoneData['iphoneAndroidNum']
    #print(w)