import pytest
import json
from is_valid_parenthesization import is_valid_parenthesization

def cargar_testcases():
    with open("is_valid_parenthesization.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['in'], outputs['isvalid']))
        return testcases

@pytest.mark.parametrize("parens, isvalid", cargar_testcases())
def test_program(parens, isvalid):
    resultado = is_valid_parenthesization("".join(parens))
    assert resultado == pytest.approx(isvalid , rel=1e-2)
    

