import pytest
import json
from kth import kth

def cargar_testcases():
    with open("kth.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['arr'], inputs['k'], outputs['e']))
        return testcases

@pytest.mark.parametrize("arr, k, e", cargar_testcases())
def test_program(arr, k, e):
    resultado = kth(arr, k)
    assert resultado == pytest.approx(e, rel=1e-2)
    

