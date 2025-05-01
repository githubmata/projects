using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using System.IO;
using System.Text;


  internal class Program
  {
    //Method used to accept the string value and 'args' variable to store strings passed to program when run
    static void Main(string[] args)
    {
      //input string
      string input = "123456789";
      
      //Convert to lower case
      input = input.ToLower();
      
      //initialize variable of left most (first char) to 0
      int left = 0;
      //calculate length of input stringthen decrease its value by 1
      int right = input.Length - 1;
      //boolean value to determine if string is palindrome
      bool isPalindrome = true;
      
      //while loop to continue looping til we get to the middle of the string
      while (left < right)
      {
        //compare left most character with right most character and if they don't match we return false
        if(input[left] != input[right])
        {
          isPalindrome = false;
          break;
        }
        
        //Incrementing left most index by 1 and decreasing right most index by 1, continue loop as long as both match
        left++;
        right--;
      }
      
      //Print the result using an if condition statement
      if (isPalindrome)
      {
        Console.WriteLine("The string is a palindrome");
      }
      else
      {
        Console.WriteLine("No, the string is not a palindrome");
      }
    }
  }

