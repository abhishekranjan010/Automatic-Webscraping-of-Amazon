#!/usr/bin/env python
# coding: utf-8

# In[11]:


get_ipython().system('pip install autoscraper')


# In[25]:


from autoscraper import AutoScraper


# In[26]:


amazon_url= 'https://www.amazon.in/s?k=headphones+%E0%A4%82&crid=3I8WNR820AB95&sprefix=head%2Caps%2C366&ref=nb_sb_ss_ts-doa-p_2_4'


# In[27]:


wanted_list= ["₹399", "MAGBOT GH56 Extra Bass Over The Ear Wired XB450 Headphone with Stereo Sound Quality 3.5mm Audio Cable Compatible with All Devices", "3"]


# In[35]:


scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)
print(result)


# In[36]:


scraper.get_result_similar(amazon_url,grouped=True)


# In[37]:


scraper.set_rule_aliases({'rule_jj8t':'Title', 'rule_hj21': 'Price'})
scraper.keep_rules(['rule_jj8t', 'rule_hj21'])
scraper.save('amazon-search')


# In[38]:


results=scraper.get_result_similar('https://www.amazon.in/s?k=bluetooth+headphones+under+500&crid=32312UVKDNVLW&sprefix=bluet%2Caps%2C331&ref=nb_sb_ss_ts-doa-p_6_5',group_by_alias=True)


# In[42]:


results['Title']


# In[43]:


results['Price']


# In[44]:


results['Title','Price']


# In[ ]:




