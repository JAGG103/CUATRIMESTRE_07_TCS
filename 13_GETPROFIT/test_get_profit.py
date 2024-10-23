import pytest
import json
from get_profit import get_profit

def cargar_testcases():
    with open("get_profit.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['dic1'],inputs['dic2'], outputs['sum']))
        return testcases

@pytest.mark.parametrize("dic1, dic2, sum", cargar_testcases())
def test_program(dic1, dic2, sum):
    resultado = get_profit(dict(dic1), dict(dic2))
    assert resultado == pytest.approx(sum , rel=1e-2)
    

