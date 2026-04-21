using System;

namespace CountrySupremacyGame
{
    public class City : Selectable
    {
        public int Population { get; private set; }
        public int GoldProduction { get; private set; }
        public int FoodProduction { get; private set; }
        public int DefenseLevel { get; private set; }
        public int Garrison { get; private set; }

        public City(int population, int goldProduction, int foodProduction, int defenseLevel, int garrison)
        {
            Population = population;
            GoldProduction = goldProduction;
            FoodProduction = foodProduction;
            DefenseLevel = defenseLevel;
            Garrison = garrison;
        }

        public void ProduceResources()
        {
            // Implement resource production logic here
            Console.WriteLine("Producing resources...");
        }

        public void TakeDamage(int damage)
        {
            DefenseLevel -= damage;
            if (DefenseLevel < 0) DefenseLevel = 0;
            Console.WriteLine($"City damaged, new defense level: {DefenseLevel}");
        }

        public void ManageGarrisonTroops(int troops)
        {
            Garrison += troops;
            Console.WriteLine($"Garrison updated, new troop count: {Garrison}");
        }
    }
}