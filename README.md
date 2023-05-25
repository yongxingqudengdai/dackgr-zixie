# 	DacKGR

Source codes and datasets for EMNLP 2020 paper [Dynamic Anticipation and Completion for Multi-Hop Reasoning over Sparse Knowledge Graph](https://arxiv.org/pdf/2010.01899.pdf)

## Requirements

- python3 (tested on 3.6.6)
- pytorch (tested on 1.5.0)

## Data Preparation

Unpack the data files

``` bash
unzip data.zip
```

and there will be five datasets under folder `data`.

``` bash
# dataset FB15K-237-10%   
# 数据集FB15K-237是一个常用的知识图谱数据集，用于关系抽取和知识图谱补全任务。
# ***"10%"是指在该数据集中随机选择的10%的数据作为训练、验证或测试集。
data/FB15K-237-10

# dataset FB15K-237-20%
data/FB15K-237-20

# dataset FB15K-237-50%
data/FB15K-237-50

# dataset NELL23K
# 数据集NELL23K是一个用于知识图谱补全任务的常用数据集，其中NELL代表"Never-Ending Language Learner"（永不停止的语言学习者）。NELL23K数据集包含了23,000个三元组，每个三元组由实体之间的关系构成，形式为 (实体1, 关系, 实体2)。
data/NELL23K

# dataset WD-singer
data/WD-singer
```

## Data Processing

``` bash
./experiment.sh configs/<dataset>.sh --process_data <gpu-ID>

<example> ./experiment.sh configs/fb15k-237-20.sh --process_data <gpu-ID>
```

`dataset` is the name of datasets. In our experiments, `dataset` could be `fb15k-237-10`, `fb15k-237-20`, `fb15k-237-50`, `nell23k` and `wd-singer`. `<gpu-ID>` is a non-negative integer number representing the GPU index.

## Pretrain Knowledge Graph Embedding

``` bash
./experiment-emb.sh configs/<dataset>-<model>.sh --train <gpu-ID>
```

`dataset` is the name of datasets and `model` is the name of knowledge graph embedding model. In our experiments, `dataset` could be `fb15k-237-10`, `fb15k-237-20`, `fb15k-237-50`, `nell23k` and `wd-singer`, `model` could be `conve`. `<gpu-ID>` is a non-negative integer number representing the GPU index.

## Train

``` bash
# take FB15K-237-20% for example
./experiment-rs.sh configs/fb15k-237-20-rs.sh --train <gpu-ID> 
```

## Test

``` bash
# take FB15K-237-20% for example
./experiment-rs.sh configs/fb15k-237-20-rs.sh --inference <gpu-ID> 
```

## Cite 

If you use the code, please cite this paper:

Xin Lv, Xu Han, Lei Hou, Juanzi Li, Zhiyuan Liu, Wei Zhang, Yichi Zhang, Hao Kong, Suhui Wu. Dynamic Anticipation and Completion for Multi-Hop Reasoning over Sparse Knowledge Graph. *The Conference on Empirical Methods in Natural Language Processing (EMNLP 2020)*.
