



<!DOCTYPE html>
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
 <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" >
 
 <meta name="ROBOTS" content="NOARCHIVE">
 
 <link rel="icon" type="image/vnd.microsoft.icon" href="https://ssl.gstatic.com/codesite/ph/images/phosting.ico">
 
 
 <script type="text/javascript">
 
 
 
 
 var codesite_token = "RfCbSacEIWHqXSi63eO8BYZKC08:1375051174505";
 
 
 var CS_env = {"relativeBaseUrl":"","projectHomeUrl":"/p/ourproject-007","assetVersionPath":"https://ssl.gstatic.com/codesite/ph/3783617020303179221","profileUrl":"/u/105550342260037177437/","loggedInUserEmail":"isakebedeachs@gmail.com","assetHostPath":"https://ssl.gstatic.com/codesite/ph","projectName":"ourproject-007","domainName":null,"token":"RfCbSacEIWHqXSi63eO8BYZKC08:1375051174505"};
 var _gaq = _gaq || [];
 _gaq.push(
 ['siteTracker._setAccount', 'UA-18071-1'],
 ['siteTracker._trackPageview']);
 
 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
 })();
 
 </script>
 
 
 <title>strips_engine.py - 
 ourproject-007 -
 
 
 our project 007 - Google Project Hosting
 </title>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/3783617020303179221/css/core.css">
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/3783617020303179221/css/ph_detail.css" >
 
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/3783617020303179221/css/d_sb.css" >
 
 
 
<!--[if IE]>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/3783617020303179221/css/d_ie.css" >
<![endif]-->
 <style type="text/css">
 .menuIcon.off { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -42px }
 .menuIcon.on { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -28px }
 .menuIcon.down { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 0; }
 
 
 
  tr.inline_comment {
 background: #fff;
 vertical-align: top;
 }
 div.draft, div.published {
 padding: .3em;
 border: 1px solid #999; 
 margin-bottom: .1em;
 font-family: arial, sans-serif;
 max-width: 60em;
 }
 div.draft {
 background: #ffa;
 } 
 div.published {
 background: #e5ecf9;
 }
 div.published .body, div.draft .body {
 padding: .5em .1em .1em .1em;
 max-width: 60em;
 white-space: pre-wrap;
 white-space: -moz-pre-wrap;
 white-space: -pre-wrap;
 white-space: -o-pre-wrap;
 word-wrap: break-word;
 font-size: 1em;
 }
 div.draft .actions {
 margin-left: 1em;
 font-size: 90%;
 }
 div.draft form {
 padding: .5em .5em .5em 0;
 }
 div.draft textarea, div.published textarea {
 width: 95%;
 height: 10em;
 font-family: arial, sans-serif;
 margin-bottom: .5em;
 }

 
 .nocursor, .nocursor td, .cursor_hidden, .cursor_hidden td {
 background-color: white;
 height: 2px;
 }
 .cursor, .cursor td {
 background-color: darkblue;
 height: 2px;
 display: '';
 }
 
 
.list {
 border: 1px solid white;
 border-bottom: 0;
}

 
 </style>
</head>
<body class="t4">
<script type="text/javascript">
 window.___gcfg = {lang: 'en'};
 (function() 
 {var po = document.createElement("script");
 po.type = "text/javascript"; po.async = true;po.src = "https://apis.google.com/js/plusone.js";
 var s = document.getElementsByTagName("script")[0];
 s.parentNode.insertBefore(po, s);
 })();
</script>
<div class="headbg">

 <div id="gaia">
 

 <span>
 
 
 
 <a href="#" id="multilogin-dropdown" onclick="return false;"
 ><u><b>isakebedeachs@gmail.com</b></u> <small>&#9660;</small></a>
 
 
 | <a href="/u/105550342260037177437/" id="projects-dropdown" onclick="return false;"
 ><u>My favorites</u> <small>&#9660;</small></a>
 | <a href="/u/105550342260037177437/" onclick="_CS_click('/gb/ph/profile');"
 title="Profile, Updates, and Settings"
 ><u>Profile</u></a>
 | <a href="https://www.google.com/accounts/Logout?continue=https%3A%2F%2Fcode.google.com%2Fp%2Fourproject-007%2Fsource%2Fbrowse%2Ftrunk%2Fpart1%2Fstrips_engine.py" 
 onclick="_CS_click('/gb/ph/signout');"
 ><u>Sign out</u></a>
 
 </span>

 </div>

 <div class="gbh" style="left: 0pt;"></div>
 <div class="gbh" style="right: 0pt;"></div>
 
 
 <div style="height: 1px"></div>
<!--[if lte IE 7]>
<div style="text-align:center;">
Your version of Internet Explorer is not supported. Try a browser that
contributes to open source, such as <a href="http://www.firefox.com">Firefox</a>,
<a href="http://www.google.com/chrome">Google Chrome</a>, or
<a href="http://code.google.com/chrome/chromeframe/">Google Chrome Frame</a>.
</div>
<![endif]-->



 <table style="padding:0px; margin: 0px 0px 10px 0px; width:100%" cellpadding="0" cellspacing="0"
 itemscope itemtype="http://schema.org/CreativeWork">
 <tr style="height: 58px;">
 
 
 
 <td id="plogo">
 <link itemprop="url" href="/p/ourproject-007">
 <a href="/p/ourproject-007/">
 
 <img src="https://ssl.gstatic.com/codesite/ph/images/defaultlogo.png" alt="Logo" itemprop="image">
 
 </a>
 </td>
 
 <td style="padding-left: 0.5em">
 
 <div id="pname">
 <a href="/p/ourproject-007/"><span itemprop="name">ourproject-007</span></a>
 </div>
 
 <div id="psum">
 <a id="project_summary_link"
 href="/p/ourproject-007/"><span itemprop="description">our project 007</span></a>
 
 </div>
 
 
 </td>
 <td style="white-space:nowrap;text-align:right; vertical-align:bottom;">
 
 <form action="/hosting/search">
 <input size="30" name="q" value="" type="text">
 
 <input type="submit" name="projectsearch" value="Search projects" >
 </form>
 
 </tr>
 </table>

</div>

 
<div id="mt" class="gtb"> 
 <a href="/p/ourproject-007/" class="tab ">Project&nbsp;Home</a>
 
 
 
 
 
 
 <a href="/p/ourproject-007/w/list" class="tab ">Wiki</a>
 
 
 
 
 
 <a href="/p/ourproject-007/issues/list"
 class="tab ">Issues</a>
 
 
 
 
 
 <a href="/p/ourproject-007/source/checkout"
 class="tab active">Source</a>
 
 
 
 
 
 
 
 
 <div class=gtbc></div>
</div>
<table cellspacing="0" cellpadding="0" width="100%" align="center" border="0" class="st">
 <tr>
 
 
 
 
 
 
 <td class="subt">
 <div class="st2">
 <div class="isf">
 
 


 <span class="inst1"><a href="/p/ourproject-007/source/checkout">Checkout</a></span> &nbsp;
 <span class="inst2"><a href="/p/ourproject-007/source/browse/">Browse</a></span> &nbsp;
 <span class="inst3"><a href="/p/ourproject-007/source/list">Changes</a></span> &nbsp;
 
 
 
 
 
 <a href="/p/ourproject-007/issues/entry?show=review&former=sourcelist">Request code review</a>
 
 
 
 </form>
 <script type="text/javascript">
 
 function codesearchQuery(form) {
 var query = document.getElementById('q').value;
 if (query) { form.action += '%20' + query; }
 }
 </script>
 </div>
</div>

 </td>
 
 
 
 <td align="right" valign="top" class="bevel-right"></td>
 </tr>
</table>


<script type="text/javascript">
 var cancelBubble = false;
 function _go(url) { document.location = url; }
</script>
<div id="maincol"
 
>

 




<div class="expand">
<div id="colcontrol">
<style type="text/css">
 #file_flipper { white-space: nowrap; padding-right: 2em; }
 #file_flipper.hidden { display: none; }
 #file_flipper .pagelink { color: #0000CC; text-decoration: underline; }
 #file_flipper #visiblefiles { padding-left: 0.5em; padding-right: 0.5em; }
</style>
<table id="nav_and_rev" class="list"
 cellpadding="0" cellspacing="0" width="100%">
 <tr>
 
 <td nowrap="nowrap" class="src_crumbs src_nav" width="33%">
 <strong class="src_nav">Source path:&nbsp;</strong>
 <span id="crumb_root">
 
 <a href="/p/ourproject-007/source/browse/">svn</a>/&nbsp;</span>
 <span id="crumb_links" class="ifClosed"><a href="/p/ourproject-007/source/browse/trunk/">trunk</a><span class="sp">/&nbsp;</span><a href="/p/ourproject-007/source/browse/trunk/part1/">part1</a><span class="sp">/&nbsp;</span>strips_engine.py</span>
 
 


 </td>
 
 
 <td nowrap="nowrap" width="33%" align="center">
 <a href="/p/ourproject-007/source/browse/trunk/part1/strips_engine.py?edit=1"
 ><img src="https://ssl.gstatic.com/codesite/ph/images/pencil-y14.png"
 class="edit_icon">Edit file</a>
 </td>
 
 
 <td nowrap="nowrap" width="33%" align="right">
 <table cellpadding="0" cellspacing="0" style="font-size: 100%"><tr>
 
 
 <td class="flipper"><b>r70</b></td>
 
 </tr></table>
 </td> 
 </tr>
</table>

<div class="fc">
 
 
 
