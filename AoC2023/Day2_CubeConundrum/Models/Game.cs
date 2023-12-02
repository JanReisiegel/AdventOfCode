using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Day2_CubeConundrum.Models
{
    internal class Game
    {
        public int Id { get; set; }
        public List<Dictionary<string,int>> Sets { get; set; } = new List<Dictionary<string,int>>();

        public long PowerOfGame { get; set; } = 1;

        public Game(string input)
        {
            input = input.Replace("\r", String.Empty);
            string[] inputParams = input.Split(": ");
            Id = int.Parse(inputParams[0].Split(" ")[1]);
            string[] sets = inputParams[1].Split(";");
            foreach (var set in sets)
            {
                string[] sets2 = set.Split(',');
                Dictionary<string, int> setDict = new Dictionary<string, int>();
                foreach (string s in sets2)
                {
                    
                    string s1 = "";
                    if(s.StartsWith(" "))
                    {
                        s1 = s.Substring(1);
                    }
                    else if (s.EndsWith(" "))
                    {
                        s1 = s.Substring(0, s.Length - 1);
                    }
                    else
                    {
                        s1 = s;
                    }
                    string[] color = s1.Split(" ");
                    setDict.Add(color[1], int.Parse(color[0]));
                }
                Sets.Add(setDict);
            }
            PowerOfGame = 1;
            UpdatePowerOfGame();
        }

        public bool IsPossible(Dictionary<string, int> conditions)
        {
            foreach (var set in Sets)
            {
                foreach(var condition in conditions)
                {
                    if (set.ContainsKey(condition.Key))
                    {
                        if (condition.Value < set[condition.Key]) return false;
                    }
                }
            }
            return true;
        }

        private void UpdatePowerOfGame()
        {
            Dictionary<string, int> cubes = new Dictionary<string, int>
            {
                { "red", 0 },
                { "green", 0 },
                { "blue", 0 }
            };
            foreach (var set in Sets)
            {
                foreach (var cube in cubes)
                {
                    if(set.ContainsKey(cube.Key))
                    {
                        if(cube.Value < set[cube.Key])
                        {
                            cubes[cube.Key] = set[cube.Key];
                            continue;
                        }
                    }
                }
            }
            foreach (var cube in cubes)
            {
                PowerOfGame = PowerOfGame * cube.Value;
            }

        }
    }
}
