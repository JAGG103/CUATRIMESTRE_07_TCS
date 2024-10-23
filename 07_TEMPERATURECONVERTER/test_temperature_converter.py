import pytest
import json
from temperature_converter import temperatureConverter

def cargar_testcases():
    with open("temperature_converter.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['T'],inputs['KoF'], outputs['C']))
        return testcases

@pytest.mark.parametrize("T, KoF, C", cargar_testcases())
def test_grade_calculator(T, KoF, C):
    result = temperatureConverter(T, KoF)
    assert result == pytest.approx(C, rel=1e-2)