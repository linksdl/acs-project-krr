# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Project : acs-project-krr      
@File    : owners_and_pets_models.py.py
@Author  : Billy Sheng 
@Contact : shengdl999links@gmail.com  
@Date    : 2020/11/18 4:18 下午
@Version  : 1.0.0
@License : Apache License 2.0
@Desc    : None
"""

MODELS = [
    {
        'DOMAIN': {1, 2, 3, 4},
        'Owner': {1, 2},
        'Pet': {3, 4},
        'R': {(1, 3), (1, 4), (2, 3), (2, 4)}
    },
    {
        'DOMAIN': {1, 2, 3, 4},
        'Owner': {1, 2},
        'Pet': {3, 4},
        'R': {(1, 3), (1, 4), (2, 3)}
    },
    {
        'DOMAIN': {1, 2, 3, 4},
        'Owner': {1, 2},
        'Pet': {3, 4},
        'R': {(1, 3), (2, 3)}
    },
    ## Add more models specified in similar form to the above,
    ## and remove the above, since it does not satisfy the axioms.
]
