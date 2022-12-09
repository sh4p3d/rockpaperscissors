from calendar import c
import random

valid_answers = ["tas", "kagit", "makas"]
valid_answers2 = ["q", "w", "e"]
users_wins = 0
computer_wins = 0
print("Tas Kagit Makas!\n(cikmak icin icin q)\n(kendi puanlarini gormek icin icin w)\n(bilgisayarin puanlarini gormek icin e):")
while True:
    userinput = input("Secimin:").lower()
    computerinput = random.choice(valid_answers)
    if userinput == "q":
        print(f"-------------------------------------------\nSon Puanlar:\n\nBilgisayar:{computer_wins}\nSen:{users_wins}")
        break
    if userinput == "w":
        print("Senin Puanlarin:" + str(users_wins))
    if userinput == "e":
        print("Bilgisayarin Puanlari:" + str(computer_wins))
    if userinput not in valid_answers and userinput not in valid_answers2:
        print("Yanlis Cevap")
    if userinput == computerinput:
        print("Bilgisayarin Secimi: " + computerinput + "\nTarafsiz")

    elif userinput == "tas" and computerinput == "makas":
        print("Bilgisayarin Secimi: " + computerinput + "\nKazandin!")
        users_wins += 1
    elif userinput == "tas" and computerinput == "kagit":
        print("Bilgisayarin Secimi: " + computerinput + "\nKaybettin!")
        computer_wins += 1
    elif userinput == "makas" and computerinput == "tas":
        print("Bilgisayarin Secimi: " + computerinput + "\nKaybettin!")
        computer_wins += 1
    elif userinput == "makas" and computerinput == "kagit":
        print("Bilgisayarin Secimi: " + computerinput + "\nKazandin!")
        users_wins += 1
    elif userinput == "kagit" and computerinput == "makas":
        print("Bilgisayarin Secimi: " + computerinput + "\nKaybettin!")
        computer_wins +=1
    elif userinput == "kagit" and computerinput == "tas":
        print("Bilgisayarin Secimi: " + computerinput + "\nKazandin!")
        users_wins += 1