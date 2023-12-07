using Day7_CamelCards.Models;
using System.Numerics;

Console.WriteLine("-----------------------------------------------\n\n\tTest\n");
var test = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day7_CamelCards/Test.txt"); //desktop
//var test1 = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day7_CamelCards/Test.txt");  //laptop
CamelCards cc1 = new CamelCards(test.ToList());
Console.WriteLine("PartOne: " + cc1.PartOne());
Console.WriteLine("PartTwo: " + cc1.PartTwo());

Console.WriteLine("-----------------------------------------------\n\n\tÚloha\n");
var input = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day7_CamelCards/Puzzle.txt"); //desktop
//var input = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day7_CamelCards/Puzzle.txt"); //laptop
CamelCards cc2 = new CamelCards(input.ToList());
Console.WriteLine("PartOne: " + cc2.PartOne());
var input1 = await File.ReadAllTextAsync("E:/++AdventOfCode/AoC2023/Day7_CamelCards/Puzzle.txt");
Console.WriteLine("PartTwo: " + PartTwo(input1));


object PartTwo(string input) => Solve(input, Part2Points);

BigInteger Part2Points(string hand)
{
    // The most frequent card ignoring J with a special case for "JJJJJ":
    var replacement = (
        from ch in hand
        where ch != 'J'
        group ch by ch into g
        orderby g.Count() descending
        select g.Key
    ).FirstOrDefault('J');

    var cv = CardValue(hand, "J123456789TQKA");
    var pv = PatternValue(hand.Replace('J', replacement));
    return (pv << 64) + cv;
}

BigInteger CardValue(string hand, string cardOrder) =>
         new BigInteger(hand.Select(ch => (byte)cardOrder.IndexOf(ch)).Reverse().ToArray());

BigInteger PatternValue(string hand) =>
       new BigInteger(hand.Select(ch => (byte)hand.Count(x => x == ch)).Order().ToArray());
int Solve(string input, Func<string, BigInteger> getPoints)
{
    var bidsByRanking = (
        from line in input.Split("\n")
        let hand = line.Split(" ")[0]
        let bid = int.Parse(line.Split(" ")[1])
        orderby getPoints(hand)
        select bid
    );

    return bidsByRanking.Select((bid, rank) => (rank + 1) * bid).Sum();
}