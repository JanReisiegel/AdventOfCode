using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day8_HauntedWasteland.Models
{
    public class Node
    {
        public string Left { get; set; } 
        public string Right {  get; set; }
        public Node(string left, string right)
        {
            Right = right;
            Left = left;
        }

    }
}
