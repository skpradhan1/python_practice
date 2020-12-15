def calculate_bitwise_complement(num):
    bit_count, n = 0, num
    while n >0:
        bit_count +=1
        n = n >> 1
    all_bit_set = pow(2, bit_count) -1

    return num^all_bit_set

def main():
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

main()