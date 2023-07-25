Title: 台灣資料科學年會之系列活動：深入淺出深度學習 (Dive into Deep Learning)  
Slug: dive-into-deep-learning-datasci-tw  
Date: 2017-08-12 17:02:14  
Authors: fkz  
Category: Conf/Meetup  
Tags: Deep Learning, DNN, CNN, RNN, Machine Learning  
Summary: 《資料科學年會系列活動：深入淺出深度學習》筆記  
  
  
+ Links  
    + <http://foundation.datasci.tw/dive-deep-learning-170812/>  
    + <https://dsc.kktix.cc/events/series-events-081213>  
+ Slides  
    + [DiveDL_0326_v1.pdf](https://drive.google.com/file/d/0B9cCeTKOkfWIVF9CeXpXaC1lUVk/view?usp=sharing)  
  
---  
  
### Regression  
  
+ 適用場景  
    + 股票預測  
    + 無人車方向調整  
    + 推薦系統  
+ 步驟  
    + 決定 Model  
    + 評估所使用的函數夠不夠好  
        + Loss Funciton  
            + output 分數低，代表 loss 少，所以比較好。  
    + 找出表現最好的 Loss Function  
        + 利用 Gradient Descent 來找  
            + 縱軸為 L 的 output，橫軸為 w  
            + L 對 w 偏微分，取得其切線斜率  
            + 切線斜率為負時，增加 w，來取得較低的 L output  
            + 切線斜率為正時，減少 w，來取得較低的 L output  
        + 非 Linear 的話，會出現 Local optimal 和 Global optimal 的狀況  
    + 得到 Model  
    + Model Generalization  
        + 嘗試不同的 Model  
        + 太過複雜的 Model 會出現 Overfitting 的狀況  
  
---  
  
### Classification  
  
+ 分類  
    + Binary Classification  
        + Yes/No  
        + Example  
            + Spam Filtering  
                + 把 email 裡面的詞都當作一個 feature，透過 trained model 來得到 Boolean 的結果。  
    + Multi-Class Classification  
        + 判斷是哪個種類  
        + Example  
            + 餵入圖片，判斷是哪種動物  
            + 判斷新聞是屬於哪一種主題  
  
---  
  
# Introduction to ML & DL  
  
## Basic Deep Learning  
  
+ Stacked function learned by machine  
+ Deep Learning 三步驟  
    + Define a set of function  
    + Godness of function  
    + pick the best function  
    + (和 ML 很像）  
  
  
#### Step 1: Define a set of function  
  
+ Neural Network  
    + Neuron: input, weights, bias, Activation function  
    + 將多個 Neuron 組合在一起，形成 Neuron Network  
    + 愈多層的話需要調整的參數越多  
    + 不同的 Connections 可以形成不同的 Neural Network  
        + Fully-Connected Feedforward Network  
            + 每一個 Neuron 都跟前一個相連，會一直把數值傳下去。  
            + Input Layer + Hidden Layers + Output Layer  
            + "Deep" means multiple hidden layers  
                + DNN 的 hidden layers 至少要大於 2  
    + Why Deep?  
        + Fat + Shallow vs Thin + Deep  
            + 在數學上被證明是可以用一層很寬的 layer 來取代多層的 layers，但為什麼不用？  
            + 因為只用一層的話會需要使用到更多的 Neurons。（可以用類似 Logic Gates 簡化的方式來想）  
        + Examples  
            + AlexNet (2012): 8 layers, 16.4%  
            + VGG (2014): 19 layers, 7.3%  
            + GoogleNet (2014): 22 layers, 6.7%  
            + Residual Net (2015): 152 layers, 3.57%  
                + 人類自己把所有的 training data 看完後下去做測試，error rate 大概是 4~5%  
                + 首度超越人類  
                + 因為疊了很多層，所以可能有些資訊會在傳遞中遺失，所以使用了 Special structure，會把一些一開始就學到的很重要 information 直接保留下來，確保不會在傳遞過程中遺失。  
                + 使用 Softmax layer 來當 Output layer  
                    + 可以對 output 的數值做 normalize，直接以機率的方式呈現結果。  
                + Example  
                    + Handwriting Digit Recognition  
        + Input => Neuron Network => Output  
        + Neuron Network => A function set containing the candidates  
        + FAQ  
            + 要用幾層？每層要用多少 Neuron？  
                + 試誤 + 直覺  
            + 我們可以自己設計 neuron network structure 嗎？  
                + 有很多不同的結構可以選擇  
            + 有辦法讓程式自動幫我們決定要使用哪種 structure  
                + 有，但還沒有被研究的非常透徹。  
  
  
#### Step 2: goodness of function  
  
+ Loss  
    + A good function should make the loss of all examples as small as possible.  
+ Total Loss  
    + As small as possible  
    + Find a function in function set that minimizes total loss  
    + Find the network parameter `θ*` that minimize total loss  
  
  
#### Step 3: pick the best function  
  
+ Gradient Descent  
    + Local minima  
        + Very slow at the plateau  
        + Stuck at saddle point  
        + Stuck at local minima  
        + Gradient descent never guarantee global minima  
            + Use different & random initial point to reach different minima  
    + Even AlphaGo using this approach  
        + 其實 AI 並沒有那麼厲害，他們也是像探索戰爭迷霧那樣，一步一步去探索和嘗試的。  
  
  
## Deep Learning Toolkit  
  
+ Backpropagation  
    + An efficient way to compute `∂L/∂w` in neural network  
+ Frameworks  
    + TensorFlow  
        + 比較多人在用且資料比較多  
    + Torch  
    + Pytorch  
        + 比較多人在用且資料比較多  
    + Theano  
        + AlexNet 的作者  
    + Microsoft CNTK  
    + Caffe  
    + DSSTNE  
    + mxnet  
    + Chainer  
+ 有 input 和 output，就可以使用這些工具幫你找尋合適的 Function Set  
  
  
#### Keras  
  
+ TensorFlow 和 Theano 的 Wrapper  
+ 非常容易寫  
+ 雖然可以細部調整的地方沒有直接使用 TensorFlow 和 Theano 來的多，但有足夠的彈性做一些調整。  
  
  
## Learning Recipe  
  
+ 在 Training Data 上的表現好嗎？  
    + 不好  
        + 重新 train  
        + 可能原因  
            + no good function exists: bad hypothesis function set => reconstruct the model architecture  
            + cannot find a good function: local optima => change the training strategy  
  
+ 在 Testing Data 上的表現好嗎？  
    + 不好的話就是 Overfitting，要重新 train model  
  
### Overfitting  
  
+ High variance  
+ 可能的解法  
    + more training samples  
    + dropout  
        + 每次 random 讓數個 node 不工作  
    + 降維  
        + PCA  
  
## Concluding Remarks  
  
+ 3 steps of Basic Machine Learning 很重要  
+ Stacked functions  
  
---  
  
# Part II: Variants of Neural Nets  
  
+ Convolutional Neural Network (CNN)  
+ Recurrent Neural Network (RNN)  
  
## Convolutional Neural Network (CNN)  
  
+ 在影像處理上被廣泛使用  
  
### Why CNN for Image?  
  
+ Some patterns are much smaller than the whole image.  
    + A neuron does not have to see the whole image to discover pattern.  
    + Connecting to small region with less parameters.  
+ The same patterns appear in different regions.  
+ Subsampling the pixels will not change the object.  
    + 算是處理 image 上獨有的特性  
    + We can subsmaple the pixel to make image smaller  
        + Less parameters for the network to process the image  
  
### The Whole CNN  
  
+ Image => `{Convolution => Max Pooling}*N` => Flatten => Fully Connected Feedforward Network  
+ 特性  
    + 和 Convolution 有關  
        + Some patterns are much smaller than the whole image.  
        + The same patterns appear in different regions.  
    + 和 Max Pooling 有關  
        + Subsampling the pixels will not change the object  
  
### Image Recognition  
  
+ Local Connectivity  
    + Neurons connected to a small region  
+ Parameter Sharing  
    + The same feature in different positions  
        + Neurons share the same weights  
    + Different features in the same position  
        + Neurons have different weights  
  
+ Convolutional Layers  
+ Hyper-parameters of CNN  
    + Stride  
        + 要隔多少去算下一個 information  
        + 如果覺得這張圖上的 information 是非常鬆散的，那 stride 就可以設高一點，讓他多隔幾層再去找 pattern  
        + 如果覺得這張圖上的 information 是非常緊密的，那 stride 就只能設低一點。  
    + Padding  
        + 讓每一層的數值不要減少的太快  
+ Pooling Layer  
    + Max Pooling  
        + 把最大的值保存下來  
        + Image processing 比較常使用 Max Pooling  
    + Average Pooling  
        + 把平均的數值保存下來  
    + 壓縮資訊，減少下一層需要參數的量，使其更有效率。  
+ Why Deep Learing works for image recogniton?  
    + 每個 node 會學習一些簡單的筆劃，組合起來後才會變成一個字。  
    + 愈前面的結果會愈簡單和基本，可能只是些筆劃，經過 Convolution 和 Max Pooling 後，可以用被壓縮後的較少資訊學習比較抽象的組合。  
+ Fully-Connected Layer  
    + Global feature extraction  
    + Softmax Layer: Classifier  
+ What CNN Learned  
    + [AlexNet]  
+ DNN are easily fooled  
    + 可以捏造一些奇怪的 input，看起來只是一些 noise，因為 DNN 會特別著重某些 pattern，所以會將這些圖誤判為目標物。  
    + 滿多資安的論文現在在探討攻擊 DNN 的手法。  
    + Visualizing CNN  
        + 調整 noise 的 input，使其 filter response 更接近目標物的 filter response，有點像是反過來的 training  
        + 透過 Gradient Ascent 去微調  
        + <https://deepdreamgenerator.com/>  
        + Deep Style  
            + 一張圖保留 Content  
            + 另一張圖保留 Style  
            + 然後去調整保留 Content 的那張圖，並使用另一張圖的 Style  
+ Go Playing （下圍棋）  
    + Conditions  
        + Input: 目前棋盤的狀況  
        + Output: 下一步應該下哪裡？  
        + 19x19 vector  
        + black = 1, white = -1, none = 0  
    + Fully-Connected Feedforward Network could be used, but why CNN?  
        + Some patterns are much smaller than the whole image  
            + 棋譜會有一些固定的 pattern  
        + The same patterns appear in different regions  
            + 同樣的 pattern 有可能出現在棋盤上不同的地方  
        + Subsampling the pixels will not change the object  
            + 把棋譜作 subsampling 會讓整個棋譜的結果失真  
            + 因為 Subsampling 只和 Max Pooling Layer 有關，所以在 AlphaGo 的論文中有提到只有使用 Convolutional Layer，把 Max Pooling Layer 拿掉了。  
            + 如果不是很熟悉下圍棋以及 DNN 的 domain knowledge 的話，直接拿 CNN 去做是訓練不出什麼結果的，這也是為什麼 Alpha Go 會需要像黃士傑博士這樣會下圍棋又懂 Machine Learning 的人。  
  
## Recurrent Neural Network (RNN)  
  
+ Example Application  
    + Slot Filling  
        + Solved by Feedforward Network?  
            + Input: a word  
            + Output: probability distribution that the input word belonging to the slots  
            + Problem  
                + Arrive Taipei on November 2nd  
                    + Taipei 是目的地  
                + Leave Taipei on November 2nd  
                    + Taipei 是出發地  
        + 用 RNN 來解決  
+ One-Hot Vector  
    + 1-of-N Encoding  
    + 有 N 個詞就用 N 維的矩陣來表示，如果該字有出現的話值就是 1，其他值就會是 0。  
+ RNN  
    + The output of hidden layer are stored in the memory  
    + Memory can be considered as another input  
    + 每一層都是拿現在看到的資訊和上一層的 memory 當成 input  
    + 不會因為層數比較多（語句比較長）就導致參數變多，參數的數量都是一樣的。  
    + 存在 memory 的 value 會影響最終的 prediction  
+ Deep RNN: 多層  
+ Why use RNN in language processing?  
    + 因為語言是有時間順序的  
    + 如果 input 是時間順序非常重要的話，就可以考慮用 RNN 來做。  
+ Bidirectional RNN  
    + 將 input 反向來作並加入 memory  
    + 缺點是會比較費時  
+ Learning Target  
    + 會比較複雜一些  
    + 一句話有五個詞，訓練一句話等於要拿到 5 個 targets  
        + 因為要判斷每個詞的 label  
        + 因為彼此是有順序相依性的，所以 loss 會是每層 layer 相加  
    + Training Difficulty - Rough Error Surface  
        + The error surface is either very flat or very steep  
            + 非常難學習  
            + 所以會有一些各式各樣的小技巧出現在 RNN 裏面  
                + Clipping  
        + Large `δL/δw` => Large Learning rate  
+ Many-to-One  
    + Input is a vector sequence, but output is only one vector  
+ Many-to-Many (Output is shorter)  
    + Both input and output are sequences, but the output is shorter  
    + E.g. Speech Recognition  
        + Input: vector sequence  
        + Output: character sequence  
        + Connectionist Temporal Classification (CTC)  
            + 加了一個額外的 symble `ϕ` 來代表 Null  
            + `好好好棒棒棒棒` vs `好ϕϕ棒ϕϕ棒`  
                + 這樣就可以知道到底是一個棒還是兩個棒  
+ Many-to-Many (Output is no limitation)  
    + Both input and output are sequences with different lengths  
        + Sequence to sequence learning  
    + E.g. Machine Translation  
        + "Machine Learning" => "機器學習"  
        + Problem: Don't know when to stop  
            + 加上一個代表斷句或結尾的符號  
+ Image Caption Generation  
    + 給一張圖，描述出圖裏面有什麼  
    + 將圖餵給 CNN 後，會產出一個代表整章圖的 vector  
    + 將 vector 餵給 RNN  
    + Example  
        + <http://www.captionbot.ai/>  
+ Video Caption Generation  
    + 每一個 Video 用 CNN  
    + Video 裡面的每一張 Image 用 RNN  
+ Chit-Chat Bot  
    + 拿對話中其中一方的話當 input，另一方的話當 output 去訓練。  
    + 比較常用到 [LSTM](https://en.wikipedia.org/wiki/Long_short-term_memory)  
        + <http://colah.github.io/posts/2015-08-Understanding-LSTMs/>  
    + Sci-Fi Short Film generated by AI - SUNSPRING  
        + <https://www.youtube.com/watch?v=LY7x2lhqj>  
+ Attention and Memory  
    + Question => Organize => Answer  
        + 被稱做 Attention  
        + 只會拿有用的資訊出來回答  
    + Attention on Sensory Info  
        + Info from the sensors => Sensory Memory == Attention ==> Working Memeory == Encode ==> Long-term Memory  
        + Logn-term Memory == Retrieval ==> Working Memory  
    + Machine Translation with Attention  
        + Keyword: "Attentional sequence to sequence model"  
        + 先用 match 判斷跟哪一塊的相似程度最高  
        + 目前 Google Translation 就是用這個 model 實現的  
    + Speech Recognition with Attention  
        + 比較深色的地方就是 Attention 比較高的部份  
    + Image Captioning with Attention  
        + 從錯誤的 prediction 中去瞭解判斷錯誤的可能原因  
    + Video Captioning with Attention  
    + Reading Comprehension  
        + Document => 被切分成不同的詞被當作 feature  
        + Question == RNN ==> q vector  
        + 根據 q vector 去決定哪一個句子最相關，再放入 DNN 裡頭去回答  
        + Hopping  
            + Memory Network  
                + 有可能第一次得到的結果不夠準確  
                + 用抽取出來資訊再做一次 Attention，再得到新的 information 並把它抽取出來。  
    +  When the input is a very long sequence or an image  
        + Pay attention on partial of the input object each time  
    + In RNN/LSTM, larger memory implies more parameters  
        + Increasing memory size will not increasing parameters  
+ Neural Turing Machine  
    + an advanced RNN/LSTM  
    + 把 Long-term Memory 裡頭的資訊 retrieve 出來  
  
---  
  
# Part III: Beyond Supervised Learning & Recent Trends (Unsupervised Learning)  
  
## Introduction  
  
+ Big data != Big annotated data  
    + What can we do if there is no sufficient labelled training data?  
+ Machine learning techniques include:  
    + Supervised learning (if we have labelled data)  
    + Reinforcement learning (if we have an environment for reward)  
    + Unsupervised learning (if we do not have labelled data)  
  
  
### Semi-Supervised Learning  
  
+ 應用環境  
    + 沒有全部的 input data 都有 label 時  
+ 概念  
    + The distribution of the unlabeled data provides some cues  
  
  
### Transfer Learning  
  
+ 應用環境  
    + Input data 中沒有 output 想要的 class label  
+ 概念  
    + Using sufficient labeled data to learn a CNN  
    + Using this CNN as feature extractor  
+ 舉例  
    + 研究生 vs 漫畫家  
        + 研究生 == 漫畫家  
        + 指導教授 == 責任編輯  
        + 跑實驗 == 畫分鏡  
        + 投稿期刊 == 投稿 Jump  
  
  
### Unsupervised Learning  
  
+ 概念  
    + Representation Learning: 化繁為簡  
    + Generative Model: 無中生有  
    + 化繁為簡和無中生有的過程是相反的  
        + 化繁為簡：拿到很多跟樹有關的圖片，簡化得出一個代表樹的 output，學習到的是這些圖片共同的特徵  
        + 無中生有：code 經過 function 之後就生成很多跟樹很像的圖片  
    + Latent Factors  
        + 共同特徵  
+ 化繁為簡 Representation Learning  
    + Autoencoder  
        + 希望能把比較重要的資訊壓縮到比較小的 pattern 裏面  
        + represent the images of digits in a more compact way  
        + Output of the hidden layer is the code  
        + Deep autoencoder  
        + Similar Image Retrieval  
        + 可以把 image 最重要的 feature 保留起來  
        + For DNN Pre-Training  
    + Word Vector/Embedding  
        + Machine learn the meaning of words from reading a lot of documents without supervision  
        + A word can be understood by its context  
        + 類似的句型中，同樣位置的不相同詞可能有高度相關性  
        + Prediction-Based  
            + 給前面的字 predict 下一個字 (Linear Model)  
                + 前面的字當 input，後面的字當 output，一直這樣接下去。  
            + Various Architecture  
                + Continuous bag of word (CBOW) model  
                    + 給兩邊的字 predict 中間的字  
                + Skip-gram  
                    + 給中間的字 predict 兩邊的字  
        + 完全不需要 label data，程式可以自己去學習這些詞之間的關係  
+ 無中生有 Generative model  
    + 概念  
        + 想讓程式自動幫我們生不同的 training data  
        + <https://blog.openai.com/generative-models/>  
    + PixelRNN  
        + To create an image, generating a pixel each time  
        + Can be trained just with a large collection of images without any annotation  
    + Generative Adversarial Network (GAN)  
        + Discriminative vs Generative Models  
            + Discriminative  
                + learns a function that maps the input data (x) to some desired output class label (y)  
                    + directly learn the conditional distribution P(y|x)  
            + Generative  
                + tries to learn the joint probability of the input data and labels simultaneously, i.e. P(x,y)  
                    + can be converted to P(y|x) for classification via Bayes rule  
            + generative models have the potential to understand and explain  
    the underlying structure of the input data even when there are no labels  
        + 跟演化的感覺有點類似  
            + Generator  
                + Hidden Layer (code) ===decode===> output layer => output  
        + 概念  
            + Two competing neural networks: generator & discriminator  
            + noise ==generator==> generator sample => discriminator ==yes/no==> data sample  
            + generator 生出圖片，discriminator 判斷這張產生出來的圖片是不是真的  
            + 彼此之間會互相競爭學習  
            + Training two networks jointly => the generator knows how to adapt its parameters in order to produce output data that can fool the discriminator  
        + Examples  
            + [Cifar-10](https://openai.com/blog/generative-models)  
            + Generated Bedrooms  
            + [Comics Drawing](https://github.com/mattya/chainer-DCGAN)  
            + Pokémon Creation  
  
  
### Reinforcement Learning  
  
+ 概念  
    + Agent, Environment 之間彼此是可以互動的  
    + Environment 會給 Agent 一個 Observation  
    + Agent 會對這個 Observation 做出 Action  
    + Environment 會根據 Action 的不同給予 Agent 不同的 Reward  
    + 根據 Reward 來學習要做或不做哪些行為  
    + Agent learns to take actions to maximize expected reward.  
    + 困難點  
        + 可能的 sequence 是非常龐大的  
        + 很難調整，因為只拿得到一連串的 Actions 之後的 Reward，無法確定到底是錯在哪一個 Action  
        + Reward may be delayed  
+ Supervised vs Reinforcement  
    + Supervised  
        + 就像在學校裏面，每一步都有老師會帶領你，告訴你每一步是對是錯  
    + Reinforcement  
        + 做了一連串的動作以後，到一個正面或負面的回饋，不確定到底問題出錯在哪一個地方。  
+ 範例  
    + 走迷宮  
+ Reinforcement Learning Approach  
    + Policy-based RL  
        + Search directly for optimal policy  
    + Value-based RL  
        + Estimate the optimal value function  
    + Model-based RL  
        + Build a model of the environment  
        + Plan (e.g. by lookahead) using model  
+ Deep Reinforcement Learning  
    + Idea: deep learning for reinforcement learning  
        + Use deep neural networks to represent  
        + Optimize loss function by SGD  
    + Value Function Approximation  
    + Q-Networks  
        + Q-networks represent value functions with weights  
    + Q-Learning  
        + Goal: estimate optimal Q-values  
            + Optimal Q-values obey a Bellman equation  
            + Value iteration algorithms solve the Bellman equation  
    + Deep Q-Networks (DQN)  
    + Stability Issues with Deep RL  
        + Naive Q-learning oscillates or diverges with neural nets  
            + Data is sequential  
                + Successive samples are correlated, non-iid (independent and  
identically distributed)  
            + Policy changes rapidly with slight changes to Q-values  
                + Policy may oscillate  
                + Distribution of data can swing from one extreme to another  
            + Scale of rewards and Q-values is unknown  
                + Naive Q-learning gradients can be unstable when backpropagated  
    + Stable Solutions for DQN  
        + DQN provides a stable solutions to deep value-based RL  
            + Use experience replay  
                + Break correlations in data, bring us back to iid setting  
                + Learn from all past policies  
            + Freeze target Q-network  
                + Avoid oscillation  
                + Break correlations between Q-network and target  
            + Clip rewards or normalize network adaptively to sensible range  
                + Robust gradients  
    + DQN in Atari  
        + Goal: end-to-end learning of values Q(s, a) from pixels  
            + Input: state is stack of raw pixels from last 4 frames  
            + Output: Q(s, a) for all joystick/button positions a  
            + Reward is the score change for that step  
    + DQN in E2E Task-Completion Bot  
        + Simulated User  
            + Generate interactions based on a predefined fake goal  
            + Automatically learn strategy by training on the simulated data  
    + Model-Based Deep RL  
        + Goal: learn a transition model of the environment and plan based on the transition model  
        + Model-based deep RL is challenging, and so far has failed in Atari  
        + Model-Based Deep RL in AlphaGo  
            + Monte-Carlo tree search (MCTS)  
                + MCTS simulates future trajectories  
                + Builds large lookahead search tree with millions of positions  
                + State-of-the-art Go programs use MCTS  
            + Convolutional Networks  
                + 12-layer CNN trained to predict expert moves  
                + Raw CNN (looking at 1 position, no search at all) equals performance of MoGo with 105 position search tree  
    + More Applications  
        + AlphaGo  
        + [Flying Helicoptor](https://www.youtube.com/watch?v=0JL04JJjocc)  
        + [Driving](https://www.youtube.com/watch?v=0xo1Ldx3L5Q)  
        + [Google Cuts Its Giant Electricity Bill With DeepMind-Powered AI](https://www.bloomberg.com/news/articles/2016-07-19/google-cuts-its-giant-electricity-bill-with-deepmind-powered-ai)  
    + [OpenAI Universe](https://universe.openai.com/)  
        + Software platform for measuring and training an AI's general  
intelligence via the [OpenAI gym](https://gym.openai.com/) environment  
  
---  
  
# Conclusion  
  
+ Machine Learning & Deep Learning 需要  
    + 足夠的運算資源  
    + 各種經驗及技巧  
  
---  
  
### FAQ  
  
+ Deep Learning 的 model 會是 non-linear 的  
+ 機器翻譯目前在台灣的狀況如何？要如何著手？  
    + 機器翻譯的話，目前在國外算是滿成熟的，目前會使用 RNN 來做。  
    + 如果是台語的部份，目前好像比較少看到，會是個還有發展空間的方向。  
+ 為什麼需要 Activation Function？他在 Deep Learning 中扮演的角色是什麼？  
    + 處理 non-linear 的部份，如果沒有 Actication Function 的話，多層的結果用一層就可以去表示。  
+ 為什麼會選擇 Sigmoid 作為 Activation Function?  
    + 其實有很多種 Activation Function，拿 Sigmoid 來講是因為他比較簡單，把 output 壓在 -1~1 之間  
    + 另外一個比較常見的是 Relu 這個 Activation Function  
        + 0 以下的就刪除掉  
        + 避免 information 被壓縮的太小，用來解決經過太多層之後 information 被壓得太小。  
+ Deep Learning 的最佳化要具備哪些能力  
    + 如果是純理論的部份會跟數學方面相關。  
    + 但如果是實務上的 task，會跟該 task 的 domain knowledge 比較相關。  
+ CNN 對於影像旋轉是否也有夠好的識別度？  
    + 第一個作法就是把你的 training data 也旋轉過再丟進去訓練  
    + 另外一個作法是使用會考慮旋轉相關的 model 放進去 train，input data 不需要特別旋轉過  
+ 學 Machine Learning 需要學習微積分、統計和線性代數嗎？  
    + 基本的微積分概念是要的，但沒有很複雜，如果完全不會微分的話要學一下。  
    + 統計的話基本概念要有，但不會太多。  
     線性代數是最重要的，會看到很多 vector, matrix 以及 space 上的處理，有很多假設是必須要知道的。  
