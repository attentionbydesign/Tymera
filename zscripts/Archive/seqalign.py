from chimera import openModels, runCommand as rc
from chimera.colorTable import getColorByName

def mol_select():
    mol_objs = chimera.openModels.list()
    for mobj in mol_objs:
        print "#"+str(mobj.id), mobj.name
    mid = input("Model ID#: ")
    for mobj in mol_objs:
        if mobj.id == mid:
            mobj_sel = mobj
    return mobj_sel

def chain_select():
    m = mol_select()
    chain_objs = m.sequences()
    for cobj in chain_objs:
        print cobj.chainID, len(cobj)
    cid = raw_input("Chain ID: ")
    for cobj in chain_objs:
        if cobj.chainID == cid:
            cobj_sel = cobj
    return cobj_sel

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
    
def align_sequences(short_seq, long_seq):
    max_similarity = 0
    best_alignment = ("", "")

    short_len = len(short_seq)
    long_len = len(long_seq)

    sass={}
    for i in range(long_len - short_len + 1):
        substring = long_seq[i:i + short_len]
        similarity = sum(1 for a, b in zip(short_seq, substring) if a == b)
        sass[substring] = similarity
        print similarity
    best_substring = max(sass, key=sass.get)
    best_alignment = (short_seq, best_substring)
    return best_alignment

def calculate_similarity(seq1, seq2):
    matches = sum(1 for a, b in zip(seq1, seq2) if a == b)
    similarity = float(matches) / len(seq1) * 100
    return similarity

chain_key = {}
chain_key = r2d('cky.txt')

selcobj = chain_select()

s1 = str(selcobj)
s2 = chain_key[raw_input("Reference: ")]

if len(s1) > len(s2):
    short_sequence = s2
    long_sequence = s1
else:
    short_sequence = s1
    long_sequence = s2

aligned_seq1, aligned_seq2 = align_sequences(short_sequence, long_sequence)
similarity = calculate_similarity(aligned_seq1, aligned_seq2)

print("Short sequence:", short_sequence)
print("Long sequence: ", long_sequence)
print("Aligned sequences:")
print("Aligned short sequence:", aligned_seq1)
print("Aligned long sequence: ", aligned_seq2)
print("Similarity: {:.2f}%".format(similarity))
