import pytest
import json
from discount_collage import discount_collage

def cargar_testcases():
    with open("discount_collage.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['month'],inputs['college'], outputs['total']))
        return testcases

@pytest.mark.parametrize("m, c, t", cargar_testcases())
def test_program(m,c,t):
    resultado = discount_collage("".join(m).replace(" ",""), c)
    assert resultado == pytest.approx(t , rel=1e-2)
    

