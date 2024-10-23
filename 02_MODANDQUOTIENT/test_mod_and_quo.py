import pytest
import json
from mod_and_quotient import mod

def cargar_testcases():
    with open("mod_and_quo.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['x'],inputs['y'],outputs['r'],outputs['q']))
        return testcases

@pytest.mark.parametrize("x, y, r, q", cargar_testcases())
def test_modanquo(x,y,r,q):
    resultado = mod(x,y)
    assert resultado == pytest.approx((r,q), rel=1e-2)