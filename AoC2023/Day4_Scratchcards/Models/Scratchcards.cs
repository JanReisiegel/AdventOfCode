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
        
        public int GetGameValue()
        {
            int value = 0;
            foreach (var card in CardsLines)
            {
                value += card.GetCardValue();
            }
            return value;
        }
        public int GetScratchcardsNumber()
        {
            var counts = CardsLines.Select(x=>x.Matches).ToList();
            for(int i = 0; i < CardsLines.Count; i++)
            {
                var (card, count) = (CardsLines[i], counts[i]);
                for(int j = 0; j < card.Matches; j++)
                {
                    counts[i + j + 1] += count;
                }
            }
            return counts.Sum();
        }
    }
}
