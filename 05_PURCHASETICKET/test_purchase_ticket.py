import pytest
import json
from purchase_ticket import purchase_ticket

def cargar_testcases():
    with open("purchase_ticket.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['status'],inputs['fare'],inputs['_buffer'],outputs['actual_fare'],outputs['buffer']))
        return testcases

@pytest.mark.parametrize("status, fare, _buffer, actual_fare, buffer", cargar_testcases())
def test_purchase_ticket(status, fare, _buffer, actual_fare, buffer):
    resultado = purchase_ticket(status, fare, _buffer)
    assert resultado == pytest.approx( (actual_fare, buffer), rel=1e-2)
    

