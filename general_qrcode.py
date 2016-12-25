# 萌芽停车-服务端
# 用于产生停车位二维码

import leancloud
leancloud.init("6FR9SJu9wGBKXVN95sV48xNB-gzGzoHsz", "AIWvKAxqanTFEmMC8vfrtzw5")
Parking_space = leancloud.Object.extend('Parking_space')


lot = list(range(1,21))
ABC = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
# 存储位置
ABC_lot = []
# 存储位置的ID操作
ABC_lot_id =[]

for abc in ABC:
	for l in lot:

		ABC_lot.append(abc +' '+str(l))

		parking_space = Parking_space()
		parking_space.set('Parking_space', abc +' '+str(l))
		parking_space.set('Is_using', 0)
		parking_space.save()
		ABC_lot_id.append(parking_space.id)

# parking_space.save()
print(ABC_lot_id)
# print()

