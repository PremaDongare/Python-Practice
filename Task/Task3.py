#Prime Number



start=int(input("Enter the starting number"))
end = int(input("enter the end number"))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

prime_list=[]
for num in range(start, end+1):
    if is_prime(num):
        prime_list.append(num)

print(prime_list)