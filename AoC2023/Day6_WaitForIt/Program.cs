using Day6_WaitForIt.Models;

Console.WriteLine("-----------------------------------------------\n\n\tTest\n");
var test = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day6_WaitForIt/Test.txt"); //desktop
//var test1 = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day6_WaitForIt/Test.txt");  //laptop
WaitForIt wft1 = new WaitForIt(test);
Console.WriteLine("PartOne: " + wft1.PartOne());
Console.WriteLine("PartTwo: " + wft1.PartTwo());

Console.WriteLine("-----------------------------------------------\n\n\tÚloha\n");
var input = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day6_WaitForIt/Puzzle.txt"); //desktop
//var input = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day6_WaitForIt/Puzzle.txt"); //laptop
WaitForIt wft2 = new WaitForIt(input);
Console.WriteLine("PartOne: " + wft2.PartOne());
Console.WriteLine("PartTwo: " + wft2.PartTwo());