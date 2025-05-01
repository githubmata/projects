
using System;

namespace LoggingTest
{

    //Define an enum for log levels
    public enum LogLevel
    {
        //list all the types of errors that can be captured. 
        Debug,
        Information,        
        Warning,
        Error,
        Critical        
    }


    //Define the ILogger interface
    public interface ILogger
    {
        public void Log(LogLevel level, string message);
        public void Log(LogLevel level, string message, Exception exception);
    }
    
    //Implementing the ILogger interface
    public class FileLogger : ILogger
    {
        //implement methods
        public void Log(LogLevel level, string message)
        {
            Console.WriteLine($"[{DateTime.Now}] [{level}]: {message}")
        }

        public void Log(LogLevel level, string message, Exception exception)
        {
            Conosole.WriteLine($"[{DateTime.Now}] [{level}]: {message}")
            Console.WriteLine($"  Exception: {exception}");
            
            //capture the data from request


            //write the data to file
            Console.WriteLine("2025" + "randomPatient" + .txt);

        }
    }

    public class TextBoxLogger
    {
        //implement methods
        private readonly ILogger _logger;
        
        public TextBoxLogger(ILogger logger)
        {
            _logger = logger;
        }

        public void MessageFromLogger()
        {
            _logger.Log(LogLevel.Information, "We are sending log message about log captured as INFO");
            _logger.Log(LogLevel.Warning, "Here is a warning log event captured in application");
            
            //write try catch for critical errors logged/captured
            try
            {
                throw new Exception("An error happened");
            }
            catch (Exception ex)
            {
                _logger.Log(LogLevel.Error, "A bad error has occurred", ex);
            }
        }
    }
}


