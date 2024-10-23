import random
import string

import pytest
import json
from password_generator import password_generator

def password_score(password):
    lower_alpha_count = upper_alpha_count = number_count = whitespace_count = special_char_count = 0
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_alpha_count += 1
        elif char in string.ascii_uppercase:
            upper_alpha_count += 1
        elif char in string.digits:
            number_count += 1
        elif char == ' ':
            whitespace_count += 1
        else:
            special_char_count += 1
    strength = 0

    if lower_alpha_count >= 1:
        strength += 1
    if upper_alpha_count >= 1:
        strength += 1
    if number_count >= 1:
        strength += 1
    if whitespace_count >= 1:
        strength += 1
    if special_char_count >= 1:
        strength += 1

    return strength


def cargar_testcases():
    with open("password_generator.json",'r') as file:
        data = json.load(file)

        testcases = list()
        for case, values in data.items():
            inputs = values['input']
            outputs = values['output']
            testcases.append((inputs['req'],inputs['lenght'], outputs['out']))
        return testcases

@pytest.mark.parametrize("config, longitud, contrasenia", cargar_testcases())
def test_program(config, longitud, contrasenia):
    result1 = password_generator(config, longitud)
    score1 = password_score(result1)
    result2 = "".join(contrasenia)
    score2 = password_score(result2)
    
    assert score1 == pytest.approx(score2 , rel=1e-2)
    

