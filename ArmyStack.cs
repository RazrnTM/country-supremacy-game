using System;
using System.Collections.Generic;

namespace CountrySupremacyGame
{
    public class ArmyStack
    {
        // Properties to represent the state of the ArmyStack
        public List<Unit> Units { get; private set; }
        public int Morale { get; private set; }
        public int Movement { get; private set; }
        public string Formation { get; private set; }

        // Constructor to initialize the ArmyStack with default values
        public ArmyStack()
        {
            Units = new List<Unit>();
            Morale = 100; // Default morale
            Movement = 5; // Default movement range
            Formation = "Line"; // Default formation
        }

        // Method to add a unit to the ArmyStack
        public void AddUnit(Unit unit)
        {
            Units.Add(unit);
        }

        // Method to remove a unit from the ArmyStack
        public void RemoveUnit(Unit unit)
        {
            Units.Remove(unit);
        }

        // Method to change the morale of the ArmyStack
        public void ChangeMorale(int amount)
        {
            Morale += amount;
            Morale = Math.Max(0, Morale); // Ensure morale doesn't go below 0
        }

        // Method to move the ArmyStack
        public void Move(int distance)
        {
            // Update movement logic here
            Movement -= distance;
        }

        // Method for battle engagement with another ArmyStack
        public void EngageInBattle(ArmyStack enemy)
        {
            // Simplified battle logic
            int battleOutcome = Morale - enemy.Morale;
            if(battleOutcome > 0)
            {
                // Victory logic
                Console.WriteLine("Victory!");
            }
            else if(battleOutcome < 0)
            {
                // Defeat logic
                Console.WriteLine("Defeat!");
            }
            else
            {
                // Draw logic
                Console.WriteLine("It's a draw!");
            }
        }
    }
}