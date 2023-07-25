Title: Taipei.py 20160421 Meetup Note  
Slug: taipei-py-20160421-meetup-note  
Date: 2016-04-21 19:08:26  
Authors: fkz  
Category: Conf/Meetup  
Tags: Python, Taipei.py, Neural Network, KKBOX, Meetup  
Summary: "Neural Art and Neural Doodle in Python" & "Experience from KKBOX"  
Modified: 2016-04-22 00:15  
  
  
<http://www.meetup.com/Taipei-py/events/230083921/>  
  
Topic 1: Neural Art and Neural Doodle in Python  
Topic 2: Experience from KKBOX  
  
---  
  
# Neural Art and Neural Doodle in Python  
  
+ Slides  
    + [Neural Art](http://www.slideshare.net/ckmarkohchang/neural-art-english-version)  
    + [Neural Doodle](http://www.slideshare.net/ckmarkohchang/neural-doodle)  
+ [Neural Art](http://www.slideshare.net/ckmarkohchang/neural-art-english-version)  
    + Neural Networks - 模擬人腦的神經元  
        + Sigmoid  
        + Rectified Linear  
    + Convolutional Neural Networks - 處理影像上很常用  
        + Convolutional Layer  
        + Pooling Layer - 把重要的訊息保留下來，不重要的丟掉。  
            + Maximum Pooling  
            + Average Pooling  
        + Architecture  
            + Input Layer  
            + Convolutional Layer  
            + Pooling Layer  
            + Convolutional Layer  
    + [VGG19](http://arxiv.org/pdf/1409.1556.pdf) - 可以模擬人腦看東西的過程  
        + What is VGG19?  
            + VGG Net-E (19 layers)  
            + Pre-trained model  
    + 如何產生畫作  
        + Content Generation  
            + 比較景物跟現在的畫布有何不同  
            + Backward Propagation  
        + Style Generation  
            + Style 是比較抽象的概念  
            + 在這裡被當成是一種特徵，而且是跟位置無關的特徵。  
            + Style Extraction  
                + 同一幅畫的的不同位置，轉換出來的風格會是一樣的。  
                + [Gram Matrix](https://en.wikipedia.org/wiki/Gramian_matrix)  
                + 把位置的訊息拿掉後，讓 Canvas （畫布）的風格愈來愈接近目標畫作  
        + Artwork Generation  
            + 把景物跟風格都一起丟進 VGG19 後，再把兩個一起做最佳化。  
                + Layer_total == (alpha)*Layer_content + (beta)*Layer_style  
                    + alpha 的比重愈高，畫作愈寫實。  
                    + beta 的比重愈高，愈接近畫作。  
+ [Neural Doodle](http://www.slideshare.net/ckmarkohchang/neural-doodle)  
    + 改良 Neural Art 的缺點  
        + <http://arxiv.org/abs/1601.04589>  
    + Neural Art 採用 gram-based matrix 取得風格，因為忽略位置訊息，所以所有的部份風格都是相同的。  
    + Neural Doodle 則採用了不會忽略位置訊息的 Patch-based Matrix，會尋找畫作中與畫布相近的部份取得該部份的風格，因此改善了 Neural Art 的缺點。  
    + Patch-Based Style Transfer  
        + 透過兩向量內積除以兩向量絕對值來判斷相近的程度，然後自動去尋找最相近的 patch，得到 Most simillar patch  
    + Sematic Style Transfer  
        + 可以為每個部份加上標籤  
        + 可以比 Patch-based 產生更精準的畫作  
        + 可以用小畫家上色，也可以使用 Pixel Labeling  
        + Canvas 不經過 VGG19 而是透過 Average Pooling 再把 Canvas 和 Style 相加  
    + Image Analogy  
        + 直接用畫作產生 Semantic Map，然後再修改該 Sematic Map，再使用修改過後的 Semantic Map 生成新的畫作。  
  
  
---  
  
# Experience from KKBOX  
  
+ PyKKBOX  
    + 2011 initiate, private repo.  
    + iOS team  
    + KKBOX 一起聽  
        + Challenges  
            + iOS (client) co-works with Windows (broadcaster) only.  
            + In 3 months, the API's verion changed 5 times.  
            + There is even no broadcasters to listen to.  
            + In academia, we may call this "ill-posed (optimization) problem".  
    + A bot for poc  
        + 主管要求在沒有 broadcaster 的情況下 demo iOS client 的功能，只好用 Python 接 API 快速刻一個偽 broadcaster 出來。  
    + 因為 iOS team 的不熟 Python，不打算教 venv 那類的東西，所以只用到 built-in modules 跟 PyObject，code 直接 clone 下來就能跑了，完全不用 third-party packages。  
    + 用 Python 可以快速的建出 PoC，協助開發。  
    + 2013 就停止開發了。停止原因是沒有進一步的計劃和需求，而且畢竟是個 iOS team。  
+ [PyUIA](https://github.com/imsardine/pyuia)  
    + Started in 2013.  
    + Testing for Playlist Auto-Sync  
    + 想做到讓 unittestings 可以儘量不需要額外寫程式碼，讓不會寫程式的 QA 可以用特定格式的 natural language 就可以新增測試。  
        + （我記得 robotframework 好像也可以辦到這件事？）  
+ Video Encoding System  
    + Challenges  
        + Given a thousands of videos  
        + Given ~150 videos per day  
        + Given a scalable number of encoders on EC2 instances  
        + Assuming the workflow for each video can be different  
            + 根據每個客戶有不同的限制和需求  
        + How to make a robust system to handle this challenge in consideration of  
            + Just 1.5 developer(s)  
            + everything can be broken  
            + computing resource is expensive (AWS)  
            + AWS is weak  
    + 用 tcl 寫 Job Script，使用 Producter-Consumer model  
    + [Mass](https://github.com/KKBOX/mass)  
    + 最大的挑戰是一天要轉三千部影片  
        + 最後成功了，但一天內用 AWS 燒掉了十幾萬還是幾十萬台幣，忘了。  
+ RDC Toolbox  
+ Python 是個方便且讓人寫起來感到快樂的語言，歡迎大家一起開心地寫 Python。  
