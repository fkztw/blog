Title: Cat System Workshop #12: SkyPat: C++ Performance Analysis and Testing Framework  
Slug: cat-system-workshop-12-skypat-c-performance-analysis-and-testing-framework  
Date: 2016-10-11 19:46:58  
Authors: fkz  
Category: Conf/Meetup  
Tags: Skymizer, Cat System Workshop, Meetup, C++, Performance, Unit-test, framework  
Summary: Note for Cat System Workshop #11 (2016/10/11)  
  
  
## Info  
  
+ Speaker: Peter Chang  
+ Event Link: <http://www.accupass.com/go/cat1011>  
+ GitHub Repo: <https://github.com/skymizer/SkyPat>  
  
---  
  
## Note  
  
+ Regions of code  
+ SkyPat  
    + Define unittest, checking both correctness and performance for you.  
    + `#include <pat/pat.h>`  
    + A glace at SkyPat  
  
```Cpp  
#include <pat/pat.h>  
  
// In MathCase, fibonacci_test  
PAT_F(MathCase, fibonacci_test)  
{  
    ASSERT_TRUE(fibonacci(3) == 3);  
    EXPECT_EQ(fibonacci(3), 3);  
    PERFORM {  
        fibonacci(3);  
    }  
}  
  
// 一個 case 裏面有很多個 tests  
```  
  
+ Loop-Intensive  
    + Benefic Compiler Optimization  
    + 比較容易展開  
    + 測試效能也比較沒那麼困難，主要就看這段 code 要被執行幾次。  
    + Example:  
        + GIMP  
        + Skymizer  
+ Call Intensive  
    + Damage Compilter Optimization  
    + Difficult to Evaluate  
    + 比較難處理  
    + 如果產生得出夠完整的 call graph，可能可以做些優化  
    + Loop 展開不太有效果  
    + 只能試試看能不能減少呼叫  
    + 有很多不知道的小瓶頸  
    + Example:  
        + Browsers (Chrome, Firefox)  
        + Editors (Evernote, ...)  
  
---  
  
+ SkyPat 就是專門用來處理 Call Intensive 這種惱人的效能分析的  
+ `perf` cannot evaluate regions of code.  
+ SkyPat integrates `perf_event` to evaluate regions of code.  
+ "Software Task Clock" is still not cycle-accurate  
+ Only cycle-accurate timer w/o OS interference.  
+ Can evaluate call-intensive program  
  
---  
  
+ Install:  
    + `$ git clone https://github.com/skymizer/SkyPat.git`  
  
---  
  
Usage  
  
```Cpp  
#include <pat/pat.h>  
  
int main(int argc, char* argv[]) {  
    pat::Test::Initialize(&argc, argv);  
    pat::Test::RunAll();  
}  
```  
  
---  
  
+ SkyPat v3.0 will be released at Oct 30th.  
+ Add more Perf events  
+ Welcome feedbac and patches  
  
---  
  
其他的 tool 只能測量 function level，  
但 SkyPat 可以測量 block level。  
  
---  
  
## Conclusion  
  
目前還是非常初步的產品，  
也歡迎使用者、貢獻者開 Issues 跟 Pull Request，  
一起討論也很歡迎。  
  
---  
  
## Related links  
  
+ [GitHub - google/googletest: Google Test](https://github.com/google/googletest)  
