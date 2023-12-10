using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day10_PipeMaze.Models
{
    public class PipeMaze
    {
        public string[] Text { get; set; }
        private readonly char startSymbol = 'S';
        private readonly List<int[]> directions = new List<int[]> { new int[] { 0, 1 }, new int[] { 1, 0 }, new int[] { 0, -1 }, new int[] { -1, 0 } };
        private readonly string[] happyChars = new string[] { "-7J", "|LJ", "-FL", "|F7" };
        private readonly Dictionary<(int, char), int> directTransformation = new Dictionary<(int, char), int>
        {
            { (0, '-'), 0 },
            { (0, '7'), 1 },
            { (0, 'J'), 3 },
            { (2, '-'), 2 },
            { (2, 'F'), 1 },
            { (2, 'L'), 3 },
            { (1, '|'), 1 },
            { (1, 'L'), 0 },
            { (1, 'J'), 2 },
            { (3, '|'), 3 },
            { (3, 'F'), 0 },
            { (3, '7'), 2 }
        };
        public PipeMaze(string[] input)
        {
            Text = input;
        }

        public long PartOne()
        {
            int[] startPosition = FindStartPossition();
            List<int> validDirections = GetValidDirections(startPosition);
            int result = CalculatePathLength(startPosition, validDirections);
            return result;
        }
        public int PartTwo()
        {
            int[] startPosition = FindStartPossition();
            var validDirections = GetValidDirections(startPosition);
            return CalculateInnerPathCount(startPosition, validDirections);
        }

        private int CalculateInnerPathCount(int[] startPosition, List<int> validDirections)
        {
            int rows = Text.Length;
            int cols = Text[0].Length;
            List<int[]> output = new List<int[]>();
            for (int i = 0; i < rows; i++)
            {
                output.Add(new int[cols]);
            }
            bool isValidDirections = validDirections.Contains(3);

            int currentDirection = validDirections[0];
            int currentX = startPosition[0] + directions[currentDirection][0];
            int currentY = startPosition[1] + directions[currentDirection][1];
            int pathLength = 1;
            output[startPosition[0]][startPosition[1]] = 1;

            while(currentX != startPosition[0] && currentY != startPosition[1])
            {
                output[currentX][currentY] = 1;
                pathLength++;
                currentDirection = directTransformation[(currentDirection, Text[currentX][currentY])];
                currentX += directions[currentDirection][0];
                currentY += directions[currentDirection][1];
            }

            int count = 0;
            for (int i = 0; i < rows; i++)
            {
                bool inside = false;
                for (int j = 0; j < cols; j++)
                {
                    if (output[i][j] != 0)
                    {
                        if ("|JL".Contains(Text[i][j]) || (Text[i][j] == startSymbol && isValidDirections)) inside = !inside;
                    }
                    else if (inside)
                    {
                        count++;
                    }
                }
            }
            return count;
        }

        private int CalculatePathLength(int[] startPosition, List<int> validDirections)
        {
            int currentDirection = validDirections[0];
            int currentX = startPosition[0] + directions[currentDirection][0];
            int currentY = startPosition[1] + directions[currentDirection][1];
            int pathLength = 1;
            while (currentX != startPosition[0] && currentY != startPosition[1])
            {
                pathLength++;
                currentDirection = directTransformation[(currentDirection, Text[currentX][currentY])];
                currentX += directions[currentDirection][0];
                currentY += directions[currentDirection][1];
            }
            return pathLength/2;
        }

        private List<int> GetValidDirections(int[] startPosition)
        {
            List<int> validDirections = new List<int>();
            for (int i = 0; i < happyChars.Length; i++)
            {
                int[] position = directions[i];
                int nextX = startPosition[0] + position[0];
                int nextY = startPosition[1] + position[1];
                if(nextX >= 0 && nextX < Text.Length && nextY >= 0 && nextY < Text[0].Length && happyChars[i].Contains(Text[nextX][nextY])) 
                {
                    validDirections.Add(i);
                }
            }
            return validDirections;
        }

        public int[] FindStartPossition()
        {
            for (int i = 0; i < Text.Length; i++)
            {
                int index = Text[i].IndexOf(startSymbol);
                if(index != -1) return new int[] { i, index};
            }
            return new int[] { -1, -1 };
        }


    }
}
