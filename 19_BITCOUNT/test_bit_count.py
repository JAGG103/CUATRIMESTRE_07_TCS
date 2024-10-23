import pytest
import json
from bit_count import bitcount

def cargar_testcases():
    with open("bit_count.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['n'], outputs['count']))
        return testcases

@pytest.mark.parametrize("n, count", cargar_testcases())
def test_program(n, count):
    resultado = bitcount(n)
    assert resultado == pytest.approx(count, rel=1e-2)
    
