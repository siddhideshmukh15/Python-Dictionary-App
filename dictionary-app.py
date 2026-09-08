dictionary ={
    "happy":"feeling good or pleased",
    "Wamble":"A feeling of nausea or uneasy sound in stomach",
    "obfuscate":"confusing",
    "recreant":"Cowardly",
    "moonglade":"The bright track of moonlight",
    "clever":"quick to learn"
}
while True:
    word =input("\n Enter a word:").lower()

    if word in dictionary:
        print("Meaning",dictionary[word])

    else:
        print("word not found!")

    again =input("search another word?(Y/N):").lower()


    if again!="y":
        print("Thank you! visit again!")
        break