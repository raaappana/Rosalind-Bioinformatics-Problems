import os

def GCcontent(sequence):
    #get rid of new lines
    GC = sequence.count('G') + sequence.count('C')
    GCratio = GC/len(sequence)*100

    return GCratio



def main(textFile='test.txt'):

    i = -1
    seqArray = []
    seqh = ''
    seqt = ''

    with open(textFile) as f:
        for line in f:
            if line[0] == r'>':

                if seqh !='':
                    seqArray.append([seqt,GCcontent(seqh)])

                seqh=''
                i+=1
                seqt = line[1:]
            else:
                seqh = seqh+line.rstrip()

    print(seqArray)

    GCmax = ['title', 0]

    print(GCmax)


    max = 0
    best = ''

    for seq in seqArray:

        if seq[1]>max:
            max = seq[1]
            best =seq[0]

    print(best)
    print(max)
    return [max,best]



if __name__ == '__main__':
    main(textFile='rosalind_gc.txt')

