import sys



class FASTQ():
    def __init__(self, file_name :str):
        self.file_name = file_name
        self.base = {}
        self.read_num = 0

    def count_read_num(self):
        cnt = 0
        with open(file_name, 'r') as handle:
            for line in handle:
                if cnt % 4 ==0:
                    header = line.strip()
                if cnt % 3 == 0:
                    seq = line.strip()
                    for s in seq:
                        if s in self.base:
                            self.base[s] += 1
                        else:
                            self.base[s] = 1


if __name__ =="__main__":
    if len(sys.argv) != 2:
        print(f"#Usage : python {sys.argv[0]} [FASTQ]")
        sys.exit()

    file_name = sys.argv[1]
    f = FASTQ(file_name)
    f.count_read_num()
    print(f.base)
