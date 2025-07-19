filename=input("Enter name of your file with txt:")
try:
    with open(filename,'r') as file:
        content = file. read()
    content = content.lower()

    vowels="aeiou"
    voule_count=0
    constant_count=0

    digit_count=0

    for char in content:
        if char in vowels:
            voule_count+=1
        elif char.isalpha():
            constant_count +=1
        elif char.isdigit():
            digit_count +=1
    
    print (f"\nVowels:{voule_count}")
    print(f"constants:{constant_count}")
    print(f"Digits:{digit_count}")

except FileNotFoundError:
    print("File not exist")
    