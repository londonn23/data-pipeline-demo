import time as t
import datetime
from functions import *

print('Starting data pipeline at ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('----------------------------------------------')

#step 1 extract video ids

t0 = t.time()
getVideoIDs()
t1 = t.time()
print('step 1 done')
print('---> video ids downloaded in', str(t1 - t0), 'seconds', '\n')

#step 2 extract transcripts

t0 = t.time()
getVideoTranscripts()
t1 = t.time()
print('step 2 done')
print('---> transcript downloaded in', str(t1 - t0), 'seconds', '\n')


#step 3 transform data

t0 = t.time()
transformData()
t1 = t.time()
print('step 3 done')
print('---> data transformed in', str(t1 - t0), 'seconds', '\n')


#step 4 generate text embeddings

t0 = t.time()
createTextEmbeddings()
t1 = t.time()
print('step 4 done')
print('---> embeddings generated in', str(t1 - t0), 'seconds', '\n')