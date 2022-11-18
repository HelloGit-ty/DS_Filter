#from functools import lru_cache
def is_apna_secret_var(line: str) -> bool:
    if "auth" in line.lower() or "token" in line.lower() or "key" in line.lower() or "pass" in line.lower():
        if any(chr.isdigit() for chr in line):
            return False
        else:
            return True
    elif "srv" in line.lower():
        return False
    else:
        return True
