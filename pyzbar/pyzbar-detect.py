'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.10.10
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode \n')   

import os,sys,shutil,csv
from pyzbar.pyzbar import decode
from PIL import Image

def detect(full_name):
    print(full_name)
    #打开图片
    img = Image.open(full_name)
    #解析图片
    res = decode(img)
    #打印结果
    for re in res:
        print('data:',re.data)  
        print('type:',re.type)  
    if res:
        return res[0]
    else:
        return None

def main():
    #检查目录
    if not os.path.exists('ok\\'):
        os.mkdir('ok\\')
    if not os.path.exists('ng\\'):
        os.mkdir('ng\\')
        
    #遍历文件    
    report = []
    files = os.listdir('todo\\')
    for file in files:
        src_file = 'todo\\'+ file
        res = detect(src_file)
        if res is not None:
            rep = [file,res.type,'\''+res.data.decode('utf8')]
            dest_file = 'ok\\'+file
        else:
            print('未识别到条码:',file)
            rep = [file,'NONE','NONE']
            dest_file = 'ng\\'+file
        
        report.append(rep)
        shutil.copyfile(src_file,dest_file)
        
    #生成报表
    with open('report.csv','w',newline='') as f:
        writer_obj= csv.writer(f) #创建写csv对象
        for rep in report:
            print(rep)
            writer_obj.writerow(rep) #写入记录
    
     
if __name__ == "__main__":
    main() 