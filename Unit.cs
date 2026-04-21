using System;
using System.Collections.Generic;

namespace CountrySupremacyGame
{
    public class Unit
    {
        public string Name { get; set; }
        public int Health { get; set; }
        public int AttackPower { get; set; }
        public int Defense { get; set; }
        public int Morale { get; set; }

        public Unit(string name, int health, int attackPower, int defense)
        {
            Name = name;
            Health = health;
            AttackPower = attackPower;
            Defense = defense;
            Morale = 100; // Default morale
        }

        public void TakeDamage(int damage)
        {
            int effectiveDamage = damage - Defense;
            if (effectiveDamage > 0)
            {
                Health -= effectiveDamage;
            }
        }
    }
}