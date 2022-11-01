import numpy as np
import pandas as pd
import joblib,json,sys,os,warnings

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Bidirectional, LSTM, Dropout, Dense, Activation, Flatten,Reshape
from tensorflow.keras.optimizers import Adam
from xgboost.sklearn import XGBClassifier
from keras.models import load_model
from sklearn.metrics import f1_score, precision_recall_curve, roc_auc_score,confusion_matrix ,precision_recall_curve,average_precision_score

if not sys.warnoptions:
    warnings.simplefilter("ignore")
    os.environ["PYTHONWARNINGS"] = "ignore" # Also affect subprocesses
warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore")

def fasta2str(in_file, out_file):    # Converting sequences into a format that bertmodel can use
    ngram = 1
    ng = int(ngram)

    fout = open(out_file, 'w')

    spe_character = []

    with open(in_file) as f:
        for line in f:
            if (line.startswith('>') == False) and (any(x in line for x in spe_character) == False):
                sequence = ''.join(line).replace('\n', '')
                fout.write(' '.join([sequence[i:i + ng] for i in range(len(sequence) - ng + 1)]) + '\n')

    fout.close()

def bert_ex(train_fc,out_json,sp_name):   # json file for extracting features from bert model
    cmd_0 = 'bash ./extral_feature.sh '
    a=os.system(cmd_0)
    print('----')
    print(a)
    print('-----')
    return a

def ex_json_cls(input_file,output_file):   # extracting cls features from json file
    
    with open(input_file, 'r') as json_file:
        json_list = list(json_file)
    
    fout_cls = open(output_file, 'w')

    for json_str in json_list:
        tokens = json.loads(json_str)["features"]
# 提取CLS特征
        for token in tokens:
            if token['token'] in ['[CLS]']:
                last_layers = [
                    token['layers'][0]['values'],
                ]
                fout_cls.write(f'{",".join(["{:f}".format(i) for i in last_layers])}\n')
    fout_cls.close()

def ex_json_avg(input_file,output_file):   # extracting avg features from json file

    with open(input_file, 'r') as json_file:
        json_list = list(json_file)
    
    fout_avg = open(output_file, 'w')

    for json_str in json_list:
        tokens = json.loads(json_str)["features"]

    feature_sum = np.zeros(768)
    count = 0
    for token in tokens:
        if token['token'] in ['[CLS]', '[SEP]']:
            continue
        else:
            last_layers = token['layers'][0]['values']
        feature_sum = feature_sum+last_layers
        count = count + 1
        if count == 21:
            feature_sum = feature_sum/21
            fout_avg.write(f'{",".join(["{:f}".format(i) for i in feature_sum])}\n')
    fout_avg.close()

def ex_json_all(input_file,output_file): # extracting all features from json file

    with open(input_file, 'r') as json_file:
        json_list = list(json_file)
    
    fout_all = open(output_file, 'w')

    for json_str in json_list:
        tokens = json.loads(json_str)["features"]
   
    for token in tokens:
        if token['token'] in ['[CLS]', '[SEP]']:
            continue
        else:
            last_layers = token['layers'][0]['values']
            fout_all.write(f'{",".join(["{:f}".format(i) for i in last_layers])}\n')
    fout_all.close()    


def get_features(file_name,sp_name):
    out_name = './temp.txt'
    out_json = './temp/temp.json'
    out_fea = './temp/temp.csv'
    fasta2str(file_name,out_name)
    a = bert_ex(out_name,out_json)
    
    a = 1
    if sp_name in ['BS','CG','MT']:
        ex_json_cls(out_json,out_fea)
    elif sp_name in ['GK','ST']:
        ex_json_avg(out_json,out_fea)
    elif sp_name=='EC':
        ex_json_all(out_json,out_fea)


def get_features(file_name,sp_name):
    out_name = './temp.txt'
    out_json = './temp/temp.json'
    out_fea = './temp/temp.csv'
    fasta2str(file_name,out_name)
    a = bert_ex(out_name,out_json)
    
    a = 1
    if sp_name in ['BS','CG','MT']:
        ex_json_cls(out_json,out_fea)
    elif sp_name in ['GK','ST']:
        ex_json_avg(out_json,out_fea)
    elif sp_name=='EC':
        ex_json_all(out_json,out_fea)


def load_predict_model(sp_name):
    if sp_name in ['BS','GK','MT','ST']:
        model=joblib.load('predict_model/model_{}.pkl'.format(sp_name))
    elif sp_name in ['CG','EC']:
        model=load_model('predict_model/model_{}.h5'.format(sp_name))
    return model

def do_predict(sp_name):
    
    print('Loading predictmodel')
    model = load_predict_model(sp_name)
    print('Reading test feature')
    feature=np.array(pd.read_csv('./temp/temp.csv'))
    if sp_name=='EC':
        feature = np.array(feature).astype(np.float)
        feature = feature.reshape(-1,21,768).transpose(0,2,1).reshape(-1,768,1,21)
    elif sp_name=='CG':
        feature = np.array(feature).astype(np.float).reshape(-1,1,768)
    
    pred=model.predict(feature)
    prob = model.predict_proba(feature)
    np.savetxt('./result/prob.txt',pred,fmt='%s')
    print('Saved Result')


