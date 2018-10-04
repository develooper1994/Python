with open("exercise1.txt","a+") as file:
    file.seek(0);
    content=file.read()
    print(content)
    file.write("\nLine 6")

