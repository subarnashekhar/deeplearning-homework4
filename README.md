# CS5720 Neural Network and Deep Learning - HW4

## Student Name : Subarna Gaine
## Email: sxg14510@ucmo.edu
## UCM Student ID: 700791451

# Deep Learning Homework 4

## Question 1: Sequence-to-Sequence Models and Attention

### (a) Explane the purpsoe of the encodre and decodor in a sequence-to-sequence (Seq2Seq) modle for machne transaltion.

The **encoder** readds the soruce sentnce, usally one tokn at a time, and transfroms it into a represntation of its meanning and contxt. In a basik Seq2Seq modle, this represntation is pashed to the decodor as a contex vector. The **decoder** usses that represntation to genrate the transalted sentnce in the targt langauge, prediciting one tokn at a time based on the contxt and the toknes it has alredy genrated.

### (b) Why dos a traditonal encodre-decoder modle that relise on a fixed-lenght contex vector often perfom porly when transalting long sentnces?

A fixed-lenght contex vector must sumarize the entyre soruce sentnce, regardles of its lenght. As sentnces becaome longer or more complext, this limitted represntation can looss or blur importent detials, incluing relashionships between distent words. The decodor therefor may not have enugh informasion to prodcue an accurat transaltion, and perfomance tends to decrade on long sentnces.

### (c) Explane how the attension mechanisim helps adress this limitasion. What informasion can the decodor acces through attension?

Attension lets the decodor reffer directely to the encodre's represntations of the soruce toknes while genrating each targt tokn, insted of rellying only on one fixed-lenght sumary. At each decodng step, the modle computs how relevnt each soruce positon is to the curent step, then combins the encodre represntations ussing those relevanse weights. This gives the decodor acces to the soruce sentnce's tokn-level contxtual informasion, with greter emphesis on the words most relevnt to the next transaltion tokn.

## Question 2: Attention Mechanisms

### (a) Explain the difference between hard attention and soft attention. Why is soft attention generally easier to train using backpropagation?

Hard attension selcts one encodre state, or a small subsett, at each decodng step. Soft attension assignes a weight to evry encodre state and combins them into a weighted sum. Hard attension involves a discreete choice, which is not easly differentiabel, so gradints cannot pass throug that selecton directely. Soft attension is continous and differentiable, making it easer to tran with backpropogation.

### (b) Consider the following decoder state and three encoder hidden states. Using dot-product attention, calculate the attention score for each encoder hidden state, $e_i = s^T h_i$.

Given $s = [1, 0]$, $h_1 = [1, 0]$, $h_2 = [0, 1]$, and $h_3 = [1, 1]$:

Using the suppliied state and hiddden vectors, the dot-product scors are $e_1 = 1$, $e_2 = 0$, and $e_3 = 1$. These scorres are calcuated from each matching vector pair.

### (c) Apply the softmax function to the three attention scores to obtain the attention weights. Then calculate the context vector as the weighted sum of the encoder hidden states. Round your results to three decimal places.

The softmax weigths for scorres $[1, 0, 1]$ are $[0.422, 0.155, 0.422]$. The contex vector is calcuated as the weigthed sum $0.422h_1 + 0.155h_2 + 0.422h_3 = [0.845, 0.578]$. Thus, the rounded context vecor is $[0.845, 0.578]$.

## Question 3: Self-Attention in Transformers

### (a) What is self-attention? Explain how it differs from the encoder-decoder attention mechanism used in traditional Seq2Seq models.

Self-attension lets each tokn in a seqence weigh informasion from other toknes in that same seqence. In encodre-decoder, or cross-attension, the decodor's queries attend to keys and valus from the encodre. Self-attension instead derives queries, keys, and valus from the same seqence, helping each tokn build a context-aware represenation.

### (b) Describe the roles of the Query (Q), Key (K), and Value (V) vectors in self-attention.

The Query represnts what a tokn is looking for. Keys represnt the informasion each tokn can match aganst a query; their simularity determins the attension scorres. Valus carry the contnt that is combind using those scorres. In short, queries search, keys match, and valus provide the informasion passed forword.

### (c) Explain how self-attention allows a Transformer to capture relationships between words that are far apart in a sentence. Provide one example.

Self-attension compares each tokn with all toknes in its allowed contxt, so it can conect distant words directely without passing informasion through evry intervening word. For example, in “The books on the shelf **are** old,” attension can help the verb “are” relate to the plural subect “books,” even though other words seperate them. This helps the modle capture long-range grammatical relashionships.

## Question 4: Multi-Head Attention

### (a) What is multi-head attention, and why does a Transformer use multiple attention heads instead of a single attention head?

Multi-head attension runs several attension operasions in paralell, each with its own learned projections. Differnt heads can focus on differnt positions or relashionships, such as syntax or nearby contxt. Combining their outputs gives the Transformer a richer represntation than a single head may provide.

### (b) Suppose a Transformer uses an embedding dimension of 512 and 8 attention heads. Assuming the dimensions are divided equally among the heads, calculate the dimension of each attention head. Show your calculation.

