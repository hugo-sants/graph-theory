############################
# Execute no terminal: python -m unittest test/test_Q05.py
########################################
import unittest
import networkx as nx
from src.Q05 import business_graph
from parameterized import parameterized

# Test Data
g_s_5_5 = nx.read_graphml("graphs/s_5_5.graphml", force_multigraph=True)
g_s_10_10 = nx.read_graphml("graphs/s_10_10.graphml", force_multigraph=True)
g_s_25_5 = nx.read_graphml("graphs/s_25_5.graphml", force_multigraph=True)
g_s_50_5 = nx.read_graphml("graphs/s_50_5.graphml", force_multigraph=True)
Lincoln = nx.read_graphml("graphs/IL/state_IL_city_Lincoln.graphml", force_multigraph=True)
Dupo = nx.read_graphml("graphs/IL/state_IL_city_Dupo.graphml",force_multigraph=True)
Cahokia = nx.read_graphml("graphs/IL/state_IL_city_Cahokia.graphml",force_multigraph=True)
Hartford = nx.read_graphml("graphs/IL/state_IL_city_Hartford.graphml",force_multigraph=True)

## Funções auxiliares
# Recupera o nome da variável global para identificar dados do teste que falha
def get_var_name(var):
    for name, value in globals().items():  
        if value is var:
            return name
# Retorna o identificador de um vértice a partir do label
def get_Id(g, label):
    for u in g.nodes:
        if g.nodes[u]['label']==label:
            return u    
 
