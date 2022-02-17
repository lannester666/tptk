import pickle

class node:
    def __init__(self):
        self.id = ''     # 名称
        self.lat = ''     # 尺寸
        self.lon = ''     # 列表
        self.hascarema=False
        self.intersection_num=0
        self.carema_num = '-1'
        self.feature = {}  # feature 字典
        self.dir_list=[]

class way:
    def __init__(self):
        self.id = ''     #  id
        self.ref = []     # node list
        self.feature ={}    # feature 字典
        self.poi={}
        self.hascarema=0
        self.hascarema2 = 0
        #self.hascarema3 = 0
        #self.carema_num='-1'
        self.carema_num2 = '-1'
        #self.carema_num3 = '-1'
        self.node_camera=0  #处理过程中用到的临时字段，merge的时候判断细短路是否连接卡口的

        self.direction=''
        self.volume= 0
        self.tmp=''


class camera_volume:  #卡口流量
    def __init__(self):
        self.id = ''
        self.all_volume=0
        self.E_volume=0
        self.S_volume = 0
        self.W_volume = 0
        self.N_volume = 0


class camera_class:
    def __init__(self):
        self.id = ''
        self.lat=0
        self.lon=0
        self.dir =''
        self.node_list=''
        self.way_list=[]
        self.fix_node=''


class merge_way:
    def __init__(self):
        self.id=""
        self.ref=[]
        self.link=[]
        self.bi_ref=[]
        self.bi_link=[]




