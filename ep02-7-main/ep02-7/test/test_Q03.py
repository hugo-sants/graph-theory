############################
# Execute no terminal: python -m unittest test/test_Q03.py
import unittest
import networkx as nx
from parameterized import parameterized
from src.Q03 import dense_biclique  # Pylance: garantir símbolo existente em Q03

# Test Data
s_5_5 = nx.read_graphml("graphs/s_5_5.graphml", force_multigraph=True)
s_10_10 = nx.read_graphml("graphs/s_10_10.graphml", force_multigraph=True)
s_25_5 = nx.read_graphml("graphs/s_25_5.graphml", force_multigraph=True)
s_50_5 = nx.read_graphml("graphs/s_50_5.graphml", force_multigraph=True)
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
Sauget_3_2 = nx.read_graphml("graphs/Sauget_3_2.graphml", force_multigraph=True)
Sauget_5_2 = nx.read_graphml("graphs/Sauget_5_2.graphml", force_multigraph=True)
Sauget_10_2 = nx.read_graphml("graphs/Sauget_10_2.graphml", force_multigraph=True)
Sauget_20_2 = nx.read_graphml("graphs/Sauget_20_2.graphml", force_multigraph=True)

## Funções auxiliares
# Recupera o nome da variável global para identificar dados do teste que falha
def get_var_name(var):
    for name, value in globals().items():  
        if value is var:
            return name

