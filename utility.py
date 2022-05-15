def take_multiple_inputs(list_of_inputs):
    inputs_req = list_of_inputs
    inputs = []
    for i in inputs_req:
        inputs.append(input(f"> Enter your {i}: "))

    return inputs


def validate(string):
    return string != ""
