# Custom practice: portfolio vs benchmark -> BUY / SELL transactions
# Format: Vodafone,STOCK,10|Google,STOCK,15   (split('|') needs no escape in Python)
def parse_portfolio(s):
    holdings = {}
    if not s.strip():
        return holdings
    for item in s.split('|'):
        name, kind, qty = item.split(',')
        key = (name.strip(), kind.strip())
        holdings[key] = holdings.get(key, 0) + int(qty)
    return holdings


def rebalance(portfolio, benchmark):
    current = parse_portfolio(portfolio)
    target = parse_portfolio(benchmark)
    result = []
    # sorted keys give alphabetical output
    for name, kind in sorted(set(current) | set(target)):
        diff = target.get((name, kind), 0) - current.get((name, kind), 0)
        if diff > 0:
            result.append(f'BUY,{name},{kind},{diff}')
        elif diff < 0:
            result.append(f'SELL,{name},{kind},{-diff}')
    return result


if __name__ == '__main__':
    print(rebalance('Vodafone,STOCK,10|Google,STOCK,15', 'Vodafone,STOCK,12|Apple,STOCK,5'))
    # ['BUY,Apple,STOCK,5', 'SELL,Google,STOCK,15', 'BUY,Vodafone,STOCK,2']
    print(rebalance('A,STOCK,5', 'A,STOCK,5'))  # []
    print(rebalance('', 'A,STOCK,5'))           # ['BUY,A,STOCK,5']
