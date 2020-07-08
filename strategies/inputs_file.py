def user_inputter(info_message_str):
    print(info_message_str)
    ################"""
    input_abs=input()
    return input_abs


def read_resource(filename):
    with open(filename, 'r') as f:
        list_of_sentences=f.readlines()
    return list_of_sentences
