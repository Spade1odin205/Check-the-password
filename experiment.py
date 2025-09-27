import pandas as pd
from evaluator import evaluate_password

def run_on_list(password_list, name):
    rows=[]
    for pw in password_list:
        res = evaluate_password(pw)
        res['pw'] = pw
        rows.append(res)
    df = pd.DataFrame(rows)
    df.to_csv(f'results_{name}.csv', index=False)
    return df

# example usage:
if __name__ == "__main__":
    # load your lists
    with open('generated_random.txt') as f:
        gen = [l.strip() for l in f if l.strip()]
    df = run_on_list(gen[:2000], 'generated')
    print(df[['pw','label','total_bits','alphabet']].head())
