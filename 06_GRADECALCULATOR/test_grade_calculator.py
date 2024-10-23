import pytest
import json
from grade_calculator import grade_calculator

def cargar_testcases():
    with open("grade_calculator.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['score'], outputs['grade']))
        return testcases

@pytest.mark.parametrize("score, grade", cargar_testcases())
def test_grade_calculator(score, grade):
    result = grade_calculator(score)
    assert result == grade