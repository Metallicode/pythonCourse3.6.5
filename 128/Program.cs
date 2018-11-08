using System;
using System.IO;
using System.Net;


namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello from c# subProcess!");
            string url = args[0];
            WebClient webClient = new WebClient();
            string downloadString = webClient.DownloadString(url);

            string cDir = Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);
            File.WriteAllText(cDir + "\\webPage.html", downloadString);
            Console.WriteLine("c# subProcess Exit...");

        }
    }
}
