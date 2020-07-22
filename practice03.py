import sys

class FASTQ():
    def __init__(self, file_name : str):
        self.file_name = file_name
        self.read = 0

    def count(self):
        a = []
        with open(file_name, 'r') as handle:
            for i in handle:
                i = i.split("\n")
                a.append(i)
        print(len(a)/4)
       

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("f #usage: python {sys.argv[0]} [FASTQ]")
        sys.exit()

    file_name = sys.argv[1]
    t = FASTQ(file_name)
    t.count()
 
