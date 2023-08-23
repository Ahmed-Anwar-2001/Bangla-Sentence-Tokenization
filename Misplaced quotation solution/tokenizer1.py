import sys
import csv

maxInt = sys.maxsize

# Increase the field size limit
while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)


tokenized_sentence = []
def sentence_tokenize(text,author,btype,bname):
    from bltk.langtools import Tokenizer
    tokenizer = Tokenizer()

    # Tokenizing Sentences
    #print("TOKENIZED SENTENCES:")

    sentences = tokenizer.sentence_tokenizer(text)

    temp = ''
    flag = False
    c = 0
    tokenized = []
    i = 0
    while i<len(sentences):
        if '"' in sentences[i] and flag==False:
            if sentences[i].count('"')%2==0:
                c+=1
                tokenized.append([author,btype,bname,sentences[i]])
            else:
                temp+=sentences[i]
                flag = True
        elif '"' in sentences[i] and flag:
            a = sentences[i].find('"')
            temp+=sentences[i][:a]+'"'
            tokenized.append([author,btype,bname,temp.strip()])
            c+=1
            temp = ""   
            flag = False
            sentences[i] = sentences[i][a+1:]
            continue
        
        else:
            if flag==True:
                temp+=sentences[i]
            else:
                c+=1
                tokenized.append([author,btype,bname,sentences[i]])
        i+=1
    #print("Total Samples",c)
    return tokenized






# Read the CSV file
csv_file_path = "C:\\Users\\HP\\Desktop\\thesis\\archive\\csv\\novel.csv"
with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        novel_name = row['name']
        genre = row['genre']
        content = row['content']

        # Tokenize sentences
        sentences = sentence_tokenize(content,'Sharat Chandra',genre,novel_name)
        tokenized_sentence+=sentences


# Write tokenized sentences to a new CSV file

#Declare the fields of the csv file
fields = ['Author', 'Genre', 'Source', 'Text']    
filename = "sharatchandra.csv"    
# writing to csv file 
with open(filename, 'w', encoding='utf-8') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile)        
    # writing the fields 
    csvwriter.writerow(fields)        
    # writing the data rows 
    csvwriter.writerows(tokenized_sentence)


print("Tokenized sentences saved to:", filename)
