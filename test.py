import os, time

imagelist = os.listdir('image')
print(os.listdir('image'))
# count = 0
# for imagepath in imagelist:
#     print(count, time.asctime())
#     if count < 2:
#         count += 1
#     else:
#         count = 1
#         print('睡一分钟,再继续！')
#         time.sleep(60)
#     print(imagepath)
#     filename = imagepath.split('.')[0]
#     print('请求文件', filename)

img_dir = os.path.abspath('image')
json_dir = os.path.abspath('json')
excel_dir = os.path.abspath('excel')
print(img_dir,json_dir,excel_dir)
print(os.path.abspath(__file__),os.path.dirname(__file__),os.path.join(img_dir,'page-134.png'))