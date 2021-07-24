#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install ibm_watson


# In[2]:


pip install ibm_cloud_sdk_core


# In[3]:


from ibm_watson import TextToSpeechV1


# In[4]:


from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[6]:


api = IAMAuthenticator("-CkF5LL02xYLq9eh12wtIy1kGj_cHgshEWs164TbM8ER")


# In[7]:


text_2_speech = TextToSpeechV1(authenticator=api)


# In[8]:


text_2_speech.set_service_url("https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/7d47af77-1364-460c-93a0-5d927e8ade25")


# In[9]:


with open("welcome.mp3","wb") as audiofile:
    audiofile.write(
    text_2_speech.synthesize("Welcome to Smart Method company ",
                            accept="audio/mp3").get_result().content)


# In[ ]:





# In[ ]:




