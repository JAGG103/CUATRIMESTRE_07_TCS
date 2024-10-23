import pytest
import json
from prime_checker import PrimeChecker

def cargar_testcases():
    with open("prime_checker.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['num'], outputs['out']))
        return testcases

@pytest.mark.parametrize("num, out", cargar_testcases())
def test_program(num, out):
    resultado = PrimeChecker(num)
    assert resultado == pytest.approx(out , rel=1e-2)
    

