using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Tinkoff.Trading.OpenApi.Network;

namespace Тиньков
{
    class Program
    {
        static void Main(string[] args)
        {
            var token = "t.FeAhvntO9rW0Xez_WkisBwCr-yQ3mcPXfPh6zTzJcuULXWJ9mdoDpM7eROHzv-tTePBx8LLkSKJvxszjXhK2gw";
            var connection = ConnectionFactory.GetSandboxConnection(token); 
            var context = connection.Context;
            var portfolion = context.PortfolioAsync();
            var t = context.MarketCurrenciesAsync();
            var t1 = context.MarketSearchByTickerAsync("AMD");
            var cand = context.MarketCandlesAsync("BBG000BBQCY0", new DateTime(2020, 07, 15), new DateTime(2020, 07, 16), Tinkoff.Trading.OpenApi.Models.CandleInterval.Hour);
            cand.Wait();

        }
    }
}