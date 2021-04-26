# MiniSTRyplace
We were given the source code for this website. This was a typical example of directory transversal through PHP webpage.

![website](https://github.com/1n4n0/HTB-Cyber-Apocalypse-2021/blob/main/Web/MiniSTRypalace/images/S1.png?raw=true)

Clicking on either of the pages from upper right corner of the page gives:

![url](https://github.com/1n4n0/HTB-Cyber-Apocalypse-2021/blob/main/Web/MiniSTRypalace/images/S2.png?raw=true)
## Solution
*When we check the source code of the website we see this PHP snippet :*

```php
<?php
    $lang = ['en.php', 'qw.php'];
    include('pages/' . (isset($_GET['lang']) ? str_replace('../', '', $_GET['lang']) : $lang[array_rand($lang)]));
?>
```
Here, it checks if the `GET` parameter is empty or not and then display the webpage. There are two possibilities :
1. If the `GET` parameter is empty:
 - It will randomly select from the array of two web pages.

2. If the `GET` parameter is not empty:
- It will remove `../` from our passed parameter 
- Then it will append the `GET` parameter to `pages/{parameter}` and display the page.

To go back from current directory we need `../` but as we can see there is a filter for this.

To bypass this filter we can do something like this `....//` as after replacement it would evaluate to `../`

Now we need to know where the flag is located, so we check the `Dockerfile` which was provided along with the source code and found this:
```docker
# Copy challenge files
COPY challenge /www
COPY flag /
```
This implies that the flag file is located in the **root directory**.

*Now we have all the required information, so now we open up `Burp Suite` to intercept the traffic. This can also done using `Firefox` browser through it's networking section but we will stick with burp.*

*Intercept the traffic and send the request to __repeater__ window. Now we will add multiple `....//` to go to root directory. Just to be sure we will try to open `/etc/passwd` file for sanity check.*

![burp](https://github.com/1n4n0/HTB-Cyber-Apocalypse-2021/blob/main/Web/MiniSTRypalace/images/S4.png?raw=true)

*And boom! we get the file output. So now, we just replace `/etc/passwd` with `flag.txt`.*

![notflag](https://github.com/1n4n0/HTB-Cyber-Apocalypse-2021/blob/main/Web/MiniSTRypalace/images/S5.png?raw=true)

But what the heck?! No flag? I thought that the flag file might not be in root directory so I checked for `flag.txt` in all preceeding directories. Still, no luck : (

*Then it clicked me that how dumb I was for assuming `.txt` extension to flag file. So after removing `.txt` and only appending `flag` to our parameter it worked and gave us the flag!*

![flag](https://github.com/1n4n0/HTB-Cyber-Apocalypse-2021/blob/main/Web/MiniSTRypalace/images/S6.png?raw=true)

> **Flag :** _CHTB{b4d_4li3n_pr0gr4m1ng}_
