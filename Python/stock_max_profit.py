'''
Stock max problem
URL: https://www.hackerrank.com/challenges/stockmax/problem
URL: https://www.geeksforgeeks.org/stock-buy-sell/
fast and simple. find the max price, split the array before and after max price, 
buy all stocks before max price and then sell them at max price; 
repeat above procedure on the array after max element. Thats it!
'''
def iter_over_p(p):
    ind_max = p.index(max(p))
    inv = sum(p[:ind_max])
    pf = len(p[:ind_max])*p[ind_max] - inv
    if len(p[ind_max+1:]) > 0:
        pf += iter_over_p(p[ind_max+1:])
    return pf

def stockmax(p):
    c=p[len(p)-1]
    a=0
    for i in range(len(p)-1,-1,-1):
        if c<p[i]:
            c=p[i]

        a+=(c-p[i])
        print(f"C: {c} P:{p[i]} Add: {c-p[i]} A: {a}")

    return a

if __name__ == '__main__':

    # prices = [1, 2, 3] # : buy 1 share, buy 1 share, sell 2 shares at $3 per share 
    prices = [4, 3, 2] # : do nothing
    prices = [5, 7, 1, 2] # : buy 1 share at $5, sell 1 share at $7, buy 1 share at $1, sell one share at $2

    # profit = iter_over_p(prices)
    profit = stockmax(prices)
    print(f"Profit: {profit}")