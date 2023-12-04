using Day4_Scratchcards.Models;
using System.Text.RegularExpressions;

Console.WriteLine("-----------------------------------------------\n\n\tTest 1\n");
var test1 = await File.ReadAllTextAsync("E:/++AdventOfCode/AoC2023/Day4_Scratchcards/Test2.txt"); 
//var test1 = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day4_Scratchcards/Test1.txt"); 
Scratchcards sc1 = new Scratchcards(test1);

Console.WriteLine("PartOne: " + sc1.GetGameValue());
Console.WriteLine("PartTwo: " + sc1.GetScratchcardsNumber());

Console.WriteLine("-----------------------------------------------\n\n\tÚloha1\n");
var input = await File.ReadAllTextAsync("E:/++AdventOfCode/AoC2023/Day4_Scratchcards/Puzzle1.txt");
//var input = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day4_Scratchcards/Puzzle1.txt");
Scratchcards sc2 = new Scratchcards(input);
Console.WriteLine("PartOne: " + sc2.GetGameValue());
Console.WriteLine("PartTwo: " + sc2.GetScratchcardsNumber());