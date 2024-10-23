import pytest
import json
from middle_number import middle_number

def cargar_testcases():
    with open("middle_number.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['x'],inputs['y'],inputs['z'], outputs['middle']))
        return testcases

@pytest.mark.parametrize("x,y,z,middle", cargar_testcases())
def test_program(x,y,z,middle):
    resultado = middle_number(x,y,z)
    assert resultado == pytest.approx(middle , rel=1e-2)
    

