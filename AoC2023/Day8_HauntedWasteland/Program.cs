using Day8_HauntedWasteland.Models;
using System.Text.RegularExpressions;

Console.WriteLine("-----------------------------------------------\n\n\tTest0\n");
var test0 = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day8_HauntedWasteland/Test1.txt"); //desktop
//var test1 = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day8_HauntedWasteland/Test1.txt");  //laptop
HauntedWasteland hw0 = new HauntedWasteland(test0.ToList());
Console.WriteLine("PartOne: " + hw0.PartOne());
//Console.WriteLine("PartTwo: " + hw1.PartTwo());

Console.WriteLine("-----------------------------------------------\n\n\tTest1\n");
var test = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day8_HauntedWasteland/Test2.txt"); //desktop
//var test1 = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day8_HauntedWasteland/Test2.txt");  //laptop
HauntedWasteland hw1 = new HauntedWasteland(test.ToList());
Console.WriteLine("PartOne: " + hw1.PartOne());
//Console.WriteLine("PartTwo: " + hw1.PartTwo());

Console.WriteLine("-----------------------------------------------\n\n\tTest3\n");
var test2 = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day8_HauntedWasteland/Test3.txt"); //desktop
//var test1 = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day8_HauntedWasteland/Test3.txt");  //laptop
HauntedWasteland hw3 = new HauntedWasteland(test.ToList());
Console.WriteLine("PartTwo: " + hw3.PartTwo());

Console.WriteLine("-----------------------------------------------\n\n\tÚloha\n");
var input = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day8_HauntedWasteland/Puzzle.txt"); //desktop
//var input = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day8_HauntedWasteland/Puzzle.txt"); //laptop
HauntedWasteland hw2 = new HauntedWasteland(input.ToList());
Console.WriteLine("PartOne: " + hw2.PartOne());
Console.WriteLine("PartTwo: " + hw2.PartTwo());