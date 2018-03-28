from Bio.Seq import Seq

def palindrome_finder(seq):

    template = seq.complement()

    print('template '+str(template))

    dict = {}

    l = len(seq)

    for p in range(4,13):


        for i in range(len(seq)-p+1):

            templateT = template[i:i+p][::-1]

            print(str(i+1) ,seq[i:i+p], templateT)

            if seq[i:i+p] == templateT:
                dict.update({i+1:p})

    return dict

def main():

    a = "CGCGCATGTTTACACTCATCGAATCTGGCAGGTCGCTTCTTCCAACCTCGGACGTGCCGTACATACAGGTCCGCACAATTCCACTACCGGTCGGGCATGAGGTGGGTTGCCAACCTACGCCACAACGCTCTCGAATTATGCGCCGTACGTATAAGATATACCATCATATGGATGTAGGGGAGCGCCTCTGGTTCTAATGTTAAAAACCACAATAAGTAGACATCGTAGGAGCTTCAAATCATGTGCTCTAAATATCGTCATAACCCCCTATCCGGATGGCAGTGGGGATTCGCGAATTAATCTTATCTCGGTTCGAGGCTCAGCCTGTTTGGGGCCTTGGGATGACATTAATGAGGTGCAGCAAAGTGAGTACAAGTTTATGTACTTCACTGCTACGTGGGATGTTTAATACGAGCTGCAAGATAACTTTTGCTCGATGCATATGCGACCAATTCGTCTTTTTCGCTAGTATATCCTCGGACTAATTAGTCGGTGGGCCCCCGATAAAGTGGACTGTGGTCAGTCACGAGGGGAAGTGATCGATCTCGTTGGCCCTATCGGCTGAGCGGCACCGGCAACCAAAACAGTGCAGTTGTTTCTGTACATGGGCGGGCCTCCAATCCGCGCGAAGGTTGATACGTCAACCGTCAGCTCCGAGCACTTAAGCACGTTTCCAGCAGCATGTAACAAGTCCGCTATGGTTTAACAACGAAGAATTTACCTGCGAAATTTGTGTCGGTACCCCAGAACGGTAACCCAACGGCCCCCATAACATCCGAAAATCCCTATAGGTGTACTGGAAAAAACGGTGCCAACCGTGACCATTGGATCATAGTGTAGAGAGTGACTATTAAGGGCTCGGACTATGCGATTTAACGAGCAAGGGCTCCGTAGAAGGCGCTGAGAGCAGCGCTGGATTCCCTGTTAACATCGAACACCGCCTCGTTCGCACGTGTAGGATAGCCGTATA"
    testSeq = Seq(a)

    print('conplate '+ str(a))
    res = palindrome_finder(testSeq)

    for key in res:
        print(key,res[key])

if __name__ == "__main__":
    main()
