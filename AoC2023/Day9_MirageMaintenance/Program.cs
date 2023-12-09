using Day9_MirageMaintenance.Models;

Console.WriteLine("-----------------------------------------------\n\n\tTest\n");
var test = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day9_MirageMaintenance/Test.txt"); //desktop
//var test1 = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day9_MirageMaintenance/Test.txt");  //laptop
MirageMaintenance mm1 = new MirageMaintenance(test.ToList());
Console.WriteLine("PartOne: " + mm1.PartOne());
Console.WriteLine("PartTwo: " + mm1.PartTwo());

Console.WriteLine("-----------------------------------------------\n\n\tÚloha\n");
var input = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day9_MirageMaintenance/Puzzle.txt"); //desktop
//var input = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day9_MirageMaintenance/Puzzle.txt"); //laptop
MirageMaintenance mm2 = new MirageMaintenance(input.ToList());
Console.WriteLine("PartOne: " + mm2.PartOne());
Console.WriteLine("PartTwo: " + mm2.PartTwo());