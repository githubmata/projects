
using System;

namespace LoggingTest
{

    //Define an enum for log levels
    public enum LogLevel
    {
        Debug,
        Information,
        Warning,
        error,
        Critical        
    }


    //Define the ILogger interface
    public interface ILogger
    {
        public void Log(LogLevel level, string message);
        public void Log(LogLevel level, string message, Exception exception);
        // public void Log(string msg);
        // public void Log(string msgType, string msg);
        // public void InitLogSession();
        // public void EndLogSession();
        // public void AddLogger(Logger appendedLogger);
        // public void RemoveLogger(Logger appendedLogger);
    }
    
    //Sample class using the ILogger interface
    public class FileLogger : Logger
    {
        public void Log(LogLevel level, string message)
        //implement methods
    }

    public class TextBoxLogger : Logger
    {
        //implement methods
    }

    public class DBLogger : Logger
    {
        //implement methods
    }


}


