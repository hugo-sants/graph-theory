############################
# Execute no terminal: python -m unittest test/test_Q01.py
########################################
import unittest
import networkx as nx
from src.Q01 import co_reviewers
from parameterized import parameterized

# Test Data
g_s_5_5 = nx.read_graphml("graphs/s_5_5.graphml", force_multigraph=True)
g_s_10_10 = nx.read_graphml("graphs/s_10_10.graphml", force_multigraph=True)
g_s_25_5 = nx.read_graphml("graphs/s_25_5.graphml", force_multigraph=True)
g_s_50_5 = nx.read_graphml("graphs/s_50_5.graphml", force_multigraph=True)
Dupo = nx.read_graphml("graphs/IL/state_IL_city_Dupo.graphml",force_multigraph=True)
Bellville = nx.read_graphml("graphs/IL/state_IL_city_Bellville.graphml",force_multigraph=True)
Chicago = nx.read_graphml("graphs/IL/state_IL_city_Chicago.graphml",force_multigraph=True)
Lincoln = nx.read_graphml("graphs/IL/state_IL_city_Lincoln.graphml",force_multigraph=True)
Roxana = nx.read_graphml("graphs/IL/state_IL_city_Roxana.graphml",force_multigraph=True)
St_Louis = nx.read_graphml("graphs/IL/state_IL_city_St_Louis.graphml",force_multigraph=True)
#CentreVille = nx.read_graphml("graphs/IL/state_IL_city_CentreVille.graphml",force_multigraph=True)
#Hartford = nx.read_graphml("graphs/IL/state_IL_city_Hartford.graphml",force_multigraph=True)
#OFallon = nx.read_graphml("graphs/IL/state_IL_city_OFallon.graphml",force_multigraph=True)
#Scott_AFB = nx.read_graphml("graphs/IL/state_IL_city_Scott_AFB.graphml",force_multigraph=True)
#Rosewood_Heights = nx.read_graphml("graphs/IL/state_IL_city_Rosewood_Heights.graphml",force_multigraph=True)


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
 
