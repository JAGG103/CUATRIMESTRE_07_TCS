import pytest
import json
from triangle_type import triangletype

def cargar_testcases():
    with open("triangle_type.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['a'],inputs['b'],inputs['c'],outputs['q']))
        return testcases

@pytest.mark.parametrize("a, b, c, q", cargar_testcases())
def test_triangle_type(a,b,c,q):
    resultado = triangletype(a,b,c)
    assert resultado == pytest.approx(q, rel=1e-2)
    

