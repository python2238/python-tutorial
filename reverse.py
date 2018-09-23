while True:  #Infinite Loop
    print("Press 0 to exit")
    inp = int(input("=== Enter Year to Check ===\n"))
    if inp == 0:
        break
    else:
        if inp%4==0:
            if inp%100 == 0:
                if inp%400 == 0:
                    print("It is a leep Year")
                else:
                    print("It is Not a leep Year")
            else:
                print("It is a leep Year")
        else:
            print("It is not a leep Year")
