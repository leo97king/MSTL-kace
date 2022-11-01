# BERT-kace
A prediction for prokaryotic lysine acetylation site


## Highlights:
* BERT-kace use NLP（natural language processing）methods to better learn the intrinsic information of protein sequences.
* Fine-tune the pre-train model to adapt different prokaryotic species and extracte embedding features.
* Comparing different computational frameworks using tree different machine learning and two different deep learning methods。 
* The results on the benchmark independent test set shows that BERT-kcae achieves superior performance in Kace site prediction compared to other resultant methods.

## Introduction
Lysine acetylation (kace) as an important form of PTM plays an important role in various life activities，such as cellular metabolism, transcriptional regulation. Traditional experimental methods are time-consuming and costly, so predicting acetylation site accurately and quickly is a meaningful and challenging task. Recently, several machine learning and deep learning methods have been developed for acetylation site prediction, but they use traditional features such as sequence features and physicochemical features, which are diverse and cumbersome to extract. In this study, we proposed a novel model, BERT-kace, which was developed with pre-trained bidirectional encoder representations from transformers (BERT) model. A large amount of protein sequences was used to pre-train a BERT model, then we fine-tuned the pre-train model for different species, and extracted embedding features from the fine-tuned BERT model. To compare the performance of the different classifiers, we used tree different machine learning and two different deep learning methods. The results on the benchmark independent test set showed that our model generally outperformed other resultant methods. The AUROC value is higher than existing predictor in four of the six prokaryotic species. It indicates that our model can predict lysine acetylation site better.If your input is small, you can also use our [web server](http://bert-kace.zhulab.org.cn/) of BERT-Kace.
![BERT_Kace_architecture](https://github.com/leo97king/BERT-kace/blob/main/image/BERT_Kace_architecture.png)

## System requirement
BERT-kace is developed under Linux environment with:  
python  3.6.8  
numpy  1.19.1  
pandas  1.1.5  
tensorflow  1.15.0  
sentencepiece  0.1.96  
transformers  4.9.1  
tqdm  4.56.0  


## Run BERT-Kace for prediction
1. Modify shell file: `./extral_feature.sh` Change the filepath of `init_checkpoint`.
```
python extract_features.py \
  --input_file= ./temp.txt \  
  --output_file=./temp/temp.json\
  --vocab_file=./vocab.txt \
  --bert_config_file=./bert_config.json \
  --init_checkpoint=./bert_model/fine_tuned_model/BS/model.ckpt \ #chose the species
  --layers=-1 \
  --max_seq_length=128 \
  --batch_size=32 
```

2. Run `./bert_kace_predict.py`. We also provide the corresponding canonical prediction results in `./result/prob.txt` for your reference.



## Dataset and model
We provide the datasets and the trained  models here for those interested in reproducing our paper.
The  datasets used in this study are stored in `./data/` in fasta format.  
The predict models  can be found under `./model/`.

