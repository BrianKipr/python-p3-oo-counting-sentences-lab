#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        sentences = [s.strip() for s in self.value.split('.') if s.strip()]
        return len(sentences)

# Example usage:
if __name__ == "__main__":
    my_string = MyString("This is a sentence. And another one! How many sentences are here?")
    print(f"Is a sentence: {my_string.is_sentence()}")
    print(f"Is a question: {my_string.is_question()}")
    print(f"Is an exclamation: {my_string.is_exclamation()}")
    print(f"Number of sentences: {my_string.count_sentences()}")
