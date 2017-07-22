import re

def is_isogram(word):
    sanitized = re.sub(r'[\s\-]*', '', word)
    sanitized = sanitized.upper()
    if not sanitized or len(sanitized) == 1:
        return True
    else:
        for i,c in enumerate(sanitized):
            if i < len(sanitized) - 1 and sanitized[0] == sanitized[i+1]:
                return False
            elif  i < len(sanitized) - 1 and sanitized[0] != sanitized[i+1]:
                continue
            else:
                return is_isogram(sanitized[1:])
