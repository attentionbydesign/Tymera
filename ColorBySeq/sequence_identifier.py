import chimera

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
        
    best_substring = max(sass, key=sass.get)
    best_alignment = (short_seq, best_substring)
    
    return best_alignment

def calculate_similarity(seq1, seq2):
    matches = sum(1 for a, b in zip(seq1, seq2) if a == b)
    similarity = float(matches) / len(seq1) * 100
    return similarity

def identify_seq(cobj,calcsim=False):
    chain_key = {}
    chain_key = r2d('../ref/chain_key.txt')
    seq1 = str(cobj)
    match_rank = {}

    for sname in chain_key:
        seq2 = chain_key[sname]
        if len(seq1) > len(seq2):
            short_sequence = seq2
            long_sequence = seq1
        else:
            short_sequence = seq1
            long_sequence = seq2

        ###FLANKING SEQUENCE BUFFER###
        long_buff_length = int(float(len(short_sequence)) * 0.05) 
        for count in range(long_buff_length):
            long_sequence = 'X' + long_sequence + 'X'
        ###------------------------###

        aligned_seq1, aligned_seq2 = align_sequences(short_sequence, long_sequence)

        similarity = calculate_similarity(aligned_seq1, aligned_seq2)

        match_rank[similarity] = sname
    max_similarity = max(match_rank)
    best_match = match_rank[max_similarity]

    #print best_match, max_similarity
    if calcsim == True:
        return max_similarity
    else:
        return best_match

def identify_sel():
    seld_chains = chimera.selection.currentChains()
    for cobj in seld_chains:
        name = identify_seq(cobj)
        print cobj.name,'\t',name
