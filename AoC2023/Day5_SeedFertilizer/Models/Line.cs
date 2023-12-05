using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day5_SeedFertilizer.Models
{
    public class Line
    {
        public int SourceRangeStart {  get; set; }
        public int DestinationRangeStart { get; set; }
        public int RangeLength {  get; set; }

        public Line(string input)
        {
            var numbers = input.Replace("\r", String.Empty).Split(" ").ToList();
            DestinationRangeStart = int.Parse(numbers[0]);
            SourceRangeStart = int.Parse(numbers[1]);
            RangeLength = int.Parse(numbers[2]);
        }

        public List<int> GetCorresponds()
        {
            List<int> result = new List<int>();
            for(int i = 0;i<RangeLength;i++)
            {
                result.Add(DestinationRangeStart + i);
            }
            return result;
        }
    }
}