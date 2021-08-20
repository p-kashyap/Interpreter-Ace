import ace
while True:
    text=input("Ace-> ")
    result,error=ace.Run(text)
    if error:
        print(error)
    else:
        print(result)
