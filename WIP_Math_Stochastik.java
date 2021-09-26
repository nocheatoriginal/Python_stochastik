/// <Copyright> (c) 2021 nocheatoriginal
/// </Copyright>
public class Math_Stochastik
    {
        static void main(String[] args)
        {
            boolean running = true;

            while (running)
            {
                menu();
                System.out.print("Eingabe> ");
                String input = Console.ReadLine().ToString();

                if (input == "1")
                {
                    System.out.println("[1] fakultät(int zahl)");
                    System.out.print("Parameter eingeben >>> ");
                    String parameter = Console.ReadLine().ToString();
                    System.out.println(fakultät(parseInt(parameter.Split(',')[0])));
                }
                else if (input == "2")
                {
                    System.out.println("[2] potenz(double zahl, int hoch)");
                    System.out.print("Parameter eingeben >>> ");
                    String parameter = Console.ReadLine().ToString();
                    System.out.println(potenz(Double.parseDouble(parameter.Split(',')[0]), parseInt((parameter.Split(',')[1]))));
                }
                else if (input == "3")
                {
                    System.out.println("[3] binomialkoeffizient(int n, int k)");
                    System.out.print("Parameter eingeben >>> ");
                    String parameter = Console.ReadLine().ToString();
                    System.out.println(binomialkoeffizient(parseInt(parameter.Split(',')[0]), parseInt((parameter.Split(',')[1]))));
                }
                else if (input == "4")
                {
                    System.out.println("[4] bernouliFormel(double p, int n, int k)");
                    System.out.print("Parameter eingeben >>> ");
                    String parameter = Console.ReadLine().ToString();
                    System.out.println(bernouliFormel(Double.parseDouble(parameter.Split(',')[0]), parseInt(parameter.Split(',')[1]), parseInt((parameter.Split(',')[2]))));
                }
                else if (input == "5")
                {
                    System.out.println("[5] binomCdf(int n, double p, int untereGrenze, int obereGrenze)");
                    System.out.print("Parameter eingeben >>> ");
                    String parameter = Console.ReadLine().ToString();
                    System.out.println(binomCdf(parseInt(parameter.Split(',')[0]), Double.parseDouble(parameter.Split(',')[1]), parseInt(parameter.Split(',')[2]), parseInt((parameter.Split(',')[3]))));
                }
                else if (input == "6")
                {
                    System.out.println("[6] dezimalzahl(int zähler, int nenner)");
                    System.out.print("Parameter eingeben >>> ");
                    String parameter = Console.ReadLine().ToString();
                    System.out.println(dezimalzahl(parseInt(parameter.Split(',')[0]), parseInt((parameter.Split(',')[1]))));
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
            System.out.println("Menu\n-----");
            System.out.println("[1] fakultät(int zahl)");
            System.out.println("[2] potenz(double zahl, int hoch)");
            System.out.println("[3] binomialkoeffizient(int n, int k)");
            System.out.println("[4] bernouliFormel(double p, int n, int k)");
            System.out.println("[5] binomCdf(int n, double p, int untereGrenze, int obereGrenze)");
            System.out.println("[6] dezimalzahl(int zähler, int nenner)");
            System.out.println("clear");
            System.out.println("exit\n-----");
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
