import random

def main():
    numbers = [16.2, 75.1, 52.3]
    words = ['join', 'love', 'smile', 'love', 'cloud', 'head']
    
    quantity = 5
    print(f" numbers {numbers}")  
    append_random_numbers(numbers)
    append_random_numbers(numbers, quantity)
    append_random_words(words, quantity)
    print(f" numbers {numbers}") 
    print(f"Words {words}")

def append_random_numbers(numbers_list, quantity = 1):
    random_number = random.choice(numbers_list)
    new_quantity = random.uniform(quantity, random_number)
    round_number = round(new_quantity,1)
    numbers_list.append(round_number)
    return numbers_list

def append_random_words(words_list, quantity = 1):
    word_random = ['ok', 'haop', 'beans']
    random_word = random.choice(word_random)
    words_list.append(random_word)
    return words_list



if __name__ == "__main__":
    main()