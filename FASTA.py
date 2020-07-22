import sys

class FASTA():
    def __init__(self ,file_name :str):
        self.file_name = file_name
        self.count = {}
        self.length = 0

    def base(self):
        with open(file_name, 'r') as handle:
            for line in handle:
                if line.startswith('>'):
                    continue
                line = line.strip()
                for s in line:
                    if s in self.count:
                        self.count[s] += 1
                    else:
                        self.count[s] = 1

    def __len__(self):
        for k,v in self.count.items():
            self.length  += v
        return self.count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#usage : python {sys.argv[0]} [fasta]")
        sys.exit()

    file_name = sys.argv[1]
    f = FASTA(file_name)
    f.base()
    print(f.count)
    f.__len__()
    print(f.length)

    
