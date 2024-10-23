import pytest
import json
from password_strength import check_password_strength

def cargar_testcases():
    with open("password_strenght.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['pass'], outputs['score']))
        return testcases

@pytest.mark.parametrize("password, score", cargar_testcases())
def test_program(password, score):
    resultado = check_password_strength(password if type(password)==str else "".join(password))
    assert resultado == pytest.approx(tuple(score) , rel=1e-2)
    

