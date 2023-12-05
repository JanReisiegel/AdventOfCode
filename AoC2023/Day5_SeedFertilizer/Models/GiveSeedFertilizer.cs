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

        public GiveseedFertilizer(string input)
        {

            Maps = Regex.Split(input, @"(\n)+").Select(x=>new Map(x)).ToList();
        }
    }
}
