
def test(Letter):
    global updatedWord
    global Letter
    global Secret
    if Letter in Secret:
        updatedWord.append(Letter)
        ifwon()