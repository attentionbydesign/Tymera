import chimera
from chimera import openModels

mid=4
def mol_select(mid):
    mol_objs = chimera.openModels.list()
    #for mobj in mol_objs:
        #print "#"+str(mobj.id), mobj.name
    #mid = input("Model ID#: ")
    for mobj in mol_objs:
        if mobj.id == mid:
            mobj_sel = mobj
    return mobj_sel

def chain_select():
    m = mol_select(mid)
    chain_objs = m.sequences()
    for cobj in chain_objs:
        print cobj.chainID, len(cobj)
    cid = raw_input("Chain ID: ")
    for cobj in chain_objs:
        if cobj.chainID == cid:
            cobj_sel = cobj
    return cobj_sel

def getSeq():
    c = chain_select()
    cseq = str(c)
    return cseq

##chain_key = {}
##while True:
##    seq = getSeq()
##    prot = raw_input("Protein Name: ")
##    chain_key[prot]=seq
##    print chain_key

def r2d(filename):
    result_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) == 2:
                key = columns[0]
                value = columns[1]
                result_dict[key] = value
    return result_dict
    file.close()

chain_key = {}
def getRefSeq():
    chain_key = r2d('cky.txt')
    key = raw_input('Protein name: ')
    return chain_key[key]

### Print the resulting dictionary
##for key, value in chain_key.items():
##    print("Key: {}, Value: {}".format(key, value))

def align_sequences(short_seq, long_seq):
    max_similarity = 0
    best_alignment = ("", "")

    short_len = len(short_seq)
    long_len = len(long_seq)

    for i in range(long_len - short_len + 1):
        substring = long_seq[i:i + short_len]
        similarity = sum(1 for a, b in zip(short_seq, substring) if a == b)
        if similarity > max_similarity:
            max_similarity = similarity
            best_alignment = (short_seq, substring)

    return best_alignment

def calculate_similarity(seq1, seq2):
    matches = sum(1 for a, b in zip(seq1, seq2) if a == b)
    similarity = float(matches) / len(seq1) * 100
    return similarity

while True:
    # Example sequences
    s1 = getSeq()
    s2 = getRefSeq()
    
    if len(s1) > len(s2):
        short_sequence = s2
        long_sequence = s1
    else:
        short_sequence = s1
        long_sequence = s2      

    aligned_seq1, aligned_seq2 = align_sequences(short_sequence, long_sequence)
    similarity = calculate_similarity(aligned_seq1, aligned_seq2)

##    print("Short sequence:", short_sequence)
##    print("Long sequence: ", long_sequence)
##    print("Aligned sequences:")
##    print("Aligned short sequence:", aligned_seq1)
##    print("Aligned long sequence: ", aligned_seq2)
    print("Similarity: {:.2f}%".format(similarity))

