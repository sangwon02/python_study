infile = open("c:\\input.txt", "r")
outfile = open("c:\\output.txt", "w")

word_dic = {}
total_count = 0

for line in infile:
    line = line.rstrip()
    word_list = line.split()

    for word in word_list:
        word = word.lower()
        word = word.rstrip(',')
        word = word.rstrip('.')

        if word in word_dic:
            word_dic[word] = word_dic[word] + 1
            total_count = total_count + 1
        else:
            word_dic[word] = 1
            total_count = total_count + 1

result = ""
for key in sorted(word_dic.keys()):
    result = key+" "+str(word_dic[key])+"\n"
    outfile.write(result)

print("총 단어 수 = ", total_count)

outfile.close()
