using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day7_CamelCards.Models
{
    public class CamelCards
    {
        private readonly Dictionary<char, int> cards = new Dictionary<char, int>
        {
            {'2' , 2 },
            {'3' , 3 },
            {'4' , 4 },
            {'5' , 5 },
            {'6' , 6 },
            {'7' , 7 },
            {'8' , 8 },
            {'9' , 9 },
            {'T' , 10 },
            {'J' , 11 },
            {'Q' , 12 },
            {'K' , 13 },
            {'A' , 14 }
        };

        public Dictionary<string, int> Hands { get; set; } = new Dictionary<string, int>();
        
        public CamelCards(List<string> input)
        {
            input.ForEach(x =>
            {
                var help = x.Split(" ");
                Hands.Add(help[0], int.Parse(help[1].Replace("\r", String.Empty)));
            });
        }


    }
}
