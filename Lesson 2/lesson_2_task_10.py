def bank(X, Y): 
    total = X * (1 + 0.1)**Y 
    return round(total, 2) 
 
X = 1000 
Y = 5 
total_amount = bank(X, Y) 
 
print("Сумма на вашем счету через", Y, "лет(года), составит:", total_amount, "рублей") 