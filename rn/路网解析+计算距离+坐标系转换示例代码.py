import data_structure
import read_xml
import create_xml
#读路网
node_list,way_list=read_xml.read_xml('./实验区域3reindex.xml')
for idx,node in enumerate(node_list):
	id=node.id
	lat=node.lat
	lon=node.lon
	has_camera=node.hascarema
	camera_num=node.carema_num  #todo  list,有个别路口对应两个卡口
	print("第"+str(idx)+"个路口的id,lat,lon,是否有卡口,卡口编号:",id,lat,lon,has_camera,camera_num)

node_map={}
for node in node_list:
	node_map[node.id]=node

for idx,way in enumerate(way_list):
	id=way.id
	ref=way.ref
	print("第"+str(idx)+"条路的起终点是",ref)
	print("对应的坐标是", node_map[ref[0]].lon,node_map[ref[0]].lat)
	#todo 注意 1.纯gps坐标系 2.有的路是存在正反双向的，存了两条way，有的路就一条，对于你们的系统来说其实只需有单向路就行了，可以根据ref做个过滤
	#todo 如果两条路的way1.ref[0]==way2.ref[1] and way1.ref[1]==way2.ref[2] 就可以去掉其中一条

#存路网
create_xml.create_xml(node_list,way_list,'你的路网名.xml')


#######################################################################
#计算距离
import cal_distance
for idx,way in enumerate(way_list):
	id=way.id
	ref=way.ref
	node1=node_map[ref[0]]
	node2 = node_map[ref[1]]
	dis1 = cal_distance.geodistance1(float(node1.lon), float(node1.lat), float(node2.lon), float(node2.lat))
	print("第"+str(idx)+"条路的起终点是",ref)
	print("对应的坐标是", node_map[ref[0]].lon,node_map[ref[0]].lat)
	print("距离",dis1)
	print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


#######################################################################

#计算距离
import cal_distance

for idx,way in enumerate(way_list):
	id=way.id
	ref=way.ref
	node1=node_map[ref[0]]
	node2 = node_map[ref[1]]
	dis1 = cal_distance.geodistance1(float(node1.lon), float(node1.lat), float(node2.lon), float(node2.lat))
	print("第"+str(idx)+"条路的起终点是",ref)
	print("对应的坐标是", node_map[ref[0]].lon,node_map[ref[0]].lat)
	print("距离",dis1)
	print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")



#######################################################################
#坐标系转换
import transform_gps
for idx,node in enumerate(node_list):
	id=node.id
	lat=float(node.lat)
	lon=float(node.lon)
	new_lat,new_lon=transform_gps.wgs2gcj(lat,lon)
	print("高德坐标系对应坐标",lat,lon)
	print("高德坐标系对应坐标：",new_lat,new_lon)
	print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

