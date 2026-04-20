# Warfare Mechanics in Country Supremacy Game

## Unit Types

1. **Infantry**  
   - Health: 100  
   - Attack Power: 10  
   - Range: 1  

2. **Archers**  
   - Health: 75  
   - Attack Power: 12  
   - Range: 3  

3. **Cavalry**  
   - Health: 120  
   - Attack Power: 15  
   - Range: 1  

4. **Siege Weapons**  
   - Health: 150  
   - Attack Power: 25  
   - Range: 5  

## Attack Calculation

```python
class Unit:
    def __init__(self, unit_type, health, attack_power, range):
        self.unit_type = unit_type
        self.health = health
        self.attack_power = attack_power
        self.range = range

class Battle:
    def __init__(self):
        self.units = []

    def add_unit(self, unit):
        self.units.append(unit)

    def calculate_damage(self, attacker, target):
        if attacker.range >= target.range:
            return attacker.attack_power
        else:
            return 0  # No damage if out of range

    def resolve_battle(self):
        # Simplified battle resolution
        for attacker in self.units:
            for target in self.units:
                if attacker != target:
                    damage = self.calculate_damage(attacker, target)
                    target.health -= damage
                    print(f'{attacker.unit_type} attacks {target.unit_type} for {damage} damage!')
                    if target.health <= 0:
                        print(f'{target.unit_type} has been defeated!')
                        self.units.remove(target)

# Example usage
infantry = Unit('Infantry', 100, 10, 1)
archer = Unit('Archer', 75, 12, 3)
battle = Battle()
battle.add_unit(infantry)
battle.add_unit(archer)
battle.resolve_battle()
```

## Battle Resolution
- The battle is resolved in turns, with each unit attacking based on their range.
- Units are removed from the battle once their health reaches zero.