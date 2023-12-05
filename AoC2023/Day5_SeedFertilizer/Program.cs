using Day5_SeedFertilizer.Models;

List<List<(long from, long to, long range)>> Maps = new();

Console.WriteLine("-----------------------------------------------\n\n\tTest 1\n");
var test1 = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day5_SeedFertilizer/Test.txt"); //desktop
//var test1 = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day5_SeedFertilizer/Test.txt");  //laptop
//GiveseedFertilizer gf1 = new GiveseedFertilizer(test1);
PartOne(test1);//Console.WriteLine("PartOne: " + gf1.MinimumResult);
PartTwo(test1);//Console.WriteLine("PartTwo: " + sc1.GetScratchcardsNumber());

Console.WriteLine("-----------------------------------------------\n\n\tÚloha1\n");
var input = await File.ReadAllLinesAsync("E:/++AdventOfCode/AoC2023/Day5_SeedFertilizer/Puzzle.txt"); //desktop
//var input = await File.ReadAllTextAsync("D:/++AoC/AoC2023/Day5_SeedFertilizer/Puzzle.txt"); //laptop
//Scratchcards sc2 = new Scratchcards(input);
PartOne(input);//Console.WriteLine("PartOne: " + sc2.GetGameValue());
PartTwo(input);//Console.WriteLine("PartTwo: " + sc2.GetScratchcardsNumber());



void PartOne(string[] input)
{
    var inputString = string.Join('\n', input);
    var seedsAndMaps = inputString.Split("\n\n");

    var seedsData = seedsAndMaps[0];
    var mapData = seedsAndMaps.Skip(1).ToArray();

    foreach (string line in mapData)
    {
        Maps.Add(ParseMap(line));
    }

    var minimumResult = seedsData.Split().Skip(1).Select(long.Parse).Min(seed => ProcessSeed(seed));
    Console.WriteLine(minimumResult);
}

void PartTwo(string[] input)
{
    var seeds = input[0].Split(' ').Skip(1).Select(x => long.Parse(x)).ToList();
    List<(long from, long to, long adjustment)>? currentMap = null;
    Maps = new List<List<(long from, long to, long range)>>();

    foreach (var line in input.Skip(2))
    {
        if (line.EndsWith(':'))
        {
            currentMap = new List<(long from, long to, long adjustment)>();
            continue;
        }

        if (line.Length == 0 && currentMap != null)
        {
            Maps.Add(currentMap!);
            currentMap = null;
            continue;
        }

        var nums = line.Split(' ').Select(x => long.Parse(x)).ToArray();
        currentMap!.Add((nums[1], nums[1] + nums[2] - 1, nums[0] - nums[1]));
    }

    if (currentMap != null) Maps.Add(currentMap);

    var ranges = new List<(long from, long to)>();
    for (var i = 0; i < seeds.Count; i += 2) ranges.Add((from: seeds[i], to: seeds[i] + seeds[i + 1] - 1));

    foreach (var map in Maps)
    {
        var orderedmap = map.OrderBy(x => x.from).ToList();

        var newranges = new List<(long from, long to)>();
        foreach (var r in ranges)
        {
            var range = r;
            foreach (var mapping in orderedmap)
            {
                if (range.from < mapping.from)
                {
                    newranges.Add((range.from, Math.Min(range.to, mapping.from - 1)));
                    range.from = mapping.from;
                    if (range.from >= range.to)
                        break;
                }

                if (range.from <= mapping.to)
                {
                    newranges.Add((range.from + mapping.range, Math.Min(range.to, mapping.to) + mapping.range));
                    range.from = mapping.to + 1;
                    if (range.from >= range.to)
                        break;
                }
            }

            if (range.from < range.to)
                newranges.Add(range);
        }

        ranges = newranges;
    }

    var result2 = ranges.Min(r => r.from);
    Console.WriteLine(result2);
}


List<(long from, long to, long range)> ParseMap(string map)
{
    var mapData =
        new List<(long source, long destination, long range)>();
    var mapLines = map.Split('\n');
    foreach (var line in mapLines.Skip(1))
    {
        var parts = line.Split();
        var destination = long.Parse(parts[0]);
        var source = long.Parse(parts[1]);
        var range = long.Parse(parts[2]);
        mapData.Add((source, destination, range));
    }

    return mapData;
}

long LookupValue(long value, List<(long source, long destination, long range)> mapData)
{
    foreach (var mapEntry in mapData)
    {
        if (mapEntry.source <= value && value < mapEntry.source + mapEntry.range)
        {
            return value - mapEntry.source + mapEntry.destination;
        }
    }

    return value;
}

long ProcessSeed(long seed)
{
    foreach (var map in Maps)
    {
        seed = LookupValue(seed, map);
    }

    return seed;
}