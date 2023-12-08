using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Day8_HauntedWasteland.Models
{
    public class HauntedWasteland
    {
        public Dictionary<string, Node> Nodes { get; set; } = new Dictionary<string, Node>();
        public string Key { get; set; }
        public string Start {  get; set; } = "AAA";
        public List<string> Starts { get; set; } = new List<string>();
        public string Destination { get; set; } = "ZZZ";

        public HauntedWasteland(List<string> lines)
        {
            Key = Regex.Replace(lines[0], @"[^RL]", String.Empty);
            foreach (var line in lines.Skip(2))
            {
                var items = Regex.Split(line, @"\W+").ToList();
                Nodes.Add(items[0], new Node(items[1], items[2]));
                if (items[0].EndsWith('A')) 
                { 
                    Starts.Add(items[0]); 
                }
            }
        }
        public long PartOne()
        {
            long steps = 0;
            string node = Start;
            while (true)
            {
                int index = int.Parse($"{steps % Key.Length}");
                char nextNode = Key[index];
                if(nextNode == 'R')
                {
                    node = Nodes[node].Right; 
                }
                else
                {
                    node = Nodes[node].Left;
                }
                steps++;
                if(node == Destination) return steps;
            }
        }

        public long PartTwo()
        {
            long steps = 0;
            List<string> nodes = Starts.ToList();
            while (true)
            {
                int ends = 0;
                int keyIndex = int.Parse($"{steps % Key.Length}");
                char nextNode = Key[keyIndex];
                for (int i = 0; i < Starts.Count; i++)
                {
                    if(nextNode == 'R')
                    {
                        nodes[i] = Nodes[nodes[i]].Right;
                    }
                    else
                    {
                        nodes[i] = Nodes[nodes[i]].Left;
                    }
                    if (nodes[i].EndsWith('Z')) ends++;
                }
                steps++;
                if(ends == Starts.Count) return steps;
            }
        }
    }
}
