def print_formatted(number):
    a = bin(number)
    b = len(a)
    for i in range(1, number+1):
        dec = str(i)
        octal = str(oct(i))
        hexa = str(hex(i)).upper()
        binary = str(bin(i))
        print(dec.rjust(b-2)+(octal[2:].rjust(b-1))+(hexa[2:].rjust(b-1))+(binary[2:].rjust(b-1)))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