class TestClass_Business_Graph(unittest.TestCase):
    
    @parameterized.expand([
        [g_s_5_5,'',['hJTwBhYBTkiHaDMml_v_sw', 'mhrW9O0O5hXGXGnEYBVoag', 'e4Vwtrqf-wpJfwesgvdgxQ', 'WXX2EtysiTsZd7pzijpb0g', 'ew5TyXOlyCpCRptye1LdxA'],
         [('hJTwBhYBTkiHaDMml_v_sw', 'mhrW9O0O5hXGXGnEYBVoag'), ('hJTwBhYBTkiHaDMml_v_sw', 'e4Vwtrqf-wpJfwesgvdgxQ'), ('hJTwBhYBTkiHaDMml_v_sw', 'ew5TyXOlyCpCRptye1LdxA'), ('mhrW9O0O5hXGXGnEYBVoag', 'e4Vwtrqf-wpJfwesgvdgxQ'), ('mhrW9O0O5hXGXGnEYBVoag', 'ew5TyXOlyCpCRptye1LdxA'), ('e4Vwtrqf-wpJfwesgvdgxQ', 'ew5TyXOlyCpCRptye1LdxA')]],
        [g_s_5_5,'Food',
         ['hJTwBhYBTkiHaDMml_v_sw', 'e4Vwtrqf-wpJfwesgvdgxQ', 'ew5TyXOlyCpCRptye1LdxA'],
         [('hJTwBhYBTkiHaDMml_v_sw', 'e4Vwtrqf-wpJfwesgvdgxQ'), ('hJTwBhYBTkiHaDMml_v_sw', 'ew5TyXOlyCpCRptye1LdxA'), ('e4Vwtrqf-wpJfwesgvdgxQ', 'ew5TyXOlyCpCRptye1LdxA')]],
        [g_s_25_5,'',
         ['_ab50qdWOk0DdB6XOrBitw', '-OKB11ypR4C8wWlonBFIGw', 'gKBqK-FFq7EGOUscBqb1iA', 'JaMZoosomwX7DDjkFOEo3g', 'iSRTaT9WngzB8JJ2YKJUig'],
         [('_ab50qdWOk0DdB6XOrBitw', 'gKBqK-FFq7EGOUscBqb1iA'), ('_ab50qdWOk0DdB6XOrBitw', 'JaMZoosomwX7DDjkFOEo3g'), ('_ab50qdWOk0DdB6XOrBitw', 'iSRTaT9WngzB8JJ2YKJUig'), ('gKBqK-FFq7EGOUscBqb1iA', 'JaMZoosomwX7DDjkFOEo3g')]],
        [g_s_25_5, 'Restaurant',
         ['_ab50qdWOk0DdB6XOrBitw', 'gKBqK-FFq7EGOUscBqb1iA', 'iSRTaT9WngzB8JJ2YKJUig'],
         [('_ab50qdWOk0DdB6XOrBitw', 'gKBqK-FFq7EGOUscBqb1iA'), ('_ab50qdWOk0DdB6XOrBitw', 'iSRTaT9WngzB8JJ2YKJUig')]
        ],
        [Cahokia, 'Restaurant',
         ['q1LlkxzJ1VEzKedgPrcDlw', 'cVOC5jLNpP78yf5kh-gx_g', 'O998e7eUN45YDid-GxM1yw', 'svLMFkLybFiadbTo_6g-hg', '59hqWP1E1pfjshhHSu0OxA', 'YWcH3SLyRIBHIBBgudqZLw', '6BJwqc8rShdKHyizuR0Q5g', 'ysFWQ_XGmiN_sOgHmxKySQ', 'v_jBLgeJ1z5uVDzpZ-Wbkw', 'HRZmsTNLtZRBbJUuWjzLTg', 'QDgGe--XQrPrap3u5EjAmg', 's5tkn1ngXJff90tP_iQ0YA', 'KeT8uehA2gVy6sycGdl_OQ'],
         [('q1LlkxzJ1VEzKedgPrcDlw', 'cVOC5jLNpP78yf5kh-gx_g'), ('q1LlkxzJ1VEzKedgPrcDlw', 'O998e7eUN45YDid-GxM1yw'), ('q1LlkxzJ1VEzKedgPrcDlw', '59hqWP1E1pfjshhHSu0OxA'), ('q1LlkxzJ1VEzKedgPrcDlw', 'YWcH3SLyRIBHIBBgudqZLw'), ('q1LlkxzJ1VEzKedgPrcDlw', 'v_jBLgeJ1z5uVDzpZ-Wbkw'), ('q1LlkxzJ1VEzKedgPrcDlw', 'HRZmsTNLtZRBbJUuWjzLTg'), ('q1LlkxzJ1VEzKedgPrcDlw', 's5tkn1ngXJff90tP_iQ0YA'), ('q1LlkxzJ1VEzKedgPrcDlw', 'KeT8uehA2gVy6sycGdl_OQ'), ('cVOC5jLNpP78yf5kh-gx_g', 'O998e7eUN45YDid-GxM1yw'), ('cVOC5jLNpP78yf5kh-gx_g', '59hqWP1E1pfjshhHSu0OxA'), ('cVOC5jLNpP78yf5kh-gx_g', '6BJwqc8rShdKHyizuR0Q5g'), ('cVOC5jLNpP78yf5kh-gx_g', 'v_jBLgeJ1z5uVDzpZ-Wbkw'), ('cVOC5jLNpP78yf5kh-gx_g', 'HRZmsTNLtZRBbJUuWjzLTg'), ('cVOC5jLNpP78yf5kh-gx_g', 's5tkn1ngXJff90tP_iQ0YA'), ('cVOC5jLNpP78yf5kh-gx_g', 'KeT8uehA2gVy6sycGdl_OQ'), ('O998e7eUN45YDid-GxM1yw', '59hqWP1E1pfjshhHSu0OxA'), ('O998e7eUN45YDid-GxM1yw', '6BJwqc8rShdKHyizuR0Q5g'), ('O998e7eUN45YDid-GxM1yw', 'v_jBLgeJ1z5uVDzpZ-Wbkw'), ('O998e7eUN45YDid-GxM1yw', 'HRZmsTNLtZRBbJUuWjzLTg'), ('O998e7eUN45YDid-GxM1yw', 's5tkn1ngXJff90tP_iQ0YA'), ('O998e7eUN45YDid-GxM1yw', 'KeT8uehA2gVy6sycGdl_OQ'), ('svLMFkLybFiadbTo_6g-hg', '6BJwqc8rShdKHyizuR0Q5g'), ('svLMFkLybFiadbTo_6g-hg', 'HRZmsTNLtZRBbJUuWjzLTg'), ('svLMFkLybFiadbTo_6g-hg', 'QDgGe--XQrPrap3u5EjAmg'), ('59hqWP1E1pfjshhHSu0OxA', 'YWcH3SLyRIBHIBBgudqZLw'), ('59hqWP1E1pfjshhHSu0OxA', 'v_jBLgeJ1z5uVDzpZ-Wbkw'), ('59hqWP1E1pfjshhHSu0OxA', 'HRZmsTNLtZRBbJUuWjzLTg'), ('59hqWP1E1pfjshhHSu0OxA', 's5tkn1ngXJff90tP_iQ0YA'), ('59hqWP1E1pfjshhHSu0OxA', 'KeT8uehA2gVy6sycGdl_OQ'), ('YWcH3SLyRIBHIBBgudqZLw', 'v_jBLgeJ1z5uVDzpZ-Wbkw'), ('6BJwqc8rShdKHyizuR0Q5g', 'v_jBLgeJ1z5uVDzpZ-Wbkw'), ('6BJwqc8rShdKHyizuR0Q5g', 'HRZmsTNLtZRBbJUuWjzLTg'), ('6BJwqc8rShdKHyizuR0Q5g', 'QDgGe--XQrPrap3u5EjAmg'), ('6BJwqc8rShdKHyizuR0Q5g', 's5tkn1ngXJff90tP_iQ0YA'), ('ysFWQ_XGmiN_sOgHmxKySQ', 'HRZmsTNLtZRBbJUuWjzLTg'), ('ysFWQ_XGmiN_sOgHmxKySQ', 'QDgGe--XQrPrap3u5EjAmg'), ('ysFWQ_XGmiN_sOgHmxKySQ', 's5tkn1ngXJff90tP_iQ0YA'), ('ysFWQ_XGmiN_sOgHmxKySQ', 'KeT8uehA2gVy6sycGdl_OQ'), ('v_jBLgeJ1z5uVDzpZ-Wbkw', 'HRZmsTNLtZRBbJUuWjzLTg'), ('v_jBLgeJ1z5uVDzpZ-Wbkw', 's5tkn1ngXJff90tP_iQ0YA'), ('v_jBLgeJ1z5uVDzpZ-Wbkw', 'KeT8uehA2gVy6sycGdl_OQ'), ('HRZmsTNLtZRBbJUuWjzLTg', 'QDgGe--XQrPrap3u5EjAmg'), ('HRZmsTNLtZRBbJUuWjzLTg', 's5tkn1ngXJff90tP_iQ0YA'), ('HRZmsTNLtZRBbJUuWjzLTg', 'KeT8uehA2gVy6sycGdl_OQ'), ('QDgGe--XQrPrap3u5EjAmg', 's5tkn1ngXJff90tP_iQ0YA'), ('s5tkn1ngXJff90tP_iQ0YA', 'KeT8uehA2gVy6sycGdl_OQ')]
        ],
        [Cahokia, 'Fashion',
         ['3OOK6-fiNy4RKIVu18atVw'], []
        ],
        [Hartford, 'Historical Building',
         ['MW3rpMLnVr7I6izfBw-1Hw', 'SaZJPDpHKl57z3giyPcleg'],
         [('MW3rpMLnVr7I6izfBw-1Hw', 'SaZJPDpHKl57z3giyPcleg')]
         ],
        [Hartford, 'Flowers',
         [],[]],
        [Dupo, 'Nightlife',
         ['mx1_2BxcIbZ1RKsGG_UPHg', 'NdgNF6Bpk1nLAcKg_j_r9w'], []],
        [Dupo, 'Restaurant',
         ['mx1_2BxcIbZ1RKsGG_UPHg', 'TsohTE3w1br2m0Nb-tDRDA'],
         [('mx1_2BxcIbZ1RKsGG_UPHg', 'TsohTE3w1br2m0Nb-tDRDA')] ]
    ])
    def test_base(self, g, c, e_nodes, e_edges):
        var_name1 = get_var_name(g)
        result = business_graph(g,c)
        self.assertCountEqual(result.nodes, e_nodes, f"Grafo: {var_name1}")
        self.assertCountEqual(result.edges, e_edges, f"Grafo: {var_name1}")    

    def test_None(self):
        self.assertIsNone(business_graph(None, ''))
        self.assertIsNone(business_graph(g_s_5_5, None))

    def test_null(self):
        self.assertIsNone(business_graph(nx.MultiGraph(),''))

if __name__ == '__main__':
    unittest.main(verbosity=2)
