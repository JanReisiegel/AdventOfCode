using Day3_GearRatios.Models;

Console.WriteLine("-----------------------------------------------\n\n\tTest 1\n");
var test1 = await File.ReadAllTextAsync("E:/++AdventOfCode/AoC2023/Day3_GearRatios/test1.txt");
GearRatios gr1 = new GearRatios(test1);

Console.WriteLine("PartOne: " + gr1.SumPartNumbers);
Console.WriteLine("PartTwo: " + gr1.SumGearNumbers);

Console.WriteLine("-----------------------------------------------\n\n\tÚloha1\n");
var input = await File.ReadAllTextAsync("E:/++AdventOfCode/AoC2023/Day3_GearRatios/Puzzle1.txt");
GearRatios gr2 = new GearRatios(input);
Console.WriteLine("PartOne: " + gr2.SumPartNumbers);
Console.WriteLine("PartTwo: " + gr2.SumGearNumbers);
