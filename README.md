# MSTL-kace
A prediction for prokaryotic lysine acetylation site

## Introduction
As one of the most important post-translational modifications (PTM), lysine acetylation (Kace) plays important roles in various life activities, such as cellular metabolism, and transcriptional regulation. Traditional experimental methods for identifying Kace are inefficient and expensive, alternatively, computational methods could facilitate the detection of Kace sites. Recently, several machine learning and deep learning methods have been developed for Kace site prediction and hand-crafted features have been used to encode the protein sequences. However, the complex biological information might be under-represented by these man-made features, which attenuates the performance of the models. In this study, we proposed a novel model, MSTL-Kace, which was developed based on transfer learning strategy with pre-trained bidirectional encoder representations from transformers (BERT) model. By considering the protein sequences as natural language sentences, a domain-specific BERT model was pre-trained using all the sequences in our datasets. Then, we fine-tuned, or two-stage fine-tuned the pre-trained model based on the training dataset of each species, and the embeddings of residues were extracted from the fine-tuned model which were fed to the different downstream learning algorithms. After comparison, the best model for the six prokaryotic species was built by using random forest.![image](https://github.com/leo97king/MSTL-kace/assets/87485193/fafdbd63-26b2-46f1-9be5-a35f68e79c6c).If your input is small, you can also use our [web server](http://bert-kace.zhulab.org.cn/) of BERT-Kace.

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

2. Run `./bert_kace_predict.py`. We also provide the corresponding canonical prediction results in `./temp/prob.txt` for your reference.



## Dataset and model
We provide the datasets and the trained  models here for those interested in reproducing our paper.
The  datasets used in this study are stored in `./data/` in fasta format.  
The predict models  can be found under `./model/`.

