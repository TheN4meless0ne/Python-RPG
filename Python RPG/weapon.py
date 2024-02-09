class weapon:
  def __init__(self, name: str, weapon_type: str,damage: int, value: int) -> None:
    self.name = name
    self.weapon_type = weapon_type
    self.damage = damage
    self.value = value


fists = weapon(name="Fists",
              weapon_type="body",
              damage= 2,
              value= 0)

rusty_sword = weapon(name="Rusty Sword",
                    weapon_type="sword",
                    damage= 5,
                    value= 2)

rock = weapon(name="Rock",
                    weapon_type="Stone",
                    damage= 5,
                    value= 1)


