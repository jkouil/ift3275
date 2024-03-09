import sys


def read_problem(input1="code.txt"):
    """Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier,
    faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
    d'autres librairies.
    Functions to read/write in files. you can modify them, do some parsing,
    add a return value, but don't use other librairies"""

    # lecture du fichier/file reading
    file1 = open(input1, "r")
    tab1 = file1.readlines()
    file1.close()

    xor = ""
    for code in tab1:
        xor = code

    result = []

    for i in range(len(xor)):
        if(i % 8 == 0) and i != 0:
            result.append(xor[i-8:i])

    result2 = []
    phrase = []
    for letter in result:
        if letter == "00001010":
            result2.append(phrase)
            phrase = []
        else: phrase.append(letter)


    return result2

def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    for phrase in content:
        for letter in phrase:
            file.write(letter + " ")
        file.write(" END PHRASE")
        file.write("\n")

    file.close()


def main(args):
    """Fonction main/Main function"""
    input_file = args[0]
    output_file = args[1]

    # TODO : Compléter ici/Complete here...
    # Vous pouvez découper votre code en d'autres fonctions...
    # You may split your code in other functions...
    solution = read_problem(input_file)

    write(output_file, solution)

# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])