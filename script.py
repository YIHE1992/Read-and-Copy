import shutil
import os
import pandas as pd

index = pd.read_table("./emailData/TREC2007/full/index", header = None, delim_whitespace = True)
index = index.head(10000) // only read first 10,000 line of data
index[1] = index[1].map(lambda x: str(x)[2:]) // delete the first 2 char of data directories

def label(n):
    label = index.iloc[n][0]
    return label
def directory(n):
    directory = index.iloc[n][1]
    return directory

spam_email = []
ham_email = []

for i in range(len(index)):
    if label(i) == 'ham':
        ham_email.append("D:/Online_Learning_Variable_Features/emailData/TREC2007"+directory(i))
    if label(i) == 'spam':
        spam_email.append("D:/Online_Learning_Variable_Features/emailData/TREC2007"+directory(i))

print(spam_email[:5]) // check the appended data directories' format


destination_spam = "./emailData/TREC2007/spam_10k"
destination_ham = "./emailData/TREC2007/ham_10k"

count_spam = 1
count_ham = 1

for spam_path in spam_email:
    try:
        shutil.copy(spam_path, os.path.join(destination_spam, "spam-" + str(count_spam))) // copy in destinational folder and rename each file
        count_spam += 1
    except:
        print("No file exists: " + str(count_spam))

for ham_path in ham_email:
    try:
        shutil.copy(ham_path, os.path.join(destination_ham, "ham-" + str(count_ham)))
        count_ham += 1
    except:
        print("No file exists: " + str(count_ham))
        
