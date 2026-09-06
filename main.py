from player import add_player, view_players, update_player, search_player, delete_player

while True:
    print("\n"+"-"*35)
    print("         Cricket IQ")
    print("-"*35)

    print("1.Add Player")
    print("2.View Player")
    print("3.Search Player")
    print("4.Update Player")
    print("5.Delete Player")
    print("6.Exit")

    userChoice=input("Enter your choice:")

    if userChoice =="1":
        add_player()
    elif userChoice=="2":
        view_players()
    elif userChoice=="3":
        search_player()
    elif userChoice=="4":
        update_player()
    elif userChoice=="5":
        delete_player()
    elif userChoice=="6":
        print("Exiting..!")
        break
    else:
        print("Invalid choice!")
