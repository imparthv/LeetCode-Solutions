# 884. Uncommon Words from Two Sentences
def uncommonFromSentences(s1, s2):
    '''
    uncommon_list = []
    stmt_1 = s1.split()
    stmt_2 = s2.split()
    full_stmt  = stmt_1 + stmt_2
    for item in full_stmt:
        if full_stmt.count(item) < 2:
            uncommon_list.append(item)
    return uncommon_list
    '''
    uncommon_list = []
    stmt_1 = s1.split()
    stmt_2 = s2.split()
    full_stmt  = stmt_1 + stmt_2
    uncommon_list = [item for item in full_stmt if full_stmt.count(item) < 2]
    return uncommon_list


print("Enter inputs:")
sentence_1 = input()
sentence_2 = input()
uncommon_word = uncommonFromSentences(sentence_1, sentence_2)
print(uncommon_word)