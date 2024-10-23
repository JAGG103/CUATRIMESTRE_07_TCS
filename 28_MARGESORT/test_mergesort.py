import pytest
import json
from mergesort import mergesort

def cargar_testcases():
    with open("margesort.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['arr'], outputs['arrsorted']))
        return testcases

@pytest.mark.parametrize("arr, arrsorted", cargar_testcases())
def test_program(arr, arrsorted):
    resultado = mergesort(arr)
    assert resultado == pytest.approx(arrsorted , rel=1e-2)
    
