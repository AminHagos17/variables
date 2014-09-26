#test grading program

test_score = int(input("Please enter your test score: "))
# the test score is meant to be a number so "int(" should be entered before "input("
if test_score >= 40 and testScore < 50:
    print("E grade")
elif test_score >= 50 and testScore < 60:
    print("D grade")
elif test_score >= 60 and testScore < 70:
    print("C grade")
elif test_score >= 70 and testScore <80:
    print("B grade")
elif test_score >= 80:
    print("A grade")
else:
    print("Fail")
