import os,shutil


imglist = os.listdir('image')
img_dir = os.path.abspath('image')
excel_dir = os.path.abspath('excel')
pass_dir = os.path.abspath('passed')
for img in imglist:
    filename = img.split('.')[0]
    if os.path.exists(f'{excel_dir}/{filename}.xlsx'):
        shutil.move(f'{img_dir}/{img}',f'{pass_dir}')

