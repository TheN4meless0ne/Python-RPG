# Imports
import json
import random


# Player stats
class Player:
  def __init__(self, name):
    self.name = playerName
    self.health = 100
    self.attack = 10
    self.crit_attack = self.attack * 1.5
    self.crit_chance = 0.15
    self.defense = 5
    self.coins = 0
  def is_alive(self):
    return self.health > 0
  def take_damage(self, damage):
    self.health -= damage
  def attack_enemy(self, enemy):
    damage = self.attack
    enemy.take_damage(damage)
    print(f"{self.name} attacks {enemy.name} for {damage} damage.")
  def __str__(self):
    return f"{self.name} - Health: {self.health}, Coins: {self.coins}"

class Enemy:
  def __init__(self, name, health, attack):
    self.name = name
    self.health = health
    self.attack = attack
  def is_alive(self):
    return self.health > 0
  def take_damage(self, damage):
    self.health -= damage
  def attack_player(self, player):
    damage = self.attack
    player.take_damage(damage)
    print(f"{self.name} attacks {player.name} for {damage} damage.")

# Main game loop
def main():
  playerName = input("What be the name of your champion? ")
  print("Welcome to the dungeon,", playerName)
  player = Player(playerName)

  # List of enemies you can encounter
  enemies = [
    Enemy("Weak inmate", 60, 7),
  ]

  # Game starts
  print("You wake up in a dark room.")
  




if __name__ == "__main__":
  main()