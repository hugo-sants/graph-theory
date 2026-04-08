############################
# Execute no terminal: python -m unittest test/test_Q05.py
########################################
import unittest
import networkx as nx
from src.Q05 import business_polarization
from parameterized import parameterized

# Test Data
s_5_5 = nx.read_graphml("graphs/s_5_5.graphml", force_multigraph=True)
s_10_10 = nx.read_graphml("graphs/s_10_10.graphml", force_multigraph=True)
s_25_5 = nx.read_graphml("graphs/s_25_5.graphml", force_multigraph=True)
Dupo_5_3 = nx.read_graphml("graphs/Dupo_5_3.graphml", force_multigraph=True)
Dupo_10_3 = nx.read_graphml("graphs/Dupo_10_3.graphml", force_multigraph=True)
Dupo_15_3 = nx.read_graphml("graphs/Dupo_15_3.graphml", force_multigraph=True)
Dupo_20_3 = nx.read_graphml("graphs/Dupo_20_3.graphml", force_multigraph=True)
Sauget_3_2 = nx.read_graphml("graphs/Sauget_3_2.graphml", force_multigraph=True)
Sauget_5_2 = nx.read_graphml("graphs/Sauget_5_2.graphml", force_multigraph=True)
Sauget_10_2 = nx.read_graphml("graphs/Sauget_10_2.graphml", force_multigraph=True)
Sauget_20_2 = nx.read_graphml("graphs/Sauget_20_2.graphml", force_multigraph=True)
Cahokia_5_2 = nx.read_graphml("graphs/Cahokia_5_2.graphml", force_multigraph=True)
Cahokia_10_2 = nx.read_graphml("graphs/Cahokia_10_2.graphml", force_multigraph=True)
Belleville_3_10 = nx.read_graphml("graphs/Belleville_3_10.graphml", force_multigraph=True)
Belleville_5_3 = nx.read_graphml("graphs/Belleville_5_3.graphml", force_multigraph=True)
Belleville_15_3 = nx.read_graphml("graphs/Belleville_15_3.graphml", force_multigraph=True)
Belleville_10_3 = nx.read_graphml("graphs/Belleville_10_3.graphml", force_multigraph=True)
Belleville_5_10 = nx.read_graphml("graphs/Belleville_5_10.graphml", force_multigraph=True)
Belleville_5_1 = nx.read_graphml("graphs/Belleville_5_1.graphml", force_multigraph=True)
Columbia_5_2 = nx.read_graphml("graphs/Columbia_5_2.graphml", force_multigraph=True)
Columbia_10_2 = nx.read_graphml("graphs/Columbia_10_2.graphml", force_multigraph=True)
Columbia_15_2 = nx.read_graphml("graphs/Columbia_15_2.graphml", force_multigraph=True)
Edwardsville_5_2 = nx.read_graphml("graphs/Edwardsville_5_2.graphml", force_multigraph=True)
Edwardsville_10_2 = nx.read_graphml("graphs/Edwardsville_10_2.graphml", force_multigraph=True)
Edwardsville_15_2 = nx.read_graphml("graphs/Edwardsville_15_2.graphml", force_multigraph=True)

## Criando Grafos Toy para Teste
def create_toy_graph_polarization_zero():
    g = nx.MultiGraph()
    g.add_node('U1', type='user', name='User1')
    g.add_node('U2', type='user', name='User2')
    g.add_node('B1', type='business', name='Business1')
    g.add_edge('U1', 'B1', type='review', review_stars=2)
    g.add_edge('U2', 'B1', type='review', review_stars=1)
    return g

def create_toy_graph_no_negative():
    g = nx.MultiGraph()
    g.add_node('U1', type='user', name='User1')
    g.add_node('U2', type='user', name='User2')
    g.add_node('B1', type='business', name='Business1')
    g.add_edge('U1', 'B1', type='review', review_stars=5)
    g.add_edge('U2', 'B1', type='review', review_stars=4)
    return g


def create_toy_graph_perfect_division():
    g = nx.MultiGraph()
    g.add_node('U1', type='user', name='User1')
    g.add_node('U2', type='user', name='User2')
    g.add_node('U3', type='user', name='User3')
    g.add_node('U4', type='user', name='User4')
    g.add_node('B1', type='business', name='Business1')
    g.add_edge('U1', 'B1', type='review', review_stars=5)
    g.add_edge('U2', 'B1', type='review', review_stars=5)
    g.add_edge('U3', 'B1', type='review', review_stars=1)
    g.add_edge('U4', 'B1', type='review', review_stars=1)
    return g


