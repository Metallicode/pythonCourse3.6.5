using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            test t = new test();

            t.testFunction();
            t.testFunction(1);
            t.testFunction(1,2);

            Console.Read();

        }
    }
}
