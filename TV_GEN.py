from __future__ import print_function
import os

def TV_A(circuitName):
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
    outputFile.write("# TV SET A \n")


def TV_B(circuitName):
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
    outputFile.write("# TV SET B \n")



def TV_C(circuitName):
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
    outputFile.write("# TV SET C \n")

def TV_D(circuitName):
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
    outputFile.write("# TV SET D \n")

def TV_E(circuitName):
        netFile = open(circuitName, 'r')  # open the circuit bench and read that file

        # while True:
        outputName = "TV_E.txt"
        # print("\n Write output file: use " + outputName + "?" + " Enter to accept or type filename: ")
        # userInput = input()
        # if userInput == "":
        #   break
        # else:
        #   outputName = os.path.join(script_dir, userInput)
        #   break

        outputFile = open(outputName, 'w')
        outputFile.write("# TV SET E \n")


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
    TV_A(cktFile)
    TV_B(cktFile)
    TV_C(cktFile)
    TV_D(cktFile)
    TV_E(cktFile)

if __name__ == "__main__":
    main()
