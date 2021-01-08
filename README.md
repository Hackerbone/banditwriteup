# Bandit Write Ups
Had different txt files for passwords and writeups which I merged using a python script which You can find 
in the same repo.

# bandit 0,1,2 

#### Passwords
bandit0, boJ9jbbUNNfktd78OOpsqOltutMc3MY1, CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

Commands used : ls,cd,ls -l , ls -la, cat easy ones 


# bandit3txt

#### Password
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

Had to use \ for the spaces between the file name just had to cat using '\'


================================================================

# bandit4txt

#### Password
pIwrPrtPN36QITSp3EQaw936yaFoFgAB

File was in folder inhere and had to find a hidden file ".hidden" found it using "ls -a"


================================================================

# bandit5txt

#### Password
koReBOKuIDDepwhWk7jZC0RTdopnAYKh

Had to find humanreadable file i.e ASCII text file for this used the "file ./*" command to find
the type of file


================================================================

# bandit6txt

#### Password
DXjZPULLxYr17uwoI01bNLQbtFemEgo7

Had to just use the "find" command -
command used
"find inhere -size 1033c"
returned the location of file which
 had pass


================================================================

# bandit7txt

#### Password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
This one was a bit tricky
Had to use again the find command.
File was owned by user bandit7
group bandit6
and size was 33bytes (33c)

now to the command used (explanation)

find / (root directory) -user bandit7 -group bandit6 -size 33c 2>/dev/null

(This last but of code "2>/dev/null" is to remove all the permission denied warnings/errors so
that we can see just the files we can see)




================================================================

# bandit8txt

#### Password
cvX2JJa4CFALtqS87jk27qwqGhBM9plV

Had to use the | to use multiple commands at once

cat data.txt | grep "millionth"




================================================================

# bandit9txt

#### Password
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

Woah this one was good

So password was the one line which repeated only once in the whole txt file
task was to find it

so had to sort the list
so that all entries that are similar can be grouped together
then once done
we can use uniq -c to see all repeated lines in one line and see which line is repeated with count


command:

cat data.txt | sort | uniq -c




================================================================

# bandit10txt

#### Password
truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk



This one was easy
had to use strings command to print , printable lines in the data.txt garbage
for more readability used grep "==" to make it a narrow search


cat data.txt | strings | grep "==="



================================================================

# bandit11txt

#### Password
IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

Easy one, had to decode base64 encoded data.txt

Command:
base64 -d data.txt




================================================================

# bandit12txt

#### Password
5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

Rot13 deciphered


================================================================

# bandit13txt

#### Password
8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL


Bruh this was mad

used cp, gunzip, bunzip2, tar, mv 

cp : copy
xxd : dehex hexdumps
gunzip : uncompress .gz files
bunzip2: uncompress bzipped files
tar : un tar files

alot of commands had to be written

mkdir /tmp/situ
cd ~
cp data.txt /tmp/situ
cd /tmp/situ
xxd data.txt > dehex
mv dehex dehex.gz
gunzip dehex.gz
bunzip dehex
tar data2
......
and so on

untill we get ascii data8.txt




================================================================

# bandit14txt

