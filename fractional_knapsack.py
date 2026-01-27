def sort_by_value(item):
    return item[0]#value (profit)
def sort_by_weight(item):
    return item[1]#value (weight)
def sort_by_ratio(item):
    return item[0]/item[1]#value (profit)
def fractional_knapsack(W,items,stragery="ratio"):
    if stragery=='value':
        items.sort(key=sort_by_value,reverse=True)
    elif stragery=='weight':
        items.sort(key=sort_by_weight)
    elif stragery=='ratio':
        items.sort(key=sort_by_ratio,reverse=True)
    total_value=0.0
    result_items=[]
    for value,weight in items:
        if W==0:
            break
        if weight<=W:
            total_value+=value
            W-=weight
            result_items.append((value,weight,1.0))
        else:
            fraction=W/weight
            total_value+=value*fraction
            result_items.append((value,weight,fraction))
            W=0
    print(f"\nStragery: {stragery.upper()}")
    print(f"\nTotal Profit: {total_value:.2f}")
    print("Items taken (value,weight,fraction):")
    for v,w,f in result_items:
        print(f"Value: {v}, Weight: {w},Fraction: {f:.2f}")
    return total_value
#(profit,weight) for objects 1-7
items=[(5,1),(10,3),(15,3),(7,4),(8,1),(9,3),(4,2)]
W=15
print("Greedy by Max value:",fractional_knapsack(W,items.copy(),'value'))
print("Greedy by Min weight:",fractional_knapsack(W,items.copy(),'weight'))
print("Greedy by Profit/Weight:",fractional_knapsack(W,items.copy(),'ratio'))


