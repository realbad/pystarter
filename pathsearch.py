import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
# plt.figure(figsize=(16,8),dpi=100)
plt.rcParams['figure.figsize'] = (16.0, 8.0)
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
current_path = []

def generatePos(G):
    pos = {}
    xcoor = {
        'a': -4,
        'b': -3,
        'c': -2,
        'd': 2,
        'e': 3,
        'f': 4
    }

    pos = dict.fromkeys(G.nodes())
    for node in (pos.keys()):
        if node[0] in xcoor.keys():
            ypos = xcoor.get(node[0])
        else:
            ypos = 0
        if node[0].isalpha():
            if (node[0]) in ('d','e','f'):
                xpos = int(node[1:])-2
            else:
                xpos = int(node[1:])
        else:
            xpos = int(7)
        pos[node] = [xpos, ypos]
    return pos


def draw(G, path, title=""):#广州白云机场

    pos = generatePos(G)
    # print(pos)
    nx.draw_networkx(G, pos, node_size=150, font_size=8, alpha=0.7, node_color='c', arrows=False)
    # edge_labels = nx.get_edge_attributes(G)
    new_labels = dict(
        map(lambda x: ((x[0], x[1]), str(x[2]['weight'])), G.edges(data=True)))
    nx.draw_networkx_edge_labels(G,pos,alpha = 0.9,font_size=8,rotate = False,edge_labels=new_labels,label_pos=0.5)
    Gpath = []
    # 生成path的edge
    for i, x in enumerate(path):
        if i == len(path) - 1: break
        Gpath.append((x, path[i + 1]))
    nx.draw_networkx_edges(G, pos, edgelist=Gpath, edge_color='r', width=2)
    plt.title(title)
    plt.ylim(-5, 5)
    plt.axis('off')
    plt.show()

def findPath(io,G,ho,stand):
    if io =='i':
        path = nx.dijkstra_path(G, source=ho, target=stand)
        length = nx.dijkstra_path_length(G, source=ho, target=stand)
    elif io == 'o':
        path = nx.dijkstra_path(G, source=stand, target=ho)
        length = nx.dijkstra_path_length(G, source=stand, target=ho)
    else:
        path=[]
        length=[]
    return path,length

def changeVal(value):
    pass


