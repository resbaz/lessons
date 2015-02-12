import os
import cPickle as pickle

# Read BNC word frequency distributions using cpickle
# Note: bnc.p contains only non stopwords
BNCfile = os.path.join(os.path.dirname(__file__), "bnc.p")
fdistBNC = pickle.load( open( BNCfile, "rb" ) )

# Total number of words in Spoken BNC
sumBNC = 11606059
