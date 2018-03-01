
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib notebook')


# In[2]:

import matplotlib.pyplot as plt


# In[3]:

import numpy as np


# In[4]:

data = np.arange(10)


# In[5]:

data


# In[6]:

plt.plot(data)


# In[7]:

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)


# In[8]:

plt.plot(np.random.randn(50).cumsum(), 'k--')


# In[9]:

ax1.clear()
ax2.clear()


# In[10]:

_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)


# In[11]:

ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))


# In[12]:

fig, axes = plt.subplots(2, 3)


# In[13]:

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)


# In[14]:

for i in range(2):
    for j in range(2):
        axes[i, j].clear()
        axes[i, j].hist(np.random.rand(500), bins=50, color='k', alpha=0.5)


# In[15]:

plt.subplots_adjust(wspace=0.0, hspace=0.0)


# In[16]:

plt.figure()
plt.plot(np.arange(10), linestyle='--', color='red')


# In[17]:

get_ipython().magic(u'pinfo plt.plot')


# In[18]:

from numpy.random import randn


# In[19]:

plt.figure()
plt.plot(randn(50).cumsum(), 'go--')


# In[20]:

plt.figure()
plt.plot(randn(50).cumsum(), linestyle='--', color='g', marker='o')


# In[21]:

data = randn(50).cumsum()


# In[22]:

plt.figure()
plt.plot(data, 'k--', label='Default')


# In[23]:

plt.plot(data, 'k-', drawstyle='steps-post', label='steps post')


# In[24]:

plt.legend(loc='best')


# In[25]:

plt.xlim([0, 49])


# In[26]:

plt.xlim()


# In[27]:

fig, ax = plt.subplots(1, 1)


# In[28]:

ax.set_xlim([0, 10])


# In[29]:

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


# In[30]:

ax.plot(randn(1000).cumsum())


# In[31]:

ax.get_xticks()


# In[32]:

ticks = ax.set_xticks([0, 250, 500, 750, 1000])


# In[33]:

labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')


# In[34]:

ax.set_xlabel('Stages')


# In[35]:

ax.set_title('Some plot')


# In[36]:

ax.get_yticks()


# In[37]:

ax.get_ylim()


# In[38]:

props = {'xticklabels': ['one', 'two', 'three', 'four', 'five'], 'xlabel': 'Stgs', 'title': 'New plot'}
ax.set(**props)


# In[39]:

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


# In[40]:

ax.clear()
ax.plot(randn(1000).cumsum(), 'k', label='one')
ax.plot(randn(1000).cumsum(), 'k--', label='two')
ax.plot(randn(1000).cumsum(), 'k.', label='three')
ax.legend(loc='best')


# In[52]:

fig, ax = plt.subplots(1, 1)
ax.clear()
ax.plot(randn(1000).cumsum(), 'k')


# In[53]:

ax.text(600, 10, 'Hello World', family='monospace', fontsize=10)


# In[54]:

from datetime import datetime


# In[55]:

import pandas as pd


# In[87]:

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.clear()


# In[57]:

from os.path import join


# In[62]:

filename = join('..', '..', 'pydata-book', 'examples', 'spx.csv')
data = pd.read_csv(filename, index_col=0, parse_dates=True)


# In[65]:

spx = data['SPX']


# In[88]:

spx.plot(ax=ax, style='k-')


# In[70]:

crisis_data = [(datetime(2007, 10, 11), 'Peak of bull market'), 
               (datetime(2008, 3, 12), 'Bear Stearns fails'), 
               (datetime(2008, 9, 15), 'Lehman bankruptcy')]


# In[83]:

arrowprops = dict(facecolor = 'black', 
                  headwidth = 4,
                  width = 2,
                  headlength = 4)
#                   horizontalalignment = 'left',
#                   verticalalignment = 'top' )


# In[89]:

for date, label in crisis_data:
    ax.annotate(label, xy=(date, spx.asof(date) + 75), xytext=(date, spx.asof(date) + 225), arrowprops=arrowprops)


# In[90]:

ax.set_xlim([ '1/1/2007' , '1/1/2011' ])
ax.set_ylim([600, 1900])
ax.set_title('Important dates in the 2008-2009 financial crisis')


# In[101]:

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.clear()


# In[102]:

rect = plt.Rectangle((2, 1), 0.5, 1, color='g', alpha=0.3)
circ = plt.Circle((5, 1), 0.5, color='b', alpha=0.3)
poly = plt.Polygon([[2, 2], [1, 4], [5, 1]], color='r', alpha=0.3)


# In[103]:

ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(poly)


# In[104]:

ax.set_xlim([0, 10])
ax.set_ylim([0, 10])


# In[105]:

fig.savefig('figure.png')


# In[106]:

plt.savefig('figure.pdf', dpi=400, bbox_inches='tight')


# In[107]:

from io import BytesIO


# In[108]:

buffer = BytesIO()
fig.savefig(buffer)


# In[109]:

plot_data = buffer.getvalue()

