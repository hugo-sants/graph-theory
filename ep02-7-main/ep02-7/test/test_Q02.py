############################
# Execute no terminal: python -m unittest test/test_Q02.py
#############################
import unittest
import networkx as nx
from src.Q02 import critical_users
from parameterized import parameterized

# Dados de teste: grafos pequenos para validação
s_5_5 = nx.read_graphml("graphs/s_5_5.graphml", force_multigraph=True)
s_10_10 = nx.read_graphml("graphs/s_10_10.graphml", force_multigraph=True)
s_25_5 = nx.read_graphml("graphs/s_25_5.graphml", force_multigraph=True)
s_50_5 = nx.read_graphml("graphs/s_50_5.graphml", force_multigraph=True)
Cahokia_esparso_10 = nx.read_graphml("graphs/Cahokia_esparso_10.graphml", force_multigraph=True)
Cahokia_esparso_20 = nx.read_graphml("graphs/Cahokia_esparso_20.graphml", force_multigraph=True)
Cahokia_esparso_30 = nx.read_graphml("graphs/Cahokia_esparso_30.graphml", force_multigraph=True)
Cahokia_esparso_40 = nx.read_graphml("graphs/Cahokia_esparso_40.graphml", force_multigraph=True)
Sauget_esparso_10 = nx.read_graphml("graphs/Sauget_esparso_10.graphml", force_multigraph=True)
Sauget_esparso_20 = nx.read_graphml("graphs/Sauget_esparso_20.graphml", force_multigraph=True)
Sauget_esparso_30 = nx.read_graphml("graphs/Sauget_esparso_30.graphml", force_multigraph=True)
Sauget_esparso_40 = nx.read_graphml("graphs/Sauget_esparso_40.graphml", force_multigraph=True)
Sauget_esparso_50 = nx.read_graphml("graphs/Sauget_esparso_50.graphml", force_multigraph=True)
Dupo_esparso_10 = nx.read_graphml("graphs/Dupo_esparso_10.graphml", force_multigraph=True)
Dupo_esparso_30 = nx.read_graphml("graphs/Dupo_esparso_30.graphml", force_multigraph=True)
Dupo_esparso_50 = nx.read_graphml("graphs/Dupo_esparso_50.graphml", force_multigraph=True)
state_IL_city_Dupo = nx.read_graphml("graphs/IL/state_IL_city_Dupo.graphml", force_multigraph=True)
state_IL_city_Lincoln = nx.read_graphml("graphs/IL/state_IL_city_Lincoln.graphml", force_multigraph=True)
state_IL_city_Sauget = nx.read_graphml("graphs/IL/state_IL_city_Sauget.graphml", force_multigraph=True)
state_IL_city_Bethalto = nx.read_graphml("graphs/IL/state_IL_city_Bethalto.graphml", force_multigraph=True)
state_IL_city_Caseyville = nx.read_graphml("graphs/IL/state_IL_city_Caseyville.graphml", force_multigraph=True)
state_IL_city_Columbia = nx.read_graphml("graphs/IL/state_IL_city_Columbia.graphml", force_multigraph=True)
state_IL_city_Edwardsville = nx.read_graphml("graphs/IL/state_IL_city_Edwardsville.graphml", force_multigraph=True)

## Funções auxiliares
# Recupera o nome da variável global para identificar dados do teste que falha
def get_var_name(var):
	for name, value in globals().items():
		if value is var:
			return name
		