<style type="text/css">
.undermouse span {
 background-image: url(https://ssl.gstatic.com/codesite/ph/images/comments.gif); }
</style>
<table class="opened" id="review_comment_area"
onmouseout="gutterOut()"><tr>
<td id="nums">
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
<pre><table width="100%" id="nums_table_0"><tr id="gr_svn70_1"

 onmouseover="gutterOver(1)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',1);">&nbsp;</span
></td><td id="1"><a href="#1">1</a></td></tr
><tr id="gr_svn70_2"

 onmouseover="gutterOver(2)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',2);">&nbsp;</span
></td><td id="2"><a href="#2">2</a></td></tr
><tr id="gr_svn70_3"

 onmouseover="gutterOver(3)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',3);">&nbsp;</span
></td><td id="3"><a href="#3">3</a></td></tr
><tr id="gr_svn70_4"

 onmouseover="gutterOver(4)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',4);">&nbsp;</span
></td><td id="4"><a href="#4">4</a></td></tr
><tr id="gr_svn70_5"

 onmouseover="gutterOver(5)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',5);">&nbsp;</span
></td><td id="5"><a href="#5">5</a></td></tr
><tr id="gr_svn70_6"

 onmouseover="gutterOver(6)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',6);">&nbsp;</span
></td><td id="6"><a href="#6">6</a></td></tr
><tr id="gr_svn70_7"

 onmouseover="gutterOver(7)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',7);">&nbsp;</span
></td><td id="7"><a href="#7">7</a></td></tr
><tr id="gr_svn70_8"

 onmouseover="gutterOver(8)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',8);">&nbsp;</span
></td><td id="8"><a href="#8">8</a></td></tr
><tr id="gr_svn70_9"

 onmouseover="gutterOver(9)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',9);">&nbsp;</span
></td><td id="9"><a href="#9">9</a></td></tr
><tr id="gr_svn70_10"

 onmouseover="gutterOver(10)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',10);">&nbsp;</span
></td><td id="10"><a href="#10">10</a></td></tr
><tr id="gr_svn70_11"

 onmouseover="gutterOver(11)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',11);">&nbsp;</span
></td><td id="11"><a href="#11">11</a></td></tr
><tr id="gr_svn70_12"

 onmouseover="gutterOver(12)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',12);">&nbsp;</span
></td><td id="12"><a href="#12">12</a></td></tr
><tr id="gr_svn70_13"

 onmouseover="gutterOver(13)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',13);">&nbsp;</span
></td><td id="13"><a href="#13">13</a></td></tr
><tr id="gr_svn70_14"

 onmouseover="gutterOver(14)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',14);">&nbsp;</span
></td><td id="14"><a href="#14">14</a></td></tr
><tr id="gr_svn70_15"

 onmouseover="gutterOver(15)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',15);">&nbsp;</span
></td><td id="15"><a href="#15">15</a></td></tr
><tr id="gr_svn70_16"

 onmouseover="gutterOver(16)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',16);">&nbsp;</span
></td><td id="16"><a href="#16">16</a></td></tr
><tr id="gr_svn70_17"

 onmouseover="gutterOver(17)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',17);">&nbsp;</span
></td><td id="17"><a href="#17">17</a></td></tr
><tr id="gr_svn70_18"

 onmouseover="gutterOver(18)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',18);">&nbsp;</span
></td><td id="18"><a href="#18">18</a></td></tr
><tr id="gr_svn70_19"

 onmouseover="gutterOver(19)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',19);">&nbsp;</span
></td><td id="19"><a href="#19">19</a></td></tr
><tr id="gr_svn70_20"

 onmouseover="gutterOver(20)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',20);">&nbsp;</span
></td><td id="20"><a href="#20">20</a></td></tr
><tr id="gr_svn70_21"

 onmouseover="gutterOver(21)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',21);">&nbsp;</span
></td><td id="21"><a href="#21">21</a></td></tr
><tr id="gr_svn70_22"

 onmouseover="gutterOver(22)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',22);">&nbsp;</span
></td><td id="22"><a href="#22">22</a></td></tr
><tr id="gr_svn70_23"

 onmouseover="gutterOver(23)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',23);">&nbsp;</span
></td><td id="23"><a href="#23">23</a></td></tr
><tr id="gr_svn70_24"

 onmouseover="gutterOver(24)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',24);">&nbsp;</span
></td><td id="24"><a href="#24">24</a></td></tr
><tr id="gr_svn70_25"

 onmouseover="gutterOver(25)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',25);">&nbsp;</span
></td><td id="25"><a href="#25">25</a></td></tr
><tr id="gr_svn70_26"

 onmouseover="gutterOver(26)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',26);">&nbsp;</span
></td><td id="26"><a href="#26">26</a></td></tr
><tr id="gr_svn70_27"

 onmouseover="gutterOver(27)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',27);">&nbsp;</span
></td><td id="27"><a href="#27">27</a></td></tr
><tr id="gr_svn70_28"

 onmouseover="gutterOver(28)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',28);">&nbsp;</span
></td><td id="28"><a href="#28">28</a></td></tr
><tr id="gr_svn70_29"

 onmouseover="gutterOver(29)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',29);">&nbsp;</span
></td><td id="29"><a href="#29">29</a></td></tr
><tr id="gr_svn70_30"

 onmouseover="gutterOver(30)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',30);">&nbsp;</span
></td><td id="30"><a href="#30">30</a></td></tr
><tr id="gr_svn70_31"

 onmouseover="gutterOver(31)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',31);">&nbsp;</span
></td><td id="31"><a href="#31">31</a></td></tr
><tr id="gr_svn70_32"

 onmouseover="gutterOver(32)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',32);">&nbsp;</span
></td><td id="32"><a href="#32">32</a></td></tr
><tr id="gr_svn70_33"

 onmouseover="gutterOver(33)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',33);">&nbsp;</span
></td><td id="33"><a href="#33">33</a></td></tr
><tr id="gr_svn70_34"

 onmouseover="gutterOver(34)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',34);">&nbsp;</span
></td><td id="34"><a href="#34">34</a></td></tr
><tr id="gr_svn70_35"

 onmouseover="gutterOver(35)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',35);">&nbsp;</span
></td><td id="35"><a href="#35">35</a></td></tr
><tr id="gr_svn70_36"

 onmouseover="gutterOver(36)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',36);">&nbsp;</span
></td><td id="36"><a href="#36">36</a></td></tr
><tr id="gr_svn70_37"

 onmouseover="gutterOver(37)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',37);">&nbsp;</span
></td><td id="37"><a href="#37">37</a></td></tr
><tr id="gr_svn70_38"

 onmouseover="gutterOver(38)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',38);">&nbsp;</span
></td><td id="38"><a href="#38">38</a></td></tr
><tr id="gr_svn70_39"

 onmouseover="gutterOver(39)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',39);">&nbsp;</span
></td><td id="39"><a href="#39">39</a></td></tr
><tr id="gr_svn70_40"

 onmouseover="gutterOver(40)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',40);">&nbsp;</span
></td><td id="40"><a href="#40">40</a></td></tr
><tr id="gr_svn70_41"

 onmouseover="gutterOver(41)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',41);">&nbsp;</span
></td><td id="41"><a href="#41">41</a></td></tr
><tr id="gr_svn70_42"

 onmouseover="gutterOver(42)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',42);">&nbsp;</span
></td><td id="42"><a href="#42">42</a></td></tr
><tr id="gr_svn70_43"

 onmouseover="gutterOver(43)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',43);">&nbsp;</span
></td><td id="43"><a href="#43">43</a></td></tr
><tr id="gr_svn70_44"

 onmouseover="gutterOver(44)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',44);">&nbsp;</span
></td><td id="44"><a href="#44">44</a></td></tr
><tr id="gr_svn70_45"

 onmouseover="gutterOver(45)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',45);">&nbsp;</span
></td><td id="45"><a href="#45">45</a></td></tr
><tr id="gr_svn70_46"

 onmouseover="gutterOver(46)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',46);">&nbsp;</span
></td><td id="46"><a href="#46">46</a></td></tr
><tr id="gr_svn70_47"

 onmouseover="gutterOver(47)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',47);">&nbsp;</span
></td><td id="47"><a href="#47">47</a></td></tr
><tr id="gr_svn70_48"

 onmouseover="gutterOver(48)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',48);">&nbsp;</span
></td><td id="48"><a href="#48">48</a></td></tr
><tr id="gr_svn70_49"

 onmouseover="gutterOver(49)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',49);">&nbsp;</span
></td><td id="49"><a href="#49">49</a></td></tr
><tr id="gr_svn70_50"

 onmouseover="gutterOver(50)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',50);">&nbsp;</span
></td><td id="50"><a href="#50">50</a></td></tr
><tr id="gr_svn70_51"

 onmouseover="gutterOver(51)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',51);">&nbsp;</span
></td><td id="51"><a href="#51">51</a></td></tr
><tr id="gr_svn70_52"

 onmouseover="gutterOver(52)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',52);">&nbsp;</span
></td><td id="52"><a href="#52">52</a></td></tr
><tr id="gr_svn70_53"

 onmouseover="gutterOver(53)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',53);">&nbsp;</span
></td><td id="53"><a href="#53">53</a></td></tr
><tr id="gr_svn70_54"

 onmouseover="gutterOver(54)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',54);">&nbsp;</span
></td><td id="54"><a href="#54">54</a></td></tr
><tr id="gr_svn70_55"

 onmouseover="gutterOver(55)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',55);">&nbsp;</span
></td><td id="55"><a href="#55">55</a></td></tr
><tr id="gr_svn70_56"

 onmouseover="gutterOver(56)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',56);">&nbsp;</span
></td><td id="56"><a href="#56">56</a></td></tr
><tr id="gr_svn70_57"

 onmouseover="gutterOver(57)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',57);">&nbsp;</span
></td><td id="57"><a href="#57">57</a></td></tr
><tr id="gr_svn70_58"

 onmouseover="gutterOver(58)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',58);">&nbsp;</span
></td><td id="58"><a href="#58">58</a></td></tr
><tr id="gr_svn70_59"

 onmouseover="gutterOver(59)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',59);">&nbsp;</span
></td><td id="59"><a href="#59">59</a></td></tr
><tr id="gr_svn70_60"

 onmouseover="gutterOver(60)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',60);">&nbsp;</span
></td><td id="60"><a href="#60">60</a></td></tr
><tr id="gr_svn70_61"

 onmouseover="gutterOver(61)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',61);">&nbsp;</span
></td><td id="61"><a href="#61">61</a></td></tr
><tr id="gr_svn70_62"

 onmouseover="gutterOver(62)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',62);">&nbsp;</span
></td><td id="62"><a href="#62">62</a></td></tr
><tr id="gr_svn70_63"

 onmouseover="gutterOver(63)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',63);">&nbsp;</span
></td><td id="63"><a href="#63">63</a></td></tr
><tr id="gr_svn70_64"

 onmouseover="gutterOver(64)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',64);">&nbsp;</span
></td><td id="64"><a href="#64">64</a></td></tr
><tr id="gr_svn70_65"

 onmouseover="gutterOver(65)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',65);">&nbsp;</span
></td><td id="65"><a href="#65">65</a></td></tr
><tr id="gr_svn70_66"

 onmouseover="gutterOver(66)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',66);">&nbsp;</span
></td><td id="66"><a href="#66">66</a></td></tr
><tr id="gr_svn70_67"

 onmouseover="gutterOver(67)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',67);">&nbsp;</span
></td><td id="67"><a href="#67">67</a></td></tr
><tr id="gr_svn70_68"

 onmouseover="gutterOver(68)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',68);">&nbsp;</span
></td><td id="68"><a href="#68">68</a></td></tr
><tr id="gr_svn70_69"

 onmouseover="gutterOver(69)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',69);">&nbsp;</span
></td><td id="69"><a href="#69">69</a></td></tr
><tr id="gr_svn70_70"

 onmouseover="gutterOver(70)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',70);">&nbsp;</span
></td><td id="70"><a href="#70">70</a></td></tr
><tr id="gr_svn70_71"

 onmouseover="gutterOver(71)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',71);">&nbsp;</span
></td><td id="71"><a href="#71">71</a></td></tr
><tr id="gr_svn70_72"

 onmouseover="gutterOver(72)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',72);">&nbsp;</span
></td><td id="72"><a href="#72">72</a></td></tr
><tr id="gr_svn70_73"

 onmouseover="gutterOver(73)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',73);">&nbsp;</span
></td><td id="73"><a href="#73">73</a></td></tr
><tr id="gr_svn70_74"

 onmouseover="gutterOver(74)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',74);">&nbsp;</span
></td><td id="74"><a href="#74">74</a></td></tr
><tr id="gr_svn70_75"

 onmouseover="gutterOver(75)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',75);">&nbsp;</span
></td><td id="75"><a href="#75">75</a></td></tr
><tr id="gr_svn70_76"

 onmouseover="gutterOver(76)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',76);">&nbsp;</span
></td><td id="76"><a href="#76">76</a></td></tr
><tr id="gr_svn70_77"

 onmouseover="gutterOver(77)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',77);">&nbsp;</span
></td><td id="77"><a href="#77">77</a></td></tr
><tr id="gr_svn70_78"

 onmouseover="gutterOver(78)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',78);">&nbsp;</span
></td><td id="78"><a href="#78">78</a></td></tr
><tr id="gr_svn70_79"

 onmouseover="gutterOver(79)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',79);">&nbsp;</span
></td><td id="79"><a href="#79">79</a></td></tr
><tr id="gr_svn70_80"

 onmouseover="gutterOver(80)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',80);">&nbsp;</span
></td><td id="80"><a href="#80">80</a></td></tr
><tr id="gr_svn70_81"

 onmouseover="gutterOver(81)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',81);">&nbsp;</span
></td><td id="81"><a href="#81">81</a></td></tr
><tr id="gr_svn70_82"

 onmouseover="gutterOver(82)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',82);">&nbsp;</span
></td><td id="82"><a href="#82">82</a></td></tr
><tr id="gr_svn70_83"

 onmouseover="gutterOver(83)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',83);">&nbsp;</span
></td><td id="83"><a href="#83">83</a></td></tr
><tr id="gr_svn70_84"

 onmouseover="gutterOver(84)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',84);">&nbsp;</span
></td><td id="84"><a href="#84">84</a></td></tr
><tr id="gr_svn70_85"

 onmouseover="gutterOver(85)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',85);">&nbsp;</span
></td><td id="85"><a href="#85">85</a></td></tr
><tr id="gr_svn70_86"

 onmouseover="gutterOver(86)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',86);">&nbsp;</span
></td><td id="86"><a href="#86">86</a></td></tr
><tr id="gr_svn70_87"

 onmouseover="gutterOver(87)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',87);">&nbsp;</span
></td><td id="87"><a href="#87">87</a></td></tr
><tr id="gr_svn70_88"

 onmouseover="gutterOver(88)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',88);">&nbsp;</span
></td><td id="88"><a href="#88">88</a></td></tr
><tr id="gr_svn70_89"

 onmouseover="gutterOver(89)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',89);">&nbsp;</span
></td><td id="89"><a href="#89">89</a></td></tr
><tr id="gr_svn70_90"

 onmouseover="gutterOver(90)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',90);">&nbsp;</span
></td><td id="90"><a href="#90">90</a></td></tr
><tr id="gr_svn70_91"

 onmouseover="gutterOver(91)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',91);">&nbsp;</span
></td><td id="91"><a href="#91">91</a></td></tr
><tr id="gr_svn70_92"

 onmouseover="gutterOver(92)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',92);">&nbsp;</span
></td><td id="92"><a href="#92">92</a></td></tr
><tr id="gr_svn70_93"

 onmouseover="gutterOver(93)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',93);">&nbsp;</span
></td><td id="93"><a href="#93">93</a></td></tr
><tr id="gr_svn70_94"

 onmouseover="gutterOver(94)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',94);">&nbsp;</span
></td><td id="94"><a href="#94">94</a></td></tr
><tr id="gr_svn70_95"

 onmouseover="gutterOver(95)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',95);">&nbsp;</span
></td><td id="95"><a href="#95">95</a></td></tr
><tr id="gr_svn70_96"

 onmouseover="gutterOver(96)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',96);">&nbsp;</span
></td><td id="96"><a href="#96">96</a></td></tr
><tr id="gr_svn70_97"

 onmouseover="gutterOver(97)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',97);">&nbsp;</span
></td><td id="97"><a href="#97">97</a></td></tr
><tr id="gr_svn70_98"

 onmouseover="gutterOver(98)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',98);">&nbsp;</span
></td><td id="98"><a href="#98">98</a></td></tr
><tr id="gr_svn70_99"

 onmouseover="gutterOver(99)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',99);">&nbsp;</span
></td><td id="99"><a href="#99">99</a></td></tr
><tr id="gr_svn70_100"

 onmouseover="gutterOver(100)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',100);">&nbsp;</span
></td><td id="100"><a href="#100">100</a></td></tr
><tr id="gr_svn70_101"

 onmouseover="gutterOver(101)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',101);">&nbsp;</span
></td><td id="101"><a href="#101">101</a></td></tr
><tr id="gr_svn70_102"

 onmouseover="gutterOver(102)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',102);">&nbsp;</span
></td><td id="102"><a href="#102">102</a></td></tr
><tr id="gr_svn70_103"

 onmouseover="gutterOver(103)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',103);">&nbsp;</span
></td><td id="103"><a href="#103">103</a></td></tr
><tr id="gr_svn70_104"

 onmouseover="gutterOver(104)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',104);">&nbsp;</span
></td><td id="104"><a href="#104">104</a></td></tr
><tr id="gr_svn70_105"

 onmouseover="gutterOver(105)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',105);">&nbsp;</span
></td><td id="105"><a href="#105">105</a></td></tr
><tr id="gr_svn70_106"

 onmouseover="gutterOver(106)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',106);">&nbsp;</span
></td><td id="106"><a href="#106">106</a></td></tr
><tr id="gr_svn70_107"

 onmouseover="gutterOver(107)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',107);">&nbsp;</span
></td><td id="107"><a href="#107">107</a></td></tr
><tr id="gr_svn70_108"

 onmouseover="gutterOver(108)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',108);">&nbsp;</span
></td><td id="108"><a href="#108">108</a></td></tr
><tr id="gr_svn70_109"

 onmouseover="gutterOver(109)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',109);">&nbsp;</span
></td><td id="109"><a href="#109">109</a></td></tr
><tr id="gr_svn70_110"

 onmouseover="gutterOver(110)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',110);">&nbsp;</span
></td><td id="110"><a href="#110">110</a></td></tr
><tr id="gr_svn70_111"

 onmouseover="gutterOver(111)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',111);">&nbsp;</span
></td><td id="111"><a href="#111">111</a></td></tr
><tr id="gr_svn70_112"

 onmouseover="gutterOver(112)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',112);">&nbsp;</span
></td><td id="112"><a href="#112">112</a></td></tr
><tr id="gr_svn70_113"

 onmouseover="gutterOver(113)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',113);">&nbsp;</span
></td><td id="113"><a href="#113">113</a></td></tr
><tr id="gr_svn70_114"

 onmouseover="gutterOver(114)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',114);">&nbsp;</span
></td><td id="114"><a href="#114">114</a></td></tr
><tr id="gr_svn70_115"

 onmouseover="gutterOver(115)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',115);">&nbsp;</span
></td><td id="115"><a href="#115">115</a></td></tr
><tr id="gr_svn70_116"

 onmouseover="gutterOver(116)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',116);">&nbsp;</span
></td><td id="116"><a href="#116">116</a></td></tr
><tr id="gr_svn70_117"

 onmouseover="gutterOver(117)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',117);">&nbsp;</span
></td><td id="117"><a href="#117">117</a></td></tr
><tr id="gr_svn70_118"

 onmouseover="gutterOver(118)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',118);">&nbsp;</span
></td><td id="118"><a href="#118">118</a></td></tr
><tr id="gr_svn70_119"

 onmouseover="gutterOver(119)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',119);">&nbsp;</span
></td><td id="119"><a href="#119">119</a></td></tr
><tr id="gr_svn70_120"

 onmouseover="gutterOver(120)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',120);">&nbsp;</span
></td><td id="120"><a href="#120">120</a></td></tr
><tr id="gr_svn70_121"

 onmouseover="gutterOver(121)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',121);">&nbsp;</span
></td><td id="121"><a href="#121">121</a></td></tr
><tr id="gr_svn70_122"

 onmouseover="gutterOver(122)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',122);">&nbsp;</span
></td><td id="122"><a href="#122">122</a></td></tr
><tr id="gr_svn70_123"

 onmouseover="gutterOver(123)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',123);">&nbsp;</span
></td><td id="123"><a href="#123">123</a></td></tr
><tr id="gr_svn70_124"

 onmouseover="gutterOver(124)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',124);">&nbsp;</span
></td><td id="124"><a href="#124">124</a></td></tr
><tr id="gr_svn70_125"

 onmouseover="gutterOver(125)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',125);">&nbsp;</span
></td><td id="125"><a href="#125">125</a></td></tr
><tr id="gr_svn70_126"

 onmouseover="gutterOver(126)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',126);">&nbsp;</span
></td><td id="126"><a href="#126">126</a></td></tr
><tr id="gr_svn70_127"

 onmouseover="gutterOver(127)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',127);">&nbsp;</span
></td><td id="127"><a href="#127">127</a></td></tr
><tr id="gr_svn70_128"

 onmouseover="gutterOver(128)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',128);">&nbsp;</span
></td><td id="128"><a href="#128">128</a></td></tr
><tr id="gr_svn70_129"

 onmouseover="gutterOver(129)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',129);">&nbsp;</span
></td><td id="129"><a href="#129">129</a></td></tr
><tr id="gr_svn70_130"

 onmouseover="gutterOver(130)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',130);">&nbsp;</span
></td><td id="130"><a href="#130">130</a></td></tr
><tr id="gr_svn70_131"

 onmouseover="gutterOver(131)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',131);">&nbsp;</span
></td><td id="131"><a href="#131">131</a></td></tr
><tr id="gr_svn70_132"

 onmouseover="gutterOver(132)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',132);">&nbsp;</span
></td><td id="132"><a href="#132">132</a></td></tr
><tr id="gr_svn70_133"

 onmouseover="gutterOver(133)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',133);">&nbsp;</span
></td><td id="133"><a href="#133">133</a></td></tr
><tr id="gr_svn70_134"

 onmouseover="gutterOver(134)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',134);">&nbsp;</span
></td><td id="134"><a href="#134">134</a></td></tr
><tr id="gr_svn70_135"

 onmouseover="gutterOver(135)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',135);">&nbsp;</span
></td><td id="135"><a href="#135">135</a></td></tr
><tr id="gr_svn70_136"

 onmouseover="gutterOver(136)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',136);">&nbsp;</span
></td><td id="136"><a href="#136">136</a></td></tr
><tr id="gr_svn70_137"

 onmouseover="gutterOver(137)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',137);">&nbsp;</span
></td><td id="137"><a href="#137">137</a></td></tr
><tr id="gr_svn70_138"

 onmouseover="gutterOver(138)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',138);">&nbsp;</span
></td><td id="138"><a href="#138">138</a></td></tr
><tr id="gr_svn70_139"

 onmouseover="gutterOver(139)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',139);">&nbsp;</span
></td><td id="139"><a href="#139">139</a></td></tr
><tr id="gr_svn70_140"

 onmouseover="gutterOver(140)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',140);">&nbsp;</span
></td><td id="140"><a href="#140">140</a></td></tr
><tr id="gr_svn70_141"

 onmouseover="gutterOver(141)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',141);">&nbsp;</span
></td><td id="141"><a href="#141">141</a></td></tr
><tr id="gr_svn70_142"

 onmouseover="gutterOver(142)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',142);">&nbsp;</span
></td><td id="142"><a href="#142">142</a></td></tr
><tr id="gr_svn70_143"

 onmouseover="gutterOver(143)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',143);">&nbsp;</span
></td><td id="143"><a href="#143">143</a></td></tr
><tr id="gr_svn70_144"

 onmouseover="gutterOver(144)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',144);">&nbsp;</span
></td><td id="144"><a href="#144">144</a></td></tr
><tr id="gr_svn70_145"

 onmouseover="gutterOver(145)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',145);">&nbsp;</span
></td><td id="145"><a href="#145">145</a></td></tr
><tr id="gr_svn70_146"

 onmouseover="gutterOver(146)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',146);">&nbsp;</span
></td><td id="146"><a href="#146">146</a></td></tr
><tr id="gr_svn70_147"

 onmouseover="gutterOver(147)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',147);">&nbsp;</span
></td><td id="147"><a href="#147">147</a></td></tr
><tr id="gr_svn70_148"

 onmouseover="gutterOver(148)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',148);">&nbsp;</span
></td><td id="148"><a href="#148">148</a></td></tr
><tr id="gr_svn70_149"

 onmouseover="gutterOver(149)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',149);">&nbsp;</span
></td><td id="149"><a href="#149">149</a></td></tr
><tr id="gr_svn70_150"

 onmouseover="gutterOver(150)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',150);">&nbsp;</span
></td><td id="150"><a href="#150">150</a></td></tr
><tr id="gr_svn70_151"

 onmouseover="gutterOver(151)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',151);">&nbsp;</span
></td><td id="151"><a href="#151">151</a></td></tr
><tr id="gr_svn70_152"

 onmouseover="gutterOver(152)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',152);">&nbsp;</span
></td><td id="152"><a href="#152">152</a></td></tr
><tr id="gr_svn70_153"

 onmouseover="gutterOver(153)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',153);">&nbsp;</span
></td><td id="153"><a href="#153">153</a></td></tr
><tr id="gr_svn70_154"

 onmouseover="gutterOver(154)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',154);">&nbsp;</span
></td><td id="154"><a href="#154">154</a></td></tr
><tr id="gr_svn70_155"

 onmouseover="gutterOver(155)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',155);">&nbsp;</span
></td><td id="155"><a href="#155">155</a></td></tr
><tr id="gr_svn70_156"

 onmouseover="gutterOver(156)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',156);">&nbsp;</span
></td><td id="156"><a href="#156">156</a></td></tr
><tr id="gr_svn70_157"

 onmouseover="gutterOver(157)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',157);">&nbsp;</span
></td><td id="157"><a href="#157">157</a></td></tr
><tr id="gr_svn70_158"

 onmouseover="gutterOver(158)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',158);">&nbsp;</span
></td><td id="158"><a href="#158">158</a></td></tr
><tr id="gr_svn70_159"

 onmouseover="gutterOver(159)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',159);">&nbsp;</span
></td><td id="159"><a href="#159">159</a></td></tr
><tr id="gr_svn70_160"

 onmouseover="gutterOver(160)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',160);">&nbsp;</span
></td><td id="160"><a href="#160">160</a></td></tr
><tr id="gr_svn70_161"

 onmouseover="gutterOver(161)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',161);">&nbsp;</span
></td><td id="161"><a href="#161">161</a></td></tr
><tr id="gr_svn70_162"

 onmouseover="gutterOver(162)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',162);">&nbsp;</span
></td><td id="162"><a href="#162">162</a></td></tr
><tr id="gr_svn70_163"

 onmouseover="gutterOver(163)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',163);">&nbsp;</span
></td><td id="163"><a href="#163">163</a></td></tr
><tr id="gr_svn70_164"

 onmouseover="gutterOver(164)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',164);">&nbsp;</span
></td><td id="164"><a href="#164">164</a></td></tr
><tr id="gr_svn70_165"

 onmouseover="gutterOver(165)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',165);">&nbsp;</span
></td><td id="165"><a href="#165">165</a></td></tr
><tr id="gr_svn70_166"

 onmouseover="gutterOver(166)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',166);">&nbsp;</span
></td><td id="166"><a href="#166">166</a></td></tr
><tr id="gr_svn70_167"

 onmouseover="gutterOver(167)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',167);">&nbsp;</span
></td><td id="167"><a href="#167">167</a></td></tr
><tr id="gr_svn70_168"

 onmouseover="gutterOver(168)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',168);">&nbsp;</span
></td><td id="168"><a href="#168">168</a></td></tr
><tr id="gr_svn70_169"

 onmouseover="gutterOver(169)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',169);">&nbsp;</span
></td><td id="169"><a href="#169">169</a></td></tr
><tr id="gr_svn70_170"

 onmouseover="gutterOver(170)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',170);">&nbsp;</span
></td><td id="170"><a href="#170">170</a></td></tr
><tr id="gr_svn70_171"

 onmouseover="gutterOver(171)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',171);">&nbsp;</span
></td><td id="171"><a href="#171">171</a></td></tr
><tr id="gr_svn70_172"

 onmouseover="gutterOver(172)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',172);">&nbsp;</span
></td><td id="172"><a href="#172">172</a></td></tr
><tr id="gr_svn70_173"

 onmouseover="gutterOver(173)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',173);">&nbsp;</span
></td><td id="173"><a href="#173">173</a></td></tr
><tr id="gr_svn70_174"

 onmouseover="gutterOver(174)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',174);">&nbsp;</span
></td><td id="174"><a href="#174">174</a></td></tr
><tr id="gr_svn70_175"

 onmouseover="gutterOver(175)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',175);">&nbsp;</span
></td><td id="175"><a href="#175">175</a></td></tr
><tr id="gr_svn70_176"

 onmouseover="gutterOver(176)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',176);">&nbsp;</span
></td><td id="176"><a href="#176">176</a></td></tr
><tr id="gr_svn70_177"

 onmouseover="gutterOver(177)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',177);">&nbsp;</span
></td><td id="177"><a href="#177">177</a></td></tr
><tr id="gr_svn70_178"

 onmouseover="gutterOver(178)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',178);">&nbsp;</span
></td><td id="178"><a href="#178">178</a></td></tr
><tr id="gr_svn70_179"

 onmouseover="gutterOver(179)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',179);">&nbsp;</span
></td><td id="179"><a href="#179">179</a></td></tr
><tr id="gr_svn70_180"

 onmouseover="gutterOver(180)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',180);">&nbsp;</span
></td><td id="180"><a href="#180">180</a></td></tr
><tr id="gr_svn70_181"

 onmouseover="gutterOver(181)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',181);">&nbsp;</span
></td><td id="181"><a href="#181">181</a></td></tr
><tr id="gr_svn70_182"

 onmouseover="gutterOver(182)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',182);">&nbsp;</span
></td><td id="182"><a href="#182">182</a></td></tr
><tr id="gr_svn70_183"

 onmouseover="gutterOver(183)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',183);">&nbsp;</span
></td><td id="183"><a href="#183">183</a></td></tr
><tr id="gr_svn70_184"

 onmouseover="gutterOver(184)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',184);">&nbsp;</span
></td><td id="184"><a href="#184">184</a></td></tr
><tr id="gr_svn70_185"

 onmouseover="gutterOver(185)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',185);">&nbsp;</span
></td><td id="185"><a href="#185">185</a></td></tr
><tr id="gr_svn70_186"

 onmouseover="gutterOver(186)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',186);">&nbsp;</span
></td><td id="186"><a href="#186">186</a></td></tr
><tr id="gr_svn70_187"

 onmouseover="gutterOver(187)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',187);">&nbsp;</span
></td><td id="187"><a href="#187">187</a></td></tr
><tr id="gr_svn70_188"

 onmouseover="gutterOver(188)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',188);">&nbsp;</span
></td><td id="188"><a href="#188">188</a></td></tr
><tr id="gr_svn70_189"

 onmouseover="gutterOver(189)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',189);">&nbsp;</span
></td><td id="189"><a href="#189">189</a></td></tr
><tr id="gr_svn70_190"

 onmouseover="gutterOver(190)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',190);">&nbsp;</span
></td><td id="190"><a href="#190">190</a></td></tr
><tr id="gr_svn70_191"

 onmouseover="gutterOver(191)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',191);">&nbsp;</span
></td><td id="191"><a href="#191">191</a></td></tr
><tr id="gr_svn70_192"

 onmouseover="gutterOver(192)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',192);">&nbsp;</span
></td><td id="192"><a href="#192">192</a></td></tr
><tr id="gr_svn70_193"

 onmouseover="gutterOver(193)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',193);">&nbsp;</span
></td><td id="193"><a href="#193">193</a></td></tr
><tr id="gr_svn70_194"

 onmouseover="gutterOver(194)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',194);">&nbsp;</span
></td><td id="194"><a href="#194">194</a></td></tr
><tr id="gr_svn70_195"

 onmouseover="gutterOver(195)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',195);">&nbsp;</span
></td><td id="195"><a href="#195">195</a></td></tr
><tr id="gr_svn70_196"

 onmouseover="gutterOver(196)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',196);">&nbsp;</span
></td><td id="196"><a href="#196">196</a></td></tr
><tr id="gr_svn70_197"

 onmouseover="gutterOver(197)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',197);">&nbsp;</span
></td><td id="197"><a href="#197">197</a></td></tr
><tr id="gr_svn70_198"

 onmouseover="gutterOver(198)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',198);">&nbsp;</span
></td><td id="198"><a href="#198">198</a></td></tr
><tr id="gr_svn70_199"

 onmouseover="gutterOver(199)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',199);">&nbsp;</span
></td><td id="199"><a href="#199">199</a></td></tr
><tr id="gr_svn70_200"

 onmouseover="gutterOver(200)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',200);">&nbsp;</span
></td><td id="200"><a href="#200">200</a></td></tr
><tr id="gr_svn70_201"

 onmouseover="gutterOver(201)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',201);">&nbsp;</span
></td><td id="201"><a href="#201">201</a></td></tr
><tr id="gr_svn70_202"

 onmouseover="gutterOver(202)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',202);">&nbsp;</span
></td><td id="202"><a href="#202">202</a></td></tr
><tr id="gr_svn70_203"

 onmouseover="gutterOver(203)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',203);">&nbsp;</span
></td><td id="203"><a href="#203">203</a></td></tr
><tr id="gr_svn70_204"

 onmouseover="gutterOver(204)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',204);">&nbsp;</span
></td><td id="204"><a href="#204">204</a></td></tr
><tr id="gr_svn70_205"

 onmouseover="gutterOver(205)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',205);">&nbsp;</span
></td><td id="205"><a href="#205">205</a></td></tr
><tr id="gr_svn70_206"

 onmouseover="gutterOver(206)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',206);">&nbsp;</span
></td><td id="206"><a href="#206">206</a></td></tr
><tr id="gr_svn70_207"

 onmouseover="gutterOver(207)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',207);">&nbsp;</span
></td><td id="207"><a href="#207">207</a></td></tr
><tr id="gr_svn70_208"

 onmouseover="gutterOver(208)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',208);">&nbsp;</span
></td><td id="208"><a href="#208">208</a></td></tr
><tr id="gr_svn70_209"

 onmouseover="gutterOver(209)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',209);">&nbsp;</span
></td><td id="209"><a href="#209">209</a></td></tr
><tr id="gr_svn70_210"

 onmouseover="gutterOver(210)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',210);">&nbsp;</span
></td><td id="210"><a href="#210">210</a></td></tr
><tr id="gr_svn70_211"

 onmouseover="gutterOver(211)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',211);">&nbsp;</span
></td><td id="211"><a href="#211">211</a></td></tr
><tr id="gr_svn70_212"

 onmouseover="gutterOver(212)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',212);">&nbsp;</span
></td><td id="212"><a href="#212">212</a></td></tr
><tr id="gr_svn70_213"

 onmouseover="gutterOver(213)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',213);">&nbsp;</span
></td><td id="213"><a href="#213">213</a></td></tr
><tr id="gr_svn70_214"

 onmouseover="gutterOver(214)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',214);">&nbsp;</span
></td><td id="214"><a href="#214">214</a></td></tr
><tr id="gr_svn70_215"

 onmouseover="gutterOver(215)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',215);">&nbsp;</span
></td><td id="215"><a href="#215">215</a></td></tr
><tr id="gr_svn70_216"

 onmouseover="gutterOver(216)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',216);">&nbsp;</span
></td><td id="216"><a href="#216">216</a></td></tr
><tr id="gr_svn70_217"

 onmouseover="gutterOver(217)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',217);">&nbsp;</span
></td><td id="217"><a href="#217">217</a></td></tr
><tr id="gr_svn70_218"

 onmouseover="gutterOver(218)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',218);">&nbsp;</span
></td><td id="218"><a href="#218">218</a></td></tr
><tr id="gr_svn70_219"

 onmouseover="gutterOver(219)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',219);">&nbsp;</span
></td><td id="219"><a href="#219">219</a></td></tr
><tr id="gr_svn70_220"

 onmouseover="gutterOver(220)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',220);">&nbsp;</span
></td><td id="220"><a href="#220">220</a></td></tr
><tr id="gr_svn70_221"

 onmouseover="gutterOver(221)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',221);">&nbsp;</span
></td><td id="221"><a href="#221">221</a></td></tr
><tr id="gr_svn70_222"

 onmouseover="gutterOver(222)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',222);">&nbsp;</span
></td><td id="222"><a href="#222">222</a></td></tr
><tr id="gr_svn70_223"

 onmouseover="gutterOver(223)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',223);">&nbsp;</span
></td><td id="223"><a href="#223">223</a></td></tr
><tr id="gr_svn70_224"

 onmouseover="gutterOver(224)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',224);">&nbsp;</span
></td><td id="224"><a href="#224">224</a></td></tr
><tr id="gr_svn70_225"

 onmouseover="gutterOver(225)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',225);">&nbsp;</span
></td><td id="225"><a href="#225">225</a></td></tr
><tr id="gr_svn70_226"

 onmouseover="gutterOver(226)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',226);">&nbsp;</span
></td><td id="226"><a href="#226">226</a></td></tr
><tr id="gr_svn70_227"

 onmouseover="gutterOver(227)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',227);">&nbsp;</span
></td><td id="227"><a href="#227">227</a></td></tr
><tr id="gr_svn70_228"

 onmouseover="gutterOver(228)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',228);">&nbsp;</span
></td><td id="228"><a href="#228">228</a></td></tr
><tr id="gr_svn70_229"

 onmouseover="gutterOver(229)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',229);">&nbsp;</span
></td><td id="229"><a href="#229">229</a></td></tr
><tr id="gr_svn70_230"

 onmouseover="gutterOver(230)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',230);">&nbsp;</span
></td><td id="230"><a href="#230">230</a></td></tr
><tr id="gr_svn70_231"

 onmouseover="gutterOver(231)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',231);">&nbsp;</span
></td><td id="231"><a href="#231">231</a></td></tr
><tr id="gr_svn70_232"

 onmouseover="gutterOver(232)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',232);">&nbsp;</span
></td><td id="232"><a href="#232">232</a></td></tr
><tr id="gr_svn70_233"

 onmouseover="gutterOver(233)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',233);">&nbsp;</span
></td><td id="233"><a href="#233">233</a></td></tr
><tr id="gr_svn70_234"

 onmouseover="gutterOver(234)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',234);">&nbsp;</span
></td><td id="234"><a href="#234">234</a></td></tr
><tr id="gr_svn70_235"

 onmouseover="gutterOver(235)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',235);">&nbsp;</span
></td><td id="235"><a href="#235">235</a></td></tr
><tr id="gr_svn70_236"

 onmouseover="gutterOver(236)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',236);">&nbsp;</span
></td><td id="236"><a href="#236">236</a></td></tr
><tr id="gr_svn70_237"

 onmouseover="gutterOver(237)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',237);">&nbsp;</span
></td><td id="237"><a href="#237">237</a></td></tr
><tr id="gr_svn70_238"

 onmouseover="gutterOver(238)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',238);">&nbsp;</span
></td><td id="238"><a href="#238">238</a></td></tr
><tr id="gr_svn70_239"

 onmouseover="gutterOver(239)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',239);">&nbsp;</span
></td><td id="239"><a href="#239">239</a></td></tr
><tr id="gr_svn70_240"

 onmouseover="gutterOver(240)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',240);">&nbsp;</span
></td><td id="240"><a href="#240">240</a></td></tr
><tr id="gr_svn70_241"

 onmouseover="gutterOver(241)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',241);">&nbsp;</span
></td><td id="241"><a href="#241">241</a></td></tr
><tr id="gr_svn70_242"

 onmouseover="gutterOver(242)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',242);">&nbsp;</span
></td><td id="242"><a href="#242">242</a></td></tr
><tr id="gr_svn70_243"

 onmouseover="gutterOver(243)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',243);">&nbsp;</span
></td><td id="243"><a href="#243">243</a></td></tr
><tr id="gr_svn70_244"

 onmouseover="gutterOver(244)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',244);">&nbsp;</span
></td><td id="244"><a href="#244">244</a></td></tr
><tr id="gr_svn70_245"

 onmouseover="gutterOver(245)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',245);">&nbsp;</span
></td><td id="245"><a href="#245">245</a></td></tr
><tr id="gr_svn70_246"

 onmouseover="gutterOver(246)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',246);">&nbsp;</span
></td><td id="246"><a href="#246">246</a></td></tr
><tr id="gr_svn70_247"

 onmouseover="gutterOver(247)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',247);">&nbsp;</span
></td><td id="247"><a href="#247">247</a></td></tr
><tr id="gr_svn70_248"

 onmouseover="gutterOver(248)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',248);">&nbsp;</span
></td><td id="248"><a href="#248">248</a></td></tr
><tr id="gr_svn70_249"

 onmouseover="gutterOver(249)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',249);">&nbsp;</span
></td><td id="249"><a href="#249">249</a></td></tr
><tr id="gr_svn70_250"

 onmouseover="gutterOver(250)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',250);">&nbsp;</span
></td><td id="250"><a href="#250">250</a></td></tr
><tr id="gr_svn70_251"

 onmouseover="gutterOver(251)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',251);">&nbsp;</span
></td><td id="251"><a href="#251">251</a></td></tr
><tr id="gr_svn70_252"

 onmouseover="gutterOver(252)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',252);">&nbsp;</span
></td><td id="252"><a href="#252">252</a></td></tr
><tr id="gr_svn70_253"

 onmouseover="gutterOver(253)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',253);">&nbsp;</span
></td><td id="253"><a href="#253">253</a></td></tr
><tr id="gr_svn70_254"

 onmouseover="gutterOver(254)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',254);">&nbsp;</span
></td><td id="254"><a href="#254">254</a></td></tr
><tr id="gr_svn70_255"

 onmouseover="gutterOver(255)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',255);">&nbsp;</span
></td><td id="255"><a href="#255">255</a></td></tr
><tr id="gr_svn70_256"

 onmouseover="gutterOver(256)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',256);">&nbsp;</span
></td><td id="256"><a href="#256">256</a></td></tr
><tr id="gr_svn70_257"

 onmouseover="gutterOver(257)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',257);">&nbsp;</span
></td><td id="257"><a href="#257">257</a></td></tr
><tr id="gr_svn70_258"

 onmouseover="gutterOver(258)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',258);">&nbsp;</span
></td><td id="258"><a href="#258">258</a></td></tr
><tr id="gr_svn70_259"

 onmouseover="gutterOver(259)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',259);">&nbsp;</span
></td><td id="259"><a href="#259">259</a></td></tr
><tr id="gr_svn70_260"

 onmouseover="gutterOver(260)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',260);">&nbsp;</span
></td><td id="260"><a href="#260">260</a></td></tr
><tr id="gr_svn70_261"

 onmouseover="gutterOver(261)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',261);">&nbsp;</span
></td><td id="261"><a href="#261">261</a></td></tr
><tr id="gr_svn70_262"

 onmouseover="gutterOver(262)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',262);">&nbsp;</span
></td><td id="262"><a href="#262">262</a></td></tr
><tr id="gr_svn70_263"

 onmouseover="gutterOver(263)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',263);">&nbsp;</span
></td><td id="263"><a href="#263">263</a></td></tr
><tr id="gr_svn70_264"

 onmouseover="gutterOver(264)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',264);">&nbsp;</span
></td><td id="264"><a href="#264">264</a></td></tr
><tr id="gr_svn70_265"

 onmouseover="gutterOver(265)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',265);">&nbsp;</span
></td><td id="265"><a href="#265">265</a></td></tr
><tr id="gr_svn70_266"

 onmouseover="gutterOver(266)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',266);">&nbsp;</span
></td><td id="266"><a href="#266">266</a></td></tr
><tr id="gr_svn70_267"

 onmouseover="gutterOver(267)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',267);">&nbsp;</span
></td><td id="267"><a href="#267">267</a></td></tr
><tr id="gr_svn70_268"

 onmouseover="gutterOver(268)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',268);">&nbsp;</span
></td><td id="268"><a href="#268">268</a></td></tr
><tr id="gr_svn70_269"

 onmouseover="gutterOver(269)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',269);">&nbsp;</span
></td><td id="269"><a href="#269">269</a></td></tr
><tr id="gr_svn70_270"

 onmouseover="gutterOver(270)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',270);">&nbsp;</span
></td><td id="270"><a href="#270">270</a></td></tr
><tr id="gr_svn70_271"

 onmouseover="gutterOver(271)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',271);">&nbsp;</span
></td><td id="271"><a href="#271">271</a></td></tr
><tr id="gr_svn70_272"

 onmouseover="gutterOver(272)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',272);">&nbsp;</span
></td><td id="272"><a href="#272">272</a></td></tr
><tr id="gr_svn70_273"

 onmouseover="gutterOver(273)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',273);">&nbsp;</span
></td><td id="273"><a href="#273">273</a></td></tr
><tr id="gr_svn70_274"

 onmouseover="gutterOver(274)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',274);">&nbsp;</span
></td><td id="274"><a href="#274">274</a></td></tr
><tr id="gr_svn70_275"

 onmouseover="gutterOver(275)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',275);">&nbsp;</span
></td><td id="275"><a href="#275">275</a></td></tr
><tr id="gr_svn70_276"

 onmouseover="gutterOver(276)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',276);">&nbsp;</span
></td><td id="276"><a href="#276">276</a></td></tr
><tr id="gr_svn70_277"

 onmouseover="gutterOver(277)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',277);">&nbsp;</span
></td><td id="277"><a href="#277">277</a></td></tr
><tr id="gr_svn70_278"

 onmouseover="gutterOver(278)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',278);">&nbsp;</span
></td><td id="278"><a href="#278">278</a></td></tr
><tr id="gr_svn70_279"

 onmouseover="gutterOver(279)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',279);">&nbsp;</span
></td><td id="279"><a href="#279">279</a></td></tr
><tr id="gr_svn70_280"

 onmouseover="gutterOver(280)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',280);">&nbsp;</span
></td><td id="280"><a href="#280">280</a></td></tr
><tr id="gr_svn70_281"

 onmouseover="gutterOver(281)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',281);">&nbsp;</span
></td><td id="281"><a href="#281">281</a></td></tr
><tr id="gr_svn70_282"

 onmouseover="gutterOver(282)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',282);">&nbsp;</span
></td><td id="282"><a href="#282">282</a></td></tr
><tr id="gr_svn70_283"

 onmouseover="gutterOver(283)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',283);">&nbsp;</span
></td><td id="283"><a href="#283">283</a></td></tr
><tr id="gr_svn70_284"

 onmouseover="gutterOver(284)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',284);">&nbsp;</span
></td><td id="284"><a href="#284">284</a></td></tr
><tr id="gr_svn70_285"

 onmouseover="gutterOver(285)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',285);">&nbsp;</span
></td><td id="285"><a href="#285">285</a></td></tr
><tr id="gr_svn70_286"

 onmouseover="gutterOver(286)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',286);">&nbsp;</span
></td><td id="286"><a href="#286">286</a></td></tr
><tr id="gr_svn70_287"

 onmouseover="gutterOver(287)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',287);">&nbsp;</span
></td><td id="287"><a href="#287">287</a></td></tr
><tr id="gr_svn70_288"

 onmouseover="gutterOver(288)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',288);">&nbsp;</span
></td><td id="288"><a href="#288">288</a></td></tr
><tr id="gr_svn70_289"

 onmouseover="gutterOver(289)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',289);">&nbsp;</span
></td><td id="289"><a href="#289">289</a></td></tr
><tr id="gr_svn70_290"

 onmouseover="gutterOver(290)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',290);">&nbsp;</span
></td><td id="290"><a href="#290">290</a></td></tr
><tr id="gr_svn70_291"

 onmouseover="gutterOver(291)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',291);">&nbsp;</span
></td><td id="291"><a href="#291">291</a></td></tr
><tr id="gr_svn70_292"

 onmouseover="gutterOver(292)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',292);">&nbsp;</span
></td><td id="292"><a href="#292">292</a></td></tr
><tr id="gr_svn70_293"

 onmouseover="gutterOver(293)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',293);">&nbsp;</span
></td><td id="293"><a href="#293">293</a></td></tr
><tr id="gr_svn70_294"

 onmouseover="gutterOver(294)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',294);">&nbsp;</span
></td><td id="294"><a href="#294">294</a></td></tr
><tr id="gr_svn70_295"

 onmouseover="gutterOver(295)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',295);">&nbsp;</span
></td><td id="295"><a href="#295">295</a></td></tr
><tr id="gr_svn70_296"

 onmouseover="gutterOver(296)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',296);">&nbsp;</span
></td><td id="296"><a href="#296">296</a></td></tr
><tr id="gr_svn70_297"

 onmouseover="gutterOver(297)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',297);">&nbsp;</span
></td><td id="297"><a href="#297">297</a></td></tr
><tr id="gr_svn70_298"

 onmouseover="gutterOver(298)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',298);">&nbsp;</span
></td><td id="298"><a href="#298">298</a></td></tr
><tr id="gr_svn70_299"

 onmouseover="gutterOver(299)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',299);">&nbsp;</span
></td><td id="299"><a href="#299">299</a></td></tr
><tr id="gr_svn70_300"

 onmouseover="gutterOver(300)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',300);">&nbsp;</span
></td><td id="300"><a href="#300">300</a></td></tr
><tr id="gr_svn70_301"

 onmouseover="gutterOver(301)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',301);">&nbsp;</span
></td><td id="301"><a href="#301">301</a></td></tr
><tr id="gr_svn70_302"

 onmouseover="gutterOver(302)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',302);">&nbsp;</span
></td><td id="302"><a href="#302">302</a></td></tr
><tr id="gr_svn70_303"

 onmouseover="gutterOver(303)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',303);">&nbsp;</span
></td><td id="303"><a href="#303">303</a></td></tr
><tr id="gr_svn70_304"

 onmouseover="gutterOver(304)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',304);">&nbsp;</span
></td><td id="304"><a href="#304">304</a></td></tr
><tr id="gr_svn70_305"

 onmouseover="gutterOver(305)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',305);">&nbsp;</span
></td><td id="305"><a href="#305">305</a></td></tr
><tr id="gr_svn70_306"

 onmouseover="gutterOver(306)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',306);">&nbsp;</span
></td><td id="306"><a href="#306">306</a></td></tr
><tr id="gr_svn70_307"

 onmouseover="gutterOver(307)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',307);">&nbsp;</span
></td><td id="307"><a href="#307">307</a></td></tr
><tr id="gr_svn70_308"

 onmouseover="gutterOver(308)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',308);">&nbsp;</span
></td><td id="308"><a href="#308">308</a></td></tr
><tr id="gr_svn70_309"

 onmouseover="gutterOver(309)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',309);">&nbsp;</span
></td><td id="309"><a href="#309">309</a></td></tr
><tr id="gr_svn70_310"

 onmouseover="gutterOver(310)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',310);">&nbsp;</span
></td><td id="310"><a href="#310">310</a></td></tr
><tr id="gr_svn70_311"

 onmouseover="gutterOver(311)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',311);">&nbsp;</span
></td><td id="311"><a href="#311">311</a></td></tr
><tr id="gr_svn70_312"

 onmouseover="gutterOver(312)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',312);">&nbsp;</span
></td><td id="312"><a href="#312">312</a></td></tr
><tr id="gr_svn70_313"

 onmouseover="gutterOver(313)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',313);">&nbsp;</span
></td><td id="313"><a href="#313">313</a></td></tr
><tr id="gr_svn70_314"

 onmouseover="gutterOver(314)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',314);">&nbsp;</span
></td><td id="314"><a href="#314">314</a></td></tr
><tr id="gr_svn70_315"

 onmouseover="gutterOver(315)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',315);">&nbsp;</span
></td><td id="315"><a href="#315">315</a></td></tr
><tr id="gr_svn70_316"

 onmouseover="gutterOver(316)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',316);">&nbsp;</span
></td><td id="316"><a href="#316">316</a></td></tr
><tr id="gr_svn70_317"

 onmouseover="gutterOver(317)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',317);">&nbsp;</span
></td><td id="317"><a href="#317">317</a></td></tr
><tr id="gr_svn70_318"

 onmouseover="gutterOver(318)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',318);">&nbsp;</span
></td><td id="318"><a href="#318">318</a></td></tr
><tr id="gr_svn70_319"

 onmouseover="gutterOver(319)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',319);">&nbsp;</span
></td><td id="319"><a href="#319">319</a></td></tr
><tr id="gr_svn70_320"

 onmouseover="gutterOver(320)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',320);">&nbsp;</span
></td><td id="320"><a href="#320">320</a></td></tr
><tr id="gr_svn70_321"

 onmouseover="gutterOver(321)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',321);">&nbsp;</span
></td><td id="321"><a href="#321">321</a></td></tr
><tr id="gr_svn70_322"

 onmouseover="gutterOver(322)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',322);">&nbsp;</span
></td><td id="322"><a href="#322">322</a></td></tr
><tr id="gr_svn70_323"

 onmouseover="gutterOver(323)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',323);">&nbsp;</span
></td><td id="323"><a href="#323">323</a></td></tr
><tr id="gr_svn70_324"

 onmouseover="gutterOver(324)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',324);">&nbsp;</span
></td><td id="324"><a href="#324">324</a></td></tr
><tr id="gr_svn70_325"

 onmouseover="gutterOver(325)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',325);">&nbsp;</span
></td><td id="325"><a href="#325">325</a></td></tr
><tr id="gr_svn70_326"

 onmouseover="gutterOver(326)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',326);">&nbsp;</span
></td><td id="326"><a href="#326">326</a></td></tr
><tr id="gr_svn70_327"

 onmouseover="gutterOver(327)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',327);">&nbsp;</span
></td><td id="327"><a href="#327">327</a></td></tr
><tr id="gr_svn70_328"

 onmouseover="gutterOver(328)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',328);">&nbsp;</span
></td><td id="328"><a href="#328">328</a></td></tr
><tr id="gr_svn70_329"

 onmouseover="gutterOver(329)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',329);">&nbsp;</span
></td><td id="329"><a href="#329">329</a></td></tr
><tr id="gr_svn70_330"

 onmouseover="gutterOver(330)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',330);">&nbsp;</span
></td><td id="330"><a href="#330">330</a></td></tr
><tr id="gr_svn70_331"

 onmouseover="gutterOver(331)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',331);">&nbsp;</span
></td><td id="331"><a href="#331">331</a></td></tr
><tr id="gr_svn70_332"

 onmouseover="gutterOver(332)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',332);">&nbsp;</span
></td><td id="332"><a href="#332">332</a></td></tr
><tr id="gr_svn70_333"

 onmouseover="gutterOver(333)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',333);">&nbsp;</span
></td><td id="333"><a href="#333">333</a></td></tr
><tr id="gr_svn70_334"

 onmouseover="gutterOver(334)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',334);">&nbsp;</span
></td><td id="334"><a href="#334">334</a></td></tr
><tr id="gr_svn70_335"

 onmouseover="gutterOver(335)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',335);">&nbsp;</span
></td><td id="335"><a href="#335">335</a></td></tr
><tr id="gr_svn70_336"

 onmouseover="gutterOver(336)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',336);">&nbsp;</span
></td><td id="336"><a href="#336">336</a></td></tr
><tr id="gr_svn70_337"

 onmouseover="gutterOver(337)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',337);">&nbsp;</span
></td><td id="337"><a href="#337">337</a></td></tr
><tr id="gr_svn70_338"

 onmouseover="gutterOver(338)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',338);">&nbsp;</span
></td><td id="338"><a href="#338">338</a></td></tr
><tr id="gr_svn70_339"

 onmouseover="gutterOver(339)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',339);">&nbsp;</span
></td><td id="339"><a href="#339">339</a></td></tr
><tr id="gr_svn70_340"

 onmouseover="gutterOver(340)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',340);">&nbsp;</span
></td><td id="340"><a href="#340">340</a></td></tr
><tr id="gr_svn70_341"

 onmouseover="gutterOver(341)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',341);">&nbsp;</span
></td><td id="341"><a href="#341">341</a></td></tr
><tr id="gr_svn70_342"

 onmouseover="gutterOver(342)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',342);">&nbsp;</span
></td><td id="342"><a href="#342">342</a></td></tr
><tr id="gr_svn70_343"

 onmouseover="gutterOver(343)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',343);">&nbsp;</span
></td><td id="343"><a href="#343">343</a></td></tr
><tr id="gr_svn70_344"

 onmouseover="gutterOver(344)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',344);">&nbsp;</span
></td><td id="344"><a href="#344">344</a></td></tr
><tr id="gr_svn70_345"

 onmouseover="gutterOver(345)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',345);">&nbsp;</span
></td><td id="345"><a href="#345">345</a></td></tr
><tr id="gr_svn70_346"

 onmouseover="gutterOver(346)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',346);">&nbsp;</span
></td><td id="346"><a href="#346">346</a></td></tr
><tr id="gr_svn70_347"

 onmouseover="gutterOver(347)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',347);">&nbsp;</span
></td><td id="347"><a href="#347">347</a></td></tr
><tr id="gr_svn70_348"

 onmouseover="gutterOver(348)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',348);">&nbsp;</span
></td><td id="348"><a href="#348">348</a></td></tr
><tr id="gr_svn70_349"

 onmouseover="gutterOver(349)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',349);">&nbsp;</span
></td><td id="349"><a href="#349">349</a></td></tr
><tr id="gr_svn70_350"

 onmouseover="gutterOver(350)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',350);">&nbsp;</span
></td><td id="350"><a href="#350">350</a></td></tr
><tr id="gr_svn70_351"

 onmouseover="gutterOver(351)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',351);">&nbsp;</span
></td><td id="351"><a href="#351">351</a></td></tr
><tr id="gr_svn70_352"

 onmouseover="gutterOver(352)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',352);">&nbsp;</span
></td><td id="352"><a href="#352">352</a></td></tr
><tr id="gr_svn70_353"

 onmouseover="gutterOver(353)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',353);">&nbsp;</span
></td><td id="353"><a href="#353">353</a></td></tr
><tr id="gr_svn70_354"

 onmouseover="gutterOver(354)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',354);">&nbsp;</span
></td><td id="354"><a href="#354">354</a></td></tr
><tr id="gr_svn70_355"

 onmouseover="gutterOver(355)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',355);">&nbsp;</span
></td><td id="355"><a href="#355">355</a></td></tr
><tr id="gr_svn70_356"

 onmouseover="gutterOver(356)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',356);">&nbsp;</span
></td><td id="356"><a href="#356">356</a></td></tr
><tr id="gr_svn70_357"

 onmouseover="gutterOver(357)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',357);">&nbsp;</span
></td><td id="357"><a href="#357">357</a></td></tr
><tr id="gr_svn70_358"

 onmouseover="gutterOver(358)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',358);">&nbsp;</span
></td><td id="358"><a href="#358">358</a></td></tr
><tr id="gr_svn70_359"

 onmouseover="gutterOver(359)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',359);">&nbsp;</span
></td><td id="359"><a href="#359">359</a></td></tr
><tr id="gr_svn70_360"

 onmouseover="gutterOver(360)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',360);">&nbsp;</span
></td><td id="360"><a href="#360">360</a></td></tr
><tr id="gr_svn70_361"

 onmouseover="gutterOver(361)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',361);">&nbsp;</span
></td><td id="361"><a href="#361">361</a></td></tr
><tr id="gr_svn70_362"

 onmouseover="gutterOver(362)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',362);">&nbsp;</span
></td><td id="362"><a href="#362">362</a></td></tr
><tr id="gr_svn70_363"

 onmouseover="gutterOver(363)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',363);">&nbsp;</span
></td><td id="363"><a href="#363">363</a></td></tr
><tr id="gr_svn70_364"

 onmouseover="gutterOver(364)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',364);">&nbsp;</span
></td><td id="364"><a href="#364">364</a></td></tr
><tr id="gr_svn70_365"

 onmouseover="gutterOver(365)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',365);">&nbsp;</span
></td><td id="365"><a href="#365">365</a></td></tr
><tr id="gr_svn70_366"

 onmouseover="gutterOver(366)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',366);">&nbsp;</span
></td><td id="366"><a href="#366">366</a></td></tr
><tr id="gr_svn70_367"

 onmouseover="gutterOver(367)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',367);">&nbsp;</span
></td><td id="367"><a href="#367">367</a></td></tr
><tr id="gr_svn70_368"

 onmouseover="gutterOver(368)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',368);">&nbsp;</span
></td><td id="368"><a href="#368">368</a></td></tr
><tr id="gr_svn70_369"

 onmouseover="gutterOver(369)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',369);">&nbsp;</span
></td><td id="369"><a href="#369">369</a></td></tr
><tr id="gr_svn70_370"

 onmouseover="gutterOver(370)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',370);">&nbsp;</span
></td><td id="370"><a href="#370">370</a></td></tr
><tr id="gr_svn70_371"

 onmouseover="gutterOver(371)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',371);">&nbsp;</span
></td><td id="371"><a href="#371">371</a></td></tr
><tr id="gr_svn70_372"

 onmouseover="gutterOver(372)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',372);">&nbsp;</span
></td><td id="372"><a href="#372">372</a></td></tr
><tr id="gr_svn70_373"

 onmouseover="gutterOver(373)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',373);">&nbsp;</span
></td><td id="373"><a href="#373">373</a></td></tr
><tr id="gr_svn70_374"

 onmouseover="gutterOver(374)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',374);">&nbsp;</span
></td><td id="374"><a href="#374">374</a></td></tr
><tr id="gr_svn70_375"

 onmouseover="gutterOver(375)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',375);">&nbsp;</span
></td><td id="375"><a href="#375">375</a></td></tr
><tr id="gr_svn70_376"

 onmouseover="gutterOver(376)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',376);">&nbsp;</span
></td><td id="376"><a href="#376">376</a></td></tr
><tr id="gr_svn70_377"

 onmouseover="gutterOver(377)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',377);">&nbsp;</span
></td><td id="377"><a href="#377">377</a></td></tr
><tr id="gr_svn70_378"

 onmouseover="gutterOver(378)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',378);">&nbsp;</span
></td><td id="378"><a href="#378">378</a></td></tr
><tr id="gr_svn70_379"

 onmouseover="gutterOver(379)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',379);">&nbsp;</span
></td><td id="379"><a href="#379">379</a></td></tr
><tr id="gr_svn70_380"

 onmouseover="gutterOver(380)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',380);">&nbsp;</span
></td><td id="380"><a href="#380">380</a></td></tr
><tr id="gr_svn70_381"

 onmouseover="gutterOver(381)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',381);">&nbsp;</span
></td><td id="381"><a href="#381">381</a></td></tr
><tr id="gr_svn70_382"

 onmouseover="gutterOver(382)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',382);">&nbsp;</span
></td><td id="382"><a href="#382">382</a></td></tr
><tr id="gr_svn70_383"

 onmouseover="gutterOver(383)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',383);">&nbsp;</span
></td><td id="383"><a href="#383">383</a></td></tr
><tr id="gr_svn70_384"

 onmouseover="gutterOver(384)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',384);">&nbsp;</span
></td><td id="384"><a href="#384">384</a></td></tr
><tr id="gr_svn70_385"

 onmouseover="gutterOver(385)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',385);">&nbsp;</span
></td><td id="385"><a href="#385">385</a></td></tr
><tr id="gr_svn70_386"

 onmouseover="gutterOver(386)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',386);">&nbsp;</span
></td><td id="386"><a href="#386">386</a></td></tr
><tr id="gr_svn70_387"

 onmouseover="gutterOver(387)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',387);">&nbsp;</span
></td><td id="387"><a href="#387">387</a></td></tr
><tr id="gr_svn70_388"

 onmouseover="gutterOver(388)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',388);">&nbsp;</span
></td><td id="388"><a href="#388">388</a></td></tr
><tr id="gr_svn70_389"

 onmouseover="gutterOver(389)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',389);">&nbsp;</span
></td><td id="389"><a href="#389">389</a></td></tr
><tr id="gr_svn70_390"

 onmouseover="gutterOver(390)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',390);">&nbsp;</span
></td><td id="390"><a href="#390">390</a></td></tr
><tr id="gr_svn70_391"

 onmouseover="gutterOver(391)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',391);">&nbsp;</span
></td><td id="391"><a href="#391">391</a></td></tr
><tr id="gr_svn70_392"

 onmouseover="gutterOver(392)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',392);">&nbsp;</span
></td><td id="392"><a href="#392">392</a></td></tr
><tr id="gr_svn70_393"

 onmouseover="gutterOver(393)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',393);">&nbsp;</span
></td><td id="393"><a href="#393">393</a></td></tr
><tr id="gr_svn70_394"

 onmouseover="gutterOver(394)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',394);">&nbsp;</span
></td><td id="394"><a href="#394">394</a></td></tr
><tr id="gr_svn70_395"

 onmouseover="gutterOver(395)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',395);">&nbsp;</span
></td><td id="395"><a href="#395">395</a></td></tr
><tr id="gr_svn70_396"

 onmouseover="gutterOver(396)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',396);">&nbsp;</span
></td><td id="396"><a href="#396">396</a></td></tr
><tr id="gr_svn70_397"

 onmouseover="gutterOver(397)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',397);">&nbsp;</span
></td><td id="397"><a href="#397">397</a></td></tr
><tr id="gr_svn70_398"

 onmouseover="gutterOver(398)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',398);">&nbsp;</span
></td><td id="398"><a href="#398">398</a></td></tr
><tr id="gr_svn70_399"

 onmouseover="gutterOver(399)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',399);">&nbsp;</span
></td><td id="399"><a href="#399">399</a></td></tr
><tr id="gr_svn70_400"

 onmouseover="gutterOver(400)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',400);">&nbsp;</span
></td><td id="400"><a href="#400">400</a></td></tr
><tr id="gr_svn70_401"

 onmouseover="gutterOver(401)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',401);">&nbsp;</span
></td><td id="401"><a href="#401">401</a></td></tr
><tr id="gr_svn70_402"

 onmouseover="gutterOver(402)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',402);">&nbsp;</span
></td><td id="402"><a href="#402">402</a></td></tr
><tr id="gr_svn70_403"

 onmouseover="gutterOver(403)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',403);">&nbsp;</span
></td><td id="403"><a href="#403">403</a></td></tr
><tr id="gr_svn70_404"

 onmouseover="gutterOver(404)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',404);">&nbsp;</span
></td><td id="404"><a href="#404">404</a></td></tr
><tr id="gr_svn70_405"

 onmouseover="gutterOver(405)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',405);">&nbsp;</span
></td><td id="405"><a href="#405">405</a></td></tr
><tr id="gr_svn70_406"

 onmouseover="gutterOver(406)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',406);">&nbsp;</span
></td><td id="406"><a href="#406">406</a></td></tr
><tr id="gr_svn70_407"

 onmouseover="gutterOver(407)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',407);">&nbsp;</span
></td><td id="407"><a href="#407">407</a></td></tr
><tr id="gr_svn70_408"

 onmouseover="gutterOver(408)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',408);">&nbsp;</span
></td><td id="408"><a href="#408">408</a></td></tr
><tr id="gr_svn70_409"

 onmouseover="gutterOver(409)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',409);">&nbsp;</span
></td><td id="409"><a href="#409">409</a></td></tr
><tr id="gr_svn70_410"

 onmouseover="gutterOver(410)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',410);">&nbsp;</span
></td><td id="410"><a href="#410">410</a></td></tr
><tr id="gr_svn70_411"

 onmouseover="gutterOver(411)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',411);">&nbsp;</span
></td><td id="411"><a href="#411">411</a></td></tr
><tr id="gr_svn70_412"

 onmouseover="gutterOver(412)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',412);">&nbsp;</span
></td><td id="412"><a href="#412">412</a></td></tr
><tr id="gr_svn70_413"

 onmouseover="gutterOver(413)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',413);">&nbsp;</span
></td><td id="413"><a href="#413">413</a></td></tr
><tr id="gr_svn70_414"

 onmouseover="gutterOver(414)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',414);">&nbsp;</span
></td><td id="414"><a href="#414">414</a></td></tr
><tr id="gr_svn70_415"

 onmouseover="gutterOver(415)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',415);">&nbsp;</span
></td><td id="415"><a href="#415">415</a></td></tr
><tr id="gr_svn70_416"

 onmouseover="gutterOver(416)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',416);">&nbsp;</span
></td><td id="416"><a href="#416">416</a></td></tr
><tr id="gr_svn70_417"

 onmouseover="gutterOver(417)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',417);">&nbsp;</span
></td><td id="417"><a href="#417">417</a></td></tr
><tr id="gr_svn70_418"

 onmouseover="gutterOver(418)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',418);">&nbsp;</span
></td><td id="418"><a href="#418">418</a></td></tr
><tr id="gr_svn70_419"

 onmouseover="gutterOver(419)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',419);">&nbsp;</span
></td><td id="419"><a href="#419">419</a></td></tr
><tr id="gr_svn70_420"

 onmouseover="gutterOver(420)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',420);">&nbsp;</span
></td><td id="420"><a href="#420">420</a></td></tr
><tr id="gr_svn70_421"

 onmouseover="gutterOver(421)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',421);">&nbsp;</span
></td><td id="421"><a href="#421">421</a></td></tr
><tr id="gr_svn70_422"

 onmouseover="gutterOver(422)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',422);">&nbsp;</span
></td><td id="422"><a href="#422">422</a></td></tr
><tr id="gr_svn70_423"

 onmouseover="gutterOver(423)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',423);">&nbsp;</span
></td><td id="423"><a href="#423">423</a></td></tr
><tr id="gr_svn70_424"

 onmouseover="gutterOver(424)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',424);">&nbsp;</span
></td><td id="424"><a href="#424">424</a></td></tr
><tr id="gr_svn70_425"

 onmouseover="gutterOver(425)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',425);">&nbsp;</span
></td><td id="425"><a href="#425">425</a></td></tr
><tr id="gr_svn70_426"

 onmouseover="gutterOver(426)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',426);">&nbsp;</span
></td><td id="426"><a href="#426">426</a></td></tr
><tr id="gr_svn70_427"

 onmouseover="gutterOver(427)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',427);">&nbsp;</span
></td><td id="427"><a href="#427">427</a></td></tr
><tr id="gr_svn70_428"

 onmouseover="gutterOver(428)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',428);">&nbsp;</span
></td><td id="428"><a href="#428">428</a></td></tr
><tr id="gr_svn70_429"

 onmouseover="gutterOver(429)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',429);">&nbsp;</span
></td><td id="429"><a href="#429">429</a></td></tr
><tr id="gr_svn70_430"

 onmouseover="gutterOver(430)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',430);">&nbsp;</span
></td><td id="430"><a href="#430">430</a></td></tr
><tr id="gr_svn70_431"

 onmouseover="gutterOver(431)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',431);">&nbsp;</span
></td><td id="431"><a href="#431">431</a></td></tr
><tr id="gr_svn70_432"

 onmouseover="gutterOver(432)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',432);">&nbsp;</span
></td><td id="432"><a href="#432">432</a></td></tr
><tr id="gr_svn70_433"

 onmouseover="gutterOver(433)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',433);">&nbsp;</span
></td><td id="433"><a href="#433">433</a></td></tr
><tr id="gr_svn70_434"

 onmouseover="gutterOver(434)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',434);">&nbsp;</span
></td><td id="434"><a href="#434">434</a></td></tr
><tr id="gr_svn70_435"

 onmouseover="gutterOver(435)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',435);">&nbsp;</span
></td><td id="435"><a href="#435">435</a></td></tr
><tr id="gr_svn70_436"

 onmouseover="gutterOver(436)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',436);">&nbsp;</span
></td><td id="436"><a href="#436">436</a></td></tr
><tr id="gr_svn70_437"

 onmouseover="gutterOver(437)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',437);">&nbsp;</span
></td><td id="437"><a href="#437">437</a></td></tr
><tr id="gr_svn70_438"

 onmouseover="gutterOver(438)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',438);">&nbsp;</span
></td><td id="438"><a href="#438">438</a></td></tr
><tr id="gr_svn70_439"

 onmouseover="gutterOver(439)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',439);">&nbsp;</span
></td><td id="439"><a href="#439">439</a></td></tr
><tr id="gr_svn70_440"

 onmouseover="gutterOver(440)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',440);">&nbsp;</span
></td><td id="440"><a href="#440">440</a></td></tr
><tr id="gr_svn70_441"

 onmouseover="gutterOver(441)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',441);">&nbsp;</span
></td><td id="441"><a href="#441">441</a></td></tr
><tr id="gr_svn70_442"

 onmouseover="gutterOver(442)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',442);">&nbsp;</span
></td><td id="442"><a href="#442">442</a></td></tr
><tr id="gr_svn70_443"

 onmouseover="gutterOver(443)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',443);">&nbsp;</span
></td><td id="443"><a href="#443">443</a></td></tr
><tr id="gr_svn70_444"

 onmouseover="gutterOver(444)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',444);">&nbsp;</span
></td><td id="444"><a href="#444">444</a></td></tr
><tr id="gr_svn70_445"

 onmouseover="gutterOver(445)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',445);">&nbsp;</span
></td><td id="445"><a href="#445">445</a></td></tr
><tr id="gr_svn70_446"

 onmouseover="gutterOver(446)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',446);">&nbsp;</span
></td><td id="446"><a href="#446">446</a></td></tr
><tr id="gr_svn70_447"

 onmouseover="gutterOver(447)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',447);">&nbsp;</span
></td><td id="447"><a href="#447">447</a></td></tr
><tr id="gr_svn70_448"

 onmouseover="gutterOver(448)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',448);">&nbsp;</span
></td><td id="448"><a href="#448">448</a></td></tr
><tr id="gr_svn70_449"

 onmouseover="gutterOver(449)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',449);">&nbsp;</span
></td><td id="449"><a href="#449">449</a></td></tr
><tr id="gr_svn70_450"

 onmouseover="gutterOver(450)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',450);">&nbsp;</span
></td><td id="450"><a href="#450">450</a></td></tr
><tr id="gr_svn70_451"

 onmouseover="gutterOver(451)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',451);">&nbsp;</span
></td><td id="451"><a href="#451">451</a></td></tr
><tr id="gr_svn70_452"

 onmouseover="gutterOver(452)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',452);">&nbsp;</span
></td><td id="452"><a href="#452">452</a></td></tr
><tr id="gr_svn70_453"

 onmouseover="gutterOver(453)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',453);">&nbsp;</span
></td><td id="453"><a href="#453">453</a></td></tr
><tr id="gr_svn70_454"

 onmouseover="gutterOver(454)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',454);">&nbsp;</span
></td><td id="454"><a href="#454">454</a></td></tr
><tr id="gr_svn70_455"

 onmouseover="gutterOver(455)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',455);">&nbsp;</span
></td><td id="455"><a href="#455">455</a></td></tr
><tr id="gr_svn70_456"

 onmouseover="gutterOver(456)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',456);">&nbsp;</span
></td><td id="456"><a href="#456">456</a></td></tr
><tr id="gr_svn70_457"

 onmouseover="gutterOver(457)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',457);">&nbsp;</span
></td><td id="457"><a href="#457">457</a></td></tr
><tr id="gr_svn70_458"

 onmouseover="gutterOver(458)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',458);">&nbsp;</span
></td><td id="458"><a href="#458">458</a></td></tr
><tr id="gr_svn70_459"

 onmouseover="gutterOver(459)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',459);">&nbsp;</span
></td><td id="459"><a href="#459">459</a></td></tr
><tr id="gr_svn70_460"

 onmouseover="gutterOver(460)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',460);">&nbsp;</span
></td><td id="460"><a href="#460">460</a></td></tr
><tr id="gr_svn70_461"

 onmouseover="gutterOver(461)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',461);">&nbsp;</span
></td><td id="461"><a href="#461">461</a></td></tr
><tr id="gr_svn70_462"

 onmouseover="gutterOver(462)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',462);">&nbsp;</span
></td><td id="462"><a href="#462">462</a></td></tr
><tr id="gr_svn70_463"

 onmouseover="gutterOver(463)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',463);">&nbsp;</span
></td><td id="463"><a href="#463">463</a></td></tr
><tr id="gr_svn70_464"

 onmouseover="gutterOver(464)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',464);">&nbsp;</span
></td><td id="464"><a href="#464">464</a></td></tr
><tr id="gr_svn70_465"

 onmouseover="gutterOver(465)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',465);">&nbsp;</span
></td><td id="465"><a href="#465">465</a></td></tr
><tr id="gr_svn70_466"

 onmouseover="gutterOver(466)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',466);">&nbsp;</span
></td><td id="466"><a href="#466">466</a></td></tr
><tr id="gr_svn70_467"

 onmouseover="gutterOver(467)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',467);">&nbsp;</span
></td><td id="467"><a href="#467">467</a></td></tr
><tr id="gr_svn70_468"

 onmouseover="gutterOver(468)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',468);">&nbsp;</span
></td><td id="468"><a href="#468">468</a></td></tr
><tr id="gr_svn70_469"

 onmouseover="gutterOver(469)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',469);">&nbsp;</span
></td><td id="469"><a href="#469">469</a></td></tr
><tr id="gr_svn70_470"

 onmouseover="gutterOver(470)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',470);">&nbsp;</span
></td><td id="470"><a href="#470">470</a></td></tr
><tr id="gr_svn70_471"

 onmouseover="gutterOver(471)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',471);">&nbsp;</span
></td><td id="471"><a href="#471">471</a></td></tr
><tr id="gr_svn70_472"

 onmouseover="gutterOver(472)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',472);">&nbsp;</span
></td><td id="472"><a href="#472">472</a></td></tr
><tr id="gr_svn70_473"

 onmouseover="gutterOver(473)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',473);">&nbsp;</span
></td><td id="473"><a href="#473">473</a></td></tr
><tr id="gr_svn70_474"

 onmouseover="gutterOver(474)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',474);">&nbsp;</span
></td><td id="474"><a href="#474">474</a></td></tr
><tr id="gr_svn70_475"

 onmouseover="gutterOver(475)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',475);">&nbsp;</span
></td><td id="475"><a href="#475">475</a></td></tr
><tr id="gr_svn70_476"

 onmouseover="gutterOver(476)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',476);">&nbsp;</span
></td><td id="476"><a href="#476">476</a></td></tr
><tr id="gr_svn70_477"

 onmouseover="gutterOver(477)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',477);">&nbsp;</span
></td><td id="477"><a href="#477">477</a></td></tr
><tr id="gr_svn70_478"

 onmouseover="gutterOver(478)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',478);">&nbsp;</span
></td><td id="478"><a href="#478">478</a></td></tr
><tr id="gr_svn70_479"

 onmouseover="gutterOver(479)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',479);">&nbsp;</span
></td><td id="479"><a href="#479">479</a></td></tr
><tr id="gr_svn70_480"

 onmouseover="gutterOver(480)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',480);">&nbsp;</span
></td><td id="480"><a href="#480">480</a></td></tr
><tr id="gr_svn70_481"

 onmouseover="gutterOver(481)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',481);">&nbsp;</span
></td><td id="481"><a href="#481">481</a></td></tr
><tr id="gr_svn70_482"

 onmouseover="gutterOver(482)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',482);">&nbsp;</span
></td><td id="482"><a href="#482">482</a></td></tr
><tr id="gr_svn70_483"

 onmouseover="gutterOver(483)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',483);">&nbsp;</span
></td><td id="483"><a href="#483">483</a></td></tr
><tr id="gr_svn70_484"

 onmouseover="gutterOver(484)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',484);">&nbsp;</span
></td><td id="484"><a href="#484">484</a></td></tr
><tr id="gr_svn70_485"

 onmouseover="gutterOver(485)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',485);">&nbsp;</span
></td><td id="485"><a href="#485">485</a></td></tr
><tr id="gr_svn70_486"

 onmouseover="gutterOver(486)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',486);">&nbsp;</span
></td><td id="486"><a href="#486">486</a></td></tr
><tr id="gr_svn70_487"

 onmouseover="gutterOver(487)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',487);">&nbsp;</span
></td><td id="487"><a href="#487">487</a></td></tr
><tr id="gr_svn70_488"

 onmouseover="gutterOver(488)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',488);">&nbsp;</span
></td><td id="488"><a href="#488">488</a></td></tr
><tr id="gr_svn70_489"

 onmouseover="gutterOver(489)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',489);">&nbsp;</span
></td><td id="489"><a href="#489">489</a></td></tr
><tr id="gr_svn70_490"

 onmouseover="gutterOver(490)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',490);">&nbsp;</span
></td><td id="490"><a href="#490">490</a></td></tr
><tr id="gr_svn70_491"

 onmouseover="gutterOver(491)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',491);">&nbsp;</span
></td><td id="491"><a href="#491">491</a></td></tr
><tr id="gr_svn70_492"

 onmouseover="gutterOver(492)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',492);">&nbsp;</span
></td><td id="492"><a href="#492">492</a></td></tr
><tr id="gr_svn70_493"

 onmouseover="gutterOver(493)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',493);">&nbsp;</span
></td><td id="493"><a href="#493">493</a></td></tr
><tr id="gr_svn70_494"

 onmouseover="gutterOver(494)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',494);">&nbsp;</span
></td><td id="494"><a href="#494">494</a></td></tr
><tr id="gr_svn70_495"

 onmouseover="gutterOver(495)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',495);">&nbsp;</span
></td><td id="495"><a href="#495">495</a></td></tr
><tr id="gr_svn70_496"

 onmouseover="gutterOver(496)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',496);">&nbsp;</span
></td><td id="496"><a href="#496">496</a></td></tr
><tr id="gr_svn70_497"

 onmouseover="gutterOver(497)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',497);">&nbsp;</span
></td><td id="497"><a href="#497">497</a></td></tr
><tr id="gr_svn70_498"

 onmouseover="gutterOver(498)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',498);">&nbsp;</span
></td><td id="498"><a href="#498">498</a></td></tr
><tr id="gr_svn70_499"

 onmouseover="gutterOver(499)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',499);">&nbsp;</span
></td><td id="499"><a href="#499">499</a></td></tr
><tr id="gr_svn70_500"

 onmouseover="gutterOver(500)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',500);">&nbsp;</span
></td><td id="500"><a href="#500">500</a></td></tr
><tr id="gr_svn70_501"

 onmouseover="gutterOver(501)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',501);">&nbsp;</span
></td><td id="501"><a href="#501">501</a></td></tr
><tr id="gr_svn70_502"

 onmouseover="gutterOver(502)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',502);">&nbsp;</span
></td><td id="502"><a href="#502">502</a></td></tr
><tr id="gr_svn70_503"

 onmouseover="gutterOver(503)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',503);">&nbsp;</span
></td><td id="503"><a href="#503">503</a></td></tr
><tr id="gr_svn70_504"

 onmouseover="gutterOver(504)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',504);">&nbsp;</span
></td><td id="504"><a href="#504">504</a></td></tr
><tr id="gr_svn70_505"

 onmouseover="gutterOver(505)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',505);">&nbsp;</span
></td><td id="505"><a href="#505">505</a></td></tr
><tr id="gr_svn70_506"

 onmouseover="gutterOver(506)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',506);">&nbsp;</span
></td><td id="506"><a href="#506">506</a></td></tr
><tr id="gr_svn70_507"

 onmouseover="gutterOver(507)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',507);">&nbsp;</span
></td><td id="507"><a href="#507">507</a></td></tr
><tr id="gr_svn70_508"

 onmouseover="gutterOver(508)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',508);">&nbsp;</span
></td><td id="508"><a href="#508">508</a></td></tr
><tr id="gr_svn70_509"

 onmouseover="gutterOver(509)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',509);">&nbsp;</span
></td><td id="509"><a href="#509">509</a></td></tr
><tr id="gr_svn70_510"

 onmouseover="gutterOver(510)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',510);">&nbsp;</span
></td><td id="510"><a href="#510">510</a></td></tr
><tr id="gr_svn70_511"

 onmouseover="gutterOver(511)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',511);">&nbsp;</span
></td><td id="511"><a href="#511">511</a></td></tr
><tr id="gr_svn70_512"

 onmouseover="gutterOver(512)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',512);">&nbsp;</span
></td><td id="512"><a href="#512">512</a></td></tr
><tr id="gr_svn70_513"

 onmouseover="gutterOver(513)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',513);">&nbsp;</span
></td><td id="513"><a href="#513">513</a></td></tr
><tr id="gr_svn70_514"

 onmouseover="gutterOver(514)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',514);">&nbsp;</span
></td><td id="514"><a href="#514">514</a></td></tr
><tr id="gr_svn70_515"

 onmouseover="gutterOver(515)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',515);">&nbsp;</span
></td><td id="515"><a href="#515">515</a></td></tr
><tr id="gr_svn70_516"

 onmouseover="gutterOver(516)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',516);">&nbsp;</span
></td><td id="516"><a href="#516">516</a></td></tr
><tr id="gr_svn70_517"

 onmouseover="gutterOver(517)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',517);">&nbsp;</span
></td><td id="517"><a href="#517">517</a></td></tr
><tr id="gr_svn70_518"

 onmouseover="gutterOver(518)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',518);">&nbsp;</span
></td><td id="518"><a href="#518">518</a></td></tr
><tr id="gr_svn70_519"

 onmouseover="gutterOver(519)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',519);">&nbsp;</span
></td><td id="519"><a href="#519">519</a></td></tr
><tr id="gr_svn70_520"

 onmouseover="gutterOver(520)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',520);">&nbsp;</span
></td><td id="520"><a href="#520">520</a></td></tr
><tr id="gr_svn70_521"

 onmouseover="gutterOver(521)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',521);">&nbsp;</span
></td><td id="521"><a href="#521">521</a></td></tr
><tr id="gr_svn70_522"

 onmouseover="gutterOver(522)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',522);">&nbsp;</span
></td><td id="522"><a href="#522">522</a></td></tr
><tr id="gr_svn70_523"

 onmouseover="gutterOver(523)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',523);">&nbsp;</span
></td><td id="523"><a href="#523">523</a></td></tr
><tr id="gr_svn70_524"

 onmouseover="gutterOver(524)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',524);">&nbsp;</span
></td><td id="524"><a href="#524">524</a></td></tr
><tr id="gr_svn70_525"

 onmouseover="gutterOver(525)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',525);">&nbsp;</span
></td><td id="525"><a href="#525">525</a></td></tr
><tr id="gr_svn70_526"

 onmouseover="gutterOver(526)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',526);">&nbsp;</span
></td><td id="526"><a href="#526">526</a></td></tr
><tr id="gr_svn70_527"

 onmouseover="gutterOver(527)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',527);">&nbsp;</span
></td><td id="527"><a href="#527">527</a></td></tr
><tr id="gr_svn70_528"

 onmouseover="gutterOver(528)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',528);">&nbsp;</span
></td><td id="528"><a href="#528">528</a></td></tr
><tr id="gr_svn70_529"

 onmouseover="gutterOver(529)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',529);">&nbsp;</span
></td><td id="529"><a href="#529">529</a></td></tr
><tr id="gr_svn70_530"

 onmouseover="gutterOver(530)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',530);">&nbsp;</span
></td><td id="530"><a href="#530">530</a></td></tr
><tr id="gr_svn70_531"

 onmouseover="gutterOver(531)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',531);">&nbsp;</span
></td><td id="531"><a href="#531">531</a></td></tr
><tr id="gr_svn70_532"

 onmouseover="gutterOver(532)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',532);">&nbsp;</span
></td><td id="532"><a href="#532">532</a></td></tr
><tr id="gr_svn70_533"

 onmouseover="gutterOver(533)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',533);">&nbsp;</span
></td><td id="533"><a href="#533">533</a></td></tr
><tr id="gr_svn70_534"

 onmouseover="gutterOver(534)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',534);">&nbsp;</span
></td><td id="534"><a href="#534">534</a></td></tr
><tr id="gr_svn70_535"

 onmouseover="gutterOver(535)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',535);">&nbsp;</span
></td><td id="535"><a href="#535">535</a></td></tr
><tr id="gr_svn70_536"

 onmouseover="gutterOver(536)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',536);">&nbsp;</span
></td><td id="536"><a href="#536">536</a></td></tr
><tr id="gr_svn70_537"

 onmouseover="gutterOver(537)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',537);">&nbsp;</span
></td><td id="537"><a href="#537">537</a></td></tr
><tr id="gr_svn70_538"

 onmouseover="gutterOver(538)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',538);">&nbsp;</span
></td><td id="538"><a href="#538">538</a></td></tr
><tr id="gr_svn70_539"

 onmouseover="gutterOver(539)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',539);">&nbsp;</span
></td><td id="539"><a href="#539">539</a></td></tr
><tr id="gr_svn70_540"

 onmouseover="gutterOver(540)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',540);">&nbsp;</span
></td><td id="540"><a href="#540">540</a></td></tr
><tr id="gr_svn70_541"

 onmouseover="gutterOver(541)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',541);">&nbsp;</span
></td><td id="541"><a href="#541">541</a></td></tr
><tr id="gr_svn70_542"

 onmouseover="gutterOver(542)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',542);">&nbsp;</span
></td><td id="542"><a href="#542">542</a></td></tr
><tr id="gr_svn70_543"

 onmouseover="gutterOver(543)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',543);">&nbsp;</span
></td><td id="543"><a href="#543">543</a></td></tr
><tr id="gr_svn70_544"

 onmouseover="gutterOver(544)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',544);">&nbsp;</span
></td><td id="544"><a href="#544">544</a></td></tr
><tr id="gr_svn70_545"

 onmouseover="gutterOver(545)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',545);">&nbsp;</span
></td><td id="545"><a href="#545">545</a></td></tr
><tr id="gr_svn70_546"

 onmouseover="gutterOver(546)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',546);">&nbsp;</span
></td><td id="546"><a href="#546">546</a></td></tr
><tr id="gr_svn70_547"

 onmouseover="gutterOver(547)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',547);">&nbsp;</span
></td><td id="547"><a href="#547">547</a></td></tr
><tr id="gr_svn70_548"

 onmouseover="gutterOver(548)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',548);">&nbsp;</span
></td><td id="548"><a href="#548">548</a></td></tr
><tr id="gr_svn70_549"

 onmouseover="gutterOver(549)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',549);">&nbsp;</span
></td><td id="549"><a href="#549">549</a></td></tr
><tr id="gr_svn70_550"

 onmouseover="gutterOver(550)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',550);">&nbsp;</span
></td><td id="550"><a href="#550">550</a></td></tr
><tr id="gr_svn70_551"

 onmouseover="gutterOver(551)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',551);">&nbsp;</span
></td><td id="551"><a href="#551">551</a></td></tr
><tr id="gr_svn70_552"

 onmouseover="gutterOver(552)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',552);">&nbsp;</span
></td><td id="552"><a href="#552">552</a></td></tr
><tr id="gr_svn70_553"

 onmouseover="gutterOver(553)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',553);">&nbsp;</span
></td><td id="553"><a href="#553">553</a></td></tr
><tr id="gr_svn70_554"

 onmouseover="gutterOver(554)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',554);">&nbsp;</span
></td><td id="554"><a href="#554">554</a></td></tr
><tr id="gr_svn70_555"

 onmouseover="gutterOver(555)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',555);">&nbsp;</span
></td><td id="555"><a href="#555">555</a></td></tr
><tr id="gr_svn70_556"

 onmouseover="gutterOver(556)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',556);">&nbsp;</span
></td><td id="556"><a href="#556">556</a></td></tr
><tr id="gr_svn70_557"

 onmouseover="gutterOver(557)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',557);">&nbsp;</span
></td><td id="557"><a href="#557">557</a></td></tr
><tr id="gr_svn70_558"

 onmouseover="gutterOver(558)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',558);">&nbsp;</span
></td><td id="558"><a href="#558">558</a></td></tr
><tr id="gr_svn70_559"

 onmouseover="gutterOver(559)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',559);">&nbsp;</span
></td><td id="559"><a href="#559">559</a></td></tr
><tr id="gr_svn70_560"

 onmouseover="gutterOver(560)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',560);">&nbsp;</span
></td><td id="560"><a href="#560">560</a></td></tr
><tr id="gr_svn70_561"

 onmouseover="gutterOver(561)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',561);">&nbsp;</span
></td><td id="561"><a href="#561">561</a></td></tr
><tr id="gr_svn70_562"

 onmouseover="gutterOver(562)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',562);">&nbsp;</span
></td><td id="562"><a href="#562">562</a></td></tr
><tr id="gr_svn70_563"

 onmouseover="gutterOver(563)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',563);">&nbsp;</span
></td><td id="563"><a href="#563">563</a></td></tr
><tr id="gr_svn70_564"

 onmouseover="gutterOver(564)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',564);">&nbsp;</span
></td><td id="564"><a href="#564">564</a></td></tr
><tr id="gr_svn70_565"

 onmouseover="gutterOver(565)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',565);">&nbsp;</span
></td><td id="565"><a href="#565">565</a></td></tr
><tr id="gr_svn70_566"

 onmouseover="gutterOver(566)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',566);">&nbsp;</span
></td><td id="566"><a href="#566">566</a></td></tr
><tr id="gr_svn70_567"

 onmouseover="gutterOver(567)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',567);">&nbsp;</span
></td><td id="567"><a href="#567">567</a></td></tr
><tr id="gr_svn70_568"

 onmouseover="gutterOver(568)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',568);">&nbsp;</span
></td><td id="568"><a href="#568">568</a></td></tr
><tr id="gr_svn70_569"

 onmouseover="gutterOver(569)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',569);">&nbsp;</span
></td><td id="569"><a href="#569">569</a></td></tr
><tr id="gr_svn70_570"

 onmouseover="gutterOver(570)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',570);">&nbsp;</span
></td><td id="570"><a href="#570">570</a></td></tr
><tr id="gr_svn70_571"

 onmouseover="gutterOver(571)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',571);">&nbsp;</span
></td><td id="571"><a href="#571">571</a></td></tr
><tr id="gr_svn70_572"

 onmouseover="gutterOver(572)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',572);">&nbsp;</span
></td><td id="572"><a href="#572">572</a></td></tr
><tr id="gr_svn70_573"

 onmouseover="gutterOver(573)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',573);">&nbsp;</span
></td><td id="573"><a href="#573">573</a></td></tr
><tr id="gr_svn70_574"

 onmouseover="gutterOver(574)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',574);">&nbsp;</span
></td><td id="574"><a href="#574">574</a></td></tr
><tr id="gr_svn70_575"

 onmouseover="gutterOver(575)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',575);">&nbsp;</span
></td><td id="575"><a href="#575">575</a></td></tr
><tr id="gr_svn70_576"

 onmouseover="gutterOver(576)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',576);">&nbsp;</span
></td><td id="576"><a href="#576">576</a></td></tr
><tr id="gr_svn70_577"

 onmouseover="gutterOver(577)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',577);">&nbsp;</span
></td><td id="577"><a href="#577">577</a></td></tr
><tr id="gr_svn70_578"

 onmouseover="gutterOver(578)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',578);">&nbsp;</span
></td><td id="578"><a href="#578">578</a></td></tr
><tr id="gr_svn70_579"

 onmouseover="gutterOver(579)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',579);">&nbsp;</span
></td><td id="579"><a href="#579">579</a></td></tr
><tr id="gr_svn70_580"

 onmouseover="gutterOver(580)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',580);">&nbsp;</span
></td><td id="580"><a href="#580">580</a></td></tr
><tr id="gr_svn70_581"

 onmouseover="gutterOver(581)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',581);">&nbsp;</span
></td><td id="581"><a href="#581">581</a></td></tr
><tr id="gr_svn70_582"

 onmouseover="gutterOver(582)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',582);">&nbsp;</span
></td><td id="582"><a href="#582">582</a></td></tr
><tr id="gr_svn70_583"

 onmouseover="gutterOver(583)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',583);">&nbsp;</span
></td><td id="583"><a href="#583">583</a></td></tr
><tr id="gr_svn70_584"

 onmouseover="gutterOver(584)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',584);">&nbsp;</span
></td><td id="584"><a href="#584">584</a></td></tr
><tr id="gr_svn70_585"

 onmouseover="gutterOver(585)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',585);">&nbsp;</span
></td><td id="585"><a href="#585">585</a></td></tr
><tr id="gr_svn70_586"

 onmouseover="gutterOver(586)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',586);">&nbsp;</span
></td><td id="586"><a href="#586">586</a></td></tr
><tr id="gr_svn70_587"

 onmouseover="gutterOver(587)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',587);">&nbsp;</span
></td><td id="587"><a href="#587">587</a></td></tr
><tr id="gr_svn70_588"

 onmouseover="gutterOver(588)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',588);">&nbsp;</span
></td><td id="588"><a href="#588">588</a></td></tr
><tr id="gr_svn70_589"

 onmouseover="gutterOver(589)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',589);">&nbsp;</span
></td><td id="589"><a href="#589">589</a></td></tr
><tr id="gr_svn70_590"

 onmouseover="gutterOver(590)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',590);">&nbsp;</span
></td><td id="590"><a href="#590">590</a></td></tr
><tr id="gr_svn70_591"

 onmouseover="gutterOver(591)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',591);">&nbsp;</span
></td><td id="591"><a href="#591">591</a></td></tr
><tr id="gr_svn70_592"

 onmouseover="gutterOver(592)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',592);">&nbsp;</span
></td><td id="592"><a href="#592">592</a></td></tr
><tr id="gr_svn70_593"

 onmouseover="gutterOver(593)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',593);">&nbsp;</span
></td><td id="593"><a href="#593">593</a></td></tr
><tr id="gr_svn70_594"

 onmouseover="gutterOver(594)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',594);">&nbsp;</span
></td><td id="594"><a href="#594">594</a></td></tr
><tr id="gr_svn70_595"

 onmouseover="gutterOver(595)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',595);">&nbsp;</span
></td><td id="595"><a href="#595">595</a></td></tr
><tr id="gr_svn70_596"

 onmouseover="gutterOver(596)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',596);">&nbsp;</span
></td><td id="596"><a href="#596">596</a></td></tr
><tr id="gr_svn70_597"

 onmouseover="gutterOver(597)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',597);">&nbsp;</span
></td><td id="597"><a href="#597">597</a></td></tr
><tr id="gr_svn70_598"

 onmouseover="gutterOver(598)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',598);">&nbsp;</span
></td><td id="598"><a href="#598">598</a></td></tr
><tr id="gr_svn70_599"

 onmouseover="gutterOver(599)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',599);">&nbsp;</span
></td><td id="599"><a href="#599">599</a></td></tr
><tr id="gr_svn70_600"

 onmouseover="gutterOver(600)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',600);">&nbsp;</span
></td><td id="600"><a href="#600">600</a></td></tr
><tr id="gr_svn70_601"

 onmouseover="gutterOver(601)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',601);">&nbsp;</span
></td><td id="601"><a href="#601">601</a></td></tr
><tr id="gr_svn70_602"

 onmouseover="gutterOver(602)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',602);">&nbsp;</span
></td><td id="602"><a href="#602">602</a></td></tr
><tr id="gr_svn70_603"

 onmouseover="gutterOver(603)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',603);">&nbsp;</span
></td><td id="603"><a href="#603">603</a></td></tr
><tr id="gr_svn70_604"

 onmouseover="gutterOver(604)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',604);">&nbsp;</span
></td><td id="604"><a href="#604">604</a></td></tr
><tr id="gr_svn70_605"

 onmouseover="gutterOver(605)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',605);">&nbsp;</span
></td><td id="605"><a href="#605">605</a></td></tr
><tr id="gr_svn70_606"

 onmouseover="gutterOver(606)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',606);">&nbsp;</span
></td><td id="606"><a href="#606">606</a></td></tr
><tr id="gr_svn70_607"

 onmouseover="gutterOver(607)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',607);">&nbsp;</span
></td><td id="607"><a href="#607">607</a></td></tr
><tr id="gr_svn70_608"

 onmouseover="gutterOver(608)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',608);">&nbsp;</span
></td><td id="608"><a href="#608">608</a></td></tr
><tr id="gr_svn70_609"

 onmouseover="gutterOver(609)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',609);">&nbsp;</span
></td><td id="609"><a href="#609">609</a></td></tr
><tr id="gr_svn70_610"

 onmouseover="gutterOver(610)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',610);">&nbsp;</span
></td><td id="610"><a href="#610">610</a></td></tr
><tr id="gr_svn70_611"

 onmouseover="gutterOver(611)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',611);">&nbsp;</span
></td><td id="611"><a href="#611">611</a></td></tr
><tr id="gr_svn70_612"

 onmouseover="gutterOver(612)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',612);">&nbsp;</span
></td><td id="612"><a href="#612">612</a></td></tr
><tr id="gr_svn70_613"

 onmouseover="gutterOver(613)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',613);">&nbsp;</span
></td><td id="613"><a href="#613">613</a></td></tr
><tr id="gr_svn70_614"

 onmouseover="gutterOver(614)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',614);">&nbsp;</span
></td><td id="614"><a href="#614">614</a></td></tr
><tr id="gr_svn70_615"

 onmouseover="gutterOver(615)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',615);">&nbsp;</span
></td><td id="615"><a href="#615">615</a></td></tr
><tr id="gr_svn70_616"

 onmouseover="gutterOver(616)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',616);">&nbsp;</span
></td><td id="616"><a href="#616">616</a></td></tr
><tr id="gr_svn70_617"

 onmouseover="gutterOver(617)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',617);">&nbsp;</span
></td><td id="617"><a href="#617">617</a></td></tr
><tr id="gr_svn70_618"

 onmouseover="gutterOver(618)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',618);">&nbsp;</span
></td><td id="618"><a href="#618">618</a></td></tr
><tr id="gr_svn70_619"

 onmouseover="gutterOver(619)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',619);">&nbsp;</span
></td><td id="619"><a href="#619">619</a></td></tr
><tr id="gr_svn70_620"

 onmouseover="gutterOver(620)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',620);">&nbsp;</span
></td><td id="620"><a href="#620">620</a></td></tr
><tr id="gr_svn70_621"

 onmouseover="gutterOver(621)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',621);">&nbsp;</span
></td><td id="621"><a href="#621">621</a></td></tr
><tr id="gr_svn70_622"

 onmouseover="gutterOver(622)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',622);">&nbsp;</span
></td><td id="622"><a href="#622">622</a></td></tr
><tr id="gr_svn70_623"

 onmouseover="gutterOver(623)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',623);">&nbsp;</span
></td><td id="623"><a href="#623">623</a></td></tr
><tr id="gr_svn70_624"

 onmouseover="gutterOver(624)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',624);">&nbsp;</span
></td><td id="624"><a href="#624">624</a></td></tr
><tr id="gr_svn70_625"

 onmouseover="gutterOver(625)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',625);">&nbsp;</span
></td><td id="625"><a href="#625">625</a></td></tr
><tr id="gr_svn70_626"

 onmouseover="gutterOver(626)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',626);">&nbsp;</span
></td><td id="626"><a href="#626">626</a></td></tr
><tr id="gr_svn70_627"

 onmouseover="gutterOver(627)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',627);">&nbsp;</span
></td><td id="627"><a href="#627">627</a></td></tr
><tr id="gr_svn70_628"

 onmouseover="gutterOver(628)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',628);">&nbsp;</span
></td><td id="628"><a href="#628">628</a></td></tr
><tr id="gr_svn70_629"

 onmouseover="gutterOver(629)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',629);">&nbsp;</span
></td><td id="629"><a href="#629">629</a></td></tr
><tr id="gr_svn70_630"

 onmouseover="gutterOver(630)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',630);">&nbsp;</span
></td><td id="630"><a href="#630">630</a></td></tr
><tr id="gr_svn70_631"

 onmouseover="gutterOver(631)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',631);">&nbsp;</span
></td><td id="631"><a href="#631">631</a></td></tr
><tr id="gr_svn70_632"

 onmouseover="gutterOver(632)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',632);">&nbsp;</span
></td><td id="632"><a href="#632">632</a></td></tr
><tr id="gr_svn70_633"

 onmouseover="gutterOver(633)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',633);">&nbsp;</span
></td><td id="633"><a href="#633">633</a></td></tr
><tr id="gr_svn70_634"

 onmouseover="gutterOver(634)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',634);">&nbsp;</span
></td><td id="634"><a href="#634">634</a></td></tr
><tr id="gr_svn70_635"

 onmouseover="gutterOver(635)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',635);">&nbsp;</span
></td><td id="635"><a href="#635">635</a></td></tr
><tr id="gr_svn70_636"

 onmouseover="gutterOver(636)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',636);">&nbsp;</span
></td><td id="636"><a href="#636">636</a></td></tr
><tr id="gr_svn70_637"

 onmouseover="gutterOver(637)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',637);">&nbsp;</span
></td><td id="637"><a href="#637">637</a></td></tr
><tr id="gr_svn70_638"

 onmouseover="gutterOver(638)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',638);">&nbsp;</span
></td><td id="638"><a href="#638">638</a></td></tr
><tr id="gr_svn70_639"

 onmouseover="gutterOver(639)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',639);">&nbsp;</span
></td><td id="639"><a href="#639">639</a></td></tr
><tr id="gr_svn70_640"

 onmouseover="gutterOver(640)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',640);">&nbsp;</span
></td><td id="640"><a href="#640">640</a></td></tr
><tr id="gr_svn70_641"

 onmouseover="gutterOver(641)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',641);">&nbsp;</span
></td><td id="641"><a href="#641">641</a></td></tr
><tr id="gr_svn70_642"

 onmouseover="gutterOver(642)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',642);">&nbsp;</span
></td><td id="642"><a href="#642">642</a></td></tr
><tr id="gr_svn70_643"

 onmouseover="gutterOver(643)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',643);">&nbsp;</span
></td><td id="643"><a href="#643">643</a></td></tr
><tr id="gr_svn70_644"

 onmouseover="gutterOver(644)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',644);">&nbsp;</span
></td><td id="644"><a href="#644">644</a></td></tr
><tr id="gr_svn70_645"

 onmouseover="gutterOver(645)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',645);">&nbsp;</span
></td><td id="645"><a href="#645">645</a></td></tr
><tr id="gr_svn70_646"

 onmouseover="gutterOver(646)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',646);">&nbsp;</span
></td><td id="646"><a href="#646">646</a></td></tr
><tr id="gr_svn70_647"

 onmouseover="gutterOver(647)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',647);">&nbsp;</span
></td><td id="647"><a href="#647">647</a></td></tr
><tr id="gr_svn70_648"

 onmouseover="gutterOver(648)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',648);">&nbsp;</span
></td><td id="648"><a href="#648">648</a></td></tr
><tr id="gr_svn70_649"

 onmouseover="gutterOver(649)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',649);">&nbsp;</span
></td><td id="649"><a href="#649">649</a></td></tr
><tr id="gr_svn70_650"

 onmouseover="gutterOver(650)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',650);">&nbsp;</span
></td><td id="650"><a href="#650">650</a></td></tr
><tr id="gr_svn70_651"

 onmouseover="gutterOver(651)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',651);">&nbsp;</span
></td><td id="651"><a href="#651">651</a></td></tr
><tr id="gr_svn70_652"

 onmouseover="gutterOver(652)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',652);">&nbsp;</span
></td><td id="652"><a href="#652">652</a></td></tr
><tr id="gr_svn70_653"

 onmouseover="gutterOver(653)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',653);">&nbsp;</span
></td><td id="653"><a href="#653">653</a></td></tr
><tr id="gr_svn70_654"

 onmouseover="gutterOver(654)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',654);">&nbsp;</span
></td><td id="654"><a href="#654">654</a></td></tr
><tr id="gr_svn70_655"

 onmouseover="gutterOver(655)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',655);">&nbsp;</span
></td><td id="655"><a href="#655">655</a></td></tr
><tr id="gr_svn70_656"

 onmouseover="gutterOver(656)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',656);">&nbsp;</span
></td><td id="656"><a href="#656">656</a></td></tr
><tr id="gr_svn70_657"

 onmouseover="gutterOver(657)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',657);">&nbsp;</span
></td><td id="657"><a href="#657">657</a></td></tr
><tr id="gr_svn70_658"

 onmouseover="gutterOver(658)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',658);">&nbsp;</span
></td><td id="658"><a href="#658">658</a></td></tr
><tr id="gr_svn70_659"

 onmouseover="gutterOver(659)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',659);">&nbsp;</span
></td><td id="659"><a href="#659">659</a></td></tr
><tr id="gr_svn70_660"

 onmouseover="gutterOver(660)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',660);">&nbsp;</span
></td><td id="660"><a href="#660">660</a></td></tr
><tr id="gr_svn70_661"

 onmouseover="gutterOver(661)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',661);">&nbsp;</span
></td><td id="661"><a href="#661">661</a></td></tr
><tr id="gr_svn70_662"

 onmouseover="gutterOver(662)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',662);">&nbsp;</span
></td><td id="662"><a href="#662">662</a></td></tr
><tr id="gr_svn70_663"

 onmouseover="gutterOver(663)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',663);">&nbsp;</span
></td><td id="663"><a href="#663">663</a></td></tr
><tr id="gr_svn70_664"

 onmouseover="gutterOver(664)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',664);">&nbsp;</span
></td><td id="664"><a href="#664">664</a></td></tr
><tr id="gr_svn70_665"

 onmouseover="gutterOver(665)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',665);">&nbsp;</span
></td><td id="665"><a href="#665">665</a></td></tr
><tr id="gr_svn70_666"

 onmouseover="gutterOver(666)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',666);">&nbsp;</span
></td><td id="666"><a href="#666">666</a></td></tr
><tr id="gr_svn70_667"

 onmouseover="gutterOver(667)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',667);">&nbsp;</span
></td><td id="667"><a href="#667">667</a></td></tr
><tr id="gr_svn70_668"

 onmouseover="gutterOver(668)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',668);">&nbsp;</span
></td><td id="668"><a href="#668">668</a></td></tr
><tr id="gr_svn70_669"

 onmouseover="gutterOver(669)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',669);">&nbsp;</span
></td><td id="669"><a href="#669">669</a></td></tr
><tr id="gr_svn70_670"

 onmouseover="gutterOver(670)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',670);">&nbsp;</span
></td><td id="670"><a href="#670">670</a></td></tr
><tr id="gr_svn70_671"

 onmouseover="gutterOver(671)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',671);">&nbsp;</span
></td><td id="671"><a href="#671">671</a></td></tr
><tr id="gr_svn70_672"

 onmouseover="gutterOver(672)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',672);">&nbsp;</span
></td><td id="672"><a href="#672">672</a></td></tr
><tr id="gr_svn70_673"

 onmouseover="gutterOver(673)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',673);">&nbsp;</span
></td><td id="673"><a href="#673">673</a></td></tr
><tr id="gr_svn70_674"

 onmouseover="gutterOver(674)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',674);">&nbsp;</span
></td><td id="674"><a href="#674">674</a></td></tr
><tr id="gr_svn70_675"

 onmouseover="gutterOver(675)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',675);">&nbsp;</span
></td><td id="675"><a href="#675">675</a></td></tr
><tr id="gr_svn70_676"

 onmouseover="gutterOver(676)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',676);">&nbsp;</span
></td><td id="676"><a href="#676">676</a></td></tr
><tr id="gr_svn70_677"

 onmouseover="gutterOver(677)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',677);">&nbsp;</span
></td><td id="677"><a href="#677">677</a></td></tr
><tr id="gr_svn70_678"

 onmouseover="gutterOver(678)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',678);">&nbsp;</span
></td><td id="678"><a href="#678">678</a></td></tr
><tr id="gr_svn70_679"

 onmouseover="gutterOver(679)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',679);">&nbsp;</span
></td><td id="679"><a href="#679">679</a></td></tr
><tr id="gr_svn70_680"

 onmouseover="gutterOver(680)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',680);">&nbsp;</span
></td><td id="680"><a href="#680">680</a></td></tr
><tr id="gr_svn70_681"

 onmouseover="gutterOver(681)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',681);">&nbsp;</span
></td><td id="681"><a href="#681">681</a></td></tr
><tr id="gr_svn70_682"

 onmouseover="gutterOver(682)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',682);">&nbsp;</span
></td><td id="682"><a href="#682">682</a></td></tr
><tr id="gr_svn70_683"

 onmouseover="gutterOver(683)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',683);">&nbsp;</span
></td><td id="683"><a href="#683">683</a></td></tr
><tr id="gr_svn70_684"

 onmouseover="gutterOver(684)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',684);">&nbsp;</span
></td><td id="684"><a href="#684">684</a></td></tr
><tr id="gr_svn70_685"

 onmouseover="gutterOver(685)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',685);">&nbsp;</span
></td><td id="685"><a href="#685">685</a></td></tr
><tr id="gr_svn70_686"

 onmouseover="gutterOver(686)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',686);">&nbsp;</span
></td><td id="686"><a href="#686">686</a></td></tr
><tr id="gr_svn70_687"

 onmouseover="gutterOver(687)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',687);">&nbsp;</span
></td><td id="687"><a href="#687">687</a></td></tr
><tr id="gr_svn70_688"

 onmouseover="gutterOver(688)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',688);">&nbsp;</span
></td><td id="688"><a href="#688">688</a></td></tr
><tr id="gr_svn70_689"

 onmouseover="gutterOver(689)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',689);">&nbsp;</span
></td><td id="689"><a href="#689">689</a></td></tr
><tr id="gr_svn70_690"

 onmouseover="gutterOver(690)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',690);">&nbsp;</span
></td><td id="690"><a href="#690">690</a></td></tr
><tr id="gr_svn70_691"

 onmouseover="gutterOver(691)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',691);">&nbsp;</span
></td><td id="691"><a href="#691">691</a></td></tr
><tr id="gr_svn70_692"

 onmouseover="gutterOver(692)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',692);">&nbsp;</span
></td><td id="692"><a href="#692">692</a></td></tr
><tr id="gr_svn70_693"

 onmouseover="gutterOver(693)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',693);">&nbsp;</span
></td><td id="693"><a href="#693">693</a></td></tr
><tr id="gr_svn70_694"

 onmouseover="gutterOver(694)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',694);">&nbsp;</span
></td><td id="694"><a href="#694">694</a></td></tr
><tr id="gr_svn70_695"

 onmouseover="gutterOver(695)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',695);">&nbsp;</span
></td><td id="695"><a href="#695">695</a></td></tr
><tr id="gr_svn70_696"

 onmouseover="gutterOver(696)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',696);">&nbsp;</span
></td><td id="696"><a href="#696">696</a></td></tr
><tr id="gr_svn70_697"

 onmouseover="gutterOver(697)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',697);">&nbsp;</span
></td><td id="697"><a href="#697">697</a></td></tr
><tr id="gr_svn70_698"

 onmouseover="gutterOver(698)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',698);">&nbsp;</span
></td><td id="698"><a href="#698">698</a></td></tr
><tr id="gr_svn70_699"

 onmouseover="gutterOver(699)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',699);">&nbsp;</span
></td><td id="699"><a href="#699">699</a></td></tr
><tr id="gr_svn70_700"

 onmouseover="gutterOver(700)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',700);">&nbsp;</span
></td><td id="700"><a href="#700">700</a></td></tr
><tr id="gr_svn70_701"

 onmouseover="gutterOver(701)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',701);">&nbsp;</span
></td><td id="701"><a href="#701">701</a></td></tr
><tr id="gr_svn70_702"

 onmouseover="gutterOver(702)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',702);">&nbsp;</span
></td><td id="702"><a href="#702">702</a></td></tr
><tr id="gr_svn70_703"

 onmouseover="gutterOver(703)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',703);">&nbsp;</span
></td><td id="703"><a href="#703">703</a></td></tr
><tr id="gr_svn70_704"

 onmouseover="gutterOver(704)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',704);">&nbsp;</span
></td><td id="704"><a href="#704">704</a></td></tr
><tr id="gr_svn70_705"

 onmouseover="gutterOver(705)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',705);">&nbsp;</span
></td><td id="705"><a href="#705">705</a></td></tr
><tr id="gr_svn70_706"

 onmouseover="gutterOver(706)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',706);">&nbsp;</span
></td><td id="706"><a href="#706">706</a></td></tr
><tr id="gr_svn70_707"

 onmouseover="gutterOver(707)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',707);">&nbsp;</span
></td><td id="707"><a href="#707">707</a></td></tr
><tr id="gr_svn70_708"

 onmouseover="gutterOver(708)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',708);">&nbsp;</span
></td><td id="708"><a href="#708">708</a></td></tr
><tr id="gr_svn70_709"

 onmouseover="gutterOver(709)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',709);">&nbsp;</span
></td><td id="709"><a href="#709">709</a></td></tr
><tr id="gr_svn70_710"

 onmouseover="gutterOver(710)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',710);">&nbsp;</span
></td><td id="710"><a href="#710">710</a></td></tr
><tr id="gr_svn70_711"

 onmouseover="gutterOver(711)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',711);">&nbsp;</span
></td><td id="711"><a href="#711">711</a></td></tr
><tr id="gr_svn70_712"

 onmouseover="gutterOver(712)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',712);">&nbsp;</span
></td><td id="712"><a href="#712">712</a></td></tr
><tr id="gr_svn70_713"

 onmouseover="gutterOver(713)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',713);">&nbsp;</span
></td><td id="713"><a href="#713">713</a></td></tr
><tr id="gr_svn70_714"

 onmouseover="gutterOver(714)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',714);">&nbsp;</span
></td><td id="714"><a href="#714">714</a></td></tr
><tr id="gr_svn70_715"

 onmouseover="gutterOver(715)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',715);">&nbsp;</span
></td><td id="715"><a href="#715">715</a></td></tr
><tr id="gr_svn70_716"

 onmouseover="gutterOver(716)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',716);">&nbsp;</span
></td><td id="716"><a href="#716">716</a></td></tr
><tr id="gr_svn70_717"

 onmouseover="gutterOver(717)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',717);">&nbsp;</span
></td><td id="717"><a href="#717">717</a></td></tr
><tr id="gr_svn70_718"

 onmouseover="gutterOver(718)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',718);">&nbsp;</span
></td><td id="718"><a href="#718">718</a></td></tr
><tr id="gr_svn70_719"

 onmouseover="gutterOver(719)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',719);">&nbsp;</span
></td><td id="719"><a href="#719">719</a></td></tr
><tr id="gr_svn70_720"

 onmouseover="gutterOver(720)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',720);">&nbsp;</span
></td><td id="720"><a href="#720">720</a></td></tr
><tr id="gr_svn70_721"

 onmouseover="gutterOver(721)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',721);">&nbsp;</span
></td><td id="721"><a href="#721">721</a></td></tr
><tr id="gr_svn70_722"

 onmouseover="gutterOver(722)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',722);">&nbsp;</span
></td><td id="722"><a href="#722">722</a></td></tr
><tr id="gr_svn70_723"

 onmouseover="gutterOver(723)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',723);">&nbsp;</span
></td><td id="723"><a href="#723">723</a></td></tr
><tr id="gr_svn70_724"

 onmouseover="gutterOver(724)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',724);">&nbsp;</span
></td><td id="724"><a href="#724">724</a></td></tr
><tr id="gr_svn70_725"

 onmouseover="gutterOver(725)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',725);">&nbsp;</span
></td><td id="725"><a href="#725">725</a></td></tr
><tr id="gr_svn70_726"

 onmouseover="gutterOver(726)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',726);">&nbsp;</span
></td><td id="726"><a href="#726">726</a></td></tr
><tr id="gr_svn70_727"

 onmouseover="gutterOver(727)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',727);">&nbsp;</span
></td><td id="727"><a href="#727">727</a></td></tr
><tr id="gr_svn70_728"

 onmouseover="gutterOver(728)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',728);">&nbsp;</span
></td><td id="728"><a href="#728">728</a></td></tr
><tr id="gr_svn70_729"

 onmouseover="gutterOver(729)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',729);">&nbsp;</span
></td><td id="729"><a href="#729">729</a></td></tr
><tr id="gr_svn70_730"

 onmouseover="gutterOver(730)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',730);">&nbsp;</span
></td><td id="730"><a href="#730">730</a></td></tr
><tr id="gr_svn70_731"

 onmouseover="gutterOver(731)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',731);">&nbsp;</span
></td><td id="731"><a href="#731">731</a></td></tr
><tr id="gr_svn70_732"

 onmouseover="gutterOver(732)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',732);">&nbsp;</span
></td><td id="732"><a href="#732">732</a></td></tr
><tr id="gr_svn70_733"

 onmouseover="gutterOver(733)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',733);">&nbsp;</span
></td><td id="733"><a href="#733">733</a></td></tr
><tr id="gr_svn70_734"

 onmouseover="gutterOver(734)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',734);">&nbsp;</span
></td><td id="734"><a href="#734">734</a></td></tr
><tr id="gr_svn70_735"

 onmouseover="gutterOver(735)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',735);">&nbsp;</span
></td><td id="735"><a href="#735">735</a></td></tr
><tr id="gr_svn70_736"

 onmouseover="gutterOver(736)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',736);">&nbsp;</span
></td><td id="736"><a href="#736">736</a></td></tr
><tr id="gr_svn70_737"

 onmouseover="gutterOver(737)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',737);">&nbsp;</span
></td><td id="737"><a href="#737">737</a></td></tr
><tr id="gr_svn70_738"

 onmouseover="gutterOver(738)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',738);">&nbsp;</span
></td><td id="738"><a href="#738">738</a></td></tr
><tr id="gr_svn70_739"

 onmouseover="gutterOver(739)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',739);">&nbsp;</span
></td><td id="739"><a href="#739">739</a></td></tr
><tr id="gr_svn70_740"

 onmouseover="gutterOver(740)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',740);">&nbsp;</span
></td><td id="740"><a href="#740">740</a></td></tr
><tr id="gr_svn70_741"

 onmouseover="gutterOver(741)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',741);">&nbsp;</span
></td><td id="741"><a href="#741">741</a></td></tr
><tr id="gr_svn70_742"

 onmouseover="gutterOver(742)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',742);">&nbsp;</span
></td><td id="742"><a href="#742">742</a></td></tr
><tr id="gr_svn70_743"

 onmouseover="gutterOver(743)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',743);">&nbsp;</span
></td><td id="743"><a href="#743">743</a></td></tr
><tr id="gr_svn70_744"

 onmouseover="gutterOver(744)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',744);">&nbsp;</span
></td><td id="744"><a href="#744">744</a></td></tr
><tr id="gr_svn70_745"

 onmouseover="gutterOver(745)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',745);">&nbsp;</span
></td><td id="745"><a href="#745">745</a></td></tr
><tr id="gr_svn70_746"

 onmouseover="gutterOver(746)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',746);">&nbsp;</span
></td><td id="746"><a href="#746">746</a></td></tr
><tr id="gr_svn70_747"

 onmouseover="gutterOver(747)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',747);">&nbsp;</span
></td><td id="747"><a href="#747">747</a></td></tr
><tr id="gr_svn70_748"

 onmouseover="gutterOver(748)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',748);">&nbsp;</span
></td><td id="748"><a href="#748">748</a></td></tr
><tr id="gr_svn70_749"

 onmouseover="gutterOver(749)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',749);">&nbsp;</span
></td><td id="749"><a href="#749">749</a></td></tr
><tr id="gr_svn70_750"

 onmouseover="gutterOver(750)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',750);">&nbsp;</span
></td><td id="750"><a href="#750">750</a></td></tr
><tr id="gr_svn70_751"

 onmouseover="gutterOver(751)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',751);">&nbsp;</span
></td><td id="751"><a href="#751">751</a></td></tr
><tr id="gr_svn70_752"

 onmouseover="gutterOver(752)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',752);">&nbsp;</span
></td><td id="752"><a href="#752">752</a></td></tr
><tr id="gr_svn70_753"

 onmouseover="gutterOver(753)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',753);">&nbsp;</span
></td><td id="753"><a href="#753">753</a></td></tr
><tr id="gr_svn70_754"

 onmouseover="gutterOver(754)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',754);">&nbsp;</span
></td><td id="754"><a href="#754">754</a></td></tr
><tr id="gr_svn70_755"

 onmouseover="gutterOver(755)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',755);">&nbsp;</span
></td><td id="755"><a href="#755">755</a></td></tr
><tr id="gr_svn70_756"

 onmouseover="gutterOver(756)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',756);">&nbsp;</span
></td><td id="756"><a href="#756">756</a></td></tr
><tr id="gr_svn70_757"

 onmouseover="gutterOver(757)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',757);">&nbsp;</span
></td><td id="757"><a href="#757">757</a></td></tr
><tr id="gr_svn70_758"

 onmouseover="gutterOver(758)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',758);">&nbsp;</span
></td><td id="758"><a href="#758">758</a></td></tr
><tr id="gr_svn70_759"

 onmouseover="gutterOver(759)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',759);">&nbsp;</span
></td><td id="759"><a href="#759">759</a></td></tr
><tr id="gr_svn70_760"

 onmouseover="gutterOver(760)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',760);">&nbsp;</span
></td><td id="760"><a href="#760">760</a></td></tr
><tr id="gr_svn70_761"

 onmouseover="gutterOver(761)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',761);">&nbsp;</span
></td><td id="761"><a href="#761">761</a></td></tr
><tr id="gr_svn70_762"

 onmouseover="gutterOver(762)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',762);">&nbsp;</span
></td><td id="762"><a href="#762">762</a></td></tr
><tr id="gr_svn70_763"

 onmouseover="gutterOver(763)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',763);">&nbsp;</span
></td><td id="763"><a href="#763">763</a></td></tr
><tr id="gr_svn70_764"

 onmouseover="gutterOver(764)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',764);">&nbsp;</span
></td><td id="764"><a href="#764">764</a></td></tr
><tr id="gr_svn70_765"

 onmouseover="gutterOver(765)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',765);">&nbsp;</span
></td><td id="765"><a href="#765">765</a></td></tr
><tr id="gr_svn70_766"

 onmouseover="gutterOver(766)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',766);">&nbsp;</span
></td><td id="766"><a href="#766">766</a></td></tr
><tr id="gr_svn70_767"

 onmouseover="gutterOver(767)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',767);">&nbsp;</span
></td><td id="767"><a href="#767">767</a></td></tr
><tr id="gr_svn70_768"

 onmouseover="gutterOver(768)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',768);">&nbsp;</span
></td><td id="768"><a href="#768">768</a></td></tr
><tr id="gr_svn70_769"

 onmouseover="gutterOver(769)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',769);">&nbsp;</span
></td><td id="769"><a href="#769">769</a></td></tr
><tr id="gr_svn70_770"

 onmouseover="gutterOver(770)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',770);">&nbsp;</span
></td><td id="770"><a href="#770">770</a></td></tr
><tr id="gr_svn70_771"

 onmouseover="gutterOver(771)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',771);">&nbsp;</span
></td><td id="771"><a href="#771">771</a></td></tr
><tr id="gr_svn70_772"

 onmouseover="gutterOver(772)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',772);">&nbsp;</span
></td><td id="772"><a href="#772">772</a></td></tr
><tr id="gr_svn70_773"

 onmouseover="gutterOver(773)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',773);">&nbsp;</span
></td><td id="773"><a href="#773">773</a></td></tr
><tr id="gr_svn70_774"

 onmouseover="gutterOver(774)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',774);">&nbsp;</span
></td><td id="774"><a href="#774">774</a></td></tr
><tr id="gr_svn70_775"

 onmouseover="gutterOver(775)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',775);">&nbsp;</span
></td><td id="775"><a href="#775">775</a></td></tr
><tr id="gr_svn70_776"

 onmouseover="gutterOver(776)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',776);">&nbsp;</span
></td><td id="776"><a href="#776">776</a></td></tr
><tr id="gr_svn70_777"

 onmouseover="gutterOver(777)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',777);">&nbsp;</span
></td><td id="777"><a href="#777">777</a></td></tr
><tr id="gr_svn70_778"

 onmouseover="gutterOver(778)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',778);">&nbsp;</span
></td><td id="778"><a href="#778">778</a></td></tr
><tr id="gr_svn70_779"

 onmouseover="gutterOver(779)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',779);">&nbsp;</span
></td><td id="779"><a href="#779">779</a></td></tr
><tr id="gr_svn70_780"

 onmouseover="gutterOver(780)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',780);">&nbsp;</span
></td><td id="780"><a href="#780">780</a></td></tr
><tr id="gr_svn70_781"

 onmouseover="gutterOver(781)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',781);">&nbsp;</span
></td><td id="781"><a href="#781">781</a></td></tr
><tr id="gr_svn70_782"

 onmouseover="gutterOver(782)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',782);">&nbsp;</span
></td><td id="782"><a href="#782">782</a></td></tr
><tr id="gr_svn70_783"

 onmouseover="gutterOver(783)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',783);">&nbsp;</span
></td><td id="783"><a href="#783">783</a></td></tr
><tr id="gr_svn70_784"

 onmouseover="gutterOver(784)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',784);">&nbsp;</span
></td><td id="784"><a href="#784">784</a></td></tr
><tr id="gr_svn70_785"

 onmouseover="gutterOver(785)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',785);">&nbsp;</span
></td><td id="785"><a href="#785">785</a></td></tr
><tr id="gr_svn70_786"

 onmouseover="gutterOver(786)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',786);">&nbsp;</span
></td><td id="786"><a href="#786">786</a></td></tr
><tr id="gr_svn70_787"

 onmouseover="gutterOver(787)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',787);">&nbsp;</span
></td><td id="787"><a href="#787">787</a></td></tr
><tr id="gr_svn70_788"

 onmouseover="gutterOver(788)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',788);">&nbsp;</span
></td><td id="788"><a href="#788">788</a></td></tr
><tr id="gr_svn70_789"

 onmouseover="gutterOver(789)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',789);">&nbsp;</span
></td><td id="789"><a href="#789">789</a></td></tr
><tr id="gr_svn70_790"

 onmouseover="gutterOver(790)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',790);">&nbsp;</span
></td><td id="790"><a href="#790">790</a></td></tr
><tr id="gr_svn70_791"

 onmouseover="gutterOver(791)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',791);">&nbsp;</span
></td><td id="791"><a href="#791">791</a></td></tr
><tr id="gr_svn70_792"

 onmouseover="gutterOver(792)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',792);">&nbsp;</span
></td><td id="792"><a href="#792">792</a></td></tr
><tr id="gr_svn70_793"

 onmouseover="gutterOver(793)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',793);">&nbsp;</span
></td><td id="793"><a href="#793">793</a></td></tr
><tr id="gr_svn70_794"

 onmouseover="gutterOver(794)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',794);">&nbsp;</span
></td><td id="794"><a href="#794">794</a></td></tr
><tr id="gr_svn70_795"

 onmouseover="gutterOver(795)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',795);">&nbsp;</span
></td><td id="795"><a href="#795">795</a></td></tr
><tr id="gr_svn70_796"

 onmouseover="gutterOver(796)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',796);">&nbsp;</span
></td><td id="796"><a href="#796">796</a></td></tr
><tr id="gr_svn70_797"

 onmouseover="gutterOver(797)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',797);">&nbsp;</span
></td><td id="797"><a href="#797">797</a></td></tr
><tr id="gr_svn70_798"

 onmouseover="gutterOver(798)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',798);">&nbsp;</span
></td><td id="798"><a href="#798">798</a></td></tr
><tr id="gr_svn70_799"

 onmouseover="gutterOver(799)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',799);">&nbsp;</span
></td><td id="799"><a href="#799">799</a></td></tr
><tr id="gr_svn70_800"

 onmouseover="gutterOver(800)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',800);">&nbsp;</span
></td><td id="800"><a href="#800">800</a></td></tr
><tr id="gr_svn70_801"

 onmouseover="gutterOver(801)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',801);">&nbsp;</span
></td><td id="801"><a href="#801">801</a></td></tr
><tr id="gr_svn70_802"

 onmouseover="gutterOver(802)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn70',802);">&nbsp;</span
></td><td id="802"><a href="#802">802</a></td></tr
></table></pre>
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
</td>
<td id="lines">
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
<pre class="prettyprint lang-py"><table id="src_table_0"><tr
id=sl_svn70_1

 onmouseover="gutterOver(1)"

><td class="source"># This file need to import search.py<br></td></tr
><tr
id=sl_svn70_2

 onmouseover="gutterOver(2)"

><td class="source"># Author: Wen Shen and Issak Gezehei<br></td></tr
><tr
id=sl_svn70_3

 onmouseover="gutterOver(3)"

><td class="source">import copy<br></td></tr
><tr
id=sl_svn70_4

 onmouseover="gutterOver(4)"

><td class="source">import itertools<br></td></tr
><tr
id=sl_svn70_5

 onmouseover="gutterOver(5)"

><td class="source">import search<br></td></tr
><tr
id=sl_svn70_6

 onmouseover="gutterOver(6)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_7

 onmouseover="gutterOver(7)"

><td class="source">class UnreachableError(Exception):<br></td></tr
><tr
id=sl_svn70_8

 onmouseover="gutterOver(8)"

><td class="source">    pass<br></td></tr
><tr
id=sl_svn70_9

 onmouseover="gutterOver(9)"

><td class="source">class ParseError(Exception):<br></td></tr
><tr
id=sl_svn70_10

 onmouseover="gutterOver(10)"

><td class="source">    pass<br></td></tr
><tr
id=sl_svn70_11

 onmouseover="gutterOver(11)"

><td class="source">class Condition(object):<br></td></tr
><tr
id=sl_svn70_12

 onmouseover="gutterOver(12)"

><td class="source">    def __init__(self, parts):<br></td></tr
><tr
id=sl_svn70_13

 onmouseover="gutterOver(13)"

><td class="source">        self.parts = tuple(parts)<br></td></tr
><tr
id=sl_svn70_14

 onmouseover="gutterOver(14)"

><td class="source">        self.hash = hash((self.__class__, self.parts))<br></td></tr
><tr
id=sl_svn70_15

 onmouseover="gutterOver(15)"

><td class="source">    def __hash__(self):<br></td></tr
><tr
id=sl_svn70_16

 onmouseover="gutterOver(16)"

><td class="source">        return self.hash<br></td></tr
><tr
id=sl_svn70_17

 onmouseover="gutterOver(17)"

><td class="source">    def __ne__(self, other):<br></td></tr
><tr
id=sl_svn70_18

 onmouseover="gutterOver(18)"

><td class="source">        return not self == other<br></td></tr
><tr
id=sl_svn70_19

 onmouseover="gutterOver(19)"

><td class="source">    def printer(self, indent=&quot;  &quot;):<br></td></tr
><tr
id=sl_svn70_20

 onmouseover="gutterOver(20)"

><td class="source">        print &quot;%s%s&quot; % (indent, self._printer())<br></td></tr
><tr
id=sl_svn70_21

 onmouseover="gutterOver(21)"

><td class="source">        for part in self.parts:<br></td></tr
><tr
id=sl_svn70_22

 onmouseover="gutterOver(22)"

><td class="source">            part.printer(indent + &quot;  &quot;)<br></td></tr
><tr
id=sl_svn70_23

 onmouseover="gutterOver(23)"

><td class="source">    def _printer(self):<br></td></tr
><tr
id=sl_svn70_24

 onmouseover="gutterOver(24)"

><td class="source">        return self.__class__.__name__<br></td></tr
><tr
id=sl_svn70_25

 onmouseover="gutterOver(25)"

><td class="source">    <br></td></tr
><tr
id=sl_svn70_26

 onmouseover="gutterOver(26)"

><td class="source">class Literal(Condition):<br></td></tr
><tr
id=sl_svn70_27

 onmouseover="gutterOver(27)"

><td class="source">    parts = []<br></td></tr
><tr
id=sl_svn70_28

 onmouseover="gutterOver(28)"

><td class="source">    def __init__(self, predicate, args):<br></td></tr
><tr
id=sl_svn70_29

 onmouseover="gutterOver(29)"

><td class="source">        self.predicate = predicate<br></td></tr
><tr
id=sl_svn70_30

 onmouseover="gutterOver(30)"

><td class="source">        self.args = tuple(args)<br></td></tr
><tr
id=sl_svn70_31

 onmouseover="gutterOver(31)"

><td class="source">        self.hash = hash((self.__class__, self.predicate, self.args))<br></td></tr
><tr
id=sl_svn70_32

 onmouseover="gutterOver(32)"

><td class="source">    def __eq__(self, other):<br></td></tr
><tr
id=sl_svn70_33

 onmouseover="gutterOver(33)"

><td class="source">        # Compare hash first for speed reasons.<br></td></tr
><tr
id=sl_svn70_34

 onmouseover="gutterOver(34)"

><td class="source">        return (self.hash == other.hash and<br></td></tr
><tr
id=sl_svn70_35

 onmouseover="gutterOver(35)"

><td class="source">                self.__class__ is other.__class__ and<br></td></tr
><tr
id=sl_svn70_36

 onmouseover="gutterOver(36)"

><td class="source">                self.predicate == other.predicate and<br></td></tr
><tr
id=sl_svn70_37

 onmouseover="gutterOver(37)"

><td class="source">                self.args == other.args)<br></td></tr
><tr
id=sl_svn70_38

 onmouseover="gutterOver(38)"

><td class="source">    def __str__(self):<br></td></tr
><tr
id=sl_svn70_39

 onmouseover="gutterOver(39)"

><td class="source">        return &quot;%s %s(%s)&quot; % (self.__class__.__name__, self.predicate,<br></td></tr
><tr
id=sl_svn70_40

 onmouseover="gutterOver(40)"

><td class="source">                              &quot;, &quot;.join(map(str, self.args)))<br></td></tr
><tr
id=sl_svn70_41

 onmouseover="gutterOver(41)"

><td class="source">    def _printer(self):<br></td></tr
><tr
id=sl_svn70_42

 onmouseover="gutterOver(42)"

><td class="source">        return str(self)<br></td></tr
><tr
id=sl_svn70_43

 onmouseover="gutterOver(43)"

><td class="source">    def change_parts(self, parts):<br></td></tr
><tr
id=sl_svn70_44

 onmouseover="gutterOver(44)"

><td class="source">        return self<br></td></tr
><tr
id=sl_svn70_45

 onmouseover="gutterOver(45)"

><td class="source">        <br></td></tr
><tr
id=sl_svn70_46

 onmouseover="gutterOver(46)"

><td class="source">class Atom(Literal):<br></td></tr
><tr
id=sl_svn70_47

 onmouseover="gutterOver(47)"

><td class="source">    negated = False<br></td></tr
><tr
id=sl_svn70_48

 onmouseover="gutterOver(48)"

><td class="source">    def instantiate(self, var_mapping, init_facts, fluent_facts, result):<br></td></tr
><tr
id=sl_svn70_49

 onmouseover="gutterOver(49)"

><td class="source">        args = [var_mapping.get(arg, arg) for arg in self.args]<br></td></tr
><tr
id=sl_svn70_50

 onmouseover="gutterOver(50)"

><td class="source">        atom = Atom(self.predicate, args)<br></td></tr
><tr
id=sl_svn70_51

 onmouseover="gutterOver(51)"

><td class="source">        if atom in fluent_facts:<br></td></tr
><tr
id=sl_svn70_52

 onmouseover="gutterOver(52)"

><td class="source">            result.append(atom)<br></td></tr
><tr
id=sl_svn70_53

 onmouseover="gutterOver(53)"

><td class="source">        elif atom not in init_facts:<br></td></tr
><tr
id=sl_svn70_54

 onmouseover="gutterOver(54)"

><td class="source">            raise UnreachableError()<br></td></tr
><tr
id=sl_svn70_55

 onmouseover="gutterOver(55)"

><td class="source">    def negate(self):<br></td></tr
><tr
id=sl_svn70_56

 onmouseover="gutterOver(56)"

><td class="source">        return NegatedAtom(self.predicate, self.args)<br></td></tr
><tr
id=sl_svn70_57

 onmouseover="gutterOver(57)"

><td class="source">    def positive(self):<br></td></tr
><tr
id=sl_svn70_58

 onmouseover="gutterOver(58)"

><td class="source">        return self<br></td></tr
><tr
id=sl_svn70_59

 onmouseover="gutterOver(59)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_60

 onmouseover="gutterOver(60)"

><td class="source">class NegatedAtom(Literal):<br></td></tr
><tr
id=sl_svn70_61

 onmouseover="gutterOver(61)"

><td class="source">   negated = True<br></td></tr
><tr
id=sl_svn70_62

 onmouseover="gutterOver(62)"

><td class="source">   def instantiate(self, var_mapping, init_facts, fluent_facts, result):<br></td></tr
><tr
id=sl_svn70_63

 onmouseover="gutterOver(63)"

><td class="source">        args = [var_mapping.get(arg, arg) for arg in self.args]<br></td></tr
><tr
id=sl_svn70_64

 onmouseover="gutterOver(64)"

><td class="source">        atom = Atom(self.predicate, args)<br></td></tr
><tr
id=sl_svn70_65

 onmouseover="gutterOver(65)"

><td class="source">        if atom in fluent_facts:<br></td></tr
><tr
id=sl_svn70_66

 onmouseover="gutterOver(66)"

><td class="source">            result.append(NegatedAtom(self.predicate, args))<br></td></tr
><tr
id=sl_svn70_67

 onmouseover="gutterOver(67)"

><td class="source">        elif atom in init_facts:<br></td></tr
><tr
id=sl_svn70_68

 onmouseover="gutterOver(68)"

><td class="source">            #raise UnreachableError()<br></td></tr
><tr
id=sl_svn70_69

 onmouseover="gutterOver(69)"

><td class="source">            pass<br></td></tr
><tr
id=sl_svn70_70

 onmouseover="gutterOver(70)"

><td class="source">   def negate(self):<br></td></tr
><tr
id=sl_svn70_71

 onmouseover="gutterOver(71)"

><td class="source">        return Atom(self.predicate, self.args)<br></td></tr
><tr
id=sl_svn70_72

 onmouseover="gutterOver(72)"

><td class="source">   positive = negate<br></td></tr
><tr
id=sl_svn70_73

 onmouseover="gutterOver(73)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_74

 onmouseover="gutterOver(74)"

><td class="source">class Term(object):<br></td></tr
><tr
id=sl_svn70_75

 onmouseover="gutterOver(75)"

><td class="source">    def __eq__(self, other):<br></td></tr
><tr
id=sl_svn70_76

 onmouseover="gutterOver(76)"

><td class="source">        return (self.__class__ == other.__class__ and self.name == other.name)<br></td></tr
><tr
id=sl_svn70_77

 onmouseover="gutterOver(77)"

><td class="source">    def printer(self, indent=&quot;  &quot;):<br></td></tr
><tr
id=sl_svn70_78

 onmouseover="gutterOver(78)"

><td class="source">        print &quot;%s%s %s&quot; % (indent, self._printer(), self.name)<br></td></tr
><tr
id=sl_svn70_79

 onmouseover="gutterOver(79)"

><td class="source">        for arg in self.args:<br></td></tr
><tr
id=sl_svn70_80

 onmouseover="gutterOver(80)"

><td class="source">            arg.printer(indent + &quot;  &quot;)<br></td></tr
><tr
id=sl_svn70_81

 onmouseover="gutterOver(81)"

><td class="source">    def _printer(self):<br></td></tr
><tr
id=sl_svn70_82

 onmouseover="gutterOver(82)"

><td class="source">        return self.__class__.__name__<br></td></tr
><tr
id=sl_svn70_83

 onmouseover="gutterOver(83)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_84

 onmouseover="gutterOver(84)"

><td class="source">class Variable(Term):<br></td></tr
><tr
id=sl_svn70_85

 onmouseover="gutterOver(85)"

><td class="source">    args = []<br></td></tr
><tr
id=sl_svn70_86

 onmouseover="gutterOver(86)"

><td class="source">    def __init__(self, name):<br></td></tr
><tr
id=sl_svn70_87

 onmouseover="gutterOver(87)"

><td class="source">        self.name = name<br></td></tr
><tr
id=sl_svn70_88

 onmouseover="gutterOver(88)"

><td class="source">    def __str__(self):<br></td></tr
><tr
id=sl_svn70_89

 onmouseover="gutterOver(89)"

><td class="source">        return self.name<br></td></tr
><tr
id=sl_svn70_90

 onmouseover="gutterOver(90)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_91

 onmouseover="gutterOver(91)"

><td class="source">class ObjectTerm(Term):<br></td></tr
><tr
id=sl_svn70_92

 onmouseover="gutterOver(92)"

><td class="source">    args = []<br></td></tr
><tr
id=sl_svn70_93

 onmouseover="gutterOver(93)"

><td class="source">    def __init__(self, name):<br></td></tr
><tr
id=sl_svn70_94

 onmouseover="gutterOver(94)"

><td class="source">        self.name = name<br></td></tr
><tr
id=sl_svn70_95

 onmouseover="gutterOver(95)"

><td class="source">    def __str__(self):<br></td></tr
><tr
id=sl_svn70_96

 onmouseover="gutterOver(96)"

><td class="source">        return self.name<br></td></tr
><tr
id=sl_svn70_97

 onmouseover="gutterOver(97)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_98

 onmouseover="gutterOver(98)"

><td class="source">class ConstantCondition(Condition):<br></td></tr
><tr
id=sl_svn70_99

 onmouseover="gutterOver(99)"

><td class="source">    parts = ()<br></td></tr
><tr
id=sl_svn70_100

 onmouseover="gutterOver(100)"

><td class="source">    def __init__(self):<br></td></tr
><tr
id=sl_svn70_101

 onmouseover="gutterOver(101)"

><td class="source">        self.hash = hash(self.__class__)<br></td></tr
><tr
id=sl_svn70_102

 onmouseover="gutterOver(102)"

><td class="source">    def change_parts(self, parts):<br></td></tr
><tr
id=sl_svn70_103

 onmouseover="gutterOver(103)"

><td class="source">        return self<br></td></tr
><tr
id=sl_svn70_104

 onmouseover="gutterOver(104)"

><td class="source">    def __eq__(self, other):<br></td></tr
><tr
id=sl_svn70_105

 onmouseover="gutterOver(105)"

><td class="source">        return self.__class__ is other.__class__<br></td></tr
><tr
id=sl_svn70_106

 onmouseover="gutterOver(106)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_107

 onmouseover="gutterOver(107)"

><td class="source">class Falsity(ConstantCondition):<br></td></tr
><tr
id=sl_svn70_108

 onmouseover="gutterOver(108)"

><td class="source">    def instantiate(self, var_mapping, init_facts, fluent_facts, result):<br></td></tr
><tr
id=sl_svn70_109

 onmouseover="gutterOver(109)"

><td class="source">        raise UnreachableError()<br></td></tr
><tr
id=sl_svn70_110

 onmouseover="gutterOver(110)"

><td class="source">    def negate(self):<br></td></tr
><tr
id=sl_svn70_111

 onmouseover="gutterOver(111)"

><td class="source">        return Truth()<br></td></tr
><tr
id=sl_svn70_112

 onmouseover="gutterOver(112)"

><td class="source">class Truth(ConstantCondition):<br></td></tr
><tr
id=sl_svn70_113

 onmouseover="gutterOver(113)"

><td class="source">    def instantiate(self, var_mapping, init_facts, fluent_facts, result):<br></td></tr
><tr
id=sl_svn70_114

 onmouseover="gutterOver(114)"

><td class="source">        pass<br></td></tr
><tr
id=sl_svn70_115

 onmouseover="gutterOver(115)"

><td class="source">    def negate(self):<br></td></tr
><tr
id=sl_svn70_116

 onmouseover="gutterOver(116)"

><td class="source">        return Falsity()<br></td></tr
><tr
id=sl_svn70_117

 onmouseover="gutterOver(117)"

><td class="source">        <br></td></tr
><tr
id=sl_svn70_118

 onmouseover="gutterOver(118)"

><td class="source">class JunctorCondition(Condition):<br></td></tr
><tr
id=sl_svn70_119

 onmouseover="gutterOver(119)"

><td class="source">    def __eq__(self, other):<br></td></tr
><tr
id=sl_svn70_120

 onmouseover="gutterOver(120)"

><td class="source">        return (self.hash == other.hash and<br></td></tr
><tr
id=sl_svn70_121

 onmouseover="gutterOver(121)"

><td class="source">                self.__class__ is other.__class__ and<br></td></tr
><tr
id=sl_svn70_122

 onmouseover="gutterOver(122)"

><td class="source">                self.parts == other.parts)<br></td></tr
><tr
id=sl_svn70_123

 onmouseover="gutterOver(123)"

><td class="source">    def change_parts(self, parts):<br></td></tr
><tr
id=sl_svn70_124

 onmouseover="gutterOver(124)"

><td class="source">        return self.__class__(parts)<br></td></tr
><tr
id=sl_svn70_125

 onmouseover="gutterOver(125)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_126

 onmouseover="gutterOver(126)"

><td class="source">class Conjunction(JunctorCondition):<br></td></tr
><tr
id=sl_svn70_127

 onmouseover="gutterOver(127)"

><td class="source">    def _simplified(self, parts):<br></td></tr
><tr
id=sl_svn70_128

 onmouseover="gutterOver(128)"

><td class="source">        result_parts = []<br></td></tr
><tr
id=sl_svn70_129

 onmouseover="gutterOver(129)"

><td class="source">        for part in parts:<br></td></tr
><tr
id=sl_svn70_130

 onmouseover="gutterOver(130)"

><td class="source">            if isinstance(part, Conjunction):<br></td></tr
><tr
id=sl_svn70_131

 onmouseover="gutterOver(131)"

><td class="source">                result_parts += part.parts<br></td></tr
><tr
id=sl_svn70_132

 onmouseover="gutterOver(132)"

><td class="source">            elif isinstance(part, Falsity):<br></td></tr
><tr
id=sl_svn70_133

 onmouseover="gutterOver(133)"

><td class="source">                return Falsity()<br></td></tr
><tr
id=sl_svn70_134

 onmouseover="gutterOver(134)"

><td class="source">            elif not isinstance(part, Truth):<br></td></tr
><tr
id=sl_svn70_135

 onmouseover="gutterOver(135)"

><td class="source">                result_parts.append(part)<br></td></tr
><tr
id=sl_svn70_136

 onmouseover="gutterOver(136)"

><td class="source">        if not result_parts:<br></td></tr
><tr
id=sl_svn70_137

 onmouseover="gutterOver(137)"

><td class="source">            return Truth()<br></td></tr
><tr
id=sl_svn70_138

 onmouseover="gutterOver(138)"

><td class="source">        if len(result_parts) == 1:<br></td></tr
><tr
id=sl_svn70_139

 onmouseover="gutterOver(139)"

><td class="source">            return result_parts[0]<br></td></tr
><tr
id=sl_svn70_140

 onmouseover="gutterOver(140)"

><td class="source">        return Conjunction(result_parts)<br></td></tr
><tr
id=sl_svn70_141

 onmouseover="gutterOver(141)"

><td class="source">    def instantiate(self, var_mapping, init_facts, fluent_facts, result):<br></td></tr
><tr
id=sl_svn70_142

 onmouseover="gutterOver(142)"

><td class="source">        assert not result, &quot;Condition not simplified&quot;<br></td></tr
><tr
id=sl_svn70_143

 onmouseover="gutterOver(143)"

><td class="source">        for part in self.parts:<br></td></tr
><tr
id=sl_svn70_144

 onmouseover="gutterOver(144)"

><td class="source">            part.instantiate(var_mapping, init_facts, fluent_facts, result)<br></td></tr
><tr
id=sl_svn70_145

 onmouseover="gutterOver(145)"

><td class="source">    def negate(self):<br></td></tr
><tr
id=sl_svn70_146

 onmouseover="gutterOver(146)"

><td class="source">        return Disjunction([p.negate() for p in self.parts])<br></td></tr
><tr
id=sl_svn70_147

 onmouseover="gutterOver(147)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_148

 onmouseover="gutterOver(148)"

><td class="source">class Disjunction(JunctorCondition):<br></td></tr
><tr
id=sl_svn70_149

 onmouseover="gutterOver(149)"

><td class="source">    def _simplified(self, parts):<br></td></tr
><tr
id=sl_svn70_150

 onmouseover="gutterOver(150)"

><td class="source">        result_parts = []<br></td></tr
><tr
id=sl_svn70_151

 onmouseover="gutterOver(151)"

><td class="source">        for part in parts:<br></td></tr
><tr
id=sl_svn70_152

 onmouseover="gutterOver(152)"

><td class="source">            if isinstance(part, Disjunction):<br></td></tr
><tr
id=sl_svn70_153

 onmouseover="gutterOver(153)"

><td class="source">                result_parts += part.parts<br></td></tr
><tr
id=sl_svn70_154

 onmouseover="gutterOver(154)"

><td class="source">            elif isinstance(part, Truth):<br></td></tr
><tr
id=sl_svn70_155

 onmouseover="gutterOver(155)"

><td class="source">                return Truth()<br></td></tr
><tr
id=sl_svn70_156

 onmouseover="gutterOver(156)"

><td class="source">            elif not isinstance(part, Falsity):<br></td></tr
><tr
id=sl_svn70_157

 onmouseover="gutterOver(157)"

><td class="source">                result_parts.append(part)<br></td></tr
><tr
id=sl_svn70_158

 onmouseover="gutterOver(158)"

><td class="source">        if not result_parts:<br></td></tr
><tr
id=sl_svn70_159

 onmouseover="gutterOver(159)"

><td class="source">            return Falsity()<br></td></tr
><tr
id=sl_svn70_160

 onmouseover="gutterOver(160)"

><td class="source">        if len(result_parts) == 1:<br></td></tr
><tr
id=sl_svn70_161

 onmouseover="gutterOver(161)"

><td class="source">            return result_parts[0]<br></td></tr
><tr
id=sl_svn70_162

 onmouseover="gutterOver(162)"

><td class="source">        return Disjunction(result_parts)<br></td></tr
><tr
id=sl_svn70_163

 onmouseover="gutterOver(163)"

><td class="source">    def negate(self):<br></td></tr
><tr
id=sl_svn70_164

 onmouseover="gutterOver(164)"

><td class="source">        return Conjunction([p.negate() for p in self.parts])<br></td></tr
><tr
id=sl_svn70_165

 onmouseover="gutterOver(165)"

><td class="source">    def has_disjunction(self):<br></td></tr
><tr
id=sl_svn70_166

 onmouseover="gutterOver(166)"

><td class="source">        return True<br></td></tr
><tr
id=sl_svn70_167

 onmouseover="gutterOver(167)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_168

 onmouseover="gutterOver(168)"

><td class="source">class Type(object):<br></td></tr
><tr
id=sl_svn70_169

 onmouseover="gutterOver(169)"

><td class="source">    def __init__(self, name, basetype_name=None):<br></td></tr
><tr
id=sl_svn70_170

 onmouseover="gutterOver(170)"

><td class="source">        self.name = name<br></td></tr
><tr
id=sl_svn70_171

 onmouseover="gutterOver(171)"

><td class="source">        self.basetype_name = basetype_name<br></td></tr
><tr
id=sl_svn70_172

 onmouseover="gutterOver(172)"

><td class="source">    def __str__(self):<br></td></tr
><tr
id=sl_svn70_173

 onmouseover="gutterOver(173)"

><td class="source">        return self.name<br></td></tr
><tr
id=sl_svn70_174

 onmouseover="gutterOver(174)"

><td class="source">    def __repr__(self):<br></td></tr
><tr
id=sl_svn70_175

 onmouseover="gutterOver(175)"

><td class="source">        return &quot;Type(%s, %s)&quot; % (self.name, self.basetype_name)<br></td></tr
><tr
id=sl_svn70_176

 onmouseover="gutterOver(176)"

><td class="source">        <br></td></tr
><tr
id=sl_svn70_177

 onmouseover="gutterOver(177)"

><td class="source">class Effect(object):<br></td></tr
><tr
id=sl_svn70_178

 onmouseover="gutterOver(178)"

><td class="source">    def __init__(self, parameters, condition, literal):<br></td></tr
><tr
id=sl_svn70_179

 onmouseover="gutterOver(179)"

><td class="source">        self.parameters = parameters<br></td></tr
><tr
id=sl_svn70_180

 onmouseover="gutterOver(180)"

><td class="source">        self.condition = condition<br></td></tr
><tr
id=sl_svn70_181

 onmouseover="gutterOver(181)"

><td class="source">        self.literal = literal<br></td></tr
><tr
id=sl_svn70_182

 onmouseover="gutterOver(182)"

><td class="source">    def __eq__(self, other):<br></td></tr
><tr
id=sl_svn70_183

 onmouseover="gutterOver(183)"

><td class="source">        return (self.__class__ is other.__class__ and<br></td></tr
><tr
id=sl_svn70_184

 onmouseover="gutterOver(184)"

><td class="source">                self.parameters == other.parameters and<br></td></tr
><tr
id=sl_svn70_185

 onmouseover="gutterOver(185)"

><td class="source">                self.condition == other.condition and<br></td></tr
><tr
id=sl_svn70_186

 onmouseover="gutterOver(186)"

><td class="source">                self.literal == other.literal)<br></td></tr
><tr
id=sl_svn70_187

 onmouseover="gutterOver(187)"

><td class="source">    def printer(self):<br></td></tr
><tr
id=sl_svn70_188

 onmouseover="gutterOver(188)"

><td class="source">        indent = &quot;  &quot;<br></td></tr
><tr
id=sl_svn70_189

 onmouseover="gutterOver(189)"

><td class="source">        if self.parameters:<br></td></tr
><tr
id=sl_svn70_190

 onmouseover="gutterOver(190)"

><td class="source">            print &quot;%sforall %s&quot; % (indent, &quot;, &quot;.join(map(str, self.parameters)))<br></td></tr
><tr
id=sl_svn70_191

 onmouseover="gutterOver(191)"

><td class="source">            indent += &quot;  &quot;<br></td></tr
><tr
id=sl_svn70_192

 onmouseover="gutterOver(192)"

><td class="source">        if self.condition != Truth():<br></td></tr
><tr
id=sl_svn70_193

 onmouseover="gutterOver(193)"

><td class="source">            print &quot;%sif&quot; % indent<br></td></tr
><tr
id=sl_svn70_194

 onmouseover="gutterOver(194)"

><td class="source">            self.condition.printer(indent + &quot;  &quot;)<br></td></tr
><tr
id=sl_svn70_195

 onmouseover="gutterOver(195)"

><td class="source">            print &quot;%sthen&quot; % indent<br></td></tr
><tr
id=sl_svn70_196

 onmouseover="gutterOver(196)"

><td class="source">            indent += &quot;  &quot;<br></td></tr
><tr
id=sl_svn70_197

 onmouseover="gutterOver(197)"

><td class="source">        print &quot;%s%s&quot; % (indent, self.literal)<br></td></tr
><tr
id=sl_svn70_198

 onmouseover="gutterOver(198)"

><td class="source">    <br></td></tr
><tr
id=sl_svn70_199

 onmouseover="gutterOver(199)"

><td class="source">    def instantiate(self, var_mapping, init_facts, fluent_facts, result):<br></td></tr
><tr
id=sl_svn70_200

 onmouseover="gutterOver(200)"

><td class="source">        condition = []<br></td></tr
><tr
id=sl_svn70_201

 onmouseover="gutterOver(201)"

><td class="source">        try:<br></td></tr
><tr
id=sl_svn70_202

 onmouseover="gutterOver(202)"

><td class="source">            self.condition.instantiate(var_mapping, init_facts, fluent_facts, condition)<br></td></tr
><tr
id=sl_svn70_203

 onmouseover="gutterOver(203)"

><td class="source">        except  UnreachableError:<br></td></tr
><tr
id=sl_svn70_204

 onmouseover="gutterOver(204)"

><td class="source">            return<br></td></tr
><tr
id=sl_svn70_205

 onmouseover="gutterOver(205)"

><td class="source">        effects = []<br></td></tr
><tr
id=sl_svn70_206

 onmouseover="gutterOver(206)"

><td class="source">        self.literal.instantiate(var_mapping, init_facts, fluent_facts, effects)<br></td></tr
><tr
id=sl_svn70_207

 onmouseover="gutterOver(207)"

><td class="source">        assert len(effects) &lt;= 1<br></td></tr
><tr
id=sl_svn70_208

 onmouseover="gutterOver(208)"

><td class="source">        if effects:<br></td></tr
><tr
id=sl_svn70_209

 onmouseover="gutterOver(209)"

><td class="source">            result.append((condition, effects[0]))<br></td></tr
><tr
id=sl_svn70_210

 onmouseover="gutterOver(210)"

><td class="source">            <br></td></tr
><tr
id=sl_svn70_211

 onmouseover="gutterOver(211)"

><td class="source">class CostEffect(object):<br></td></tr
><tr
id=sl_svn70_212

 onmouseover="gutterOver(212)"

><td class="source">    def __init__(self, effect):<br></td></tr
><tr
id=sl_svn70_213

 onmouseover="gutterOver(213)"

><td class="source">        self.effect = effect<br></td></tr
><tr
id=sl_svn70_214

 onmouseover="gutterOver(214)"

><td class="source">    def dump(self, indent=&quot;  &quot;):<br></td></tr
><tr
id=sl_svn70_215

 onmouseover="gutterOver(215)"

><td class="source">        print &quot;%s%s&quot; % (indent, self.effect)<br></td></tr
><tr
id=sl_svn70_216

 onmouseover="gutterOver(216)"

><td class="source">    def normalize(self):<br></td></tr
><tr
id=sl_svn70_217

 onmouseover="gutterOver(217)"

><td class="source">        return self<br></td></tr
><tr
id=sl_svn70_218

 onmouseover="gutterOver(218)"

><td class="source">    def extract_cost(self):<br></td></tr
><tr
id=sl_svn70_219

 onmouseover="gutterOver(219)"

><td class="source">        return self, None <br></td></tr
><tr
id=sl_svn70_220

 onmouseover="gutterOver(220)"

><td class="source">    <br></td></tr
><tr
id=sl_svn70_221

 onmouseover="gutterOver(221)"

><td class="source">class ConjunctiveEffect(object):<br></td></tr
><tr
id=sl_svn70_222

 onmouseover="gutterOver(222)"

><td class="source">    def __init__(self, effects):<br></td></tr
><tr
id=sl_svn70_223

 onmouseover="gutterOver(223)"

><td class="source">        flattened_effects = []<br></td></tr
><tr
id=sl_svn70_224

 onmouseover="gutterOver(224)"

><td class="source">        for effect in effects:<br></td></tr
><tr
id=sl_svn70_225

 onmouseover="gutterOver(225)"

><td class="source">            if isinstance(effect, ConjunctiveEffect):<br></td></tr
><tr
id=sl_svn70_226

 onmouseover="gutterOver(226)"

><td class="source">                flattened_effects += effect.effects<br></td></tr
><tr
id=sl_svn70_227

 onmouseover="gutterOver(227)"

><td class="source">            else:<br></td></tr
><tr
id=sl_svn70_228

 onmouseover="gutterOver(228)"

><td class="source">                flattened_effects.append(effect)<br></td></tr
><tr
id=sl_svn70_229

 onmouseover="gutterOver(229)"

><td class="source">        self.effects = flattened_effects<br></td></tr
><tr
id=sl_svn70_230

 onmouseover="gutterOver(230)"

><td class="source">    def printer(self, indent=&quot;  &quot;):<br></td></tr
><tr
id=sl_svn70_231

 onmouseover="gutterOver(231)"

><td class="source">        print &quot;%sand&quot; % (indent)<br></td></tr
><tr
id=sl_svn70_232

 onmouseover="gutterOver(232)"

><td class="source">        for eff in self.effects:<br></td></tr
><tr
id=sl_svn70_233

 onmouseover="gutterOver(233)"

><td class="source">            eff.printer(indent + &quot;  &quot;)<br></td></tr
><tr
id=sl_svn70_234

 onmouseover="gutterOver(234)"

><td class="source">    def normalize(self):<br></td></tr
><tr
id=sl_svn70_235

 onmouseover="gutterOver(235)"

><td class="source">        new_effects = []<br></td></tr
><tr
id=sl_svn70_236

 onmouseover="gutterOver(236)"

><td class="source">        for effect in self.effects:<br></td></tr
><tr
id=sl_svn70_237

 onmouseover="gutterOver(237)"

><td class="source">            new_effects.append(effect.normalize())<br></td></tr
><tr
id=sl_svn70_238

 onmouseover="gutterOver(238)"

><td class="source">        return ConjunctiveEffect(new_effects)<br></td></tr
><tr
id=sl_svn70_239

 onmouseover="gutterOver(239)"

><td class="source">    def extract_cost(self):<br></td></tr
><tr
id=sl_svn70_240

 onmouseover="gutterOver(240)"

><td class="source">        new_effects = []<br></td></tr
><tr
id=sl_svn70_241

 onmouseover="gutterOver(241)"

><td class="source">        cost_effect = None<br></td></tr
><tr
id=sl_svn70_242

 onmouseover="gutterOver(242)"

><td class="source">        for effect in self.effects:<br></td></tr
><tr
id=sl_svn70_243

 onmouseover="gutterOver(243)"

><td class="source">            if isinstance(effect, CostEffect):<br></td></tr
><tr
id=sl_svn70_244

 onmouseover="gutterOver(244)"

><td class="source">                cost_effect = effect<br></td></tr
><tr
id=sl_svn70_245

 onmouseover="gutterOver(245)"

><td class="source">            else:<br></td></tr
><tr
id=sl_svn70_246

 onmouseover="gutterOver(246)"

><td class="source">                new_effects.append(effect)<br></td></tr
><tr
id=sl_svn70_247

 onmouseover="gutterOver(247)"

><td class="source">        return cost_effect, ConjunctiveEffect(new_effects)<br></td></tr
><tr
id=sl_svn70_248

 onmouseover="gutterOver(248)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_249

 onmouseover="gutterOver(249)"

><td class="source">class SimpleEffect(object):<br></td></tr
><tr
id=sl_svn70_250

 onmouseover="gutterOver(250)"

><td class="source">    def __init__(self, effect):<br></td></tr
><tr
id=sl_svn70_251

 onmouseover="gutterOver(251)"

><td class="source">        self.effect = effect<br></td></tr
><tr
id=sl_svn70_252

 onmouseover="gutterOver(252)"

><td class="source">    def printer(self, indent=&quot;  &quot;):<br></td></tr
><tr
id=sl_svn70_253

 onmouseover="gutterOver(253)"

><td class="source">        print &quot;%s%s&quot; % (indent, self.effect)<br></td></tr
><tr
id=sl_svn70_254

 onmouseover="gutterOver(254)"

><td class="source">    def normalize(self):<br></td></tr
><tr
id=sl_svn70_255

 onmouseover="gutterOver(255)"

><td class="source">        return self<br></td></tr
><tr
id=sl_svn70_256

 onmouseover="gutterOver(256)"

><td class="source">    def extract_cost(self):<br></td></tr
><tr
id=sl_svn70_257

 onmouseover="gutterOver(257)"

><td class="source">        return None, self<br></td></tr
><tr
id=sl_svn70_258

 onmouseover="gutterOver(258)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_259

 onmouseover="gutterOver(259)"

><td class="source">class TypedObject(object):<br></td></tr
><tr
id=sl_svn70_260

 onmouseover="gutterOver(260)"

><td class="source">    def __init__(self, name, type):<br></td></tr
><tr
id=sl_svn70_261

 onmouseover="gutterOver(261)"

><td class="source">        self.name = name<br></td></tr
><tr
id=sl_svn70_262

 onmouseover="gutterOver(262)"

><td class="source">        self.type = type<br></td></tr
><tr
id=sl_svn70_263

 onmouseover="gutterOver(263)"

><td class="source">    def __hash__(self):<br></td></tr
><tr
id=sl_svn70_264

 onmouseover="gutterOver(264)"

><td class="source">        return hash((self.name, self.type))<br></td></tr
><tr
id=sl_svn70_265

 onmouseover="gutterOver(265)"

><td class="source">    def __eq__(self, other):<br></td></tr
><tr
id=sl_svn70_266

 onmouseover="gutterOver(266)"

><td class="source">        return self.name == other.name and self.type == other.type<br></td></tr
><tr
id=sl_svn70_267

 onmouseover="gutterOver(267)"

><td class="source">    def __ne__(self, other):<br></td></tr
><tr
id=sl_svn70_268

 onmouseover="gutterOver(268)"

><td class="source">        return not self == other<br></td></tr
><tr
id=sl_svn70_269

 onmouseover="gutterOver(269)"

><td class="source">    def __str__(self):<br></td></tr
><tr
id=sl_svn70_270

 onmouseover="gutterOver(270)"

><td class="source">        return &quot;%s: %s&quot; % (self.name, self.type)<br></td></tr
><tr
id=sl_svn70_271

 onmouseover="gutterOver(271)"

><td class="source">        <br></td></tr
><tr
id=sl_svn70_272

 onmouseover="gutterOver(272)"

><td class="source">class Predicate(object):<br></td></tr
><tr
id=sl_svn70_273

 onmouseover="gutterOver(273)"

><td class="source">    def __init__(self, name, arguments):<br></td></tr
><tr
id=sl_svn70_274

 onmouseover="gutterOver(274)"

><td class="source">        self.name = name<br></td></tr
><tr
id=sl_svn70_275

 onmouseover="gutterOver(275)"

><td class="source">        self.arguments = arguments<br></td></tr
><tr
id=sl_svn70_276

 onmouseover="gutterOver(276)"

><td class="source">    def parse(alist):<br></td></tr
><tr
id=sl_svn70_277

 onmouseover="gutterOver(277)"

><td class="source">        name = alist[0]<br></td></tr
><tr
id=sl_svn70_278

 onmouseover="gutterOver(278)"

><td class="source">        arguments = parse_typed_list(alist[1:], only_variables=True)<br></td></tr
><tr
id=sl_svn70_279

 onmouseover="gutterOver(279)"

><td class="source">        return Predicate(name, arguments)<br></td></tr
><tr
id=sl_svn70_280

 onmouseover="gutterOver(280)"

><td class="source">    parse = staticmethod(parse)<br></td></tr
><tr
id=sl_svn70_281

 onmouseover="gutterOver(281)"

><td class="source">    def __str__(self):<br></td></tr
><tr
id=sl_svn70_282

 onmouseover="gutterOver(282)"

><td class="source">        return &quot;%s(%s)&quot; % (self.name, &quot;, &quot;.join(map(str, self.arguments)))<br></td></tr
><tr
id=sl_svn70_283

 onmouseover="gutterOver(283)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_284

 onmouseover="gutterOver(284)"

><td class="source">class Action(object):<br></td></tr
><tr
id=sl_svn70_285

 onmouseover="gutterOver(285)"

><td class="source">    def __init__(self, name, parameters, precondition, effects):<br></td></tr
><tr
id=sl_svn70_286

 onmouseover="gutterOver(286)"

><td class="source">        self.name = name<br></td></tr
><tr
id=sl_svn70_287

 onmouseover="gutterOver(287)"

><td class="source">        self.parameters = parameters<br></td></tr
><tr
id=sl_svn70_288

 onmouseover="gutterOver(288)"

><td class="source">        self.precondition = precondition<br></td></tr
><tr
id=sl_svn70_289

 onmouseover="gutterOver(289)"

><td class="source">        self.effects = effects<br></td></tr
><tr
id=sl_svn70_290

 onmouseover="gutterOver(290)"

><td class="source">    def __repr__(self):<br></td></tr
><tr
id=sl_svn70_291

 onmouseover="gutterOver(291)"

><td class="source">        return &quot;&lt;Action %r&gt;&quot; % (self.name, id(self))<br></td></tr
><tr
id=sl_svn70_292

 onmouseover="gutterOver(292)"

><td class="source">    def parse(alist):<br></td></tr
><tr
id=sl_svn70_293

 onmouseover="gutterOver(293)"

><td class="source">        iterator = iter(alist)<br></td></tr
><tr
id=sl_svn70_294

 onmouseover="gutterOver(294)"

><td class="source">        if iterator.next() == &quot;:action&quot;:<br></td></tr
><tr
id=sl_svn70_295

 onmouseover="gutterOver(295)"

><td class="source">            pass<br></td></tr
><tr
id=sl_svn70_296

 onmouseover="gutterOver(296)"

><td class="source">        else:<br></td></tr
><tr
id=sl_svn70_297

 onmouseover="gutterOver(297)"

><td class="source">            raise SystemExit(&quot;Error! The typed STRIPS PDDL file should include actions!&quot;)<br></td></tr
><tr
id=sl_svn70_298

 onmouseover="gutterOver(298)"

><td class="source">        name = iterator.next()<br></td></tr
><tr
id=sl_svn70_299

 onmouseover="gutterOver(299)"

><td class="source">        parameters_tag_opt = iterator.next()<br></td></tr
><tr
id=sl_svn70_300

 onmouseover="gutterOver(300)"

><td class="source">        if parameters_tag_opt == &quot;:parameters&quot;:<br></td></tr
><tr
id=sl_svn70_301

 onmouseover="gutterOver(301)"

><td class="source">            parameters = parse_typed_list(iterator.next(),<br></td></tr
><tr
id=sl_svn70_302

 onmouseover="gutterOver(302)"

><td class="source">                                                     only_variables=True)<br></td></tr
><tr
id=sl_svn70_303

 onmouseover="gutterOver(303)"

><td class="source">            precondition_tag_opt = iterator.next()<br></td></tr
><tr
id=sl_svn70_304

 onmouseover="gutterOver(304)"

><td class="source">        else:<br></td></tr
><tr
id=sl_svn70_305

 onmouseover="gutterOver(305)"

><td class="source">            parameters = []<br></td></tr
><tr
id=sl_svn70_306

 onmouseover="gutterOver(306)"

><td class="source">            precondition_tag_opt = parameters_tag_opt<br></td></tr
><tr
id=sl_svn70_307

 onmouseover="gutterOver(307)"

><td class="source">        if precondition_tag_opt == &quot;:precondition&quot;:<br></td></tr
><tr
id=sl_svn70_308

 onmouseover="gutterOver(308)"

><td class="source">            precondition = parse_condition(iterator.next())<br></td></tr
><tr
id=sl_svn70_309

 onmouseover="gutterOver(309)"

><td class="source">            effect_tag = iterator.next()<br></td></tr
><tr
id=sl_svn70_310

 onmouseover="gutterOver(310)"

><td class="source">        else:<br></td></tr
><tr
id=sl_svn70_311

 onmouseover="gutterOver(311)"

><td class="source">            precondition = Conjunction([])<br></td></tr
><tr
id=sl_svn70_312

 onmouseover="gutterOver(312)"

><td class="source">            effect_tag = precondition_tag_opt<br></td></tr
><tr
id=sl_svn70_313

 onmouseover="gutterOver(313)"

><td class="source">        if effect_tag == &quot;:effect&quot;:<br></td></tr
><tr
id=sl_svn70_314

 onmouseover="gutterOver(314)"

><td class="source">            pass<br></td></tr
><tr
id=sl_svn70_315

 onmouseover="gutterOver(315)"

><td class="source">        else:<br></td></tr
><tr
id=sl_svn70_316

 onmouseover="gutterOver(316)"

><td class="source">            raise SystemExit(&quot;Error! The action should include the effect properly.&quot;)<br></td></tr
><tr
id=sl_svn70_317

 onmouseover="gutterOver(317)"

><td class="source">        effect_list = iterator.next()<br></td></tr
><tr
id=sl_svn70_318

 onmouseover="gutterOver(318)"

><td class="source">        eff = []<br></td></tr
><tr
id=sl_svn70_319

 onmouseover="gutterOver(319)"

><td class="source">        parse_effects(effect_list, eff)<br></td></tr
><tr
id=sl_svn70_320

 onmouseover="gutterOver(320)"

><td class="source">        for rest in iterator:<br></td></tr
><tr
id=sl_svn70_321

 onmouseover="gutterOver(321)"

><td class="source">            assert False, rest<br></td></tr
><tr
id=sl_svn70_322

 onmouseover="gutterOver(322)"

><td class="source">        return Action(name, parameters, precondition, eff)<br></td></tr
><tr
id=sl_svn70_323

 onmouseover="gutterOver(323)"

><td class="source">    parse = staticmethod(parse)<br></td></tr
><tr
id=sl_svn70_324

 onmouseover="gutterOver(324)"

><td class="source">    def printer(self):<br></td></tr
><tr
id=sl_svn70_325

 onmouseover="gutterOver(325)"

><td class="source">        print &quot;%s(%s)&quot; % (self.name, &quot;, &quot;.join(map(str, self.parameters)))<br></td></tr
><tr
id=sl_svn70_326

 onmouseover="gutterOver(326)"

><td class="source">        print &quot;Precondition:&quot;<br></td></tr
><tr
id=sl_svn70_327

 onmouseover="gutterOver(327)"

><td class="source">        self.precondition.printer()<br></td></tr
><tr
id=sl_svn70_328

 onmouseover="gutterOver(328)"

><td class="source">        print &quot;Effects:&quot;<br></td></tr
><tr
id=sl_svn70_329

 onmouseover="gutterOver(329)"

><td class="source">        for eff in self.effects:<br></td></tr
><tr
id=sl_svn70_330

 onmouseover="gutterOver(330)"

><td class="source">            eff.printer()<br></td></tr
><tr
id=sl_svn70_331

 onmouseover="gutterOver(331)"

><td class="source">    def instantiate(self, var_mapping, init_facts, fluent_facts):<br></td></tr
><tr
id=sl_svn70_332

 onmouseover="gutterOver(332)"

><td class="source">        arg_list = [var_mapping[par.name] for par in self.parameters]<br></td></tr
><tr
id=sl_svn70_333

 onmouseover="gutterOver(333)"

><td class="source">        name = &quot;(%s %s)&quot; % (self.name, &quot; &quot;.join(arg_list))<br></td></tr
><tr
id=sl_svn70_334

 onmouseover="gutterOver(334)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_335

 onmouseover="gutterOver(335)"

><td class="source">        precondition = []<br></td></tr
><tr
id=sl_svn70_336

 onmouseover="gutterOver(336)"

><td class="source">        try:<br></td></tr
><tr
id=sl_svn70_337

 onmouseover="gutterOver(337)"

><td class="source">            self.precondition.instantiate(var_mapping, init_facts,<br></td></tr
><tr
id=sl_svn70_338

 onmouseover="gutterOver(338)"

><td class="source">                                          fluent_facts, precondition)<br></td></tr
><tr
id=sl_svn70_339

 onmouseover="gutterOver(339)"

><td class="source">        except UnreachableError:<br></td></tr
><tr
id=sl_svn70_340

 onmouseover="gutterOver(340)"

><td class="source">            return None<br></td></tr
><tr
id=sl_svn70_341

 onmouseover="gutterOver(341)"

><td class="source">        effects = []<br></td></tr
><tr
id=sl_svn70_342

 onmouseover="gutterOver(342)"

><td class="source">        for eff in self.effects:<br></td></tr
><tr
id=sl_svn70_343

 onmouseover="gutterOver(343)"

><td class="source">            eff.instantiate(var_mapping, init_facts, fluent_facts,<br></td></tr
><tr
id=sl_svn70_344

 onmouseover="gutterOver(344)"

><td class="source">                             effects)<br></td></tr
><tr
id=sl_svn70_345

 onmouseover="gutterOver(345)"

><td class="source">        if effects:<br></td></tr
><tr
id=sl_svn70_346

 onmouseover="gutterOver(346)"

><td class="source">            return PropositionalAction(name, precondition, effects)<br></td></tr
><tr
id=sl_svn70_347

 onmouseover="gutterOver(347)"

><td class="source">        else:<br></td></tr
><tr
id=sl_svn70_348

 onmouseover="gutterOver(348)"

><td class="source">            return None<br></td></tr
><tr
id=sl_svn70_349

 onmouseover="gutterOver(349)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_350

 onmouseover="gutterOver(350)"

><td class="source">class PropositionalAction:<br></td></tr
><tr
id=sl_svn70_351

 onmouseover="gutterOver(351)"

><td class="source">    def __init__(self, name, precondition, effects):<br></td></tr
><tr
id=sl_svn70_352

 onmouseover="gutterOver(352)"

><td class="source">        self.name = name<br></td></tr
><tr
id=sl_svn70_353

 onmouseover="gutterOver(353)"

><td class="source">        self.precondition = precondition<br></td></tr
><tr
id=sl_svn70_354

 onmouseover="gutterOver(354)"

><td class="source">        self.add_effects = []<br></td></tr
><tr
id=sl_svn70_355

 onmouseover="gutterOver(355)"

><td class="source">        self.del_effects = []<br></td></tr
><tr
id=sl_svn70_356

 onmouseover="gutterOver(356)"

><td class="source">        for condition, effect in effects:<br></td></tr
><tr
id=sl_svn70_357

 onmouseover="gutterOver(357)"

><td class="source">            if not effect.negated:<br></td></tr
><tr
id=sl_svn70_358

 onmouseover="gutterOver(358)"

><td class="source">                self.add_effects.append((condition, effect))<br></td></tr
><tr
id=sl_svn70_359

 onmouseover="gutterOver(359)"

><td class="source">        for condition, effect in effects:<br></td></tr
><tr
id=sl_svn70_360

 onmouseover="gutterOver(360)"

><td class="source">            if effect.negated and (condition, effect.negate()) not in self.add_effects:<br></td></tr
><tr
id=sl_svn70_361

 onmouseover="gutterOver(361)"

><td class="source">                self.del_effects.append((condition, effect.negate()))<br></td></tr
><tr
id=sl_svn70_362

 onmouseover="gutterOver(362)"

><td class="source">    def __repr__(self):<br></td></tr
><tr
id=sl_svn70_363

 onmouseover="gutterOver(363)"

><td class="source">            return &quot;&lt;Action: %s&gt;&quot; %(self.name)<br></td></tr
><tr
id=sl_svn70_364

 onmouseover="gutterOver(364)"

><td class="source">            <br></td></tr
><tr
id=sl_svn70_365

 onmouseover="gutterOver(365)"

><td class="source">class Domain:<br></td></tr
><tr
id=sl_svn70_366

 onmouseover="gutterOver(366)"

><td class="source">    def __init__(self, domain_name,  requirements,  typing,  constants,  predicates,  actions):<br></td></tr
><tr
id=sl_svn70_367

 onmouseover="gutterOver(367)"

><td class="source">        self.domain_name = domain_name<br></td></tr
><tr
id=sl_svn70_368

 onmouseover="gutterOver(368)"

><td class="source">        self.requirements = requirements<br></td></tr
><tr
id=sl_svn70_369

 onmouseover="gutterOver(369)"

><td class="source">        self.types = typing<br></td></tr
><tr
id=sl_svn70_370

 onmouseover="gutterOver(370)"

><td class="source">        self.constants = constants<br></td></tr
><tr
id=sl_svn70_371

 onmouseover="gutterOver(371)"

><td class="source">        self.predicates = predicates<br></td></tr
><tr
id=sl_svn70_372

 onmouseover="gutterOver(372)"

><td class="source">        self.actions = actions<br></td></tr
><tr
id=sl_svn70_373

 onmouseover="gutterOver(373)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_374

 onmouseover="gutterOver(374)"

><td class="source">    def get_instance(typed_strips_domain_file):<br></td></tr
><tr
id=sl_svn70_375

 onmouseover="gutterOver(375)"

><td class="source">        domain_file = parse_pddl(&#39;domain&#39;, typed_strips_domain_file) <br></td></tr
><tr
id=sl_svn70_376

 onmouseover="gutterOver(376)"

><td class="source">        domain_name, requirements, types, constants, predicates, actions \<br></td></tr
><tr
id=sl_svn70_377

 onmouseover="gutterOver(377)"

><td class="source">        = parse_domain(domain_file)<br></td></tr
><tr
id=sl_svn70_378

 onmouseover="gutterOver(378)"

><td class="source">        <br></td></tr
><tr
id=sl_svn70_379

 onmouseover="gutterOver(379)"

><td class="source">        return Domain(domain_name, requirements, types, constants, predicates, actions)<br></td></tr
><tr
id=sl_svn70_380

 onmouseover="gutterOver(380)"

><td class="source">    get_instance = staticmethod(get_instance)<br></td></tr
><tr
id=sl_svn70_381

 onmouseover="gutterOver(381)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_382

 onmouseover="gutterOver(382)"

><td class="source">    def printer(self):<br></td></tr
><tr
id=sl_svn70_383

 onmouseover="gutterOver(383)"

><td class="source">        print &quot;Domain %s: [%s]&quot; % (self.domain_name, self.requirements)<br></td></tr
><tr
id=sl_svn70_384

 onmouseover="gutterOver(384)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_385

 onmouseover="gutterOver(385)"

><td class="source">        print &quot;Types:&quot;<br></td></tr
><tr
id=sl_svn70_386

 onmouseover="gutterOver(386)"

><td class="source">        for type_ in self.types:<br></td></tr
><tr
id=sl_svn70_387

 onmouseover="gutterOver(387)"

><td class="source">            print &quot;  %s&quot; % type_<br></td></tr
><tr
id=sl_svn70_388

 onmouseover="gutterOver(388)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_389

 onmouseover="gutterOver(389)"

><td class="source">        print &quot;Constants:&quot;<br></td></tr
><tr
id=sl_svn70_390

 onmouseover="gutterOver(390)"

><td class="source">        for const in self.constants:<br></td></tr
><tr
id=sl_svn70_391

 onmouseover="gutterOver(391)"

><td class="source">            print &quot;  %s&quot; % const<br></td></tr
><tr
id=sl_svn70_392

 onmouseover="gutterOver(392)"

><td class="source">        print &quot;Predicates:&quot;<br></td></tr
><tr
id=sl_svn70_393

 onmouseover="gutterOver(393)"

><td class="source">        for pred in self.predicates:<br></td></tr
><tr
id=sl_svn70_394

 onmouseover="gutterOver(394)"

><td class="source">            print &quot;  %s&quot; % pred<br></td></tr
><tr
id=sl_svn70_395

 onmouseover="gutterOver(395)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_396

 onmouseover="gutterOver(396)"

><td class="source">        print &quot;Actions:&quot;<br></td></tr
><tr
id=sl_svn70_397

 onmouseover="gutterOver(397)"

><td class="source">        for action in self.actions:<br></td></tr
><tr
id=sl_svn70_398

 onmouseover="gutterOver(398)"

><td class="source">            action.printer()<br></td></tr
><tr
id=sl_svn70_399

 onmouseover="gutterOver(399)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_400

 onmouseover="gutterOver(400)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_401

 onmouseover="gutterOver(401)"

><td class="source">class Problem:<br></td></tr
><tr
id=sl_svn70_402

 onmouseover="gutterOver(402)"

><td class="source">    def __init__(self, problem_name, domain_name, requirements, objects, init, goal):<br></td></tr
><tr
id=sl_svn70_403

 onmouseover="gutterOver(403)"

><td class="source">        self.problem_name = problem_name<br></td></tr
><tr
id=sl_svn70_404

 onmouseover="gutterOver(404)"

><td class="source">        self.domain_name = domain_name<br></td></tr
><tr
id=sl_svn70_405

 onmouseover="gutterOver(405)"

><td class="source">        self.requirements = requirements<br></td></tr
><tr
id=sl_svn70_406

 onmouseover="gutterOver(406)"

><td class="source">        self.objects = objects<br></td></tr
><tr
id=sl_svn70_407

 onmouseover="gutterOver(407)"

><td class="source">        self.init = init<br></td></tr
><tr
id=sl_svn70_408

 onmouseover="gutterOver(408)"

><td class="source">        self.goal = goal<br></td></tr
><tr
id=sl_svn70_409

 onmouseover="gutterOver(409)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_410

 onmouseover="gutterOver(410)"

><td class="source">    def get_instance(typed_strips_problem_file):<br></td></tr
><tr
id=sl_svn70_411

 onmouseover="gutterOver(411)"

><td class="source">        problem_pddl= parse_pddl(&#39;problem&#39;, typed_strips_problem_file) <br></td></tr
><tr
id=sl_svn70_412

 onmouseover="gutterOver(412)"

><td class="source">        problem_name, domain_name, requirements,  objects, init, goal = parse_problem(problem_pddl)<br></td></tr
><tr
id=sl_svn70_413

 onmouseover="gutterOver(413)"

><td class="source">        return Problem(problem_name, domain_name, requirements, objects, init, goal)<br></td></tr
><tr
id=sl_svn70_414

 onmouseover="gutterOver(414)"

><td class="source">    get_instance = staticmethod(get_instance)<br></td></tr
><tr
id=sl_svn70_415

 onmouseover="gutterOver(415)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_416

 onmouseover="gutterOver(416)"

><td class="source">    def printer(self):<br></td></tr
><tr
id=sl_svn70_417

 onmouseover="gutterOver(417)"

><td class="source">        print &quot;Problem %s: %s [%s]&quot; % (self.problem_name, self.domain_name, self.requirements)<br></td></tr
><tr
id=sl_svn70_418

 onmouseover="gutterOver(418)"

><td class="source">        print &quot;Objects:&quot;<br></td></tr
><tr
id=sl_svn70_419

 onmouseover="gutterOver(419)"

><td class="source">        for obj in self.objects:<br></td></tr
><tr
id=sl_svn70_420

 onmouseover="gutterOver(420)"

><td class="source">            print &quot;  %s&quot; % obj<br></td></tr
><tr
id=sl_svn70_421

 onmouseover="gutterOver(421)"

><td class="source">        print &quot;Init:&quot;<br></td></tr
><tr
id=sl_svn70_422

 onmouseover="gutterOver(422)"

><td class="source">        for init_ in self.init:<br></td></tr
><tr
id=sl_svn70_423

 onmouseover="gutterOver(423)"

><td class="source">            print &quot;  %s&quot; % init_<br></td></tr
><tr
id=sl_svn70_424

 onmouseover="gutterOver(424)"

><td class="source">        print &quot;Goals:&quot;<br></td></tr
><tr
id=sl_svn70_425

 onmouseover="gutterOver(425)"

><td class="source">        print self.goal.printer()<br></td></tr
><tr
id=sl_svn70_426

 onmouseover="gutterOver(426)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_427

 onmouseover="gutterOver(427)"

><td class="source">class State:<br></td></tr
><tr
id=sl_svn70_428

 onmouseover="gutterOver(428)"

><td class="source">    def __init__(self, domain, problem):<br></td></tr
><tr
id=sl_svn70_429

 onmouseover="gutterOver(429)"

><td class="source">        assert(domain.domain_name == problem.domain_name)<br></td></tr
><tr
id=sl_svn70_430

 onmouseover="gutterOver(430)"

><td class="source">        self.domain = domain<br></td></tr
><tr
id=sl_svn70_431

 onmouseover="gutterOver(431)"

><td class="source">        self.problem = problem<br></td></tr
><tr
id=sl_svn70_432

 onmouseover="gutterOver(432)"

><td class="source">        self.goal = problem.goal<br></td></tr
><tr
id=sl_svn70_433

 onmouseover="gutterOver(433)"

><td class="source">        self.objects = domain.constants+problem.objects<br></td></tr
><tr
id=sl_svn70_434

 onmouseover="gutterOver(434)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_435

 onmouseover="gutterOver(435)"

><td class="source">class Task(search.Problem):<br></td></tr
><tr
id=sl_svn70_436

 onmouseover="gutterOver(436)"

><td class="source">    def __init__(self, domain,  problem):<br></td></tr
><tr
id=sl_svn70_437

 onmouseover="gutterOver(437)"

><td class="source">        self.initial = State(domain, problem)<br></td></tr
><tr
id=sl_svn70_438

 onmouseover="gutterOver(438)"

><td class="source">        self.goal = self.initial.goal<br></td></tr
><tr
id=sl_svn70_439

 onmouseover="gutterOver(439)"

><td class="source">        search.Problem.__init__(self, self.initial, self.initial.goal)<br></td></tr
><tr
id=sl_svn70_440

 onmouseover="gutterOver(440)"

><td class="source">        <br></td></tr
><tr
id=sl_svn70_441

 onmouseover="gutterOver(441)"

><td class="source">    def successor(self, state):<br></td></tr
><tr
id=sl_svn70_442

 onmouseover="gutterOver(442)"

><td class="source">        return self.get_successors(self.get_actions(state),  state)<br></td></tr
><tr
id=sl_svn70_443

 onmouseover="gutterOver(443)"

><td class="source">        <br></td></tr
><tr
id=sl_svn70_444

 onmouseover="gutterOver(444)"

><td class="source">    def get_successors(self, actions,  state):<br></td></tr
><tr
id=sl_svn70_445

 onmouseover="gutterOver(445)"

><td class="source">        successors =[]<br></td></tr
><tr
id=sl_svn70_446

 onmouseover="gutterOver(446)"

><td class="source">        for action_ in actions:<br></td></tr
><tr
id=sl_svn70_447

 onmouseover="gutterOver(447)"

><td class="source">            successor = self.successor_assist(action_, state)<br></td></tr
><tr
id=sl_svn70_448

 onmouseover="gutterOver(448)"

><td class="source">            successors.append(successor)<br></td></tr
><tr
id=sl_svn70_449

 onmouseover="gutterOver(449)"

><td class="source">        return successors<br></td></tr
><tr
id=sl_svn70_450

 onmouseover="gutterOver(450)"

><td class="source">        <br></td></tr
><tr
id=sl_svn70_451

 onmouseover="gutterOver(451)"

><td class="source">    def successor_assist(self, action, state):<br></td></tr
><tr
id=sl_svn70_452

 onmouseover="gutterOver(452)"

><td class="source">         new_facts =[]<br></td></tr
><tr
id=sl_svn70_453

 onmouseover="gutterOver(453)"

><td class="source">         new_state = copy.deepcopy(state)<br></td></tr
><tr
id=sl_svn70_454

 onmouseover="gutterOver(454)"

><td class="source">         for fact in state.problem.init:<br></td></tr
><tr
id=sl_svn70_455

 onmouseover="gutterOver(455)"

><td class="source">            if fact not in action.del_effects:<br></td></tr
><tr
id=sl_svn70_456

 onmouseover="gutterOver(456)"

><td class="source">                new_facts.append(fact)<br></td></tr
><tr
id=sl_svn70_457

 onmouseover="gutterOver(457)"

><td class="source">         new_state.problem.init = new_facts<br></td></tr
><tr
id=sl_svn70_458

 onmouseover="gutterOver(458)"

><td class="source">         new_state.problem.init += action.add_effects<br></td></tr
><tr
id=sl_svn70_459

 onmouseover="gutterOver(459)"

><td class="source">         return (action,  new_state)<br></td></tr
><tr
id=sl_svn70_460

 onmouseover="gutterOver(460)"

><td class="source">         <br></td></tr
><tr
id=sl_svn70_461

 onmouseover="gutterOver(461)"

><td class="source">    def get_fluent_facts(self,para_mapping,action):<br></td></tr
><tr
id=sl_svn70_462

 onmouseover="gutterOver(462)"

><td class="source">        fluent_facts = []<br></td></tr
><tr
id=sl_svn70_463

 onmouseover="gutterOver(463)"

><td class="source">        for effect in action.effects:<br></td></tr
><tr
id=sl_svn70_464

 onmouseover="gutterOver(464)"

><td class="source">            args =[]<br></td></tr
><tr
id=sl_svn70_465

 onmouseover="gutterOver(465)"

><td class="source">            for argument in effect.literal.args:<br></td></tr
><tr
id=sl_svn70_466

 onmouseover="gutterOver(466)"

><td class="source">                new_arg =para_mapping.get(argument, argument)<br></td></tr
><tr
id=sl_svn70_467

 onmouseover="gutterOver(467)"

><td class="source">                args.append(new_arg)<br></td></tr
><tr
id=sl_svn70_468

 onmouseover="gutterOver(468)"

><td class="source">            if  effect.literal.negated:<br></td></tr
><tr
id=sl_svn70_469

 onmouseover="gutterOver(469)"

><td class="source">                atom = NegatedAtom(effect.literal.predicate,args)<br></td></tr
><tr
id=sl_svn70_470

 onmouseover="gutterOver(470)"

><td class="source">            else:<br></td></tr
><tr
id=sl_svn70_471

 onmouseover="gutterOver(471)"

><td class="source">                atom =Atom(effect.literal.predicate,args)<br></td></tr
><tr
id=sl_svn70_472

 onmouseover="gutterOver(472)"

><td class="source">            fluent_facts.append(atom)<br></td></tr
><tr
id=sl_svn70_473

 onmouseover="gutterOver(473)"

><td class="source">        return fluent_facts<br></td></tr
><tr
id=sl_svn70_474

 onmouseover="gutterOver(474)"

><td class="source">        <br></td></tr
><tr
id=sl_svn70_475

 onmouseover="gutterOver(475)"

><td class="source">    #To get all the possible actions<br></td></tr
><tr
id=sl_svn70_476

 onmouseover="gutterOver(476)"

><td class="source">    def get_actions(self, state):<br></td></tr
><tr
id=sl_svn70_477

 onmouseover="gutterOver(477)"

><td class="source">        actions =[]<br></td></tr
><tr
id=sl_svn70_478

 onmouseover="gutterOver(478)"

><td class="source">        for action in state.domain.actions:<br></td></tr
><tr
id=sl_svn70_479

 onmouseover="gutterOver(479)"

><td class="source">            actions += self.get_new_action(action, state)<br></td></tr
><tr
id=sl_svn70_480

 onmouseover="gutterOver(480)"

><td class="source">        return actions<br></td></tr
><tr
id=sl_svn70_481

 onmouseover="gutterOver(481)"

><td class="source">        <br></td></tr
><tr
id=sl_svn70_482

 onmouseover="gutterOver(482)"

><td class="source">    def get_new_action(self, action,  state):<br></td></tr
><tr
id=sl_svn70_483

 onmouseover="gutterOver(483)"

><td class="source">        actions_result = [] <br></td></tr
><tr
id=sl_svn70_484

 onmouseover="gutterOver(484)"

><td class="source">        pairs = []<br></td></tr
><tr
id=sl_svn70_485

 onmouseover="gutterOver(485)"

><td class="source">        parameters = action.parameters<br></td></tr
><tr
id=sl_svn70_486

 onmouseover="gutterOver(486)"

><td class="source">        parameter_types = [parameter.type for parameter in parameters]<br></td></tr
><tr
id=sl_svn70_487

 onmouseover="gutterOver(487)"

><td class="source">        for parameter_type in parameter_types:<br></td></tr
><tr
id=sl_svn70_488

 onmouseover="gutterOver(488)"

><td class="source">            all_objects = self.get_objects(parameter_type,state.objects)<br></td></tr
><tr
id=sl_svn70_489

 onmouseover="gutterOver(489)"

><td class="source">            pairs.append(all_objects)<br></td></tr
><tr
id=sl_svn70_490

 onmouseover="gutterOver(490)"

><td class="source">        para_combinators= [list(comb) for comb in itertools.product(*pairs)]<br></td></tr
><tr
id=sl_svn70_491

 onmouseover="gutterOver(491)"

><td class="source">        for combinator in para_combinators:<br></td></tr
><tr
id=sl_svn70_492

 onmouseover="gutterOver(492)"

><td class="source">            var_mapping = dict([param.name,cob.name] for param,cob in zip(parameters,combinator))<br></td></tr
><tr
id=sl_svn70_493

 onmouseover="gutterOver(493)"

><td class="source">            #To get the fluent_facts based on the var_mapping<br></td></tr
><tr
id=sl_svn70_494

 onmouseover="gutterOver(494)"

><td class="source">            fluent_facts = self.get_fluent_facts(var_mapping,action)<br></td></tr
><tr
id=sl_svn70_495

 onmouseover="gutterOver(495)"

><td class="source">            #To get all the actions based on the generated vara_mapping and fluent_facts<br></td></tr
><tr
id=sl_svn70_496

 onmouseover="gutterOver(496)"

><td class="source">            new_action = action.instantiate(var_mapping,state.problem.init,fluent_facts)<br></td></tr
><tr
id=sl_svn70_497

 onmouseover="gutterOver(497)"

><td class="source">            if new_action:<br></td></tr
><tr
id=sl_svn70_498

 onmouseover="gutterOver(498)"

><td class="source">                actions_result.append(new_action)<br></td></tr
><tr
id=sl_svn70_499

 onmouseover="gutterOver(499)"

><td class="source">        return actions_result<br></td></tr
><tr
id=sl_svn70_500

 onmouseover="gutterOver(500)"

><td class="source">        <br></td></tr
><tr
id=sl_svn70_501

 onmouseover="gutterOver(501)"

><td class="source">    def get_objects(self,parameters_type,objects):<br></td></tr
><tr
id=sl_svn70_502

 onmouseover="gutterOver(502)"

><td class="source">    #To get the objects which meet the type of the parameter<br></td></tr
><tr
id=sl_svn70_503

 onmouseover="gutterOver(503)"

><td class="source">        return [obj for obj in objects if obj.type == parameters_type]<br></td></tr
><tr
id=sl_svn70_504

 onmouseover="gutterOver(504)"

><td class="source">    <br></td></tr
><tr
id=sl_svn70_505

 onmouseover="gutterOver(505)"

><td class="source"> # To parse the conditions   <br></td></tr
><tr
id=sl_svn70_506

 onmouseover="gutterOver(506)"

><td class="source">def parse_condition(alist):<br></td></tr
><tr
id=sl_svn70_507

 onmouseover="gutterOver(507)"

><td class="source">    condition = parse_condition_aux(alist, False)<br></td></tr
><tr
id=sl_svn70_508

 onmouseover="gutterOver(508)"

><td class="source">    return condition<br></td></tr
><tr
id=sl_svn70_509

 onmouseover="gutterOver(509)"

><td class="source">    <br></td></tr
><tr
id=sl_svn70_510

 onmouseover="gutterOver(510)"

><td class="source">def parse_condition_aux(alist, negated):<br></td></tr
><tr
id=sl_svn70_511

 onmouseover="gutterOver(511)"

><td class="source">    tag = alist[0]<br></td></tr
><tr
id=sl_svn70_512

 onmouseover="gutterOver(512)"

><td class="source">    if tag in (&quot;and&quot;, &quot;or&quot;, &quot;not&quot;):<br></td></tr
><tr
id=sl_svn70_513

 onmouseover="gutterOver(513)"

><td class="source">        args = alist[1:]<br></td></tr
><tr
id=sl_svn70_514

 onmouseover="gutterOver(514)"

><td class="source">        if tag == &quot;not&quot;:<br></td></tr
><tr
id=sl_svn70_515

 onmouseover="gutterOver(515)"

><td class="source">            assert len(args) == 1<br></td></tr
><tr
id=sl_svn70_516

 onmouseover="gutterOver(516)"

><td class="source">            return parse_condition_aux(args[0], not negated)<br></td></tr
><tr
id=sl_svn70_517

 onmouseover="gutterOver(517)"

><td class="source">    elif negated:<br></td></tr
><tr
id=sl_svn70_518

 onmouseover="gutterOver(518)"

><td class="source">        return NegatedAtom(alist[0], alist[1:])<br></td></tr
><tr
id=sl_svn70_519

 onmouseover="gutterOver(519)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_520

 onmouseover="gutterOver(520)"

><td class="source">        return Atom(alist[0], alist[1:])<br></td></tr
><tr
id=sl_svn70_521

 onmouseover="gutterOver(521)"

><td class="source">    parts = [parse_condition_aux(part, negated) for part in args]<br></td></tr
><tr
id=sl_svn70_522

 onmouseover="gutterOver(522)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_523

 onmouseover="gutterOver(523)"

><td class="source">    if tag == &quot;and&quot; and not negated or tag == &quot;or&quot; and negated:<br></td></tr
><tr
id=sl_svn70_524

 onmouseover="gutterOver(524)"

><td class="source">        return Conjunction(parts)<br></td></tr
><tr
id=sl_svn70_525

 onmouseover="gutterOver(525)"

><td class="source">    elif tag == &quot;or&quot; and not negated or tag == &quot;and&quot; and negated:<br></td></tr
><tr
id=sl_svn70_526

 onmouseover="gutterOver(526)"

><td class="source">        return Disjunction(parts)<br></td></tr
><tr
id=sl_svn70_527

 onmouseover="gutterOver(527)"

><td class="source">        <br></td></tr
><tr
id=sl_svn70_528

 onmouseover="gutterOver(528)"

><td class="source"># To parse the literals<br></td></tr
><tr
id=sl_svn70_529

 onmouseover="gutterOver(529)"

><td class="source">def parse_literal(alist):<br></td></tr
><tr
id=sl_svn70_530

 onmouseover="gutterOver(530)"

><td class="source">    if alist[0] == &quot;not&quot;:<br></td></tr
><tr
id=sl_svn70_531

 onmouseover="gutterOver(531)"

><td class="source">        assert len(alist) == 2<br></td></tr
><tr
id=sl_svn70_532

 onmouseover="gutterOver(532)"

><td class="source">        alist = alist[1]<br></td></tr
><tr
id=sl_svn70_533

 onmouseover="gutterOver(533)"

><td class="source">        return NegatedAtom(alist[0], alist[1:])<br></td></tr
><tr
id=sl_svn70_534

 onmouseover="gutterOver(534)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_535

 onmouseover="gutterOver(535)"

><td class="source">        return Atom(alist[0], alist[1:])<br></td></tr
><tr
id=sl_svn70_536

 onmouseover="gutterOver(536)"

><td class="source"># To parse the terms<br></td></tr
><tr
id=sl_svn70_537

 onmouseover="gutterOver(537)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_538

 onmouseover="gutterOver(538)"

><td class="source">def parse_term(term):<br></td></tr
><tr
id=sl_svn70_539

 onmouseover="gutterOver(539)"

><td class="source">    if isinstance(term, list): <br></td></tr
><tr
id=sl_svn70_540

 onmouseover="gutterOver(540)"

><td class="source">        return FunctionTerm(term[0],[parse_term(t) for t in term[1:]])<br></td></tr
><tr
id=sl_svn70_541

 onmouseover="gutterOver(541)"

><td class="source">    elif term.startswith(&quot;?&quot;):<br></td></tr
><tr
id=sl_svn70_542

 onmouseover="gutterOver(542)"

><td class="source">        return Variable(term)<br></td></tr
><tr
id=sl_svn70_543

 onmouseover="gutterOver(543)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_544

 onmouseover="gutterOver(544)"

><td class="source">        return ObjectTerm(term)<br></td></tr
><tr
id=sl_svn70_545

 onmouseover="gutterOver(545)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_546

 onmouseover="gutterOver(546)"

><td class="source">def transitive_closure(pairs):<br></td></tr
><tr
id=sl_svn70_547

 onmouseover="gutterOver(547)"

><td class="source">    result = set(pairs)<br></td></tr
><tr
id=sl_svn70_548

 onmouseover="gutterOver(548)"

><td class="source">    nodes = set(u for (u, v) in pairs) | set(v for (u, v) in pairs)<br></td></tr
><tr
id=sl_svn70_549

 onmouseover="gutterOver(549)"

><td class="source">    for k in nodes:<br></td></tr
><tr
id=sl_svn70_550

 onmouseover="gutterOver(550)"

><td class="source">        for i in nodes:<br></td></tr
><tr
id=sl_svn70_551

 onmouseover="gutterOver(551)"

><td class="source">            for j in nodes:<br></td></tr
><tr
id=sl_svn70_552

 onmouseover="gutterOver(552)"

><td class="source">                if (i, j) not in result and (i, k) in result and (k, j) in result:<br></td></tr
><tr
id=sl_svn70_553

 onmouseover="gutterOver(553)"

><td class="source">                    result.add((i, j))<br></td></tr
><tr
id=sl_svn70_554

 onmouseover="gutterOver(554)"

><td class="source">    return sorted(result)<br></td></tr
><tr
id=sl_svn70_555

 onmouseover="gutterOver(555)"

><td class="source">    <br></td></tr
><tr
id=sl_svn70_556

 onmouseover="gutterOver(556)"

><td class="source">def set_uppertypes(type_list):<br></td></tr
><tr
id=sl_svn70_557

 onmouseover="gutterOver(557)"

><td class="source">    typename_to_type = {}<br></td></tr
><tr
id=sl_svn70_558

 onmouseover="gutterOver(558)"

><td class="source">    child_types = []<br></td></tr
><tr
id=sl_svn70_559

 onmouseover="gutterOver(559)"

><td class="source">    for type in type_list:<br></td></tr
><tr
id=sl_svn70_560

 onmouseover="gutterOver(560)"

><td class="source">        type.supertype_names = []<br></td></tr
><tr
id=sl_svn70_561

 onmouseover="gutterOver(561)"

><td class="source">        typename_to_type[type.name] = type<br></td></tr
><tr
id=sl_svn70_562

 onmouseover="gutterOver(562)"

><td class="source">        if type.basetype_name:<br></td></tr
><tr
id=sl_svn70_563

 onmouseover="gutterOver(563)"

><td class="source">            child_types.append((type.name, type.basetype_name))<br></td></tr
><tr
id=sl_svn70_564

 onmouseover="gutterOver(564)"

><td class="source">    for (desc_name, anc_name) in transitive_closure(child_types):<br></td></tr
><tr
id=sl_svn70_565

 onmouseover="gutterOver(565)"

><td class="source">        typename_to_type[desc_name].supertype_names.append(anc_name)<br></td></tr
><tr
id=sl_svn70_566

 onmouseover="gutterOver(566)"

><td class="source">        <br></td></tr
><tr
id=sl_svn70_567

 onmouseover="gutterOver(567)"

><td class="source"># To parse the effects<br></td></tr
><tr
id=sl_svn70_568

 onmouseover="gutterOver(568)"

><td class="source">def parse_effects(alist, result):<br></td></tr
><tr
id=sl_svn70_569

 onmouseover="gutterOver(569)"

><td class="source">    tmp_effect = parse_effect(alist)<br></td></tr
><tr
id=sl_svn70_570

 onmouseover="gutterOver(570)"

><td class="source">    normalized = tmp_effect.normalize()<br></td></tr
><tr
id=sl_svn70_571

 onmouseover="gutterOver(571)"

><td class="source">    cost_eff, rest_effect = normalized.extract_cost()<br></td></tr
><tr
id=sl_svn70_572

 onmouseover="gutterOver(572)"

><td class="source">    add_effect(rest_effect, result)<br></td></tr
><tr
id=sl_svn70_573

 onmouseover="gutterOver(573)"

><td class="source">    if cost_eff:<br></td></tr
><tr
id=sl_svn70_574

 onmouseover="gutterOver(574)"

><td class="source">        return cost_eff.effect<br></td></tr
><tr
id=sl_svn70_575

 onmouseover="gutterOver(575)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_576

 onmouseover="gutterOver(576)"

><td class="source">        return None<br></td></tr
><tr
id=sl_svn70_577

 onmouseover="gutterOver(577)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_578

 onmouseover="gutterOver(578)"

><td class="source">def add_effect(tmp_effect, result):<br></td></tr
><tr
id=sl_svn70_579

 onmouseover="gutterOver(579)"

><td class="source">    if isinstance(tmp_effect, ConjunctiveEffect):<br></td></tr
><tr
id=sl_svn70_580

 onmouseover="gutterOver(580)"

><td class="source">        for effect in tmp_effect.effects:<br></td></tr
><tr
id=sl_svn70_581

 onmouseover="gutterOver(581)"

><td class="source">            add_effect(effect, result)<br></td></tr
><tr
id=sl_svn70_582

 onmouseover="gutterOver(582)"

><td class="source">        return<br></td></tr
><tr
id=sl_svn70_583

 onmouseover="gutterOver(583)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_584

 onmouseover="gutterOver(584)"

><td class="source">        parameters = []<br></td></tr
><tr
id=sl_svn70_585

 onmouseover="gutterOver(585)"

><td class="source">        condition = Truth()<br></td></tr
><tr
id=sl_svn70_586

 onmouseover="gutterOver(586)"

><td class="source">        assert isinstance(tmp_effect, SimpleEffect)<br></td></tr
><tr
id=sl_svn70_587

 onmouseover="gutterOver(587)"

><td class="source">        effect = tmp_effect.effect<br></td></tr
><tr
id=sl_svn70_588

 onmouseover="gutterOver(588)"

><td class="source">        assert isinstance(effect, Literal)<br></td></tr
><tr
id=sl_svn70_589

 onmouseover="gutterOver(589)"

><td class="source">        # Check for contradictory effects<br></td></tr
><tr
id=sl_svn70_590

 onmouseover="gutterOver(590)"

><td class="source">        new_effect = Effect(parameters, condition, effect)<br></td></tr
><tr
id=sl_svn70_591

 onmouseover="gutterOver(591)"

><td class="source">        contradiction = Effect(parameters, condition, effect.negate())<br></td></tr
><tr
id=sl_svn70_592

 onmouseover="gutterOver(592)"

><td class="source">        if not contradiction in result:<br></td></tr
><tr
id=sl_svn70_593

 onmouseover="gutterOver(593)"

><td class="source">            result.append(new_effect)<br></td></tr
><tr
id=sl_svn70_594

 onmouseover="gutterOver(594)"

><td class="source">        else:<br></td></tr
><tr
id=sl_svn70_595

 onmouseover="gutterOver(595)"

><td class="source">            if isinstance(contradiction.literal, NegatedAtom):<br></td></tr
><tr
id=sl_svn70_596

 onmouseover="gutterOver(596)"

><td class="source">                result.remove(contradiction)<br></td></tr
><tr
id=sl_svn70_597

 onmouseover="gutterOver(597)"

><td class="source">                result.append(new_effect)<br></td></tr
><tr
id=sl_svn70_598

 onmouseover="gutterOver(598)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_599

 onmouseover="gutterOver(599)"

><td class="source">def parse_effect(alist):<br></td></tr
><tr
id=sl_svn70_600

 onmouseover="gutterOver(600)"

><td class="source">    tag = alist[0]<br></td></tr
><tr
id=sl_svn70_601

 onmouseover="gutterOver(601)"

><td class="source">    if tag == &quot;and&quot;:<br></td></tr
><tr
id=sl_svn70_602

 onmouseover="gutterOver(602)"

><td class="source">        return ConjunctiveEffect([parse_effect(eff) for eff in alist[1:]])<br></td></tr
><tr
id=sl_svn70_603

 onmouseover="gutterOver(603)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_604

 onmouseover="gutterOver(604)"

><td class="source">        return SimpleEffect(parse_literal(alist))<br></td></tr
><tr
id=sl_svn70_605

 onmouseover="gutterOver(605)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_606

 onmouseover="gutterOver(606)"

><td class="source">def parse_typed_list(alist, only_variables=False, constructor=TypedObject, functions=False):<br></td></tr
><tr
id=sl_svn70_607

 onmouseover="gutterOver(607)"

><td class="source">    result = []<br></td></tr
><tr
id=sl_svn70_608

 onmouseover="gutterOver(608)"

><td class="source">    while alist:<br></td></tr
><tr
id=sl_svn70_609

 onmouseover="gutterOver(609)"

><td class="source">        try:<br></td></tr
><tr
id=sl_svn70_610

 onmouseover="gutterOver(610)"

><td class="source">            separator_position = alist.index(&quot;-&quot;)<br></td></tr
><tr
id=sl_svn70_611

 onmouseover="gutterOver(611)"

><td class="source">        except ValueError:<br></td></tr
><tr
id=sl_svn70_612

 onmouseover="gutterOver(612)"

><td class="source">            items = alist<br></td></tr
><tr
id=sl_svn70_613

 onmouseover="gutterOver(613)"

><td class="source">            if functions:<br></td></tr
><tr
id=sl_svn70_614

 onmouseover="gutterOver(614)"

><td class="source">                _type = &quot;number&quot;<br></td></tr
><tr
id=sl_svn70_615

 onmouseover="gutterOver(615)"

><td class="source">            else:<br></td></tr
><tr
id=sl_svn70_616

 onmouseover="gutterOver(616)"

><td class="source">                _type = &quot;object&quot;<br></td></tr
><tr
id=sl_svn70_617

 onmouseover="gutterOver(617)"

><td class="source">            alist = []<br></td></tr
><tr
id=sl_svn70_618

 onmouseover="gutterOver(618)"

><td class="source">        else:<br></td></tr
><tr
id=sl_svn70_619

 onmouseover="gutterOver(619)"

><td class="source">            items = alist[:separator_position]<br></td></tr
><tr
id=sl_svn70_620

 onmouseover="gutterOver(620)"

><td class="source">            _type = alist[separator_position + 1]<br></td></tr
><tr
id=sl_svn70_621

 onmouseover="gutterOver(621)"

><td class="source">            alist = alist[separator_position + 2:]<br></td></tr
><tr
id=sl_svn70_622

 onmouseover="gutterOver(622)"

><td class="source">        for item in items:<br></td></tr
><tr
id=sl_svn70_623

 onmouseover="gutterOver(623)"

><td class="source">            assert not only_variables or item.startswith(&quot;?&quot;)<br></td></tr
><tr
id=sl_svn70_624

 onmouseover="gutterOver(624)"

><td class="source">            entry = constructor(item, _type)<br></td></tr
><tr
id=sl_svn70_625

 onmouseover="gutterOver(625)"

><td class="source">            result.append(entry)<br></td></tr
><tr
id=sl_svn70_626

 onmouseover="gutterOver(626)"

><td class="source">    return result<br></td></tr
><tr
id=sl_svn70_627

 onmouseover="gutterOver(627)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_628

 onmouseover="gutterOver(628)"

><td class="source"># To parse the nested list<br></td></tr
><tr
id=sl_svn70_629

 onmouseover="gutterOver(629)"

><td class="source">def parse_nested_list(input_file):<br></td></tr
><tr
id=sl_svn70_630

 onmouseover="gutterOver(630)"

><td class="source">    # tokenize the input file<br></td></tr
><tr
id=sl_svn70_631

 onmouseover="gutterOver(631)"

><td class="source">    tokens = tokenize(input_file)<br></td></tr
><tr
id=sl_svn70_632

 onmouseover="gutterOver(632)"

><td class="source">    next_token = tokens.next()<br></td></tr
><tr
id=sl_svn70_633

 onmouseover="gutterOver(633)"

><td class="source">    if next_token != &quot;(&quot;:<br></td></tr
><tr
id=sl_svn70_634

 onmouseover="gutterOver(634)"

><td class="source">        raise  SystemExit(&quot;Expected &#39;(&#39;, got %s.&quot; % next_token)<br></td></tr
><tr
id=sl_svn70_635

 onmouseover="gutterOver(635)"

><td class="source">    result = list(parse_list_assist(tokens))<br></td></tr
><tr
id=sl_svn70_636

 onmouseover="gutterOver(636)"

><td class="source">    # Check that generator is exhausted.<br></td></tr
><tr
id=sl_svn70_637

 onmouseover="gutterOver(637)"

><td class="source">    for tok in tokens:  <br></td></tr
><tr
id=sl_svn70_638

 onmouseover="gutterOver(638)"

><td class="source">        raise SystemExit(&quot;Unexpected token: %s.&quot; % tok)<br></td></tr
><tr
id=sl_svn70_639

 onmouseover="gutterOver(639)"

><td class="source">    return result<br></td></tr
><tr
id=sl_svn70_640

 onmouseover="gutterOver(640)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_641

 onmouseover="gutterOver(641)"

><td class="source">def tokenize(input):<br></td></tr
><tr
id=sl_svn70_642

 onmouseover="gutterOver(642)"

><td class="source">    for line in input:<br></td></tr
><tr
id=sl_svn70_643

 onmouseover="gutterOver(643)"

><td class="source">        line = line.split(&quot;;&quot;, 1)[0]  # Strip comments.<br></td></tr
><tr
id=sl_svn70_644

 onmouseover="gutterOver(644)"

><td class="source">        # Add space<br></td></tr
><tr
id=sl_svn70_645

 onmouseover="gutterOver(645)"

><td class="source">        line = line.replace(&quot;(&quot;, &quot; ( &quot;).replace(&quot;)&quot;, &quot; ) &quot;).replace(&quot;?&quot;, &quot; ?&quot;) <br></td></tr
><tr
id=sl_svn70_646

 onmouseover="gutterOver(646)"

><td class="source">        for token in line.split():<br></td></tr
><tr
id=sl_svn70_647

 onmouseover="gutterOver(647)"

><td class="source">            yield token.lower()<br></td></tr
><tr
id=sl_svn70_648

 onmouseover="gutterOver(648)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_649

 onmouseover="gutterOver(649)"

><td class="source"># To parse the tokenstream without the pair of the parenthese<br></td></tr
><tr
id=sl_svn70_650

 onmouseover="gutterOver(650)"

><td class="source">def parse_list_assist(tokenstream):<br></td></tr
><tr
id=sl_svn70_651

 onmouseover="gutterOver(651)"

><td class="source">    # Leading &quot;(&quot; has already been swallowed.<br></td></tr
><tr
id=sl_svn70_652

 onmouseover="gutterOver(652)"

><td class="source">    while True:<br></td></tr
><tr
id=sl_svn70_653

 onmouseover="gutterOver(653)"

><td class="source">        try:<br></td></tr
><tr
id=sl_svn70_654

 onmouseover="gutterOver(654)"

><td class="source">            token = tokenstream.next()<br></td></tr
><tr
id=sl_svn70_655

 onmouseover="gutterOver(655)"

><td class="source">        except StopIteration:<br></td></tr
><tr
id=sl_svn70_656

 onmouseover="gutterOver(656)"

><td class="source">            raise ParseError()<br></td></tr
><tr
id=sl_svn70_657

 onmouseover="gutterOver(657)"

><td class="source">        if token == &quot;)&quot;:<br></td></tr
><tr
id=sl_svn70_658

 onmouseover="gutterOver(658)"

><td class="source">            return<br></td></tr
><tr
id=sl_svn70_659

 onmouseover="gutterOver(659)"

><td class="source">        elif token == &quot;(&quot;:<br></td></tr
><tr
id=sl_svn70_660

 onmouseover="gutterOver(660)"

><td class="source">            yield list(parse_list_assist(tokenstream))<br></td></tr
><tr
id=sl_svn70_661

 onmouseover="gutterOver(661)"

><td class="source">        else:<br></td></tr
><tr
id=sl_svn70_662

 onmouseover="gutterOver(662)"

><td class="source">            yield token<br></td></tr
><tr
id=sl_svn70_663

 onmouseover="gutterOver(663)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_664

 onmouseover="gutterOver(664)"

><td class="source"># To parse a pddl file: domain or problem<br></td></tr
><tr
id=sl_svn70_665

 onmouseover="gutterOver(665)"

><td class="source">def parse_pddl(type, filename):<br></td></tr
><tr
id=sl_svn70_666

 onmouseover="gutterOver(666)"

><td class="source">    try:<br></td></tr
><tr
id=sl_svn70_667

 onmouseover="gutterOver(667)"

><td class="source">        return parse_nested_list(file(filename))<br></td></tr
><tr
id=sl_svn70_668

 onmouseover="gutterOver(668)"

><td class="source">    except IOError, e:<br></td></tr
><tr
id=sl_svn70_669

 onmouseover="gutterOver(669)"

><td class="source">        raise SystemExit(&quot;Error: Can not read file: %s\nReason: %s.&quot; %<br></td></tr
><tr
id=sl_svn70_670

 onmouseover="gutterOver(670)"

><td class="source">                         (e.filename, e))<br></td></tr
><tr
id=sl_svn70_671

 onmouseover="gutterOver(671)"

><td class="source">    except ParseError, e:<br></td></tr
><tr
id=sl_svn70_672

 onmouseover="gutterOver(672)"

><td class="source">        raise SystemExit(&quot;Error: Can not parse %s file: %s\n&quot; % (type, filename))<br></td></tr
><tr
id=sl_svn70_673

 onmouseover="gutterOver(673)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_674

 onmouseover="gutterOver(674)"

><td class="source"># Parse the domain pddl<br></td></tr
><tr
id=sl_svn70_675

 onmouseover="gutterOver(675)"

><td class="source">def parse_domain(domain_pddl):<br></td></tr
><tr
id=sl_svn70_676

 onmouseover="gutterOver(676)"

><td class="source">    iterator = iter(domain_pddl)<br></td></tr
><tr
id=sl_svn70_677

 onmouseover="gutterOver(677)"

><td class="source">    <br></td></tr
><tr
id=sl_svn70_678

 onmouseover="gutterOver(678)"

><td class="source">    # To assure that the file is a domain file<br></td></tr
><tr
id=sl_svn70_679

 onmouseover="gutterOver(679)"

><td class="source">    if iterator.next() == &quot;define&quot;:<br></td></tr
><tr
id=sl_svn70_680

 onmouseover="gutterOver(680)"

><td class="source">         pass<br></td></tr
><tr
id=sl_svn70_681

 onmouseover="gutterOver(681)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_682

 onmouseover="gutterOver(682)"

><td class="source">         raise SystemExit(&quot;Error! This domain PDDL file is not a standard typed STRIPS PDDL file. It should begin with the keyword: define&quot;)<br></td></tr
><tr
id=sl_svn70_683

 onmouseover="gutterOver(683)"

><td class="source">    domain_name = iterator.next()<br></td></tr
><tr
id=sl_svn70_684

 onmouseover="gutterOver(684)"

><td class="source">    <br></td></tr
><tr
id=sl_svn70_685

 onmouseover="gutterOver(685)"

><td class="source">    # To get the domain name<br></td></tr
><tr
id=sl_svn70_686

 onmouseover="gutterOver(686)"

><td class="source">    if domain_name[0] == &quot;domain&quot; and len(domain_name) == 2:<br></td></tr
><tr
id=sl_svn70_687

 onmouseover="gutterOver(687)"

><td class="source">        yield domain_name[1]<br></td></tr
><tr
id=sl_svn70_688

 onmouseover="gutterOver(688)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_689

 onmouseover="gutterOver(689)"

><td class="source">        raise SystemExit(&quot;Error! This domain PDDL file is not a standard typed STRIPS PDDL file. It should begin with include the definition of domain&quot;)<br></td></tr
><tr
id=sl_svn70_690

 onmouseover="gutterOver(690)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_691

 onmouseover="gutterOver(691)"

><td class="source">    requirements_option = iterator.next()<br></td></tr
><tr
id=sl_svn70_692

 onmouseover="gutterOver(692)"

><td class="source">    # To get the requirements<br></td></tr
><tr
id=sl_svn70_693

 onmouseover="gutterOver(693)"

><td class="source">    if  requirements_option[0]==&quot;:requirements&quot; and len(requirements_option)==2:<br></td></tr
><tr
id=sl_svn70_694

 onmouseover="gutterOver(694)"

><td class="source">        yield requirements_option[1]<br></td></tr
><tr
id=sl_svn70_695

 onmouseover="gutterOver(695)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_696

 onmouseover="gutterOver(696)"

><td class="source">        raise SystemExit(&quot;Error! This domain PDDL file is not a standard typed STRIPS PDDL file. It should include only one requirement!&quot;)<br></td></tr
><tr
id=sl_svn70_697

 onmouseover="gutterOver(697)"

><td class="source">        <br></td></tr
><tr
id=sl_svn70_698

 onmouseover="gutterOver(698)"

><td class="source">    types_option = iterator.next()<br></td></tr
><tr
id=sl_svn70_699

 onmouseover="gutterOver(699)"

><td class="source">    # To get the types or typing<br></td></tr
><tr
id=sl_svn70_700

 onmouseover="gutterOver(700)"

><td class="source">    if  types_option[0]==&#39;:typing&#39; or types_option[0]==&#39;:type&#39;:<br></td></tr
><tr
id=sl_svn70_701

 onmouseover="gutterOver(701)"

><td class="source">        types_result = [Type(&quot;object&quot;)] # Add object to the types<br></td></tr
><tr
id=sl_svn70_702

 onmouseover="gutterOver(702)"

><td class="source">        types_result.extend(parse_typed_list(types_option[1:], constructor=Type))<br></td></tr
><tr
id=sl_svn70_703

 onmouseover="gutterOver(703)"

><td class="source">        set_uppertypes(types_result)<br></td></tr
><tr
id=sl_svn70_704

 onmouseover="gutterOver(704)"

><td class="source">        yield types_result<br></td></tr
><tr
id=sl_svn70_705

 onmouseover="gutterOver(705)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_706

 onmouseover="gutterOver(706)"

><td class="source">        raise SystemExit(&quot;Error! This domain PDDL file is not a standard typed STRIPS PDDL file. It should include at least one type&quot;)<br></td></tr
><tr
id=sl_svn70_707

 onmouseover="gutterOver(707)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_708

 onmouseover="gutterOver(708)"

><td class="source">    constants_option = iterator.next()<br></td></tr
><tr
id=sl_svn70_709

 onmouseover="gutterOver(709)"

><td class="source">    # To get the constants if any<br></td></tr
><tr
id=sl_svn70_710

 onmouseover="gutterOver(710)"

><td class="source">    if constants_option[0] == &quot;:constants&quot;:<br></td></tr
><tr
id=sl_svn70_711

 onmouseover="gutterOver(711)"

><td class="source">        yield parse_typed_list(constants_option[1:])<br></td></tr
><tr
id=sl_svn70_712

 onmouseover="gutterOver(712)"

><td class="source">        pred = iterator.next()<br></td></tr
><tr
id=sl_svn70_713

 onmouseover="gutterOver(713)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_714

 onmouseover="gutterOver(714)"

><td class="source">        yield []<br></td></tr
><tr
id=sl_svn70_715

 onmouseover="gutterOver(715)"

><td class="source">        pred = constants_option<br></td></tr
><tr
id=sl_svn70_716

 onmouseover="gutterOver(716)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_717

 onmouseover="gutterOver(717)"

><td class="source">    # To get  predicates<br></td></tr
><tr
id=sl_svn70_718

 onmouseover="gutterOver(718)"

><td class="source">    if pred[0] == &quot;:predicates&quot;:<br></td></tr
><tr
id=sl_svn70_719

 onmouseover="gutterOver(719)"

><td class="source">        yield ([Predicate.parse(entry) for entry in pred[1:]] +<br></td></tr
><tr
id=sl_svn70_720

 onmouseover="gutterOver(720)"

><td class="source">           [Predicate(&quot;=&quot;,<br></td></tr
><tr
id=sl_svn70_721

 onmouseover="gutterOver(721)"

><td class="source">                                 [TypedObject(&quot;?x&quot;, &quot;object&quot;),<br></td></tr
><tr
id=sl_svn70_722

 onmouseover="gutterOver(722)"

><td class="source">                                 TypedObject(&quot;?y&quot;, &quot;object&quot;)])])<br></td></tr
><tr
id=sl_svn70_723

 onmouseover="gutterOver(723)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_724

 onmouseover="gutterOver(724)"

><td class="source">        raise SystemExit(&quot;Error! This domain PDDL file is not a standard typed STRIPS PDDL file. It should include predicates&quot;)<br></td></tr
><tr
id=sl_svn70_725

 onmouseover="gutterOver(725)"

><td class="source">                                  <br></td></tr
><tr
id=sl_svn70_726

 onmouseover="gutterOver(726)"

><td class="source">    first_action = iterator.next()<br></td></tr
><tr
id=sl_svn70_727

 onmouseover="gutterOver(727)"

><td class="source">    entries = [first_action] + [entry for entry in iterator]<br></td></tr
><tr
id=sl_svn70_728

 onmouseover="gutterOver(728)"

><td class="source">    the_actions = []<br></td></tr
><tr
id=sl_svn70_729

 onmouseover="gutterOver(729)"

><td class="source">    for entry in entries:<br></td></tr
><tr
id=sl_svn70_730

 onmouseover="gutterOver(730)"

><td class="source">        action = Action.parse(entry)<br></td></tr
><tr
id=sl_svn70_731

 onmouseover="gutterOver(731)"

><td class="source">        the_actions.append(action)<br></td></tr
><tr
id=sl_svn70_732

 onmouseover="gutterOver(732)"

><td class="source">    yield the_actions<br></td></tr
><tr
id=sl_svn70_733

 onmouseover="gutterOver(733)"

><td class="source"># To Parse the problem pddl<br></td></tr
><tr
id=sl_svn70_734

 onmouseover="gutterOver(734)"

><td class="source">def parse_problem(problem_pddl):<br></td></tr
><tr
id=sl_svn70_735

 onmouseover="gutterOver(735)"

><td class="source">    iterator = iter(problem_pddl)<br></td></tr
><tr
id=sl_svn70_736

 onmouseover="gutterOver(736)"

><td class="source">    if iterator.next() == &quot;define&quot;:<br></td></tr
><tr
id=sl_svn70_737

 onmouseover="gutterOver(737)"

><td class="source">        pass<br></td></tr
><tr
id=sl_svn70_738

 onmouseover="gutterOver(738)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_739

 onmouseover="gutterOver(739)"

><td class="source">        raise SystemExit(&quot;Error! This problem PDDL file is not a standard typed STRIPS PDDL file. It should begin with the keyword: define&quot;)<br></td></tr
><tr
id=sl_svn70_740

 onmouseover="gutterOver(740)"

><td class="source">    problem_line = iterator.next()<br></td></tr
><tr
id=sl_svn70_741

 onmouseover="gutterOver(741)"

><td class="source">    if problem_line[0] == &quot;problem&quot; and len(problem_line) == 2:<br></td></tr
><tr
id=sl_svn70_742

 onmouseover="gutterOver(742)"

><td class="source">        yield problem_line[1]<br></td></tr
><tr
id=sl_svn70_743

 onmouseover="gutterOver(743)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_744

 onmouseover="gutterOver(744)"

><td class="source">         raise SystemExit(&quot;Error! This problem PDDL file is not a standard typed STRIPS PDDL file. It should include name of the problem&quot;)<br></td></tr
><tr
id=sl_svn70_745

 onmouseover="gutterOver(745)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_746

 onmouseover="gutterOver(746)"

><td class="source">    domain_line = iterator.next()<br></td></tr
><tr
id=sl_svn70_747

 onmouseover="gutterOver(747)"

><td class="source">    assert domain_line[0] == &quot;:domain&quot; and len(domain_line) == 2<br></td></tr
><tr
id=sl_svn70_748

 onmouseover="gutterOver(748)"

><td class="source">    yield domain_line[1]<br></td></tr
><tr
id=sl_svn70_749

 onmouseover="gutterOver(749)"

><td class="source">    requirements_line = iterator.next()<br></td></tr
><tr
id=sl_svn70_750

 onmouseover="gutterOver(750)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_751

 onmouseover="gutterOver(751)"

><td class="source">    if  requirements_line[0] ==&quot;:requirements&quot; and len(requirements_line) == 2:<br></td></tr
><tr
id=sl_svn70_752

 onmouseover="gutterOver(752)"

><td class="source">        yield requirements_line[1]<br></td></tr
><tr
id=sl_svn70_753

 onmouseover="gutterOver(753)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_754

 onmouseover="gutterOver(754)"

><td class="source">        raise SystemExit(&quot;Error! This problem PDDL file is not a standard typed STRIPS PDDL file. It should include only one requirement!&quot;)<br></td></tr
><tr
id=sl_svn70_755

 onmouseover="gutterOver(755)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_756

 onmouseover="gutterOver(756)"

><td class="source">    objects_opt = iterator.next()<br></td></tr
><tr
id=sl_svn70_757

 onmouseover="gutterOver(757)"

><td class="source">    if objects_opt[0] == &quot;:objects&quot;:<br></td></tr
><tr
id=sl_svn70_758

 onmouseover="gutterOver(758)"

><td class="source">        yield parse_typed_list(objects_opt[1:])<br></td></tr
><tr
id=sl_svn70_759

 onmouseover="gutterOver(759)"

><td class="source">        init = iterator.next()<br></td></tr
><tr
id=sl_svn70_760

 onmouseover="gutterOver(760)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_761

 onmouseover="gutterOver(761)"

><td class="source">        yield []<br></td></tr
><tr
id=sl_svn70_762

 onmouseover="gutterOver(762)"

><td class="source">        init = objects_opt<br></td></tr
><tr
id=sl_svn70_763

 onmouseover="gutterOver(763)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_764

 onmouseover="gutterOver(764)"

><td class="source">    if init[0] == &quot;:init&quot;:<br></td></tr
><tr
id=sl_svn70_765

 onmouseover="gutterOver(765)"

><td class="source">        initial = []<br></td></tr
><tr
id=sl_svn70_766

 onmouseover="gutterOver(766)"

><td class="source">        for fact in init[1:]:<br></td></tr
><tr
id=sl_svn70_767

 onmouseover="gutterOver(767)"

><td class="source">            initial.append(Atom(fact[0], fact[1:]))<br></td></tr
><tr
id=sl_svn70_768

 onmouseover="gutterOver(768)"

><td class="source">        yield initial<br></td></tr
><tr
id=sl_svn70_769

 onmouseover="gutterOver(769)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_770

 onmouseover="gutterOver(770)"

><td class="source">        raise SystemExit(&quot;Error! This domain PDDL file is not a standard typed STRIPS PDDL file. It should include inits&quot;)<br></td></tr
><tr
id=sl_svn70_771

 onmouseover="gutterOver(771)"

><td class="source">    goal = iterator.next()<br></td></tr
><tr
id=sl_svn70_772

 onmouseover="gutterOver(772)"

><td class="source">    if goal[0] == &quot;:goal&quot; and len(goal) == 2:<br></td></tr
><tr
id=sl_svn70_773

 onmouseover="gutterOver(773)"

><td class="source">        yield parse_condition(goal[1])<br></td></tr
><tr
id=sl_svn70_774

 onmouseover="gutterOver(774)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn70_775

 onmouseover="gutterOver(775)"

><td class="source">        raise SystemExit(&quot;Error! This domain PDDL file is not a standard typed STRIPS PDDL file. It should include goals&quot;)<br></td></tr
><tr
id=sl_svn70_776

 onmouseover="gutterOver(776)"

><td class="source">    <br></td></tr
><tr
id=sl_svn70_777

 onmouseover="gutterOver(777)"

><td class="source">    for entry in iterator:<br></td></tr
><tr
id=sl_svn70_778

 onmouseover="gutterOver(778)"

><td class="source">        assert False, entry<br></td></tr
><tr
id=sl_svn70_779

 onmouseover="gutterOver(779)"

><td class="source"><br></td></tr
><tr
id=sl_svn70_780

 onmouseover="gutterOver(780)"

><td class="source">def loadIntoProblem(domainFile=None, problemFile=None):<br></td></tr
><tr
id=sl_svn70_781

 onmouseover="gutterOver(781)"

><td class="source">    domain= Domain.get_instance(domainFile)<br></td></tr
><tr
id=sl_svn70_782

 onmouseover="gutterOver(782)"

><td class="source">    problem= Problem.get_instance(problemFile)<br></td></tr
><tr
id=sl_svn70_783

 onmouseover="gutterOver(783)"

><td class="source">    return Task(domain, problem)<br></td></tr
><tr
id=sl_svn70_784

 onmouseover="gutterOver(784)"

><td class="source">    <br></td></tr
><tr
id=sl_svn70_785

 onmouseover="gutterOver(785)"

><td class="source"># For Start, remove it if necessary<br></td></tr
><tr
id=sl_svn70_786

 onmouseover="gutterOver(786)"

><td class="source">if __name__ == &quot;__main__&quot;:<br></td></tr
><tr
id=sl_svn70_787

 onmouseover="gutterOver(787)"

><td class="source">    # Please change the domainFile and problemFile if necessary, these two files should be in the working directory.<br></td></tr
><tr
id=sl_svn70_788

 onmouseover="gutterOver(788)"

><td class="source">    domainFile =&quot;domain1.pddl&quot;<br></td></tr
><tr
id=sl_svn70_789

 onmouseover="gutterOver(789)"

><td class="source">    problemFile =&quot;problem1.pddl&quot;<br></td></tr
><tr
id=sl_svn70_790

 onmouseover="gutterOver(790)"

><td class="source">    <br></td></tr
><tr
id=sl_svn70_791

 onmouseover="gutterOver(791)"

><td class="source">    task= loadIntoProblem(domainFile,problemFile)<br></td></tr
><tr
id=sl_svn70_792

 onmouseover="gutterOver(792)"

><td class="source">    domain= Domain.get_instance(domainFile)<br></td></tr
><tr
id=sl_svn70_793

 onmouseover="gutterOver(793)"

><td class="source">    problem= Problem.get_instance(problemFile)<br></td></tr
><tr
id=sl_svn70_794

 onmouseover="gutterOver(794)"

><td class="source">    # Test the parser<br></td></tr
><tr
id=sl_svn70_795

 onmouseover="gutterOver(795)"

><td class="source">    domain.printer()<br></td></tr
><tr
id=sl_svn70_796

 onmouseover="gutterOver(796)"

><td class="source">    problem.printer()<br></td></tr
><tr
id=sl_svn70_797

 onmouseover="gutterOver(797)"

><td class="source">    task_state = State(domain,problem )<br></td></tr
><tr
id=sl_svn70_798

 onmouseover="gutterOver(798)"

><td class="source">    successor = task.successor(task_state)<br></td></tr
><tr
id=sl_svn70_799

 onmouseover="gutterOver(799)"

><td class="source">    # Test the successor<br></td></tr
><tr
id=sl_svn70_800

 onmouseover="gutterOver(800)"

><td class="source">    print successor<br></td></tr
><tr
id=sl_svn70_801

 onmouseover="gutterOver(801)"

><td class="source">   <br></td></tr
><tr
id=sl_svn70_802

 onmouseover="gutterOver(802)"

><td class="source">  <br></td></tr
></table></pre>
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
</td>
</tr></table>

 
<script type="text/javascript">
 var lineNumUnderMouse = -1;
 
 function gutterOver(num) {
 gutterOut();
 var newTR = document.getElementById('gr_svn70_' + num);
 if (newTR) {
 newTR.className = 'undermouse';
 }
 lineNumUnderMouse = num;
 }
 function gutterOut() {
 if (lineNumUnderMouse != -1) {
 var oldTR = document.getElementById(
 'gr_svn70_' + lineNumUnderMouse);
 if (oldTR) {
 oldTR.className = '';
 }
 lineNumUnderMouse = -1;
 }
 }
 var numsGenState = {table_base_id: 'nums_table_'};
 var srcGenState = {table_base_id: 'src_table_'};
 var alignerRunning = false;
 var startOver = false;
 function setLineNumberHeights() {
 if (alignerRunning) {
 startOver = true;
 return;
 }
 numsGenState.chunk_id = 0;
 numsGenState.table = document.getElementById('nums_table_0');
 numsGenState.row_num = 0;
 if (!numsGenState.table) {
 return; // Silently exit if no file is present.
 }
 srcGenState.chunk_id = 0;
 srcGenState.table = document.getElementById('src_table_0');
 srcGenState.row_num = 0;
 alignerRunning = true;
 continueToSetLineNumberHeights();
 }
 function rowGenerator(genState) {
 if (genState.row_num < genState.table.rows.length) {
 var currentRow = genState.table.rows[genState.row_num];
 genState.row_num++;
 return currentRow;
 }
 var newTable = document.getElementById(
 genState.table_base_id + (genState.chunk_id + 1));
 if (newTable) {
 genState.chunk_id++;
 genState.row_num = 0;
 genState.table = newTable;
 return genState.table.rows[0];
 }
 return null;
 }
 var MAX_ROWS_PER_PASS = 1000;
 function continueToSetLineNumberHeights() {
 var rowsInThisPass = 0;
 var numRow = 1;
 var srcRow = 1;
 while (numRow && srcRow && rowsInThisPass < MAX_ROWS_PER_PASS) {
 numRow = rowGenerator(numsGenState);
 srcRow = rowGenerator(srcGenState);
 rowsInThisPass++;
 if (numRow && srcRow) {
 if (numRow.offsetHeight != srcRow.offsetHeight) {
 numRow.firstChild.style.height = srcRow.offsetHeight + 'px';
 }
 }
 }
 if (rowsInThisPass >= MAX_ROWS_PER_PASS) {
 setTimeout(continueToSetLineNumberHeights, 10);
 } else {
 alignerRunning = false;
 if (startOver) {
 startOver = false;
 setTimeout(setLineNumberHeights, 500);
 }
 }
 }
 function initLineNumberHeights() {
 // Do 2 complete passes, because there can be races
 // between this code and prettify.
 startOver = true;
 setTimeout(setLineNumberHeights, 250);
 window.onresize = setLineNumberHeights;
 }
 initLineNumberHeights();
</script>

 
 
 <div id="log">
 <div style="text-align:right">
 <a class="ifCollapse" href="#" onclick="_toggleMeta(this); return false">Show details</a>
 <a class="ifExpand" href="#" onclick="_toggleMeta(this); return false">Hide details</a>
 </div>
 <div class="ifExpand">
 
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="changelog">
 <p>Change log</p>
 <div>
 <a href="/p/ourproject-007/source/detail?spec=svn70&amp;r=4">r4</a>
 by coolshenwen@gmail.com
 on Nov 5, 2011
 &nbsp; <a href="/p/ourproject-007/source/diff?spec=svn70&r=4&amp;format=side&amp;path=/trunk/part1/strips_engine.py&amp;old_path=/trunk/part1/strips_engine.py&amp;old=">Diff</a>
 </div>
 <pre>[No log message]</pre>
 </div>
 
 
 
 
 
 
 <script type="text/javascript">
 var detail_url = '/p/ourproject-007/source/detail?r=4&spec=svn70';
 var publish_url = '/p/ourproject-007/source/detail?r=4&spec=svn70#publish';
 // describe the paths of this revision in javascript.
 var changed_paths = [];
 var changed_urls = [];
 
 changed_paths.push('/trunk/part1/domain1.pddl');
 changed_urls.push('/p/ourproject-007/source/browse/trunk/part1/domain1.pddl?r\x3d4\x26spec\x3dsvn70');
 
 
 changed_paths.push('/trunk/part1/domain2.pddl');
 changed_urls.push('/p/ourproject-007/source/browse/trunk/part1/domain2.pddl?r\x3d4\x26spec\x3dsvn70');
 
 
 changed_paths.push('/trunk/part1/domain3.pddl');
 changed_urls.push('/p/ourproject-007/source/browse/trunk/part1/domain3.pddl?r\x3d4\x26spec\x3dsvn70');
 
 
 changed_paths.push('/trunk/part1/problem1.pddl');
 changed_urls.push('/p/ourproject-007/source/browse/trunk/part1/problem1.pddl?r\x3d4\x26spec\x3dsvn70');
 
 
 changed_paths.push('/trunk/part1/problem2.pddl');
 changed_urls.push('/p/ourproject-007/source/browse/trunk/part1/problem2.pddl?r\x3d4\x26spec\x3dsvn70');
 
 
 changed_paths.push('/trunk/part1/problem3.pddl');
 changed_urls.push('/p/ourproject-007/source/browse/trunk/part1/problem3.pddl?r\x3d4\x26spec\x3dsvn70');
 
 
 changed_paths.push('/trunk/part1/search.py');
 changed_urls.push('/p/ourproject-007/source/browse/trunk/part1/search.py?r\x3d4\x26spec\x3dsvn70');
 
 
 changed_paths.push('/trunk/part1/strips_engine.py');
 changed_urls.push('/p/ourproject-007/source/browse/trunk/part1/strips_engine.py?r\x3d4\x26spec\x3dsvn70');
 
 var selected_path = '/trunk/part1/strips_engine.py';
 
 
 function getCurrentPageIndex() {
 for (var i = 0; i < changed_paths.length; i++) {
 if (selected_path == changed_paths[i]) {
 return i;
 }
 }
 }
 function getNextPage() {
 var i = getCurrentPageIndex();
 if (i < changed_paths.length - 1) {
 return changed_urls[i + 1];
 }
 return null;
 }
 function getPreviousPage() {
 var i = getCurrentPageIndex();
 if (i > 0) {
 return changed_urls[i - 1];
 }
 return null;
 }
 function gotoNextPage() {
 var page = getNextPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoPreviousPage() {
 var page = getPreviousPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoDetailPage() {
 window.location = detail_url;
 }
 function gotoPublishPage() {
 window.location = publish_url;
 }
</script>

 
 <style type="text/css">
 #review_nav {
 border-top: 3px solid white;
 padding-top: 6px;
 margin-top: 1em;
 }
 #review_nav td {
 vertical-align: middle;
 }
 #review_nav select {
 margin: .5em 0;
 }
 </style>
 <div id="review_nav">
 <table><tr><td>Go to:&nbsp;</td><td>
 <select name="files_in_rev" onchange="window.location=this.value">
 
 <option value="/p/ourproject-007/source/browse/trunk/part1/domain1.pddl?r=4&amp;spec=svn70"
 
 >/trunk/part1/domain1.pddl</option>
 
 <option value="/p/ourproject-007/source/browse/trunk/part1/domain2.pddl?r=4&amp;spec=svn70"
 
 >/trunk/part1/domain2.pddl</option>
 
 <option value="/p/ourproject-007/source/browse/trunk/part1/domain3.pddl?r=4&amp;spec=svn70"
 
 >/trunk/part1/domain3.pddl</option>
 
 <option value="/p/ourproject-007/source/browse/trunk/part1/problem1.pddl?r=4&amp;spec=svn70"
 
 >/trunk/part1/problem1.pddl</option>
 
 <option value="/p/ourproject-007/source/browse/trunk/part1/problem2.pddl?r=4&amp;spec=svn70"
 
 >/trunk/part1/problem2.pddl</option>
 
 <option value="/p/ourproject-007/source/browse/trunk/part1/problem3.pddl?r=4&amp;spec=svn70"
 
 >/trunk/part1/problem3.pddl</option>
 
 <option value="/p/ourproject-007/source/browse/trunk/part1/search.py?r=4&amp;spec=svn70"
 
 >/trunk/part1/search.py</option>
 
 <option value="/p/ourproject-007/source/browse/trunk/part1/strips_engine.py?r=4&amp;spec=svn70"
 selected="selected"
 >/trunk/part1/strips_engine.py</option>
 
 </select>
 </td></tr></table>
 
 
 <div id="review_instr" class="closed">
 <a class="ifOpened" href="/p/ourproject-007/source/detail?r=4&spec=svn70#publish">Publish your comments</a>
 <div class="ifClosed">Double click a line to add a comment</div>
 </div>
 
 </div>
 
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="older_bubble">
 <p>Older revisions</p>
 
 <a href="/p/ourproject-007/source/list?path=/trunk/part1/strips_engine.py&start=4">All revisions of this file</a>
 </div>
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="fileinfo_bubble">
 <p>File info</p>
 
 <div>Size: 28551 bytes,
 802 lines</div>
 
 <div><a href="//ourproject-007.googlecode.com/svn/trunk/part1/strips_engine.py">View raw file</a></div>
 </div>
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 </div>
 </div>


</div>

</div>
</div>

<script src="https://ssl.gstatic.com/codesite/ph/3783617020303179221/js/prettify/prettify.js"></script>
<script type="text/javascript">prettyPrint();</script>


<script src="https://ssl.gstatic.com/codesite/ph/3783617020303179221/js/source_file_scripts.js"></script>

 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/3783617020303179221/js/kibbles.js"></script>
 <script type="text/javascript">
 var lastStop = null;
 var initialized = false;
 
 function updateCursor(next, prev) {
 if (prev && prev.element) {
 prev.element.className = 'cursor_stop cursor_hidden';
 }
 if (next && next.element) {
 next.element.className = 'cursor_stop cursor';
 lastStop = next.index;
 }
 }
 
 function pubRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftDestroyed(data) {
 updateCursorForCell(data.cellId, 'nocursor');
 if (initialized) {
 reloadCursors();
 }
 }
 function reloadCursors() {
 kibbles.skipper.reset();
 loadCursors();
 if (lastStop != null) {
 kibbles.skipper.setCurrentStop(lastStop);
 }
 }
 // possibly the simplest way to insert any newly added comments
 // is to update the class of the corresponding cursor row,
 // then refresh the entire list of rows.
 function updateCursorForCell(cellId, className) {
 var cell = document.getElementById(cellId);
 // we have to go two rows back to find the cursor location
 var row = getPreviousElement(cell.parentNode);
 row.className = className;
 }
 // returns the previous element, ignores text nodes.
 function getPreviousElement(e) {
 var element = e.previousSibling;
 if (element.nodeType == 3) {
 element = element.previousSibling;
 }
 if (element && element.tagName) {
 return element;
 }
 }
 function loadCursors() {
 // register our elements with skipper
 var elements = CR_getElements('*', 'cursor_stop');
 var len = elements.length;
 for (var i = 0; i < len; i++) {
 var element = elements[i]; 
 element.className = 'cursor_stop cursor_hidden';
 kibbles.skipper.append(element);
 }
 }
 function toggleComments() {
 CR_toggleCommentDisplay();
 reloadCursors();
 }
 function keysOnLoadHandler() {
 // setup skipper
 kibbles.skipper.addStopListener(
 kibbles.skipper.LISTENER_TYPE.PRE, updateCursor);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_top', 50);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_bottom', 100);
 // Register our keys
 kibbles.skipper.addFwdKey("n");
 kibbles.skipper.addRevKey("p");
 kibbles.keys.addKeyPressListener(
 'u', function() { window.location = detail_url; });
 kibbles.keys.addKeyPressListener(
 'r', function() { window.location = detail_url + '#publish'; });
 
 kibbles.keys.addKeyPressListener('j', gotoNextPage);
 kibbles.keys.addKeyPressListener('k', gotoPreviousPage);
 
 
 kibbles.keys.addKeyPressListener('h', toggleComments);
 
 }
 </script>
<script src="https://ssl.gstatic.com/codesite/ph/3783617020303179221/js/code_review_scripts.js"></script>
<script type="text/javascript">
 function showPublishInstructions() {
 var element = document.getElementById('review_instr');
 if (element) {
 element.className = 'opened';
 }
 }
 var codereviews;
 function revsOnLoadHandler() {
 // register our source container with the commenting code
 var paths = {'svn70': '/trunk/part1/strips_engine.py'}
 codereviews = CR_controller.setup(
 {"relativeBaseUrl":"","projectHomeUrl":"/p/ourproject-007","assetVersionPath":"https://ssl.gstatic.com/codesite/ph/3783617020303179221","profileUrl":"/u/105550342260037177437/","loggedInUserEmail":"isakebedeachs@gmail.com","assetHostPath":"https://ssl.gstatic.com/codesite/ph","projectName":"ourproject-007","domainName":null,"token":"RfCbSacEIWHqXSi63eO8BYZKC08:1375051174505"}, '', 'svn70', paths,
 CR_BrowseIntegrationFactory);
 
 // register our source container with the commenting code
 // in this case we're registering the container and the revison
 // associated with the contianer which may be the primary revision
 // or may be a previous revision against which the primary revision
 // of the file is being compared.
 codereviews.registerSourceContainer(document.getElementById('lines'), 'svn70');
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, showPublishInstructions);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_PUB_PLATE, pubRevealed);
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, draftRevealed);
 codereviews.registerActivityListener(CR_ActivityType.DISCARD_DRAFT_COMMENT, draftDestroyed);
 
 
 
 
 
 
 
 var initialized = true;
 reloadCursors();
 }
 window.onload = function() {keysOnLoadHandler(); revsOnLoadHandler();};

</script>
<script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/3783617020303179221/js/dit_scripts.js"></script>

 
 
 
 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/3783617020303179221/js/ph_core.js"></script>
 
 
 
 
</div> 

<div id="footer" dir="ltr">
 <div class="text">
 <a href="/projecthosting/terms.html">Terms</a> -
 <a href="http://www.google.com/privacy.html">Privacy</a> -
 <a href="/p/support/">Project Hosting Help</a>
 </div>
</div>
 <div class="hostedBy" style="margin-top: -20px;">
 <span style="vertical-align: top;">Powered by <a href="http://code.google.com/projecthosting/">Google Project Hosting</a></span>
 </div>

 
 


 
 </body>
</html>

