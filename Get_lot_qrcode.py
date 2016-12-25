# 萌芽停车-服务端
# 用于获取空闲停车位，产生二维码供扫描

import leancloud
import qrcode
from PIL import Image, ImageTk
import os
import tkinter


# 二维码生成
def make_logo_qr(str,logo,save):
    #参数配置
    qr=qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=16,
        border=2
    )
    #添加转换内容
    qr.add_data(str)
    #
    qr.make(fit=True)
    #生成二维码
    img=qr.make_image()
    #
    img=img.convert("RGBA")
 
    #添加logo
    if logo and os.path.exists(logo):
        icon=Image.open(logo)
        #获取二维码图片的大小
        img_w,img_h=img.size
 
        factor = 4
        size_w = int(img_w/factor)
        size_h = int(img_h/factor)
 
        #logo图片的大小不能超过二维码图片的1/4
        icon_w,icon_h=icon.size
        if icon_w>size_w:
            icon_w=size_w
        if icon_h>size_h:
            icon_h=size_h
        icon=icon.resize((icon_w,icon_h),Image.ANTIALIAS)
        #详见：http://pillow.readthedocs.org/handbook/tutorial.html
 
        #计算logo在二维码图中的位置
        w=int((img_w-icon_w)/2)
        h=int((img_h-icon_h)/2)
        icon=icon.convert("RGBA")
        img.paste(icon,(w,h),icon)
        #详见：http://pillow.readthedocs.org/reference/Image.html#PIL.Image.Image.paste
    #保存处理后图片
    img.save(save)


