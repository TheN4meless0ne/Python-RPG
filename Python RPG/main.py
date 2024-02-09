from character import Hero, Enemy
from weapon import rusty_sword

# ------------ future references ------------
# hero.equip(rusty_sword)
# hero.drop()

hero = Hero(name="Hero", health=100)
enemy = Enemy(name="Enemy", health=80, weapon=rusty_sword)

while True:
  hero.attack(enemy)
  enemy.attack(hero)

  hero.health_bar.draw()
  enemy.health_bar.draw()


  input()