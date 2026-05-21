def uppercase_counter(filename):

    # Run uppercase_counter("sample.txt") to use the test data set. 

    print("Line\tChars\tUppercase\t% Upper") # Print table header.

    file = open(My_file)

    linenumber = 1

    for l in file: # Iterate over each line in the text file.

        total = len(l.strip())

        uppercase = 0 # Variable for counting the number of upper case letters.

        for c in l: # Iterate over each letter in the line. 

            if c.isupper():

                uppercase += 1

        if total != 0:

            p = uppercase / total * 100

        else:

            p = 0

        print(str(linenumber) + "\t" + str(total) + "\t" + str(uppercase) + "\t" + str(round(p, 2)) + "%")

        linenumber += 1

