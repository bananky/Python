def flatten(sequence):
    result_list = []
    return flatten2(sequence, result_list)


def flatten2(sequence, result_list):
    for element in sequence:
        if isinstance(element, (list, tuple)):
            flatten2(element, result_list)
        else:
            result_list.append(element)
    return result_list


test_sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print("Spłaszczona lista elementów: ", flatten(test_sequence))
