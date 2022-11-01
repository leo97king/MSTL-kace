from utils import *


input_file = './data/example/example.txt'
sp_name='BS'  # one of ['BS','CG','EC','GK', 'MT', 'ST']
get_features(input_file,sp_name)
do_predict(sp_name)
