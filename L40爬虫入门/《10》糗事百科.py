# 糗事百科热点文章爬取
# 分析：请求url https://www.qiushibaike.com/hot/page/1/   要抓取div class='article'下内容  urllib或requests，

import urllib.request
from fake_useragent import UserAgent
import random
import re
#
# for i in range(20):
# base_url = 'https://www.qiushibaike.com/hot/'
# url = base_url + '1' + '/'
# print(url)
#
# ua = UserAgent()
#
# headers = {
#     'User-Agent': ua.random
# }
#
# req = urllib.request.Request(url, headers=headers)
# resp = urllib.request.urlopen(req)
# html_content = resp.read().decode('utf-8')
# print(html_content)

html_content = r"""

<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta http-equiv="X-UA-Compatible" content="chrome=1,IE=edge">
<meta name="renderer" content="webkit"/>
<meta name="applicable-device" content="pc">
<meta name="domain_verify" content="pmrgi33nmfuw4ir2ejyws5ltnbuweyljnnss4y3pnurcyithovuwiir2ejqwmyrtguzdgobsmezdgnbyheywcmzthbrdmmtemu4tamrqg5rtmirmej2gs3lfknqxmzjchiytkmrzgq4demjugaydcnd5">


















<title>24小时爆笑笑话大全 - 糗事百科</title>






















<meta name="keywords" content="笑话,笑话大全" />
<meta name="description" content="糗事百科官网提供24小时糗搞笑笑话大全,糗百24小时内新糗事就只在糗事百科官网24小时专题,囊括恶搞、尴尬糗事精华,快乐减压！"/>
<meta http-equiv="mobile-agent" content="format=xhtml;url=//www.qiushibaike.com/hot/">
<meta http-equiv="mobile-agent" content="format=html5;url=//www.qiushibaike.com/hot/">




<meta name="robots" content="noarchive">
<link href="//static.qiushibaike.com/css/dist/web/app.min.css?v=1a44fd15c6e802cc1ab5953bd398eea8" media="screen, projection" rel="stylesheet" type="text/css"/>
<script type="text/javascript">
// Baidu Automatic push content
var _hmt = _hmt || [];
(function() {
var hm = document.createElement("script");
hm.src = "https://hm.baidu.com/hm.js?2670efbdd59c7e3ed3749b458cafaa37";
var s = document.getElementsByTagName("script")[0];
s.parentNode.insertBefore(hm, s);
})();
// 收集运营上缓存证据
window.config = {
'user_time': '2018-12-12 11:21:57',
'version': '2017-09-04 14:36'
}
</script>
</head>
<body>



<div id="header" class="head">
<div class="content-block">
<div class="logo" id="hd_logo">
<a href="/"><h1>糗事百科</h1></a>
</div>
<div id="menu" class="menu-bar menu clearfix" style="margin:0 10px">
<a  href="/" target="_blank" rel="nofollow">热门</a>
<a  id="highlight"  href="/hot/" target="_blank">24小时</a>
<a  href="/imgrank/" target="_blank">热图</a>
<a  href="/text/" target="_blank">文字</a>
<a  href="/history/" target="_blank">穿越</a>
<a  href="/pic/" target="_blank">糗图</a>
<a  href="/textnew/" target="_blank">新鲜</a>

<!--<a href="http://www.youliaodao.cn" target="_blank" rel="nofollow">百科</a>-->
</div>
<div class="userbar clearfix hidden">
<div class="login hidden">
<a href="/my" class="username" id="uname" rel="nofollow"></a>
</div>
<div class="logout">
<a href="javascript:void(0);" class="fn-signin-required logintop" id='logintop' rel="nofollow" style="font-size:16.5px;">登录</a>
</div>
</div>
</div>
</div>



<div id="content" class="main">
<div class="content-block clearfix">
<!-- 暂停更新提示 -->
<!-- <img src="/static/images/banner.png" alt="" style="width: 100%; margin: 16px 0 0; display: block"> -->

<div id="content-left" class="col1">








<div class="article block untagged mb15 typs_long" id='qiushi_tag_121335098'>


<div class="author clearfix">
<a href="/users/22028925/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2202/22028925/thumb/20181207225632.jpg?imageView2/1/w/90/h/90" alt="毒男·i">
</a>
<a href="/users/22028925/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
毒男·i
</h2>
</a>
<div class="articleGender manIcon">101</div>
</div>

<a href="/article/121335098" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


认识了一个女朋友，女朋友昨天让我去她家，说是给她爸妈一个惊喜。<br/>我答应了，于是就买了好多礼物去她家，还买个钻戒，以示诚意当面向她求婚。<br/>女友爸妈看看我，仔细端详我，大吼：“我姑娘是大龄剩女，说---你是不是她花钱雇来的，好糊弄我们俩？”<br/>我赶紧说：“叔叔阿姨，我们是真爱！”<br/>女友爸妈满意地点点头！<br/>今天我再联系女友联系不上了，她给我留下一条短信：“一切都是假的，你吃一堑长一智吧！我的爸妈是雇来的！”

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">954</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335098" data-share="/article/121335098" id="c-121335098" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">6</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335098" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335098" class="up">
<a href="javascript:voting(121335098,1)" class="voting" data-article="121335098" id="up-121335098" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">964</span>
</a>
</li>
<li id="vote-dn-121335098" class="down">
<a href="javascript:voting(121335098,-1)" class="voting" data-article="121335098" id="dn-121335098" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-10</span>
</a>
</li>
<li class="comments">
<a href="/article/121335098" id="c-121335098" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335098" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">深巷探花郎‘：</span>
<div class="main-text">
你哈哈一笑：早就知道是假的了，我钻戒买的二元店的，就连那天晚上用的杰士邦都是二元店的。
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


42

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335730'>


<div class="author clearfix">
<a href="/users/37883273/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3788/37883273/thumb/20180805220452.jpg?imageView2/1/w/90/h/90" alt="半夜提枪就">
</a>
<a href="/users/37883273/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
半夜提枪就
</h2>
</a>
<div class="articleGender manIcon">99</div>
</div>

<a href="/article/121335730" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


看房回来，身心俱疲。<br/><br/>老婆埋怨:同样是当婆婆，你看别人家的，一下拿出几十万上百万帮着买房，你们家，哼！<br/><br/>我也气了:同样是丈母娘，别人家的，结婚前都是百般刁难，买房只是基本操作。当初房价那么低，你妈就这么草率的答应了，连最基本的刁难都没有，有这么当丈母娘的吗？

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2431</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335730" data-share="/article/121335730" id="c-121335730" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">28</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335730" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335730" class="up">
<a href="javascript:voting(121335730,1)" class="voting" data-article="121335730" id="up-121335730" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2449</span>
</a>
</li>
<li id="vote-dn-121335730" class="down">
<a href="javascript:voting(121335730,-1)" class="voting" data-article="121335730" id="dn-121335730" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-18</span>
</a>
</li>
<li class="comments">
<a href="/article/121335730" id="c-121335730" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335730" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">！未央！：</span>
<div class="main-text">
你的想法和正常人有点不一样撒？
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


87

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121333851'>


<div class="author clearfix">
<a href="/users/39388283/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3938/39388283/thumb/20181206213844.jpg?imageView2/1/w/90/h/90" alt="我打豆豆你是豆豆">
</a>
<a href="/users/39388283/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
我打豆豆你是豆豆
</h2>
</a>
<div class="articleGender manIcon">38</div>
</div>

<a href="/article/121333851" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


同事小张：“豆豆哥哥，怎么突然戒烟了？原来你不是说烟难戒么？”我：“因为最近吸烟老是头疼，所以就不吸了。”小张：“吸烟多了顶多头晕，怎么会头疼？”我：“我不是刚交个女朋友么，她看见我吸烟就拿东西砸我头。。。。。。”[捂脸][捂脸]

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2053</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121333851" data-share="/article/121333851" id="c-121333851" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">73</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121333851" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121333851" class="up">
<a href="javascript:voting(121333851,1)" class="voting" data-article="121333851" id="up-121333851" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2066</span>
</a>
</li>
<li id="vote-dn-121333851" class="down">
<a href="javascript:voting(121333851,-1)" class="voting" data-article="121333851" id="dn-121333851" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-13</span>
</a>
</li>
<li class="comments">
<a href="/article/121333851" id="c-121333851" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121333851" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">半截烟云：</span>
<div class="main-text">
有女朋友还抽什么烟，是女朋友不好玩吗？
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


22

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335072'>


<div class="author clearfix">
<a href="/users/12218602/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1221/12218602/thumb/20181007002300.jpg?imageView2/1/w/90/h/90" alt="老柴家的郡主">
</a>
<a href="/users/12218602/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
老柴家的郡主
</h2>
</a>
<div class="articleGender womenIcon">86</div>
</div>

<a href="/article/121335072" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


检查儿子作业，作文题目我的妈妈。儿子写的:孩子是遗落人间的明珠，而妈妈则是上帝派来保护孩子的天使。而我则是上帝掉落的陀螺，我妈妈就是那个喜欢抽陀螺的魔鬼……

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">9223</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335072" data-share="/article/121335072" id="c-121335072" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">92</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335072" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335072" class="up">
<a href="javascript:voting(121335072,1)" class="voting" data-article="121335072" id="up-121335072" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">9245</span>
</a>
</li>
<li id="vote-dn-121335072" class="down">
<a href="javascript:voting(121335072,-1)" class="voting" data-article="121335072" id="dn-121335072" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-22</span>
</a>
</li>
<li class="comments">
<a href="/article/121335072" id="c-121335072" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335072" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">老柴家的郡主：</span>
<div class="main-text">
我觉得这儿子平常抽少了
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


114

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_117349542'>


<div class="author clearfix">
<a href="/users/18406667/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1840/18406667/thumb/20180722205455.jpg?imageView2/1/w/90/h/90" alt="温饱思">
</a>
<a href="/users/18406667/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
温饱思
</h2>
</a>
<div class="articleGender manIcon">25</div>
</div>

<a href="/article/117349542" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


过来看，过来看啦啊，姑娘便宜卖了啊。。。

</span>

</div>
</a>
<!-- 图片或gif -->



<div class="thumb">

<a href="/article/117349542" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11734/117349542/medium/app117349542.jpg" alt="糗事#117349542" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">172</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/117349542" data-share="/article/117349542" id="c-117349542" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">8</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_117349542" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117349542" class="up">
<a href="javascript:voting(117349542,1)" class="voting" data-article="117349542" id="up-117349542" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">184</span>
</a>
</li>
<li id="vote-dn-117349542" class="down">
<a href="javascript:voting(117349542,-1)" class="voting" data-article="117349542" id="dn-117349542" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-12</span>
</a>
</li>
<li class="comments">
<a href="/article/117349542" id="c-117349542" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121336531'>


<div class="author clearfix">
<a href="/users/33887946/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3388/33887946/thumb/20181115195700.jpg?imageView2/1/w/90/h/90" alt="天涯明月刀。">
</a>
<a href="/users/33887946/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
天涯明月刀。
</h2>
</a>
<div class="articleGender manIcon">28</div>
</div>

<a href="/article/121336531" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


我二姑出嫁的时候陪嫁了一辆自行车，由于姑姑和姑父都不会骑。姑姑和姑父说留着以后给孩子骑。等表弟长大了，表弟说那个自行车太老不骑。姑妈咬着牙对表弟说：你不骑留着给你孩子骑。表弟现在都28岁了还没有女朋友，姑妈现在没事就把那辆自行车拿出来擦一擦……

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1740</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121336531" data-share="/article/121336531" id="c-121336531" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">19</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121336531" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121336531" class="up">
<a href="javascript:voting(121336531,1)" class="voting" data-article="121336531" id="up-121336531" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1746</span>
</a>
</li>
<li id="vote-dn-121336531" class="down">
<a href="javascript:voting(121336531,-1)" class="voting" data-article="121336531" id="dn-121336531" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-6</span>
</a>
</li>
<li class="comments">
<a href="/article/121336531" id="c-121336531" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121336531" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">萝卜她男人：</span>
<div class="main-text">
这是一辆传世的自行车啊
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


24

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335592'>


<div class="author clearfix">
<a href="/users/26217894/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2621/26217894/thumb/20181209042528.jpg?imageView2/1/w/90/h/90" alt="聊天不撩妹子">
</a>
<a href="/users/26217894/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
聊天不撩妹子
</h2>
</a>
<div class="articleGender manIcon">53</div>
</div>

<a href="/article/121335592" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


星期天正准备美美的睡个回笼觉。老婆一大早就把我叫醒了。<br/>问她干啥呢？难得一天休息让我多睡一会不行吗？<br/>她说：没啥事，就是让你知道每次半夜三更把我叫醒有多讨厌。<br/>我。。。。。。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1379</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335592" data-share="/article/121335592" id="c-121335592" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">26</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335592" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335592" class="up">
<a href="javascript:voting(121335592,1)" class="voting" data-article="121335592" id="up-121335592" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1386</span>
</a>
</li>
<li id="vote-dn-121335592" class="down">
<a href="javascript:voting(121335592,-1)" class="voting" data-article="121335592" id="dn-121335592" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-7</span>
</a>
</li>
<li class="comments">
<a href="/article/121335592" id="c-121335592" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335592" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">胖香：</span>
<div class="main-text">
报复！真是赤果果的报复
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


16

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121336159'>


<div class="author clearfix">
<a href="/users/37507340/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3750/37507340/thumb/20181016231924.jpg?imageView2/1/w/90/h/90" alt="奔跑的小土狼">
</a>
<a href="/users/37507340/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
奔跑的小土狼
</h2>
</a>
<div class="articleGender manIcon">26</div>
</div>

<a href="/article/121336159" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


老爸在微信上告诉我，猪场卖猪了。问我用不用钱，不用就存整年的了<br/>我回复他：给我转1万到支付宝吧<br/>……钱到账后，我点了“给对方回个话”：收到，谢谢<br/>谁知没过一会儿，我爸电话打来了：我这是借你，可不是给你啊<br/>我：我也没说不还呀<br/>老爸：你这一句谢谢，弄的我心里没底

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">3982</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121336159" data-share="/article/121336159" id="c-121336159" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">33</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121336159" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121336159" class="up">
<a href="javascript:voting(121336159,1)" class="voting" data-article="121336159" id="up-121336159" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">3997</span>
</a>
</li>
<li id="vote-dn-121336159" class="down">
<a href="javascript:voting(121336159,-1)" class="voting" data-article="121336159" id="dn-121336159" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-15</span>
</a>
</li>
<li class="comments">
<a href="/article/121336159" id="c-121336159" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121336159" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">茂比乌斯：</span>
<div class="main-text">
我对“狼子野心”这个成语有了更清晰的了解。
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


113

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335958'>


<div class="author clearfix">
<a href="/users/33676416/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3367/33676416/thumb/20181130115820.jpg?imageView2/1/w/90/h/90" alt="飞漠刀影!">
</a>
<a href="/users/33676416/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
飞漠刀影!
</h2>
</a>
<div class="articleGender manIcon">25</div>
</div>

<a href="/article/121335958" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


开会，旁边的萌妹子同事低着腰，一脸难受。这是个献殷勤的好机会，我准备找借口出去买红糖跟姨妈巾，我小声说：“我帮你。”<br/>妹子捂着胸口说你帮不了。<br/>我：我一直看着你，晓得你为什么难受……<br/>还没说完，妹子杏眼圆瞪：“你怎么知道我内衣钢圈跑出来了？你偷看我上厕所了?!”

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1571</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335958" data-share="/article/121335958" id="c-121335958" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">22</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335958" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335958" class="up">
<a href="javascript:voting(121335958,1)" class="voting" data-article="121335958" id="up-121335958" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1580</span>
</a>
</li>
<li id="vote-dn-121335958" class="down">
<a href="javascript:voting(121335958,-1)" class="voting" data-article="121335958" id="dn-121335958" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-9</span>
</a>
</li>
<li class="comments">
<a href="/article/121335958" id="c-121335958" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335958" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">天涯明月刀。：</span>
<div class="main-text">
楼主：说出来你可能不信，我刚刚低头看见的
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


28

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_117348507'>


<div class="author clearfix">
<a href="/users/31990897/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3199/31990897/thumb/2016112121193044.JPEG?imageView2/1/w/90/h/90" alt="小黄果树">
</a>
<a href="/users/31990897/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
小黄果树
</h2>
</a>
<div class="articleGender womenIcon">101</div>
</div>

<a href="/article/117348507" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


昨天在做家务，没时间陪儿子，小不点自己在那看碟片，我恍然看到看到屏幕上几个光❌❌的屁股，我说儿子你在干嘛！他说没干嘛，突然发现小家伙的脸好红，好红，我希望儿子长大不要随他老爸！

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">422</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/117348507" data-share="/article/117348507" id="c-117348507" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">20</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_117348507" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117348507" class="up">
<a href="javascript:voting(117348507,1)" class="voting" data-article="117348507" id="up-117348507" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">443</span>
</a>
</li>
<li id="vote-dn-117348507" class="down">
<a href="javascript:voting(117348507,-1)" class="voting" data-article="117348507" id="dn-117348507" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-21</span>
</a>
</li>
<li class="comments">
<a href="/article/117348507" id="c-117348507" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335576'>


<div class="author clearfix">
<a href="/users/26217894/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2621/26217894/thumb/20181209042528.jpg?imageView2/1/w/90/h/90" alt="聊天不撩妹子">
</a>
<a href="/users/26217894/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
聊天不撩妹子
</h2>
</a>
<div class="articleGender manIcon">53</div>
</div>

<a href="/article/121335576" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


没事跟老婆聊微信，我说：老婆你那么好看，当年那么多人追你为啥就看上我了。<br/>老婆：当年我口味重，想品尝牛粪是啥味的。我说：这么多尝出来吗？<br/>老婆：没有，关键是爸妈喜欢你。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1796</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335576" data-share="/article/121335576" id="c-121335576" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">37</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335576" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335576" class="up">
<a href="javascript:voting(121335576,1)" class="voting" data-article="121335576" id="up-121335576" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1805</span>
</a>
</li>
<li id="vote-dn-121335576" class="down">
<a href="javascript:voting(121335576,-1)" class="voting" data-article="121335576" id="dn-121335576" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-9</span>
</a>
</li>
<li class="comments">
<a href="/article/121335576" id="c-121335576" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335576" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">爱新觉罗.黄瓜：</span>
<div class="main-text">
好一坨牛粪！能赢得丈母娘和老丈人的青睐，也没谁了
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


23

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335078'>


<div class="author clearfix">
<a href="/users/32215536/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3221/32215536/thumb/20181122212921.jpg?imageView2/1/w/90/h/90" alt="吃了两碗又盛">
</a>
<a href="/users/32215536/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
吃了两碗又盛
</h2>
</a>
<div class="articleGender manIcon">39</div>
</div>

<a href="/article/121335078" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


儿子的数学书上有介绍衡量生活水平的恩格尔系数的计算方法，他问我一个月消费多少钱，其中购买食品消费多少。<br/>我大概地说:一共花三千左右，买吃的两千左右。<br/>儿子一算，是66%，属于贫困人口。<br/>这不得不引起我的重视，仔细想了一下，其实消费总额比三千多，购买食品比两千少，儿子再算，得出25%，属于富裕人口。<br/>媳妇在洗脸，听见这件事说:咱们家这么一会儿就脱 贫了？

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">4208</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335078" data-share="/article/121335078" id="c-121335078" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">129</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335078" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335078" class="up">
<a href="javascript:voting(121335078,1)" class="voting" data-article="121335078" id="up-121335078" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">4239</span>
</a>
</li>
<li id="vote-dn-121335078" class="down">
<a href="javascript:voting(121335078,-1)" class="voting" data-article="121335078" id="dn-121335078" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-31</span>
</a>
</li>
<li class="comments">
<a href="/article/121335078" id="c-121335078" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335078" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">无字碑9：</span>
<div class="main-text">
这个不科学，比如我天天吃食堂，食品支出约百分之十五，难道我一个月5000收入也是极其富裕！
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


83

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121331976'>


<div class="author clearfix">
<a href="/users/40079218/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/4007/40079218/thumb/20181209142829.jpg?imageView2/1/w/90/h/90" alt="美女的微笑">
</a>
<a href="/users/40079218/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
美女的微笑
</h2>
</a>
<div class="articleGender womenIcon">27</div>
</div>

<a href="/article/121331976" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


刚刚从支付宝借了5800。请问，怎样才能不还钱？身份证已经扔了，他们应该找不到我了吧😊[臭美][臭美][臭美]

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2443</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121331976" data-share="/article/121331976" id="c-121331976" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">99</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121331976" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121331976" class="up">
<a href="javascript:voting(121331976,1)" class="voting" data-article="121331976" id="up-121331976" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2461</span>
</a>
</li>
<li id="vote-dn-121331976" class="down">
<a href="javascript:voting(121331976,-1)" class="voting" data-article="121331976" id="dn-121331976" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-18</span>
</a>
</li>
<li class="comments">
<a href="/article/121331976" id="c-121331976" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121331976" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">随心灬随缘灬：</span>
<div class="main-text">
刚捡个身份证  办两张信用卡唰唰去
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


70

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335751'>


<div class="author clearfix">
<a href="/users/35959614/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3595/35959614/thumb/20181203204514.jpg?imageView2/1/w/90/h/90" alt="雷霆万钧～">
</a>
<a href="/users/35959614/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
雷霆万钧～
</h2>
</a>
<div class="articleGender manIcon">28</div>
</div>

<a href="/article/121335751" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


赶一天一趟的中巴车回老家村里，车上人爆满，好不容易挤上去，车要开了，一个大叔站在车门边，冲着司机大声说：哎，老李啊，咱们刚刚一起吃饭，你比我还多喝了二两，我都觉得晕了，你还能开车，果然你酒量比我好啊！<br/>只见刚刚还爆满的车瞬间就空了，那个大叔慢悠悠地上了车，冲一脸茫然的司机说：哎呀不好意思，喝多了，认错人了！

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2102</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335751" data-share="/article/121335751" id="c-121335751" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">21</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335751" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335751" class="up">
<a href="javascript:voting(121335751,1)" class="voting" data-article="121335751" id="up-121335751" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2107</span>
</a>
</li>
<li id="vote-dn-121335751" class="down">
<a href="javascript:voting(121335751,-1)" class="voting" data-article="121335751" id="dn-121335751" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-5</span>
</a>
</li>
<li class="comments">
<a href="/article/121335751" id="c-121335751" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335751" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">晓颜诺诺～：</span>
<div class="main-text">
把大家吓得下了车，大叔想坐哪坐哪了
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


28

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_117348312'>


<div class="author clearfix">
<a href="/users/28086408/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2808/28086408/thumb/2016073016481055.JPEG?imageView2/1/w/90/h/90" alt="道观里的和尚">
</a>
<a href="/users/28086408/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
道观里的和尚
</h2>
</a>
<div class="articleGender manIcon">26</div>
</div>

<a href="/article/117348312" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


铲屎的，你看我像不像熊大

</span>

</div>
</a>
<!-- 图片或gif -->



<div class="thumb">

<a href="/article/117348312" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11734/117348312/medium/app117348312.jpg" alt="糗事#117348312" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">194</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/117348312" data-share="/article/117348312" id="c-117348312" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">4</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_117348312" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117348312" class="up">
<a href="javascript:voting(117348312,1)" class="voting" data-article="117348312" id="up-117348312" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">205</span>
</a>
</li>
<li id="vote-dn-117348312" class="down">
<a href="javascript:voting(117348312,-1)" class="voting" data-article="117348312" id="dn-117348312" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-11</span>
</a>
</li>
<li class="comments">
<a href="/article/117348312" id="c-117348312" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335204'>


<div class="author clearfix">
<a href="/users/33491754/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3349/33491754/thumb/20181204153354.jpg?imageView2/1/w/90/h/90" alt="我是煮茶">
</a>
<a href="/users/33491754/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
我是煮茶
</h2>
</a>
<div class="articleGender manIcon">33</div>
</div>

<a href="/article/121335204" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


感冒了，我躺在床上觉得一张被子太单薄，连打了几喷嚏，我老婆立马就起来，冒着冷空气去柜子取出一张被子。<br/>我当时心里满满的感动……<br/>我老婆把被子放床上：“一人一张被子，这样你打喷嚏就不会老往我被子里灌冷风...”

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1891</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335204" data-share="/article/121335204" id="c-121335204" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">25</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335204" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335204" class="up">
<a href="javascript:voting(121335204,1)" class="voting" data-article="121335204" id="up-121335204" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1898</span>
</a>
</li>
<li id="vote-dn-121335204" class="down">
<a href="javascript:voting(121335204,-1)" class="voting" data-article="121335204" id="dn-121335204" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-7</span>
</a>
</li>
<li class="comments">
<a href="/article/121335204" id="c-121335204" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335204" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">道士下山会女神：</span>
<div class="main-text">
一人一被（辈）子，那叫单身
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


24

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335845'>


<div class="author clearfix">
<a href="/users/30523551/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3052/30523551/thumb/20181208234521.jpg?imageView2/1/w/90/h/90" alt="秋心不凉">
</a>
<a href="/users/30523551/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
秋心不凉
</h2>
</a>
<div class="articleGender manIcon">32</div>
</div>

<a href="/article/121335845" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


不好意思跟哥们开口借钱，弄了个女号，被他附近人搜到了。因为比较了解他，两人越聊越嗨，这货想看照片，就网上弄组美女照片发给他，还找了几张生活照，变声器语音都是经常的。忽悠了几天，表达了一下缺钱用，这货立马给我转了1314，然后我就把号扔了。<br/>过了几天，这小子难受来找我喝酒，结果我俩都喝大了，不小心说出了真相...

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2765</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335845" data-share="/article/121335845" id="c-121335845" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">58</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335845" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335845" class="up">
<a href="javascript:voting(121335845,1)" class="voting" data-article="121335845" id="up-121335845" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2783</span>
</a>
</li>
<li id="vote-dn-121335845" class="down">
<a href="javascript:voting(121335845,-1)" class="voting" data-article="121335845" id="dn-121335845" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-18</span>
</a>
</li>
<li class="comments">
<a href="/article/121335845" id="c-121335845" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335845" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">日丽贤：</span>
<div class="main-text">
这是钱的事吗？这是一屁股帐
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


40

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121299572'>


<div class="author clearfix">
<a href="/users/31185312/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3118/31185312/thumb/20160212061908.jpg?imageView2/1/w/90/h/90" alt="落~*.*~英">
</a>
<a href="/users/31185312/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
落~*.*~英
</h2>
</a>
<div class="articleGender womenIcon">24</div>
</div>

<a href="/article/121299572" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


上次叫女儿下楼去给我买两个蒜，回来就真的只有两个，而且还是独蒜。问她为什么不多买几个，她说你只叫我买两个的。今天叫老公给我买碗稀饭，就真的只有稀饭，连咸菜都没有。问为什么没有咸菜，人家说你只叫我买稀饭，没叫我买咸菜。你们两个真的是亲生的父女。都怪我

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">3413</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121299572" data-share="/article/121299572" id="c-121299572" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">54</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121299572" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121299572" class="up">
<a href="javascript:voting(121299572,1)" class="voting" data-article="121299572" id="up-121299572" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">3430</span>
</a>
</li>
<li id="vote-dn-121299572" class="down">
<a href="javascript:voting(121299572,-1)" class="voting" data-article="121299572" id="dn-121299572" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-17</span>
</a>
</li>
<li class="comments">
<a href="/article/121299572" id="c-121299572" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121299572" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">无^_^昵称：</span>
<div class="main-text">
你叫他们父女吃饭，如果他们吃菜你就揍他俩
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


149

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121311349'>


<div class="author clearfix">
<a href="/users/30485044/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3048/30485044/thumb/20180725151847.jpg?imageView2/1/w/90/h/90" alt="半醉半醒梦中人">
</a>
<a href="/users/30485044/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
半醉半醒梦中人
</h2>
</a>
<div class="articleGender manIcon">33</div>
</div>

<a href="/article/121311349" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


老妈最近一段时间迷上养金鱼了，由于不会养，三条五天的就死几条，这不，一大早的又在捞死鱼<br/>妈，我发现你养鱼的流程和别人养鱼的流程有点一样啊！<br/>咋不一样了?<br/>人家鱼是经常换水你养鱼是经常换鱼啊

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1761</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121311349" data-share="/article/121311349" id="c-121311349" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">28</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121311349" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121311349" class="up">
<a href="javascript:voting(121311349,1)" class="voting" data-article="121311349" id="up-121311349" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1767</span>
</a>
</li>
<li id="vote-dn-121311349" class="down">
<a href="javascript:voting(121311349,-1)" class="voting" data-article="121311349" id="dn-121311349" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-6</span>
</a>
</li>
<li class="comments">
<a href="/article/121311349" id="c-121311349" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121311349" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">咦！我的大脸猫呢：</span>
<div class="main-text">
老妈：你要是给我整个孙子，我特么还养鱼？
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


12

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_117348548'>


<div class="author clearfix">
<a href="/users/31191822/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3119/31191822/thumb/20160414192313.jpg?imageView2/1/w/90/h/90" alt="南张麻花">
</a>
<a href="/users/31191822/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
南张麻花
</h2>
</a>
<div class="articleGender manIcon">36</div>
</div>

<a href="/article/117348548" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


谁知道是什么植物？

</span>

</div>
</a>
<!-- 图片或gif -->



<div class="thumb">

<a href="/article/117348548" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11734/117348548/medium/app117348548.jpg" alt="糗事#117348548" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">109</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/117348548" data-share="/article/117348548" id="c-117348548" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">9</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_117348548" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117348548" class="up">
<a href="javascript:voting(117348548,1)" class="voting" data-article="117348548" id="up-117348548" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">123</span>
</a>
</li>
<li id="vote-dn-117348548" class="down">
<a href="javascript:voting(117348548,-1)" class="voting" data-article="117348548" id="dn-117348548" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-14</span>
</a>
</li>
<li class="comments">
<a href="/article/117348548" id="c-117348548" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121291377'>


<div class="author clearfix">
<a href="/users/17535149/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1753/17535149/thumb/20181026133404.jpg?imageView2/1/w/90/h/90" alt="无书斋主">
</a>
<a href="/users/17535149/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
无书斋主
</h2>
</a>
<div class="articleGender manIcon">40</div>
</div>

<a href="/article/121291377" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


今天去乡下办事，一别克君威别车，连别三次后，我想起兵法有云:狭路相逢勇者胜……<br/>来，别我，我就加油……<br/>别克直接怂了……<br/>到了目的地后一会，别克也来了……<br/>原单位老领导笑呵呵的过来:这么多年了，脾气还是没变啊？……

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">4393</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121291377" data-share="/article/121291377" id="c-121291377" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">40</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121291377" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121291377" class="up">
<a href="javascript:voting(121291377,1)" class="voting" data-article="121291377" id="up-121291377" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">4415</span>
</a>
</li>
<li id="vote-dn-121291377" class="down">
<a href="javascript:voting(121291377,-1)" class="voting" data-article="121291377" id="dn-121291377" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-22</span>
</a>
</li>
<li class="comments">
<a href="/article/121291377" id="c-121291377" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121291377" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">半截烟云：</span>
<div class="main-text">
领导一直换车，你还是那一辆
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


44

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335124'>


<div class="author clearfix">
<a href="/users/17221979/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1722/17221979/thumb/20180524141023.JPEG?imageView2/1/w/90/h/90" alt="挖鼻孔的老虎">
</a>
<a href="/users/17221979/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
挖鼻孔的老虎
</h2>
</a>
<div class="articleGender manIcon">101</div>
</div>

<a href="/article/121335124" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


有家洗脚店要装修，我去量尺寸、谈条件，一直倒腾到晚上九点，出来时太累就打了出租。<br/>回到小区门口下车，遇到老婆在买烧烤，她走过来问司机：“师傅，他在哪里上车的？”<br/>司机说：“新华书店。”然后一踩油门走了。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">6931</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335124" data-share="/article/121335124" id="c-121335124" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">78</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335124" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335124" class="up">
<a href="javascript:voting(121335124,1)" class="voting" data-article="121335124" id="up-121335124" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">6952</span>
</a>
</li>
<li id="vote-dn-121335124" class="down">
<a href="javascript:voting(121335124,-1)" class="voting" data-article="121335124" id="dn-121335124" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-21</span>
</a>
</li>
<li class="comments">
<a href="/article/121335124" id="c-121335124" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335124" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">醉酒提剑捉泥鳅：</span>
<div class="main-text">
还是男人了解男人。
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


187

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121336058'>


<div class="author clearfix">
<a href="/users/33887946/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3388/33887946/thumb/20181115195700.jpg?imageView2/1/w/90/h/90" alt="天涯明月刀。">
</a>
<a href="/users/33887946/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
天涯明月刀。
</h2>
</a>
<div class="articleGender manIcon">28</div>
</div>

<a href="/article/121336058" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


早 上和 女友 拌了几句 嘴，她气 鼓 鼓的躺 床 上 直到八点半都不起床，眼看 着九点我 两都要上 班，时 间不多了，好说歹说就是没用。<br/>我一看不成， 往 床 上 一 扑:生气？那就给你把 气 放咯！<br/>十分钟后……我抽 着烟，很忧愁，她更 生 气了……

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2292</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121336058" data-share="/article/121336058" id="c-121336058" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">57</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121336058" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121336058" class="up">
<a href="javascript:voting(121336058,1)" class="voting" data-article="121336058" id="up-121336058" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2311</span>
</a>
</li>
<li id="vote-dn-121336058" class="down">
<a href="javascript:voting(121336058,-1)" class="voting" data-article="121336058" id="dn-121336058" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-19</span>
</a>
</li>
<li class="comments">
<a href="/article/121336058" id="c-121336058" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121336058" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">贝格格*：</span>
<div class="main-text">
用你的牙签用力扎，不信放不了气
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


35

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335055'>


<div class="author clearfix">
<a href="/users/34246786/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3424/34246786/thumb/20181208211338.jpg?imageView2/1/w/90/h/90" alt="老巫婆～～">
</a>
<a href="/users/34246786/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
老巫婆～～
</h2>
</a>
<div class="articleGender womenIcon">22</div>
</div>

<a href="/article/121335055" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


一大早老公就在我耳边吹气，让我想办法帮他给公司里请假。<br/>也不知道这辈子是不是欠他的，他只要在我面前软言软语，我就特别心软。<br/>无奈之下我只能含情脉脉的对老公说:“请假的事包在我身上，但是你要先满 足 我一个 要 求！”<br/>老公立马翻身下床，一边穿衣服一边说:“还是工作要紧！”

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2456</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335055" data-share="/article/121335055" id="c-121335055" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">48</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335055" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335055" class="up">
<a href="javascript:voting(121335055,1)" class="voting" data-article="121335055" id="up-121335055" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2472</span>
</a>
</li>
<li id="vote-dn-121335055" class="down">
<a href="javascript:voting(121335055,-1)" class="voting" data-article="121335055" id="dn-121335055" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-16</span>
</a>
</li>
<li class="comments">
<a href="/article/121335055" id="c-121335055" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335055" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">爱新觉罗.黄瓜：</span>
<div class="main-text">
你万一给我弄骨折了咋办？所以上班才最安全的
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


35

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_117349314'>


<div class="author clearfix">
<a href="/users/20927437/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2092/20927437/thumb/20151119063828.jpg?imageView2/1/w/90/h/90" alt="张西贝">
</a>
<a href="/users/20927437/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
张西贝
</h2>
</a>
<div class="articleGender manIcon">24</div>
</div>

<a href="/article/117349314" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


人真的他娘的不能太善良。以后我再善良我是个驴。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">237</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/117349314" data-share="/article/117349314" id="c-117349314" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">14</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_117349314" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117349314" class="up">
<a href="javascript:voting(117349314,1)" class="voting" data-article="117349314" id="up-117349314" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">249</span>
</a>
</li>
<li id="vote-dn-117349314" class="down">
<a href="javascript:voting(117349314,-1)" class="voting" data-article="117349314" id="dn-117349314" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-12</span>
</a>
</li>
<li class="comments">
<a href="/article/117349314" id="c-117349314" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>





<!-- 全局翻页组件 -->

<ul class="pagination">


<li>
<span class="current" >
1
</span>
</li>




<li>
<a href="/hot/page/2/" rel="nofollow">
<!--<a href="/hot/page/2/" rel="nofollow">-->
<span class="page-numbers">
2
</span>
</a>
</li>



<li>
<a href="/hot/page/3/" rel="nofollow">
<!--<a href="/hot/page/3/" rel="nofollow">-->
<span class="page-numbers">
3
</span>
</a>
</li>



<li>
<a href="/hot/page/4/" rel="nofollow">
<!--<a href="/hot/page/4/" rel="nofollow">-->
<span class="page-numbers">
4
</span>
</a>
</li>



<li>
<a href="/hot/page/5/" rel="nofollow">
<!--<a href="/hot/page/5/" rel="nofollow">-->
<span class="page-numbers">
5
</span>
</a>
</li>



<li>
<span class="dots">
…
</span>
</li>


<li>
<a href="/hot/page/13/" rel="nofollow">
<!--<a href="/hot/page/13/" rel="nofollow">-->
<span class="page-numbers">
13
</span>
</a>
</li>


<li>
<a href="/hot/page/2/" rel="nofollow">
<!--<a href="/hot/page/2/" rel="nofollow">-->
<span class="next">
下一页
</span>
</a>
</li>

</ul>


</div>



<div class="col2">
<div id="sidebar" class="sidebar">

<div class="shopwindow">
<!-- 55736473：web-右侧悬浮-up 类型：固定 尺寸：300x250-->
<!-- 新广告代码：2017-05-03 -->
<!-- <script type="text/javascript">
document.write('<a style="display:none!important" id="tanx-a-mm_108378320_8760716_29674533"></a>');
tanx_s = document.createElement("script");
tanx_s.type = "text/javascript";
tanx_s.charset = "gbk";
tanx_s.id = "tanx-s-mm_108378320_8760716_29674533";
tanx_s.async = true;
tanx_s.src = "https://phs.tanx.com/ex?i=mm_108378320_8760716_29674533";
tanx_h = document.getElementsByTagName("head")[0];
if(tanx_h)tanx_h.insertBefore(tanx_s,tanx_h.firstChild);
</script> -->
<!-- <script type="text/javascript">
var cpro_id = "u693365";
</script>
<script type="text/javascript" src="https://cpro.baidustatic.com/cpro/ui/c.js"></script> -->
<script>
document.write('<script src="//becode.qiushibaike.com/common/e9w7.js?kfxohnx=go" type="text/javascript"><\/script>');
</script>
</div>

<div class="shopwindow" id="listAd2">
<!-- 55736473：web-右侧悬浮-up 类型：固定 尺寸：300x250-->
<!-- 新广告代码：2017-05-03 -->
<!-- <script type="text/javascript">
/*右侧2*/
// var cpro_id = "u693365";
// document.write('<script type="text/javascript" src="https://cpro.baidustatic.com/cpro/ui/c.js"><\/script>');
// 2017-5-23 修改
// FTAPI_slotid = 1026761;FTAPI_sync = true
// document.write('<script src="//pic.fastapi.net/sdk/js/a.js" charset="utf-8"><\/script>')
</script> -->
<script type="text/javascript" src="//becode.qiushibaike.com/production/resource/d3nkw.js?m=hgpzzge"></script>
</div>


<div class="sidebar-other">
<img src="/static/images/productlist/ctrl_d.png">
<p>把糗事百科加入收藏夹</p>
</div>
<div class="sidebar-hot clearfix" id="sidebar-qrcode">
<div class="float-left qrcode">
<img src="/static/images/web_v3/sidebar/qiubai_qrcode.png" alt="糗事百科 APP 下载二维码">
</div>
<div class="float-left btn-box">
<a href="javascript:void(0)" class="btn-download ios" onclick="window.open('https://itunes.apple.com/cn/app/id422853458?mt=8')" target="_blank">iOS 下载</a>
<a href="javascript:void(0)" class="btn-download android" onclick="window.open('http://static.qiushibaike.com/qiushibaike.apk')" target="_blank">Android 下载</a>
<p class="tips">扫码下载糗事百科app</p>
</div>
</div>
<!-- 直播下载链接 -->
<div class="sidebar-hot clearfix" id="sidebar-remix">
<a href="https://www.app-remix.com/v1/pc/living?chn=qiubai" onclick="_hmt.push(['_trackEvent', 'web-remix', 'chick']);" target="_blank">
<img src="//static.qiushibaike.com/images/web_v3/sidebar/remix_banner.gif?v=f8bbbe7ca7cd5b9314e8235d6290fb0f" alt="">
</a>
</div>
<!-- 浪人杀下载链接 -->
<!--<div class="sidebar-hot clearfix" id="sidebar-wolf">-->
<!--<img src="//static.qiushibaike.com/images/web_v3/sidebar/wolf_banner.png?v=b18dc8556489b273af99197ebcf01a1c" alt="">-->
<!--</div>-->
<div class="sidebar-hot clearfix">
<h3>爆笑糗事精选</h3>
<ul>

<li class="item">
<a href="/article/121258827" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12125/121258827/medium/CXKLD1EJB0C22V5V.jpg?imageView2/1/w/146/h/146" alt="现在离职太任性了"/></span>
</a>
<a href="/article/121258827" title="现在离职太任性了" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>现在离职太任性了</p>
</a>
</li>

<li class="item">
<a href="/article/121227810" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12122/121227810/medium/94FHHDU8FDTXFFXP.jpg?imageView2/1/w/146/h/146" alt="对"/></span>
</a>
<a href="/article/121227810" title="对" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>对</p>
</a>
</li>

<li class="item">
<a href="/article/121296724" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12129/121296724/medium/R0UB0GWZ4CHFASXG.jpg?imageView2/1/w/146/h/146" alt="你觉得自己是亲生的吗"/></span>
</a>
<a href="/article/121296724" title="你觉得自己是亲生的吗" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>你觉得自己是亲生的吗</p>
</a>
</li>

<li class="item">
<a href="/article/121262405" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12126/121262405/medium/PD5VPVIO93C3NZKX.jpg?imageView2/1/w/146/h/146" alt="被按在地上摩擦的小熊哥"/></span>
</a>
<a href="/article/121262405" title="被按在地上摩擦的小熊哥" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>被按在地上摩擦的小熊哥</p>
</a>
</li>

<li class="item">
<a href="/article/121297587" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12129/121297587/medium/LI0UZG1D12Y4VAEZ.jpg?imageView2/1/w/146/h/146" alt="你喜欢水手服吗"/></span>
</a>
<a href="/article/121297587" title="你喜欢水手服吗" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>你喜欢水手服吗</p>
</a>
</li>

<li class="item">
<a href="/article/121309939" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12130/121309939/medium/ZD0FZ6K4KSPDAZQM.jpg?imageView2/1/w/146/h/146" alt="这快递为什么要先到东莞再往回跑送惠州"/></span>
</a>
<a href="/article/121309939" title="这快递为什么要先到东莞再往回跑送惠州" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>这快递为什么要先到东莞再往回跑送惠州</p>
</a>
</li>

<li class="item">
<a href="/article/121287240" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12128/121287240/medium/KR32DD85AADFAS7O.jpg?imageView2/1/w/146/h/146" alt="睡个素觉[捂脸]"/></span>
</a>
<a href="/article/121287240" title="睡个素觉[捂脸]" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>睡个素觉[捂脸]</p>
</a>
</li>

<li class="item">
<a href="/article/121268648" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12126/121268648/medium/D69ORH4HIP0BB0E3.jpg?imageView2/1/w/146/h/146" alt="你和你的吃鸡四排队友"/></span>
</a>
<a href="/article/121268648" title="你和你的吃鸡四排队友" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>你和你的吃鸡四排队友</p>
</a>
</li>

</ul>
</div>
<div class="sidebar-hot clearfix" id="sidebar-tab">
<div class="tab-head">
<h3 class="active" data-type="0">热门</h3>
<h3 data-type="1">话题</h3>
<h3 data-type="2">专区</h3>
<h3 data-type="3">推荐</h3>
</div>
<div class="sidebar-tag-block tab-content0">

</div>
<div class="sidebar-tag-block tab-content1 hide">

</div>
<div class="sidebar-tag-block tab-content2 hide">


<li><i># </i><a href="/key/6468931/">深圳联想工资怎么样啊</a><i> #</i></li>

<li><i># </i><a href="/key/6494407/">小乌龟吃什么水草</a><i> #</i></li>

<li><i># </i><a href="/key/6494689/">吃什么补肾养精</a><i> #</i></li>

<li><i># </i><a href="/key/6491499/">脑出血病人恢复期吃什么好</a><i> #</i></li>

<li><i># </i><a href="/key/6455707/">南华大学建筑系怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6454170/">08别克音响怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6476173/">深圳综合高中怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6493912/">乌龟通常吃什么</a><i> #</i></li>

<li><i># </i><a href="/key/6478447/">润雪祛痘霜效果怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6472396/">深圳心华科技电子厂怎么样</a><i> #</i></li>


</div>
<div class="sidebar-tag-block tab-content3 hide">

</div>
</div>

<div class="shopwindow" id="listAd3">
<!-- 55736473：web-右侧悬浮-up 类型：固定 尺寸：300x250-->
<!-- <script type="text/javascript">
document.write('<a style="display:none!important" id="tanx-a-mm_108378320_8760716_29640993"></a >');
tanx_s = document.createElement("script");
tanx_s.type = "text/javascript";
tanx_s.charset = "gbk";
tanx_s.id = "tanx-s-mm_108378320_8760716_29640993";
tanx_s.async = true;
tanx_s.src = "https://phs.tanx.com/ex?i=mm_108378320_8760716_29640993";
tanx_h = document.getElementsByTagName("head")[0];
if(tanx_h)tanx_h.insertBefore(tanx_s,tanx_h.firstChild);
</script> -->
<!-- 新广告代码：2017-05-03 -->
<!-- <script>
var cpro_id = "u1101312";
document.write('<script type="text/javascript" src="https://cpro.baidustatic.com/cpro/ui/c.js"><\/script>');
</script> -->
<script type="text/javascript" src="//becode.qiushibaike.com/production/klcawm.js?gb=tytyyhc"></script>
</div>

<div class="shopwindow">
<!-- 2017.10.16 注释 -->
<!-- <script type="text/javascript" src="https://s.haiyunimg.com/SSP/30169.js"></script> -->
<!-- 2017.10.16 添加 -->
<!-- <script>
var mediav_ad_pub = 'klT513_2129270';
var mediav_ad_width = '300';
var mediav_ad_height = '250';
</script>
<script type="text/javascript" language="javascript" charset="utf-8" src="//static.mediav.com/js/mvf_g2.js"></script> -->
<script type="text/javascript" src="//becode.qiushibaike.com/common/exweb.js?h=cuzuzzie"></script>
</div>

</div>
</div>



</div>
</div>


<div class="foot">
 <div class="foot-ad" id="footAd">
<!-- 68902435：web-底部固定 类型：固定 尺寸：728x90-->
<!-- 2017/2/28 注释旧的广告代码，改为使用 https 的广告 -->
<!-- <script type="text/javascript">//<![CDATA[
ac_as_id = "mm_108378320_13540554_68902435";
ac_format = 1;
ac_mode = 1;
ac_group_id = 1;
ac_server_base_url = "afpeng.alimama.com/";
//]]></script>
<script type="text/javascript" src="//afpmm.alicdn.com/g/mm/afp-cdn/JS/k.js"></script> -->
<!-- <script type="text/javascript">//<!—
google_ad_client = "ca-pub-7443704194229694";
/* IDG.CN_B2C_qiushibaike.com_HY_728x90 */
google_ad_slot = "9826878184";
google_ad_width = 728;
google_ad_height = 90;
//—>
document.write('<script type="text/javascript" src="//pagead2.googlesyndication.com/pagead/show_ads.js"><\/script>');
</script> -->
<script type="text/javascript" src="//becode.qiushibaike.com/production/s401mj.js?ezovy=frbr"></script>
</div>

<div class="foot-nav clearfix">
<div class="foot-nav-col">
<h3>
关于
</h3>
<ul>
<li>
<a href="//about.qiushibaike.com/web_jobs.html#team" target="_blank" rel="nofollow">
关于糗百
</a>
</li>
<li>
<a href="//about.qiushibaike.com/web_jobs.html#tech" target="_blank" rel="nofollow">
加入我们
</a>
</li>
<li>
<a href="//about.qiushibaike.com/web_jobs.html#contact" target="_blank" rel="nofollow">
联系方式
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
帮助
</h3>
<ul>
<li>
<a href="//about.qiushibaike.com/feedback.html" target="_blank" rel="nofollow">
在线反馈
</a>
</li>
<li>
<a href="//about.qiushibaike.com/agreement.html" target="_blank" rel="nofollow">
用户协议
</a>
</li>
<li>
<a href="//about.qiushibaike.com/policy.html" target="_blank" rel="nofollow">
隐私政策
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
下载
</h3>
<ul>
<li>
<a href="https://android.myapp.com/myapp/detail.htm?apkName=qsbk.app"
target="_blank" rel="external nofollow">
Android 客户端
</a>
</li>
<li>
<a href="https://itunes.apple.com/cn/app/id422853458" target="_blank" rel="external nofollow">
iPhone 客户端
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
关注
</h3>
<ul>
<li>
<a href="#" class="foot-wechat">
微信
<div class="foot-wechat-tips">
<span class="foot-wechat-icon"></span>
手机扫描二维码关注
</div>
</a>
</li>
<li>
<a href="http://weibo.com/qiushibaike" target="_blank" rel="external nofollow">
新浪微博
</a>
</li>
<li>
<a href="http://user.qzone.qq.com/1492495058" target="_blank" rel="external nofollow">
QQ空间
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
组织
</h3>
<ul>
<li>
<a href="http://user.qzone.qq.com/1492495058/blog/1408597608" target="_blank"
rel="external nofollow">
官方粉丝群
</a>
</li>
<li>
<a href="https://www.qiushibaike.com/users/37042475" target="_blank"
rel="external nofollow">
<img style="vertical-align: middle;height: 16px;margin-top: -2px;" src="/static/images/beian.png">
首都网警
</a>
</li>
</ul>
</div>
</div>
<div class="foot-copyrights">
<!-- <p>&copy; Qiushibaike.com 糗事百科版权所有</p>
<p>
<span>京ICP备14028348号-1</span>
<span>京ICP证140448号</span>
<span>京网文[2017]2369-247号</span>
<span>
<a style='color:#333' target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502031601" rel="nofollow"><img style='vertical-align: top;' src="/static/images/beian.png?v=d0289dc0a46fc5b15b3363ffa78cf6c7" />京公网安备11010502031601号</a>
</span>
</p>
<p style="margin-top:8px">友际无限（北京）科技有限公司</p>
<p style="margin-top:8px">
<span>互联网违法和不良信息举报电话：010-84872896</span>
<span>邮箱：kefu@qiushibaike.com</span>
</p> -->
<p>互联网ICP备案：京ICP备14028348号-1</p>
<p>
<span>广播电视节目制作经营许可证：（京）字第08319号</span>
<span>网络文化经营许可证：
<a style='color:#333' target="_blank" href="http://sq.ccm.gov.cn:80/ccnt/sczr/service/business/emark/toDetail/"
rel="nofollow">
<img src="/static/images/wenhuajingying.png?v=f5f3976cf4be787ad2be202a19d40823" style='width: 20px; height: 20px; vertical-align: top;'>京网文[2017]2369-247号</a>
</span>
</p>
<p style="margin-top: 8px">电信与信息服务业务经营许可证：京ICP证140448号</p>
<p style="margin-top: 8px"><span>营业性演出许可证：京演(机构)(2018)1940号</span></p>
<p>
<span>计算机信息网络国际联网单位备案：<a style='color:#333' target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502031601" rel="nofollow"><img style='vertical-align: top;' src="/static/images/beian.png?v=d0289dc0a46fc5b15b3363ffa78cf6c7" />京公网安备11010502031601号</a></span>
</p>
<br>
<p style="margin-top: 8px">友际无限（北京）科技有限公司</p>
<p>
<span>违法和不良信息举报电话：0755-86967540</span>
<span>邮箱：kefu@qiushibaike.com</span>
</p>
<br>
<p style="margin-top: 8px">&copy; Qiushibaike.com 糗事百科版权所有</p>
</div>
</div>


<div class="signin-box" id="login-form">
<div class="sigin-left">
<div class="signin-account clearfix">
<h4 class="social-signin-heading">社交帐号登录</h4>
<a rel="external nofollow" oauth_href href="https://open.weixin.qq.com/connect/qrconnect?appid=wx559af2d26b56c655&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fnew4%2Fsession%3Fsrc%3Dwx&response_type=code&scope=snsapi_login#wechat_redirect" class="social-btn social-wechat">
使用 微信 账号</a>
<a rel="external nofollow" oauth_href href="https://api.weibo.com/oauth2/authorize?client_id=63372306&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fnew4%2Fsession" class="social-btn social-weibo">
使用 微博 账号</a>
<a rel="external nofollow" oauth_href href="https://graph.qq.com/oauth2.0/authorize?which=Login&display=pc&client_id=100251437&response_type=code&redirect_uri=www.qiushibaike.com/new4/session?src=qq" class="social-btn social-qq">
使用 QQ 账号 </a>
</div>
<div class="signin-form clearfix">
<h4 class="social-signin-heading">糗事百科账号登录</h4>
<form method="post" action="/new4/session">
<input type="hidden" name="_xsrf" value="2|03a2505e|944ef69494747f26312cb3cbe0e250a8|1544577837"/>
<div class="signin-section clearfix">
<input type="text" class="form-input form-input-first" name="login" placeholder="昵称或邮箱">
<input type="password" class="form-input" name="password" placeholder="密码">
<input type="checkbox" id="remember_me" name="remember_me" checked="" value="checked" style="display:none">
</div>
<div class="signin-error" id="signin-error"></div>
<button type="submit" id="form-submit" class="form-submit">登录</button>
</form>
</div>
<div class="signin-foot clearfix">
<a rel="nofollow" href="/new4/fetchpass" class="fetch-password">忘记密码?</a>
</div>
</div>
</div>

<div class="float-nav">
<a class="float-nav-backtop" href="#" rel="nofollow">
<span class="float-nav-backtop-icon"></span>
</a>
</div>

<!--[if gte IE 6]>
<script type="text/javascript" src="//static.qiushibaike.com/js/src/web/json3.js?v=3a7f66a11a09842cd7555fad039657be"></script>
<![endif]-->
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/libs.min.js?v=bc8ddd36f0e7fed7c27f437c17f23ce0"></script>
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/app.min.js?v=5997ad16edca8ec50a1fcc40913785a6"></script>



<script type="text/javascript">
// Google Analytics
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-8780108-1', 'auto');
ga('send', 'pageview');
</script>

<script type="text/javascript" async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script type="text/javascript" src="https://cbjs.baidu.com/js/m.js"></script>
<script type="text/javascript">



window.broadJson = '[]'
</script>
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/v3/adsAdmin.min.js?v=9c42f35ae43e17caf141e9d6ebe32cbb"></script>
</body>
</html>

 """

pattern = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
results = re.findall(pattern, html_content)
for row in results:
    print(row)

pattern2 = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>', re.S)
results2 = re.findall(pattern2, html_content)
print(results2)


# 可能出现的问题：
# 1.pycharm一gbk方式编码.py文件。