def create_toy_graph_well_connected():
    g = nx.MultiGraph()
    g.add_node('U1', type='user', name='User1')
    g.add_node('U2', type='user', name='User2')
    g.add_node('U3', type='user', name='User3')
    g.add_node('U4', type='user', name='User4')
    g.add_node('B1', type='business', name='Business1')
    g.add_node('B2', type='business', name='Business2')
    g.add_node('B3', type='business', name='Business3')
    g.add_node('B4', type='business', name='Business4')
    g.add_edge('U1', 'B1', type='review', review_stars=5)
    g.add_edge('U2', 'B1', type='review', review_stars=4)
    g.add_edge('U3', 'B1', type='review', review_stars=1)
    g.add_edge('U4', 'B1', type='review', review_stars=2)
    g.add_edge('U1', 'B2', type='review', review_stars=5)
    g.add_edge('U2', 'B2', type='review', review_stars=4)
    g.add_edge('U3', 'B2', type='review', review_stars=2)    
    g.add_edge('U1', 'B3', type='review', review_stars=5)
    g.add_edge('U4', 'B3', type='review', review_stars=1)    
    g.add_edge('U2', 'B4', type='review', review_stars=3)
    g.add_edge('U4', 'B4', type='review', review_stars=2)
    g.add_edge('U3', 'B4', type='review', review_stars=1)   
    return g


def create_toy_graph_highly_polarized():
    g = nx.MultiGraph()
    g.add_node('U1', type='user', name='User1')
    g.add_node('U2', type='user', name='User2')
    g.add_node('U3', type='user', name='User3')
    g.add_node('U4', type='user', name='User4')
    g.add_node('U5', type='user', name='User5')
    g.add_node('U6', type='user', name='User6')
    g.add_node('B1', type='business', name='Business1')
    g.add_node('B2', type='business', name='Business2')
    g.add_node('B3', type='business', name='Business3')
    g.add_node('B4', type='business', name='Business4')
    g.add_node('B5', type='business', name='Business5')
    g.add_edge('U1', 'B1', type='review', review_stars=5)
    g.add_edge('U2', 'B1', type='review', review_stars=5)
    g.add_edge('U3', 'B1', type='review', review_stars=5)
    g.add_edge('U4', 'B1', type='review', review_stars=1)
    g.add_edge('U5', 'B1', type='review', review_stars=1)
    g.add_edge('U6', 'B1', type='review', review_stars=1)
    g.add_edge('U1', 'B2', type='review', review_stars=5)
    g.add_edge('U2', 'B2', type='review', review_stars=5)
    g.add_edge('U1', 'B3', type='review', review_stars=4)
    g.add_edge('U3', 'B3', type='review', review_stars=5)
    g.add_edge('U2', 'B3', type='review', review_stars=5)
    g.add_edge('U3', 'B3', type='review', review_stars=4)
    g.add_edge('U4', 'B4', type='review', review_stars=1)
    g.add_edge('U5', 'B4', type='review', review_stars=2)
    g.add_edge('U4', 'B5', type='review', review_stars=2)
    g.add_edge('U6', 'B5', type='review', review_stars=1)   
    g.add_edge('U5', 'B5', type='review', review_stars=1)
    g.add_edge('U6', 'B5', type='review', review_stars=2)    
    return g


def create_toy_graph_neutral_ignored():
    g = nx.MultiGraph()
    g.add_node('U1', type='user', name='User1')
    g.add_node('U2', type='user', name='User2')  # Neutro
    g.add_node('U3', type='user', name='User3')
    g.add_node('B1', type='business', name='Business1')
    g.add_edge('U1', 'B1', type='review', review_stars=5)
    g.add_edge('U2', 'B1', type='review', review_stars=3)  # será ignorado
    g.add_edge('U3', 'B1', type='review', review_stars=1)
    return g


