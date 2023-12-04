using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day3_GearRatios.Models
{
    class Part
    {
        public string Text { get; set; }
        public int Row { get; set; }
        public int Col { get; set; }

        public Part(string text, int row, int col)
        {
            Text = text;
            Row = row;
            Col = col;
        }

        public int GetCislo()
        {
            int.TryParse(Text, out var cislo);
            return cislo;
        }
    }
}
