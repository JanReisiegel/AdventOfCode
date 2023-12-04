using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Day3_GearRatios.Models
{
    class GearRatios
    {
        public List<string> EngineSchematic { get; private set; }

        public List<int> PartNumbers { get; private set; } = new List<int>();
        public List<int> GearNumbers { get; private set; } = new List<int>();
        public int SumPartNumbers { get; private set; }
        public int SumGearNumbers { get; private set; }

        public GearRatios(string input)
        {
            string text = input.Replace("\r",String.Empty);
            EngineSchematic = text.Split("\n").ToList();
            GetPartNumbers();
        }

        public void GetPartNumbers()
        {
            var symbols = ParseSymbols(new Regex(@"[^.0-9]"));
            var numbers = ParseSymbols(new Regex(@"\d+"));
            PartNumbers = numbers.Where(x=>symbols.Any(s=>Adjacent(s,x))).Select(x=>x.GetCislo()).ToList();
            SumPartNumbers = PartNumbers.Sum();

            var gears = ParseSymbols(new Regex(@"\*"));
            foreach (var gear in gears)
            {
                List<int> adjacentNumbers = new List<int>();
                foreach (var number in numbers)
                {
                    if(Adjacent(number, gear))
                    {
                        adjacentNumbers.Add(number.GetCislo());
                    }
                }
                if(adjacentNumbers.Count == 2)
                {
                    GearNumbers.Add(adjacentNumbers.First() * adjacentNumbers.Last());
                }
            }
            SumGearNumbers = GearNumbers.Sum();
        }

        private List<Part> ParseSymbols(Regex rx)
        {
            List<Part> parts = new List<Part>();
            IEnumerable<int> iRows = Enumerable.Range(0, EngineSchematic.Count);
            foreach (var iRow in iRows)
            {
                var parts2 = rx.Matches(EngineSchematic[iRow]);
                foreach(Match item in parts2)
                {
                    parts.Add(new Part(item.Value, iRow, item.Index));
                }
            }

            return parts;
        }

        private bool Adjacent(Part p1, Part p2)
        {
            return Math.Abs(p2.Row - p1.Row) <= 1 &&
                p1.Col <= p2.Col + p2.Text.Length &&
                p2.Col <= p1.Col + p1.Text.Length;
        }
    }
}
