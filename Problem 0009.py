#finding Pythagorean triplets 

def pythagorean_triplets(x):
    main_list = []
    product_list = []
    dictionary = {}
    for a in range(1 , x+1):
        for b in range(a + 1 , x+1-a):
                c = x-a-b
                if b < c and (a**2) + (b**2) == (c**2):
                      main_list.append((a,b,c))
                      product_list.append(a*c*b)

    for triplet,product in zip(main_list, product_list):
        dictionary[triplet] = product

    return dictionary
    
                 
print(pythagorean_triplets(1000))
