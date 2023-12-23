def repeated_dna(s):
    visited_seq, result = set(), set()

    for left_ptr in range(len(s) - 9):
        curr_seq = s[left_ptr:left_ptr + 10]
        if curr_seq in visited_seq:
            result.add(curr_seq)
        visited_seq.add(curr_seq)

    return list(result)


"""The above stores characters in the set as hash keys which are 8 bits long. 
Therefore a sequence will store 10*8=80bits hash keys. 
In order to optimize it mapping the chars to 2 bits number either 01, 10, 11, 00 
as the DNA sequence will contain 'A', 'C', 'G', and 'T'. The hash key size will reduce to 2*10=20 bits"""

# NOTE: Improve the code for the below input
# def repeated_dna_2(s):
#     mapping = {
#         'A': '11',
#         'C': '00',
#         'G': '10',
#         'T': '01'
#     }
#     new_input = ''
#     for char in s:
#         new_input += mapping[char]
#
#     # mapping the chars back to the original one
#     def remap_sequence(seq):
#         result_seq = ''
#         for i in range(0, len(seq) - 1, 2):
#             for key, val in mapping.items():
#                 if seq[i:i + 2] == val:
#                     result_seq += key
#                     break
#
#         return result_seq
#
#     visited_seq, result = set(), set()
#
#     for left_ptr in range(len(new_input) - 19):
#         curr_seq = new_input[left_ptr:left_ptr + 20]
#         if curr_seq in visited_seq:
#             remapped_seq = remap_sequence(curr_seq)
#             result.add(remapped_seq)
#         visited_seq.add(curr_seq)
#
#     return list(result)


res = repeated_dna("GAGAGAGAGAGAG")
# res = repeated_dna_2("GAGAGAGAGAGAG")
print(res)