class TestClass_DenseBicliques(unittest.TestCase):
    
    @parameterized.expand([
        [ s_5_5, 1, 4, [({'bcjbaE6dDog4jkNY91ncLQ'}, {'mhrW9O0O5hXGXGnEYBVoag', 'ew5TyXOlyCpCRptye1LdxA', 'hJTwBhYBTkiHaDMml_v_sw', 'e4Vwtrqf-wpJfwesgvdgxQ'})] ],
        [ s_10_10, 1, 4, [({'j14WgRoU_-2ZE1aw1dXrJg'}, {'ompDR5sUDpoI6gnTldmneQ', 'ytynqOUb3hjKeJfRj5Tshw', 'Qw7tz-UkPrpXaVidWuab4Q', '-xaY1TlMf20Ol9QLcDSU6Q'}), ({'qVc8ODYU5SZjKXVBgXdI7w'}, {'-OKB11ypR4C8wWlonBFIGw', 'ytynqOUb3hjKeJfRj5Tshw', 'Qw7tz-UkPrpXaVidWuab4Q', 'Xq-8-I0U8Artr7d70SjX-g'})] ],
        [ s_10_10, 2, 2, [({'SZDeASXq7o05mMNLshsdIA', 'j14WgRoU_-2ZE1aw1dXrJg'}, {'ompDR5sUDpoI6gnTldmneQ', '-xaY1TlMf20Ol9QLcDSU6Q'}), ({'qVc8ODYU5SZjKXVBgXdI7w', 'j14WgRoU_-2ZE1aw1dXrJg'}, {'ytynqOUb3hjKeJfRj5Tshw', 'Qw7tz-UkPrpXaVidWuab4Q'})] ],
        [ s_25_5, 1, 3, [({'MGPQVLsODMm9ZtYQW-g_OA'}, {'JaMZoosomwX7DDjkFOEo3g', 'gKBqK-FFq7EGOUscBqb1iA', '_ab50qdWOk0DdB6XOrBitw'})] ],
        [ s_25_5, 3, 1, [({'xoZvMJPDW6Q9pDAXI0e_Ww', 'qVc8ODYU5SZjKXVBgXdI7w', '2WnXYQFK0hXEoTxPtV2zvg'}, {'-OKB11ypR4C8wWlonBFIGw'}), ({'j14WgRoU_-2ZE1aw1dXrJg', 'SgiBkhXeqIKl1PlFpZOycQ', 'MGPQVLsODMm9ZtYQW-g_OA'}, {'_ab50qdWOk0DdB6XOrBitw'}), ({'SZDeASXq7o05mMNLshsdIA', 'SgiBkhXeqIKl1PlFpZOycQ', '1L3O2CUTk27SnmqyPBWQdQ'}, {'iSRTaT9WngzB8JJ2YKJUig'})] ],
        [ s_50_5, 1, 2, [({'qVc8ODYU5SZjKXVBgXdI7w'}, {'-OKB11ypR4C8wWlonBFIGw', 'Xq-8-I0U8Artr7d70SjX-g'}), ({'NIhcRW6DWvk1JQhDhXwgOQ'}, {'_C7QiQQc47AOEv4PE3Kong', 'Xq-8-I0U8Artr7d70SjX-g'}), ({'SgiBkhXeqIKl1PlFpZOycQ'}, {'_C7QiQQc47AOEv4PE3Kong', '_ab50qdWOk0DdB6XOrBitw'})] ],
        [ s_50_5, 4, 1, [({'MGPQVLsODMm9ZtYQW-g_OA', 'j14WgRoU_-2ZE1aw1dXrJg', 'AkBtT43dYcttxQ3qOzPBAg', 'SgiBkhXeqIKl1PlFpZOycQ'}, {'_ab50qdWOk0DdB6XOrBitw'})] ],
        [ Dupo_5_3, 5, 1, [({'RXSd57z_afLK9nWKHmIsTQ', '9SQPIP8ASyy6J7Ujjzi3Ag', 'FFUZykBvwrC2_dOYQjIYxQ', '_pcJosyzxpJTyIuvs_pMqg', 'fxeRdFmgY6tbTyidpcdFLw'}, {'mx1_2BxcIbZ1RKsGG_UPHg'})] ],
        [ Dupo_10_3, 1, 2, [({'lKs439UQaYTvI3SHSHTsVg'}, {'TsohTE3w1br2m0Nb-tDRDA', 'mx1_2BxcIbZ1RKsGG_UPHg'})] ],
        [ Dupo_15_3, 4, 4, [({'j3cmlhUwxmbHjTwHiLuhVA', 'CoULkkk4RQ2q5yfT6ULdCw', 'aT3nby92m66Qdg2TBzcCjg', 'fxeRdFmgY6tbTyidpcdFLw'}, {'zMe0kY6KMRVdlUKmme-JpA', 'wTrE0XUyPtRa2qRVPj4Vog', 'Xfv4ZGJ4u5t3LtSuZHpA0g', 'nwN92Uje-xIKE5voPTTvBQ'})] ],
        [ Dupo_20_3, 4, 4, [({'j3cmlhUwxmbHjTwHiLuhVA', 'aT3nby92m66Qdg2TBzcCjg', 'CoULkkk4RQ2q5yfT6ULdCw', 'fxeRdFmgY6tbTyidpcdFLw'}, {'zMe0kY6KMRVdlUKmme-JpA', 'wTrE0XUyPtRa2qRVPj4Vog', 'Xfv4ZGJ4u5t3LtSuZHpA0g', 'nwN92Uje-xIKE5voPTTvBQ'})] ],
        [ Sauget_3_2, 1, 4, [({'mKBl4fAqTfNts7B78aOPVg'}, {'7xAnCle53yC6GHa22j69jg', 'rnjXf1zDn9LGejhIX1tqxA', 'xXYYMUKs6mAGdLAXiTScvg', '4a15acANJFUsS3KxAzOT0g'})] ],
        [ Sauget_3_2, 2, 3, [({'mKBl4fAqTfNts7B78aOPVg', 'bSWWV65xqwiHf6njt1LwWg'}, {'7xAnCle53yC6GHa22j69jg', '4a15acANJFUsS3KxAzOT0g', 'xXYYMUKs6mAGdLAXiTScvg'})] ],
        [ Sauget_3_2, 4, 2, [({'qWYEuBZP7av55tewg3PXKg', 'mKBl4fAqTfNts7B78aOPVg', 'bSWWV65xqwiHf6njt1LwWg', 'TMLVzNYs-zwwREudyvI08A'}, {'7xAnCle53yC6GHa22j69jg', 'xXYYMUKs6mAGdLAXiTScvg'})] ],
        [ Sauget_3_2, 5, 1, [({'qTMK2qr6ngof4fe29qyooA', 'TMLVzNYs-zwwREudyvI08A', 'qWYEuBZP7av55tewg3PXKg', 'mKBl4fAqTfNts7B78aOPVg', 'bSWWV65xqwiHf6njt1LwWg'}, {'xXYYMUKs6mAGdLAXiTScvg'})] ],
        [ Sauget_5_2, 1, 4, [({'mKBl4fAqTfNts7B78aOPVg'}, {'7xAnCle53yC6GHa22j69jg', '4a15acANJFUsS3KxAzOT0g', 'xXYYMUKs6mAGdLAXiTScvg', 'rnjXf1zDn9LGejhIX1tqxA'})] ],
        [ Sauget_5_2, 2, 3, [({'mKBl4fAqTfNts7B78aOPVg', 'bSWWV65xqwiHf6njt1LwWg'}, {'7xAnCle53yC6GHa22j69jg', '4a15acANJFUsS3KxAzOT0g', 'xXYYMUKs6mAGdLAXiTScvg'})] ],
        [ Sauget_5_2, 4, 2, [({'qWYEuBZP7av55tewg3PXKg', 'mKBl4fAqTfNts7B78aOPVg', 'bSWWV65xqwiHf6njt1LwWg', 'TMLVzNYs-zwwREudyvI08A'}, {'7xAnCle53yC6GHa22j69jg', 'xXYYMUKs6mAGdLAXiTScvg'})] ],
        [ Sauget_5_2, 5, 1, [({'qTMK2qr6ngof4fe29qyooA', 'TMLVzNYs-zwwREudyvI08A', 'qWYEuBZP7av55tewg3PXKg', 'mKBl4fAqTfNts7B78aOPVg', 'bSWWV65xqwiHf6njt1LwWg'}, {'xXYYMUKs6mAGdLAXiTScvg'})] ],
        [ Sauget_10_2, 1, 4, [({'mKBl4fAqTfNts7B78aOPVg'}, {'7xAnCle53yC6GHa22j69jg', '4a15acANJFUsS3KxAzOT0g', 'xXYYMUKs6mAGdLAXiTScvg', 'rnjXf1zDn9LGejhIX1tqxA'})] ],
        [ Sauget_10_2, 2, 3, [({'mKBl4fAqTfNts7B78aOPVg', 'bSWWV65xqwiHf6njt1LwWg'}, {'7xAnCle53yC6GHa22j69jg', '4a15acANJFUsS3KxAzOT0g', 'xXYYMUKs6mAGdLAXiTScvg'})] ],
        [ Sauget_10_2, 4, 2, [({'qWYEuBZP7av55tewg3PXKg', 'mKBl4fAqTfNts7B78aOPVg', 'bSWWV65xqwiHf6njt1LwWg', 'TMLVzNYs-zwwREudyvI08A'}, {'7xAnCle53yC6GHa22j69jg', 'xXYYMUKs6mAGdLAXiTScvg'})] ],
        [ Sauget_20_2, 1, 4, [({'mKBl4fAqTfNts7B78aOPVg'}, {'7xAnCle53yC6GHa22j69jg', '4a15acANJFUsS3KxAzOT0g', 'xXYYMUKs6mAGdLAXiTScvg', 'rnjXf1zDn9LGejhIX1tqxA'})] ],
        [ Sauget_20_2, 2, 3, [({'mKBl4fAqTfNts7B78aOPVg', 'bSWWV65xqwiHf6njt1LwWg'}, {'7xAnCle53yC6GHa22j69jg', '4a15acANJFUsS3KxAzOT0g', 'xXYYMUKs6mAGdLAXiTScvg'})] ],
        [ Sauget_20_2, 4, 2, [({'qWYEuBZP7av55tewg3PXKg', 'mKBl4fAqTfNts7B78aOPVg', 'bSWWV65xqwiHf6njt1LwWg', 'TMLVzNYs-zwwREudyvI08A'}, {'7xAnCle53yC6GHa22j69jg', 'xXYYMUKs6mAGdLAXiTScvg'})] ],
        [ Cahokia_5_2, 3, 2, [({'fxeRdFmgY6tbTyidpcdFLw', 'ZYdN05c0LC8OMJob0FWQdQ', 'wm3UghkWy48CWlcOHeq_tg'}, {'cVOC5jLNpP78yf5kh-gx_g', 'v_jBLgeJ1z5uVDzpZ-Wbkw'}), ({'fxeRdFmgY6tbTyidpcdFLw', 'ZYdN05c0LC8OMJob0FWQdQ', 'wm3UghkWy48CWlcOHeq_tg'}, {'cVOC5jLNpP78yf5kh-gx_g', '3OOK6-fiNy4RKIVu18atVw'}), ({'fxeRdFmgY6tbTyidpcdFLw', 'ZYdN05c0LC8OMJob0FWQdQ', 'wm3UghkWy48CWlcOHeq_tg'}, {'v_jBLgeJ1z5uVDzpZ-Wbkw', '3OOK6-fiNy4RKIVu18atVw'})] ],
        [ Cahokia_5_2, 3, 3, [({'fxeRdFmgY6tbTyidpcdFLw', 'ZYdN05c0LC8OMJob0FWQdQ', 'wm3UghkWy48CWlcOHeq_tg'}, {'cVOC5jLNpP78yf5kh-gx_g', 'v_jBLgeJ1z5uVDzpZ-Wbkw', '3OOK6-fiNy4RKIVu18atVw'})] ],
        [ Cahokia_5_2, 5, 1, [({'dxnaNew02Mu_391Xi1z2cQ', 'wm3UghkWy48CWlcOHeq_tg', 'ZYdN05c0LC8OMJob0FWQdQ', 'fxeRdFmgY6tbTyidpcdFLw', 'ZLjJPu8ebws1EM0lUZQ_Dw'}, {'v_jBLgeJ1z5uVDzpZ-Wbkw'})] ],
        [ Cahokia_10_2, 3, 3, [({'wm3UghkWy48CWlcOHeq_tg', 'ZYdN05c0LC8OMJob0FWQdQ', 'fxeRdFmgY6tbTyidpcdFLw'}, {'cVOC5jLNpP78yf5kh-gx_g', 'v_jBLgeJ1z5uVDzpZ-Wbkw', '3OOK6-fiNy4RKIVu18atVw'})] ],
        [ Cahokia_10_2, 4, 2, [({'ZYdN05c0LC8OMJob0FWQdQ', 'hKBQ-PFlcB-t5FK3HUxoyQ', 'DzTIbRWh5RJ_k6MIOuWvcQ', 'fxeRdFmgY6tbTyidpcdFLw'}, {'v_jBLgeJ1z5uVDzpZ-Wbkw', 'O998e7eUN45YDid-GxM1yw'}), ({'wm3UghkWy48CWlcOHeq_tg', 'ZYdN05c0LC8OMJob0FWQdQ', 's5udbbR5aP-W8eUFC5T9yQ', 'fxeRdFmgY6tbTyidpcdFLw'}, {'v_jBLgeJ1z5uVDzpZ-Wbkw', '3OOK6-fiNy4RKIVu18atVw'})] ],
        [ Belleville_5_3, 4, 2, [({'j3cmlhUwxmbHjTwHiLuhVA', 'fxeRdFmgY6tbTyidpcdFLw', 'lt666id1nW1OzT2wZDvrQA', '_xnLj_MdytIHGRpnoBBHOA'}, {'gfQmLdpBzhs_y1sQhIzjBQ', 'nwN92Uje-xIKE5voPTTvBQ'})] ],
        [ Belleville_15_3, 4, 4, [({'CoULkkk4RQ2q5yfT6ULdCw', 'j3cmlhUwxmbHjTwHiLuhVA', 'fxeRdFmgY6tbTyidpcdFLw', 'aT3nby92m66Qdg2TBzcCjg'}, {'wTrE0XUyPtRa2qRVPj4Vog', 'nwN92Uje-xIKE5voPTTvBQ', 'Xfv4ZGJ4u5t3LtSuZHpA0g', 'zMe0kY6KMRVdlUKmme-JpA'})] ],      
        [ Belleville_10_3, 6, 2, [({'lt666id1nW1OzT2wZDvrQA', 'fHK7WP6myyC7yF4sCA1MvQ', 'fxeRdFmgY6tbTyidpcdFLw', 'ur1iQz6TuEClyYYo4fd2Og', '_xnLj_MdytIHGRpnoBBHOA', 'j3cmlhUwxmbHjTwHiLuhVA'}, {'gfQmLdpBzhs_y1sQhIzjBQ', 'nwN92Uje-xIKE5voPTTvBQ'})] ],      
        [ Belleville_5_10, 5, 1, [({'OCwLhS1CwFYwmzTnKpdkpg', 'fxeRdFmgY6tbTyidpcdFLw', 'hKBQ-PFlcB-t5FK3HUxoyQ', 'j3cmlhUwxmbHjTwHiLuhVA', 'huHPQSQgw4kFakc0Vq7TDA'}, {'omKVwCFLQYs_ySD1bPk6iw'}), ({'OCwLhS1CwFYwmzTnKpdkpg', 'fxeRdFmgY6tbTyidpcdFLw', 'hKBQ-PFlcB-t5FK3HUxoyQ', 'j3cmlhUwxmbHjTwHiLuhVA', 'huHPQSQgw4kFakc0Vq7TDA'}, {'zMe0kY6KMRVdlUKmme-JpA'})] ],
        [ Belleville_5_10, 5, 2, [({'OCwLhS1CwFYwmzTnKpdkpg', 'fxeRdFmgY6tbTyidpcdFLw', 'hKBQ-PFlcB-t5FK3HUxoyQ', 'j3cmlhUwxmbHjTwHiLuhVA', 'huHPQSQgw4kFakc0Vq7TDA'}, {'omKVwCFLQYs_ySD1bPk6iw', 'zMe0kY6KMRVdlUKmme-JpA'})] ],
        [ Belleville_5_1, 4, 2, [({'j3cmlhUwxmbHjTwHiLuhVA', 'fxeRdFmgY6tbTyidpcdFLw', 'lt666id1nW1OzT2wZDvrQA', '_xnLj_MdytIHGRpnoBBHOA'}, {'gfQmLdpBzhs_y1sQhIzjBQ', 'nwN92Uje-xIKE5voPTTvBQ'})] ],
        [ Columbia_5_2, 4, 3, [({'amm1JkCs7Xv5hFb747AVUg', 'xdQzGzNu3nIUEvOGPW1tYw', '9SQPIP8ASyy6J7Ujjzi3Ag', 'DzTIbRWh5RJ_k6MIOuWvcQ'}, {'sMjjClYrGEXcTFG66qmg8A', 'IMCfwsS5hMrgSkyz_RlqLw', 's7JxSEtIumoFod2Jdj0_-g'}), ({'huHPQSQgw4kFakc0Vq7TDA', 'xdQzGzNu3nIUEvOGPW1tYw', 'amm1JkCs7Xv5hFb747AVUg', 'DzTIbRWh5RJ_k6MIOuWvcQ'}, {'sMjjClYrGEXcTFG66qmg8A', 's7JxSEtIumoFod2Jdj0_-g', 'C361vgN_65reegQhfOhFhw'}), ({'huHPQSQgw4kFakc0Vq7TDA', '9SQPIP8ASyy6J7Ujjzi3Ag', 'amm1JkCs7Xv5hFb747AVUg', 'DzTIbRWh5RJ_k6MIOuWvcQ'}, {'sMjjClYrGEXcTFG66qmg8A', 'qp63mnXqo2oMRrAKVoIm-g', 's7JxSEtIumoFod2Jdj0_-g'})] ],
        [ Columbia_5_2, 5, 1, [({'xdQzGzNu3nIUEvOGPW1tYw', '9SQPIP8ASyy6J7Ujjzi3Ag', 'DzTIbRWh5RJ_k6MIOuWvcQ', 'huHPQSQgw4kFakc0Vq7TDA', 'amm1JkCs7Xv5hFb747AVUg'}, {'sMjjClYrGEXcTFG66qmg8A'}), ({'xdQzGzNu3nIUEvOGPW1tYw', '9SQPIP8ASyy6J7Ujjzi3Ag', 'DzTIbRWh5RJ_k6MIOuWvcQ', 'huHPQSQgw4kFakc0Vq7TDA', 'amm1JkCs7Xv5hFb747AVUg'}, {'s7JxSEtIumoFod2Jdj0_-g'})] ],
        [ Columbia_5_2, 5, 2, [({'xdQzGzNu3nIUEvOGPW1tYw', '9SQPIP8ASyy6J7Ujjzi3Ag', 'DzTIbRWh5RJ_k6MIOuWvcQ', 'huHPQSQgw4kFakc0Vq7TDA', 'amm1JkCs7Xv5hFb747AVUg'}, {'sMjjClYrGEXcTFG66qmg8A', 's7JxSEtIumoFod2Jdj0_-g'})] ],
        [ Columbia_10_2, 4, 4, [({'huHPQSQgw4kFakc0Vq7TDA', 'xdQzGzNu3nIUEvOGPW1tYw', 'amm1JkCs7Xv5hFb747AVUg', 'zb4mISA7APPJUuQ_uidX6Q'}, {'sMjjClYrGEXcTFG66qmg8A', 's7JxSEtIumoFod2Jdj0_-g', '_D7QoWuQKMXk0mEE7r_Ftw', 'C361vgN_65reegQhfOhFhw'})] ],        
        [ Columbia_10_2, 5, 3, [({'xdQzGzNu3nIUEvOGPW1tYw', 'zb4mISA7APPJUuQ_uidX6Q', 'DzTIbRWh5RJ_k6MIOuWvcQ', 'huHPQSQgw4kFakc0Vq7TDA', 'amm1JkCs7Xv5hFb747AVUg'}, {'sMjjClYrGEXcTFG66qmg8A', 'C361vgN_65reegQhfOhFhw', 's7JxSEtIumoFod2Jdj0_-g'})] ],        
        [ Columbia_15_2, 4, 4, [({'huHPQSQgw4kFakc0Vq7TDA', 'amm1JkCs7Xv5hFb747AVUg', 'xdQzGzNu3nIUEvOGPW1tYw', 'zb4mISA7APPJUuQ_uidX6Q'}, {'sMjjClYrGEXcTFG66qmg8A', 'C361vgN_65reegQhfOhFhw', '_D7QoWuQKMXk0mEE7r_Ftw', 's7JxSEtIumoFod2Jdj0_-g'})] ],        
        [ Columbia_15_2, 6, 3, [({'ZYdN05c0LC8OMJob0FWQdQ', 'zb4mISA7APPJUuQ_uidX6Q', 'huHPQSQgw4kFakc0Vq7TDA', 'DzTIbRWh5RJ_k6MIOuWvcQ', 'njDoXyobuiqHKvtH8Iqgmw', '9TQVq1SDKnSZTt027y-ZAA'}, {'sMjjClYrGEXcTFG66qmg8A', 'SPfdgCODDJE1zTj5fACOGw', 's7JxSEtIumoFod2Jdj0_-g'})] ],
        [ Edwardsville_10_2, 6, 4, [({'n9GaZ_kxv03a86UrRtm1LA', 'VxQdmAO6lghp7_ZG0hpojA', 's6QghJT6IHNxV5MX8a66tw', 'MWxyukeYIxIbuzpciZNhXw', 'yKlcLYZ7w6XGU4JD3UjWJg', 'MTPka8o3xwDpEMMGQBtg5g'}, {'wMGjF3eTtmkOPudjV_z--Q', '4wep1OfeJbpz0DvBsoDdVg', 'zwGvMQ7Nw0VwqLUYDuxRXQ', 'EvBeuDww_OCNQZ-dRy6qzA'}), ({'XW-BonrE_YzzSgfdRD_1KA', 'n9GaZ_kxv03a86UrRtm1LA', 's6QghJT6IHNxV5MX8a66tw', 'MWxyukeYIxIbuzpciZNhXw', 'yKlcLYZ7w6XGU4JD3UjWJg', 'MTPka8o3xwDpEMMGQBtg5g'}, {'wbLXXbI-T6Av71i9AoiZRQ', 'AF4eN-oI7IWwjv0M9BiHxQ', '4wep1OfeJbpz0DvBsoDdVg', 'EvBeuDww_OCNQZ-dRy6qzA'})] ],
        [ Sauget_3_2, 1, 4, [({'mKBl4fAqTfNts7B78aOPVg'}, {'xXYYMUKs6mAGdLAXiTScvg', '7xAnCle53yC6GHa22j69jg', 'rnjXf1zDn9LGejhIX1tqxA', '4a15acANJFUsS3KxAzOT0g'})] ],
        [ Sauget_3_2, 2, 3, [({'mKBl4fAqTfNts7B78aOPVg', 'bSWWV65xqwiHf6njt1LwWg'}, {'xXYYMUKs6mAGdLAXiTScvg', '7xAnCle53yC6GHa22j69jg', '4a15acANJFUsS3KxAzOT0g'})] ],
        [ Sauget_3_2, 4, 2, [({'mKBl4fAqTfNts7B78aOPVg', 'TMLVzNYs-zwwREudyvI08A', 'bSWWV65xqwiHf6njt1LwWg', 'qWYEuBZP7av55tewg3PXKg'}, {'xXYYMUKs6mAGdLAXiTScvg', '7xAnCle53yC6GHa22j69jg'})] ],
        [ Sauget_3_2, 5, 1, [({'TMLVzNYs-zwwREudyvI08A', 'bSWWV65xqwiHf6njt1LwWg', 'qTMK2qr6ngof4fe29qyooA', 'qWYEuBZP7av55tewg3PXKg', 'mKBl4fAqTfNts7B78aOPVg'}, {'xXYYMUKs6mAGdLAXiTScvg'})] ],
        [ Sauget_5_2, 1, 4, [({'mKBl4fAqTfNts7B78aOPVg'}, {'xXYYMUKs6mAGdLAXiTScvg', '7xAnCle53yC6GHa22j69jg', '4a15acANJFUsS3KxAzOT0g', 'rnjXf1zDn9LGejhIX1tqxA'})] ],
        [ Sauget_5_2, 2, 3, [({'mKBl4fAqTfNts7B78aOPVg', 'bSWWV65xqwiHf6njt1LwWg'}, {'xXYYMUKs6mAGdLAXiTScvg', '7xAnCle53yC6GHa22j69jg', '4a15acANJFUsS3KxAzOT0g'})] ],
        [ Sauget_5_2, 4, 2, [({'mKBl4fAqTfNts7B78aOPVg', 'TMLVzNYs-zwwREudyvI08A', 'bSWWV65xqwiHf6njt1LwWg', 'qWYEuBZP7av55tewg3PXKg'}, {'xXYYMUKs6mAGdLAXiTScvg', '7xAnCle53yC6GHa22j69jg'})] ],
        [ Sauget_5_2, 5, 1, [({'TMLVzNYs-zwwREudyvI08A', 'bSWWV65xqwiHf6njt1LwWg', 'qTMK2qr6ngof4fe29qyooA', 'qWYEuBZP7av55tewg3PXKg', 'mKBl4fAqTfNts7B78aOPVg'}, {'xXYYMUKs6mAGdLAXiTScvg'})] ],
        [ Sauget_10_2, 1, 4, [({'mKBl4fAqTfNts7B78aOPVg'}, {'xXYYMUKs6mAGdLAXiTScvg', '7xAnCle53yC6GHa22j69jg', '4a15acANJFUsS3KxAzOT0g', 'rnjXf1zDn9LGejhIX1tqxA'})] ],
        [ Sauget_10_2, 2, 3, [({'mKBl4fAqTfNts7B78aOPVg', 'bSWWV65xqwiHf6njt1LwWg'}, {'xXYYMUKs6mAGdLAXiTScvg', '7xAnCle53yC6GHa22j69jg', '4a15acANJFUsS3KxAzOT0g'})] ],
        [ Sauget_10_2, 4, 2, [({'mKBl4fAqTfNts7B78aOPVg', 'TMLVzNYs-zwwREudyvI08A', 'bSWWV65xqwiHf6njt1LwWg', 'qWYEuBZP7av55tewg3PXKg'}, {'xXYYMUKs6mAGdLAXiTScvg', '7xAnCle53yC6GHa22j69jg'})] ],
        [ Sauget_20_2, 1, 4, [({'mKBl4fAqTfNts7B78aOPVg'}, {'xXYYMUKs6mAGdLAXiTScvg', '7xAnCle53yC6GHa22j69jg', '4a15acANJFUsS3KxAzOT0g', 'rnjXf1zDn9LGejhIX1tqxA'})] ],
        [ Sauget_20_2, 2, 3, [({'mKBl4fAqTfNts7B78aOPVg', 'bSWWV65xqwiHf6njt1LwWg'}, {'xXYYMUKs6mAGdLAXiTScvg', '7xAnCle53yC6GHa22j69jg', '4a15acANJFUsS3KxAzOT0g'})] ],
        [ Sauget_20_2, 4, 2, [({'mKBl4fAqTfNts7B78aOPVg', 'TMLVzNYs-zwwREudyvI08A', 'bSWWV65xqwiHf6njt1LwWg', 'qWYEuBZP7av55tewg3PXKg'}, {'xXYYMUKs6mAGdLAXiTScvg', '7xAnCle53yC6GHa22j69jg'})] ],
    ])

    def test_base(self, g, u, b, expected):
        var_name1 = get_var_name(g)
        result = dense_biclique(g, u, b)
        self.assertTrue(len(result)>0)
        self.assertTrue(all(any(X == U and Y == B for X, Y in expected) for U,B in result), f"Grafo: {var_name1}")
        self.assertTrue(all(any(X == U and Y == B for X, Y in result) for U,B in expected), f"Grafo: {var_name1}")

    def test_None(self):
        self.assertIsNone(dense_biclique(None, 1, 1))
        self.assertIsNone(dense_biclique(s_5_5, None, 1))
        self.assertIsNone(dense_biclique(s_5_5, 1, None))

    def test_null(self):
        self.assertIsNone(dense_biclique(nx.MultiGraph(),1,1))

    def test_positive (self):
        self.assertIsNone(dense_biclique(s_5_5, -1, 1))
        self.assertIsNone(dense_biclique(s_5_5, 1, -1))
        self.assertIsNone(dense_biclique(s_5_5, 1, 0))
        self.assertIsNone(dense_biclique(s_5_5, 0, 1))

if __name__ == '__main__':
    unittest.main(verbosity=2)
