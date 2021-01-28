# Created for an assignment where we had to search through a text file finding lines
# that start with "X-DSPAM-Confidence".  There were decimals after the text that we
# had to find, add them all together, and then create an average of those decimals
# to get an average "spam confidence" number.  The mbox-short.txt is included with this
# repository.  The assignment instructions are listed below this.

#7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form: "X-DSPAM-Confidence:    0.8475" Count these lines and extract the
# floating point values from each of the lines and compute the average of those values and
# produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0.0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    fdec = line[20:26]
    fdec = float(fdec)
    tot = tot + float(fdec)
    count = count + 1
avg = tot / count
print(f"Average spam confidence:",avg)
