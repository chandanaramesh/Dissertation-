import re

#Only grep for lines as described in variable text
#text = "1,1.555370698,google-analytics.com"

#Ignore lines with format described in variable value
#value = "1,5.000510496,"

#Read text file obtained from tshark
f = open("ubuntu.txt", "r")
for text in f:
    split = re.split(r',',text)
    decimal = bool(re.match(r'^-?\d+(\.\d+)?$', split[1]))
    alphanum = bool((re.match(r'^[a-zA-Z\d-]{,63}(\.[a-zA-Z\d-]{,63})*$', split[2])))
    if split[0] == '1' and decimal == True and alphanum == True:
        print("True {}".format(text))
