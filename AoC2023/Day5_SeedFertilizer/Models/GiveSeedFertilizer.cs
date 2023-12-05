using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Day5_SeedFertilizer.Models
{
    class GiveseedFertilizer
    {
        public List<Map> Maps { get; set; }
        public List<long> SeedsData { get; set; }
         public long MinimumResult { get; set; }

        public GiveseedFertilizer(string input)
        {
            var modInput = input.Replace("\r", String.Empty).Split("\n").ToList();
            SeedsData = modInput[0].Split(" ").Skip(1).Select(long.Parse).ToList();
            Maps = modInput.Skip(1).Select(x=> new Map(x)).ToList();
            MinimumResult = SeedsData.Min(x => ProcessSeed(x));
        }

        private long ProcessSeed(long seed)
        {
            foreach(var map in Maps)
            {
                seed = LookupValue(seed, map.Lines);
            }
            return seed;
        }

        private long LookupValue(long value, List<Line> mapLines)
        {
            foreach(var line in mapLines)
            {
                if(line.SourceRangeStart <= value && value < line.SourceRangeStart + line.RangeLength)
                {
                    return value - line.SourceRangeStart + line.DestinationRangeStart;
                }
            }
            return value;
        }
    }
}
