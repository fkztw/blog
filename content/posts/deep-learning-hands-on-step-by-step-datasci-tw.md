Title: 台灣資料科學年會之系列活動：手把手的深度學習實務  
Slug: deep-learning-hands-on-step-by-step-datasci-tw  
Date: 2017-08-13 17:08:45  
Authors: fkz  
Category: Conf/Meetup  
Tags: Deep Learning, Keras, CNN, DNN  
Summary: 《台灣資料科學年會之系列活動：手把手的深度學習實務》筆記  
  
  
+ <http://foundation.datasci.tw/step-by-step-dl-170813/>  
+ [Slides](https://drive.google.com/file/d/0B9cCeTKOkfWIbWtjdWJaRl9YRmM/view?usp=sharing)  
  
---  
  
### 六步完模 – 建立深度學習模型  
  
1. 決定 hidden layers 層數與其中的 neurons 數量  
2. 決定該層使用的 activation function  
3. 決定模型的 loss function  
4. 決定 optimizer  
    + Parameters: learning rate, momentum, decay  
5. 編譯模型 (Compile model)  
6. 開始訓練囉!(Fit model)  
  
---  
  
### 關於 `validation_split` 要注意的小地方  
  
用 Keras 的 `validation_split` 之前要記得把資料先弄亂，  
因為它會從資料的最尾端開始取，  
如果沒有弄亂的話切出來的資料 bias 會很大。  
可以使用 `np.shuffle` 來弄亂  
  
---  
  
### Functional API  
  
+ Why “Functional API” ?  
    + All layers and models are callable (like function call)  
```  
from keras.layers import Input, Dense  
input = Input(shape=(200,))  
output = Dense(10)(input)  
```  
    + 類似 f(x) 的寫法  
        + Dense(10) == f  
        + input == x  
    + 好處是可以 assign 給自己後再用 for loop 很快建非常多層 layer，不用一直用 `model.add`  
    + Easy to manipulate various inpout sources  
```  
x1 = input(shape=(10,))  
y1 = Dense(100)(x1)  
  
x2 = input(shape=(20,))  
new_x2 = keras.layers.concatenate([y1,x2])  
output = Dense(200)(new_x2)  
  
Model = Model(inputs=[x1,x2],outputs=[output])  
```  
  
---  
  
### Loss function  
  
+ 為什麼 Cross-entropy 比 Squared error 好？  
    + Cross-entropy 的 Gradient 比較大，學習速度比較快。  
    + [The error surface of logarithmic functions is steeper than  
that of quadratic functions.](http://www.complex-systems.com/pdf/02-6-1.pdf)  
+ How to select Loss function  
    + Classification 常用 cross-entropy  
        + 搭配 softmax 當作 output layer 的 activation function  
    + Regression 常用 mean absolute/squared error  
    + 對特定問題定義 loss function  
        + Unbalanced dataset, class 0 : class 1 = 99 : 1  
            + Class 1 做錯的話，給它 penalty 99  
        + Self-defined loss function  
  
---  
  
### Learning Rate  
  
+ 觀察 Loss，如果有振盪的話，代表 learning rate 可能太大  
+ 觀察 Loss，下降的太緩慢的話，代表 learning rate 可能太小  
+ 選擇適合的 learning rate 對於 training model 會是很大的影響  
+ 通常不會大於 0.1  
+ 一次調整一個數量級  
  
---  
  
### Activation Function  
  
> Activation Function 可能是最重要的  
  
+ Sigmoid, Tanh, Softsign  
    + Sigmoid 介於 0~1 之間  
    + Tanh, Softsign 介於 -1~1 之間  
    + 值域是有限制的  
        + Input 過大或過小影響其實不大  
+ Derivatives of Sigmoid, Tanh, Softsign  
    + Input 過大或過小時，Gradient 太小，學習就會很慢  
    + 所以通常太深的 model 不建議用這 3 個 Activation Function  
+ Drawbacks of Sigmoid, Tanh, Softsign  
    + Vanishing gradient problem  
        + 原因: input 被壓縮到一個相對很小的output range  
        + 結果: 很大的 input 變化只能產生很小的 output 變化 => Gradient 小 => 無法有效地學習  
    + 特別不適用於深的深度學習模型  
+ ReLU, Softplus  
    + > 在 TensorFlow 上用 Softplus 好像會遇到一些問題  
+ Derivatives of ReLU, Softplus  
    + ReLU 在輸入小於零時, gradient 等於零,會有問題嗎?  
        + 小於 0 的時候可能就不學習了，所以有人提出了 Leaky ReLU  
+ Leaky ReLU  
    + Allow a small gradient while the input to activation function smaller than 0  
    + 在 input < 0 時，還是給他一點些微的斜率  
    + > 在用 ReLU 的時候 Learning rate 可能要用小一點，效果會比較好。  
  
---  
  
### Optimizer  
  
+ SGD – Stochastic Gradient Descent  
    + Stochastic gradient descent  
    + 支援 momentum, learning rate decay, Nesterov momentum  
        + `keras.optimizer.SGD(lr=0.01, momentum=0.0, decay=0.0, nesterov=False)`  
    + Momentum 的影響  
        + 無 momentum: `update = -lr*gradient`  
        + 有 momentum: `update = -lr*gradient + m*last_update`  
    + Learning rate decay after update once  
        + 屬於 `1/t decay => lr = lr / (1 + decay*t)`  
        + t: number of done updates  
    + Momentum vs Nesterov Momentum  
        + Momentum  
            + 先算 gradient  
            + 加上 momentum  
            + 更新  
        + Nesterov Momentum  
            + 加上 momentum  
            + 再算 gradient  
            + 更新  
        + 兩者出來的效果沒有太大的差別，沒有誰比較好，只是聽到有人用 Nesterov 的時候要知道差別。  
+ Adagrad – Adaptive Learning Rate  
    + 因材施教:每個參數都有不同的 learning rate  
    + 根據之前所有 gradient 的 root mean square 修改  
    + Feature scales 不同,需要不同的 learning rates  
    + 每個 weight 收斂的速度不一致  
        + 但 learning rate 沒有隨著減少的話  bumpy  
    + 根據之前所有 gradient 的 root mean square 修改  
    + 老馬識途,參考之前的經驗修正現在的步伐  
    + 不完全相信當下的 gradient  
+ RMSprop – Similar with Adagrad  
    + 另一種參考過去 gradient 的方式  
        + `keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)`  
    + Adagrad 不管多久之前的經驗都把其權重視為相同的，RMSprop 就是針對這部份做改進，愈久之前的經驗其權重會變得愈低。  
    + 這個 Activation 是作者在 Coursera 授課時提出的，沒有論文，所以大家在論文使用這個 activation function 的時候都會 cite 那個 coursera 課程的網址，而且還不少人用的 XDDD  
+ Adam – Similar with RMSprop + Momentum  
    + Close to RMSprop + Momentum  
    + [ADAM: A Method For Stochastic Optimization](https://arxiv.org/pdf/1412.6980v8.pdf)  
    + In practice, 不改參數也會做得很好  
        + `keras.optimizer.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)`  
+ Nadam – Adam + Nesterov Momentum  
+ How to select Optimizer  
    + 一般的起手式: Adam  
        + Adaptive learning rate for every weights  
        + Momentum included  
    + Keras 推薦 RNN 使用 RMSProp  
        + 在訓練 RNN 需要注意 explosive gradient 的問題 => clip gradient 的暴力美學  
    + RMSProp 與 Adam 的戰爭仍在延燒  
        + 各有千秋  
  
---  
  
### 處理 Overfitting  
  
+ Regularization  
    + 限制 weights 的大小讓 output 曲線比較平滑  
    + Weight 較小，input 的差異對 output 產生的影響比較沒有那麼大  
    + α (Regularizer) 是用來調整 regularization 的比重  
        + 避免顧此失彼 (降低 weights 的大小而犧牲模型準確性)  
避免顧此失彼 (降低 weights 的大小而犧牲模型準確性)  
    + L1 and L2 Regularizers  
        + L1 norm: Sum of absolute values  
        + L2 norm: Root mean square of absolute values  
+ Early Stopping  
    + 希望在 Model overfitting 之前就停止 training  
    + 假如可以停在 loss 最低的點的話就好了  
    + Early Stopping in Keras  
        + `from keras.callbacks import EarlyStopping`  
        + `early_stopping=EarlyStopping(monitor='val_loss', patience=3)`  
        + monitor: 要監控的 performance index  
        + patience: 可以容忍連續幾次的不思長進  
+ Dropout  
    + What is Dropout  
        + 原本為 neurons 跟 neurons 之間為 fully connected  
        + 在訓練過程中,隨機拿掉一些連結 (weight 設為0)  
    + 會造成 training performance 變差  
        + Error 變大 => 每個 neuron 修正得越多 => 做得越好  
    + Implications  
        + 增加訓練的難度，在真正的考驗時爆發  
        + Dropout 可視為一種終極的 ensemble 方法，N 個 weights 會有 2^N 種 network structures  
    + 通常只加在 hidden layer，不會加在 output layer，因為影響太大了，除非 output layer 的 dimension 很大。  
    + 注意事項  
        + 「不要一開始就加入 Dropout」*3  
        + 確定有遇到 Overfitting 再加 Dropout  
        + Dropout 會讓 training performance 變差  
        + 確定 performance 夠好再加 Dropout，不然 Performance 變低，就算解掉了 Overfitting，出來的結果也沒啥用。  
        + Dropout 是在避免 overfitting，不是萬靈丹  
        + 參數少時，regularization  
  
---  
  
### Callbacks: 善用 Callbacks 幫助你躺著 train models  
  
####  Callback Class  
```  
from keras.callbacks import Callbacks  
  
Class LossHistory(Callbacks):  
    def on_train_begin(self, logs={}):  
        self.loss = []  
        self.acc = []  
        self.val_loss = []  
        self.val_acc = []  
  
    def on_batch_end(self, batch, logs={}):  
        self.loss.append(logs.get('loss'))  
        self.acc.append(logs.get('acc'))  
        self.val_loss.append(logs.get('val_loss'))  
        self.val_acc.append(logs.get('val_acc'))  
  
    loss_history = LossHistory()  
```  
  
#### Callback 的時機  
  
+ on_train_begin  
+ on_train_end  
+ on_batch_begin  
+ on_batch_end  
+ on_epoch_begin  
+ on_epoch_end  
  
  
#### LearningRateScheduler  
```  
from keras.callbacks import LearningRateScheduler  
  
def step_decay(epoch):  
    initial_lrate = 0.1  
    lrate = initial_lrate * (0.999^epoch)  
    return lrate  
  
Lrate = LearningRateScheduler(step_decay)  
```  
  
#### ModelCheckpoint  
  
超級好用  
  
```  
from keras.callbacks import ModelCheckpoint  
  
checkpoint = ModelCheckpoint(  
    'model.h5',  
    monitor = 'val_loss',  
    verbose = 1,  
    save_best_only = True,  
    mode = 'min',  
)  
```  
  
+ `mode` 可以設定成 `'auto'`  
  
  
#### 在 `model.fit` 時加入 Callbacks  
  
```  
history = model.fit(  
    X_train,  
    Y_train,  
    batch_size=16,  
    verbose=0,  
    epochs=30,  
    shuffle=True,  
    validation_split=0.1,  
    callbacks=[  
        early_stopping,  
        loss_history,  
        lrate,  
        checkpoint,  
    ],  
)  
```  
  
但也不要一開始就加一堆 callbacks  
尤其是 Learning Rate Scheduler  
不好的 Learning Rate Scheduler 會導致不好的結果  
  
---  
  
### Semi-supervised Learning  
  
+ 解決的問題  
    + 收集到的標籤遠少於實際擁有的資料量  
        + 該如何增加 label 呢?  
            + Crowd-sourcing  
            + Semi-supervised learning  
+ 步驟  
    + 先用 labeled dataset to train model  
        + 至少 train 到一定的程度 (良心事業)  
    + 拿 unlabeled dataset 來測試，挑出預測好的 unlabeled dataset  
    + 假設預測的都是對的 (unlabeled => labeled)  
        + 有更多 labeled dataset 了!  
    + Repeat the above steps  
+ 注意事項  
    + 加入品質不佳的 labels 反而會讓 model 變差  
    + 要注意加入的資料有沒有偏差的情況，否則最後 train 出來的 model 會變成只偏向某一類的結果  
    + 慎選要加入的 samples  
  
  
### Transfer Learning  
  
+ “transfer”: use the knowledge learned from task A to tackle another task B  
+ Use as Fixed Feature Extractor  
    + A known model, like VGG, trained on ImageNet  
    + ImageNet: 10 millions images with labels  
    + 取某一個 layer output 當作 feature vectors  
    + Train a classifier based on the features extracted by a known model  
    + 當資料很少的時候這招很好用  
+ Use as Initialization  
    + Initialize your net by the weights of a known model  
    + Use your dataset to further train your model  
    + Fine-tuning the known model  
  
  
### Short Summary  
  
+ Unlabeled data (lack of y) => Semi-supervised learning  
+ Insufficient data (lack of both x and y) => Transfer learning (focus on layer transfer)  
    + Use as fixed feature extractor  
    + Use as initialization  
    + Resources: https://keras.io/applications/  
  
  
---  
  
## Convolutional Neural Network (CNN)  
  
+ 只要 input 是二維以上，且要找特定的 Pattern 的話，就可以用 CNN，不侷限於影像。  
+ DNN 的輸入是一維的向量,那二維的矩陣呢? 例如：圖形資料  
+ 將圖形轉換成一維向量  
    + Weight 數過多,造成 training 所需時間太長  
    + 左上的圖形跟右下的圖形真的有關係嗎?  
        + 只要留下重要的地方就好了，不需要全部的 neuron 都連接起來  
+ 圖的構成  
    + 線條 (Line Segment)  
    + 圖案 (Pattern)  
    + 物件 (Object)  
    + 場景 (Scene)  
+ 辨識一個物件只需要幾個特定的圖案  
+ Property  
    + What: 圖案的類型  
    + Where: 重複的圖案可能出現在很多不同的地方  
    + Size: 大小的變化並沒有太多的影響  
        + Subsampling  
+ Convolution in Computer Vision  
    + Common applications  
        + 模糊化、銳利化、浮雕  
        + <http://setosa.io/ev/image-kernels/>  
    + Adding each pixel and its local neighbors which are weighted by a filter (kernel)  
    + Perform this convolution process to every pixels  
        + 當 pixel 的 value 高的時候，代表 pattern 有出現在該位置  
        + 當 pixel 的 value 低的時候，代表 pattern 沒有出現在該位置  
    + A filter could be seen as a pattern  
    + 常拿來做 Edge Detection  
        + edge = 亮度變化大的地方  
        + 凸顯兩像素之間的差異  
        + 如果覺得 gap 太小的話，可以再乘上一個 constant 將其凸顯出來  
    + 相鄰兩像素值差異越大,convolution 後新像素絕對值越大  
+ Convolutional Layer  
    + Convolution 執行越多次影像越小  
    + Hyper-parameters of Convolutional Layer  
        + Filter size  
        + Zero-padding  
            + Add additional zeros at the border of image  
            + Zero-padding 不會影響 convolution 的性質  
        + Stride  
            + Shrink the output of the convolutional layer  
        + Depth (total number of filters)  
+ Pooling Layer  
    + Why do we need pooling layers?  
        + Reduce the number of weights  
        + Prevent overfitting  
    + Max pooling  
        + Consider the existence of patterns in each region  
        + 在作 Classification 上用得到  
            + 因為我們在做分類的時候會找尋特定的 pattern 是否有出現在該圖片中  
        + 但是會有些資訊喪失  
    + Average Pooling  
        + 因為是取平均的關係，所以出來的結果很高的話，代表該區域的值都很高，所以 pattern 出現在該位置的可能性也很高  
        + 用來找尋一再重複出現的 pattern  
+ A CNN Example (Object Recognition)  
    + [CS321n, Standford](http://cs231n.github.io/convolutional-networks/)  
+ Filters Visualization  
    + [RSIP VISION](http://www.rsipvision.com/exploring-deep-learning/)  
  
  
#### CNN in Keras  
  
+ Concatenate Datasets by Numpy Functions  
    + hstack, dim(6,)  
        + [1, 2, 3, 4, 5, 6], Labels  
    + vstack, dim(2,3)  
        + [[1, 2, 3], [4, 5, 6]], Pixel values  
    + dstack, dim(1, 3, 2)  
        + [[1, 2], [3, 4], [5, 6]], Dimensions  
+ Concatenating Input Datasets  
    + 利用 vstack 連接 pixel values;用 hstack 連接 labels  
+ Reshape the Training/Testing Inputs  
    + 利用影像的長寬資訊先將 RGB 影像分開,再利用 reshape 函式將一維向量轉換為二維矩陣,最後用 dstack 將 RGB image 連接成三維陣列  
+ Saving Each Data as Image  
    + `scipy.misc.imsave`  
    + `PIL.Image`  
+ Building Your Own CNN Model  
```  
'''CNN model'''  
  
# CNN  
model = Sequential()  
model.add(  
Convolution2D(  
    32,  
    3,  
    3,  
    border_mode='same',  # 有做 zero-padding 的意思  
    input_shape=X_train[0].shape)  
)  
model.add(Activation('relu'))  
model.add(Convolution2D(32, 3, 3))  
model.add(Activation('relu'))  
model.add(MaxPooling2D(pool_size=(2, 2)))  
model.add(Dropout(0.2))  
  
model.add(Flatten())  
  
# DNN  
model.add(Dense(512))  
model.add(Activation('relu'))  
model.add(Dropout(0.5))  
model.add(Dense(10))  
model.add(Activation('softmax'))  
```  
+ Tips for Setting Hyper-parameters  
    + 影像的大小須要能夠被 2 整除數次  
    + Convolutional Layer  
        + 比起使用一個 size 較大的 filter (7x7),可以先嘗試連續使用數個 size 小的 filter (3x3)  
        + Stride 的值與 filter size 相關,通常 stride ≤ (W_f - 1)/2  
    + Very deep CNN model (16+ Layers) 多使用 3x3 filter 與 stride 1  
    + Zero-padding 與 pooling layer 是選擇性的結構  
    + Zero-padding 的使用取決於是否要保留邊界的資訊  
    + Pooling layer 旨在避免 overfitting 與降低 weights 的數量, 但也減少影像所包含資訊,一般不會大於 3x3  
        + 像圍棋就不太適合用 Pooling，因為可能會失真。所以 AlphaGo 其實只有用 Convolutional Layer，沒有用 Pooling Layer。  
    + 嘗試修改有不錯效能的 model,會比建立一個全新的模型容易收斂,且 model weights 越多越難 tune 出好的參數  
  
---  
  
### Deep Learning Applications  
  
+ [Visual Question Answering](http://visualqa.org/)  
+ Video Captioning  
+ [Text-To-Image](https://arxiv.org/pdf/1701.00160.pdf)  
+ [Vector Arithmetic for Visual Concepts](https://arxiv.org/pdf/1511.06434.pdf)  
+ Go Deeper in Deep Learning  
    + [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)  
    + [Deep Learning](http://www.iro.umontreal.ca/~bengioy/dlbook/)  
    + [Course: Machine learning and having it deep and structured](http://speech.ee.ntu.edu.tw/~tlkagk/courses_MLSD15_2.html)  
  
---  
  
### References  
  
+ [Keras documentation](https://keras.io/)  
+ [Keras GitHub](https://github.com/fchollet/keras)  
+ [台大電機李宏毅教授 Youtube 頻道](https://www.youtube.com/channel/UC2ggjtuuWvxrHHHiaDH1dlQ)  
+ [Convolutional Neural Networks for Visual Recognition cs231n](http://cs231n.stanford.edu/)  
  
---  
  
### Q&A  
  
+ 如果 feature 數量不夠的話，可以做些簡單的運算增加 feature 的量，尤其是已經知道這樣的 feature 會對 training 有幫助的話。  
+ Keras model 相關的操作  
    + 用 `model.save()` 來將訓練好的 model 存起來  
    + 之後可用 `keras.models.load_model()` 來讀入已經訓練好的 model  
    + 讀入之後可再用 `model.summary()` 來確認一下 model 的資訊  
    + `model.layers[0].get_weights()` 可以得到此 model 第 1 層的 weights  
    + 用 `model.predict()` 來預測結果  
+ 當資料太大無法一次讀進來時，可以用 [Fit Generator](https://keras.io/models/sequential/#fit_generator)。  
    + 需要自己撰寫一個 generator  
