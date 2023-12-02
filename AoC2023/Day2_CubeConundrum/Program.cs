using Day2_CubeConundrum.Models;

Console.WriteLine("-----------------------------------------------\n\n\tTest 1\n");
var test1 = await File.ReadAllTextAsync("E:/++AdventOfCode/AoC2023/Day2_CubeConundrum/test1.txt");
Dictionary<string, int> testConditions1 = new Dictionary<string, int>
{
    {"red", 12},
    {"green", 13},
    {"blue", 14},
};
CubeConundrum gTest1 = new CubeConundrum(test1, testConditions1);
Console.WriteLine(gTest1.SumOfPosGames);
Console.WriteLine("Power: " + gTest1.PowerOfGames);

Console.WriteLine("-----------------------------------------------\n\n\tÚloha1\n");
var input = await File.ReadAllTextAsync("E:/++AdventOfCode/AoC2023/Day2_CubeConundrum/Puzzle1.txt");
Console.WriteLine(input.Substring(input.Length-3));
Dictionary<string, int> conditions = new Dictionary<string, int>
{
    {"red", 12},
    {"green", 13},
    {"blue", 14},
};
CubeConundrum games1 = new CubeConundrum(input, testConditions1);
Console.WriteLine(games1.SumOfPosGames);
Console.WriteLine("Power: " + games1.PowerOfGames);