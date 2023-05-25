# 以fb15k-237-20 为范例:
# 实验一 Data Processing

    # ./experiment.sh configs/<dataset>.sh --process_data <gpu-ID>

    # <example> ./experiment.sh configs/fb15k-237-20.sh --process_data <gpu-ID>

# 实验二 Pretrain Knowledge Graph Embedding

    # ./experiment-emb.sh configs/<dataset>-<model>.sh --train <gpu-ID>

        # 问题:<model>包括 conve 和 rs
            # ConvE（Convolutional 2D Knowledge Graph Embedding）是一种嵌入模型，用于知识图谱表示学习。它是基于卷积神经网络（CNN）的模型，用于将实体和关系映射到低维连续向量空间中。ConvE模型的主要思想是将知识图谱中的三元组（实体、关系、实体）表示为二维矩阵，然后通过卷积操作来捕捉实体和关系之间的语义信息。它在知识图谱推理和链接预测等任务上取得了一定的性能。

            # *** rs是什么？

    #<example> ./experiment-emb.sh configs/fb15k-237-20-rs.sh --train <gpu-ID>

    # python3.6 -m src.experiments --data_dir data/FB15K-237-20 --train --model conve --entity_dim 200 --relation_dim 200 --num_rollouts 1 --bucket_interval 10 --num_epochs 1000 --num_wait_epochs 20 --batch_size 512 --train_batch_size 512 --dev_batch_size 128 --num_negative_samples 100 --margin 0.5 --learning_rate 0.003 --grad_norm 0 --emb_dropout_rate 0.3 --beam_size 128 --emb_2D_d1 10 --emb_2D_d2 20 --group_examples_by_query --add_reversed_training_edges --gpu 0

#
