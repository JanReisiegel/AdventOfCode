using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day2_CubeConundrum.Models
{
    class CubeConundrum
    {
        public List<Game> Games { get; private set; } = new List<Game>();
        public int SumOfPosGames {  get; private set; }
        public long PowerOfGames { get; private set; } = 0;

        public CubeConundrum(string input, Dictionary<string, int> conditions)
        {
            string[] lines = input.Split("\n");
            foreach (string line in lines)
            {
                Games.Add(new Game(line));
            }
            UpdateSumOfPos(conditions);
            foreach (var game in Games)
            {
                PowerOfGames = PowerOfGames + game.PowerOfGame;
            }
        }

        private void UpdateSumOfPos(Dictionary<string, int> conditions)
        {
            foreach (var game in Games)
            {
                if (game.IsPossible(conditions))
                {
                    SumOfPosGames += game.Id;
                }
            }
        }
    }
}
