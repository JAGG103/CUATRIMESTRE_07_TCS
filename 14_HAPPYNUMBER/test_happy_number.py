import pytest
import json
from happy_number import happy_number

def cargar_testcases():
    with open("happy_number.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['number'], outputs['ishappy']))
        return testcases

@pytest.mark.parametrize("num, ishappy", cargar_testcases())
def test_program(num, ishappy):
    resultado = happy_number(num)
    assert resultado == pytest.approx(ishappy , rel=1e-2)
    
