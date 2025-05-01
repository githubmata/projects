using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using System.IO;
using System.Text;


internal class Program
{
    static void Main(string[] args)
    {
      string inputStr = "Man, I need a new job!";
      
      int index = inputStr.Length - 1;
      string revString = " ";
      
      while(index >= 0)
      {
        revString = revString + inputStr[index];
        index--;
      }
      
      Console.WriteLine($"Reversted string: {revString}");

    }
}

