# ------------ class setup ------------
class weapon:
  def __init__(self, name: str, weapon_type: str,damage: int, value: int) -> None:
    self.name = name
    self.weapon_type = weapon_type
    self.damage = damage
    self.value = value

# ------------ items ------------
fists = weapon(name="Fists",
              weapon_type="body",
              damage= 2,
              value= 0)

rusty_sword = weapon(name="Rusty Sword",
                    weapon_type="sword",
                    damage= 12,
                    value= 1)

rock = weapon(name="Rock",
                    weapon_type="Stone",
                    damage= 10,
                    value= 1)


