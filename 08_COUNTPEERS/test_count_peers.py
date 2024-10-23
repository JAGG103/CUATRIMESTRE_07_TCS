import pytest
import json
from count_peers import count_peers

def cargar_testcases():
    with open("count_peers.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['number'], outputs['countOut']))
        return testcases

@pytest.mark.parametrize("n, c", cargar_testcases())
def test_program(n, c):
    resultado = count_peers(n)
    assert resultado == pytest.approx(c, rel=1e-2)
    
