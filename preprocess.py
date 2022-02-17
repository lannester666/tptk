import os

with open("/home/zhangtaiyan/tmp/pycharm_project_570/2020-5-18-traj.csv", 'r') as f:
    dict = {}
    for lines in f.readlines():
        attrs = lines.strip('\n').split(',')
        if attrs[3] == "Latitude":
            continue
        id = attrs[0]
        if id not in dict:
            dict.setdefault(id, []).append(attrs)
        else:
            dict.get(id).append(attrs)
    for No in dict.keys():
        content = dict[No]
        # print(str(content[0]))
        f2 = open(os.path.join("/home/zhangtaiyan/tmp/pycharm_project_570/data1/", No), "w")
        for line in content:
            f2.write(str(line)+'\n')
        f2.close()
