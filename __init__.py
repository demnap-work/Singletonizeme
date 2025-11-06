"""
===============================================================================

  █████████   ███                      ████           ███████████            
 ███▒▒▒▒▒███ ▒▒▒                      ▒▒███          ▒▒███▒▒▒▒▒███           
▒███    ▒▒▒  ████  ████████    ███████ ▒███   ██████  ▒███    ▒███ █████ ████
▒▒█████████ ▒▒███ ▒▒███▒▒███  ███▒▒███ ▒███  ███▒▒███ ▒██████████ ▒▒███ ▒███ 
 ▒▒▒▒▒▒▒▒███ ▒███  ▒███ ▒███ ▒███ ▒███ ▒███ ▒███████  ▒███▒▒▒▒▒▒   ▒███ ▒███ 
 ███    ▒███ ▒███  ▒███ ▒███ ▒███ ▒███ ▒███ ▒███▒▒▒   ▒███         ▒███ ▒███ 
▒▒█████████  █████ ████ █████▒▒███████ █████▒▒██████  █████        ▒▒███████ 
 ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒ ▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒███▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒          ▒▒▒▒▒███ 
                              ███ ▒███                              ███ ▒███ 
                             ▒▒██████                              ▒▒██████  
                              ▒▒▒▒▒▒                                ▒▒▒▒▒▒    

 SinglePy - Configurable Thread-Safe Singleton Decorator
===============================================================================

Author: Giuseppe De Martino, PhD
Created: 2025-11-06
Version: 1.0.0
License: MIT

Description:
    A lightweight and configurable Singleton class decorator for Python.
    This utility ensures that any decorated class can have only one instance
    throughout the program's lifecycle.

    The decorator supports two key configuration options:
        - thread_safe (bool): Guarantees safe instantiation across multiple threads.
        - strict (bool): Raises an exception when attempting to instantiate
                         the class more than once.

    This module is designed for both academic and professional use, following
    PEP-8 and PEP-257 standards, and supports full type annotations.

Usage Example:
    from singletonlib.singleton import Singleton

    @Singleton(thread_safe=True, strict=False)
    class DatabaseConnection:
        def __init__(self, host: str, port: int):
            self.host = host
            self.port = port

    db1 = DatabaseConnection("localhost", 5432)
    db2 = DatabaseConnection("remotehost", 3306)
    print(db1 is db2)  # True

-------------------------------------------------------------------------------
"""

from .Singletonizeme import Singleton
__all__ = ["Singletonizeme"]