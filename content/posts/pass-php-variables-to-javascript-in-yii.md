Title: Pass PHP Variables to JavaScript in Yii  
Date: 2014-02-27 13:55  
Author: fkz  
Category: Note  
Tags: Web, JavaScript, PHP, jQuery, Yii  
Slug: pass-php-variables-to-javascript-in-yii  
Modified: 2015-10-27 22:40  
  
  
## Preface  
  
因為網站需求 想找看看有沒有可以把 PHP 中的變數傳給 JavaScript 使用的方法  
  
主要是因為 URL 不想像之前一樣是寫死在 JavaScript 裡面  
  
不然之後 URL routing 又改的話 又得重新修改 實在很麻煩  
  
想用 `Yii::app()->createAbsoluteUrl('');` 生成該頁面的網址之後  
  
再丟給 JavaScript  
  
這樣就不用把網址寫死在裡面  
  
其實找了有點久 好像沒找比較好的解法  
  
  
## Solution  
  
所以最後用了 [stackoverflow 上的這篇](http://stackoverflow.com/questions/8912548/in-yii-pass-php-variables-to-javascript) 中最底下的回覆  
  
但裡面的寫法有一點點小錯誤  
  
```php  
Yii::app()->clientScript->registerScript("myVarList",  
    'myVarList = jQuery.parseJSON('.CJSON::encode($myVarList).');'  
```  
  
小括號的內層必須再多一對單引號  
  
不然 [jQuery.parseJSON](https://api.jquery.com/jQuery.parseJSON/) 會出錯  
  
所以最後寫的 Code 長這樣  
  
```php  
<?php  
$myVar = ['url' => Yii::app()->createAbsoluteUrl($this->module->id.'/default/list/json/1')];  
?>  
  
<?php  
Yii::app()->clientScript->registerScript('', "myVar = jQuery.parseJSON('".CJSON::encode($myVar)."');\n" . <<<EOD  
function updateList(name)  
{  
    $('#company-list').html($('#loading-tmpl').text());  
    $.getJSON(myVar.url + (name !== null ? ('/name/' + name) : ''), function (data) {  
        $('#company-list').empty();  
        $('#company-tmpl').tmpl(data).appendTo('#company-list');  
    });  
}  
  
...  
?>  
```  
  
在 JavaScript 中，可以透過 `myVar.url` 順利拿到 URL  
  
## Appendix  
  
```php  
<<<EOD  
...  
EOD;  
```  
  
此種寫法在 PHP 中稱為 `HEREDOC`  
  
> A third way to delimit strings is the heredoc syntax: <<<.  
> After this operator, an identifier is provided, then a newline.  
> The string itself follows, and then the same identifier again to close the quotation.  
  
詳見官方說明 [PHP - HEREDOC syntax](http://www.php.net/manual/en/language.types.string.php#language.types.string.syntax.heredoc)  
  
---  
  
## References  
  
+ [In Yii, pass PHP variables to JavaScript](http://stackoverflow.com/questions/8912548/in-yii-pass-php-variables-to-javascript "In Yii, pass PHP variables to JavaScript")  
+ [jQuery.parseJSON](https://api.jquery.com/jQuery.parseJSON/)  
+ [jQuery.getJSON](http://api.jquery.com/jquery.getjson/)  
+ [Yii - CClientScript ](http://www.yiiframework.com/doc/api/1.1/CClientScript#registerScript-detail)  
+ [Yii - CJSON](http://www.yiiframework.com/doc/api/1.1/CJSON#encode-detail)  
+ [What is the use of <<<EOD in PHP?](http://stackoverflow.com/questions/6924193/what-is-the-use-of-eod-in-php)  
