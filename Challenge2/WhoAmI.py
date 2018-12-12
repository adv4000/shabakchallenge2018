# =============================================================
# Shabak Challenge 2018 in Software and Data Science
# Solution for Part-2
# By ADV-IT
import json
import statistics
import base64


#=========Fix JSON======================
old_json = open("WhoAmI.jpg",       mode='r', encoding="UTF-8")
new_json = open("WhoAmI-fixed.json", mode="w", encoding="UTF-8")

for line in old_json:
    newline = line.replace('"value": ?','"value": "?"')
    new_json.write(newline)
old_json.close()
new_json.close()

#=======Read JSON and Calculate GEMATRIA Values

HebrewGematria = {
            'u05D0':    1,
            'u05D1':	2,
            'u05D2':	3,
            'u05D3':	4,
            'u05D4':	5,
            'u05D5':	6,
            'u05D6':	7,
            'u05D7':	8,
            'u05D8':	9,
            'u05D9':	10,
            'u05DB':	20,
            'u05DC':	30,
            'u05DE':	40,
            'u05E0':	50,
            'u05E1':	60,
            'u05E2':	70,
            'u05E4':	80,
            'u05E6':	90,
            'u05E7':	100,
            'u05E8':	200,
            'u05E9':	300,
            'u05EA':	400
}

myfile = open("WhoAmI-fixed.json", mode='r', encoding='latin_1')
jsondata = json.load(myfile)      # Load Whole File as JSON

list_of_values = [] # Will store here all values we found

for key in jsondata.keys():       # Start moving key one by one
    print(key)                    # Print key
    for line_of_text in jsondata[key]:    # Read line of text one by one, line of our key
        print(line_of_text)               # Print whole line
        print("Value  = " + str(line_of_text['value']))     # Print Value which is SET by guys from Shabak

        # Lets start counting our Gematria Value :)
        mystring = str(line_of_text)   # Convent json to string
        total = 0                      # Sum of Gematria for this key
        for hebrew_unicode in HebrewGematria.keys():                # Check every unicode in the string
            howmanyfound = mystring.count(hebrew_unicode.lower())   # Count number of appearance
            total = total + (howmanyfound * HebrewGematria[hebrew_unicode])  # Summorize
        print("Counted: " + str(total))
        list_of_values.append(total)

  #  wait = input("PRESS ENTER TO CONTINUE.")


#=======Calculate MEIDAN and Get our Secret Word

print(list_of_values)    # Print list of Found Values

MEDIAN = statistics.median(list_of_values)  # Calculate MEDIAN value
print("Median is: " + str(MEDIAN))

sum_of_values_below_median = 0    # Our final answer
for i in list_of_values:
    if i < MEDIAN:
        sum_of_values_below_median = sum_of_values_below_median + i    # Final Sum of values below 'median'

print("\n\nFinal Sum is: " + str(sum_of_values_below_median))
print("Secret in Base64: ", end='')
secret_password = str(sum_of_values_below_median)
print(base64.b64encode(secret_password.encode()))
