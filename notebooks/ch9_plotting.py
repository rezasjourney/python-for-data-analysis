
# coding: utf-8

# In[2]:

get_ipython().magic(u'matplotlib notebook')


# In[3]:

import matplotlib.pyplot as plt


# In[4]:

import numpy as np


# In[5]:

data = np.arange(10)


# In[6]:

data


# In[7]:

plt.plot(data)


# In[12]:

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)


# In[13]:

plt.plot(np.random.randn(50).cumsum(), 'k--')


# In[63]:

ax1.clear()
ax2.clear()


# In[64]:

_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)


# In[65]:

ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))


# In[66]:

fig, axes = plt.subplots(2, 3)


# In[74]:

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)


# In[107]:

for i in range(2):
    for j in range(2):
        axes[i, j].clear()
        axes[i, j].hist(np.random.rand(500), bins=50, color='k', alpha=0.5)


# In[80]:

plt.subplots_adjust(wspace=0.0, hspace=0.0)


# In[84]:

plt.figure()
plt.plot(np.arange(10), linestyle='--', color='red')


# In[86]:

get_ipython().magic(u'pinfo plt.plot')


# In[87]:

from numpy.random import randn


# In[94]:

plt.figure()
plt.plot(randn(50).cumsum(), 'go--')


# In[95]:

plt.figure()
plt.plot(randn(50).cumsum(), linestyle='--', color='g', marker='o')


# In[96]:

data = randn(50).cumsum()


# In[101]:

plt.figure()
plt.plot(data, 'k--', label='Default')


# In[102]:

plt.plot(data, 'k-', drawstyle='steps-post', label='steps post')


# In[103]:

plt.legend(loc='best')


# In[110]:

plt.xlim([0, 49])


# In[111]:

plt.xlim()


# In[115]:

fig, ax = plt.subplots(1, 1)


# In[118]:

ax.set_xlim([0, 10])


# In[122]:

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


# In[123]:

ax.plot(randn(1000).cumsum())


# In[124]:

ax.get_xticks()


# In[129]:

ticks = ax.set_xticks([0, 250, 500, 750, 1000])


# In[137]:

labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')


# In[138]:

ax.set_xlabel('Stages')


# In[139]:

ax.set_title('Some plot')


# In[141]:

ax.get_yticks()


# In[142]:

ax.get_ylim()


# In[143]:

props = {'xticklabels': ['one', 'two', 'three', 'four', 'five'], 'xlabel': 'Stgs', 'title': 'New plot'}
ax.set(**props)


# In[144]:

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


# In[149]:

ax.clear()
ax.plot(randn(1000).cumsum(), 'k', label='one')
ax.plot(randn(1000).cumsum(), 'k--', label='two')
ax.plot(randn(1000).cumsum(), 'k.', label='three')
ax.legend(loc='best')

