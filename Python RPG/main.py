from character import Player, Prison_Guard
from weapon import rusty_sword, rock

while True:
  # ------------ setup ------------
  player_name = input("What is your name, champion? ")
  print("Welcome,", player_name + "!")

  player = Player(name=player_name, health=100)
  prison_guard = Prison_Guard(name="Enemy", health=80, weapon=rusty_sword)

  # ------------ game loop ------------
  while True:
    print("You wake up in a dark prison cell.")
    input()
    print("You decide to look around and find a rock laying on the ground.")
    player.equip(rock)


  input("Press ENTER to restart..")