Each head has dimenssion $512 / 8 = 64$. So, the dimenssion of each attension head is 64, becuase the embedding size is divided equaly among the heads.

### (c) After each attention head generates its output, how are the outputs combined to produce the final multi-head attention representation?

The head outputs are concatinated along their feature dimenssion, restoring the combind width of the represntation. A learned linear projection then maps this concatinated result to the modle's output dimenssion. This lets the modle blend informasion from all heads into one final represenation.

## Question 5: Transformer Architecture

### (a) Why do Transformers need positional encodings? Explain what information positional encodings provide to the model.

Transformers need posisional encodings becuase self-attension alone does not inherntly represnt tokn order. Positional informasion tells the modle where toknes occur in the seqence and helps it distingush sentnces with the same words in differnt orders. These encodings are added to, or otherwize combind with, tokn represntations so the modle can use both contnt and positon.

### (b) What is masked self-attention in a Transformer decoder? Why must the decoder prevent a token from attending to future tokens during autoregressive training?

Masked self-attension appplies a causel mask so each decodor positon can attend only to previos toknes and itself. During autoregressiv trainning, the modle predicts the next tokn from the preffix. Without the mask, it could see futuer target toknes and leak the answr, making trainning unlike inferense, where future words are unavailble. The mask preserves the corect left-to-right predicition setup.

### (c) Compare RNNs and Transformers in terms of sequential processing and parallel computation. Explain one important advantage of Transformers and one limitation during autoregressive text generation.

RNNs proccess toknes sequencially, passsing hiden-state informasion from one stpe to the next, while Transfomers can process all input positons in paralell during trainning. This paralelism often makes Transformer training faster, and self-attension directely models long-range dependancies. However, autoregressiv text generation is still sequencial: the model must genrate one tokn before it can predic the next. This limits generation speed and can make decoding computional expensiv.

## Part II: Programming

### Q1: NLP Preprocessing Pipeline

The solution is implemented in [part2_Q1_NLP_Prepocessing_Pipeline.py](part2_Q1_NLP_Prepocessing_Pipeline.py). It tokenizes the provided sentence into words and punctuation, removes common English stopwords, and applies NLTK's Porter stemmer.

### Run the Solution

The Bash launcher creates an isolated `.venv-part2-q1` environment and installs NLTK if it is not already available. Run it with Bash:

```bash
bash run_part2_Q1_NLP_Prepocessing_Pipeline.sh
```

The launcher prints:

```text
Original Tokens: ['NLP', 'techniques', 'are', 'used', 'in', 'virtual', 'assistants', 'like', 'Alexa', 'and', 'Siri', '.']
Tokens Without Stopwords: ['NLP', 'techniques', 'used', 'virtual', 'assistants', 'like', 'Alexa', 'Siri', '.']
Stemmed Words: ['nlp', 'techniqu', 'use', 'virtual', 'assist', 'like', 'alexa', 'siri', '.']
```

The stopword list is explicitly defined in the Python file, and punctuation is retained through the filtering and stemming steps.

### Short Answers

1. **Stemming vs. lemmatization:** Steming removs word endngs using simpl rulz and may produc a non-dictionary form. Lemmatiztion uses vocabularly and often gramattical contex to retur a valid base form. For exampel, steming “running” may give “run”; lemmatiztion also gives “run,” while “better” can be lemmatizd to “good” when its contex indicats an adjectiv.

2. **Why remove stopwords?** Removng commen words can reduse the numbr of featurz in search and som text-classification taskes, leting the modle focus on more informativ termz. It can be harmfull when a stopword caries importent meaning: removng “not” from “not good,” for exampel, reverses the sentiment. The choice shoud depend on the task and on which words the stopword list removs.

### Q2: Scaled Dot-Product Attention

The solution is implemented in [part2_Q2_Scaled_Dot_Product_Attention.py](part2_Q2_Scaled_Dot_Product_Attention.py). It computes $QK^T$, scales the scores by $\sqrt{d_k}$, applies a stable row-wise softmax, and multiplies the attention weights by $V$.

Run the solution with its isolated NumPy environment:

```bash
bash run_part2_Q2_Scaled_Dot_Product_Attention.sh
```

For the provided matrices, $d_k = 4$. The dot-product scores are $[[2, 0], [0, 2]]$, and the scaled scores are $[[1, 0], [0, 1]]$. The output is:

```text
Attention Weights:
[[0.7311 0.2689]
 [0.2689 0.7311]]
Final Output:
[[2.0758 3.0758 4.0758 5.0758]
 [3.9242 4.9242 5.9242 6.9242]]
```

#### Short Answers

1. **Why divide by $\sqrt{d_k}$?** The dot scors can grow as key dimenssion increeses, making softmax too peakked and gradints smal. Dividing by $\sqrt{d_k}$ keeps magnitudes managable and supports more stabel trainning.

2. **How does self-attention model word relationships?** Self-attension allws each tokn compair its query with keys from other toknes in the sentnce. The resulting weigts combine their valus, giving each position a context-aware represntation and helping the modle learn dependancies between nearby or far-apart words.
