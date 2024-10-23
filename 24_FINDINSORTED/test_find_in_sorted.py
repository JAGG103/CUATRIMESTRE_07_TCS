import pytest
import json
from find_in_sorted import find_in_sorted

def cargar_testcases():
    with open("find_in_sorted.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['arr'],inputs['x'], outputs['ind']))
        return testcases

@pytest.mark.parametrize("arr, x, ind", cargar_testcases())
def test_program(arr, x, ind):
    resultado = find_in_sorted(arr, x)
    assert resultado == pytest.approx(ind, rel=1e-2)
    

