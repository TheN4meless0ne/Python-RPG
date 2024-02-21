# ------------ imports ------------
import time
import random
import sys
from character import Player, Prison_Guard
from weapon import rusty_sword, rock, fists

# ------------ functions ------------
def fake_type(words):
  words += "\n"
  for char in words:
      time.sleep(random.choice([
        0.03
      ]))
      sys.stdout.write(char)
      sys.stdout.flush()
  time.sleep(0.5)

# ------------ outer game loop ------------
while True:
  # ------------ pregame ------------
  player_name = input("What is your name, human? ")
  fake_type(f"Welcome, {player_name}.")
  fake_type("If the game asks you to choose an option, it wants you to write one of the words that are in brackets.")
  fake_type("Use the ENTER key to advance through the story.")

  player = Player(name=player_name, health=100, weapon=fists)
  prison_guard = Prison_Guard(name="Prison Guard", health=50, weapon=rusty_sword)

  copper_coin = 0
  silver_coin = 0
  gold_coin = 0

  # ------------ inner game loop ------------
  while True:
    input()
    fake_type("You wake up in a dark prison cell.")
    fake_type("You decide to look around and find a rock laying on the ground.")
    player.drop()
    player.equip(rock)
    fake_type("A few days pass, and you decide you need to escape.")
    fake_type("On your way out you stumble upon a prison guard.")
    fake_type("The prison guard has a rusty sword, but you remember that you found a rock in your cell.")
    desicion1 = input("Do you wish to 'fight' the prison guard or 'run' away? ").lower()
    while True:
      if desicion1 == "fight":
        player.attack(prison_guard)
        prison_guard.attack(player)

        player.health_bar.draw()
        prison_guard.health_bar.draw()

        if player.health <= 0:
          fake_type(f"You were defeated by {prison_guard.name}, and have lost the game.")
          break
        elif prison_guard.health <= 0:
          fake_type(f"You defeated the {prison_guard.name}!")
          fake_type(f"You drop the {player.weapon.name} and pick up the {prison_guard.weapon.name}.")
          player.drop()
          player.equip(prison_guard.weapon)
          fake_type("You decide to search the body, and find 6 silver coins.")
          silver_coin += 6
          fake_type("[+ 6 Silver Coins]")
          break
        else:
          input("Press ENTER to strike again.")

      elif desicion1 == "run":
        if player.health <= 8:
          break
        else:
          fake_type(f"You run away, but the {prison_guard.name} catches up and beats you.")
          fake_type("Your lose 20 health.")
          player.health -= 28
          player.health_bar.update()
          player.health_bar.draw()
          input()
          fake_type("You realize that you have no choice.")
          fake_type("You have to fight the prison guard again.")
          fake_type("But this time you're weaker..")
          input()
          while True:
            player.attack(prison_guard)
            prison_guard.attack(player)

            player.health_bar.draw()
            prison_guard.health_bar.draw()

            if player.health <= 0:
              fake_type(f"You were defeated by {prison_guard.name}, and have lost the game.")
              break
            elif prison_guard.health <= 0:
              fake_type(f"You defeated the {prison_guard.name}!")
              fake_type(f"You drop the {player.weapon.name} and pick up the {prison_guard.weapon.name}.")
              player.drop()
              player.equip(prison_guard.weapon)
              fake_type("You decide to search the body, and find 6 silver coins.")
              silver_coin += 6
              print("[+ 6 Silver Coins]")
              break
            else:
              input("Press ENTER to strike again.")
    if player.health <= 0:
      fake_type("You have lost the game.")
      fake_type("Thank you for playtesting this game!")
      break
    else:
      input()
    
    fake_type("You manage to escape the prison.")
    fake_type("You spend the next few days getting as far away from the prison as possible.")
    fake_type("Living off of berries and shrubbery, you manage to find your way to a trader outpost.")
    fake_type("You spot a doctor who says that he can treat you for 4 silver coins.")
    desicion2 = input("Do you 'accept' the offer, or 'decline' it? ").lower()
    while True:
      if desicion2 == "accept":
        fake_type("You pay the 4 silvers and the doctor heals your wounds.")
        silver_coin -= 4
        player.health += 60
        player.health_bar.update()
        player.health_bar.draw()
        print("[- 4 Silver Coins]")
        fake_type("You continue on your way.")
        break
      elif desicion2 == "decline":
        fake_type("You decline the doctors offer, and continue on your way.")
        break
    
    


    if player.health <= 0:
      print("You have lost the game.")
      print("Thank you for playtesting this game!")
      break
    else:
      print("You won!")
      print(f"You have", silver_coin, "silver coins.")
      print(f"Thank you for playtesting this game!")
      break


  input("Press ENTER to restart..")