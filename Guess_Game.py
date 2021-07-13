import random
import time
import csv
import Welcome_File

run = '1'
while run.isalnum():
    name = ''
    while name == '':
        name = input("Enter your name:")
        if name == '':
            print("Please Enter your name.\n")
    if name.lower() == 'white_worm':
        print("Boss you are always no. one")
        break
    computer_guess = random.randint(1, 1000)
    user_guess = None
    gusses = 0
    score = []
    print("\nGuess a number between 1 and 1000::\n")
    start_time = time.time()
    valid = False
    # Main Game
    while user_guess != computer_guess:
        try:
            user_guess = int(input("Enter a number ::"))
        except:
            print("Wrong Input please try again")
            valid = True
            break
        gusses += 1
        if user_guess == computer_guess:
            print("\nYou guessed it right!!")
        else:
            if user_guess > computer_guess:
                print("You guessed it wrong!! Guess a smaller number")
            else:
                print("You guessed it wrong!! Guess a larger number")

    if valid:
        print("\n-----------------------------------------------------------------------------")
        print("If you want to EXIT press ENTER ")
        print("or")
        print("else press any NUMBER OR ALPHABET")
        run = input()
        print("-----------------------------------------------------------------------------\n")
    else:
        print("You guessed it right in {} guesses".format(gusses))
        total_time = time.time() - start_time
        print("You took %s seconds" % total_time)

        # fill score list
        with open('Score.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            i = 1
            for row in reader:
                if i % 2 != 0:
                    score.append(row)
                i += 1
            if len(score) == 0:
                high = []
                for i in range(3):
                    high.append('')
                    high.append(1000)
                    high.append(100000.0)
                with open('high.txt', 'w') as f2:
                    f2.write(str(high))


        # Entry of name score and time taken in score.csv
        with open('Score.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([name, gusses, total_time])
            score.append([str(name), str(gusses), str(total_time)])

        # Opening of highest record file
        with open("high.txt", "r") as f:
            high = eval(f.read())

        if high[1] > gusses or (high[1] == gusses and high[2] > total_time):
            if high[0] != '':
                print("You just broke the first highest score made by ", high[0])
        elif high[4] > gusses or (high[4] == gusses and high[5] > total_time):
            if high[3] != '':
                print("You just broke the second highest score made by ", high[3])
        elif high[7] > gusses or (high[7] == gusses and high[8] > total_time):
            if high[6] != '':
                print("You just broke the third highest score made by ", high[6])
        else:
            if high[1] != '':
                print("\nBetter Luck Next Time")

        # Work completed on top 3 score


        # All time score output
        def Score_Card():
            l = []
            for i in range(0, len(score)):
                l.append(int(score[i][1]))

            # Sorting by guesses
            for i in range(0, len(l) - 1, 1):
                k = i
                for j in range((i + 1), len(l), 1):
                    if l[j] < l[k]:
                        k = j
                s = l[k]
                p = score[k]
                l[k] = l[i]
                score[k] = score[i]
                l[i] = s
                score[i] = p

            l = []
            t = []
            for i in range(0, len(score)):
                l.append(int(score[i][1]))
                t.append(float(score[i][2]))

            # Sorting by Time
            for k in range(0, len(l) - 1):
                if l.index(l[k]) != (len(l) - 1 - l[::-1].index(l[k])):
                    for i in range(l.index(l[k]), (len(l) - 1 - l[::-1].index(l[k]))):
                        key = i
                        for j in range(i + 1, len(l) - l[::-1].index(l[k])):
                            if t[j] < t[key]:
                                key = j
                        s = t[key]
                        p = score[key]
                        t[key] = t[i]
                        score[key] = score[i]
                        t[i] = s
                        score[i] = p

            # Operation on highest rank file
            with open("high.txt","w") as f:
                high = []
                if len(score) >= 3:
                    for i in range(3):
                        high.append(score[i][0])
                        high.append(int(score[i][1]))
                        high.append(float(score[i][2]))
                elif len(score) == 2:
                    high = []
                    for i in range(2):
                        high.append(score[i][0])
                        high.append(int(score[i][1]))
                        high.append(float(score[i][2]))
                    high.append('')
                    high.append(1000)
                    high.append(1000.0)
                elif len(score) == 1:
                    high = []
                    high.append(score[0][0])
                    high.append(int(score[0][1]))
                    high.append(float(score[0][2]))
                    for i in range(2):
                        high.append('')
                        high.append(1000)
                        high.append(1000.0)

                f.write(str(high))

        # Used to display score board
        def Display():
            print('%5s'%('S.No.'), '%10s'%("NAME"), '\t%5s'%('SCORE'), '\t%13s'%('TIME TAKEN'))
            for i in range(0, len(score)):
                print('%5d'%(i+1),'%10s'%score[i][0],'\t%5d'%int(score[i][1]),'\t{0:.10f}'.format(float(score[i][2])))

        Score_Card()
        print("\nCurrent Rankings ::\n")
        print('%4s'%('RANK'), '%10s'%("NAME"), '\t%5s'%('SCORE'), '\t%13s'%('TIME TAKEN'))
        if len(score) >= 3:
            n = 3
        else:
            n = len(score)
        for i in range(n):
            if score[i][0] != '':
                print('%4d'%(i+1),'%10s'%score[i][0],'\t%5d'%int(score[i][1]),'\t{0:.10f}'.format(float(score[i][2])))

        for i in range(len(score)):
            if score[i][0] == name and int(score[i][1]) == gusses and float(score[i][2]) == float(total_time) :
                print("\nYour Current Rank :: ", i+1)
                break

        if input("\nIf you want to see all score please enter 'S' else press ENTER :: ").lower() == 's':
            Display()
        print("\n-----------------------------------------------------------------------------")
        print("If you want to EXIT press ENTER ")
        print("or")
        print("else press any NUMBER OR ALPHABET")
        run = input()
        print("-----------------------------------------------------------------------------\n")
else:
    print("Thank You for playing the game...")
    print("Come Again soon I will be waiting for you")
