using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Day6_WaitForIt.Models
{
    class WaitForIt
    {
        public List<long> Times { get; set; }
        public List<long> Distances { get; set; }

        public WaitForIt(string[] lines)
        {
            Times = Regex.Split(lines[0].Replace("\r",String.Empty), @"\W+").Skip(1).Select(long.Parse).ToList();
            Distances = Regex.Split(lines[1].Replace("\r", String.Empty), @"\W+").Skip(1).Select(long.Parse).ToList();
        }

        public long PartOne()
        {
            List<long> wins = new List<long>();
            foreach (var time in Times)
            {
                long win = 0;
                for (long i = 0; i <= time; i++)
                {
                    long distance = (time - i) * i;
                    if (distance > Distances[Times.IndexOf(time)])
                    {
                        win++;
                    }
                }
                
                wins.Add(win);
            }
            long result = 1;
            foreach (var win in wins)
            {
                result = result * win;
            }
            return result;
        }

        public long PartTwo()
        {
            long time = long.Parse(String.Join("", Times));
            long defDistance = long.Parse(String.Join("", Distances)); 
            long result = 0;
            for (long i = 0; i <= time; i++)
            {
                long distance = (time - i) * i;
                if (distance > defDistance)
                {
                    result++;
                }
            }
            return result;
        }
    }
}
