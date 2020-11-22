# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Project : acs-project-krr      
@File    : all_models.py
@Author  : Billy Sheng 
@Contact : shengdl999links@gmail.com  
@Date    : 2020/11/20 3:55 下午
@Version  : 1.0.0
@License : Apache License 2.0
@Desc    : None
"""


MODELS = [
    # No 1
    {
        "DOMAIN": {1, 2, 3, 4, 5, 6, 7},
        "City": {1},
        "Town": {2, 3},
        "Village": {4, 5, 6, 7},
        "Road": {(1, 2), (2, 1),
                 (1, 3), (3, 1),
                 (2, 4), (4, 2),
                 (2, 5), (5, 2),
                 (3, 6), (6, 3),
                 (3, 7), (7, 3),
                 },
        ">": {(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
              (2, 4), (2, 5), (2, 6), (2, 7),
              (3, 4), (3, 5), (3, 6), (3, 7),
              }
    },
    # OTHER MODELS SHOULD BE ADDED HERE
    # No 2
    {
        "DOMAIN": {1, 2, 3, 4, 5, 6, 7, 8},
        "City": {1},
        "Town": {2, 3},
        "Village": {4, 5, 6, 7, 8},
        "Road": {(1, 2), (2, 1),
                 (1, 3), (3, 1),
                 (1, 8), (8, 1),
                 (2, 4), (4, 2),
                 (2, 5), (5, 2),
                 (3, 6), (6, 3),
                 (3, 7), (7, 3),
                 },
        ">": {(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
              (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
              (3, 4), (3, 5), (3, 6), (3, 7), (2, 8),
              }
    },
    # No 3
    {
        "DOMAIN": {1, 2, 3, 4, 5},
        "City": {1},
        "Town": {2, 3},
        "Village": {4, 5},
        "Road": {(1, 2), (2, 1),
                 (1, 3), (3, 1),
                 (2, 3), (3, 2),
                 (2, 4), (4, 2),
                 (3, 5), (5, 3),
                 },
        ">": {(1, 2), (1, 3), (1, 4), (1, 5),
              (2, 4), (2, 5),
              (3, 4), (3, 5),
              }
    },
    # No 4
    {
        "DOMAIN": {1, 2, 3, 4, 5, 6},
        "City": {1},
        "Town": {2, 3},
        "Village": {4, 5, 6},
        "Road": {(1, 2), (2, 1),
                 (1, 3), (3, 1),
                 (1, 6), (6, 1),
                 (2, 3), (3, 2),
                 (2, 4), (4, 2),
                 (3, 5), (5, 3),
                 },
        ">": {(1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
              (2, 4), (2, 5), (2, 6),
              (3, 4), (3, 5), (3, 6),
              }
    },
    # No 5
    {
        "DOMAIN": {1, 2, 3, 4},
        "City": {1},
        "Town": {2, 3, 4},
        "Village": {},
        "Road": {(1, 2), (2, 1),
                 (1, 3), (3, 1),
                 (1, 4), (4, 1),
                 (2, 3), (3, 2),
                 (2, 4), (4, 2),
                 (3, 4), (4, 3),
                 },
        ">": {(1, 2), (1, 3), (1, 4)}
    },
    # No 6
    {
        "DOMAIN": {1, 2, 3, 4, 5, 6},
        "City": {1},
        "Town": {2, 3, 4},
        "Village": {5, 6},
        "Road": {(1, 2), (2, 1),
                 (1, 3), (3, 1),
                 (1, 4), (4, 1),
                 (2, 3), (3, 2),
                 (2, 4), (4, 2),
                 (3, 6), (6, 3),
                 (4, 5), (5, 4)
                 },
        ">": {(1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
              (2, 5), (2, 6),
              (3, 5), (3, 6),
              (4, 5), (4, 6)
              }
    },
    # No 7
    {
        "DOMAIN": {1, 2, 3, 4, 5, 6, 7, 8},
        "City": {1},
        "Town": {2, 3, 4},
        "Village": {5, 6, 7, 8},
        "Road": {(1, 2), (2, 1),
                 (1, 3), (3, 1),
                 (1, 4), (4, 1),
                 (2, 7), (7, 2),
                 (2, 8), (8, 2),
                 (3, 6), (6, 3),
                 (3, 4), (4, 3),
                 (4, 5), (5, 4)
                 },
        ">": {(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
              (2, 5), (2, 6), (2, 7), (2, 8),
              (3, 5), (3, 6), (3, 7), (3, 8),
              (4, 5), (4, 6), (4, 7), (4, 8),
              }
    },
    # No 8
    {
        "DOMAIN": {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
        "City": {1},
        "Town": {2, 3, 4},
        "Village": {5, 6, 7, 8, 9, 10},
        "Road": {(1, 2), (2, 1),
                 (1, 3), (3, 1),
                 (1, 4), (4, 1),

                 (2, 5), (5, 2),
                 (2, 6), (6, 2),
                 (3, 7), (7, 3),
                 (3, 8), (8, 3),

                 (4, 9), (9, 4),
                 (4, 10), (10, 4)
                 },
        ">": {(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10),
              (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10),
              (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10),
              (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10)
              }
    },
]

nodes = []
links = []
for i in range(len(MODELS)):
    m = "m"+str(i)+"_"
    model = MODELS[i]

    city_nodes = model['City']
    town_nodes = model['Town']
    village_nodes = model['Village']
    road_nodes = model['Road']

    for c in city_nodes:
        cnode = {"name": m+str(c), "symbolSize": 66, "itemStyle": {"normal": {"color": "red"}}}
        nodes.append(cnode)

    for t in town_nodes:
        tnode = {"name": m+str(t), "symbolSize": 30, "itemStyle": {"normal": {"color": "blue"}}}
        nodes.append(tnode)

    for v in village_nodes:
        vnode = {"name": m+str(v), "symbolSize": 10, "itemStyle": {"normal": {"color": "green"}}}
        nodes.append(vnode)


    for r in road_nodes:
        links.append({"source": m+str(r[0]), "target": m+str(r[1])})


import json
import os

from pyecharts import options as opts
from pyecharts.charts import Graph, Page

graph = (
    Graph(init_opts = opts.InitOpts(width="1500px", height="1000px"))
        .add("", nodes, links, repulsion=8000)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Graph-基本示例"))
)
graph.render("assigment.html")

