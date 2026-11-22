import pandas as pd

data = {
    "Call Bid" : [6.67,6.18,5.68,5.19,4.7,4.22,3.75,3.28,2.83,2.39,1.98],
    "Call Theo" : [6.71,6.216,5.722, 5.231,4.744,4.261,3.785,3.319,2.867,2.434,2.024],
    "Call Ask" : [6.74,6.25,5.75,5.27,4.78,4.29,3.82,3.35,2.90,2.47,2.06],
    "Strike": [60.0,60.5,61.0,61.5,62.0,62.5,63.0,63.5,64.0,64.5,65.0],
    "Put Bid": [0.01,0.02,0.03, 0.03, 0.04, 0.06, 0.09, 0.12, 0.17, 0.23, 0.32],
    "Put Theo": [0.017,0.022,0.029, 0.038, 0.050, 0.067, 0.091, 0.125, 0.172, 0.239, 0.329],
    "Put Ask": [0.02,0.03, 0.04, 0.04, 0.06, 0.08, 0.10, 0.13, 0.18, 0.25, 0.34]
}

options = pd.DataFrame(data)
print(options)
underlying_price = 63.0 

def getCB(x):
    return options.loc[options["Strike"] == x, "Call Bid"].item()
def getCA(x):
    return options.loc[options["Strike"] == x, "Call Ask"].item()
def getCT(x):
    return options.loc[options["Strike"] == x, "Call Theo"].item()
def getPB(x):
    return options.loc[options["Strike"] == x, "Put Bid"].item()
def getPA(x):
    return options.loc[options["Strike"] == x, "Put Ask"].item()
def getPT(x):
    return options.loc[options["Strike"] == x, "Put Theo"].item()

print(getPT(63.0))
put_bid = options.loc[options["Strike"] == 64.0, "Put Bid"].item()
put_ask = options.loc[options["Strike"] == 64.0, "Put Ask"].item()
print(put_bid)
print(put_ask)

def edge(x,y):
    cost = getPA(x) - getPB(y)
    theo = getPT(x) - getPT(y)
    return theo - cost
print(f"{edge(64,63):.3f}")

def IVC(u,k):
    return print(max(0,u-k))
print(IVC(underlying_price, 64))

def IVP(u,k):
    return max(0,k-u)
print(IVP(underlying_price, 64))


def call_moneyness(u,k):
    if(u-k > 0):
        return print("ITM")
    elif(u-k == 0):
        return print("ATM")
    else:
        return print("OTM")
call_moneyness(underlying_price, 62)
call_moneyness(underlying_price, 63)
call_moneyness(underlying_price, 64)

def put_moneyness(u,k):
    if(k-u > 0):
        return print("ITM")
    elif(k-u == 0):
        return print("ATM")
    else:
        return print("OTM")
put_moneyness(underlying_price, 64)
put_moneyness(underlying_price, 63)
put_moneyness(underlying_price, 62)