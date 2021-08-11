import re

def search_date(source):
    try:
        output=re.findall('\d{2}-\d{2}-\d{4}',source)
        if len(output)==0:
            print("Dates in (DD-MM-YYYY) format are not present in source text.\n")
        else:
            print(output)
    except:
        print("Error occurred.Please try again.")

def All_num(source):
    try:
        output=re.findall('\d+',source)
        if len(output)==0:
            print("Numbers are not present in source text.")
        else:
            print(output)
    except:
        print("Error occurred.Please try again.")

def Search_word(source):
    try:
        Word=input("Please enter the word you want to search in source:\n")
        output=re.findall(Word,source)
        if len(output)==0:
            print("Entered word is not present in source text.Please try another word.")
        else:
            print(output)
    except:
        print("Error occurred.Please try again.")

def Search_regex(source):
    try:
        regex=input('Please enter the regex which you want to run on source:\n')
        output=re.findall(regex,source)
        if len(output)==0:
            print("Text matching with regex pattern you enter is not present in source text.Please try another regex.")
        else:
            print(output)
    except:
        print("Error occurred.Please try again.")
    

def main():
    print("Hiii...Welcome to regex tool!!")
    print("\nHere you can enter your source text and enter the regex to fetch the data from source text.And we provide some preset functions.")
    Source= input("\nPlease enter your source text here:\n")
    while True:
        try:
            while True:
                sel=int(input("\nPlease select the operation:\n1:Search of numbers in source.\n2:Search all dates('dd-mm-yyyy') from source\n3:Specific word\n4:Custom regex\n0:quit\n"))
                if sel==1:
                    All_num(Source)
                elif sel==2:
                    search_date(Source)
                elif sel == 3:
                    Search_word(Source)
                elif sel == 4:
                    Search_regex(Source)
                elif sel==0:
                    break
                else:
                    print("You have selected wrong option.Please select one of the mentioned operation.\n")
            break
        except:
            print("Error occured. Please try again!!\n")


main()