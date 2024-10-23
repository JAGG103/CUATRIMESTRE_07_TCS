import pytest
import json
from bucketsort import bucketsort

def cargar_testcases():
    with open("bucketsort.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['seqin'],inputs['up'], outputs['seqout']))
        return testcases

@pytest.mark.parametrize("arr, k, arrsorted", cargar_testcases())
def test_program(arr, k, arrsorted):
    resultado = bucketsort(arr,k)
    assert resultado == pytest.approx(arrsorted , rel=1e-2)
    

