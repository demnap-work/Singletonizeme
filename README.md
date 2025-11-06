# Singletonizeme

**Singletonizeme** is a lightweight Python library that provides a simple and elegant way to make any class behave as a *singleton* — ensuring only one instance of the class exists throughout the entire program.

It offers an easy-to-use decorator — `@Singleton` — that supports optional thread-safety and strict mode, making it suitable for both small projects and production-level systems.

---

## Features

- 🔹 Simple decorator-based usage  
- 🔹 Guarantees a single instance across your program  
- 🔹 Optional thread-safety using Python’s `Lock`  
- 🔹 Optional strict mode to raise errors on multiple instantiations  
- 🔹 Fully type-annotated and PEP-8 compliant  
- 🔹 Pure Python implementation (no external dependencies)  
- 🔹 Python 3.8+ compatible  

---

## 1. Installation

You can install **SinglePy** directly from [PyPI](https://pypi.org/project/singletonizeme/):

```bash
pip install singletonizeme

```

---

## 2. Import and Basic Usage

The decorator can be applied to any class to ensure it has only one instance.

```python
from singletonizeme import Singleton

@Singleton
class DatabaseConnection:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

db1 = DatabaseConnection("localhost", 5432)
db2 = DatabaseConnection("remotehost", 3306)

print(db1 is db2)  # ✅ True

```

Behavior:

The first instantiation (db1) creates the object.

All subsequent instantiations (db2, etc.) return the same instance.

---

## 3. Decorator Parameters
thread_safe (bool)

Purpose: Enables or disables thread-safe instantiation.

Default: True

Description:
When True, a threading.Lock ensures that only one instance can be created, even in multi-threaded environments.

Example:

```python
@Singleton(thread_safe=True)
class MyService:
    ...

strict (bool)

```

Purpose: Controls behavior on multiple instantiation attempts.

Default: False

Description:
When True, attempting to instantiate the singleton more than once raises a RuntimeError.
When False, all calls return the same existing instance silently.

Example:

```python
@Singleton(strict=True)
class Logger:
    def __init__(self, name: str):
        self.name = name

```

log1 = Logger("App")
log2 = Logger("Core")  # ❌ Raises RuntimeError

---

## 4. Usage Examples
## 4.1 Integer Example

```python
@Singleton
class Counter:
    def __init__(self, start: int):
        self.value = start

counter1 = Counter(10)
counter2 = Counter(99)

print(counter1.value)  # 10
print(counter1 is counter2)  # True

```

## 4.2 Float Example

```python
@Singleton
class TemperatureSensor:
    def __init__(self, default_temp: float):
        self.temperature = default_temp

sensor1 = TemperatureSensor(23.5)
sensor2 = TemperatureSensor(99.9)

print(sensor1.temperature)  # 23.5
print(sensor1 is sensor2)   # True

```

## 4.3 String Example

```python
@Singleton
class AppConfig:
    def __init__(self, mode: str):
        self.mode = mode

config1 = AppConfig("production")
config2 = AppConfig("development")

print(config1.mode)        # "production"
print(config1 is config2)  # True
```

## 4.4 List Example

```python
@Singleton
class DataBuffer:
    def __init__(self, data: list):
        self.data = data

buffer1 = DataBuffer([1, 2, 3])
buffer2 = DataBuffer([9, 8, 7])

print(buffer1.data)        # [1, 2, 3]
print(buffer1 is buffer2)  # True

```

## 4.5 Dictionary Example

```python
@Singleton
class Settings:
    def __init__(self, config: dict):
        self.config = config

settings1 = Settings({"theme": "dark", "lang": "en"})
settings2 = Settings({"theme": "light", "lang": "fr"})

print(settings1.config)     # {"theme": "dark", "lang": "en"}
print(settings1 is settings2)  # True

```

## 4.6 Custom Object Example

```python
class User:
    def __init__(self, username):
        self.username = username

@Singleton
class Session:
    def __init__(self, user: User):
        self.user = user

session1 = Session(User("Alice"))
session2 = Session(User("Bob"))

print(session1.user.username)  # "Alice"
print(session1 is session2)    # True

```

## 5. Thread-Safe Example

```python
import threading
from singlepy import Singleton

@Singleton(thread_safe=True)
class ThreadSafeSingleton:
    def __init__(self):
        print("Instance created!")

def create_instance():
    instance = ThreadSafeSingleton()

threads = [threading.Thread(target=create_instance) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

```
# Output: "Instance created!" printed only once

## 6. License


MIT License © 2025 Giuseppe De Martino, PhD


