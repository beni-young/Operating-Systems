def main():

    contents = []
    linelist = []
    parentlist = []
    comparelist = []
    testlist = []
    level = 0
    
    f=open("simplegraph.dot", "r")
    if f.mode == 'r':
        contents = f.readlines()
        for x in contents:
            for word in x.split("\""):
                comparelist.append(word)
                process = word.rsplit(' ', 1)[-1]
                if process.isdigit():
                    linelist.append(process)

                    
    parentlist = linelist[0::2];
    childlist = linelist[1::2];
    
    print(linelist)
    print(parentlist)
    print(childlist)
    print(comparelist)
    
    for p in parentlist:
        if not p in childlist:
            ix = parentlist.index(p)
            topnode = p
            print(p)
            parentnode = childlist[ix]
            print(parentnode)
            
    g = open("demo.dot", "w")
    quotes = "\""
    grr = []
    
    for chk in comparelist:
        if not topnode in chk and "Parent" in chk:
            grr = quotes + chk + quotes + "\n" 
            testlist.append(grr.replace("Parent", "Process"))
        elif topnode in chk:
            #grr = quotes + chk + quotes
            #testlist.append(grr)            
            srch = comparelist.index("Parent ID: " + topnode)
            del comparelist[ srch:srch + 2]
            
        elif "Process" in chk:
            grr = quotes + chk + quotes + "\n"
            testlist.append(grr)
        else:
            testlist.append(chk)


    levellist = [parentnode]

    for i in linelist:
        for j in levellist:
            if i == j:
                ind = linelist.index(i) + 1
                lnd = levellist.index(j) + 1
                levellist.insert(lnd, levellist[lnd] + " " + linelist[ind])
            #else:
             #   levellist.append(i)
                # levellist.append(linelist[linelist.index(j+1)])
    
    print(levellist)
                                 
#    for cln in testlist:
#        if parentnode in cln:
#            xrr = cln + "Level: " + level
      

#    print(testlist)
    g.writelines(testlist)
    g.write("")
    g.close()
    
if __name__== "__main__":
    main()
    
    
