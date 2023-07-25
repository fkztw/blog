Title: 視訊訊號處理與深度學習應用  
Slug: video-signal-processing-and-the-application-of-deep-learning  
Date: 2016-04-23 09:20:46  
Authors: fkz  
Category: Conf/Meetup  
Tags: Data Science, Deep Learning, Conf  
Summary: 台灣資料科學愛好者年會系列活動筆記  
Modified: 2016-04-24 14:43  
  
  
+ <http://dsc.kktix.cc/events/video-signal>  
+ <http://datasci.tw/event/vision_and_learning/>  
+ Slides: <http://www.slideshare.net/tw_dsconf/ss-61255961>  
    + [備份](https://drive.google.com/file/d/0B9cCeTKOkfWITllMazh2a0ctZVk/view?usp=sharing)  
  
---  
  
# 【判讀】電腦視覺簡介  
  
## Real Cases in Computer Vision  
  
+ Character Recognition (LeNet)  
+ [Microsoft PhotoSynth](https://www.youtube.com/watch?v=4LxlhoemR3A)  
+ [Video Reenactment](https://www.youtube.com/watch?v=ohmajJTcpNk)  
+ Auto Driving  
    + Autonomous Cars - NVIDIA Drive PX2  
        + Object class recognition  
        + Semantic Segmentation  
            + 分辨出哪裡是車子可以開的地方  
        + Radar  
            + 用雷射去掃周邊的環境，可以很快速的去辨認，但跟電腦視覺比較無關。  
        + 電子後照鏡  
            + 解決視線死角問題  
    + [Grandma rides a Tesla](https://www.youtube.com/watch?v=gUIKtqyUIo8)  
+ Trip Wire  
+ Loitering  
+ People Count  
+ Speed Test  
    + 不用都卜勒雷達算，直接用影像計算。  
    + 不小心歪掉就不準了，所以大家知道怎麼躲這種測速了吧 （XDD  
+ Smart Daily  
    + 用監視器的影像辨認人臉打卡。  
+ Smart Fast Forward (Skywatch 的產品)  
    + 用影像辨識來判斷農舍監視器畫面中哪些時間是有人的，主要是用來定期追蹤是否有記得噴灑農藥。  
+ Structure from motion  
+ 3D Reconstruction  
+ Person tracking  
+ Face detection  
  
  
## Relationship to Data Science?  
  
+ Rich info, lots of data (in terms of bits)  
+ Unstructured, usually without much context / semantics  
+ Difficult to process and query  
+ We are generating them every day  
    + 要變成人類歷史的一部份，轉化成可搜尋的話，是個問題。  
  
  
## A Brief History of Computer Vision  
  
+ 1966, Marvin Minsky  
    + 50 年過後，我們還沒完全解決這個問題。  
+ 1960's: Interpretation of Synthetic Worlds  
    + Larry Roberts (Father of Computer Vision)  
+ 1970's: Some progress on interpreting selected images  
+ 1980's: AI Winter ... back to basics  
    + 1984: Perceptual Organization and Visual Recognition, David Lowe  
    + Blending  
    + Shape from shading  
        + 用三角函數找出反光的角度建模  
    + Edge Detection  
    + From Science to Engineering  
+ 1990's: structure, segmentation and face recognition  
+ 2000's: more object classes, computational photography, video processing  
    + 重新對焦的照相機  
    + Texture Sythesis  
+ 2010's: Deep Learning is Back!!  
    + AlexNet NIPS 2012  
    + DeepFace CVPR 2014  
    + DeepPose CVPR 2014  
    + Show, Attend and Tell ICML 2015  
  
  
## Basic parts of Computer Vision  
  
### Reference Books  
  
+ "Multiple View Geometry in Computer Vision", Richard Hartley and Andrew Zisserman  
    + A good book to get started on camera geometry  
    + More math heavry but very old school  
+ ["Computer Vision: Algorithms and Applications", Richard Szeliski](http://szeliski.org/Book/)  
    + More balanced mix between math and application  
    + Freely available online.  
  
### Image Formation and 2D Image Processing  
  
+ Image formation  
    + 照相原理：散射會造成無法成像，所以透過針孔（作為 barrier），使其成像。  
        + 缺點  
            + 光線不足，所以很暗  
            + 針孔太大的話，成像會變模糊，所以加上透鏡輔助。  
                + Circle of Confusion  
                    + 有散景表示你的鏡頭光圈夠大，代表你是有錢人。 XDD  
    + Modeling Projection  
        + The coordinate system  
            + Homogeneous Coordinations  
                + 3D 轉 2D  
                + 4D 轉 3D  
    + Projection equations  
    + Camera parameters  
        + 外部參數(extrinsics)  
        + 內部參數(intrinsics)  
        + <http://ai.stanford.edu/~saumitro/projektiv/> 可以透過這個網址來瞭解外部參數和內部參數實際上的影響  
    + Distortion （扭曲）  
        + Types  
            + Pin Cushion Distortion（針包）  
            + Barrel Distortion （木桶）  
        + Camera Calibration （攝影機校正）  
            + 使用時機：把扭曲移除、改變照片的角度、要辨認轉了角度的物件畫面 (Low Level Projection)  
    + Tilt-shift  
        + Digital Color Images  
            + Bayer Filter  
                + 人對綠色比較敏感，對藍色比較不敏感。  
                + 彩色的照片是 3 個黑白的 RGB 疊加起來  
                + Many early algorithms use greyscale instead of color images, Why?  
                    + 早期只有灰階照片  
                    + 彩色會有偏差  
            + Image Filtering  
                + Sliding Window  
                + Sharpening filter (Unsharp Mask)  
                + Vertical Edge  
                + Horizontal Edge  
  
### Epipolar geomerty and stereo matching  
  
+ Recovering structure from a single view  
    + Intrinsic ambiguity of the mapping from 3D to image (2D)  
    + 2D 是無法直接確定物體距離與深度的，必須用兩個眼睛來看，三角定位。  
+ [Epipolar geomerty](https://en.wikipedia.org/wiki/Epipolar_geometry)  
    + Parallel Images Plane  
    + Forward translation  
    + Epipolar line  
    + [The "Vertigo" Effect](https://www.youtube.com/watch?v=sKJeTaIEldM)  
    + Epipolar Constraint (F)  
        + Estimating F  
            + The Eight-Point Algorithm  
    + Fundamental Matrix 很重要！  
    + Rectification  
        + Your basic stereo algorithm  
        + Triangulation  
    + Depth Map Results  
    + Active stereo with structured light  
        + Data Acquisition  
  
### Structure from motion and tracking  
  
+ Finding Path Through the World's Photos  
+ Pose Estimation  
+ Structure from motion  
    + Tracking  
        + 找特徵點去追蹤，然後解出結構。  
  
### Stitching and computational photography  
  
如何把一堆照片合起來變成一張大照片  
  
+ Image Mosaics  
+ Recognizing Panormas  
+ De-Ghosting  
    + Cutout-based de-ghosting  
        + Cutout-based compositing  
        + Photomontage  
        + 可以把好幾張裏面有不同人閉眼的照片合成一張沒有人閉眼的照片。  
    + Poisson Image Editing  
        + Possion Equation: 微分、微分、再積分  
        + 照片合成特效  
        + Seamless Poisson cloning  
        + Face Cloning  
        + Texture Swapping  
+ Interactive Mobile Panorama  
+ High Dynamic Range Imaging (HDR)  
    + The real word is high dynamic range  
        + Typical cameras have limited dynamic range  
            + Solution: Merge multiple exposures  
    + Varying Exposure  
    + Tone Mapping  
    + Simple Global Operator  
+ Interactive Local Adjustment of Tonal Values  
    + Tonal （色調） Manipulation  
    + Constraint Propagation  
    + Touch-Tone: Point-and-Swipe Image Editing  
  
### Visual Recognition and Query  
  
+ 1989  
    + MNIST, Backpropagation applied to handwritten zip code recognition  
    + Character Recognition (LeNet)  
+ 1998, Neural Network-Based Face Detection  
+ 1999, SIFT (Scale Invariant Feature Transform)  
    + Object Recognition from Local Scale-Invariant Features, Lowe, ICCV 1999.  
    + No more sliding windows (interest points)  
    + Better features (use more computation)  
    + 找出來的特徵點會是一個球，而不是邊邊角角。  
    + Better Descriptor  
        + Image gradients => Keypoint descriptor  
        + Truncated normalization (globally)  
        + 高維度的球  
    + What worked  
        + Object instance recognition  
        + Panaroma  
    + What failed?  
        + 無法認東西  
+ 2001, Rapid Object Detection using a Boosted Cascade of Simple Features, Viola and Jones  
    + Why did it work?  
        + Simple Features (Haar wavelets)  
        + 假設光線都是從上打下來，直接去認眼睛和鼻子的陰影，覺得有可能的保留，沒可能的就丟掉，所以速度很快。  
    + Why did it fail?  
        + 側面就無法 work  
+ 2003, Constellatioin model (redux) (related to SIFT)  
    + Object Class Recognition by Unsupervised Scale-Invariant Learning  
+ 2005, HOG (Histograms of oriented gradients) (related to SIFT)  
    + Normalize locally not globally  
    + Why worked?  
        + Hard negative mining  
        + Computers are fast enought  
    + What failed?  
        + 無法認出運動中的人，必須要站著。  
+ 2007, Pascal VOC  
    + The PASCAL Visual Object Classes (VOC) Challenge  
    + 只有 20 個分類  
+ 2008, DPM (Deformable parts model)  
    + Object Detection with Discriminatively Trained Part Based Model  
    + Star-structure  
+ 2009, Caltech Pedestrian  
+ 2009, ImageNet  
    + ImageNet, A Large-Scale Hierarchical Image Database  
+ 2010, SUN  
    + SUN Database: Large-scale Scene Recognition from Abbey to Zoo  
+ [MS COCO](http://mscoco.org)  
    + over 77,000 worker hours (8+ years)  
+ 2012 DNNs  
    + GPUs + Data  
    + Classification vs Deteciton  
        + Detection need to know the position of the target object  
    + CNN, RNN  
    + Why it fails  
        + 找不到位置的話就很難去判斷  
        + Neural Networks are easily fooled  
            + 會把看起來完全不相關的雜訊誤判成某些物件  
                + Neural Networks are easily fooled: High Confidence Predictions for Unrecognizable Images  
            + PANDA: Pose Aligned Networks for Deep Attribute Modeling  
            + DeepFace: closing the gap to  human-Level performance in fac verification  
    + Additional Challenges  
        + Detecgtion in context (with common sense)  
            + 加入一些常識的判斷，例如：人在普通情況下不可能在天上飛之類的等等  
        + Model awareness  
        + Training time (when dataset is incrementally updated)  
            + 每個公司都用大量的電腦去運算，不僅耗時，也蠻浪費電的。  
        + More science?  
            + 目前比較像是大量嘗試去找出方法，不太有系統且有科學性。  
  
---  
  
# 【索引】多媒體檢索  
  
## Search By Image Examples  
  
+ Still very much an open problem  
+ Most commercial applications use a mixture of algorithms  
    + 沒有一種演算法可以完全解決這個問題  
+ Google Goggles in action  
    + Text => OCR  
    + Landmarks, Books, Artwork, Wine, Logos => SIFT  
    + Contact Info  
+ TinEye  
    + 以圖找圖  
+ Instance Recognition  
+ Search Structure  
+ Possible Solutions  
    + Find approximate words  
        + Approximate nearest neighbour (ANN)  
        + 維度比較高，所以速度比較慢  
    + Find lower dimensional spae to split the data  
        + 找 2D 的的資料，雖然沒那麼準確，但速度會比較快。  
    + Scalable Recognition with a Vocabulary Tree  
        + 先拿一張圖找 Feature  
        + 找出來後丟到高維度的空間（約兩百多維)  
        + 會有很多不同的點  
        + 用定義好的向量距離，用 [K-means](https://en.wikipedia.org/wiki/K-means_clustering) 做分群  
        + 遞迴做下去就可以得到愈多種類的分群結果  
        + 最後再把不需要的東西去掉，得到 Vocabulary Tree  
        + 得到 Vocabulary Tree 後，把每個 Feature 丟進去，會知道在 Vocabulary Tree 的哪個節點  
        + 如果該 Feature 的結果只指向一張圖的話，就很有可能是這張圖。  
        + 但當某個節點有關的圖愈多的話，entropy 愈高，結果就愈難判斷。  
        + 這時候可以使用 [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)  
  
---  
  
# 【加速】圖形處理器與深度學習 (GPU and Computation)  
  
## Parallel Processing and GPU  
  
### Parallel Computing Goals  
  
+ To slove your problem in less time  
    + 平行化去處理  
+ In order to parallelize a problem  
    + 要去看哪邊有關聯性，並確定處理這些關聯性對演算法的影響。  
  
### Types of Parallelism  
  
+ Multiple Programs  
    + Multi-tasking  
    + Multi-threading  
+ Single Program  
    + Instruction-levl parallelism  
        + Multiple instructions in a serial program get excuted simultaneously  
    + Data-level parallelism  
        + **S**ingle **I**nstruction, **M**ultiple **D**ata processing model (SIMD)  
+ Amdahl's Law  
    + Named after computer architect Gene Amdahl  
    + Speedup of a parallel computer is limited by the amount of serial work  
+ Resource Management  
    + 哲學家晚餐問題  
  
### GPU Applications  
  
+ Real-time rendering. e.g. Game  
+ Movie Effect  
  
### GPUs Today  
  
+ GPUs are becoming more programmable  
+ GPUs now support 32/64 bit floating points numbers  
+ GPUs have higher memory bandwidth than CPUs  
  
### NVIDIA CUDA  
  
+ Compute Unified Device Architecture  
+ CUDA Workflow  
    + Get a CUDA-enabled GPU  
    + Write C/C++ like code (\*.cu)  
    + Compile with CUDA compiler (nvcc)  
        + Generated PTX code ("Parallel Thread Execution")  
    + Applications auto-magically run on GPUs  
        + Many many parallel threads  
        + CUDA driver translate PTX code into hardware.  
+ CUDA Overview  
  
> 之前學 CUDA 時收集的一份不錯的 CUDA 教學系列文：[Nice Series of CUDA Tutorials on ptt.cc](/posts/2015/08/15/nice-series-of-cuda-tutorials-on-ptt-cc/)  
  
### Frameworks and Libraries  
  
+ MATLAB  
+ BLAS Library (Basic Linear Algebra Subprograms)  
    + 和 Fortran 同年代的產物  
    + Processor vendors implement their BLAS library  
        + e.g., Intel MKL (Math Kernel Library)  
    + cuBLAS - CUDA version, very fast  
+ NVIDIA Thrust Library  
    + A little like C++ STL library for CUDA  
    + Very few lines of code for vector manipulation  
    + Fast implementation of parallel primitives  
        + reduce  
            + mapreduce  
        + scan  
        + sort  
+ NVIDIA cuDNN  
    + Deep Neural Network Library for CUDA  
    + TensorFlow, Caffe, Microsoft CNTK  
    + Deep Learning Getting Started Advises  
        + Borrow (steal if you must) a modern GPU  
        + Use [Caffe](http://caffe.berkeleyvision.org) for your deep learning projects  
        + Browse through the Caffe Model Zoo and try out the existing (pre-trained) models (AlexNet, R-CNN and GooLeNet  
  
---  
  
# 電腦視覺之實作演示  
  
+ Introduct OpenCV by the official tutorials  
    + Core functionality  
    + Image processing  
    + Demos  
  
+ Python, OpenCV, Numpy  
    + Canny Edge Detection  
        1. Detect unique edges  
            + 不管是 strong edge 或 weak edge 在經過微分後都會產生一個 peak  
        2. Edge Voting (Use 2 threshold)  
            + Strong edge: Always accept.  
            + Weak edge: Accept when connected.  
        + 是很多後續演算法的基礎  
    + Histogram  
+ Demo  
    + OpenCV QR Drive  
        + QR code Marker Detection  
            + 1:1:3:1:1 black-white markers at the coners  
        + How to detect 11311?  
            + Only need to use raster scan  
            + Use [Otsu algorithm](https://en.wikipedia.org/wiki/Otsu%27s_method)  
                + Thresholding: leave only white and black  
                + A binarization algorithm that minimize the weighted intra-class variance algorighm for bimodal distributioin.  
            +  Detect the most bright points  
                1. Dilate  
                2. Equality check  
                3. Threshold  
            + Dilation and thresholding  
    + Make a little PiBorg which will chase the $1,000 NTD bill.  
        + The PiBorg (RPi + Motor) aka [DoodleBorg](https://www.youtube.com/watch?v=s3Qdsn401H0)  
        + Camshift (WACV 98)  
        + Meanshift  
        + [OpenCV: Meanshift and Camshift](http://docs.opencv.org/3.1.0/db/df8/tutorial_py_meanshift.html)  
        + Camshift 比 Meanshift 多了一個 scale 的選項  
+ Conclusion  
    + Basic OpenCV functionalities  
    + OpenCV and image processing  
    + OpenCV and detection  
