#python2
m = int(raw_input())
coins = 0

if m/10:
    coins += m/10
    m= m%10
if m/5:
    coins+= m/5
    m= m%5
if m/1:
    coins+=m

print coins
