using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <Copyright> (c) 2021 nocheatoriginal
/// </Copyright>
namespace Math_Stochastik
{
    class Program
    {
        static void Main(string[] args)
        {
            bool running = true;

            while (running)
            {
                menu();
                Console.Write("Eingabe> ");
                string input = Console.ReadLine().ToString();

                if (input == "1")
                {
                    Console.WriteLine("[1] fakultät(int zahl)");
                    Console.Write("Parameter eingeben >>> ");
                    string parameter = Console.ReadLine().ToString();
                    Console.WriteLine(fakultät(Convert.ToInt32(parameter.Split(',')[0])));
                }
                else if (input == "2")
                {
                    Console.WriteLine("[2] potenz(double zahl, int hoch)");
                    Console.Write("Parameter eingeben >>> ");
                    string parameter = Console.ReadLine().ToString();
                    Console.WriteLine(potenz(Convert.ToDouble(parameter.Split(',')[0]), Convert.ToInt32((parameter.Split(',')[1]))));
                }
                else if (input == "3")
                {
                    Console.WriteLine("[3] binomialkoeffizient(int n, int k)");
                    Console.Write("Parameter eingeben >>> ");
                    string parameter = Console.ReadLine().ToString();
                    Console.WriteLine(binomialkoeffizient(Convert.ToInt32(parameter.Split(',')[0]), Convert.ToInt32((parameter.Split(',')[1]))));
                }
                else if (input == "4")
                {
                    Console.WriteLine("[4] bernouliFormel(double p, int n, int k)");
                    Console.Write("Parameter eingeben >>> ");
                    string parameter = Console.ReadLine().ToString();
                    Console.WriteLine(bernouliFormel(Convert.ToDouble(parameter.Split(',')[0]), Convert.ToInt32(parameter.Split(',')[1]), Convert.ToInt32((parameter.Split(',')[2]))));
                }
                else if (input == "5")
                {
                    Console.WriteLine("[5] binomCdf(int n, double p, int untereGrenze, int obereGrenze)");
                    Console.Write("Parameter eingeben >>> ");
                    string parameter = Console.ReadLine().ToString();
                    Console.WriteLine(binomCdf(Convert.ToInt32(parameter.Split(',')[0]), Convert.ToDouble(parameter.Split(',')[1]), Convert.ToInt32(parameter.Split(',')[2]), Convert.ToInt32((parameter.Split(',')[3]))));
                }
                else if (input == "6")
                {
                    Console.WriteLine("[6] dezimalzahl(int zähler, int nenner)");
                    Console.Write("Parameter eingeben >>> ");
                    string parameter = Console.ReadLine().ToString();
                    Console.WriteLine(dezimalzahl(Convert.ToInt32(parameter.Split(',')[0]), Convert.ToInt32((parameter.Split(',')[1]))));
                }
                else if (input == "clear")
                {
                    Console.Clear();
                }
                else if (input == "exit")
                {
                    running = false;
                }
            }

        }

        static void menu()
        {
            Console.WriteLine("Menu\n-----");
            Console.WriteLine("[1] fakultät(int zahl)");
            Console.WriteLine("[2] potenz(double zahl, int hoch)");
            Console.WriteLine("[3] binomialkoeffizient(int n, int k)");
            Console.WriteLine("[4] bernouliFormel(double p, int n, int k)");
            Console.WriteLine("[5] binomCdf(int n, double p, int untereGrenze, int obereGrenze)");
            Console.WriteLine("[6] dezimalzahl(int zähler, int nenner)");
            Console.WriteLine("clear");
            Console.WriteLine("exit\n-----");
        }

        static int fakultät(int zahl)
        {
            int ergebnis = zahl;
            if (zahl == 0)
            {
                return 1;
            }
            else
            {
                while (zahl > 1)
                {
                    ergebnis *= (zahl - 1);
                    zahl -= 1;
                }
                return ergebnis;
            }
        }

        static double potenz(double zahl, int hoch)
        {
            if (hoch == 0)
            {
                return 1;
            }
            else if (hoch < 0)
            {
                int positivhoch = hoch * -1;
                double ergebnis = zahl;
                for (int i = 0; i <= positivhoch -1; i++)
                {
                    ergebnis *= zahl;
                }
                return 1 / ergebnis;
            }
            else
            {
                double ergebnis = zahl;
                for (int i = 0; i <= hoch - 1; i++)
                {
                    ergebnis *= zahl;
                }
                return ergebnis;
            }
        }

        static double binomialkoeffizient(int n, int k)
        {
            if (k == 0)
            {
                return 1;
            }
            else if (k > n || k < 0 || n < 0)
            {
                return 0;
            }
            else
            {
                return fakultät(n) / (fakultät(k) * fakultät(n - k));
            }
        }

        static double bernouliFormel(double p, int n, int k)
        {
            return potenz(p, k) * potenz((1-p), (n - k)) * binomialkoeffizient(n, k);
        }

        static double binomCdf(int n, double p, int untereGrenze, int obereGrenze)
        {
            double ergebnis = 0;

            while (!(untereGrenze > obereGrenze))
            {
                ergebnis += bernouliFormel(p, n, untereGrenze);
                untereGrenze++;
            }
            return ergebnis;
        }

        static double dezimalzahl(int zähler, int nenner)
        {
            return zähler / nenner;
        }
    }
}
