import logging
logging.basicConfig(level=logging.DEBUG)
# time = '2020-05-18 09:50:40.000'
# time = time.split('.')
# print(type(time[0]))
# logging.debug("group after filters:%d", 123)
# logging.debug("next%d",456)
attrs = "['3468042174', '2020-05-18 09:51:30.000', '117.13800', '36.18941']"
attrs = attrs.replace('\'', '')
attrs = attrs.replace(']', '')
attrs = attrs.replace('[', '')
print(attrs)
attrs = attrs.strip('\n').split(',')
print(attrs[1])
# for attr in attrs:
#     print(attr)