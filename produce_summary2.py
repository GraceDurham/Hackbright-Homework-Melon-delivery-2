choice = raw_input("Please choose a day, day 1, day 2, and day 3")

def choose(day):
    
    if day == "1":
        the_file = open("um-deliveries-20140519.txt")
        print the_file

    elif day == "2":
        the_file = open("um-deliveries-20140520.txt")

    elif day == "3":
        the_file = open("um-deliveries-20140521.txt")

    else:
        print "That is not a valid input. Please choose day 1, day 2, or day 3."
        

            
    for line in the_file:
        print line
        line = line.rstrip()
        print line
        words = line.split('|')
        print words

        melon = words[0]
        count = words[1]
        amount = words[2]

        print "Delivered {} {}s for total of ${}".format(
            count, melon, amount)

        # the_file.close()

choose(choice)