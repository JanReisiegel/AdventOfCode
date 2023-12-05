using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day5_SeedFertilizer.Models
{
    public class Line
    {
        public long SourceRangeStart {  get; set; }
        public long DestinationRangeStart { get; set; }
        public long RangeLength {  get; set; }
        

        public Line(string input)
        {
            var numbers = input.Replace("\r", String.Empty).Split(" ").ToList();
            DestinationRangeStart = long.Parse(numbers[0]);
            SourceRangeStart = long.Parse(numbers[1]);
            RangeLength = long.Parse(numbers[2]);
        }

        public List<long> GetCorresponds()
        {
            List<long> result = new List<long>();
            for(int i = 0;i<RangeLength;i++)
            {
                result.Add(DestinationRangeStart + i);
            }
            return result;
        }
    }
}