python extract_features.py \
  --input_file=./data/train/ST_nolabel.txt\
  --output_file=./ft_test_fea/train/ST.json\
  --vocab_file=./vocab/vocab_1kmer.txt \
  --bert_config_file=./bert_config_1.json \
  --init_checkpoint=./rt_model/ST/model/model.ckpt-123 \
  --layers=-1 \
  --max_seq_length=128 \
  --batch_size=32 

