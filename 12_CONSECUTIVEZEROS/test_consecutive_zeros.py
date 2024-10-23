import pytest
import json
from consecutive_zeros import consecutive_zeroes

def cargar_testcases():
    with open("consecutive_zeros.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['number'], inputs['base'], outputs['iscz']))
        return testcases

@pytest.mark.parametrize("N, k, iscz", cargar_testcases())
def test_program(N, k, iscz):
    resultado = consecutive_zeroes(N, k)
    assert resultado == pytest.approx(iscz, rel=1e-2)
    

