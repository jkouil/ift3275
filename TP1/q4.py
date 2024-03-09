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

    code = ""


    for line in tab1:
        code = code + line

    newCode = code.splitlines()
    code = ""
    for line in newCode:
        code = code + line

    motie = len(code) // 2
    c1 = code[0:motie]
    c2 = code[motie:len(code)]

    comb = ""

    for i in range(len(c1)):
        char1 = c1[i]
        char2 = c2[i]
        comb = comb + str(int(char1) ^ int(char2))
        print(comb)


    return comb

def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
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