using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day7_CamelCards.Models
{
    public class CamelCards
    {
        private readonly Dictionary<char, int> cardsOne = new Dictionary<char, int>
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
        private readonly Dictionary<char, int> cardsTwo = new Dictionary<char, int>
        {
            {'J' , 1 },
            {'2' , 2 },
            {'3' , 3 },
            {'4' , 4 },
            {'5' , 5 },
            {'6' , 6 },
            {'7' , 7 },
            {'8' , 8 },
            {'9' , 9 },
            {'T' , 10 },
            {'Q' , 11 },
            {'K' , 12 },
            {'A' , 13 }
        };

        public List<Hand> HandsOne { get; set; } = new List<Hand>();
        public List<Hand> HandsTwo { get; set; } = new List<Hand>();

        public CamelCards(List<string> input)
        {
            HandsOne = input.Select(x =>
            {
                var help = x.Split(" ");
                return new Hand(help[0], long.Parse(help[1]));
            }).ToList();
            HandsTwo = input.Select(x =>
            {
                var help = x.Split(" ");
                return new Hand(help[0], long.Parse(help[1]));
            }).ToList();
        }

        public long PartOne()
        {
            HandsOne.Sort((Hand h1, Hand h2) =>
            {
                if (h1.TypeOne < h2.TypeOne)
                {
                    return -1;
                }
                else if (h1.TypeOne > h2.TypeOne)
                {
                    return 1;
                }
                else
                {
                    for (int i = 0; i < h1.Cards.Length; i++)
                    {
                        if (cardsOne[h1.Cards[i]] < cardsOne[h2.Cards[i]])
                        {
                            return -1;
                        }
                        else if (cardsOne[h1.Cards[i]] > cardsOne[h2.Cards[i]])
                        {
                            return 1;
                        }
                    }
                }
                return 0;
            });
            long result = 0;
            for (int i = 0;i < HandsOne.Count;i++)
            {
                result += (HandsOne[i].Bid * (i + 1));
            }
            return result;
        }
        
        public long PartTwo()
        {
            HandsTwo.Sort((Hand h1, Hand h2) =>
            {
                if (h1.TypeTwo < h2.TypeTwo)
                {
                    return -1;
                }
                else if (h1.TypeTwo > h2.TypeTwo)
                {
                    return 1;
                }
                else
                {
                    for (int i = 0; i < h1.Cards.Length; i++)
                    {
                        if (cardsTwo[h1.Cards[i]] < cardsTwo[h2.Cards[i]])
                        {
                            return -1;
                        }
                        else if (cardsTwo[h1.Cards[i]] > cardsTwo[h2.Cards[i]])
                        {
                            return 1;
                        }
                    }
                }
                return 0;
            });
            long result = 0;
            for (int i = 0; i < HandsTwo.Count; i++)
            {
                result += (HandsTwo[i].Bid * (i + 1));
            }
            return result;
        }
    }
}
