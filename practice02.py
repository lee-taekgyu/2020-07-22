import sys

class FASTA:
    def __init__(self, file_name :str):
        self.file_name = file_name
        self.count = {}
        self.length = 0

    def base_count(self):
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if line.startswith('>'):
                    continue
                line = line.strip()
                for s in line:
                    if s in self.count:
                        self.count[s] += 1
                    else:
                        self.count[s] = 1

    def get_length(self):
        for k,v in self.count.items():
            self.length += v
            return self.length


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("f#usage python : {sys.argv[0]} [fasta]")
        sys.exit()

    file_name = sys.argv[1]
    t = FASTA(file_name)
    t.base_count()
    print(t.count)
    t.get_length()
    print(t.length)
