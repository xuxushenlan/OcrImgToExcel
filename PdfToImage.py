import fitz  # pdf转为图片


'''
将PDF转化为图片
pdfPath pdf文件的路径
imgPath 图片要保存的路径
zoom_x x方向的缩放系数
zoom_y y方向的缩放系数
rotation_angle 旋转角度
zoom_x和zoom_y一般取相同值，值越大，图像分片率越高
返回目标pdf的名称和页数，便于下一步操作

'''


def pdf_image(pdfPath, imgPath, zoom_x=5, zoom_y=5, rotation_angle=0):
    # 打开PDF文件
    pdf = fitz.open(pdfPath)
    # 获取pdf页数
    num = pdf.page_count
    # 逐页读取PDF
    for page_index in range(num):  # iterate over pdf pages
        page = pdf[page_index]  # get the page
        mat = fitz.Matrix(zoom_x, zoom_y, rotation_angle)  # zoom factor 2 in each dimension
        pix = page.get_pixmap(matrix=mat)  # use 'mat' instead of the identity matrix
        pix.save(f'{imgPath}\\page-{page.number+1}.png')  # store image as a PNG
        print(page.number+1)


pdfPath = '20230912112751.pdf'
imgPath = 'image'
pdf_image(pdfPath, imgPath)
