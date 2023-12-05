using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day5_SeedFertilizer.Models
{
    class Map
    {
        public List<Line> Lines { get; set; }
        public Map(string input)
        {
            Lines = input.Split("\n").Skip(1).Select(x => new Line(x)).ToList();
        }
    }
}
