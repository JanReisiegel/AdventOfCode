using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Day1_Trebuchet.Models
{
    internal class Trebuchet
    {
        private readonly List<string> numbers = new List<string>{ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
        private readonly List<string> numbers2 = new List<string> { "o1e", "t2o", "th3ee", "fo4r", "fi5e", "s6x", "se7en", "ei8ht", "ni9e" };
        private Dictionary<string, int> myDict = new Dictionary<string, int>(); 
        private List<string> inputLines;
        public List<string> InputLines { get { return inputLines; } set { inputLines = value; GetCalibrationValues(); } }
        public List<int> calibrationValues = new List<int>();
        public List<int> CalibrationValues { get { return calibrationValues; } set {  calibrationValues = value; } }
        public Trebuchet(string input)
        {
            InputLines = input.Split("\n").ToList();
        }

        private void GetCalibrationValues()
        {
            foreach (string line in InputLines)
            {
                if(string.IsNullOrEmpty(line)) continue;
                SearchNumbers(line);
            }
        }
        private void SearchNumbers(string input)
        {
            string pattern = @"("+ String.Join("|", numbers.Select(Regex.Escape)) + @")";
            MatchCollection matches = Regex.Matches(input, pattern, RegexOptions.IgnoreCase);
            List<int> nalezenaCisla = matches.Cast<Match>().Select(x=>numbers.IndexOf(x.Value.ToLower())+1).ToList();
            foreach(int num in nalezenaCisla)
            {
                input = input.Replace(numbers[num - 1], numbers2[num-1]);
            }
            string[] resNumb = new string[2];
            pattern = @"\D+";
            input = Regex.Replace(input, pattern, String.Empty);
            List<char> tempValues = input.ToCharArray().ToList();
            resNumb[0] = String.IsNullOrEmpty(tempValues.First().ToString()) ? tempValues[1].ToString() : tempValues.First().ToString();
            resNumb[1] = String.IsNullOrEmpty(tempValues.Last().ToString()) ? tempValues[tempValues.Count - 2].ToString() : tempValues.Last().ToString();
            CalibrationValues.Add(Int32.Parse(String.Concat(resNumb)));
        } 

        public static async Task<string> ReadAll(CancellationToken cancellationToken = default)
        {
            var input = await Console.In.ReadToEndAsync();
            return input;
        }

        public string PrintTrebuchet()
        {
            var output = new StringBuilder();
            /*foreach(string line in InputLines)
            {
                output.AppendLine(line);
            }*/
            BigInteger integer = 0;
            foreach(var i in CalibrationValues)
            {
                integer += i;
            }
            output.AppendLine($"vysledek: {integer}");
            return output.ToString();
        }
    }
}
