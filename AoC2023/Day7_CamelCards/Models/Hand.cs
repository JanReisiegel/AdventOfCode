using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Day7_CamelCards.Models
{
    public class Hand
    {
        public string Cards {  get; set; }
        public long Bid { get; set; }
        public int TypeOne { get; set; }
        public int TypeTwo { get; set; }

        public Hand(string cards, long bid)
        {
            Cards = cards;
            Bid = bid;
            TypeOne = HandTypeOne();
            TypeTwo = HandTypeTwo();
        }
        private int HandTypeOne()
        {
            Dictionary<char, int> Matches = new Dictionary<char, int>();
            foreach (char c in Cards)
            {
                if (Matches.ContainsKey(c))
                {
                    Matches[c] += 1;
                    continue;
                }
                Matches.Add(c, 1);
            }
            if(Matches.Count == 1) return (int)ClassType.FiveOfKind;
            if (Matches.Count == 5) return (int)ClassType.HighCard;
            int value = 0;
            foreach (var item in Matches)
            {
                if(item.Value == 4) return (int)ClassType.FourOfKind;
                if(item.Value == 3 && Matches.Count == 2) return (int)ClassType.FullHouse;
                if(item.Value == 3 && Matches.Count != 2) return (int)ClassType.ThreeOfKind;
                if(item.Value == 2 && Matches.Count == 3) return (int)ClassType.TwoPair;
                if(item.Value == 2 && Matches.Count == 4) return(int)ClassType.OnePair;
            }
            return (int)ClassType.HighCard;
        }
        public int HandTypeTwo()
        {
            Dictionary<char, int> Matches = new Dictionary<char, int>();
            foreach (char c in Cards)
            {
                if (Matches.ContainsKey(c))
                {
                    Matches[c] += 1;
                    continue;
                }
                Matches.Add(c, 1);
            }
            if (Matches.Count == 1) return (int)ClassType.FiveOfKind;
            if (Matches.ContainsKey('J'))
            {
                switch (Matches['J'])
                {
                    case 1:
                        if (Matches.Count == 2) return (int)ClassType.FiveOfKind;
                        if (Matches.Count == 3) return (int)ClassType.FourOfKind;
                        if (Matches.Count == 4) return (int)ClassType.ThreeOfKind;
                        if (Matches.Count == 5) return (int)ClassType.OnePair;
                        break;
                    case 2:
                        if (Matches.Count == 2) return (int)ClassType.FiveOfKind;
                        if (Matches.Count == 3) return (int)ClassType.FourOfKind;
                        if (Matches.Count == 4) return (int)ClassType.ThreeOfKind;
                        break;
                    case 3:
                        if (Matches.Count == 2) return (int)ClassType.FiveOfKind;
                        if (Matches.Count == 3) return (int)ClassType.FourOfKind;
                        break;
                    case 4:
                        return (int)ClassType.FiveOfKind;
                    case 5:
                        return (int)ClassType.FiveOfKind;
                    default:
                        break;
                }
            }
            int value = 0;
            foreach (var item in Matches)
            {
                if (item.Key == 'J') continue;
                //if (item.Value == 4 && Matches.ContainsKey('J')) return (int)ClassType.FiveOfKind;
                if (item.Value == 4) return (int)ClassType.FourOfKind;

                //if (item.Value == 3 && Matches.ContainsKey('J') && Matches['J'] == 2) return (int)ClassType.FiveOfKind;
                if (item.Value == 3 && Matches.Count == 2) return (int)ClassType.FullHouse;
                //if (item.Value == 3 && Matches.Count != 2 && Matches.ContainsKey('J')) return (int)ClassType.FourOfKind;
                if (item.Value == 3 && Matches.Count != 2) return (int)ClassType.ThreeOfKind;

                //if (item.Value == 2 && Matches.Count == 3 && Matches.ContainsKey('J') && Matches['J']==1) return (int)ClassType.FullHouse;
                //if (item.Value == 2 && Matches.Count == 3 && Matches.ContainsKey('J') && Matches['J'] == 2) return (int)ClassType.FourOfKind;
                if (item.Value == 2 && Matches.Count == 3) return (int)ClassType.TwoPair;
                if (item.Value == 2 && Matches.Count == 4) return (int)ClassType.OnePair;
            }
            return value;
        }
    }
    public enum ClassType
    {
        HighCard = 0,
        OnePair = 1,
        TwoPair = 2,
        ThreeOfKind = 3,
        FullHouse = 4,
        FourOfKind = 5,
        FiveOfKind = 6
    }
}
