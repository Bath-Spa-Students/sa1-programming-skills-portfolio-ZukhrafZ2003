# function to ask a question
def ask_question(question,correct_answer):
    answer = input(question).strip().lower() #convert answer lowercase
    if answer==correct_answer.lower(): # ignore capitalization 
        print("correct!")
    else: 
        print("wrong!") 

# list of European counteries and their capitals 
questions= [
    ("what is the capital of Austria" ,"Vienna"),  
    ("what is the capital of Cyprus","Nicosia"),
    ("what is the capital of Finland","Helsinki"),
    ("what is the capital of Denmark","Copenhagen"), 
    ("what is the capital of Georgia","Tallinn"),
    ("what is the capital of Iceland","Reykjavik"),
    ("what is the capital of Ireland","Dublin"),   
    ("what is the capital of Norway","Oslo"), 
    ("what is the capital of Poland","Warsaw"),
    ("what is the capital of Slovakia","Bratislava"),
]  
# check for each question and ask for the answers 
for question, correct_answer in questions:
    ask_question(question, correct_answer)  
     
