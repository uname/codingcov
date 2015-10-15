#-*- cofing: utf-8 -*-
import os
import sys

def getFileList(fileDir):
    fileList = []
    for root, dirs, files in os.walk("./"):
        fileList += [os.path.join(root, name) for name in files]
        
    return fileList

def resetCodingType(fileList, fromCoding="utf-8", toCoding="gbk"):
    count = 0
    for f in fileList:
        f = f.replace("\\", "/")
        coding = os.popen("file -bi \"%s\" | gawk -F'[ =]' '{print $3}'" % f).read().strip("\r\n")
        if coding == fromCoding.lower():
            if os.system("iconv -f %s -t %s \"%s\" > \"%s.tmp\"" % (fromCoding, toCoding, f, f)) == 0 and os.system("mv \"%s.tmp\" \"%s\"" % (f, f)) == 0:
                print "OK\t%s" % f
                count += 1
    print "----------------------------------------------"
    print "%d file completed" % count
    
if __name__ == "__main__":
    resetCodingType(getFileList("./"), "utf-8", "gbk")