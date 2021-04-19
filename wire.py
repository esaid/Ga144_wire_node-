# 11/04/2021
# GA144  18  X  8  nodes
# trouve le chemin entre un node de depart et arrivee
# et permet d eviter les nodes occupees
# genere le code wire pour la liaison entre les nodes

# import matplotlib.pyplot as plt
import networkx as nx

# GA144  18  X  8  nodes
x = 18
y = 8
dicLabels = {}

node = ["000", "001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011", "012", "013", "014", "015",
        "016", "017",
        "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115",
        "116", "117",
        "200", "201", "202", "203", "204", "205", "206", "207", "208", "209", "210", "211", "212", "213", "214", "215",
        "216", "217",
        "300", "301", "302", "303", "304", "305", "306", "307", "308", "309", "310", "311", "312", "313", "314", "315",
        "316", "317",
        "400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415",
        "416", "417",
        "500", "501", "502", "503", "504", "505", "506", "507", "508", "509", "510", "511", "512", "513", "514", "515",
        "516", "517",
        "600", "601", "602", "603", "604", "605", "606", "607", "608", "609", "610", "611", "612", "613", "614", "615",
        "616", "617",
        "700", "701", "702", "703", "704", "705", "706", "707", "708", "709", "710", "711", "712", "713", "714", "715",
        "716", "717"]




# retrouve la cle du dictionnaire dicLabels en fonction de la valeur
def get_key(val):
    for key, value in dicLabels.items():
        if val == value:
            return key


def wirecode(node_Depart, node_Arrivee, list_nodes_occupe):

    # GA144  18  X  8  nodes

    # graphe 2D
    graphewire = nx.grid_2d_graph(y, x)
    pos = dict((n, n) for n in graphewire.nodes())
    # print(pos)

    # affectation des coordonnees au dictionnaire dicLabels
    labels = {}
    k = 0
    for i, j in graphewire.nodes():
        labels[i, j] = str(pos[i, j]) + " : " + node[k]
        dicLabels[pos[i, j]] = node[k]
        k = k + 1

    # Labels : labels : {(0, 0): '(0, 0) : 000', (0, 1): '(0, 1) : 001', (0, 2): '(0, 2) : 002', ....}
    # print(len(labels) , " nodes --> Labels : ",labels)

    # on retrouve la correspondance entre le node et les coordonees , ex 706 -->  (7,6)

    node_depart = get_key(node_Depart)
    node_arrivee = get_key(node_Arrivee)

    for i in range(len(list_nodes_occupe)):
        # on retrouve la correspondance entre les nodes occupes et les coordonnees , ex 706 -->  (7,6)
        list_nodes_occupe[i] = get_key(list_nodes_occupe[i])

    # remove les nodes occupes
    for ll in list_nodes_occupe:
        # print("le node : {} est occupe ".format(ll))
        graphewire.remove_node(ll)

    # on trouve le chemin s pour aller du node depart vers le node arrivee
    s = nx.shortest_path(graphewire, node_depart, node_arrivee)
    # print("Le chemin sera alors : ", s)

    # permet de trouver les directions pour wire

    dicoWire = {'west east': [], 'east west': [], 'south north': [], 'north south': [], 'west north': [],
                'north west': [],
                'south east': [], 'east south': [], 'north east': [], 'east north': [], 'south west': [],
                'west south': []}
    # parcours du chemin des nodes
    # si le chemin est inferieur a 3 nodes , on copie en double le dernier node

    if len(s) < 3:
        s.append(s[len(s) - 1])


    s.append(s[-1])  # recopie le dernier element de la liste
    #  print(s)
    l = len(s) - 1  # l = longueur de la liste -1


    for i in range(l):

        r = direction(s[i], s[i + 1])  # renvoi la direction entre le node et le node suivant
        if i < (l - 1):
            next_node = direction(s[i + 1], s[i + 2])  # renvoi la direction entre le node suivant et le node encore d'apres
            intersection = direction_intersection(r, next_node)
            # on insere le node qui correspond a la direction
            dicoWire[intersection].append(dicLabels.get(s[i + 1]))
        else:
            intersection = r
        if i == 0:
            # pour le premier node
            dicoWire[r].append(dicLabels.get(s[i]))

        # print(dicoWire)
        # print (dicLabels.get(node), r) # node correspondant

    wire = ""

    for key, values in dicoWire.items():
        #  print (key,values)
        #  print (len(values))

        if values:
            # mettre les nodes dans l'ordre
            values.sort()

            if node_Depart in values:
                values.remove(node_Depart)  # enleve le node_Depart de la liste
                wire = wire + "node " + node_Depart + "\n" + str(key).split()[1] + " a!\n"  # code specifique
            if node_Arrivee in values:
                values.remove(node_Arrivee)  # enleve le node_Depart de la liste
                wire = wire + "node " + node_Arrivee + "\n" + str(key).split()[0] + " a!\n"  # code specifique
            if values:
                wire = wire + "node " + ','.join(values) + "\nwire " + str(key) + "\n"

    return wire


def direction(d, a):
    # d[x,y] depart
    # a[x1,y1] arrivee
    direction_ = ''
    x = d[0]
    y = d[1]
    x1 = a[0]
    y1 = a[1]
    # direction west east north south
    # convention  soit node avec - , avec , ou seul suivi de wire  direction
    # node 1-16,202-216,402-416,602-616
    # wire west east
    # node 17,217,417,617
    # wire west north
    # node 0
    # wire north east
    # *** wire west east ***

    if x1 == x and y1 > y:
        # 601 602
        direction_ = "west east"

    if x1 == x and y1 < y:
        # 601 600
        direction_ = "east west"

    if x1 > x and y1 == y:
        # 501 601
        direction_ = "south north"

    if x1 < x and y1 == y:
        # 601 501
        direction_ = "north south"
    return direction_


def direction_intersection(a, b):
    if b == "":
        b = a
    # trouve la direction entre 2 nodes
    c = ["", ""]
    # on decoupe les directions en 2 parties pour a et  b
    a_split = a.split()
    b_split = b.split()
    c[0] = a_split[0]
    c[1] = b_split[1]
    # si une des parties est presente dans l'autre
    if a_split[0] in b:
        c[0] = a_split[0]
    if a_split[1] in b:
        c[1] = a_split[1]

    intersection = c[0] + " " + c[1]
    # on retourne alors la direction
    return intersection


"""
node_Depart = "600"
node_Arrivee = "708"
list_nodes_occupe = ['705', '601', '704']
print("le node de depart : ", node_Depart)
print("le node d'arrivee : ", node_Arrivee)
print("les nodes occupes " , list_nodes_occupe)

print("le code pour les liaisons wire : ")
print(wirecode(node_Depart, node_Arrivee, list_nodes_occupe))
"""