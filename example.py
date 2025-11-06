from Singletonizeme import Singleton
import datetime


@Singleton(thread_safe=True, strict=False)
class AppLogger():
    """
    A thread-safe Singleton logger class.

    This logger ensures that only one instance exists across the entire application,
    providing a centralized way to write logs to console or file.

    Args:
        logfile (str): Path to the log file.
        mode (str): File writing mode ('a' for append, 'w' for overwrite).
    """

    def __init__(self, logfile: str = "app.log", mode: str = "a"):
        self.logfile = logfile
        self.mode = mode

        # Open the file once, ensuring the same file handle is reused.
        self._file = open(self.logfile, self.mode, encoding="utf-8")
        self.write("Logger initialized.")

    def write(self, message: str):
        """Write a timestamped message to both console and log file."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted = f"[{timestamp}] {message}"
        print(formatted)
        self._file.write(formatted + "\n")
        self._file.flush()

    def close(self):
        """Close the log file (should be called at program exit)."""
        self.write("Logger closed.")
        self._file.close()


# --- Example usage ----------------------------------------------------------

if __name__ == "__main__":
    # Both calls will refer to the same instance
    logger1 = AppLogger("system.log")
    logger2 = AppLogger("debug.log")

    print(logger1 is logger2)  # ✅ True — both are the same instance

    logger1.write("Application started.")
    logger2.write("This message goes to the same file.")

    # Close the logger when done
    logger1.close()