class TestClass_CriticalUsers(unittest.TestCase):

	@parameterized.expand([
        [ s_5_5, {}],
        [ s_10_10, {'qVc8ODYU5SZjKXVBgXdI7w': 4, 'j14WgRoU_-2ZE1aw1dXrJg': 4}],
        [ s_25_5, {'SgiBkhXeqIKl1PlFpZOycQ': 4}],
        [ s_50_5, {'NIhcRW6DWvk1JQhDhXwgOQ': 4, 'qVc8ODYU5SZjKXVBgXdI7w': 4, 'SgiBkhXeqIKl1PlFpZOycQ': 5}],
        [ Cahokia_esparso_10, {}],
        [ Cahokia_esparso_20, {'hF4pvrCWNHP5LIvP5yv7KA': 2}],
        [ Cahokia_esparso_30, {'hF4pvrCWNHP5LIvP5yv7KA': 3, 'fxeRdFmgY6tbTyidpcdFLw': 21, 'Ib7dDP8W4gSlkTrdDLtHdw': 2}],
        [ Cahokia_esparso_40, {'hF4pvrCWNHP5LIvP5yv7KA': 3, 'fxeRdFmgY6tbTyidpcdFLw': 30, 'Ib7dDP8W4gSlkTrdDLtHdw': 3}],
        [ Sauget_esparso_10, {}],
        [ Sauget_esparso_20, {'bSWWV65xqwiHf6njt1LwWg': 11}],
        [ Sauget_esparso_30, {'bSWWV65xqwiHf6njt1LwWg': 16, 'IdUJDWQmhp73APOksDlkWQ': 9}],
        [ Sauget_esparso_40, {'bSWWV65xqwiHf6njt1LwWg': 26, 'IdUJDWQmhp73APOksDlkWQ': 10}],
        [ Sauget_esparso_50, {'bSWWV65xqwiHf6njt1LwWg': 29, 'IdUJDWQmhp73APOksDlkWQ': 11}],
        [ Dupo_esparso_10, {'lKs439UQaYTvI3SHSHTsVg': 6}],
        [ Dupo_esparso_30, {'lKs439UQaYTvI3SHSHTsVg': 16}],
        [ Dupo_esparso_50, {'lKs439UQaYTvI3SHSHTsVg': 19}],
        [ state_IL_city_Dupo, {'lKs439UQaYTvI3SHSHTsVg': 19}],
        [ state_IL_city_Lincoln, {}],
        [ state_IL_city_Sauget, {'_HGW2i7EdvkKH04JtByGFQ': 22, 'qTMK2qr6ngof4fe29qyooA': 67}],
        [ state_IL_city_Bethalto, {'1FewsdvGodYhLAuVfHTY1w': 35}],
        [ state_IL_city_Caseyville, {'OpLpt58fTc9TEwQpNnvhgg': 92, 'iUINaXQTcfrgCPfI9xYP-Q': 73, 'pKtnb9Nswv_FENpfEnE0Kw': 70, 'QnAU-AHDjgaGVmCVQ0z8-Q': 98, 'B4PUZAvjg9tatZMK8CzcJQ': 68, '9BaN1QJueJFwShIEgDoU1A': 84, '4HSZulJVrwIzgKyYhphecw': 30}],     
        [ state_IL_city_Columbia, {'4JvclzKO_ibX2kGJ3J_Eqg': 59, 'ywt85KtfYhGoDKKZDVhl8g': 91, 'zb4mISA7APPJUuQ_uidX6Q': 344, 'DFpiANIRnf6p9elmB5ejBQ': 32, 'lYQk0R6sPfo3WeX-l_5BuA': 30}],
        [ state_IL_city_Edwardsville, {'x-xTlMtHt5lNW3uEca_KHg': 51, 'CTbeIErjRDJgI5pDsPvTEQ': 330, '7TBqaLvv4jugAmXXcHQSmg': 128, 'H9p_sTh5cRAaOOU-F-G47Q': 406, 'sG9dTFp2WwWbRJVjj5gH2w': 3394, 'TRv-jyQMW1QiXsBxH5nR3w': 20, 'aGhUi4LfdFoiggqSwa_xfw': 159, 'qAZsDWMaXpwrbK0bQ77cOw': 186, '0DK-fg2ZBnpkMKnU9SgPMQ': 156, 'W_5vLZ2V5nLGZNBwZ27L8g': 165, 'I9BHJLX9XSRHYxf1mjHtlA': 91, 'W1IjhtwzCFC5rQHghvlneQ': 174, 'fJ1w8PpP8OxGm_hRJLrkXQ': 158, 'EDAg3FUbil6oIIY0HJctBA': 1917}]
	])
	def test_base(self, g, expected):
		var_name = get_var_name(g)
		resultado = critical_users(g)
		self.assertDictEqual(resultado, expected, f"Grafo {var_name}")

	def test_none (self):
		self.assertIsNone(critical_users(None))

	def test_nullgraph(self):
		g = nx.MultiGraph()
		self.assertIsNone(critical_users(g))


if __name__ == '__main__':
	unittest.main(verbosity=2)
