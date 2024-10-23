import pytest
import json
from longest_common_subsequence import longest_common_subsequence

def cargar_testcases():
    with open("commonsubseq.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['a'], inputs['b'], outputs['commonseq']))
        return testcases

@pytest.mark.parametrize("a,b,commonseq", cargar_testcases())
def test_program(a,b,commonseq):
    resultado = longest_common_subsequence("".join(a), "".join(b))
    assert resultado == pytest.approx("".join(commonseq), rel=1e-2)
    

