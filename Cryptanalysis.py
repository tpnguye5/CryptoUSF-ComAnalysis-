#---------Crytanalysis----------
# Goal: Write a cryptoanalytic toolkit in Python to analyze the statistical properties of files.

# Instructions:
# From the command-line, take in some text file, like a book.
# Parse through it and create a dictionary that will keep track of all the "keys" that appear.
# Sort it
# Then, print it.
# The program can print out the monogram, bigram, trigram, or any higher distribution.

#-------------------------------
import re

def main():
    message = "Suddenly I noticed that the circular westward outline of the sun " \
              "had changed; that a concavity, a bay, had appeared in the curve. I" \
              "saw this grow larger. For a minute perhaps I stared aghast at this" \
              "blackness that was creeping over the day, and then I realized that" \
              "an eclipse was beginning. Either the moon or the planet Mercury was" \
              "passing across the sun's disk. Naturally, at first I took it to be" \
              "the moon, but there is much to incline me to believe that what I" \
              "really saw was the transit of an inner planet passing very near to" \
              "the earth."

    type = str(input("Choice of analysis(Monogram, bigram, or trigram):"))

    if type == 'Monogram' or type == 'monogram':
        monogram(message)
    elif type == "Bigram" or type == "bigram":
        bigram(message)
    elif type == "Trigram" or type == "trigram":
        trigram(message)
    else:
        if type != "monogram" or type != "Monogram" or type != "bigram" or type != "Bigram" or type != "Trigram" or type != "trigram":
            print("error input")


def monogram(text):

    # file = open(inputfile)
    # text = file.read()  #turns into string
    # file.close()

    regex = re.compile('[^a-zA-Z]')
    text = regex.sub('', text).upper()  #replace

    dict= ({})
    count = 0

    for index in range(0,len(text) -1):
        char = text[index]
        if char in dict:
            #get value
            val = dict[char] + 1
            #update
            dict.update({char:val})
        else:
            dict[char] = 1

    for key, val in dict.items():
        print(key, " ", val)

def bigram(text):
    # file = open(inputFile, 'r')
    # text = file.read()  # turns into string
    # file.close()

    regex = re.compile('[^a-zA-Z]')
    text = regex.sub('', text).upper()  # replace

    dict = ({})
    count = 0

    for index in range(0, len(text) - 1):
        char = text[index] + text[index + 1]
        if char in dict:
            # get value
            val = dict[char] + 1
            # update
            dict.update({char: val})
        else:
            dict[char] = 1

    # keyList = dict.keys()
    # keyList.sort()
    # for key in keyList:
    #     print("%s: %s" % (key, dict[key]))

    for key, val in dict.items():
        print(key, " ", val)


def trigram(text):
    # file = open(filename, 'r')
    # text = file.read()  # turns into string
    # file.close()

    regex = re.compile('[^a-zA-Z]')
    text = regex.sub('', text).upper()  # replace

    dict = ({})
    count = 0

    for index in range(0, len(text) - 2):
        char = text[index] + text[index + 2]
        if char in dict:
            # get value
            val = dict[char] + 1
            # update
            dict.update({char: val})
        else:
            dict[char] = 1

    for key, val in dict.items():
        print(key, " ", val)


main()


# exit()
# exit()

# parser = argparse.ArgumentParser()
# parser.add_argument("--file","-f", type = str)
# parser.add_argument("-type", dest = "type")
#
# args = parser.parse_args()
#
# # if args.type == 'mono':
# #     print('here')
# monogram(args.file)
# elif (args.type == 'bi'):
#     bigram (args.filename)
# elif (args.type == 'tri'):
#     trigram(args.filename)




#
#     for key in wordlist:
#         key = key.upper()
#
#         if key[0] == "'" or key[0] == '"' or key[0] == "`" or key[0] == "}" or key[0] == "-" or key[0] == "(" or key[
#             0] == "*" or key[0] == ",":
#             key = key[1:]
#
#         if key != "":
#             if key[len(key) - 1] == '"' or key[len(key) - 1] == "," or key[len(key) - 1] == "-" or key[
#                         len(key) - 1] == "'" or key[len(key) - 1] == "." or key[len(key) - 1] == ":" or key[
#                         len(key) - 1] == "!" or key[len(key) - 1] == "?":
#                 key = key[:len(key) - 1]
#
#             if key != "":
#                 for i in range(len(text) - n):
#                     if text[i:i+n] in dict:
#                         count = dict[key]
#                         count = count + 1
#                         dict[key] = count
#                     else:
#                         dict[key] = 1
#                 # if key in dict:
#                 #     count = dict[key]
#                 #     count = count + 1
#                 #     dict[key] = count
#                 # else:
#                 #     dict[key] = 1
#
#
#     for i in range(len(text) - n):
#         if text[i:i + n] in dict:
#             text[i:i + n] += 1
#         else:
#             text[i: i + n] = 1
#         i+=1
#
#     for key,val in dict.items():
#         print(key, " ", val)
#
# if __name__== "__main__":
#     main(sys.argv[1:])






    # if grouping == 1:
    #     for key in text:
    #         if key != "":
    #             if key in dict:
    #                 count = dict[key]
    #                 count = count + 1
    #                 dict[key] = count
    #             else:
    #                 dict[key] = 1
    #     for item, val in dict:
    #         print(item, " ", val)
    #
    # if grouping == 2:


    # elif grouping == 2:


#By default, any boolean flag is treated as false.
#Now, we can use the information gathered from CLICK to perform our analysis

# click.echo(output)
# click.echo(analytic_type)
# text = ""
# while True:
#     # file = input.read()
#     print(input.read())
#     for ch in file:
#         text += ch
# print(text)
# if analytic_type == 'mono':
#     dist(text, 1)
# elif analytic_type == 'bi':
#     dist(input, 2)
# elif analytic_type == 'tri':
#     dist(input, 3)

 # def main(argv):
#     inputfile = ''
#     try:
#         opts, args = getopt.getopt(argv, 'hi:o:n:', ['ifile=', 'n='])
#     except getopt.GetoptError:
#         print('cryptanalysis.py -i <inputfile>')
#         sys.exit(2)
#     for opt, arg in opts:
#         if opt == '-h':
#             print('Cryptanalysis.py -i <inputfile> -n (number of characters desired to analyze')
#             sys.exit()
#         elif opt in ('-i', '--ifile'):
#             inputfile = arg
#         elif opt in ('-mono'):
#             n = arg
#             dist(inputfile, n)