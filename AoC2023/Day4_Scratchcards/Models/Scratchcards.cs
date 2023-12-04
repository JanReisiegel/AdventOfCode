using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Day4_Scratchcards.Models
{
    class Scratchcards
    {
        public List<Card> CardsLines { get; set; }
        public List<int> WinningNumbers { get; set; }
        public List<int> MyNumbers { get; set; }

        public Scratchcards(string input)
        {
            CardsLines = input.Split('\n').Select(x => new Card(x)).ToList();
        }
        
        public double GetGameValue()
        {
            double value = 0;
            foreach (var card in CardsLines)
            {
                value += card.GetCardValue();
            }
            return value;
        }
    }
}
