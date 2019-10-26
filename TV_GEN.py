from __future__ import print_function
from functools import reduce
import os
import math as m

def sublist(lst, n):
    sub=[] ; result=[]
    for i in lst:
        sub+=[i]
        if len(sub)==n: result+=[sub] ; sub=[]
    if sub: result+=[sub]
    return result

def TV_A(circuitName, seedInitial):
    lst=[]
    sum=""
    x=""
    str1=""
    netFile = open(circuitName, 'r')  #open the circuit bench and read that file

            #while True:
    outputName = "TV_A.txt"
    outputFile = open(outputName, 'w')
    outputFile.write("# TV SET A \n" + "Initial Seed: " + seedInitial + "\n\n")
    n=0

    for line in netFile:
        if line[0:5] == "INPUT":
            n = n + 1
    #loopTime = m.ceil(n / 8)
    i=0
    k=n-8
    while k!=0:
        lst.append('0')
        k=k-1


    str1 = str1.join(lst)


    reversedSeedInitial = ''.join(reversed(seedInitial))
    joined= str1+seedInitial

    outputFile.write(joined+"\n")

    num1 = '00001'
    # decimal value 17
    num2 = '10001'

    # sum - decimal value 18
    # binary value 10010
    i=0
    while i<255:
        num1= seedInitial
        num2='0001'
        sum = bin(int(num1, 2) + int(num2, 2))
        sum=sum.replace('0b', '')
       # if len(sum)==9:
            #x=str1[1:]
        x=str1+sum
        if len(x)>n:
            x =x[1:]
            x=x.replace('1', '0')
        outputFile.write(x+"\n")
        seedInitial=sum
        x=""
        i=i+1

            #print("\n Write output file: use " + outputName + "?" + " Enter to accept or type filename: ")
                #userInput = input()
                #if userInput == "":
                 #   break
                #else:
                 #   outputName = os.path.join(script_dir, userInput)
                 #   break

def TV_B(circuitName, seedInitial):
    lst = []
    gnd=[]
    sum = ""
    x = ""
    str1 = ""
    nxt=""
    netFile = open(circuitName, 'r')  # open the circuit bench and read that file

    # while True:
    outputName = "TV_B.txt"
    outputFile = open(outputName, 'w')
    outputFile.write("# TV SET B \n" + "Initial Seed: " + seedInitial + "\n\n")
    n = 0

    for line in netFile:
        if line[0:5] == "INPUT":
            n = n + 1
    # loopTime = m.ceil(n / 8)


    #str1 = str1.join(lst)



    #joined = str1 + seedInitial
    i=0
    loopTime = m.ceil(n / 8)
    while i<loopTime:
        lst.append(seedInitial)
        i=i+1
    str1 = str1.join(lst)
    str1=str1[loopTime-n:n]
    str1= ''.join(reversed(str1))


    outputFile.write(str1+"\n")

    # sum - decimal value 18
    # binary value 10010
    i = 0
    while i < 255:
        g=0
        while g<loopTime:
            num1 = str1
            num2 = '0001'
            sum = bin(int(num1, 2) + int(num2, 2))
            sum = sum.replace('0b', '')
            gnd.append(sum)
            seedInitial=sum
            g=g+1
        nxt= nxt.join(gnd)
        outputFile.write(nxt+"\n")
        nxt=""
        gnd.clear()
        #seedInitial=sum
        # if len(sum)==9:
        # x=str1[1:]
        #x = str1 + sum
        #if len(x) > n:
          #  x = x[1:]
        #outputFile.write(x + "\n")
        #seedInitial = sum
        x = ""
        i = i + 1





def TV_C(circuitName, seedInitial):
    netFile = open(circuitName, 'r')  #open the circuit bench and read that file

            #while True:
    outputName = "TV_C.txt"
                #print("\n Write output file: use " + outputName + "?" + " Enter to accept or type filename: ")
                #userInput = input()
                #if userInput == "":
                 #   break
                #else:
                 #   outputName = os.path.join(script_dir, userInput)
                 #   break

    outputFile = open(outputName, 'w')
    outputFile.write("# TV SET C \n" + seedInitial+"\n\n")

def TV_D(circuitName, seedInitial):
    netFile = open(circuitName, 'r')  #open the circuit bench and read that file

            #while True:
    outputName = "TV_D.txt"
                #print("\n Write output file: use " + outputName + "?" + " Enter to accept or type filename: ")
                #userInput = input()
                #if userInput == "":
                 #   break
                #else:
                 #   outputName = os.path.join(script_dir, userInput)
                 #   break

    outputFile = open(outputName, 'w')
    outputFile.write("# TV SET D \n" + seedInitial+"\n\n")

