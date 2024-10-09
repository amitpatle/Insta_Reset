# Insta_Reset

This tool generates random reset account URLs and check if they still valid for a complete Instagram account .

### USAGE:

`$ git clone https://github.com/amitpatle/Insta_Reset`

`$ cd Insta_Reset && pip3 install -r requirements.txt`

`$ python3.9 main.py`

### HOW IT WORKS:

When you try to reset your Instagram Password you are prompted for an email or a phone number.

Then you will receive a link like: 

Following this link you have the possibility to reset your password OR just skip and go to your account directly, like many people do. **If this happens the link will remain valid! It doesn't expire neither after 24 hours... that's crazy.**

So, this tool generates infinite URIs, call them and check status code. If 301 then our link is valid -but could be expired if user changed his passwrd- so if user didn't change his password we could takeover the account! If 302 our link is not valid.

