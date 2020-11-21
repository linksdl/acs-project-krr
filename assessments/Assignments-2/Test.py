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

# O = 3
# P = 8

nodes = []
for o in range(1, 2 + 1):
    for p in range(1, 4 + 1):
        temp = [o, p]
        nodes.append(temp)

print(len(nodes), nodes)

MODELS = [
    {
        'DOMAIN': {1, 2, 3, 4},
        'Owner': {1, 2},
        'Pet': {3, 4},
        'R': {(1, 3), (1, 4), (2, 3), (2, 4)}
    }
]


def combin(lr):
    rlist = []
    for i in range(1, len(lr) + 1):
        temp = list(combinations(lr, i))
        for x in temp:
            rlist.append(x)
    return rlist

# dd = combin([('o_1', 'p_1'), ('o_1', 'p_2'), ('o_2', 'p_1'), ('o_2', 'p_2')])
# # dd = combin([1, 2, 3])
# print(len(dd))
# for d in dd:
#     print('-----------', d)

for node in nodes:

    o_n = node[0]
    p_n = node[1]

    domain_s = set()
    owner_s = set()
    pet = set()

    for i in range(1, o_n + 1):
        d1 = 'o_' + str(i)
        domain_s.add(d1)
        owner_s.add(d1)

    for j in range(1, p_n + 1):
        d2 = 'p_' + str(j)
        domain_s.add(d2)
        pet.add(d2)

    lr = []
    for o in owner_s:
        for p in pet:
            r = (o, p)
            lr.append(r)

    lr_combin = combin(lr)

    k = 1
    for r in lr_combin:

        axiom_1 = True
        axiom_2 = True
        axiom_3 = False
        axiom_4 = False
        axiom_5 = False
        axiom_6 = False
        axiom_7 = True
        axiom_8 = True

        if len(pet) >= 1:
            axiom_3 = True

        if len(pet) <= 2:
            axiom_4 = True

        if len(owner_s) >= 2:
            axiom_5 = True

        if len(owner_s) <= 2:
            axiom_6 = True

        ll = []
        for ri in r:
            ll.append(ri[0])

        ltrue = []
        for oi in owner_s:
            if oi in ll:
                ltrue.append(True)
            else:
                ltrue.append(False)

        if False in ltrue:
            axiom_8 = False


        if axiom_1 and axiom_2 and axiom_3 and axiom_4 and axiom_5 and axiom_6 and axiom_7 and axiom_8:
            print('Domain:', sorted(domain_s))
            print(' Owner:', sorted(owner_s))
            print('   Pet:', sorted(pet))
            print('     R:', sorted(r))
            print('---------------------------', k)
            k += 1

    print('===========================')