def TV_E(circuitName, seedInitial):
    netFile = open(circuitName, 'r')  # open the circuit bench and read that file
    outputName= "TV_E.txt"
    outputFile = open(outputName, 'w')
    outputFile.write("# TV SET E \n" + "Initial Seed: " + seedInitial + "\n\n")
    n=0
    j=1

    for line in netFile:
        if line[0:5]=="INPUT":
            n=n+1
    print("N Size from circuit: " + str(n))
    loopTime= m.ceil(n/8)
    print (str(loopTime))
        # while True:
    #outputName = "TV_E.txt"
        # print("\n Write output file: use " + outputName + "?" + " Enter to accept or type filename: ")
        # userInput = input()
        # if userInput == "":
        #   break
        # else:
        #   outputName = os.path.join(script_dir, userInput)
        #   break
    reversedSeedInitial = ''.join(reversed(seedInitial))
    lst=[]
    outputList=[]
    tvSet=[]
    tv2Set=[]
    tvSet.insert(0, reversedSeedInitial)
    str1 = ""
    p=""
    i=1

    while i != loopTime:
        for bit in reversedSeedInitial:
            lst.append(bit)

        print("Reversed:" + str(lst))


        Shiftedlst = [lst[-1]] + lst[:-1]

        print("Shifted: " + str(Shiftedlst))
        #for bit in lst:
        #for i in Shiftedlst:

        if lst[len(seedInitial)-1]=='0' and Shiftedlst[2]=='0':
            Shiftedlst[2]='0'

        elif lst[len(seedInitial)-1]=='1' and Shiftedlst[2]=='0':
            Shiftedlst[2]='1'

        elif lst[len(seedInitial)-1] == '0' and Shiftedlst[2] == '1':
            Shiftedlst[2]='1'

        elif lst[len(seedInitial)-1] == '1' and Shiftedlst[2] == '1':
            Shiftedlst[2]='0'


        if lst[len(seedInitial)-1]=='0' and Shiftedlst[3]=='0':
            Shiftedlst[3]='0'

        elif lst[len(seedInitial)-1]=='1' and Shiftedlst[3]=='0':
            Shiftedlst[3]='1'

        elif lst[len(seedInitial)-1] == '0' and Shiftedlst[3] == '1':
            Shiftedlst[3]='1'

        elif lst[len(seedInitial)-1] == '1' and Shiftedlst[3] == '1':
            Shiftedlst[3]='0'


        if lst[len(seedInitial)-1] == '0' and Shiftedlst[4] == '0':
            Shiftedlst[4]='0'
        elif lst[len(seedInitial)-1] == '1' and Shiftedlst[4] == '0':
            Shiftedlst[4]='1'

        elif lst[len(seedInitial)-1] == '0' and Shiftedlst[4] == '1':
            Shiftedlst[4]='1'

        elif lst[len(seedInitial)-1] == '1' and Shiftedlst[4] == '1':
            Shiftedlst[4] = '0'
        str1= str1.join(Shiftedlst)
        tvSet.insert(i, str1)
        reversedSeedInitial=str1
        lst.clear()
        Shiftedlst.clear()
        str1=""

        i = i+1
    p = p.join(tvSet)
    #p=p[0:n]
    reversedP = ''.join(reversed(p))
    outputFile.write(reversedP+"\n")
    b=len(p)-1
    while j != 255:
        for bit in p:
            lst.append(bit)
        Shiftedlst = [lst[-1]] + lst[:-1]
       # print(Shiftedlst)
        y= sublist(lst,8)
        x = sublist(Shiftedlst, 8)

        k=0

        while k<=len(y)-1 and k<=len(x)-1:
            if y[k][7] == '0' and x[k][2] == '0':
                x[k][2] = '0'

            elif y[k][7] == '1' and x[k][2] == '0':
                x[k][2] = '1'

            elif y[k][7] == '0' and x[k][2] == '1':
                x[k][2] = '1'

            elif y[k][7] == '1' and x[k][2] == '1':
                x[k][2] = '0'

            if y[k][7] == '0' and x[k][3] == '0':
                x[k][3]='0'

            elif y[k][7]== '1' and x[k][3] == '0':
                x[k][3]= '1'

            elif y[k][7] == '0' and x[k][3] == '1':
                x[k][3]= '1'

            elif y[k][7] == '1' and x[k][3] == '1':
                x[k][3]='0'

            if y[k][7]== '0' and x[k][4] == '0':
                x[k][4]='0'
            elif y[k][7] == '1' and x[k][4] == '0':
                x[k][4]='1'

            elif y[k][7] == '0' and x[k][4] == '1':
                x[k][4]='1'

            elif y[k][7] == '1' and x[k][4] == '1':
               x[k][4] = '0'
            k=k+1
        l=reduce(lambda f, g: f + g, x)
        str1 = str1.join(l)
        print(str1)
        toGo=''.join(reversed(str1))
        outputFile.write(toGo+"\n")
        p=str1
        str1=""
        lst.clear()
        Shiftedlst.clear()
        j=j+1


    print("Normal: " + p)

    print("REverse: " + reversedP)
   # print(reversedSeedInitial)
    print("AFTER OR:" + str(Shiftedlst))
    print("TEST VECTOR SET: " + str(tvSet))






def main():
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in

    while True:
        cktFile = "circuit.bench"
        print("\n Read circuit benchmark file: use " + cktFile + "?" + " Enter to accept or type filename: ")
        userInput = input()
        if userInput == "":
            break
        else:
            cktFile = os.path.join(script_dir, userInput)
            if not os.path.isfile(cktFile):
                print("File does not exist. \n")
            else:
                break

    print("Please enter the initial seed for " + cktFile + ": ")

    while True:

        userSeed= input()

        if userSeed == "":
            print("Please enter the initial seed for " + cktFile + " (8 bits): ")

        #elif len(userSeed)!=8:
            #print("Please enter the initial seed for " + cktFile + " (8 bits): ")



        else:
            seedInitial=userSeed
            print("Initial Seed: "+seedInitial)
            break




    #TV_A(cktFile, seedInitial)
    TV_B(cktFile, seedInitial)
    #TV_C(cktFile, seedInitial)
    #TV_D(cktFile, seedInitial)
    #TV_E(cktFile, seedInitial)

if __name__ == "__main__":
    main()