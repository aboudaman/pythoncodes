from dequeue import Dequeue

def enterRear(rtext):
    rtest = Dequeue()
    entered_text = []
    for ch in rtext:
        rtest.addRear(ch)
    while not rtest.isEmpty():
        entered_text.append(rtest.removeRear())
    mytext = "".join(entered_text)
    return mytext

# def enterFront(ftext):
textToTest = "toot"
if enterRear(textToTest.lower()) == textToTest.lower():
    print(f"Text {textToTest} is a Palindrome")
else:
    print(f"Text {textToTest} is NOT a Palindrome")
