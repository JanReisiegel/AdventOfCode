using Day10_PipeMaze.Models;

Console.WriteLine("-----------------------------------------------\n\n\tTest1\n");
var test1 = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day10_PipeMaze/Test1.txt"); //desktop
//var test1 = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day10_PipeMaze/Test1.txt");  //laptop
PipeMaze pm1 = new PipeMaze(test1);
Console.WriteLine("PartOne: " + pm1.PartOne());
Console.WriteLine("PartTwo: " + pm1.PartTwo());

Console.WriteLine("-----------------------------------------------\n\n\tTest2\n");
var test2 = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day10_PipeMaze/Test2.txt"); //desktop
//var test1 = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day10_PipeMaze/Test2.txt");  //laptop
PipeMaze pm2 = new PipeMaze(test2);
Console.WriteLine("PartOne: " + pm2.PartOne());
Console.WriteLine("PartTwo: " + pm2.PartTwo());

Console.WriteLine("-----------------------------------------------\n\n\tTest3\n");
var test3 = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day10_PipeMaze/Test2.txt"); //desktop
//var test1 = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day10_PipeMaze/Test2.txt");  //laptop
PipeMaze pm3 = new PipeMaze(test3);
Console.WriteLine("PartOne: " + pm3.PartOne());
Console.WriteLine("PartTwo: " + pm3.PartTwo());

Console.WriteLine("-----------------------------------------------\n\n\tTest4\n");
var test4 = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day10_PipeMaze/Test2.txt"); //desktop
//var test1 = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day10_PipeMaze/Test2.txt");  //laptop
PipeMaze pm4 = new PipeMaze(test4);
Console.WriteLine("PartOne: " + pm4.PartOne());
Console.WriteLine("PartTwo: " + pm4.PartTwo());

Console.WriteLine("-----------------------------------------------\n\n\tTest5\n");
var test5 = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day10_PipeMaze/Test2.txt"); //desktop
//var test1 = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day10_PipeMaze/Test2.txt");  //laptop
PipeMaze pm5 = new PipeMaze(test5);
Console.WriteLine("PartOne: " + pm5.PartOne());
Console.WriteLine("PartTwo: " + pm5.PartTwo());


Console.WriteLine("-----------------------------------------------\n\n\tÚloha\n");
var input = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day10_PipeMaze/Puzzle.txt"); //desktop
//var input = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day10_PipeMaze/Puzzle.txt"); //laptop
PipeMaze pm = new PipeMaze(input);
Console.WriteLine("PartOne: " + pm.PartOne());
Console.WriteLine("PartTwo: " + pm.PartTwo());
