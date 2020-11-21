# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Project : acs-project-krr      
@File    : assignment_test.py
@Author  : Billy Sheng 
@Contact : shengdl999links@gmail.com  
@Date    : 2020/11/20 8:07 下午
@Version  : 1.0.0
@License : Apache License 2.0
@Desc    : None
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Project : acs-project-krr      
@File    : Test.py
@Author  : Billy Sheng 
@Contact : shengdl999links@gmail.com  
@Date    : 2020/11/20 4:57 下午
@Version  : 1.0.0
@License : Apache License 2.0
@Desc    : None
"""

from itertools import combinations

# MODELS = [
#     {
#         "DOMAIN": {1, 2, 3, 4, 5, 6, 7},
#         "City": {1},
#         "Town": {2, 3},
#         "Village": {4, 5, 6, 7},
#         "Road": {(1, 2), (2, 1),
#                  (1, 3), (3, 1),
#                  (2, 4), (4, 2),
#                  (2, 5), (5, 2),
#                  (3, 6), (6, 3),
#                  (3, 7), (7, 3),
#                  },
#         ">": {(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
#               (2, 4), (2, 5), (2, 6), (2, 7),
#               (3, 4), (3, 5), (3, 6), (3, 7),
#               }
#     },
#     # OTHER MODELS SHOULD BE ADDED HERE
# ]

C = 1
T = 3
V = 6

individuals = []
for C in range(1, C + 1):
    for T in range(1, T + 1):
        for V in range(1, V + 1):
            temp = [C, T, V]
            individuals.append(temp)

print(len(individuals), individuals)


# 求组合数
def query_combinations(lr):
    rlist = []
    for i in range(1, len(lr) + 1):
        temp = list(combinations(lr, i))
        for x in temp:
            rlist.append(x)
    return rlist


def query_combinations1(lr, domain_s):
    rlist = []
    num = len(domain_s) - 1
    total_list = list(combinations(lr, num))

    for x in total_list:
        key_list = []
        for m in x:
            key_list.append(m[0])

        data_dict = {}
        for key in key_list:
            data_dict[key] = data_dict.get(key, 0) + 1

        flag = True
        for d in domain_s:
            if data_dict.get(d) is not None:
                if data_dict.get(d) > 3:
                    flag = False
                    continue

        if flag:
            rlist.append(x)
    return rlist


def compute_model():
    models = []
    num_k = 0
    for node in individuals[:]:

        c_n = node[0]
        t_n = node[1]
        v_n = node[2]
        domain = set()
        city = set()
        town = set()
        village = set()

        larger = set()

        for i in range(1, c_n + 1):
            d1 = 'c_' + str(i)
            domain.add(d1)
            city.add(d1)

        for j in range(1, t_n + 1):
            d2 = 't_' + str(j)
            domain.add(d2)
            town.add(d2)

        for k in range(1, v_n + 1):
            d3 = 'v_' + str(k)
            domain.add(d3)
            village.add(d3)

        for c in city:
            for t in town:
                ct = (c, t)
                larger.add(ct)
            for v in village:
                cv = (c, v)
                larger.add(cv)

        for t in town:
            for v in village:
                tv = (t, v)
                larger.add(tv)

        road_list = []
        for di in sorted(domain):
            for dj in sorted(domain):
                if not di == dj and (dj, di) not in road_list:
                    r = (di, dj)
                    if not (r[0][0] == 'v' and r[1][0] == 'v') and not (r[0][0] == 't' and r[1][0] == 't') and not (
                            r[0][0] == 'c' and r[1][0] == 'c'):
                        # print(di, '--->', dj)
                        road_list.append(r)

        # print(' Domain:', sorted(domain))
        # print('   City:', sorted(city))
        # print('   Town:', sorted(town))
        # print('Village:', sorted(village))
        road_num = (c_n + t_n + v_n) * (c_n + t_n + v_n - 1) / 2 - v_n * (v_n - 1) / 2 - t_n * (t_n - 1) / 2
        print('道路数：', road_num, len(road_list), road_list)
        roads = query_combinations1(road_list, domain)
        print('组合数：', len(roads))

        for ri in roads:
            road = set()
            for rrr in ri:
                road.add(rrr)
                road.add((rrr[1], rrr[0]))

            # print('   Road:', sorted(road))
            axiom_1 = True
            axiom_2 = True
            axiom_3 = True
            axiom_4 = False
            axiom_5 = False
            axiom_6 = False
            axiom_7 = True
            axiom_8 = True
            axiom_9 = True
            axiom_0 = True

            if len(city) >= 1:
                axiom_4 = True

            if len(city) == 1:
                axiom_5 = True

            if len(town) >= 2:
                axiom_6 = True

            v_t_c = []
            for t_road in road:
                v_t_c.append(t_road[0] + '_' + t_road[1][0])

            # print(v_t_c)
            f_v = True
            for vtc in village:
                if vtc + '_t' in v_t_c or vtc + '_c' in v_t_c:
                    continue
                else:
                    f_v = False
                    break

            f_t = True
            for vtc in town:
                if vtc + '_c' in v_t_c:
                    continue
                else:
                    f_t = False
                    break

            if f_v and f_t:
                axiom_7 = True

            for v_domain in village:
                count = 0
                for ccc in v_t_c:
                    if v_domain + '_' + 't' == ccc[0:5] or v_domain + '_' + 'c' == ccc[0:5]:
                        count += 1
                if count > 1:
                    axiom_8 = False
                    break

            for t_domain in town:
                count = 0
                for ccc in v_t_c:
                    if t_domain + '_' + 'v' == ccc[0:5] or t_domain + '_' + 't' == ccc[
                                                                                   0:5] or t_domain + '_' + 'c' == ccc[
                                                                                                                   0:5]:
                        count += 1
                if count < 3:
                    axiom_9 = False
                    break

            true_list = [axiom_1, axiom_2, axiom_3, axiom_4, axiom_5, axiom_6, axiom_7, axiom_8, axiom_9, axiom_0]

            if axiom_1 and axiom_2 and axiom_3 and axiom_4 and axiom_5 and axiom_6 and axiom_7 and axiom_8 and axiom_9 and axiom_0:
                num_k += 1
                # print(true_list)
                # print(' Domain:', sorted(domain))
                # print('   City:', sorted(city))
                # print('   Town:', sorted(town))
                # print('Village:', sorted(village))
                # print('   Road:', sorted(road))
                # print('      >:', sorted(larger))


                key_domain = set()
                for dddd in sorted(domain):
                    key_domain.add(dddd)

                key_city = set()
                for cccc in sorted(city):
                    key_city.add(cccc)

                key_town = set()
                for tttt in sorted(town):
                    key_town.add(tttt)

                key_village = set()
                for vvvv in sorted(village):
                    key_village.add(vvvv)

                key_road = set()
                for rrrr in sorted(road):
                    key_road.add(rrrr)

                key_larger = set()
                for llll in sorted(larger):
                    key_larger.add(llll)

                model = {
                    "DOMAIN": key_domain,
                    "City": key_city,
                    "Town": key_town,
                    "Village": key_village,
                    "Road": key_road,
                    ">": key_larger
                }
                models.append(model)
                print('-----------------------------------', num_k)
                if num_k == 286:
                    break

        print('======================', node, '======================')
    return models


model_list = compute_model()
print(model_list)