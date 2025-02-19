def get_longest_valid_substring(word: str, forbidden: list[str]) -> int:
    
    # O(n^2) implementation to find longest substring not contained within the list of forbidden words
    
    left_idx = 0
    forbidden = set(forbidden)
    word_length = len(word)
    max_length = 0
    
    for right_idx in range(1, word_length + 1):
        sub_word = word[left_idx:right_idx]
        
        if any(forbidden_word in sub_word for forbidden_word in forbidden):
            max_length = max(max_length, right_idx - 1 - left_idx)
            left_idx += 1

        max_length = max(max_length, right_idx - left_idx)
            
    return max_length

def get_longest_valid_substring_improved(word: str, forbidden: list[str]) -> int:
    
    # O(mn) implementation to find longest substring not contained within the list of forbidden words optimized by only checking the substring length that is necessary
    
    left_idx = 0
    forbidden = set(forbidden)
    word_length = len(word)
    max_forbidden_length = 10
    max_length = 0
    
    for right_idx in range(word_length):
        for substring_length in range(1, min(max_forbidden_length, right_idx - left_idx + 1) + 1):
        
            sub_word = word[right_idx - substring_length + 1:right_idx + 1]
            
            if any(forbidden_word in sub_word for forbidden_word in forbidden):
                left_idx = right_idx - substring_length + 2
                break

        max_length = max(max_length, right_idx - left_idx + 1)
            
    return max_length

if __name__ == "__main__":
    print(get_longest_valid_substring_improved("aaabccccacacacaabcbaaabacbbbcabcbcaacbabccbababcabaacaacbbcbaabc", ["bbbacbcb","bcbaaabacb","abbbbcb","bcbcbac","cbaabbbbbb","bbbbaabcb","cccaaaacaa","cbabaaca","baaabacbb","abcabaacaa"]))