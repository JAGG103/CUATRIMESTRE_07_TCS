import pytest
import json
from next_day import next_day

def cargar_testcases():
    with open("next_day.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['d1'],inputs['m1'],inputs['y1'],outputs['d2'],outputs['m2'],outputs['y2']))
        return testcases

@pytest.mark.parametrize("d1, m1, y1, d2, m2, y2", cargar_testcases())
def test_triangle_type(d1,m1,y1,d2,m2,y2):
    resultado = next_day(d1,m1,y1)
    assert resultado == pytest.approx( (d2,m2,y2), rel=1e-2)