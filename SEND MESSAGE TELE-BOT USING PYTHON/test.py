#! C:/Users/lenovo/AppData/Local/Programs/Python/Python310/python.exe
#test.py
# coding: utf-8
#!/usr/bin/env python
# In[ ]:
print("Content-Type: text/html")   
import cgitb 
import requests
import time

messages =[ 'pls refer what is the tokenomics details of skyvrse.',
            'infinite possibilities to explore in skyverse.',
            'tell me something new in skyverse project.',
            'guys new website of skyverse is interesting guys go and check.',
            'how can i explore shopping mall in skyverse project .',
            'it is a grate projct i will seen ever.']


for message in messages:
    
    base_url = '<BOT-API>/sendMessage?chat_id= <CHAT ID HERE>&text={} '.format(message)
    string="'messages'"

    output=eval(string)
    
    requests.get(base_url,output)

    time.sleep(20)
   






