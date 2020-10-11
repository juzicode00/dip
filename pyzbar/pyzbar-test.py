'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.10.10
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode \n')   

 
from pyzbar.pyzbar import decode
from PIL import Image

#打开图片
img = Image.open('qr1.png')
img = Image.open('todo\\5.jpg')
#解析图片
res = decode(img)
#打印结果
print(res)  
print()
for re in res:
    print('data:',re.data)  
    print('type:',re.type)  
    
''' 
if __name__ == "__main__":
    client()''' 