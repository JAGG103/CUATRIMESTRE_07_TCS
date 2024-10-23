import pytest
import json
from modular_equation import numberOfPossibleWaysUtil

def cargar_testcases():
    with open("modular_equation.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['A'], inputs['B'], outputs['nofsOut']))
        return testcases

@pytest.mark.parametrize("A, B, nofsOut", cargar_testcases())
def test_program(A, B, nofsOut):
    resultado = numberOfPossibleWaysUtil(A, B)
    assert resultado == pytest.approx(nofsOut , rel=1e-2)
    

