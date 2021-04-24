# Misc

## 0x00 Input as Service
*We were given ip address and port numer of the server running a  **python** program.*

### Solution
---
I Used netcat to connect to the server, it was running a python binary which was taking two inputs.
>I tried few things and found that it was using exec() function.
>I tried using dir() which resulted into: 

![pyout](/S2.jpg)

It worked!

>So now I tried to import os and execute shell commands using this payload:
```python
__import__(os).system("ls")
```
![exec](/S3.jpg)

This proved RCE vulnerability as it returned the output of the shell command (also two numbers; probabily those are return values of \_\_import\_\_ )

>Finally, this comand to get the flag : 
```python
__import__(os).system("cat flag.txt")
```
![flag](/S4.jpg)

>**Flag :**
*CHTB{4li3n5_us3_pyth0n2.X?!}*