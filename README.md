To run: 

From the command line:
  $ python autoemail.py

Complete the fields username, password as the email account you are sending mail from. The field fromaddr is also the email account you are sending mail from.

Customise the file model-list.txt in the format:

NAME1 EMAIL_ADDRESS1 DATE1
NAME2 EMAIL_ADDRESS2 DATE2
NAME3 EMAIL_ADDRESS3 DATE3
...
and so forth

where DATE is in the form MM/DD.
Also have to enable gmail's allow less secure apps to access the otl.uchicago@gmail.com account.

If you want to customise the message contents, change the last string in the msg variable to your liking.
