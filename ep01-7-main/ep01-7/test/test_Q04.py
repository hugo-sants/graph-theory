############################
# Execute no terminal: python -m unittest test/test_Q04.py
import unittest
import networkx as nx
from src.Q04 import find_business
from parameterized import parameterized

# Dados de teste: grafos pequenos para validação 
g_s_5_5 = nx.read_graphml("graphs/s_5_5.graphml", force_multigraph=True)
g_s_25_5 = nx.read_graphml("graphs/s_25_5.graphml", force_multigraph=True)
Millstadt = nx.read_graphml("graphs/IL/state_IL_city_Millstadt.graphml", force_multigraph=True)
Dupo = nx.read_graphml("graphs/IL/state_IL_city_Dupo.graphml",force_multigraph=True)
Cahokia = nx.read_graphml("graphs/IL/state_IL_city_Cahokia.graphml",force_multigraph=True)
Lincoln = nx.read_graphml("graphs/IL/state_IL_city_Lincoln.graphml",force_multigraph=True)

def get_var_name(var):
	for name, value in globals().items():
		if value is var:
			return name
def get_Id(g,label):
    for u in g.nodes:
        if g.nodes[u]['label']==label:
            return u    
		
class TestClass_GetBusiness(unittest.TestCase):

	@parameterized.expand([
		[g_s_25_5, '1L3O2CUTk27SnmqyPBWQdQ', ['_ab50qdWOk0DdB6XOrBitw', 'gKBqK-FFq7EGOUscBqb1iA', 'JaMZoosomwX7DDjkFOEo3g'],],
        [g_s_25_5, 'xoZvMJPDW6Q9pDAXI0e_Ww',[]],
		[g_s_25_5, 'SgiBkhXeqIKl1PlFpZOycQ', ['gKBqK-FFq7EGOUscBqb1iA', 'JaMZoosomwX7DDjkFOEo3g']],
		[g_s_25_5, 'MGPQVLsODMm9ZtYQW-g_OA', ['iSRTaT9WngzB8JJ2YKJUig']],
		[g_s_5_5, 'bcjbaE6dDog4jkNY91ncLQ', []],
		[Millstadt, 'sZxXpvmBUN2fSCtK_BZFoQ', ['YqximOhYJza5Bp4hhnSgUQ', 'jopXZhgCjhfx5KjFJKD-vw', 'CSkIucODjUoGRxiIONcSgg', 'Y0pnoywoHENMzj5n6j4vxg', 'ttKlWxEaX4trG30xkCDYkA', 'S_xC9Xf3FNm1Bz6DCLmSuQ', '3QBpL29M2V4bIe_WZKg5lQ', 'fypGyTRBy5b60RRPG_NQ5g', 'tTyFGm2z4zqMXEN_ZWLVfQ', '0bzkJPZaxJI0aWh20ayBJQ', 'K0xjMTLYdicHvwLKNFlUZw', 'i-DkBuzDLRjs1KBb3jEkjw', 'Vr5bxmQ2C0XMXmT1WyamUQ', '861eWH26IJ3lhELxEBpSSQ']],		
		[Dupo, 'fxeRdFmgY6tbTyidpcdFLw', ['TsohTE3w1br2m0Nb-tDRDA']],
		[Cahokia, 'fxeRdFmgY6tbTyidpcdFLw', ['svLMFkLybFiadbTo_6g-hg', 'YWcH3SLyRIBHIBBgudqZLw', 
									'6BJwqc8rShdKHyizuR0Q5g', 'ysFWQ_XGmiN_sOgHmxKySQ', 'QDgGe--XQrPrap3u5EjAmg', '9Bf4mhvCmA6sv0hpwi3jDw']],
		[Cahokia, 'ZL8cgMY7b8POMaxKgd6u3g', ['q1LlkxzJ1VEzKedgPrcDlw', 'cVOC5jLNpP78yf5kh-gx_g', 'O998e7eUN45YDid-GxM1yw', '59hqWP1E1pfjshhHSu0OxA', 'YWcH3SLyRIBHIBBgudqZLw', '6BJwqc8rShdKHyizuR0Q5g', 'ysFWQ_XGmiN_sOgHmxKySQ', 'v_jBLgeJ1z5uVDzpZ-Wbkw', 'QDgGe--XQrPrap3u5EjAmg', 's5tkn1ngXJff90tP_iQ0YA', 'KeT8uehA2gVy6sycGdl_OQ', '9Bf4mhvCmA6sv0hpwi3jDw']],
		[Cahokia, 'hKBQ-PFlcB-t5FK3HUxoyQ', ['3OOK6-fiNy4RKIVu18atVw', 'q1LlkxzJ1VEzKedgPrcDlw', 'cVOC5jLNpP78yf5kh-gx_g', 'svLMFkLybFiadbTo_6g-hg', '59hqWP1E1pfjshhHSu0OxA', 'YWcH3SLyRIBHIBBgudqZLw', '6BJwqc8rShdKHyizuR0Q5g', 'ysFWQ_XGmiN_sOgHmxKySQ', 'ic2VmDDJcH9I06LU36eiAw', 'HRZmsTNLtZRBbJUuWjzLTg', 'QDgGe--XQrPrap3u5EjAmg', 's5tkn1ngXJff90tP_iQ0YA', 'KeT8uehA2gVy6sycGdl_OQ', '9Bf4mhvCmA6sv0hpwi3jDw']],
		[Lincoln, 'NdJV5jW2fkInUoSsVS_HLA', [] ],
		[Dupo, 'FFUZykBvwrC2_dOYQjIYxQ', ['TsohTE3w1br2m0Nb-tDRDA']]
	])
	def test_base(self, g, u_id, expected):
		var_name1 = get_var_name(g)
		var_name2 = get_var_name(u_id)
		result = find_business(g, u_id)
		self.assertCountEqual(result, expected, f"Grafo {var_name1}, usuário {var_name2}")

	def test_none (self):
		self.assertIsNone(find_business(None, '00'))
		self.assertIsNone(find_business(g_s_25_5, None))


if __name__ == '__main__':
	unittest.main(verbosity=2)
