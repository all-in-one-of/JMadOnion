#-*- coding:utf-8 -*-

import os
import sys
import shutil

def J_convert2utf8(J_inPath,J_outPath):
    #清理目录
    if os.path.exists(J_inPath):
        if os.path.exists(J_outPath):
            try:
                shutil.rmtree(J_outPath)
            except:
                print "fail"
    for i in os.walk(J_inPath):
        if not i[0].replace(J_inPath, '').find('.git') == 1:
            os.makedirs(i[0].replace(J_inPath, J_outPath))
            for files in i[2]:
                J_convertFile(i[0]+"/"+files,i[0].replace(J_inPath, J_outPath)+'/'+files)

def J_convertFile(J_sourceFile,J_destinationFile):
    try:
        fs=open(J_sourceFile,'r')
        texts=''
        for lines in fs.readlines():
            texts += lines.decode('gbk')
        fs.close()
        fd=open(J_destinationFile,'w')
        fd.write(texts.encode('utf-8'))
        fd.close()
        print ("file write" + J_destinationFile)
    except:
        shutil.copyfile(J_sourceFile, J_destinationFile)
        print ('file copy' +J_destinationFile)
J_madOnionPath=r'\\10.32.73.250\JmadOnionGit'
helpPath=r'e:\madOnionHelp'
J_convert2utf8(J_madOnionPath,helpPath)
doxygenPath=J_madOnionPath+r'\other\thirdParty\doxygen\doxygen.exe  '+J_madOnionPath+r'\other\thirdParty\doxygen\madonion'
doxygenConfigPathOrg=J_madOnionPath+r'\other\thirdParty\doxygen\madonionOrig'
doxygenConfigPath=J_madOnionPath+r'\other\thirdParty\doxygen\madonionX'
file_data=''
with open(doxygenConfigPathOrg,'r') as doxygenConfigOrg:
    for lines in doxygenConfigOrg.readlines():
        if 'J_getHelp' in lines:
            lines=lines.replace('J_getHelp',helpPath)
        file_data+=lines
with open(doxygenConfigPath,'w') as doxygenConfig:
    doxygenConfig.write(file_data)
print doxygenPath
#os.system(doxygenPath)