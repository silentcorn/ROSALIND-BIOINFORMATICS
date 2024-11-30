import csv


"""

Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. 
Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

"""




def main():
    # Initializing list of dictionaries
    database = []
    # Initializing while loop
    while True:
        # Getting user input until exception is met
        try:
            rid = input("Enter FASTA format: ")
            seq = input("enter DNA string: ")
            data = {}
            data["Rosalind ID"] = rid
            data["Sequence GC"] = calc_gc(seq)
            database.append(data)
        # exception = hitting CTRL+C
        except KeyboardInterrupt:
            # Quitting While loop
            break
    # Creating CSV file 
    with open("rosa.csv", mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=database[0].keys())
        writer.writerows(database)

    
    







# Creating function that calculates GC content as a percentage for given DNA string
def calc_gc(strand):
    counter = 0
    for nuc in strand:
        if nuc == "G" or nuc == "C":
            counter += 1
    return (counter/len(strand))*100
    ...





main()