#### Password
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAxkkOE83W2cOT7IWhFc9aPaaQmQDdgzuXCv+ppZHa++buSkN+
gg0tcr7Fw8NLGa5+Uzec2rEg0WmeevB13AIoYp0MZyETq46t+jk9puNwZwIt9XgB
ZufGtZEwWbFWw/vVLNwOXBe4UWStGRWzgPpEeSv5Tb1VjLZIBdGphTIK22Amz6Zb
ThMsiMnyJafEwJ/T8PQO3myS91vUHEuoOMAzoUID4kN0MEZ3+XahyK0HJVq68KsV
ObefXG1vvA3GAJ29kxJaqvRfgYnqZryWN7w3CHjNU4c/2Jkp+n8L0SnxaNA+WYA7
jiPyTF0is8uzMlYQ4l1Lzh/8/MpvhCQF8r22dwIDAQABAoIBAQC6dWBjhyEOzjeA
J3j/RWmap9M5zfJ/wb2bfidNpwbB8rsJ4sZIDZQ7XuIh4LfygoAQSS+bBw3RXvzE
pvJt3SmU8hIDuLsCjL1VnBY5pY7Bju8g8aR/3FyjyNAqx/TLfzlLYfOu7i9Jet67
xAh0tONG/u8FB5I3LAI2Vp6OviwvdWeC4nOxCthldpuPKNLA8rmMMVRTKQ+7T2VS
nXmwYckKUcUgzoVSpiNZaS0zUDypdpy2+tRH3MQa5kqN1YKjvF8RC47woOYCktsD
o3FFpGNFec9Taa3Msy+DfQQhHKZFKIL3bJDONtmrVvtYK40/yeU4aZ/HA2DQzwhe
ol1AfiEhAoGBAOnVjosBkm7sblK+n4IEwPxs8sOmhPnTDUy5WGrpSCrXOmsVIBUf
laL3ZGLx3xCIwtCnEucB9DvN2HZkupc/h6hTKUYLqXuyLD8njTrbRhLgbC9QrKrS
M1F2fSTxVqPtZDlDMwjNR04xHA/fKh8bXXyTMqOHNJTHHNhbh3McdURjAoGBANkU
1hqfnw7+aXncJ9bjysr1ZWbqOE5Nd8AFgfwaKuGTTVX2NsUQnCMWdOp+wFak40JH
PKWkJNdBG+ex0H9JNQsTK3X5PBMAS8AfX0GrKeuwKWA6erytVTqjOfLYcdp5+z9s
8DtVCxDuVsM+i4X8UqIGOlvGbtKEVokHPFXP1q/dAoGAcHg5YX7WEehCgCYTzpO+
xysX8ScM2qS6xuZ3MqUWAxUWkh7NGZvhe0sGy9iOdANzwKw7mUUFViaCMR/t54W1
GC83sOs3D7n5Mj8x3NdO8xFit7dT9a245TvaoYQ7KgmqpSg/ScKCw4c3eiLava+J
3btnJeSIU+8ZXq9XjPRpKwUCgYA7z6LiOQKxNeXH3qHXcnHok855maUj5fJNpPbY
iDkyZ8ySF8GlcFsky8Yw6fWCqfG3zDrohJ5l9JmEsBh7SadkwsZhvecQcS9t4vby
9/8X4jS0P8ibfcKS4nBP+dT81kkkg5Z5MohXBORA7VWx+ACohcDEkprsQ+w32xeD
qT1EvQKBgQDKm8ws2ByvSUVs9GjTilCajFqLJ0eVYzRPaY6f++Gv/UVfAPV4c+S0
kAWpXbv5tbkkzbS0eaLPTKgLzavXtQoTtKwrjpolHKIHUz6Wu+n4abfAIRFubOdN
/+aLoRQ0yBDRbdXMsZN/jvY44eM+xRLdRVyMmdPtP8belRi2E2aEzA==
-----END RSA PRIVATE KEY-----



Had an RSA key in the bandit 13 lvl and just cat the file
we recieve this key which is the text through which we can log into the
next level.

Saved RSA key in a file bandit14 and used ssh -i to use it as pass
 
ssh -i bandit14 bandit14@bandit.labs.overthewire.org -p 2220



================================================================

# bandit15txt

#### Password
14 pass: 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

15 pass: BfMYroe26WYalil77FoDi9qh59eK5xNr

Had to find the pass for this level in /etc/bandit_pass/bandit14

then had to pass this into the localhost:30000

using nc


COmmand


nc localhost 30000 | cat /etc/bandit_pass/bandit14




================================================================

# bandit16txt

#### Password
cluFn7wTiGryunymYOu4RcffSxQluehd

Had to send lvl 15 pass thru ssl on localhost:30001

Got back lvl16 pass


================================================================

# bandit17txt

#### Password
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----


Had to find open ports using nmap and searching for ssl using ports

used command

nmap 31000-32000 localhost -sV 

returns two ports open and using SSL
so brute forced

 


================================================================

# bandit18txt

#### Password
kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

Had to find the changed line between two lines , for that, used difference of two
files

cmd:

diff passwords.old passwords.new



================================================================

# bandit19txt

#### Password
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

Just passed cat readme command thru the ssh

cmd:


sshpass `cat bandit18` ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"




================================================================

# bandit20txt

#### Password
GbKksEFF4yrVs6il55v6gwY5aVje5f0j


Had a binary file bandit20
had to use it to gain temporary access to the bandit20 user
then just catted the pass

./bandit20-do cat /etc/bandit_pass/bandit20




================================================================

# bandit21txt

#### Password
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

Had to open two sessions for bandit lvl 20

from one had to lisen to any port in this case 9999

Terminal 1:

nc -lvp 9999

Terminal 2:

./suconnect 9999

Terminal 1:

(lvl20 pass pasted)

(lvl21 pass retrieved)


================================================================

# bandit22txt

#### Password
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

Had to go to /etc/cron.d/ where we found that cron was writing to some tmp file

which contained the password
just had to find the file path

and catted it out

used cd, cat, ls -l



================================================================

# bandit23txt

#### Password
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

Found the script in the cronjob folder, changed the script user to bandit23 to get out
file's hex code and found the pass.




================================================================

