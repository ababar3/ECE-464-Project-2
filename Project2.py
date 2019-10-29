import P1_1
import P1_2

def main():
    userInput = ""
    while userInput != "0":
        print("Choose what you’d like to do (1, 2, or 3)\n"
              "1: Test Vector Generation\n"
              "2: Fault Coverage Simulation\n"
              "3: (extra credit) Avg Fault Coverage data generation\n"
              "0: Exit\n")
        userInput = input()
        if(userInput == "1"):
            P1_1.part1()
        if(userInput == "2"):
            P1_2.part2()



if __name__ == "__main__":
    main()