class TextProcessor:
    # Implement method overloading for format_text method
    pass
    def format_text(self, word1, word2 = ""):
        if word1 and word2:
            return word1 + word2
        return word1.upper()
    

# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
