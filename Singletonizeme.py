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

import threading
from typing import Any, Type, TypeVar, Dict

T = TypeVar("T")


class Singleton:
    """
    A flexible, thread-safe Singleton decorator class.

    Usage:
        @Singleton()
        class MyClass:
            pass

        # or with parameters
        @Singleton(thread_safe=True, strict=False)
        class MyClass:
            pass
    """

    # Dictionary to store one instance per decorated class
    _instances: Dict[Type, Any] = {}
    _lock = threading.Lock()

    def __init__(self, thread_safe: bool = True, strict: bool = False):
        self.thread_safe = thread_safe
        self.strict = strict

    def __call__(self, cls: Type[T]) -> Type[T]:
        """
        Called when the decorator is applied to a class.
        Returns a wrapped class that enforces singleton behavior.
        """

        def wrapper(*args, **kwargs) -> T:
            if cls not in Singleton._instances:
                if self.thread_safe:
                    with Singleton._lock:
                        if cls not in Singleton._instances:
                            Singleton._instances[cls] = cls(*args, **kwargs)
                else:
                    Singleton._instances[cls] = cls(*args, **kwargs)
            else:
                if self.strict:
                    raise RuntimeError(
                        f"Attempt to create another instance of singleton class '{cls.__name__}'"
                    )

            return Singleton._instances[cls]

        return wrapper