class TestClass_Co_reviewers(unittest.TestCase):
    
    @parameterized.expand([
        [g_s_5_5, ['Sophia', 'Debra'], []],
        [g_s_10_10, ['John', 'Walker', 'Daniel', 'Steph', 'Mike', 'Gwen', 'Jane'],
                    [('Walker', 'Daniel', 0, 'Reading Terminal Market'), 
                     ('Walker', 'Daniel', 1, 'Philadelphia Museum of Art'), 
                     ('Walker', 'Steph', 0, 'Atlantis Casino Resort Spa'), 
                     ('Walker', 'Jane', 0, '30th Street Station'), 
                     ('Daniel', 'Gwen', 0, 'The Praline Connection'), 
                     ('Daniel', 'Gwen', 1, 'French Market')]],
        [g_s_25_5, ['Jelena', 'Eugene', 'Daniel', 'Walker', 'Ryan', 'Steph', 'Gwen', 'Helen'],
                   [('Jelena', 'Eugene', 0, 'Acme Oyster House'), 
                    ('Jelena', 'Daniel', 0, 'Acme Oyster House'), 
                    ('Eugene', 'Daniel', 0, 'Acme Oyster House'), 
                    ('Eugene', 'Gwen', 0, "Mother's Restaurant"), 
                    ('Eugene', 'Helen', 0, "Mother's Restaurant"), 
                    ('Walker', 'Ryan', 0, 'Atlantis Casino Resort Spa'), 
                    ('Walker', 'Steph', 0, 'Atlantis Casino Resort Spa'), 
                    ('Ryan', 'Steph', 0, 'Atlantis Casino Resort Spa'), 
                    ('Gwen', 'Helen', 0, "Mother's Restaurant")]],
        [g_s_50_5, ['Ryan', 'Steph', 'Walker', 'Jenna', 'John', 'Peyman', 'Lia', 'Jane', 'Eugene', 'Helen', 'Jelena', 'Sherri', 'Daniel'],
                   [('Ryan', 'Steph', 0, 'Atlantis Casino Resort Spa'), 
                    ('Ryan', 'Walker', 0, 'Atlantis Casino Resort Spa'), 
                    ('Steph', 'Walker', 0, 'Atlantis Casino Resort Spa'), 
                    ('Walker', 'Lia', 0, '30th Street Station'), 
                    ('Walker', 'Jane', 0, '30th Street Station'), 
                    ('Jenna', 'John', 0, 'Village Whiskey'), 
                    ('Jenna', 'Peyman', 0, 'Village Whiskey'), 
                    ('John', 'Peyman', 0, 'Village Whiskey'), 
                    ('Lia', 'Jane', 0, '30th Street Station'), 
                    ('Lia', 'Eugene', 0, "Commander's Palace"), 
                    ('Lia', 'Helen', 0, "Commander's Palace"), 
                    ('Eugene', 'Helen', 0, "Commander's Palace"), 
                    ('Eugene', 'Jelena', 0, 'Acme Oyster House'), 
                    ('Eugene', 'Sherri', 0, 'Acme Oyster House'), 
                    ('Eugene', 'Daniel', 0, 'Acme Oyster House'), 
                    ('Jelena', 'Sherri', 0, 'Acme Oyster House'), 
                    ('Jelena', 'Daniel', 0, 'Acme Oyster House'), 
                    ('Sherri', 'Daniel', 0, 'Acme Oyster House')]],
        [Lincoln, ['V', 'Diana', 'Gigi', 'Elizabeth', 'Angela'],
                                  [('V', 'Diana', 0, 'Helitech Waterproofing & Foundation Repair'), 
                                   ('V', 'Gigi', 0, 'Helitech Waterproofing & Foundation Repair'), 
                                   ('V', 'Elizabeth', 0, 'Helitech Waterproofing & Foundation Repair'), 
                                   ('V', 'Angela', 0, 'Helitech Waterproofing & Foundation Repair'), 
                                   ('Diana', 'Gigi', 0, 'Helitech Waterproofing & Foundation Repair'), 
                                   ('Diana', 'Elizabeth', 0, 'Helitech Waterproofing & Foundation Repair'), 
                                   ('Diana', 'Angela', 0, 'Helitech Waterproofing & Foundation Repair'), 
                                   ('Gigi', 'Elizabeth', 0, 'Helitech Waterproofing & Foundation Repair'), 
                                   ('Gigi', 'Angela', 0, 'Helitech Waterproofing & Foundation Repair'), 
                                   ('Elizabeth', 'Angela', 0, 'Helitech Waterproofing & Foundation Repair')]],
        [
        Bellville,['Chris', 'Jamie', 'James', 'Jennifer', 'Renae', 'Michael'],
        [('Chris', 'Jamie', 0, 'Subway'), ('Chris', 'James', 0, 'Subway'), ('Chris', 'Jennifer', 0, 'Subway'), ('Chris', 'Renae', 0, 'Subway'), ('Chris', 'Michael', 0, 'Subway'), ('Jamie', 'James', 0, 'Subway'), ('Jamie', 'Jennifer', 0, 'Subway'), ('Jamie', 'Renae', 0, 'Subway'), ('Jamie', 'Michael', 0, 'Subway'), ('James', 'Jennifer', 0, 'Subway'), ('James', 'Renae', 0, 'Subway'), ('James', 'Michael', 0, 'Subway'), ('Jennifer', 'Renae', 0, 'Subway'), ('Jennifer', 'Michael', 0, 'Subway'), ('Renae', 'Michael', 0, 'Subway')]],
        [
        Chicago,['Caroline', 'C-Y', 'Carrie', 'Sean', 'Shelby', 'Marcy', 'Bob', 'Clara', 'Elly', 'Allison', 'Richard'],
        [('Caroline', 'C-Y', 0, 'North Avenue Collective'), ('Caroline', 'Carrie', 0, 'North Avenue Collective'), ('Caroline', 'Sean', 0, 'North Avenue Collective'), ('Caroline', 'Shelby', 0, 'North Avenue Collective'), ('Caroline', 'Marcy', 0, 'North Avenue Collective'), ('Caroline', 'Bob', 0, 'North Avenue Collective'), ('Caroline', 'Clara', 0, 'North Avenue Collective'), ('Caroline', 'Elly', 0, 'North Avenue Collective'), ('Caroline', 'Allison', 0, 'North Avenue Collective'), ('Caroline', 'Richard', 0, 'North Avenue Collective'), ('C-Y', 'Carrie', 0, 'North Avenue Collective'), ('C-Y', 'Sean', 0, 'North Avenue Collective'), ('C-Y', 'Shelby', 0, 'North Avenue Collective'), ('C-Y', 'Marcy', 0, 'North Avenue Collective'), ('C-Y', 'Bob', 0, 'North Avenue Collective'), ('C-Y', 'Clara', 0, 'North Avenue Collective'), ('C-Y', 'Elly', 0, 'North Avenue Collective'), ('C-Y', 'Allison', 0, 'North Avenue Collective'), ('C-Y', 'Richard', 0, 'North Avenue Collective'), ('Carrie', 'Sean', 0, 'North Avenue Collective'), ('Carrie', 'Shelby', 0, 'North Avenue Collective'), ('Carrie', 'Marcy', 0, 'North Avenue Collective'), ('Carrie', 'Bob', 0, 'North Avenue Collective'), ('Carrie', 'Clara', 0, 'North Avenue Collective'), ('Carrie', 'Elly', 0, 'North Avenue Collective'), ('Carrie', 'Allison', 0, 'North Avenue Collective'), ('Carrie', 'Richard', 0, 'North Avenue Collective'), ('Sean', 'Shelby', 0, 'North Avenue Collective'), ('Sean', 'Marcy', 0, 'North Avenue Collective'), ('Sean', 'Bob', 0, 'North Avenue Collective'), ('Sean', 'Clara', 0, 'North Avenue Collective'), ('Sean', 'Elly', 0, 'North Avenue Collective'), ('Sean', 'Allison', 0, 'North Avenue Collective'), ('Sean', 'Richard', 0, 'North Avenue Collective'), ('Shelby', 'Marcy', 0, 'North Avenue Collective'), ('Shelby', 'Bob', 0, 'North Avenue Collective'), ('Shelby', 'Clara', 0, 'North Avenue Collective'), ('Shelby', 'Elly', 0, 'North Avenue Collective'), ('Shelby', 'Allison', 0, 'North Avenue Collective'), ('Shelby', 'Richard', 0, 'North Avenue Collective'), ('Marcy', 'Bob', 0, 'North Avenue Collective'), ('Marcy', 'Clara', 0, 'North Avenue Collective'), ('Marcy', 'Elly', 0, 'North Avenue Collective'), ('Marcy', 'Allison', 0, 'North Avenue Collective'), ('Marcy', 'Richard', 0, 'North Avenue Collective'), ('Bob', 'Clara', 0, 'North Avenue Collective'), ('Bob', 'Elly', 0, 'North Avenue Collective'), ('Bob', 'Allison', 0, 'North Avenue Collective'), ('Bob', 'Richard', 0, 'North Avenue Collective'), ('Clara', 'Elly', 0, 'North Avenue Collective'), ('Clara', 'Allison', 0, 'North Avenue Collective'), ('Clara', 'Richard', 0, 'North Avenue Collective'), ('Elly', 'Allison', 0, 'North Avenue Collective'), ('Elly', 'Richard', 0, 'North Avenue Collective'), ('Allison', 'Richard', 0, 'North Avenue Collective')]],
        [
        Lincoln,['Elizabeth', 'Diana', 'Angela', 'V', 'Gigi'],
        [('Elizabeth', 'Diana', 0, 'Helitech Waterproofing & Foundation Repair'), ('Elizabeth', 'Angela', 0, 'Helitech Waterproofing & Foundation Repair'), ('Elizabeth', 'V', 0, 'Helitech Waterproofing & Foundation Repair'), ('Elizabeth', 'Gigi', 0, 'Helitech Waterproofing & Foundation Repair'), ('Diana', 'Angela', 0, 'Helitech Waterproofing & Foundation Repair'), ('Diana', 'V', 0, 'Helitech Waterproofing & Foundation Repair'), ('Diana', 'Gigi', 0, 'Helitech Waterproofing & Foundation Repair'), ('Angela', 'V', 0, 'Helitech Waterproofing & Foundation Repair'), ('Angela', 'Gigi', 0, 'Helitech Waterproofing & Foundation Repair'), ('V', 'Gigi', 0, 'Helitech Waterproofing & Foundation Repair')]],
        [
        Roxana,['Justin', 'Sally Walker', 'Kevin', 'Deric', 'Kayla', 'Julie', 'Chytia', 'Andrea', 'Jennifer'],
        [('Justin', 'Sally Walker', 0, 'Cone Barn'), ('Justin', 'Kevin', 0, 'Cone Barn'), ('Justin', 'Deric', 0, 'Cone Barn'), ('Justin', 'Kayla', 0, 'Cone Barn'), ('Justin', 'Julie', 0, 'Cone Barn'), ('Justin', 'Chytia', 0, 'Cone Barn'), ('Justin', 'Andrea', 0, 'Cone Barn'), ('Justin', 'Jennifer', 0, 'Cone Barn'), ('Sally Walker', 'Kevin', 0, 'Cone Barn'), ('Sally Walker', 'Deric', 0, 'Cone Barn'), ('Sally Walker', 'Kayla', 0, 'Cone Barn'), ('Sally Walker', 'Julie', 0, 'Cone Barn'), ('Sally Walker', 'Chytia', 0, 'Cone Barn'), ('Sally Walker', 'Andrea', 0, 'Cone Barn'), ('Sally Walker', 'Jennifer', 0, 'Cone Barn'), ('Kevin', 'Deric', 0, 'Cone Barn'), ('Kevin', 'Kayla', 0, 'Cone Barn'), ('Kevin', 'Julie', 0, 'Cone Barn'), ('Kevin', 'Chytia', 0, 'Cone Barn'), ('Kevin', 'Andrea', 0, 'Cone Barn'), ('Kevin', 'Jennifer', 0, 'Cone Barn'), ('Deric', 'Kayla', 0, 'Cone Barn'), ('Deric', 'Julie', 0, 'Cone Barn'), ('Deric', 'Chytia', 0, 'Cone Barn'), ('Deric', 'Andrea', 0, 'Cone Barn'), ('Deric', 'Jennifer', 0, 'Cone Barn'), ('Kayla', 'Julie', 0, 'Cone Barn'), ('Kayla', 'Chytia', 0, 'Cone Barn'), ('Kayla', 'Andrea', 0, 'Cone Barn'), ('Kayla', 'Jennifer', 0, 'Cone Barn'), ('Julie', 'Chytia', 0, 'Cone Barn'), ('Julie', 'Andrea', 0, 'Cone Barn'), ('Julie', 'Jennifer', 0, 'Cone Barn'), ('Chytia', 'Andrea', 0, 'Cone Barn'), ('Chytia', 'Jennifer', 0, 'Cone Barn'), ('Andrea', 'Jennifer', 0, 'Cone Barn')]],
        [
        St_Louis,['Arianna', 'Jackie', 'Diane', 'Rob', 'Catherine', 'Cynthia', 'Bethany', 'Lynette', 'Jessica', 'Leslie', 'Jason', 'BJ', 'Aaron', 'Ian'],
        [('Arianna', 'Jackie', 0, 'St. Louis Paranormal Research Society'), ('Arianna', 'Diane', 0, 'St. Louis Paranormal Research Society'), ('Arianna', 'Rob', 0, 'St. Louis Paranormal Research Society'), ('Arianna', 'Catherine', 0, 'St. Louis Paranormal Research Society'), ('Arianna', 'Cynthia', 0, 'St. Louis Paranormal Research Society'), ('Arianna', 'Bethany', 0, 'St. Louis Paranormal Research Society'), ('Arianna', 'Lynette', 0, 'St. Louis Paranormal Research Society'), ('Arianna', 'Jessica', 0, 'St. Louis Paranormal Research Society'), ('Arianna', 'Leslie', 0, 'St. Louis Paranormal Research Society'), ('Arianna', 'Jason', 0, 'St. Louis Paranormal Research Society'), ('Arianna', 'BJ', 0, 'St. Louis Paranormal Research Society'), ('Arianna', 'Aaron', 0, 'St. Louis Paranormal Research Society'), ('Arianna', 'Ian', 0, 'St. Louis Paranormal Research Society'), ('Jackie', 'Diane', 0, 'St. Louis Paranormal Research Society'), ('Jackie', 'Rob', 0, 'St. Louis Paranormal Research Society'), ('Jackie', 'Catherine', 0, 'St. Louis Paranormal Research Society'), ('Jackie', 'Cynthia', 0, 'St. Louis Paranormal Research Society'), ('Jackie', 'Bethany', 0, 'St. Louis Paranormal Research Society'), ('Jackie', 'Lynette', 0, 'St. Louis Paranormal Research Society'), ('Jackie', 'Jessica', 0, 'St. Louis Paranormal Research Society'), ('Jackie', 'Leslie', 0, 'St. Louis Paranormal Research Society'), ('Jackie', 'Jason', 0, 'St. Louis Paranormal Research Society'), ('Jackie', 'BJ', 0, 'St. Louis Paranormal Research Society'), ('Jackie', 'Aaron', 0, 'St. Louis Paranormal Research Society'), ('Jackie', 'Ian', 0, 'St. Louis Paranormal Research Society'), ('Diane', 'Rob', 0, 'St. Louis Paranormal Research Society'), ('Diane', 'Catherine', 0, 'St. Louis Paranormal Research Society'), ('Diane', 'Cynthia', 0, 'St. Louis Paranormal Research Society'), ('Diane', 'Bethany', 0, 'St. Louis Paranormal Research Society'), ('Diane', 'Lynette', 0, 'St. Louis Paranormal Research Society'), ('Diane', 'Jessica', 0, 'St. Louis Paranormal Research Society'), ('Diane', 'Leslie', 0, 'St. Louis Paranormal Research Society'), ('Diane', 'Jason', 0, 'St. Louis Paranormal Research Society'), ('Diane', 'BJ', 0, 'St. Louis Paranormal Research Society'), ('Diane', 'Aaron', 0, 'St. Louis Paranormal Research Society'), ('Diane', 'Ian', 0, 'St. Louis Paranormal Research Society'), ('Rob', 'Catherine', 0, 'St. Louis Paranormal Research Society'), ('Rob', 'Cynthia', 0, 'St. Louis Paranormal Research Society'), ('Rob', 'Bethany', 0, 'St. Louis Paranormal Research Society'), ('Rob', 'Lynette', 0, 'St. Louis Paranormal Research Society'), ('Rob', 'Jessica', 0, 'St. Louis Paranormal Research Society'), ('Rob', 'Leslie', 0, 'St. Louis Paranormal Research Society'), ('Rob', 'Jason', 0, 'St. Louis Paranormal Research Society'), ('Rob', 'BJ', 0, 'St. Louis Paranormal Research Society'), ('Rob', 'Aaron', 0, 'St. Louis Paranormal Research Society'), ('Rob', 'Ian', 0, 'St. Louis Paranormal Research Society'), ('Catherine', 'Cynthia', 0, 'St. Louis Paranormal Research Society'), ('Catherine', 'Bethany', 0, 'St. Louis Paranormal Research Society'), ('Catherine', 'Lynette', 0, 'St. Louis Paranormal Research Society'), ('Catherine', 'Jessica', 0, 'St. Louis Paranormal Research Society'), ('Catherine', 'Leslie', 0, 'St. Louis Paranormal Research Society'), ('Catherine', 'Jason', 0, 'St. Louis Paranormal Research Society'), ('Catherine', 'BJ', 0, 'St. Louis Paranormal Research Society'), ('Catherine', 'Aaron', 0, 'St. Louis Paranormal Research Society'), ('Catherine', 'Ian', 0, 'St. Louis Paranormal Research Society'), ('Cynthia', 'Bethany', 0, 'St. Louis Paranormal Research Society'), ('Cynthia', 'Lynette', 0, 'St. Louis Paranormal Research Society'), ('Cynthia', 'Jessica', 0, 'St. Louis Paranormal Research Society'), ('Cynthia', 'Leslie', 0, 'St. Louis Paranormal Research Society'), ('Cynthia', 'Jason', 0, 'St. Louis Paranormal Research Society'), ('Cynthia', 'BJ', 0, 'St. Louis Paranormal Research Society'), ('Cynthia', 'Aaron', 0, 'St. Louis Paranormal Research Society'), ('Cynthia', 'Ian', 0, 'St. Louis Paranormal Research Society'), ('Bethany', 'Lynette', 0, 'St. Louis Paranormal Research Society'), ('Bethany', 'Jessica', 0, 'St. Louis Paranormal Research Society'), ('Bethany', 'Leslie', 0, 'St. Louis Paranormal Research Society'), ('Bethany', 'Jason', 0, 'St. Louis Paranormal Research Society'), ('Bethany', 'BJ', 0, 'St. Louis Paranormal Research Society'), ('Bethany', 'Aaron', 0, 'St. Louis Paranormal Research Society'), ('Bethany', 'Ian', 0, 'St. Louis Paranormal Research Society'), ('Lynette', 'Jessica', 0, 'St. Louis Paranormal Research Society'), ('Lynette', 'Leslie', 0, 'St. Louis Paranormal Research Society'), ('Lynette', 'Jason', 0, 'St. Louis Paranormal Research Society'), ('Lynette', 'BJ', 0, 'St. Louis Paranormal Research Society'), ('Lynette', 'Aaron', 0, 'St. Louis Paranormal Research Society'), ('Lynette', 'Ian', 0, 'St. Louis Paranormal Research Society'), ('Jessica', 'Leslie', 0, 'St. Louis Paranormal Research Society'), ('Jessica', 'Jason', 0, 'St. Louis Paranormal Research Society'), ('Jessica', 'BJ', 0, 'St. Louis Paranormal Research Society'), ('Jessica', 'Aaron', 0, 'St. Louis Paranormal Research Society'), ('Jessica', 'Ian', 0, 'St. Louis Paranormal Research Society'), ('Leslie', 'Jason', 0, 'St. Louis Paranormal Research Society'), ('Leslie', 'BJ', 0, 'St. Louis Paranormal Research Society'), ('Leslie', 'Aaron', 0, 'St. Louis Paranormal Research Society'), ('Leslie', 'Ian', 0, 'St. Louis Paranormal Research Society'), ('Jason', 'BJ', 0, 'St. Louis Paranormal Research Society'), ('Jason', 'Aaron', 0, 'St. Louis Paranormal Research Society'), ('Jason', 'Ian', 0, 'St. Louis Paranormal Research Society'), ('BJ', 'Aaron', 0, 'St. Louis Paranormal Research Society'), ('BJ', 'Ian', 0, 'St. Louis Paranormal Research Society'), ('Aaron', 'Ian', 0, 'St. Louis Paranormal Research Society')]],

    ])  
    def test_base(self, g, e_nodes, e_edges):
        var_name = get_var_name(g)
        result = co_reviewers(g)
        # Converte labels da saída esperada em identificadores 
        e_id_nodes = [get_Id(g,l) for l in e_nodes]
        e_id_edges = [(get_Id(g,x),get_Id(g,y),k,get_Id(g,b)) for x,y,k,b in e_edges]
        # Verifica o grafo retornado
        self.assertCountEqual(result.nodes, e_id_nodes, f"Grafo: {var_name}, vértices: {e_nodes}")
        self.assertTrue(all(any(((x==u and y==v) or (x==v) and (y==u)) and (b==result[x][y][k]['business'])  for u,v,j,b in e_id_edges) for x,y,k in result.edges))
        self.assertTrue(all(any(((x==u and y==v) or (x==v) and (y==u)) and (b==result[x][y][k]['business'])  for x,y,k in result.edges) for u,v,j,b in e_id_edges))
    
    def test_None(self):
        self.assertIsNone(co_reviewers(None))

    def test_null(self):
        self.assertIsNone(co_reviewers(nx.MultiGraph()))

    def test_graph_structure(self):
        #Testa se o resultado é um MultiGraph com propriedade 'business' nas arestas.
        result = co_reviewers(Dupo)
        # Verifica se o resultado é um MultiGraph
        self.assertIsInstance(result, nx.MultiGraph)
        # Verifica se todas as arestas possuem a propriedade 'business'
        edge_data = [data for u, v, k, data in result.edges(keys=True, data=True)]
        self.assertTrue(all('business' in data for data in edge_data), f"Alguma aresta sem propriedade 'business'")
        self.assertTrue(all(data['business'] is not None for data in edge_data), f"Alguma aresta tem valor None em 'business'")

if __name__ == '__main__':
    unittest.main(verbosity=2)
