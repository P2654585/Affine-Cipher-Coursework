import math
def entropy(s):
    # Letter Frequency Chart for English
    freq = { 
        'E': 0.1202, 'T': 0.091, 'A': 0.0812, 'O': 0.0768, 'I': 0.0731,
        'N': 0.0695, 'S': 0.0628, 'R': 0.0602, 'H': 0.0592, 'D': 0.0432, 
        'L': 0.0398, 'U': 0.0288, 'C': .0271, 'M': 0.0261, 'F': 0.023, 
        'Y': 0.0211, 'W': 0.0209, 'G': 0.0203, 'P': 0.0182, 'B': 0.0149, 
        'V': 0.0111, 'K': 0.0069, 'X': 0.0017, 'Q': 0.0011, 'J': 0.001, 
        'Z': 0.0007 
    }
    ascii_range = (65, 90)

    # Ensure the string's case matches the dictionary keys
    s = s.upper()

    # Using the frequency of a letter as p(x), calculate entropy of the string using the formula:
    # H = [sum of (-log[p(x)]_2)] / len(s)
    total_entropy = 0
    for c in s:
        if(ord(c) >= ascii_range[0] and ord(c) <= ascii_range[1]): # Only compute for values of A-Z
            total_entropy += -math.log(freq[c], 2)

    total_entropy = total_entropy / len(s)

    return total_entropy