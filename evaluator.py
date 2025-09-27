# evaluator.py
from entropy_utils import shannon_entropy, alphabet_estimate, ngram_entropy, est_crack_time_seconds, load_toplist

TOPLIST = load_toplist('D:/Code/Python/Project/Password_Entropy/Pwdb_top-1000.txt')  # bạn chuẩn bị file này (nguồn công khai)

def evaluate_password(pw):
    out = {}
    out['length'] = len(pw)
    out.update(shannon_entropy(pw))
    out['alphabet'] = alphabet_estimate(pw)
    out['ngram_2'] = ngram_entropy(pw, 2)
    out['ngram_3'] = ngram_entropy(pw, 3)
    out['in_toplist'] = pw in TOPLIST
    out['crack_time_seconds_alphabet'] = est_crack_time_seconds(out['alphabet']['total_bits'])
    # simple rule-based final score
    score = 0
    if out['alphabet']['total_bits'] > 50: score += 2
    if out['total_bits'] > 40: score += 1
    if out['ngram_2'] > (out['bits_per_char'] * 0.8): score += 1
    if not out['in_toplist']: score += 1
    # map score to label
    if out['in_toplist'] or score <=1:
        out['label'] = 'Weak'
    elif score == 2 or score == 3:
        out['label'] = 'Medium'
    else:
        out['label'] = 'Strong'
    return out
