using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Day4_Scratchcards.Models
{
    class Card
    {
        public string Text { get; private set; }
        public List<int> WinningNumbers { get; private set; }
        public List<int> MyNumbers { get; private set; }
        public int CardValue { get { return GetCardValue(); } }
        public int Matches {  get; private set; }

        public Card(string text)
        {
            Text = text.Replace("\r", String.Empty);
            GetNumbers();
            string[] text1 = text.Split(':','|');
            var l = Regex.Matches(text1[1], @"\d+").Select(x => x.Value);
            var r = Regex.Matches(text1[2], @"\d+").Select(x => x.Value);
            Matches = l.Intersect(r).Count();
        }

        private void GetNumbers()
        {
            string temp = Text;
            string pattern = @".+: ";
            temp = Regex.Replace(temp, pattern, String.Empty);
            List<string> temp2 = temp.Split(" | ").ToList();
            temp2[0] = temp2[0].Trim();
            if (temp2[0].StartsWith(" "))
            {
                temp2[0].Remove(0, 1);
            }
            WinningNumbers = Regex.Split(temp2[0],@"\W+").Select(x=>int.Parse(x)).ToList();
            MyNumbers = Regex.Split(temp2[1], @"\W+").Select(x => { if(x != String.Empty) { return int.Parse(x); }else { return 0; } }).ToList();
        }

        public int GetCardValue()
        {
            int iter = 0;
            foreach(var i in WinningNumbers)
            {
                if (MyNumbers.Contains(i))
                {
                    iter++;
                }
            }
            int result = (int)Math.Pow(2,iter-1);
            return result;
        }
    }
}
