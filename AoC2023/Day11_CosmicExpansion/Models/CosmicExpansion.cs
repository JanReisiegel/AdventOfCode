using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day11_CosmicExpansion.Models
{
    public class CosmicExpansion
    {
        public Grid<char> Lines { get; set; }
        public List<Point> Points { get; set; }
        public int NumberOfGalaxies { get; set; } = 0;
        public CosmicExpansion(string[] linesInput)
        {
            var charList = linesInput.Select(line=>line.ToCharArray().ToList()).ToList();
            for (int i = 0; i < linesInput.Length; i++)
            {
                if (!charList[i].Any(x => x != '.'))
                {
                    charList.Insert(i, new string('.', linesInput[0].Length).ToCharArray().ToList());
                    i++;
                }
            }
            for (int i = 0;i < charList[0].Count; i++)
            {
                if(charList.All(row => row[i] == '.'))
                {
                    foreach (var c in charList)
                    {
                        c.Insert(i, '.');
                    }
                    i++;
                }
            }
            Lines = new Grid<char>(ConvertToStringArray(charList));
            NumberOfGalaxies = Lines.AmountOf('#');
        }

        private string[] ConvertToStringArray(List<List<char>> charList)
        {
            return charList.Select(x=>new string(x.ToArray())).ToArray();
        }

        public int PartOne()
        {
            for (int i = 0; i < NumberOfGalaxies; i++)
            {
                var found = false;
                for (int j = 0;j < Lines.VerticalLength && !found; j++)
                {
                    for (int k = 0; k < Lines.HorizontalLength && !found; k++)
                    {
                        if (Lines.Array[j, k] == '#')
                        {
                            found = true;
                            Lines.Array[j, k] = (char)('0' + i);
                        }
                    }
                }
            }
            int result = CalculatePath();
            return result;
        }

        private int CalculatePath()
        {
            int result = 0;
            List<(int,int)> alreadyBeen = new List<(int,int)> ();
            Dictionary<(int,int), int> cache = new Dictionary<(int,int), int>();
            for(int i = 0;i < NumberOfGalaxies; i++)
            {
                for(int j = 0; j < NumberOfGalaxies; j++)
                {
                    if (j != i && !alreadyBeen.Contains((i, j)))
                    {
                        alreadyBeen.Add((i, j));
                        int pathLength = cache.TryGetValue((i, j), out var cachedLength)
                            ? cachedLength 
                            : Lines.GetShortestPath((char)('0'+i), (char)('0'+j), Barrier);
                        cache[(i, j)] = pathLength;
                        result += pathLength;
                    }
                }
            }
            return result;
        }
        public bool Barrier(char c1, char c2)
        {
            return false;
        }
    }
}
