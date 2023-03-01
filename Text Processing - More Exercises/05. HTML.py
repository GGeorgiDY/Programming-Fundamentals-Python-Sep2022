title_of_an_article = input()
print("<h1>")
print(title_of_an_article)
print("</h1>")
content_of_that_article = input()
print("<article>")
print(content_of_that_article)
print("</article>")
while True:
    command = input()
    if command == "end of comments":
        break

    print("<div>")
    print(command)
    print("</div>")