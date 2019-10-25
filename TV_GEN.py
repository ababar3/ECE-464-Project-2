from __future__ import print_function
import os
import math as m
def TV_A(circuitName, seedInitial):
    netFile = open(circuitName, 'r')  #open the circuit bench and read that file

            #while True:
    outputName = "TV_A.txt"

                #print("\n Write output file: use " + outputName + "?" + " Enter to accept or type filename: ")
                #userInput = input()
                #if userInput == "":
                 #   break
                #else:
                 #   outputName = os.path.join(script_dir, userInput)
                 #   break

    outputFile = open(outputName, 'w')
    outputFile.write("# TV SET A \n" + "Initial Seed: " + seedInitial+"\n\n")


def TV_B(circuitName, seedInitial):
    netFile = open(circuitName, 'r')  #open the circuit bench and read that file

            #while True:
    outputName = "TV_B.txt"
                #print("\n Write output file: use " + outputName + "?" + " Enter to accept or type filename: ")
                #userInput = input()
                #if userInput == "":
                 #   break
                #else:
                 #   outputName = os.path.join(script_dir, userInput)
                 #   break

    outputFile = open(outputName, 'w')
    outputFile.write("# TV SET B \n"+ seedInitial+"\n\n")



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

    while i!= loopTime:
        for bit in reversedSeedInitial:
            lst.append(bit)

        print("Reversed:" + str(lst))


        Shiftedlst = [lst[-1]] + lst[:-1]
        print("Shifted: " + str(Shiftedlst))
        #for bit in lst:
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
    p=p[0:n]
    reversedP = ''.join(reversed(p))
    outputFile.write(reversedP+"\n")
    b=len(p)-1
    while j != 255:
        for bit in p:
            lst.append(bit)
        Shiftedlst = [lst[-1]] + lst[:-1]
        if lst[b] == '0' and Shiftedlst[2] == '0':
            Shiftedlst[2] = '0'

        elif lst[b] == '1' and Shiftedlst[2] == '0':
            Shiftedlst[2] = '1'

        elif lst[b] == '0' and Shiftedlst[2] == '1':
            Shiftedlst[2] = '1'

        elif lst[b] == '1' and Shiftedlst[2] == '1':
            Shiftedlst[2] = '0'

        if lst[b] == '0' and Shiftedlst[3] == '0':
            Shiftedlst[3] = '0'

        elif lst[b] == '1' and Shiftedlst[3] == '0':
            Shiftedlst[3] = '1'

        elif lst[b] == '0' and Shiftedlst[3] == '1':
            Shiftedlst[3] = '1'

        elif lst[b] == '1' and Shiftedlst[3] == '1':
            Shiftedlst[3] = '0'

        if lst[b] == '0' and Shiftedlst[4] == '0':
            Shiftedlst[4] = '0'
        elif lst[b] == '1' and Shiftedlst[4] == '0':
            Shiftedlst[4] = '1'

        elif lst[b] == '0' and Shiftedlst[4] == '1':
            Shiftedlst[4] = '1'

        elif lst[b] == '1' and Shiftedlst[4] == '1':
            Shiftedlst[4] = '0'
        str1 = str1.join(Shiftedlst)
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




    TV_A(cktFile, seedInitial)
    TV_B(cktFile, seedInitial)
    TV_C(cktFile, seedInitial)
    TV_D(cktFile, seedInitial)
    TV_E(cktFile, seedInitial)

if __name__ == "__main__":
    main()
