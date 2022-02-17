# -*- coding: utf-8 -*-
import xml.dom.minidom

from xml.dom.minidom import parse
from math import radians, cos, sin, asin, sqrt
import json
from data_structure import node as node_class
from data_structure import way as way_class
from geographiclib.geodesic import Geodesic
import pickle


def create_xml(node_list, way_list=[], xmlname='', is_camera=False, camera_name_map={}):
    doc = xml.dom.minidom.Document()
    #print(camera_name_map)

    main_ele = doc.createElement('osm')
    doc.appendChild(main_ele)
    main_ele.setAttribute("version", "0.6")
    main_ele.setAttribute("upload", "false")
    main_ele.setAttribute("generator", "python")
    if (len(node_list) != 0):
        for node in node_list:

            node_elem = doc.createElement("node")

            node_elem.setAttribute("id", str(node.id))
            node_elem.setAttribute("lat", str(node.lat))
            node_elem.setAttribute("lon", str(node.lon))
            node_elem.setAttribute("version", str(3))

            tag1 = doc.createElement("tag")
            tag1.setAttribute("k", "id")
            tag1.setAttribute("v", str(node.id))
            tag2 = doc.createElement("tag")
            tag2.setAttribute("k", "lat")
            tag2.setAttribute("v", str(node.lat))
            tag3 = doc.createElement("tag")
            tag3.setAttribute("k", "lon")
            tag3.setAttribute("v", str(node.lon))

            node_elem.appendChild(tag1)
            # node_elem.appendChild(enter)
            node_elem.appendChild(tag2)
            # node_elem.appendChild(enter)
            node_elem.appendChild(tag3)
            # node_elem.appendChild(enter)

            if (is_camera == True):
                tag4 = doc.createElement("tag")
                tag4.setAttribute("k", "camera")
                tag4.setAttribute("v", "camera")
                node_elem.appendChild(tag4)

                if (len(camera_name_map)!=0):
                    tag4 = doc.createElement("tag")
                    tag4.setAttribute("k", "name")
                    tag4.setAttribute("v", camera_name_map[str(node.id)])
                    node_elem.appendChild(tag4)

            if (node.hascarema):
                tag = doc.createElement("tag")
                tag.setAttribute("k", 'is_kakou')
                tag.setAttribute("v", str(node.hascarema))
                node_elem.appendChild(tag)

                tag = doc.createElement("tag")
                tag.setAttribute("k", 'kakou_num')
                tag.setAttribute("v", str(node.carema_num))
                node_elem.appendChild(tag)

            if (node.dir_list!=[]):
                tag = doc.createElement("tag")
                tag.setAttribute("k", 'dirlist')
                dir_str=""
                for dir in node.dir_list:
                    dir_str+=str(dir)
                    dir_str+=','
                tag.setAttribute("v", dir_str)
                node_elem.appendChild(tag)

            main_ele.appendChild(node_elem)
            # node_elem.appendChild(enter)
            # print(node_elem)


    print("way_list num:",len(way_list))
    if (len(way_list) != 0):
        for node in way_list:

            node_elem = doc.createElement("way")

            node_elem.setAttribute("id", node.id)
            node_elem.setAttribute("version", "3")

            tagnd1 = doc.createElement("nd")
            #print(node.ref)
            tagnd1.setAttribute("ref", node.ref[0])
            node_elem.appendChild(tagnd1)

            tagnd2 = doc.createElement("nd")
            tagnd2.setAttribute("ref", node.ref[1])
            node_elem.appendChild(tagnd2)

            for k, v in node.feature.items():  # 加key value键值对
                tag = doc.createElement("tag")
                tag.setAttribute("k", k)
                tag.setAttribute("v", v)
                node_elem.appendChild(tag)

            # 加点便于查找的key value
            tag = doc.createElement("tag")
            tag.setAttribute("k", 'id')
            tag.setAttribute("v", node.id)
            node_elem.appendChild(tag)

            tag = doc.createElement("tag")
            tag.setAttribute("k", 'ref')
            tag.setAttribute("v", str(node.ref[0])+str(node.ref[1]))
            node_elem.appendChild(tag)

            tag = doc.createElement("tag")
            tag.setAttribute("k", 'dir')
            tag.setAttribute("v", node.direction)
            node_elem.appendChild(tag)
            if node.volume!=0:
                tag = doc.createElement("tag")
                tag.setAttribute("k", 'volume')
                tag.setAttribute("v", str(node.volume))
            node_elem.appendChild(tag)


            if (node.hascarema2 == 1):

                tag = doc.createElement("tag")
                tag.setAttribute("k", 'haskakou2')
                tag.setAttribute("v", str(node.hascarema2))
                node_elem.appendChild(tag)

                tag = doc.createElement("tag")
                tag.setAttribute("k", 'way_fix_camera_num_2')
                tag.setAttribute("v", str(node.carema_num2))
                node_elem.appendChild(tag)




            main_ele.appendChild(node_elem)
            # node_elem.appendChild(enter)
            # print(node_elem)

    # print(main_ele.toxml())
    # 此处需要用codecs.open可以指定编码方式
    fp = open(xmlname, 'w', encoding='utf-8')
    # 将内存中的xml写入到文件
    doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding='utf-8')
    fp.close()
