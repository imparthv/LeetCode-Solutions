# 1408. String Matching in an Array
def stringMatching(words):
    substring_array = []
    copy_words = words.copy()
    for item in words:
        copy_words.remove(item)
        for items in copy_words:
            if item in items:
                substring_array.append(item)
                break
        copy_words.append(item)
    return substring_array
        
print(stringMatching(["uexk","aeuexkf","wgxih","yuexk","gxea","yuexkm","ypmfx","jjuexkmb",
                      "wqpri","aeuexkfpo","kqtnz","pkqtnza","nrbb","hmypmfx","krqs",
                      "jjuexkmbyt","zvru","ypmfxj"]))