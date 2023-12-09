using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day9_MirageMaintenance.Models
{
    public class History
    {
        public List<long> Numbers {  get; set; }
        public List<List<long>> Differences { get; set; } = new List<List<long>>();
        public long NextNumber { get { return GetNextNumber(); } }
        public long PreviousNumber { get { return GetPreviousNumber(); } }

        public History(string numbers)
        {
            Numbers = numbers.Replace("\r", String.Empty).Split(" ").Select(long.Parse).ToList();
            bool _continnue = true;
            List<long> numForDiff = Numbers;
            while(_continnue)
            {
                List<long> differenc = new List<long>();
                for (int i = 1; i < numForDiff.Count; i++)
                {
                    differenc.Add(numForDiff[i] - numForDiff[i-1]);
                }
                Differences.Add(differenc);
                if (differenc.Sum(x=>Math.Abs(x)) == 0)
                {
                    _continnue = false;
                }
                numForDiff = differenc;
            }
        }
        private long GetNextNumber()
        {
            Differences.Last().Add(0);
            for (int i = Differences.Count - 2; i>=0; i--)
            {
                long lastNumber = Differences[i].Last();
                Differences[i].Add(lastNumber + Differences[i+1].Last());
            }
            long result = Numbers.Last() + Differences.First().Last();
            return result;
        }
        private long GetPreviousNumber()
        {
            Differences.Last().Insert(0, 0);
            for(int i = Differences.Count - 2; i>=0; i--)
            {
                long firstNumber = Differences[i].First();
                Differences[i].Insert(0, firstNumber - Differences[i+1].First());
            }
            long result = Numbers.First() - Differences.First().First();
            return result;
        }
    }
}
