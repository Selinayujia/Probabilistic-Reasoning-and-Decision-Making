# -*- coding: utf-8 -*-
"""
cs 250 hw1 1.9 c
"""

def count(all_counts):       # 1.9 a

    all_counts = sorted(all_counts, key=lambda x: x[1])
    least_frequent_15 = [item for item in all_counts[:14]]
    most_frequent_15 = [item for item in all_counts[len(all_counts)-15:]]
    most_frequent_15.reverse()
    return most_frequent_15, least_frequent_15
    
    

def best_guess(words, correct_guessed, correct_guessed_pos, incorrect_guessed):   # 1.9 b
 
    words_satisfied_evidence = 0
    alphabet_match_count = [0] * 26
                     
    for word in words:
        evidence = True
        for i, c in enumerate(correct_guessed):
            if word[0][correct_guessed_pos[i]] != c or word[0].count(c) > correct_guessed.count(c):
                evidence = False
                break
            
        if evidence:
            for c in incorrect_guessed:
                if c in word[0]:
                    evidence = False
                    break
        if evidence:

            words_satisfied_evidence += word[1]
            
            
            for c in set(word[0]):
                if c not in correct_guessed:
                    index = ord(c) - ord('A')
                    alphabet_match_count[index] += word[1]
    
    max_count = (0, None)
    for i, count in enumerate(alphabet_match_count):
        if count > max_count[0]:
            max_count = (count, chr(ord('A')+i))
        
    return max_count[1], round(max_count[0]/words_satisfied_evidence, 4)

            
            
    
    
if __name__ == "__main__":
    file = open('hw1_word_counts_05-2.txt', 'r')
    all_counts = []
    for line in file:
        line.removesuffix('\n')
        word, c = line.split(' ')
        all_counts.append((word,int(c)))
    file.close()
        
        
    most_frequent, least_frequent = count(all_counts)
    print(f'The most frequent 15 words are :{most_frequent}\n\n\n',
          f'The least frequent 14 words are :{least_frequent}\n\n\n')
    
    
    best_guess_alphabet, probability = best_guess(all_counts, [], [], [])
    print(f'Best guess is {best_guess_alphabet}, the probablity is {probability}\n\n')
    
    best_guess_alphabet, probability = best_guess(all_counts, [], [], ['E', 'A'])
    print(f'Best guess is {best_guess_alphabet}, the probablity is {probability}\n\n')
    
    best_guess_alphabet, probability = best_guess(all_counts, ['A','S'], [0,4], [])
    print(f'Best guess is {best_guess_alphabet}, the probablity is {probability}\n\n')
    
    best_guess_alphabet, probability = best_guess(all_counts, ['A','S'], [0,4], ['I'])
    print(f'Best guess is {best_guess_alphabet}, the probablity is {probability}\n\n')
    
    best_guess_alphabet, probability = best_guess(all_counts, ['O'], [2], ['A', 'E', 'M', 'N', 'T'])
    print(f'Best guess is {best_guess_alphabet}, the probablity is {probability}\n\n')
    
    best_guess_alphabet, probability = best_guess(all_counts, [], [], ['E', 'O'])
    print(f'Best guess is {best_guess_alphabet}, the probablity is {probability}\n\n')
    
    
    best_guess_alphabet, probability = best_guess(all_counts, ['D','I'], [0, 3], [])
    print(f'Best guess is {best_guess_alphabet}, the probablity is {probability}\n\n')
    
    
    best_guess_alphabet, probability = best_guess(all_counts, ['D','I'], [0, 3], ['A'])
    print(f'Best guess is {best_guess_alphabet}, the probablity is {probability}\n\n')
    
    best_guess_alphabet, probability = best_guess(all_counts, ['U'], [1], ['A', 'E', 'I', 'O', 'S'])
    print(f'Best guess is {best_guess_alphabet}, the probablity is {probability}\n\n')
    
    

    