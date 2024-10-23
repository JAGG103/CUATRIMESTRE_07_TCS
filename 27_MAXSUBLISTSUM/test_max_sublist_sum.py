import pytest
import json
from max_sublist_sum import max_sublist_sum

def cargar_testcases():
    with open("max_sublist_sum.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['arr'], outputs['sum']))
        return testcases

@pytest.mark.parametrize("arr, sum", cargar_testcases())
def test_program(arr, sum):
    resultado = max_sublist_sum(arr)
    assert resultado == pytest.approx(sum, rel=1e-2)
    

