import diff

def diff_wordMode(text1, text2):
    dmp = diff.diff_match_patch()
    a = dmp.diff_linesToWords(text1, text2)
    lineText1 = a[0]
    lineText2 = a[1]
    lineArray = a[2]

    diffs = dmp.diff_main(lineText1, lineText2)
    dmp.diff_charsToLines(diffs, lineArray)
    dmp.diff_cleanupSemantic(diffs)
    return (diffs)


file1 = open("ch46_fragment.txt")
file2 = open("chRU_fragment.txt")
text1 = file1.read()
text2 = file2.read()

#text1 = "This is an example\nAnd the second line"
#text2 = "This is a bad example\nAnd the second line"
#text1 = '\n'.join(text1.split())
#text2 = '\n'.join(text2.split())

a = diff_wordMode(text1, text2)

print a
