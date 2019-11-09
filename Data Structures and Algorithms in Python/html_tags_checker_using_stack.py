import re

opening_tags =["html","head","body","title","h1","h2","span","b","div","p","a"]
closing_tags = ["/html","/head","/body","/title","/h1","/h2","/span","/b","/div","/p","/a"]
pattern = '<(.*?)>'
# closing_pattern = '</(.*?)>'
# excluding_closing_pattern = '<([^/].*?)>'

fp = open("test_html.html","r")
html_file = fp.read()
not_self_closing_tags = re.findall(pattern,html_file)
fp.close()

if not_self_closing_tags[0] == "!DOCTYPE html":
    del not_self_closing_tags[0]

print(not_self_closing_tags)

stack =[]

def html_checker(opening_tags,not_self_closing_tags,closing_tags):
    flag = 0
    for i in not_self_closing_tags:
        z = i.split(" ")
        if z[0] in opening_tags :
            stack.append(z[0])
            # print(stack)
            # print(len(stack))
        elif z[0] in closing_tags:
            try:
                stack.pop()
            except(IndexError):
                print("Issue: Closing tag is present without its opening tag")
                return flag
            # print(stack)
            # print(len(stack))
                
    if len(stack) == 0:
        flag = 1
        return flag
    else:
        print("Opening Tag is present without its closing tag")
        return flag

result = html_checker(opening_tags,not_self_closing_tags,closing_tags)
print("Valid HTML ") if result else print("Invalid HTML ")

           