def create_toy_graph_multiple_reviews():
    g = nx.MultiGraph()
    g.add_node('U1', type='user', name='User1')
    g.add_node('U2', type='user', name='User2')
    g.add_node('B1', type='business', name='Business1')
    g.add_edge('U1', 'B1', type='review', review_stars=5)
    g.add_edge('U1', 'B1', type='review', review_stars=5)
    g.add_edge('U1', 'B1', type='review', review_stars=4)
    g.add_edge('U2', 'B1', type='review', review_stars=1)
    g.add_edge('U2', 'B1', type='review', review_stars=2)
    return g

g_zero = create_toy_graph_polarization_zero()
g_no_neg = create_toy_graph_no_negative()
g_perfect_div = create_toy_graph_perfect_division()
g_well_conn = create_toy_graph_well_connected()
g_high_pol = create_toy_graph_highly_polarized()
g_neutral = create_toy_graph_neutral_ignored()
g_multi_reviews = create_toy_graph_multiple_reviews()

## Funções auxiliares
# Recupera o nome da variável global para identificar dados do teste que falha
def get_var_name(var):
    for name, value in globals().items():  
        if value is var:
            return name

 
class TestClass_Business_Graph(unittest.TestCase):
    
    @parameterized.expand([
        [ s_5_5, 'hJTwBhYBTkiHaDMml_v_sw', 0.0 ],
        [ s_5_5, 'mhrW9O0O5hXGXGnEYBVoag', 0.8 ],
        [ s_10_10, 'u7_3L1NBWgxhBM_B-cmmnA', 0.0 ],
        [ s_25_5, '_ab50qdWOk0DdB6XOrBitw', 0.0 ],
        [ Dupo_5_3, 'mx1_2BxcIbZ1RKsGG_UPHg', 0.63 ],
        [ Dupo_10_3, 'TsohTE3w1br2m0Nb-tDRDA', 0.0 ],
        [ Dupo_10_3, 'mx1_2BxcIbZ1RKsGG_UPHg', 0.6 ],
        [ Dupo_15_3, 'WAB73KCeALEJkhdkg0Imlg', 0.0 ],
        [ Dupo_15_3, 'uT33RCQUJioJnFEh1C1u7g', 0.13 ],
        [ Dupo_15_3, 'omKVwCFLQYs_ySD1bPk6iw', 0.32 ],
        [ Dupo_15_3, 'YdbWLShEm-CAssaJ8bdipA', 0.6 ],
        [ Dupo_15_3, 'wzYmWoo7kgokWSJTpqAwAA', 0.13 ],
        [ Dupo_15_3, 'S9tdibDgtvdWLiyINyi4nw', 0.28 ],
        [ Dupo_15_3, 'zMe0kY6KMRVdlUKmme-JpA', 0.3 ],
        [ Dupo_15_3, 'S9SYcMTJvKqImncnEZ7tFw', 0.29 ],
        [ Dupo_15_3, 'wTrE0XUyPtRa2qRVPj4Vog', 0.27 ],
        [ Dupo_15_3, 'DO4Xi30b8kxEv3B5T8rAvg', 0.23 ],
        [ Dupo_15_3, 'iGudoXTmbAmz1gg3H7omyA', 0.17 ],
        [ Dupo_15_3, 'rIoYB0oURnPmou5bppJX6w', 0.39 ],
        [ Dupo_15_3, 'W_KX5Qgpk9mZEMDJJoqfLw', 0.33 ],
        [ Dupo_20_3, 'uT33RCQUJioJnFEh1C1u7g', 0.13 ],
        [ Dupo_20_3, 'RjtjAM1So4Gqd7ytN7OmHA', 0.0 ],
        [ Dupo_20_3, 'zMe0kY6KMRVdlUKmme-JpA', 0.32 ],
        [ Dupo_20_3, 'rIoYB0oURnPmou5bppJX6w', 0.39 ],
        [ Dupo_20_3, 'wTrE0XUyPtRa2qRVPj4Vog', 0.27 ],
        [ Dupo_20_3, 'YdbWLShEm-CAssaJ8bdipA', 0.6 ],
        [ Dupo_20_3, 'DO4Xi30b8kxEv3B5T8rAvg', 0.23 ],
        [ Dupo_20_3, 'wzYmWoo7kgokWSJTpqAwAA', 0.13 ],
        [ Dupo_20_3, 'W_KX5Qgpk9mZEMDJJoqfLw', 0.33 ],
        [ Dupo_20_3, 'omKVwCFLQYs_ySD1bPk6iw', 0.3 ],
        [ Dupo_20_3, 'S9tdibDgtvdWLiyINyi4nw', 0.31 ],
        [ Dupo_20_3, 'iGudoXTmbAmz1gg3H7omyA', 0.17 ],
        [ Dupo_20_3, 'WrJ76ufOQn2RGGOY7ugbbQ', 0.2 ],
        [ Dupo_20_3, 'S9SYcMTJvKqImncnEZ7tFw', 0.19 ],
        [ Dupo_20_3, 'nwN92Uje-xIKE5voPTTvBQ', 0.6 ],
        [ Dupo_20_3, 'Lh2XM7uYk_amz3SFIBeJMQ', 0.17 ],
        [ Sauget_3_2, '3u3lXfvbpD_21ZoxAk_Chg', 0.0 ],
        [ Sauget_5_2, '3u3lXfvbpD_21ZoxAk_Chg', 0.0 ],
        [ Sauget_10_2, 'xXYYMUKs6mAGdLAXiTScvg', 0.0 ],
        [ Sauget_20_2, 'xXYYMUKs6mAGdLAXiTScvg', 0.0 ],
        [ Cahokia_5_2, 'cVOC5jLNpP78yf5kh-gx_g', 0.0 ],
        [ Cahokia_10_2, 'KeT8uehA2gVy6sycGdl_OQ', 0.0 ],
        [ Cahokia_10_2, 'v_jBLgeJ1z5uVDzpZ-Wbkw', 0.36 ],
        [ Cahokia_10_2, '3OOK6-fiNy4RKIVu18atVw', 0.17 ],
        [ Belleville_3_10, 'SfzPMs5U9KcZCi6fJZArjQ', 0.0 ],
        [ Belleville_3_10, 'uT33RCQUJioJnFEh1C1u7g', 0.13 ],
        [ Belleville_3_10, '2UtP4mly2LFZpXtqiwb24g', 0.6 ],
        [ Belleville_3_10, 'YdbWLShEm-CAssaJ8bdipA', 0.6 ],
        [ Belleville_5_3, 'PUuHnOMtsnFZCeTwQ2AbcQ', 0.0 ],
        [ Belleville_5_3, 'omKVwCFLQYs_ySD1bPk6iw', 0.33 ],
        [ Belleville_5_3, 'YdbWLShEm-CAssaJ8bdipA', 0.6 ],
        [ Belleville_5_3, 'uT33RCQUJioJnFEh1C1u7g', 0.13 ],
        [ Belleville_5_3, '2UtP4mly2LFZpXtqiwb24g', 0.6 ],
        [ Belleville_15_3, '5DwRX43KmGroXBlltpCGqA', 0.0 ],
        [ Belleville_15_3, 'S9SYcMTJvKqImncnEZ7tFw', 0.29 ],
        [ Belleville_15_3, 'W_KX5Qgpk9mZEMDJJoqfLw', 0.33 ],
        [ Belleville_15_3, 'zMe0kY6KMRVdlUKmme-JpA', 0.3 ],
        [ Belleville_15_3, 'wTrE0XUyPtRa2qRVPj4Vog', 0.27 ],
        [ Belleville_15_3, 'uT33RCQUJioJnFEh1C1u7g', 0.13 ],
        [ Belleville_15_3, 'omKVwCFLQYs_ySD1bPk6iw', 0.32 ],
        [ Belleville_15_3, 'YdbWLShEm-CAssaJ8bdipA', 0.6 ],
        [ Belleville_15_3, 'wzYmWoo7kgokWSJTpqAwAA', 0.13 ],
        [ Belleville_15_3, 'DO4Xi30b8kxEv3B5T8rAvg', 0.23 ],
        [ Belleville_15_3, 'rIoYB0oURnPmou5bppJX6w', 0.39 ],
        [ Belleville_15_3, 'iGudoXTmbAmz1gg3H7omyA', 0.17 ],
        [ Belleville_15_3, 'S9tdibDgtvdWLiyINyi4nw', 0.28 ],
        [ Belleville_10_3, 'iGudoXTmbAmz1gg3H7omyA', 0.0 ],
        [ Belleville_10_3, 'omKVwCFLQYs_ySD1bPk6iw', 0.44 ],
        [ Belleville_10_3, 'YdbWLShEm-CAssaJ8bdipA', 0.6 ],
        [ Belleville_10_3, 'W_KX5Qgpk9mZEMDJJoqfLw', 0.27 ],
        [ Belleville_10_3, 'uT33RCQUJioJnFEh1C1u7g', 0.13 ],
        [ Belleville_10_3, '2UtP4mly2LFZpXtqiwb24g', 0.6 ],
        [ Belleville_10_3, 'S9tdibDgtvdWLiyINyi4nw', 0.18 ],
        [ Belleville_10_3, 'wTrE0XUyPtRa2qRVPj4Vog', 0.2 ],
        [ Belleville_10_3, 'S9SYcMTJvKqImncnEZ7tFw', 0.16 ],
        [ Belleville_10_3, 'zMe0kY6KMRVdlUKmme-JpA', 0.38 ],
        [ Belleville_5_10, 'eVPJcdu8vlsjrWFC3VHiMA', 0.0 ],
        [ Belleville_5_10, 'DO4Xi30b8kxEv3B5T8rAvg', 0.23 ],
        [ Belleville_5_10, 'W_KX5Qgpk9mZEMDJJoqfLw', 0.17 ],
        [ Belleville_5_10, 'wzYmWoo7kgokWSJTpqAwAA', 0.13 ],
        [ Belleville_5_10, 'YdbWLShEm-CAssaJ8bdipA', 0.6 ],
        [ Belleville_5_10, 'uT33RCQUJioJnFEh1C1u7g', 0.13 ],
        [ Belleville_5_10, 'zMe0kY6KMRVdlUKmme-JpA', 0.38 ],
        [ Belleville_5_1, 'fdpalN2LrEfWVqOm3eO8dQ', 0.0 ],
        [ Belleville_5_1, 'YdbWLShEm-CAssaJ8bdipA', 0.6 ],
        [ Belleville_5_1, 'omKVwCFLQYs_ySD1bPk6iw', 0.33 ],
        [ Belleville_5_1, '2UtP4mly2LFZpXtqiwb24g', 0.6 ],
        [ Belleville_5_1, 'uT33RCQUJioJnFEh1C1u7g', 0.13 ],
        [ Columbia_5_2, 'qQrNp9Q_-1GC1eRGv-HZLg', 0.0 ],
        [ Columbia_5_2, 'IMCfwsS5hMrgSkyz_RlqLw', 0.27 ],
        [ Columbia_10_2, 's7JxSEtIumoFod2Jdj0_-g', 0.0 ],
        [ Columbia_10_2, '4pPtSIMVH9r5aLHQ0HKSDw', 0.36 ],
        [ Columbia_10_2, 'vw4W_syB2Xq82USH_LF79Q', 0.09 ],
        [ Columbia_10_2, 'IMCfwsS5hMrgSkyz_RlqLw', 0.27 ],
        [ Columbia_15_2, 'KtpZkMxiOp1V9NEqMSMO3w', 0.0 ],
        [ Columbia_15_2, 'DIOROHqtXQDHQZMOMT-YzQ', 0.13 ],
        [ Columbia_15_2, 'zq2WjEegVGBejN3yqE1nSw', 0.23 ],
        [ Columbia_15_2, 'SPfdgCODDJE1zTj5fACOGw', 0.17 ],
        [ Columbia_15_2, 'm7a94wUd2yWKtmxKb_Dbrw', 0.2 ],
        [ Columbia_15_2, 'IMCfwsS5hMrgSkyz_RlqLw', 0.3 ],
        [ Columbia_15_2, 'vw4W_syB2Xq82USH_LF79Q', 0.15 ],
        [ Columbia_15_2, '4pPtSIMVH9r5aLHQ0HKSDw', 0.36 ],
        [ Edwardsville_5_2, 'L9FeMn-zHsR8O-ssVP3QEA', 0.0 ],
        [ Edwardsville_5_2, 'VvQEU1BuLoctkPlOTKm0SQ', 0.16 ],
        [ Edwardsville_5_2, '0bVcCefYVtvU8MjXC5Na_Q', 0.16 ],
        [ Edwardsville_5_2, 'UF4XfzG0kvcVQTlpa4i5lA', 0.4 ],
        [ Edwardsville_5_2, 'EvBeuDww_OCNQZ-dRy6qzA', 0.2 ],
        [ Edwardsville_5_2, 'gXg277YblY5xsaeMzJ73TA', 0.13 ],
        [ Edwardsville_5_2, 'wMGjF3eTtmkOPudjV_z--Q', 0.23 ],
        [ Edwardsville_5_2, 'G9ez1w58i_ReNqnlRoSpBA', 0.13 ],
        [ Edwardsville_5_2, 'ApcMztKwhVYYCceDX1L5qQ', 0.13 ],
        [ Edwardsville_5_2, 'OOaxVCZVCmw_kaDt1wIbnQ', 0.17 ],
        [ Edwardsville_5_2, 'JQUQ_wa8JIiSe3YIms6b6A', 0.17 ],
        [ Edwardsville_5_2, 'zwGvMQ7Nw0VwqLUYDuxRXQ', 0.12 ],
        [ Edwardsville_5_2, '4wep1OfeJbpz0DvBsoDdVg', 0.27 ],
        [ Edwardsville_5_2, 'lBtxj8nQqOmuF0b__WHWAA', 0.2 ],
        [ Edwardsville_5_2, 'OrWEym3KXdX45kFlxlIF4g', 0.13 ],
        [ Edwardsville_5_2, 'AF4eN-oI7IWwjv0M9BiHxQ', 0.13 ],
        [ Edwardsville_5_2, 'safMQyVBMEmShEaXM140Ug', 0.2 ],
        [ Edwardsville_5_2, 'wbLXXbI-T6Av71i9AoiZRQ', 0.33 ],
        [ Edwardsville_5_2, 'UBQfKxAWEXzMWzej3y2BGQ', 0.13 ],
        [ Edwardsville_5_2, 'iGdpNaFSHjjwEuUvMykm1w', 0.27 ],
        [ Edwardsville_5_2, 'IMHEEaSvQeaiRlI5rcVjdA', 0.13 ],
        [ Edwardsville_10_2, 'HPZCMZW8ADX1Qgyul4cAcQ', 0.0 ],
        [ Edwardsville_10_2, '0bVcCefYVtvU8MjXC5Na_Q', 0.08 ],
        [ Edwardsville_10_2, '2yrg5ZIlKufnRpP5GEbPiQ', 0.17 ],
        [ Edwardsville_10_2, 'gXg277YblY5xsaeMzJ73TA', 0.25 ],
        [ Edwardsville_10_2, '_cK526t2R3gqCHpEbwbUtg', 0.27 ],
        [ Edwardsville_10_2, '4wep1OfeJbpz0DvBsoDdVg', 0.33 ],
        [ Edwardsville_10_2, 'wbLXXbI-T6Av71i9AoiZRQ', 0.43 ],
        [ Edwardsville_10_2, 'b9IENYGikpojhg2s2wMBVQ', 0.24 ],
        [ Edwardsville_10_2, '-DHwIpXvOsJFqYuo585eOg', 0.27 ],
        [ Edwardsville_10_2, 'vwv7M49sCxh7pIa-cAVb4w', 0.2 ],
        [ Edwardsville_10_2, '4R6iamGpCr9vNiddyHPuIQ', 0.2 ],
        [ Edwardsville_10_2, 'iGdpNaFSHjjwEuUvMykm1w', 0.4 ],
        [ Edwardsville_10_2, 'OrWEym3KXdX45kFlxlIF4g', 0.2 ],
        [ Edwardsville_10_2, 'GTUvFEipY0bNAjQzDgDk9w', 0.2 ],
        [ Edwardsville_10_2, 'MuL05rKkVBFg2BksY5XEWg', 0.37 ],
        [ Edwardsville_10_2, '3XFmxKMesVkeEstwoiWEMA', 0.2 ],
        [ Edwardsville_10_2, 'wMGjF3eTtmkOPudjV_z--Q', 0.3 ],
        [ Edwardsville_10_2, 'JQUQ_wa8JIiSe3YIms6b6A', 0.17 ],
        [ Edwardsville_10_2, 'UBQfKxAWEXzMWzej3y2BGQ', 0.13 ],
        [ Edwardsville_10_2, 'safMQyVBMEmShEaXM140Ug', 0.33 ],
        [ Edwardsville_10_2, 'lBtxj8nQqOmuF0b__WHWAA', 0.2 ],
        [ Edwardsville_10_2, 'jgfWkoSlePEA9mqtAIgAdA', 0.23 ],
        [ Edwardsville_10_2, 'G9ez1w58i_ReNqnlRoSpBA', 0.13 ],
        [ Edwardsville_10_2, 'zwGvMQ7Nw0VwqLUYDuxRXQ', 0.24 ],
        [ Edwardsville_10_2, 'AF4eN-oI7IWwjv0M9BiHxQ', 0.25 ],
        [ Edwardsville_10_2, 'FfvLkFFWMFym6VHHRec6cQ', 0.25 ],
        [ Edwardsville_10_2, 'IMHEEaSvQeaiRlI5rcVjdA', 0.23 ],
        [ Edwardsville_10_2, 'OOaxVCZVCmw_kaDt1wIbnQ', 0.3 ],
        [ Edwardsville_10_2, 'VvQEU1BuLoctkPlOTKm0SQ', 0.16 ],
        [ Edwardsville_10_2, '0PGxzpoXZKYNRFD_7_thpA', 0.8 ],
        [ Edwardsville_10_2, 'ApcMztKwhVYYCceDX1L5qQ', 0.23 ],
        [ Edwardsville_10_2, 'iKeEhlGU9R8vUchNwF5__Q', 0.53 ],
        [ Edwardsville_10_2, 'EvBeuDww_OCNQZ-dRy6qzA', 0.47 ],
        [ Edwardsville_15_2, '4wep1OfeJbpz0DvBsoDdVg', 0.42 ],
        [ Edwardsville_15_2, '8aclz-WVqoIT_P4_83Hj9w', 0.0 ],
        [ Edwardsville_15_2, 'vwv7M49sCxh7pIa-cAVb4w', 0.2 ],
        [ Edwardsville_15_2, 'KOOutUHYJWJKsC71JKHV5Q', 0.2 ],
        [ Edwardsville_15_2, 'FfvLkFFWMFym6VHHRec6cQ', 0.25 ],
        [ Edwardsville_15_2, 'c1XNKIP9OW3Uxd7BKLgirQ', 0.13 ],
        [ Edwardsville_15_2, '-DHwIpXvOsJFqYuo585eOg', 0.25 ],
        [ Edwardsville_15_2, '2yrg5ZIlKufnRpP5GEbPiQ', 0.17 ],
        [ Edwardsville_15_2, '3X7SeQzmfLTZM5nipFsi2w', 0.27 ],
        [ Edwardsville_15_2, 'zwGvMQ7Nw0VwqLUYDuxRXQ', 0.26 ],
        [ Edwardsville_15_2, 'RLaS9hQJXAc7ED2wr9dWeA', 0.3 ],
        [ Edwardsville_15_2, 'p3mXalNahqhMXygBBBeA3A', 0.2 ],
        [ Edwardsville_15_2, 'OrWEym3KXdX45kFlxlIF4g', 0.2 ],
        [ Edwardsville_15_2, 'wbLXXbI-T6Av71i9AoiZRQ', 0.44 ],
        [ Edwardsville_15_2, 'safMQyVBMEmShEaXM140Ug', 0.39 ],
        [ Edwardsville_15_2, 'EvBeuDww_OCNQZ-dRy6qzA', 0.29 ],
        [ Edwardsville_15_2, 'VvQEU1BuLoctkPlOTKm0SQ', 0.16 ],
        [ Edwardsville_15_2, 'ApcMztKwhVYYCceDX1L5qQ', 0.29 ],
        [ Edwardsville_15_2, 'wMGjF3eTtmkOPudjV_z--Q', 0.33 ],
        [ Edwardsville_15_2, 'iKeEhlGU9R8vUchNwF5__Q', 0.56 ],
        [ Edwardsville_15_2, '4R6iamGpCr9vNiddyHPuIQ', 0.2 ],
        [ Edwardsville_15_2, 'gumsFcxRAVU-dAqmYQ5ewA', 0.2 ],
        [ Edwardsville_15_2, 'iGdpNaFSHjjwEuUvMykm1w', 0.3 ],
        [ Edwardsville_15_2, '_cK526t2R3gqCHpEbwbUtg', 0.27 ],
        [ Edwardsville_15_2, 'v-hYRlZ7d3RvaXmL3aQdvw', 0.13 ],
        [ Edwardsville_15_2, 'lBtxj8nQqOmuF0b__WHWAA', 0.24 ],
        [ Edwardsville_15_2, 'AF4eN-oI7IWwjv0M9BiHxQ', 0.27 ],
        [ Edwardsville_15_2, 'IMHEEaSvQeaiRlI5rcVjdA', 0.31 ],
        [ Edwardsville_15_2, 'MuL05rKkVBFg2BksY5XEWg', 0.37 ],
        [ Edwardsville_15_2, 'jgfWkoSlePEA9mqtAIgAdA', 0.23 ],
        [ Edwardsville_15_2, 'OOaxVCZVCmw_kaDt1wIbnQ', 0.3 ],
        [ Edwardsville_15_2, 'G9ez1w58i_ReNqnlRoSpBA', 0.2 ],
        [ Edwardsville_15_2, '-xOLxvu-xEUXPKSW263oNQ', 0.27 ],
        [ Edwardsville_15_2, 'JQUQ_wa8JIiSe3YIms6b6A', 0.17 ],
        [ Edwardsville_15_2, 'YFvlIkP3lwwyiyGY39hihA', 0.17 ],
        [ Edwardsville_15_2, 'UBQfKxAWEXzMWzej3y2BGQ', 0.13 ],
        [ Edwardsville_15_2, 'GTUvFEipY0bNAjQzDgDk9w', 0.2 ],
        [ Edwardsville_15_2, '0PGxzpoXZKYNRFD_7_thpA', 0.8 ],
        [ Edwardsville_15_2, 'gXg277YblY5xsaeMzJ73TA', 0.31 ],
        [ Edwardsville_15_2, '0bVcCefYVtvU8MjXC5Na_Q', 0.08 ],
        [ Edwardsville_15_2, '3XFmxKMesVkeEstwoiWEMA', 0.2 ],
        [ Edwardsville_15_2, 'b9IENYGikpojhg2s2wMBVQ', 0.11 ],
    ])
    def test_base(self, g, b, expected):
        var_name1 = get_var_name(g)
        result = business_polarization(g,b)
        self.assertEqual(round(result,1), round(expected,1), f"Graph {var_name1}, {b}")    

    def test_none (self):
        self.assertIsNone(business_polarization(None, 'hJTwBhYBTkiHaDMml_v_sw'))
        self.assertIsNone(business_polarization(s_5_5, None))

    def test_null (self):
        self.assertIsNone(business_polarization(nx.MultiGraph(), 'hJTwBhYBTkiHaDMml_v_sw'))

    def test_invalid_b (self):
        self.assertIsNone(business_polarization(s_5_5, 'b'))

    def test_toy_only_negative_users(self):
        result = business_polarization(g_zero, 'B1')
        self.assertEqual(result, 0.0)
    
    def test_toy_only_positive_users(self):
        result = business_polarization(g_no_neg, 'B1')
        self.assertEqual(result, 0.0)
    
    def test_toy_perfect_division_no_edges(self):
        result = business_polarization(g_perfect_div, 'B1')
        self.assertEqual(result, 0.8)
    
    def test_toy_well_connected_groups(self):
        result = business_polarization(g_well_conn, 'B1')
        self.assertLess(result, 0.4)
        self.assertGreater(result, 0.0)
    
    def test_toy_highly_polarized(self):
        result = business_polarization(g_high_pol, 'B1')
        self.assertEqual(result, 0.8)
    
    def test_toy_neutral_ratings_ignored(self):
        result = business_polarization(g_neutral, 'B1')
        self.assertEqual(result, 0.8)
    
    def test_toy_business_not_in_graph(self):
        result = business_polarization(g_zero, 'B_invalid')
        self.assertIsNone(result)
    
    def test_toy_empty_graph(self):
        empty_g = nx.MultiGraph()
        result = business_polarization(empty_g, 'B1')
        self.assertIsNone(result)
    
    def test_toy_multiple_reviews_same_user(self):
        result = business_polarization(g_multi_reviews, 'B1')
        self.assertEqual(result, 0.4)



if __name__ == '__main__':
    unittest.main(verbosity=2)
