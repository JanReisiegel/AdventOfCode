using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day9_MirageMaintenance.Models
{
    class MirageMaintenance
    {
        public List<History> Histories { get; set; }

        public MirageMaintenance(List<string> input)
        {
            Histories = input.Select(x=>new History(x)).ToList();
        }

        public long PartOne()
        {
            long result = 0;
            foreach(History history in Histories)
            {
                result += history.NextNumber;
            }
            return result;
        }
        public long PartTwo()
        {
            long result = 0;
            foreach (History history in Histories)
            {
                result += history.PreviousNumber;
            }
            return result; //Histories.Sum(x => x.PreviousNumber);
        }
    }
}
