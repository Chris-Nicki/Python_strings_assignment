# Python Strings
print()
print("# 1. Product Review Analysis")
print()
# 1. Product Review Analysis
"""Objective:The aim of this assignment is to extract insights from
 product reviews by using string manipulation to categorize and 
 summarize customer feedback for a SaaS product.
"""
# Task 1: Keyword Highlighter
"""Write a program that searches through a series of product reviews
 for keywords such as "good", "excellent", "bad", "poor", and "average".
 Print out each review with the keywords in uppercase so they stand out.
"""
python_reviews = [ "This product is really good. I'm impressed with its quality.", 
                    "The performance of this product is excellent. Highly recommended!", 
                    "I had a bad experience with this product. It didn't meet my expectations.",
                    "Poor quality product. Wouldn't recommend it to anyone.", 
                    "The product was average. Nothing extraordinary about it." ]
uppercase_reviews = []
review_words = ["good", "excellent", "bad", "poor", "average"]
for sentence in python_reviews:
    for word in review_words:
        sentence = sentence.replace(word, word.upper())
        sentence = sentence.replace(word.title(), word.upper())
        uppercase_reviews.append(sentence)
    print(sentence)
print()
print("Task 2. Sentiment Tally")
print()
# Task 2: Sentiment Tally
"""Develop a function that tallies the number of positive and negative words in each review.
   Use a predefined list of positive and negative words to check against. The function should 
   return the count of positive and negative words for each review.
"""
positive_words = ["good", "excellent","outstanding", "fantastic"]
negative_words = ["bad", "poor", "average", "terrible", "rotten"]
def positive_and_negative_count():
    number_of_positive = 0
    number_of_negative = 0
    for sentence in python_reviews:
        for word in sentence.split():
            word = word.replace(".", "")
            if word.lower() in positive_words:
                number_of_positive += 1
    print(f"Positive words: {number_of_positive}")
    for sentence in python_reviews:
        for word in sentence.split():
            word = word.replace(".", "")
            if word.lower() in negative_words:
             number_of_negative += 1
    print(f"Negative Words: {number_of_negative}")      
positive_and_negative_count()

print()
print("Task 3. Review Summaries;") 
# Task3: Review Summary
"""Implement a script that takes the first 30 characters of a review and appends "…"
   to create a summary. Ensure that the summary does not cut off in the middle of a word.
""" 
review =[ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!",  "I had a bad experience with this product. It didn't meet my expectations.","Poor quality product. Wouldn't recommend it to anyone.",  "The product was average. Nothing extraordinary about it." ]

sentence = " ".join(review), 
i = 30
for sentence in review:
    i = 30
    while sentence[i] != " ":
        i += 1
    summary_review = sentence[:i] + ".."
    print(summary_review)


print()
print("# 2. User Input Data Processor")
print()
# 2. User Input Input Data Processor
# Objective: The aim of this assignment is to process and format user input data.
# Task 1: Input the Validator
"""Write a script that checks the length of the user's first name and last name. Both should be at 
   least 2 characters long. If not, print an error message.
"""
while True:
    first_name = input("What is your first name? ")
    last_name = input("We need a last name as well please. ")
    if len(first_name) < 2 :
        print("Error! First name must be more thane 2 characters.")
        
    else:
        if len(last_name) < 2:
            print("Error! Last name must be more thane 2 characters.")
           
        else:
            name = first_name + " " + last_name 
            print(f"Welcome {name}, name verified; please turn in your homework.")
            break
 






























