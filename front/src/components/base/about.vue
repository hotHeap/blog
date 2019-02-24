<template>
	<div class = "about">
		<div class = "about-header">
			<h2>About </h2>
		</div>
		<!-- <div class = "about-content">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp本站是一个用于知识积累与分享的个人开源博客。主要技术栈为HTML+CSS、vue全家桶、axios、express、mongodb。前端采用vue-ssr渲染，支持文章评论与分享，并设置有留言功能，源码请戳<a href = "https://github.com/justJokee/vue-ssr-blog" target = "_blank">github</a></div> -->
		<div class = "about-content">
      <div slot="sidecontent">
          <h3>
            <a href="" @click="email"> 📧  </a>
            <a class="name" href="">7Ethan</a>
            <span class="maxim"> 👉  Make it Better 🆙 </span> 
          </h3>
          <div class="pres">
            <a href="" class="pic">
              <img src="/img/card.jpg" alt="我的头像">
            </a>
          </div>
          <div class="introduce">
            <ul>
              <li>90 后野生程序员 🤔 </li>
              <li>开源硬件、软件爱好者 👏 </li>
              <li>golang，Rust，Haskell粉丝</li>
            </ul>
            <div class="myGithub">
              <div id="cell">ヽ(･ω･´ﾒ) |</div>
              <a href="https://github.com/7Ethan">
                <img src="/img/github.png" alt="访问我的 github">
              </a>
            </div>
          </div>
      </div>
	  </div>
	</div> 
</template>

<script>
  export default{
    methods :{
      email : function(){
        alert("sergeychang@gmail.com");
      },
    },
  }
</script>

<style lang = "less" scoped>
  .about-header {
    text-align: center;
    padding: 15px;
    color: #eee;
    background: #2e3033;
  }
  .about-content {
    color: #1a1a1a;
    background: #faf7f7;
    padding: 15px;
    line-height: 28px;
    font-size: 14px;
    height: auto;
    /* a {
      margin-left: 5px;
      color: #16a085;
    } */
  }
  .about-content .name{
    color: brown;
    padding-left: 5px;
    font-size: 20px;
  }
  .about-content .a{
    padding-left: 5px;
  }

  .about-content .pres{
    height: auto;
    float: left;
  }
  .about-content .introduce{
    padding-bottom: 0px;
  }

  .introduce li{
    list-style-type:circle;
    height: auto;
    margin-left: 120px;
    margin-top: 0px;
    margin-bottom: 0px;
  }


  .maxim{
    padding-left: 15px;
    font-size: 15px;
  }

  .about-content a.pic img {
    height: 120px;
    width: 100px;
    display: inline-block;
    overflow: hidden;
    line-height: 1;
    vertical-align: middle;
    border-radius: 8px;
    padding-top: 10px;
  }

  .myGithub{
    display: table;
  }

  .myGithub a img{
    display: inline-block;
    overflow: hidden;
    height: 38px;
    width: 38px;
  }
   #cell{
    display:table-cell;
    vertical-align: middle;
  }
</style>