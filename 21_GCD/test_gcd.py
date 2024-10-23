import pytest
import json
from gcd import gcd

def cargar_testcases():
    with open("gcd.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['x'],inputs['y'], outputs['r']))
        return testcases

@pytest.mark.parametrize("a,b,r", cargar_testcases())
def test_program(a,b,r):
    resultado = gcd(a,b)
    assert resultado == pytest.approx(r , rel=1e-2)
    

