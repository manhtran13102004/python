import csv


def ex1():
    dict = {}
    with open("text/poem.txt", "r") as f:
        chunk_size = 1
        char = f.read(chunk_size)
        text = ""
        text += char
        word = []
        max_occur = 1
        while len(char) == 1:
            char = f.read(chunk_size)
            if char == " " or char == "\n":
                if text not in dict:
                    dict[text] = 1
                else:
                    dict[text] += 1
                    if dict[text] > max_occur:
                        max_occur = dict[text]
                        while word:
                            word.pop()
                        word.append(text)
                    elif dict[text] == max_occur:
                        word.append(text)
                text = ""
            else:
                text += char
    print(f"{word} are words that appear max times({max_occur} times)")


def ex2():
    with open("text/stock.csv", "r") as fr:
        with open("text/financial_metrics.csv", "w") as fw:
            fw.write('Company Name,PE Ratio,PB Ratio\n')
            fr = csv.reader(fr)
            next(fr)
            for line in fr:
                cn = line[0]
                pr = int(line[1])
                eps = int(line[2])
                bv = int(line[3])
                pe_ratio = round(pr/eps, 2)
                pb_ratio = round(pr/bv, 2)
                fw.write(f"{cn},{
                    pe_ratio},{pb_ratio}\n")
                
ex2()
