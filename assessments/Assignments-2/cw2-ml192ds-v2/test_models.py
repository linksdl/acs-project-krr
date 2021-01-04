# try:
#     from roadmap_models import MODELS
# except ImportError:
#     print('Set theoretic models must be named roadmap_models.py in same directory and initialise list of dictionaries in variable `MODELS`')
#     exit(1)

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
                 (3, 7), (7, 3)
                 },
        ">": {(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
              (2, 4), (2, 5), (2, 6), (2, 7),
              (3, 4), (3, 5), (3, 6), (3, 7)
              }
    },
    # OTHER MODELS SHOULD BE ADDED HERE
    #No 2
    {
        "DOMAIN": {1, 2, 3, 4, 5, 6, 7, 8},
        "City": {1},
        "Town": {2, 3},
        "Village": {4, 5, 6, 7, 8},
        "Road": {(1, 2), (2, 1),
                 (1, 3), (3, 1),
                 (1, 4), (4, 1),
                 (2, 5), (5, 2),
                 (2, 6), (6, 2),
                 (3, 7), (7, 3),
                 (3, 8), (8, 3)
                 },
        ">": {(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
              (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
              (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)
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
                 (3, 5), (5, 3)
                 },
        ">": {(1, 2), (1, 3), (1, 4), (1, 5),
              (2, 4), (2, 5),
              (3, 4), (3, 5)
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
                 (3, 5), (5, 3)
                 },
        ">": {(1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
              (2, 4), (2, 5), (2, 6),
              (3, 4), (3, 5), (3, 6)
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
                 (3, 4), (4, 3)
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
              (4, 5), (4, 6), (4, 7), (4, 8)
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
    }

]

from graphviz import Digraph

def calculate_node_sizes():
    '''Returns mapping of nodes to values that maintain relative size given by `">"`'''
    node_sizes = {}
    for node in model["DOMAIN"]:
        # Initialise all node sizes to 1
        node_sizes[node] = 1
    for a, b in model[">"]:
        for node in (a, b):
            if not(node in node_sizes):
                print(f'Road ({a},{b}) uses variable {node} but {node} not in domain')
                exit(4)
            if not(any(node in model[key] for key in ('City', 'Town','Village', 'Road'))):
                print(f'Road ({a},{b}) uses variable {node} which is in domain but not in any of `City`, `Town` and `Village`')
                exit(4)
        for _ in range(len(node_sizes)):
            for a, b in model[">"]:
                node_sizes[a] = max(node_sizes[a], node_sizes[b] + 1)
    return node_sizes

if __name__=='__main__':

    counter = 1
    main_graph = Digraph()
    main_graph.format = 'svg'

    if not(isinstance(MODELS, list)):
        print('`MODELS` must be a list of dictionaries')
        exit(5)

    for model in MODELS:

        if not(isinstance(model, dict)):
            print('The following model is not a dictionary:')
            print(model)
            exit(5)

        print('Loading model', counter)

        # Check each key is in dictionary
        for key in ('DOMAIN', 'City', 'Town', 'Village', 'Road', '>'):
            if not(key in model):
                print(f'Key `{key}` missing from model:\n{model}')
                exit(3)

        # Subgraph for model
        graph = Digraph(f'cluster_{counter}')
        graph.attr(**{'label':f'Model {counter}'})

        node_sizes = calculate_node_sizes()

        for node, size in node_sizes.items():
            if node in model['City']:
                label = 'C'
            elif node in model['Town']:
                label = 'T'
            elif node in model['Village']:
                label = 'V'
            graph.node(f'{counter}-{str(node)}',label, **{'width':str(size),'height':str(size)})

        for a,b in model["Road"]:
            graph.edge(f'{counter}-{str(a)}', f'{counter}-{str(b)}')

        main_graph.subgraph(graph)
        counter += 1
    # Uncomment to save as file
    # main_graph.render(f'model',format='png')
    # print(f'Wrote graph in file model.png')
    main_graph.view() # Display
