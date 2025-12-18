import re
import os

# --- Decorator as per 'Automation' requirement ---
def file_exists_check(func):
    """Decorator to check if the input file exists before processing."""
    def wrapper(self, filename, *args, **kwargs):
        if not os.path.exists(filename):
            print(f"Error: The file '{filename}' was not found.")
            return None
        return func(self, filename, *args, **kwargs)
    return wrapper

class TextProcessor:
    def __init__(self):
        # A basic list of stopwords to remove
        self.stopwords = set([
            "the", "is", "in", "at", "of", "a", "and", "or", "to", "for", 
            "with", "on", "as", "by", "an", "be", "it", "that", "this", 
            "are", "was", "were", "from"
        ])

    def clean_text(self, text):
        """
        Removes stopwords and punctuation to prepare text for analysis.
        Returns a list of clean words.
        """
        # Lowercase
        text = text.lower()
        
        # Remove punctuation using Regex (keeping only words and spaces)
        text = re.sub(r'[^\w\s]', '', text)
        
        # Split into words
        words = text.split()
        
        # Remove stopwords
        clean_words = [word for word in words if word not in self.stopwords]
        
        return clean_words