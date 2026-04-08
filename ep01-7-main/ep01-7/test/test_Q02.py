############################
# Execute no terminal: python -m unittest test/test_Q02.py
#############################
import unittest
import networkx as nx
from src.Q02 import get_business
from parameterized import parameterized

# Dados de teste: grafos pequenos para validação
g_s_5_5 = nx.read_graphml("graphs/s_5_5.graphml", force_multigraph=True)
g_s_25_5 = nx.read_graphml("graphs/s_25_5.graphml", force_multigraph=True)
g_s_10_10 = nx.read_graphml("graphs/s_10_10.graphml", force_multigraph=True)
g_s_50_5 = nx.read_graphml("graphs/s_50_5.graphml", force_multigraph=True)
Lincoln = nx.read_graphml("graphs/IL/state_IL_city_Lincoln.graphml", force_multigraph=True)
Columbia = nx.read_graphml("graphs/IL/state_IL_city_Columbia.graphml",force_multigraph=True)
Lincoln = nx.read_graphml("graphs/IL/state_IL_city_Lincoln.graphml", force_multigraph=True)
Dupo = nx.read_graphml("graphs/IL/state_IL_city_Dupo.graphml",force_multigraph=True)
Bellville = nx.read_graphml("graphs/IL/state_IL_city_Bellville.graphml",force_multigraph=True)
Chicago = nx.read_graphml("graphs/IL/state_IL_city_Chicago.graphml",force_multigraph=True)
Lincoln = nx.read_graphml("graphs/IL/state_IL_city_Lincoln.graphml",force_multigraph=True)
Roxana = nx.read_graphml("graphs/IL/state_IL_city_Roxana.graphml",force_multigraph=True)
St_Louis = nx.read_graphml("graphs/IL/state_IL_city_St_Louis.graphml",force_multigraph=True)

## Funções auxiliares
# Recupera o nome da variável global para identificar dados do teste que falha
def get_var_name(var):
	for name, value in globals().items():
		if value is var:
			return name
# Retorna o identificador de um vértice a partir do label
def get_Id(g,label):
    for u in g.nodes:
        if g.nodes[u]['label']==label:
            return u    
		
class TestClass_GetBusiness(unittest.TestCase):

	@parameterized.expand([
		[g_s_5_5, {'New Orleans': ['Panera Bread', "Jacques-Imo's Cafe", 'Melt', 'Pizza Hut'],
                   'Tucson': ["Finnegan's Pub"]}],
		[Lincoln, {'Lincoln': ['Helitech Waterproofing & Foundation Repair']}],
        [g_s_25_5, {
            'New Orleans': ['Acme Oyster House', "Mother's Restaurant"],
            'Reno': ['Atlantis Casino Resort Spa'],
            'St. Louis': ['The Royale Food & Spirits'],
            'Clayton': ['Schnucks Richmond Center']
        }],
        [Columbia, {
            'Columbia': ['Mokka Kaffeehaus', 'Inman Heating & Cooling', 'Taco Bell', "Joe's Pizza and Pasta", 'China Star', 'Columbia Bridges Golf Course', "Bully's Smokehouse", 'Weber Chevrolet Columbia', "Jan's Hallmark Shop", 'Image Nails and Spa', 'Rcasa Tex-Mex Restaurant', "McDonald's", 'Sonic Drive-In', 'Royal Gate Chrysler Dodge Jeep RAM of Columbia', 'Thai House', 'Cafe on the Abbey', 'Trost Plastics', "Imo's Pizza", "Washy's Pub", "Stumpy's Spirits", 'Hampton Inn St. Louis-Columbia', 'Monroe County YMCA', 'Chateau La VIn', "Domino's Pizza", 'ATI Physical Therapy', 'Tequila Mexican Restaurant', 'Lady Nails', 'Burger King', 'Dear Diva Desserts', "Joe Boccardi's Ristorante", 'Bob Brockland Buick GMC', 'Proving Ground', 'Dairy Queen Grill & Chill', 'Mokka Cafe', "Reifschneider's Grill & Grape", 'BEAST Southern Kitchen & BBQ', 'Backtothe80sarcade', "Tiny's", 'Columbia Dental Center', "Aunt Maggie's on Main", 'Top Shooters', 'Mr Chiu Restaurant', 'Bernhard Auto Works', 'Red Apple', 'Maries Ice Cream Shoppe', 'Our House Cafe', "Kritter Kare's Howliday Inn", 'Brite Worx Car Washery', "Gruchala's", "Who Dat's", 'Mueller Veterinary Services', 'Sunset Overlook', 'Merz on Main', 'Gateway Urgent Care - Columbia']
        }],
		[Bellville,
			{'Bellville': ['Subway']}
		],
		[Chicago,
			{'Chicago': ['North Avenue Collective']}
		],
		[Lincoln,
		{'Lincoln': ['Helitech Waterproofing & Foundation Repair']}
		],
		[Roxana,
		{'Roxana': ['Cone Barn']}
		],
		[St_Louis,
		{'St. Louis': ['St. Louis Paranormal Research Society']}
		],
		[g_s_10_10,
			{'Philadelphia': ['Pizzeria Vetri', 'Reading Terminal Market', 'Philadelphia Museum of Art', '30th Street Station'],
			'Reno': ['Atlantis Casino Resort Spa', '5th St. Bakehouse'],
			'Saint Louis': ["Papa John's Pizza"],
			'New Orleans': ['The Praline Connection', 'French Market'],
			'Oro Valley': ['WorldMark Rancho Vistoso']}
		],
		[g_s_50_5,
			{'Reno': ['Atlantis Casino Resort Spa'],
			'Philadelphia': ['Village Whiskey', '30th Street Station'],
			'New Orleans': ["Commander's Palace", 'Acme Oyster House']}
		],
	])
	def test_base(self, g, expected):
		var_name = get_var_name(g)
		resultado = get_business(g)
		for cidade in expected.keys():
			e_ids = [get_Id(g,b) for b in expected[cidade]]
			self.assertCountEqual(resultado[cidade], e_ids, f"Grafo: {var_name} - Businesses diferentes para cidade {cidade}")

	def test_none (self):
		self.assertIsNone(get_business(None))

	def test_nullgraph(self):
		g = nx.MultiGraph()
		self.assertIsNone(get_business(g))

	def test_sem_business(self):
		g = nx.MultiGraph()
		g.add_node('u1', type='user', name='Teste')
		self.assertEqual(get_business(g), {})

if __name__ == '__main__':
	unittest.main(verbosity=2)
