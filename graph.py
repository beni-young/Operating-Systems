def main():

    contents = []
    linelist = []
    parentlist = []
    comparelist = []
    testlist = []
    level = 0

    # Takes in dot file that was created in C part1
    # Reads each line and takes only the process ID number and stores in linelist
    f=open("simplegraph.dot", "r")
    if f.mode == 'r':
        contents = f.readlines()
        for x in contents:
            for word in x.split("\""): # splits at quotation mark " on line
                comparelist.append(word)
                process = word.rsplit(' ', 1)[-1] # takes in the process digits starting from last up to whitespace
                if process.isdigit():
                    linelist.append(process)

                    
    parentlist = linelist[0::2]; # list of just parent nodes 
    childlist = linelist[1::2]; # list of just child nodes

    # Used for testing lists
    print(linelist)     
    print(parentlist)
    print(childlist)
    print(comparelist)

    # Finds the top most node which is process that initializes the first fork() from question1.c
    for p in parentlist:
        if not p in childlist:
            ix = parentlist.index(p)
            topnode = p
            print(p)
            parentnode = childlist[ix] # establishes the Parent node of the binary tree (Level: 0)
            print(parentnode)

    # Creates dot file for graphviz viewing
    g = open("demo.dot", "w")
    g.writelines("Digraph D {\n") 
    quotes = "\""
    grr = []

    # Takes the list with still having Parent ID -> Process ID
    # and changes it Process ID -> Process ID if Parent isn't actually Parent node for graphviz
    for chk in comparelist:
        if not topnode in chk and "Parent" in chk:
            grr = quotes + chk + quotes                        # adds in back the quotes that was taken out
            testlist.append(grr.replace("Parent", "Process"))  #changes Parent to Process if not Parent node with Level: 0
        elif topnode in chk:
            #######grr = quotes + chk + quotes                     
            ######testlist.append(grr)            
            srch = comparelist.index("Parent ID: " + topnode)  # finds the line with Parent ID is Top most node that was init fork() 
            del comparelist[ srch:srch + 2]                    # takes that whole line and deletes it so doesn't show in graphviz            
        elif "Process" in chk:                                 # Process ID is just left as Process ID
            grr = quotes + chk + quotes + "\n"
            testlist.append(grr)
        else:
            testlist.append(chk)                               # the '->' and '\n' in comparelist are left alone


    # My attempt at putting Levels in the demo.dot file according to Process ID
    # I have the Parent node and from there can calculate where each node is from Parent
    
#    levellist = [parentnode]    
#    counter = 0

#    for a in parentlist:
#        if parentnode == a:
#            levellist.append(childlist[counter])
            
#        counter += 1             
#    def get_levels(tree, roots):
#        result = []
#        roots = list(roots)
#        while roots:
#            result.append(roots)
#            roots = [c for k in roots for c in tree]
#
#        return result

#    get_levels(childlist, parentnode)
     

####    print(testlist)

    # Writes out the new graph dot file demo.dot
    g.writelines(testlist)
    g.write("}")
    g.close()
    
if __name__== "__main__":
    main()
    
    
