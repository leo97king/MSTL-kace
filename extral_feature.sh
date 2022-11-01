python extract_features.py \
  --input_file= ./temp.txt \  
  --output_file=./temp/temp.json\
  --vocab_file=./vocab.txt \
  --bert_config_file=./bert_config.json \
  --init_checkpoint=./bert_model/fine_tuned_model/BS/model.ckpt \ #chose the species
  --layers=-1 \
  --max_seq_length=128 \
  --batch_size=32 