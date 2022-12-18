alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
reversed_alphabet_dict = {k: v for k, v in zip(alphabet, reversed(alphabet))}

def solution(encrypted_str)
    result = ""
    for v in encrypted_str:
        result+=reversed_alphabet_dict.get(v, v)
