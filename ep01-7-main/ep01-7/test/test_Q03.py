############################
# Execute no terminal: python -m unittest test/test_Q03.py
import unittest
import networkx as nx
from parameterized import parameterized
from src.Q03 import intergraph_users  # Pylance: garantir símbolo existente em Q03

# Test Data
Dupo = nx.read_graphml("graphs/IL/state_IL_city_Dupo.graphml", force_multigraph=True)
Millstadt = nx.read_graphml("graphs/IL/state_IL_city_Millstadt.graphml",force_multigraph=True)
Cahokia = nx.read_graphml("graphs/IL/state_IL_city_Cahokia.graphml",force_multigraph=True)
Sauget = nx.read_graphml("graphs/IL/state_IL_city_Sauget.graphml",force_multigraph=True)
Chicago = nx.read_graphml("graphs/IL/state_IL_city_Chicago.graphml",force_multigraph=True)
Godfrey = nx.read_graphml("graphs/IL/state_IL_city_Godfrey.graphml",force_multigraph=True)
OFallon = nx.read_graphml("graphs/IL/state_IL_city_OFallon.graphml",force_multigraph=True)
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

class TestClass_Intergraph_Users(unittest.TestCase):
    
    @parameterized.expand([
        [Dupo, Sauget,
            ['fxeRdFmgY6tbTyidpcdFLw', 'mx1_2BxcIbZ1RKsGG_UPHg', '3u3lXfvbpD_21ZoxAk_Chg'],
            #['Tanya', 'Good Times Saloon', 'Gateway Grizzlies']
            [('fxeRdFmgY6tbTyidpcdFLw', 'mx1_2BxcIbZ1RKsGG_UPHg'), ('fxeRdFmgY6tbTyidpcdFLw', '3u3lXfvbpD_21ZoxAk_Chg')]
            #[('Good Times Saloon', 'Tanya'), ('Gateway Grizzlies', 'Tanya')]
        ],
        [Sauget, Dupo,
            ['fxeRdFmgY6tbTyidpcdFLw', 'mx1_2BxcIbZ1RKsGG_UPHg', '3u3lXfvbpD_21ZoxAk_Chg'],
            #['Tanya', 'Good Times Saloon', 'Gateway Grizzlies']
            [('fxeRdFmgY6tbTyidpcdFLw', 'mx1_2BxcIbZ1RKsGG_UPHg'), ('fxeRdFmgY6tbTyidpcdFLw', '3u3lXfvbpD_21ZoxAk_Chg')]
            #[('Good Times Saloon', 'Tanya'), ('Gateway Grizzlies', 'Tanya')]
        ],
        [Dupo, Millstadt,
            ['ZL8cgMY7b8POMaxKgd6u3g', '62edU1CH_ki2L0FodOzavA', 'hKBQ-PFlcB-t5FK3HUxoyQ', '9SQPIP8ASyy6J7Ujjzi3Ag', 'xdQzGzNu3nIUEvOGPW1tYw', 
             'dQg16IsfcluBTkuUDQuGDQ', 'YqximOhYJza5Bp4hhnSgUQ', 'jopXZhgCjhfx5KjFJKD-vw', 'CSkIucODjUoGRxiIONcSgg', 
             '4hhC-WUKaI-g4QoZEK7yig', 'ttKlWxEaX4trG30xkCDYkA', 'fypGyTRBy5b60RRPG_NQ5g', 'tTyFGm2z4zqMXEN_ZWLVfQ', 
             '0bzkJPZaxJI0aWh20ayBJQ', 'K0xjMTLYdicHvwLKNFlUZw', 'Vr5bxmQ2C0XMXmT1WyamUQ', 'tzT32YLUpNy-Z2FN77aZrQ', 
             'mx1_2BxcIbZ1RKsGG_UPHg', 'TsohTE3w1br2m0Nb-tDRDA', 'NdgNF6Bpk1nLAcKg_j_r9w'],
            #['Jennifer', 'Evan', 'Wanda', 'Jane', 'Zoe', 'Aspin', 'Good Times Saloon', 'Dairyland', 'Triple Lakes Tavern', 'Otts Tavern & Millstadt Fish Stand', 'Happy Days', "Farmer's Inn Restaurant & Bar", "Reinhardt's Restaurant", 'Dollar General', 'Farmers Inn', 'China King', 'Subway', "Smokin K's BBQ & More", "Mariachi's", "Eckert's Millstadt Fun Farm"]
            [('ZL8cgMY7b8POMaxKgd6u3g', 'YqximOhYJza5Bp4hhnSgUQ'), ('ZL8cgMY7b8POMaxKgd6u3g', 'jopXZhgCjhfx5KjFJKD-vw'), 
             ('ZL8cgMY7b8POMaxKgd6u3g', 'CSkIucODjUoGRxiIONcSgg'), ('ZL8cgMY7b8POMaxKgd6u3g', 'ttKlWxEaX4trG30xkCDYkA'),
               ('ZL8cgMY7b8POMaxKgd6u3g', 'tTyFGm2z4zqMXEN_ZWLVfQ'), ('ZL8cgMY7b8POMaxKgd6u3g', '0bzkJPZaxJI0aWh20ayBJQ'), 
               ('ZL8cgMY7b8POMaxKgd6u3g', 'K0xjMTLYdicHvwLKNFlUZw'), ('ZL8cgMY7b8POMaxKgd6u3g', 'tzT32YLUpNy-Z2FN77aZrQ'), 
               ('ZL8cgMY7b8POMaxKgd6u3g', 'TsohTE3w1br2m0Nb-tDRDA'), ('62edU1CH_ki2L0FodOzavA', 'YqximOhYJza5Bp4hhnSgUQ'), 
               ('62edU1CH_ki2L0FodOzavA', 'Vr5bxmQ2C0XMXmT1WyamUQ'), ('62edU1CH_ki2L0FodOzavA', 'NdgNF6Bpk1nLAcKg_j_r9w'), 
               ('hKBQ-PFlcB-t5FK3HUxoyQ', 'K0xjMTLYdicHvwLKNFlUZw'), ('hKBQ-PFlcB-t5FK3HUxoyQ', 'NdgNF6Bpk1nLAcKg_j_r9w'), 
               ('9SQPIP8ASyy6J7Ujjzi3Ag', 'YqximOhYJza5Bp4hhnSgUQ'), ('9SQPIP8ASyy6J7Ujjzi3Ag', 'CSkIucODjUoGRxiIONcSgg'), 
               ('9SQPIP8ASyy6J7Ujjzi3Ag', 'mx1_2BxcIbZ1RKsGG_UPHg'), ('xdQzGzNu3nIUEvOGPW1tYw', 'fypGyTRBy5b60RRPG_NQ5g'), 
               ('xdQzGzNu3nIUEvOGPW1tYw', 'NdgNF6Bpk1nLAcKg_j_r9w'), ('dQg16IsfcluBTkuUDQuGDQ', '4hhC-WUKaI-g4QoZEK7yig'), 
               ('dQg16IsfcluBTkuUDQuGDQ', 'NdgNF6Bpk1nLAcKg_j_r9w')]
            #[('Good Times Saloon', 'Jennifer'), ('Otts Tavern & Millstadt Fish Stand', 'Jennifer'), ("Farmer's Inn Restaurant & Bar", 'Jennifer'), ('Dairyland', 'Evan'), ('Otts Tavern & Millstadt Fish Stand', 'Evan'), ('Happy Days', 'Evan'), ("Farmer's Inn Restaurant & Bar", 'Evan'), ('Dollar General', 'Evan'), ('China King', 'Evan'), ('Subway', 'Evan'), ("Smokin K's BBQ & More", 'Evan'), ("Eckert's Millstadt Fun Farm", 'Evan'), ('Triple Lakes Tavern', 'Wanda'), ("Smokin K's BBQ & More", 'Wanda'), ('Triple Lakes Tavern', 'Jane'), ('Otts Tavern & Millstadt Fish Stand', 'Jane'), ("Mariachi's", 'Jane'), ('Triple Lakes Tavern', 'Zoe'), ("Reinhardt's Restaurant", 'Zoe'), ('Triple Lakes Tavern', 'Aspin'), ('Farmers Inn', 'Aspin')]
        ],
        [Dupo, Cahokia,
            ['fxeRdFmgY6tbTyidpcdFLw', '9SQPIP8ASyy6J7Ujjzi3Ag', 'ZL8cgMY7b8POMaxKgd6u3g', 'hKBQ-PFlcB-t5FK3HUxoyQ', 
             'amm1JkCs7Xv5hFb747AVUg', 'dQg16IsfcluBTkuUDQuGDQ', 'xdQzGzNu3nIUEvOGPW1tYw', 'mx1_2BxcIbZ1RKsGG_UPHg', 
             'TsohTE3w1br2m0Nb-tDRDA', 'NdgNF6Bpk1nLAcKg_j_r9w', '3OOK6-fiNy4RKIVu18atVw', 'q1LlkxzJ1VEzKedgPrcDlw', 
             'cVOC5jLNpP78yf5kh-gx_g', 'O998e7eUN45YDid-GxM1yw', 'svLMFkLybFiadbTo_6g-hg', '59hqWP1E1pfjshhHSu0OxA', 
             'ic2VmDDJcH9I06LU36eiAw', 'v_jBLgeJ1z5uVDzpZ-Wbkw', 'HRZmsTNLtZRBbJUuWjzLTg', 's5tkn1ngXJff90tP_iQ0YA', 'KeT8uehA2gVy6sycGdl_OQ'],
         #['Tanya', 'Jennifer', 'Evan', 'Wanda', 'Renee', 'Zoe', 'Aspin', 'Good Times Saloon', 'Dairyland', 'Triple Lakes Tavern', 'Walmart', "Rally's", 'Classic K Hamburgers', 'Stingers', 'White Castle', 'KFC', 'Schnucks Cahokia', 'Sawmill BBQ', "Captain D's", "Hardee's", "Domino's Pizza"]
        [('fxeRdFmgY6tbTyidpcdFLw', 'mx1_2BxcIbZ1RKsGG_UPHg'), ('fxeRdFmgY6tbTyidpcdFLw', '3OOK6-fiNy4RKIVu18atVw'), 
         ('fxeRdFmgY6tbTyidpcdFLw', 'q1LlkxzJ1VEzKedgPrcDlw'), ('fxeRdFmgY6tbTyidpcdFLw', 'cVOC5jLNpP78yf5kh-gx_g'), 
         ('fxeRdFmgY6tbTyidpcdFLw', 'O998e7eUN45YDid-GxM1yw'), ('fxeRdFmgY6tbTyidpcdFLw', '59hqWP1E1pfjshhHSu0OxA'), 
         ('fxeRdFmgY6tbTyidpcdFLw', 'ic2VmDDJcH9I06LU36eiAw'), ('fxeRdFmgY6tbTyidpcdFLw', 'v_jBLgeJ1z5uVDzpZ-Wbkw'), 
         ('fxeRdFmgY6tbTyidpcdFLw', 'HRZmsTNLtZRBbJUuWjzLTg'), ('fxeRdFmgY6tbTyidpcdFLw', 's5tkn1ngXJff90tP_iQ0YA'), 
         ('fxeRdFmgY6tbTyidpcdFLw', 'KeT8uehA2gVy6sycGdl_OQ'), ('9SQPIP8ASyy6J7Ujjzi3Ag', 'mx1_2BxcIbZ1RKsGG_UPHg'), 
         ('9SQPIP8ASyy6J7Ujjzi3Ag', 'O998e7eUN45YDid-GxM1yw'), ('ZL8cgMY7b8POMaxKgd6u3g', 'TsohTE3w1br2m0Nb-tDRDA'), 
         ('ZL8cgMY7b8POMaxKgd6u3g', '3OOK6-fiNy4RKIVu18atVw'), ('ZL8cgMY7b8POMaxKgd6u3g', 'svLMFkLybFiadbTo_6g-hg'), 
         ('ZL8cgMY7b8POMaxKgd6u3g', 'ic2VmDDJcH9I06LU36eiAw'), ('ZL8cgMY7b8POMaxKgd6u3g', 'HRZmsTNLtZRBbJUuWjzLTg'), 
         ('hKBQ-PFlcB-t5FK3HUxoyQ', 'NdgNF6Bpk1nLAcKg_j_r9w'), ('hKBQ-PFlcB-t5FK3HUxoyQ', 'O998e7eUN45YDid-GxM1yw'), 
         ('hKBQ-PFlcB-t5FK3HUxoyQ', 'v_jBLgeJ1z5uVDzpZ-Wbkw'), ('amm1JkCs7Xv5hFb747AVUg', 'NdgNF6Bpk1nLAcKg_j_r9w'), 
         ('amm1JkCs7Xv5hFb747AVUg', 'v_jBLgeJ1z5uVDzpZ-Wbkw'), ('dQg16IsfcluBTkuUDQuGDQ', 'NdgNF6Bpk1nLAcKg_j_r9w'), 
         ('dQg16IsfcluBTkuUDQuGDQ', 'v_jBLgeJ1z5uVDzpZ-Wbkw'), ('xdQzGzNu3nIUEvOGPW1tYw', 'NdgNF6Bpk1nLAcKg_j_r9w'), 
         ('xdQzGzNu3nIUEvOGPW1tYw', 's5tkn1ngXJff90tP_iQ0YA')]],
         #[('Good Times Saloon', 'Tanya'), ('Walmart', 'Tanya'), ("Rally's", 'Tanya'), ('Classic K Hamburgers', 'Tanya'), ('Stingers', 'Tanya'), ('KFC', 'Tanya'), ('Schnucks Cahokia', 'Tanya'), ('Sawmill BBQ', 'Tanya'), ("Captain D's", 'Tanya'), ("Hardee's", 'Tanya'), ("Domino's Pizza", 'Tanya'), ('Good Times Saloon', 'Jennifer'), ('Stingers', 'Jennifer'), ('Dairyland', 'Evan'), ('Walmart', 'Evan'), ('White Castle', 'Evan'), ('Schnucks Cahokia', 'Evan'), ("Captain D's", 'Evan'), ('Triple Lakes Tavern', 'Wanda'), ('Stingers', 'Wanda'), ('Sawmill BBQ', 'Wanda'), ('Triple Lakes Tavern', 'Renee'), ('Sawmill BBQ', 'Renee'), ('Triple Lakes Tavern', 'Zoe'), ('Sawmill BBQ', 'Zoe'), ('Triple Lakes Tavern', 'Aspin'), ("Hardee's", 'Aspin')]
         [Chicago, Godfrey,
          ['UbTL4Hyh7BCzTAj3QOdFqQ', 'Ys2vnlKbOd7ObgOV_jAlYA', 'PbxGUBMCnQydOwAu4FAzNA', 'uogt8KPrcYxm7dgxm6mUHA'],
          [('UbTL4Hyh7BCzTAj3QOdFqQ', 'PbxGUBMCnQydOwAu4FAzNA'), ('UbTL4Hyh7BCzTAj3QOdFqQ', 'uogt8KPrcYxm7dgxm6mUHA'), 
           ('Ys2vnlKbOd7ObgOV_jAlYA', 'PbxGUBMCnQydOwAu4FAzNA'), ('Ys2vnlKbOd7ObgOV_jAlYA', 'uogt8KPrcYxm7dgxm6mUHA')]],
         [Godfrey, Chicago,
          ['UbTL4Hyh7BCzTAj3QOdFqQ', 'Ys2vnlKbOd7ObgOV_jAlYA', 'PbxGUBMCnQydOwAu4FAzNA', 'uogt8KPrcYxm7dgxm6mUHA'],
          [('UbTL4Hyh7BCzTAj3QOdFqQ', 'PbxGUBMCnQydOwAu4FAzNA'), ('UbTL4Hyh7BCzTAj3QOdFqQ', 'uogt8KPrcYxm7dgxm6mUHA'), 
           ('Ys2vnlKbOd7ObgOV_jAlYA', 'PbxGUBMCnQydOwAu4FAzNA'), ('Ys2vnlKbOd7ObgOV_jAlYA', 'uogt8KPrcYxm7dgxm6mUHA')]],
         [Chicago, Cahokia,
          [],
          []],
          [OFallon, Cahokia,
           ['39eWhdUHyqFdMQQCMTtmAg', 'v_jBLgeJ1z5uVDzpZ-Wbkw', 'fYE_H9XbAr6Mga1colFrtw'],
            [('39eWhdUHyqFdMQQCMTtmAg', 'v_jBLgeJ1z5uVDzpZ-Wbkw'), ('39eWhdUHyqFdMQQCMTtmAg', 'fYE_H9XbAr6Mga1colFrtw')]           
           ],
         [Hartford, Godfrey,
          ['-eNXlBt8f3peANJvNHz6Cw', 'bYENop4BuQepBjM1-BI3fA', 'sG9dTFp2WwWbRJVjj5gH2w', 'VsGuHPC3gC0eXKvVr-oWsg', 'MW3rpMLnVr7I6izfBw-1Hw', 'SaZJPDpHKl57z3giyPcleg', 'AyNciRYmmhHFwGEsMWy_7Q', 'ipllQQ16wlyHKIkCYpWaUw', '24Rr4ALt3fDNROR5LEgp0g', 'YZ2pjKlr_pU4Vr6J9S3EZQ', 'ja7cjawPhBMHsKeL_popDw', 'uKUI5kV_NUpTR4edFBL5jA', 'mbFovrFL60UWpwBfv42RVg', 'LsHyDO0k4O0mxgxcsQ5A8g', 'jGLEklebpTjVLsvYN47ESw', '_TTZv3py4nbeMzgcj4NL1w', 'eM64YFx3lLTDgJYqn4YEpA', 'uogt8KPrcYxm7dgxm6mUHA', 'vE_Y-3EWeu-IWlzpDKagvg', '8M2ZGXzscxGuqID3jFGF2w', 'gI34hM-873fwF1XQ8hOaSg', '1GOEX3GFW7cfyOTCAgcxlg', 'l_oJVXPq5rfgPRoqa3vfDQ', '3lXDdLkEq3SI4z6hCjp7FA'],
          [('-eNXlBt8f3peANJvNHz6Cw', 'MW3rpMLnVr7I6izfBw-1Hw'), ('-eNXlBt8f3peANJvNHz6Cw', 'SaZJPDpHKl57z3giyPcleg'), ('-eNXlBt8f3peANJvNHz6Cw', 'ja7cjawPhBMHsKeL_popDw'), ('-eNXlBt8f3peANJvNHz6Cw', '8M2ZGXzscxGuqID3jFGF2w'), ('bYENop4BuQepBjM1-BI3fA', 'MW3rpMLnVr7I6izfBw-1Hw'), ('bYENop4BuQepBjM1-BI3fA', 'AyNciRYmmhHFwGEsMWy_7Q'), ('bYENop4BuQepBjM1-BI3fA', '24Rr4ALt3fDNROR5LEgp0g'), ('bYENop4BuQepBjM1-BI3fA', 'YZ2pjKlr_pU4Vr6J9S3EZQ'), ('bYENop4BuQepBjM1-BI3fA', 'ja7cjawPhBMHsKeL_popDw'), ('bYENop4BuQepBjM1-BI3fA', 'uKUI5kV_NUpTR4edFBL5jA'), ('bYENop4BuQepBjM1-BI3fA', 'mbFovrFL60UWpwBfv42RVg'), ('bYENop4BuQepBjM1-BI3fA', 'LsHyDO0k4O0mxgxcsQ5A8g'), ('bYENop4BuQepBjM1-BI3fA', 'jGLEklebpTjVLsvYN47ESw'), ('bYENop4BuQepBjM1-BI3fA', 'eM64YFx3lLTDgJYqn4YEpA'), ('bYENop4BuQepBjM1-BI3fA', 'uogt8KPrcYxm7dgxm6mUHA'), ('bYENop4BuQepBjM1-BI3fA', 'vE_Y-3EWeu-IWlzpDKagvg'), ('bYENop4BuQepBjM1-BI3fA', '8M2ZGXzscxGuqID3jFGF2w'), ('bYENop4BuQepBjM1-BI3fA', 'gI34hM-873fwF1XQ8hOaSg'), ('bYENop4BuQepBjM1-BI3fA', '1GOEX3GFW7cfyOTCAgcxlg'), ('bYENop4BuQepBjM1-BI3fA', 'l_oJVXPq5rfgPRoqa3vfDQ'), ('bYENop4BuQepBjM1-BI3fA', '3lXDdLkEq3SI4z6hCjp7FA'), ('sG9dTFp2WwWbRJVjj5gH2w', 'SaZJPDpHKl57z3giyPcleg'), ('sG9dTFp2WwWbRJVjj5gH2w', 'ipllQQ16wlyHKIkCYpWaUw'), ('sG9dTFp2WwWbRJVjj5gH2w', 'LsHyDO0k4O0mxgxcsQ5A8g'), ('VsGuHPC3gC0eXKvVr-oWsg', 'SaZJPDpHKl57z3giyPcleg'), ('VsGuHPC3gC0eXKvVr-oWsg', '_TTZv3py4nbeMzgcj4NL1w')]
          ],
          [Hartford, Cahokia,
           ['bYENop4BuQepBjM1-BI3fA', 'Hxx8FmhpxiugIrGRh8RDOg', 'MW3rpMLnVr7I6izfBw-1Hw', 'SaZJPDpHKl57z3giyPcleg', 'O998e7eUN45YDid-GxM1yw', 'v_jBLgeJ1z5uVDzpZ-Wbkw'],
           [('bYENop4BuQepBjM1-BI3fA', 'MW3rpMLnVr7I6izfBw-1Hw'), ('bYENop4BuQepBjM1-BI3fA', 'O998e7eUN45YDid-GxM1yw'), ('Hxx8FmhpxiugIrGRh8RDOg', 'MW3rpMLnVr7I6izfBw-1Hw'), ('Hxx8FmhpxiugIrGRh8RDOg', 'SaZJPDpHKl57z3giyPcleg'), ('Hxx8FmhpxiugIrGRh8RDOg', 'v_jBLgeJ1z5uVDzpZ-Wbkw')]
           ]
    ])
    def test_base(self, g1, g2, e_nodes, e_edges):
        result = intergraph_users(g1, g2)
        self.assertCountEqual(result.nodes, e_nodes)
        self.assertCountEqual(result.edges, e_edges)


    def test_None(self):
        self.assertIsNone(intergraph_users(None, Cahokia))
        self.assertIsNone(intergraph_users(Cahokia, None))

    def test_null(self):
        self.assertIsNone(intergraph_users(nx.MultiGraph(),Dupo))
        self.assertIsNone(intergraph_users(Dupo, nx.MultiGraph()))
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
