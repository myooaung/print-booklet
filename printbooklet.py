def getPages():
    pages = int(input("Enter number of Pages: "))
    if pages%4 != 0:
        print("Must be a multiple of 4!")
        return
    else:
        list = []
        list.append(pages)
        t = pages
        for k in range(1, int(pages / 2), 2):
            list.append(k)
            list.append(k + 1)
            list.append(t - 1)
            if k < (pages / 2) - 1:
                list.append(t - 2)
            k = k + 2
            t = t - 2
        print(list)
        odd = []
        even = []
        count = 0
        turn = True
        evenindex = 0 
        oddindex = 0
        for index in range(0,len(list),1):
            if (count > 1):
                turn = not turn
                count = 0
            if (turn):
                odd.append(list[index])
                oddindex+=1
            
            if (not turn):
                even.append( list[index])
                evenindex+=1
            count+=1
        print('odd')
        for page in odd: 
            print (str(page)+',',end="")
            
        print('\neven')        
        for page in even:
            print(str(page)+',',end="")
        print()
getPages()
