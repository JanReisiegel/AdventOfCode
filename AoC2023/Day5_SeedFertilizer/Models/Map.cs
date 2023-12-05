using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day5_SeedFertilizer.Models
{
    class Map
    {
        public string Name { get; set; }
        public List<Line> Lines { get; set; }
        public List<int> Seeds { get; set; } = new List<int>();
        public Map(string input)
        {
            var inString = input.Split(":\n").ToList();
            Name = inString[0];
            Lines = inString[1].Split("\n").Select(x => new Line(x)).ToList();
            CalculateSeed();
        }
        private void CalculateSeed()
        {
             
        }
    }
}
