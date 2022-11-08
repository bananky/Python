def sum_seq(sequence):
    sum_of_elements = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):
            sum_of_elements += sum_seq(element)
        else:
            sum_of_elements += element
    return sum_of_elements


test_sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print("Suma elementów: ", sum_seq(test_sequence))