# PL: Sprawdzenie czy sekwencja może powstać w BST SEARCH
# EN: Check if sequence is valid BST search path

def is_valid_bst_search(sequence, key):
    low = float('-inf')
    high = float('inf')

    for x in sequence:
        if x < low or x > high:
            return False
        if key < x:
            high = x
        elif key > x:
            low = x
        else:
            return True
    return False


if __name__ == "__main__":
    seq = [2, 252, 401, 398, 330, 344, 397, 363]
    print(is_valid_bst_search(seq, 363))