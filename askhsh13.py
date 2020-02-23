def numSum(myString):
    length = len(myString)
    oddSum = 0
    evenSum = 0



    if (length==0):
        return 0
    else:
        if (length%2==0):
            last = int(myString[-1])
            evenSum += last

            return evenSum + numSum(myString[:-1])

        else:
            last = int(myString[-1])
            last = 2 * last
            part_sum = last // 10 + last % 10
            oddSum += part_sum

            return oddSum + numSum(myString[:-1])


def luhns():
    myString = input('Enter 16 digit card number: ')

    total = numSum(myString)

    if (total % 10 ==0):
        print('valid card')
    else:
        print('invalid card')



def main():
    luhns()

main()    
    
        
            
    
