import os

class aiken:
    def __init__(self, root_dir = "."):
        self.root_dir = root_dir

        self.menu_files = ["Stop"]
        for root, folders, files in os.walk(root_dir):
            for filename in files:
                if (filename.endswith(".txt")):
                    self.menu_files.append(filename)
    
    def menu(self):
        for index, file in enumerate(self.menu_files):
            print("{} - {}".format(index+1, file))

        choice = 0

        while(choice == 0 or choice > len(self.menu_files)):
            try:
                choice = int(input("\nVotre choix ({} à {}) ? => ".format(1, len(self.menu_files))))
            except:
                continue

        if choice>1:
            file = self.menu_files[choice-1]
        else:
            file = False
        
        return file

    def analyze(self, file):
        with open(file, 'r') as fp:
            line_nb = 0
            count_A = 0
            count_B = 0
            count_C = 0
            count_D = 0
            count_E = 0
            for line in fp:
                line = line.strip("\n ")
                if line != "" and not "A." in line and not "B." in line and not "C." in line and not "D." in line and not "E." in line:
                    if "ANSWER:" in line:
                        print(" ({})".format(line[8:]))
                        if line.endswith("A"):
                            count_A += 1
                        elif line.endswith("B"):
                            count_B += 1
                        elif line.endswith("C"):
                            count_C += 1
                        elif line.endswith("D"):
                            count_D += 1
                        elif line.endswith("E"):
                            count_E += 1
                    else:
                        line_nb += 1
                        print("▪️ {}".format(line), end='')

        print("Il y a {}  questions et \n {} réponses A\n {} réponses B\n {} réponses C\n {} réponses D\n {} réponses E".format(line_nb, count_A, count_B, count_C, count_D, count_E))
        print("Controle : {}".format(count_A+count_B+count_C+count_D+count_E))

if __name__ == '__main__':

    print("\n\nAnalyse fichier QCM AIKEN pour Moodle\n")

    my_aiken = aiken()

    file = True

    while file:
        file = my_aiken.menu()

        if file:
            my_aiken.analyze(file)