def main():

    stand_exit = {
        '101': ['c3', 59], '102': ['c3', 53], '103': ['c3', 46], '104': ['c3', 39], '105': ['c3', 32], '106': ['c', 16],
        '107': ['c', 16], '108': ['c4', 20], '109': ['c4', 27], '110': ['c5', 38], '111': ['c5', 43], '112': ['c5', 47],
        '113': ['c5', 45], '114': ['c5', 40], '115': ['c5', 34], '116': ['c5', 28], '117': ['c', 12.5],
        '118': ['c', 12.5], '119': ['c6', 17], '120': ['c6', 22], '121': ['c6', 27], '122': ['c7', 40],
        '123': ['c7', 45], '124': ['c7', 36], '125': ['c7', 31], '126': ['c7', 26], '127': ['c7', 21],'128': ['c', 10],
        '129': ['c', 10],'130': ['c8', 24],'131': ['c8', 29],'132': ['c8', 34],'133': ['c8', 39],'135': ['c8', 39],
        '136': ['c8', 35],'137': ['c8', 31],'138': ['c8', 27],'139': ['c8', 23],'201': ['d5', 57],'202': ['d5', 50.5],
        '203': ['d5', 44],'204': ['d5', 36],'205': ['d5', 27], '206': ['d5', 15],'207': ['d6', 13],'208': ['d6', 13],
        '209': ['d6', 19],'210': ['d6', 25],'211': ['d7', 37],'212': ['d7', 42],'213': ['d7', 46],'214': ['d7', 44],
        '215': ['d7', 36],'216': ['d7', 31],'217': ['d7', 26],

    }
    while True:
        io = str(input("进港/出港？(I/O)\t")).lower()
        if io == 'i' or io == 'o':
            break
        else:
            print('输入错误')
    while True:
        try:
            stand = str(input("请输入停机位置："))
            if stand in stand_exit:
                break
            else:
                print('输入错误')
        except:
            raise ValueError('停机位输入不合法')

    row_n4 = np.array(
        ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16'])
    row_n3 = np.array(
        ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', 'e12', 'e13', 'e14', 'e15', 'e16'])
    row_n2 = np.array(
        ['', '', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13', 'd14', 'd15', 'd16'])
    row_n1 = np.append([],stand)
    row_s1 = np.append([],stand)
    row_s2 = np.array(['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14', '', ''])
    row_s3 = np.array(
        ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10', 'b11', 'b12', 'b13', 'b14', 'b15', 'b16'])
    row_s4 = np.array(
        ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15', 'a16'])
    row = np.array([row_n4, row_n3, row_n2, row_n1, row_s1, row_s2, row_s3, row_s4])
    # 将节点以每行进行划分
    dist_n44 = np.array([21.5, 30, 10, 31, 29.5, 20, 34, 12.5, 300, 32, 28, 27.5, 29.5, 12, 10])
    dist_n34 = np.array([9] * 16)
    dist_n33 = np.array([21.5, 30, 10, 31, 29.5, 20, 34, 12.5, 300, 32, 28, 27.5, 29.5, 12, 10])
    dist_n23 = np.array([9] * 16)
    dist_n22 = np.array([21.5, 30, 10, 31, 29.5, 20, 34, 12.5, 300, 32, 28, 27.5, 29.5, 12, 10])
    dist_n12 = np.array([stand_exit.get(row_n1[0])[1]])
    dist_s12 = np.array([stand_exit.get(row_s1[0])[1]])
    dist_s22 = np.array([11, 31, 30, 20, 34, 12.5, 30, 34, 26, 30.5, 22, 16, 10, 38, 22])
    dist_s23 = np.array([14] + [10] * 15)
    dist_s33 = np.array([21.5, 31, 30, 20, 34, 12.5, 30, 34, 26, 30.5, 22, 16, 10, 38, 22])
    dist_s34 = np.array([10] * 16)
    dist_s44 = np.array([21.5, 31, 30, 20, 34, 12.5, 30, 34, 26, 30.5, 22, 16, 10, 38, 22])
    dist = np.array(
        [dist_n44, dist_n34, dist_n33, dist_n23, dist_n22, dist_n12, dist_s12, dist_s22, dist_s23, dist_s33, dist_s34,
         dist_s44])
    value = dist
    # 以路线长度作为基础权值,不区分横纵_表示
    # value = np.array([31, 13, 30, 13, 30, 10, 10, 10, 10, 10, 10, 10, 10])

    G = nx.MultiDiGraph()
    G.add_weighted_edges_from([(stand_exit.get(row_n1[0])[0],row_n1[0], dist_n12[0])])
    G.add_weighted_edges_from([(row_n1[0], stand_exit.get(row_n1[0])[0], dist_n12[0])])
    G.add_weighted_edges_from([(stand_exit.get(row_s1[0])[0],row_s1[0], dist_s12[0])])
    G.add_weighted_edges_from([(row_s1[0], stand_exit.get(row_s1[0])[0], dist_s12[0])])
    # 双向停机位进出
    G.add_weighted_edges_from([(row_s2[13], row_n2[15], 143)])
    G.add_weighted_edges_from([(row_n2[14], row_s2[12], 143)])
    G.add_weighted_edges_from([(row_n2[2], row_s2[0], 143)])
    G.add_weighted_edges_from([(row_s2[1], row_n2[3], 143)])
    # 单向T1/T2/T3/T4
    for i in range(np.size(row_s3)):
        # 需要进一步连接
        G.add_weighted_edges_from([(row_n2[i], row_n3[i], dist_n23[i])])
        G.add_weighted_edges_from([(row_n3[i], row_n2[i], dist_n23[i])])
        G.add_weighted_edges_from([(row_n3[i], row_n4[i], dist_n34[i])])
        G.add_weighted_edges_from([(row_n4[i], row_n3[i], dist_n34[i])])
    for i in range(np.size(row_s3) - 1):
        G.add_weighted_edges_from([(row_n2[i], row_n2[i + 1], dist_n22[i])])
        G.add_weighted_edges_from([(row_n2[i + 1], row_n2[i], dist_n22[i])])
        G.add_weighted_edges_from([(row_n3[i], row_n3[i + 1], dist_n33[i])])
        G.add_weighted_edges_from([(row_n3[i + 1], row_n3[i], dist_n33[i])])
        G.add_weighted_edges_from([(row_n4[i], row_n4[i + 1], dist_n44[i])])
        G.add_weighted_edges_from([(row_n4[i + 1], row_n4[i], dist_n44[i])])
        # 双向北坪滑行
    for i in range(np.size(row_s3)):
        # G.add_weighted_edges_from([(row_s1[0], row_s2[i], 10)])
        # 需要进一步连接
        G.add_weighted_edges_from([(row_s2[i], row_s3[i], dist_s23[i])])
        G.add_weighted_edges_from([(row_s3[i], row_s2[i], dist_s23[i])])
        G.add_weighted_edges_from([(row_s3[i], row_s4[i], dist_s34[i])])
        G.add_weighted_edges_from([(row_s4[i], row_s3[i], dist_s34[i])])
    for i in range(np.size(row_s3) - 1):
        G.add_weighted_edges_from([(row_s2[i], row_s2[i + 1], dist_s22[i])])
        G.add_weighted_edges_from([(row_s2[i + 1], row_s2[i], dist_s22[i])])
        G.add_weighted_edges_from([(row_s3[i], row_s3[i + 1], dist_s33[i])])
        G.add_weighted_edges_from([(row_s3[i + 1], row_s3[i], dist_s22[i])])
        G.add_weighted_edges_from([(row_s4[i], row_s4[i + 1], dist_s44[i])])
        G.add_weighted_edges_from([(row_s4[i + 1], row_s4[i], dist_s22[i])])
        # 双向南坪滑行
    # coordi = [()]
    G.remove_nodes_from([''])
    # 去掉画图所需空白
    # print(G.edges(data=True))
    while True:
        try:
            ho = str(input("请输入交接位置："))
            if ho in row_n4 or ho in row_s4:
                break
        except:
            raise ValueError

    path,length = findPath(io,G,ho,stand)
    print("path:", path)
    print("length:", length)
    current_path.append(path)
    # 对新生成的路径产生一张新图
    newG = G.copy()
    # 对场面已存在的路径进行搜索，新的路径中的节点
    for paths in current_path[:-1]:
        for cp in path:
            if cp in paths:
                # 有公共节点即存在冲突
                # 追尾冲突,前后计一次即可
                if path[path.index(cp)-1] == paths[paths.index(cp)-1]:
                    if newG[path[path.index(cp) - 1]][cp][0]['weight']<199:
                        newG[path[path.index(cp) - 1]][cp][0]['weight'] += 10
                # 对头冲突，后者weight=199
                elif not cp == path[-1] and path[path.index(cp)+1] == paths[paths.index(cp)-1]:
                    newG[cp][path[path.index(cp) + 1]][0]['weight'] = 199
                else:
                    # newG
                    # 寻找图中双向的edge并改变权重
                    for edge in newG.edges(data=True):
                        if cp in edge:
                            if edge[2]['weight']<199:
                                edge[2]['weight'] += 20
                # print(list(G.neighbors(cp)))
                
                new_path, new_weight = findPath(io, newG, ho, stand)
                current_path[-1] = new_path
                if not path == new_path:
                    print('new_path:', new_path)
                path = new_path
                if new_weight:
                    print('new_weight:', new_weight)
    new_length = 0
    for i, x in enumerate(path):
        if i == len(path) - 1: break
        new_length += G[x][path[i + 1]][0]['weight']
    if not new_length == length:
        print( 'new_length:', new_length)
    # print('new_path:', path)
    # print('newlength', newlength)
    print('current path:', current_path)
    draw(newG, path)

while True:
    main()