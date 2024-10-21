def count_vowels(input_string):
    """Count the number of vowels in a string"""
    vowels = "aeiouAEIOU"
    count = sum( 1 for char in input_string if char in vowels)
    return count

def vowel_counter():
    """Main function to take input and show the number of vowels."""
    user_input = input (" Enter a string to count its vowels: ")
    vowel_count = count_vowels(user_input)
    print(f"The string contains {vowel_count} vowels(s).")

if __name__ == "__main__":
    vowel_counter()
    