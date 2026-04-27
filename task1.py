def count_vowels_and_consonants(text: str) -> dict:
    count_vowel = 0
    count_consonants = 0
    vowels_set = set("aeiouAEIOU")
    new = {}
    for letter in text:
        if letter.isalpha():
            if letter in vowels_set:
                count_vowel+=1
            else:
                count_consonants+=1
    new.setdefault("Unli", count_vowel)
    new.setdefault("Undosh", count_consonants)
    return new

print(count_vowels_and_consonants("Salom Dunyo!"))