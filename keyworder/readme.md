
~~~shell
k                              d         
k k                            d         
kk   eee y  y w   w ooo rrr  ddd eee rrr 
k k  e e y  y w w w o o r   d  d e e r   
k  k ee   yyy  w w  ooo r    ddd ee  r   
            y                            
         yyy                             
~~~

## Description

Keyworder identifies words frequencies in job descriptions (JD) and helps identifying important keywords.
The more often a word appears in a JD, the more important it will likely be.
Make sure to integrate these high-frequency to your résumé.
However, do not omit critically evaluating lower frequency words.

NLTK is used to remove common stopwords, which are unlikely to be common keywords.


### Installation

Python 3.5+ must be installed


### Create a virtualenv 

~~~shell
python -m venv venv
~~~

### Source env

~~~shell
source venv/bin/activate
~~~

### Download requirements 

Run in your console:
~~~shell
pip install -r requirements.txt
~~~


## Usage 
1. Copy the job descritpion to your clipboard ('strg' + 'c')
2. Run 'python keyworder.py'.
3. Paste ('strg' + 'v') job description to terminal when prompted and press 'ENTER'.
