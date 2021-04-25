# Web
---
## 0x00 MiniSTRyplace
---
We were given the source code for this website. This was a typical example of directory transversal through PHP webpage.
![website](https://github.com/1n4n0/HTB-Cyber-Apocalypse-2021/blob/main/Web/MiniSTRypalace/images/S1.png?raw=true)
### Solution
> When we check the source code of the website we see this PHP snippet :
```php
<?php
    $lang = ['en.php', 'qw.php'];
    include('pages/' . (isset($_GET['lang']) ? str_replace('../', '', $_GET['lang']) : $lang[array_rand($lang)]));
?>
```
Here, it checks if the **GET** parameter is enpty or not and then display the webpage. There are two possibilities :
1. If the **GET** parameter is empty:
1.1 It will randomly select from the array of two web pages.

2. If the **GET** parameter is not empty:
2.1 It will remove "../" from our passed parameter 
2.2 Then it will append the **GET** parameter to "pages/{parameter}" and display the page.

To go back from current directory we need `../` but as we can see there is a filter for this.

To bypass this filter we can do something like this `....//` as after replacement it would evaluate to `../`

Now we need to know where the flag is located, so we check the **Dockerfile** which was provided along with the source code.
I found this:
```docker
# Copy challenge files
COPY challenge /www
COPY flag /
```
This implies that the flag file is located in the **root directory**.
> Now we have all the required information, so now we open up **Burp Suite** to intercept the traffic. This can also done using Firefox browser through it's networking section but we will stick with burp.

> Intercept the traffic and send the request to **repeater** window. Now we will add multiple `....//` to go to root directory. Just to be sure we will try to open `/etc/passwd` file for sanity check.

! [burp](burp)
> And boom! we get the file output. So now, we just replace `/etc/passwd` with `flag.txt`.

! [notflag](notflag)
But what the heck?! No flag? I thought that the flag file might not be in root directory so I checked for `flag.txt` in all preceeding directories. Still, no luck : (

> Then it clicked me that how dumb the preassumption was for including `.txt` to `flag`. Then I tried after removing `.txt` and only appending `flag` to our parameter. And It worked!

! [flag](flag)
> **Flag :** _CHTB{b4d_4li3n_pr0gr4m1ng}_









