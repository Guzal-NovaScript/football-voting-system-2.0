votes = {
    "Real Madrid": 0,
    "Barcelona": 0,
    "Manchester City": 0,
    "Bayern Munich": 0,
    "PSG": 0
}

print("--- FOOTBALL VOTING SYSTEM STARTED ---")
print("(Type 'stop' as your name to end the poll and see the results)\n")

while True:
    name = input("Enter your name: ")
    
    if name.lower() == 'stop':
        break
        
    print(f"Hello, {name}!")

    age = int(input("Enter your age: "))

    if age < 30:
        print("\nChoose one of the following clubs:")
        print("1 - Real Madrid")
        print("2 - Barcelona")
        print("3 - Manchester City")
        print("4 - Bayern Munich")
        print("5 - PSG")
        
        choice = input("\nEnter the club number to vote: ")
        
        if choice == "1":
            print("Hala Madrid! ⚪🔥\n")
            votes["Real Madrid"] += 1
        elif choice == "2":
            print("Visca el Barca! 🔵🔴\n")
            votes["Barcelona"] += 1
        elif choice == "3":
            print("Blue Moon! 🩵⚽\n")
            votes["Manchester City"] += 1
        elif choice == "4":
            print("Mia San Mia! 🔴⚪\n")
            votes["Bayern Munich"] += 1
        elif choice == "5":
            print("Ici c'est Paris! 🔵🔴\n")
            votes["PSG"] += 1
        else:
            print("Invalid choice, vote not counted.\n")

    else:
        print(f"Sorry, {name}. This poll is only for people under 30. Good luck!\n")

print("\n=== POLL RESULTS ===")
for club, count in votes.items():
    print(f"- {club}: {count} vote(s)")
