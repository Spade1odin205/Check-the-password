# entropy_utils.py
import math
from collections import Counter
import string

def shannon_entropy(s):
    if not s: return {"bits_per_char":0.0, "total_bits":0.0}
    L = len(s)
    freqs = Counter(s)
    H = 0.0
    for cnt in freqs.values():
        p = cnt / L
        H -= p * math.log2(p)
    return {"bits_per_char": H, "total_bits": H * L}

def alphabet_estimate(s):
    has_lower = any(c.islower() for c in s)
    has_upper = any(c.isupper() for c in s)
    has_digit = any(c.isdigit() for c in s)
    has_sym = any(c in string.punctuation for c in s)
    size = 0
    if has_lower: size += 26
    if has_upper: size += 26
    if has_digit: size += 10
    if has_sym: size += 32
    if size == 0:
        return {"alphabet_size":0, "bits_per_char":0, "total_bits":0}
    bpc = math.log2(size)
    return {"alphabet_size":size, "bits_per_char":bpc, "total_bits": bpc * len(s)}

def ngram_entropy(s, n=2):
    if len(s) < n: return 0.0
    ngrams = [s[i:i+n] for i in range(len(s)-n+1)]
    L = len(ngrams)
    freqs = Counter(ngrams)
    H = 0.0
    for cnt in freqs.values():
        p = cnt / L
        H -= p * math.log2(p)
    return H

def est_crack_time_seconds(bits, guesses_per_sec=1e9):
    # approximate brute-force attempts = 2^bits
    if bits <= 0: return 0.0
    attempts = 2**bits
    return attempts / guesses_per_sec

def load_toplist(path):
    # each line one password, return set for quick check
    with open(path, 'r', encoding='utf8', errors='ignore') as f:
        return set(line.strip() for line in f if line.strip())
