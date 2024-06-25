cd models/ditto

python train_ditto.py \
  --task musicbrainz \
  --batch_size 32 \
  --max_len 128 \
  --lr 3e-5 \
  --n_epochs 20 \
  --finetuning \
  --lm roberta 
