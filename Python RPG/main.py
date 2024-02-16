# ------------ imports ------------
from character import Player, Prison_Guard
from weapon import rusty_sword, rock, fists

# ------------ outer game loop ------------
while True:
  # ------------ pregame ------------
  player_name = input("What is your name, prisoner? ")
  print(f"Welcome, {player_name}.")
  print("If the game asks you to choose an option, it wants you to write one of the words that are in brackets.")
  print("Use the ENTER key to advance through the story.")

  player = Player(name=player_name, health=100, weapon=fists)
  prison_guard = Prison_Guard(name="Prison Guard", health=60, weapon=rusty_sword)

  copper_coin = 0
  silver_coin = 0
  gold_coin = 0

  # ------------ inner game loop ------------
  while True:
    input()
    print("You wake up in a dark prison cell.")
    input()
    print("You decide to look around and find a rock laying on the ground.")
    player.drop()
    player.equip(rock)
    input()
    print("A few days pass, and you decide you need to escape.")
    input()
    print("On your way out you stumble upon a prison guard.")
    print("The prison guard has a rusty sword, but you remember that you found a rock in your cell.")
    
    desicion1 = input("Do you wish to 'fight' the prison guard or 'run' away? ").lower()
    while True:
      if desicion1 == "fight":
        player.attack(prison_guard)
        prison_guard.attack(player)

        player.health_bar.draw()
        prison_guard.health_bar.draw()

        if player.health <= 0:
          print(f"You were defeated by {prison_guard.name}, and have lost the game.")
          break
        elif prison_guard.health <= 0:
          print(f"You defeated the {prison_guard.name}!")
          print(f"You drop the {player.weapon.name} and pick up the {prison_guard.weapon.name}.")
          player.drop()
          player.equip(prison_guard.weapon)
          print("You decide to search the body, and find some silver coins.")
          silver_coin += 6
          break
        else:
          input("Press ENTER to strike again.")

      elif desicion1 == "run":
        if player.health <= 8:
          break
        else:
          print(f"You run away, but the {prison_guard.name} catches up and beats you.")
          print("Your lose 20 health.")
          player.health -= 28
          player.health_bar.update()
          player.health_bar.draw()
          input()
          print("You realize that you have no choice.")
          input()
          print("You have to fight the prison guard again.")
          input()
          print("But this time you're weaker..")
          input()
          while True:
            player.attack(prison_guard)
            prison_guard.attack(player)

            player.health_bar.draw()
            prison_guard.health_bar.draw()

            if player.health <= 0:
              print(f"You were defeated by {prison_guard.name}, and have lost the game.")
              break
            elif prison_guard.health <= 0:
              print(f"You defeated the {prison_guard.name}!")
              print(f"You drop the {player.weapon.name} and pick up the {prison_guard.weapon.name}.")
              player.drop()
              player.equip(prison_guard.weapon)
              print("You decide to search the body, and find some silver coins.")
              silver_coin += 6
              break
            else:
              input("Press ENTER to strike again.")
    if player.health <= 0:
      print("You have lost the game.")
      print("Thank you for playtesting this game!")
      break
    else:
      input()
    
    print("You manage to escape the prison.")
    input()
    print("You spend the next few days getting as far away from the prison as possible.")
    input()
    print("Living off of berries and shrubbery, you find your way to a trader outpost.")
    input()
    


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