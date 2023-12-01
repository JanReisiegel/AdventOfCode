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
        private readonly List<string> numbers = new List<string>{ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9" };
        private Dictionary<string, int> myDict = new Dictionary<string, int> 
        {
            { "one", 1 },
            { "two", 2 },
            { "three", 3 },
            { "four", 4 },
            { "five",5 },
            { "six",6 },
            { "seven",7 },
            { "eight",8 },
            { "nine",9 }
        }; 
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
            /*for(int i = 0; i < InputLines.Count; i++)
            {
                myDict.Add(InputLines[i], CalibrationValues[i]);
            }*/
        }
        private void SearchNumbers(string input)
        {
            string pattern = @"("+ String.Join("|", numbers.Select(Regex.Escape)) + @")";
            MatchCollection matches = Regex.Matches(input, pattern, RegexOptions.IgnoreCase);
            List<int> results = matches.Cast<Match>()
                .Select(x =>
                {
                    if (myDict.ContainsKey(x.Value))
                    {
                        return myDict[x.Value];
                    }
                    else
                    {
                        return Int32.Parse(x.Value);
                    }
                })
                .ToList();
            
            CalibrationValues.Add(Int32.Parse(String.Concat(results.First(), results.Last())));
        } 

        public static async Task<string> ReadAll(CancellationToken cancellationToken = default)
        {
            var input = await Console.In.ReadToEndAsync();
            return input;
        }

        public string PrintTrebuchet()
        {
            var output = new StringBuilder();
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
