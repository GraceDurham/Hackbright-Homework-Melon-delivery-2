def melon_count(day_number, path):
    
    print "Day", day_number
    the_file = open(path)

            
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

    the_file.close()

melon_count(1, "um-deliveries-20140519.txt")
melon_count(2, "um-deliveries-20140520.txt")
melon_count(3, "um-deliveries-20140521.txt")
