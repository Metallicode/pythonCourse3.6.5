using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class test
    {
        /// <summary>
        /// function overloading
        /// </summary>

        public void testFunction()
        {
            Console.WriteLine("Hello from testFunction()");
        }


        public void testFunction(int num)
        {
            Console.WriteLine("Hello from testFunction(int num)");
        }


        public void testFunction(int num1, int num2)
        {
            Console.WriteLine("Hello from testFunction(int num, int num2)");
        }

    }
}
