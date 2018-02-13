# Main 
* [mattn/emmet-vim](https://github.com/mattn/emmet-vim)
* [Offical Tutorial](https://raw.githubusercontent.com/mattn/emmet-vim/master/TUTORIAL)
* [更多实例](https://www.cnblogs.com/dieangel/p/5123855.html)
* 热键`<c+y> ,`

## Expand an Abbreviation

#####生成带id的链接段落框架
```html
div>p#foo$*3>a
<div>
        <p id="foo1"><a href=""></a></p>
        <p id="foo2"><a href=""></a></p>
        <p id="foo3"><a href=""></a></p>
</div>
```
##### 生成带id的表格框架
```html
table[border="1"]>tr#row$$*2>th#col$*3
 <table border="1">
  <tr id="row01">
    <th id="col1"></th>
    <th id="col2"></th>
    <th id="col3"></th>
  </tr>
  <tr id="row02">
    <th id="col1"></th>
    <th id="col2"></th>
    <th id="col3"></th>
  </tr>
</table>
```
##### 生成基本网站框架

```html
 #main_page>(div.header>div.logo+div.menu)+div.context+div.footer
 <div id="main_page">
         <div class="header">
                 <div class="logo"></div>
                 <div class="menu"></div>
         </div>
         <div class="context"></div>
         <div class="footer"></div>
 </div>
```

## Wrap whit an Abbreviation

##### 更具内容生成表格

```html
line1
line2
line3
----------
table>tr>th*
<table>
        <tr>
                <th>line1</th>
                <th>line2</th>
                <th>line3</th>
        </tr>
</table>
```
## 其他按键
##### 生成url `<c+y> a`
在html中
```html
http://lihao2333.com/
------------
<a href="http://lihao2333.com/"></a>

```
在markdown中
```markdown
http://lihao2333.com/
------------
[](http://lihao2333.com/)
```
