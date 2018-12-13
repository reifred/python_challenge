"""
    I did this work in python 2.7 due to my PC failing to install python 3.6 and above
    Facilitator Brian has been helping in fixing this issue though not a success yet.
    So functions like "raw_input" may fail on running this work in python 3 but am going to fix the issue
    soon by upgrading to windows 10.
"""

"""Question Zero"""
def grading_system():
    marks = [23,4,5,6,64,90,67,98,45,23,67,78,89]
    list1,list2 = [],[]
    for num in marks:
        if num > 50:
            list1.append(num)
        else:
            list2.append(num)
            
        if num in range(90,101):
            print("{}  ---> Excellent".format(num))
        elif num in range(70,90):
            print("{}  ---> very good".format(num))
        elif num in range(60,70):
            print("{}  ---> good".format(num))
        elif num in range(40,60):
            print("{}  ---> poor".format(num))
        elif num in range(20,40):
            print("{}  ---> very poor".format(num))
        elif num in range(0,20):
            print("{}  ---> repeat".format(num))
        else:
            print("{}  ---> Invalid mark".format(num))

"""Question One"""
def divisible7_not5():
    return ",".join([str(num) for num in range(200,3201) if num % 7 == 0 and num % 5 != 0])

"""Question Two"""
def convert_to_upper():
    sentences = []
    enter_next = True
    while enter_next:
        sentence = raw_input("Enter the sentence: ")
        if sentence:
            sentence = sentence.upper()
            sentences.append(sentence)
        else:
            return "\n".join(sentences)

"""Question Three"""
def binary_divisible5():
    valid_binary = []
    binary_numbers = raw_input("Enter four digit binary numbers: ").split(',')
    for num in binary_numbers:
        decimal = int(num, 2)
        if decimal%5 == 0:
            valid_binary.append(num)
    return ", ".join(valid_binary)

"""Question Four"""
def present_balance():
    balance,do_transaction = 0,True
    while do_transaction:
        user_input = raw_input("Enter a transaction(D/W) and amount: ").split()
        if user_input:
            trans_type, amount = user_input[0],user_input[1]
            try:
                if trans_type in ['D','d']:
                    balance += int(amount)
                elif trans_type in ['W','w']:
                    balance -= int(amount)
                else:
                    print("Print correct transaction type")
            except ValueError:
                print("Amount should be digits only")
        else:
            do_transaction = False
    return balance

"""Question Five"""
def printList():
    square_nums = []
    for num in range(1,21):
        square_nums.append(num**2)
    return square_nums[0:5]

"""
    I did this work in python 2.7 due to my PC failing to install python 3.6 and above
    Facilitator Brian has been helping in fixing this issue though not a success yet.
    So "raw_input" may fail on running this work in python 3 but am going to fix the issue
    soon by upgrading to windows 10.
"""

if __name__ == "__main__":
    grading_system()
    print(divisible7_not5())
    print(convert_to_upper())
    print(binary_divisible5())
    print(present_balance())
    print(printList())
