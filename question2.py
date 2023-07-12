NUM = 0
printlist=[]
with open("fyx_chinamoney.csv","r") as f :
    line =1
    while line:
        line = f.readline().split("\n")[0]
        NUM += 1
        printlist.append(str(line))
        if NUM == 80 :
            NUM =0
            print(printlist)
            printlist.clear()
    print(printlist)
