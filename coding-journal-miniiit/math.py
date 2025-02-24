print ("hello world")
import re

def find_pattern(pattern, text):
    matches = re.findall(pattern, text)
    return matches

pattern = '2+5'  # This pattern finds repeated words
text = "find the pattern"
found_patterns = find_pattern(pattern, text)
print("Found patterns:", found_patterns)