leancloud.init("请换成你的leancloudID", "AIWvKAxqanTFEmMC8vfrtzw5")
Parking_space = leancloud.Object.extend('Parking_space')
parking_space_id = ['585e6616128fe1006ba9dbb4', '585e661661ff4b005815b4cd', '585e6617570c35006939c5cc', '585e6617b123db0065af7ee2', '585e661761ff4b006cdab360', '585e6617128fe1006dee37ee', '585e6617da2f6000658c432a', '585e661761ff4b005815b4d1', '585e6617128fe1006ba9dbb9', '585e6617ac502e00672a6ea5', '585e6617128fe10069d4592c', '585e6617128fe1006ba9dbbd', '585e6617b123db0065af7ee5', '585e6617ac502e00672a6ea7', '585e6617128fe1006dee37f5', '585e66181b69e600561823c3', '585e661861ff4b006897cfc8', '585e66188d6d810065e5313e', '585e661861ff4b0063f90935', '585e6618da2f6000658c4331', '585e6618da2f6000658c4333', '585e661861ff4b005815b4dd', '585e6618570c35006939c5d5', '585e6618ac502e00672a6eaa', '585e6618128fe10069d45934', '585e661861ff4b006cdab369', '585e661861ff4b006897cfca', '585e6618128fe1006ba9dbc4', '585e6618ac502e00672a6ead', '585e66191b69e6006cd2ed26', '585e6619128fe1006dee37fd', '585e66191b69e6006cd2ed27', '585e661961ff4b0063f9093d', '585e66191b69e6006cd2ed29', '585e66198d6d810065e53146', '585e661961ff4b006897cfcf', '585e6619b123db0065af7ef0', '585e6619b123db0065af7ef2', '585e6619570c35006939c5de', '585e6619ac502e00672a6eb2', '585e661961ff4b005815b4ea', '585e661961ff4b006cdab375', '585e661ab123db0065af7ef7', '585e661a8d6d810065e5314b', '585e661a128fe1006ba9dbcb', '585e661aac502e00672a6eb4', '585e661a61ff4b0063f90945', '585e661a570c35006939c5e0', '585e661a1b69e600561823d7', '585e661a61ff4b005815b4f0', '585e661ada2f6000658c4345', '585e661a8d6d810065e53154', '585e661a61ff4b006897cfd8', '585e661b8d6d810065e53158', '585e661b8d6d810065e5315c', '585e661b61ff4b006cdab381', '585e661c61ff4b006897cfe4', '585e661c61ff4b006897cfe5', '585e661c1b69e600561823eb', '585e661c128fe10069d4595f', '585e661c1b69e600561823ed', '585e661c61ff4b006897cfe7', '585e661c128fe1006ba9dbe2', '585e661c570c35006939c5f9', '585e661c1b69e6006cd2ed48', '585e661c61ff4b006cdab387', '585e661c1b69e6006cd2ed4b', '585e661c128fe1006dee381c', '585e661cda2f6000658c4352', '585e661c61ff4b006897cfea', '585e661d61ff4b006cdab38b', '585e661d61ff4b005815b506', '585e661d128fe1006ba9dbe5', '585e661d1b69e6006cd2ed50', '585e661d1b69e600561823f7', '585e661d61ff4b0063f90962', '585e661d128fe1006dee3823', '585e661d128fe1006ba9dbe9', '585e661d570c35006939c600', '585e661dac502e00672a6ed1', '585e661d61ff4b006897cff0', '585e661d128fe10069d4596c', '585e661db123db0065af7f17', '585e661e8d6d810065e5317d', '585e661eac502e00672a6ed4', '585e661e61ff4b006897cff4', '585e661e61ff4b005815b510', '585e661e570c35006939c605', '585e661e128fe1006dee382c', '585e661e1b69e6006cd2ed58', '585e661e61ff4b006cdab392', '585e661e128fe1006dee382d', '585e661eda2f6000658c435a', '585e661e1b69e600561823fd', '585e661e1b69e6006cd2ed5e', '585e661e128fe1006ba9dbfd', '585e661eda2f6000658c435c', '585e661eac502e00672a6edd', '585e661f570c35006939c608', '585e661fac502e00672a6ede', '585e661f1b69e60056182407', '585e661f128fe10069d45979', '585e661f570c35006939c60a', '585e661fac502e00672a6ee2', '585e661f61ff4b006897cffd', '585e661f128fe1006ba9dc08', '585e661f128fe1006dee3836', '585e661fb123db0065af7f23', '585e66208d6d810065e53191', '585e662061ff4b0063f9096d', '585e6620da2f6000658c4361', '585e662061ff4b006cdab39d', '585e662061ff4b006897d002', '585e6620128fe1006dee383e', '585e662061ff4b006897d003', '585e6620128fe10069d45988', '585e6620b123db0065af7f27', '585e66208d6d810065e5319b', '585e662061ff4b005815b51d', '585e662061ff4b006cdab3a3', '585e6620570c35006939c617', '585e6621128fe1006ba9dc16', '585e6621128fe1006dee3845', '585e66211b69e60056182419', '585e66211b69e6006cd2ed70', '585e662161ff4b006897d00a', '585e66218d6d810065e5319f', '585e662161ff4b006897d00d', '585e6621570c35006939c61d', '585e6621b123db0065af7f2f', '585e66218d6d810065e531a5', '585e662161ff4b0063f90979', '585e6621b123db0065af7f30', '585e6622da2f6000658c436f', '585e662261ff4b006897d012', '585e6622570c35006939c61f', '585e66221b69e6006cd2ed79', '585e6622b123db0065af7f34', '585e662261ff4b0063f9097a', '585e6622128fe1006ba9dc27', '585e66221b69e60056182421', '585e662261ff4b005815b522', '585e6622128fe1006ba9dc28', '585e6622128fe1006ba9dc2d', '585e66221b69e6006cd2ed7f', '585e662261ff4b0063f90981', '585e6623570c35006939c628', '585e6623128fe1006dee3857', '585e6623570c35006939c62a', '585e66231b69e6006cd2ed87', '585e6623ac502e00672a6f06', '585e662361ff4b006cdab3b5', '585e6623b123db0065af7f3e', '585e662361ff4b006cdab3b6', '585e6623128fe10069d459a0', '585e6623128fe1006dee3862', '585e66231b69e6006cd2ed88', '585e6623128fe1006dee3863', '585e66238d6d810065e531b7', '585e662461ff4b006897d021', '585e662461ff4b0063f9098a', '585e662461ff4b006cdab3ba', '585e662461ff4b006cdab3bc', '585e6624128fe1006dee386b', '585e66241b69e60056182439', '585e6624570c35006939c62f', '585e6624da2f6000658c4382', '585e662461ff4b005815b53b', '585e6624b123db0065af7f48', '585e6624128fe1006ba9dc39', '585e6624da2f6000658c4385', '585e662461ff4b006cdab3c6', '585e662561ff4b006897d02b', '585e6625b123db0065af7f51', '585e66251b69e6005618243f', '585e662561ff4b006cdab3c7', '585e6625128fe10069d459b3', '585e66251b69e6006cd2ed95', '585e6625128fe10069d459b4', '585e6625b123db0065af7f54']

# print(parking_space_id)





if __name__=='__main__':

	# 创建停车位查询函数
	query = leancloud.Query('Parking_space')
	# 车位已满的标志
	parking_flag =1
	for x in parking_space_id:
		query_result = query.get(x)
		print(x)
		# 创建停车位查询结果
		Parking_space_query = query_result.get('Parking_space')
		Is_using_query = query_result.get('Is_using')
		# print(Is_using_query)

		if Is_using_query == 0:
			parking_flag = 0
		    # 查询空车位后生成二维码
			save_path = Parking_space_query + '.png' 		#生成后的保存文件
			logo = 'logo.png'  			     				#logo图片
			str = x + Parking_space_query
			make_logo_qr(str,logo,save_path)
			# 检测到此车位被扫码后状态值改变后生产下一个空车位
			
	
		    # 更新停车位状态
			# parking_space_updata = Parking_space.create_without_data(x)
			# parking_space_updata.set('Is_using', 1)
			# parking_space_updata.save()

			# 二维码的GUI生成界面
			top = tkinter.Tk()
			image = Image.open(save_path)  
			im = ImageTk.PhotoImage(image)  

			label = tkinter.Label(top, image = im)
			label.pack()
			tkinter.mainloop()
			break

	if parking_flag:
		# 二维码的GUI生成界面
		top = tkinter.Tk()
		label = tkinter.Label(top, text='车位已满')
		label.pack()
		tkinter.mainloop()



