# BERT-kace
A prediction for prokaryotic lysine acetylation site


## Highlights:
* BERT-kace use NLP（natural language processing）methods to better learn the intrinsic information of protein sequences.
* Fine-tune the pre-train model to adapt different prokaryotic species and extracte embedding features.
* Comparing different computational frameworks using tree different machine learning and two different deep learning methods。 
* The results on the benchmark independent test set shows that BERT-kcae achieves superior performance in Kace site prediction compared to other resultant methods.

## Abstract
Lysine acetylation (kace) as an important form of PTM plays an important role in various life activities，such as cellular metabolism, transcriptional regulation. Traditional experimental methods are time-consuming and costly, so predicting acetylation site accurately and quickly is a meaningful and challenging task. Recently, several machine learning and deep learning methods have been developed for acetylation site prediction, but they use traditional features such as sequence features and physicochemical features, which are diverse and cumbersome to extract. In this study, we proposed a novel model, BERT-kace, which was developed with pre-trained bidirectional encoder representations from transformers (BERT) model. A large amount of protein sequences was used to pre-train a BERT model, then we fine-tuned the pre-train model for different species, and extracted embedding features from the fine-tuned BERT model. To compare the performance of the different classifiers, we used tree different machine learning and two different deep learning methods. The results on the benchmark independent test set showed that our model generally outperformed other resultant methods. The AUROC value is higher than existing predictor in four of the six prokaryotic species. It indicates that our model can predict lysine acetylation site better.
