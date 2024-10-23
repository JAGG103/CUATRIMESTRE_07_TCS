import pytest
import json
from bill_calculator import bill_calculator

def cargar_testcases():
    with open("bill_calculator.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['account'],inputs['percentage'], outputs['total']))
        return testcases

@pytest.mark.parametrize("a, p, t", cargar_testcases())
def test_program(a,p,t):
    resultado = bill_calculator(a,p)
    assert resultado == pytest.approx(t , rel=1e-2)
    
