import pytest
import json
from comission import commission

def cargar_testcases():
    with open("commission.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['a'],inputs['b'],inputs['c'],outputs['q']))
        return testcases

@pytest.mark.parametrize("a, b, c, q_esperado", cargar_testcases())
def test_commission(a,b,c,q_esperado):
    resultado = commission(a,b,c)
    assert resultado == pytest.approx(q_esperado, rel=1e-2)
    

