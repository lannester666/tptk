from xml.dom.minidom import parse
from math import radians, cos, sin, asin, sqrt

import json
from data_structure import node as node_class
from data_structure import way as way_class
from geographiclib.geodesic import Geodesic
import pickle


def read_xml(file_address):  # 读取intersection_way_taian返回nodelist 和 waylist     todo 转成了百度坐标系  如果用这个数据画图会是偏移的
    intersection_taian = file_address
    DOMTree = parse(intersection_taian)
    intersec_list = DOMTree.documentElement

    node_list = []  # 读取intersection_way_taian文件中所有的node节点  shape[n,3] n行3列  [[id，lat，lon],[]]
    nodes = intersec_list.getElementsByTagName("node")
    for node in nodes:
        id = node.getAttribute("id")
        lat = float(node.getAttribute("lat"))
        lon = float(node.getAttribute("lon"))

        action=node.getAttribute("action")
        if action=='delete':
            continue

        # todo 加上一些卡口特征
        item_node = node_class()
        item_node.id = id
        item_node.lat = str(lat)
        item_node.lon = str(lon)



        tags = node.getElementsByTagName("tag")
        tag_list = {}
        for tag in tags:
            tag_list[tag.getAttribute("k")] = tag.getAttribute("v")
        item_node.feature = tag_list
        if 'dirlist' in tag_list:
            item_node.dir_list=tag_list['dirlist'].split(",")

        '''
            def __init__(self):
                self.id = ''     # 名称
                self.lat = ''     # 尺寸
                self.lon = ''     # 列表
                self.hascarema=False
                self.intersection_num=0
                self.carema_num = '-1'
                self.feature = {}  # feature 字典

        '''

        if 'is_kakou' in item_node.feature.keys():
            if item_node.feature['is_kakou'] != 'False':
                item_node.hascarema = bool(item_node.feature['is_kakou'])

        if 'kakou_num' in item_node.feature.keys():
            if item_node.feature['kakou_num'] != '-1':
                item_node.carema_num = item_node.feature['kakou_num']

        node_list.append(item_node)

    way_list = []  # 存储intersection_way_taian文件中所有的node节点  [ [id,[nd1,nd2,nd3...],[[k1,value],[k2,value]]], ...]
    ways = intersec_list.getElementsByTagName("way")
    for way in ways:
        id = way.getAttribute("id")
        action=way.getAttribute("action")
        if action=='delete':
            continue
        nds = way.getElementsByTagName("nd")
        nd_list = []
        for nd in nds:
            nd_list.append(nd.getAttribute("ref"))

        tags = way.getElementsByTagName("tag")
        tag_list = {}
        for tag in tags:
            tag_list[tag.getAttribute("k")] = tag.getAttribute("v")

        # todo 加上一些卡口特征

        item_way = way_class()
        item_way.id = id
        item_way.ref = (nd_list)
        item_way.feature = tag_list

        '''   
            def __init__(self):
        self.id = ''     #  id
        self.ref = []     # node list
        self.feature ={}    # feature 字典
        self.poi={}
        self.hascarema=0
        self.hascarema2 = 0

        self.carema_num2 = '-1'

        self.node_camera=0
        self.direction=''
        self.volume= 0

        '''
        if 'hascarema2' in item_way.feature.keys():
            if item_way.feature['hascarema2'] != '0':
                item_way.hascarema2 = int(item_way.feature['hascarema2'])

        if 'way_fix_camera_num_2' in item_way.feature.keys():
            if item_way.feature['way_fix_camera_num_2'] != '-1':
                item_way.carema_num2 = item_way.feature['way_fix_camera_num_2']

        if 'dir' in item_way.feature.keys():
            if item_way.feature['dir'] != '':
                item_way.direction = item_way.feature['dir']

        way_list.append(item_way)
    return node_list, way_list
