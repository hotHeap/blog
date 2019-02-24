<template>
	<div class = "article-show">
		<div class = "article-show-content" >
			<div v-for = "item in articles.only" class = "article-body">
				<h2 class = "article-title">{{ item.title }}</h2>
				<div class = "article-details">
					<div class = "article-details-tag">
						<span class = "icon-tag-stroke i-p"></span>
						<span class = "each-tag" v-for = "tag in item.tag">{{ tag | changeLife }}</span>
					</div>
					<div class = "article-details-other">
						<div class = "time">
							<!-- <span class = "icon-clock i-p"></span> -->
							<!-- <span>{{ item.date | reviseTime }}</span> -->
						</div>
						<div class = "pv-c-l">
							<span class = "icon-eye i-p"></span>
							<span>{{ item.pv }}  </span>
							<span class = "icon-commenting-o i-p"></span>
							<span>{{ item.commentNum }} comments</span>
							<span class = "icon-like i-p"></span>
							<span>{{ item.likeNum }} Like</span>
						</div>
					</div>
				</div>
				<hr>
				<vue-markdown >{{ item.content }}</vue-markdown>
				<!-- <div id="articlesDetails">
					<div class="detail-body" v-compiledMarkdown>{{ item.content }}</div>	
				</div> -->
						
				<div class = "article-like" :class= "{'article-like-after': lovedArr.indexOf(item._id) !== -1}" @click = "love(item.articleId,item._id)"><span class = "love-text">{{ love_t }}</span>
				</div>
					<div class="article-warning" v-if = "item.original">
					<h6>本文为作者原创文章，转载请注明出处： </h6>
					<i><a href="javascript: void(0)">http://www.7Ethan.top{{ fullPath }}</a></i>
				</div>
				<div class="article-line"></div>
				<h4>Share：</h4>
				<div class="share">
					<a href = "javascript: void(0)" @click = "share('QQ','http://connect.qq.com/widget/shareqq/index.html')" class="design-bg-qq"></a>
					<a href = "javascript: void(0)" @click = "share('qzone','http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey')" class="design-bg-qzone"></a>
					<a href = "javascript: void(0)" @click = "share('sina','http://v.t.sina.com.cn/share/share.php')" class="design-bg-sina"></a>
					<a href = "javascript: void(0)" @click = "qrcode" class="design-bg-weixin"></a>
					<a href = "javascript: void(0)" @click = "share('douban','http://shuo.douban.com/!service/share')" class="design-bg-douban"></a>
				</div>
				<div class = "otherArticle"></div>
				<div class = "qrcode-box" v-show = "qrShow">
					<span>微信扫一扫分享到朋友圈</span><span class = "exit-qrcode" @click = "exitQrcode">X</span>
					<div id = "qrcode"></div>
				</div>
				<div class = "pre-next">
					<div class = "pre" v-if = "articles.pre_next.pre.length">
						<h4 style="color:cadetblue">Previous：</h4>
						<u><a href = "javascript: void(0)" v-for = "item in articles.pre_next.pre"><span @click = "jumpPn(item)"> {{ item.title }}</span> </a></u>
						</div>
					<div class = "next" v-if = "articles.pre_next.next.length">
						<h4 style="color:cadetblue">Next：</h4>
						<u><a href = "javascript: void(0)" v-for = "item in articles.pre_next.next"><span @click = "jumpPn(item)"> {{ item.title }}</span> </a></u>
						</div>
				</div>
			</div>
			
		</div>
		<comment></comment>
	</div>
</template>

<script>
	import VueMarkdown from "vue-markdown"
	import { mapState,mapMutations,mapActions } from "vuex"
	import comment from "@/components/comment/comment"
	import marked from 'marked'
	// import 'highlight.js/styles/googlecode.css'
	// import highlight from 'highlight.js'

	/*
	* highlightCode
	*/
	// hljs.highlightCode =   function () { //自定义highlightCode方法，将只执行一次的逻辑去掉
	// 	let blocks = document.querySelectorAll('pre code');
	// 	// [].forEach.call(blocks, hljs.highlightBlock);
	// 	blocks.forEach((block)=>{
    // 		hljs.highlightBlock(block)
  	// 	})
	//  };
	//highlight.highlightCode = function () { //自定义highlightCode方法，将只执行一次的逻辑去掉
	//	let blocks = document.querySelectorAll('pre code');
	//	[].forEach.call(blocks, highlight.highlightBlock);
 	//};


	export default{
		components: {
			comment,
			VueMarkdown,
			marked
		},
		data(){
			return {
				qrShow: false,
				loveText: " 👍 ",
				lovedArr: [],
				fullPath: "",
			}
		},
		metaInfo(){
			const title = this.articles.only[0].title
			return {
				title: title + " -7Ethan",
				meta: [{vmid: "description",name: "description",content: title + " -7Ethan"}]
			}
		},
		asyncData({store,route}){
		return store.dispatch("getArticle",{
				publish: true,
				tag: route.params.articleList,
				articleId: route.params.id,
				cache: true 	
         	}).then(() => {
         		store.commit("changeTitle",store.state.articles.only[0].title)
         	})
		},
		filters: {
			changeLife: function(value){
				if(value == "life"){
					return "more"
				}else{
					return value
				}
			}
		},
		mounted(){
			if(localStorage.getItem("articleLoved")){
				this.lovedArr = JSON.parse(localStorage.getItem("articleLoved"))
			}
			this.$nextTick(function(){
				Prism.highlightAll()
			})
			this.getOriginUrl()
			// highlight.highlightCode()
			// marked.setOptions({
			// 	renderer: new marked.Renderer(),
			// 	gfm: true,
			// 	tables: true,
			// 	breaks: false,
			// 	pedantic: false,
			// 	sanitize: false,
			// 	smartLists: true,
			// 	smartypants: false,
			// 	highlight: function (code) {
			// 		return highlight.highlightAuto(code).value;
            // 	}
       		//  })
		},
		computed: {
			...mapState(["articles"]),
			love_t: function(){
				if(this.lovedArr.indexOf(this.articles.only[0]._id) !== -1){
					return " "//不显示内容
				}else{
					return " 👍 "
				}
			},
			ifCatch: function(){
				return this.articles.only
			},
			// compiledMarkdown: function () { 
			// 	return marked(this.articles.only[0].content, { sanitize: true })
			//  }
		},
		watch: {
			//推荐文章的引起路由变化重新进行抓取
			$route(){
				//二级评论进行锚点跳转
				let r = this.$route
				if(r.fullPath.indexOf("#anchor-comment") === -1){
					this.getArticle({
						publish: true,
						tag: r.params.articleList,
						articleId: r.params.id  
					}).then(()=>{
						this.changeTitle(this.articles.only[0].title)
						this.$nextTick(function(){
							Prism.highlightAll()
						})
					})
				}
			},
			//抓取数据延时较高时，确保抓取到数据之后进行一次代码样式的渲染
			ifCatch(){
				this.$nextTick(function(){
					Prism.highlightAll()
				})
			}
		},
		methods: {
			...mapActions(["getArticle","loveArticle"]),
			...mapMutations(["changeTitle"]),

			/*
			* Marked
			*/
			// markdown: function(){
			// 	Marked.setOptions({
			// 		renderer: new Marked.Renderer(),
			// 		gfm: true,
			// 		tables: true,
			// 		breaks: false,
			// 		pedantic: false,
			// 		sanitize: false,
			// 		smartLists: true,
			// 		smartypants: false
            // 	});
			// },
			
			// 点击回复按钮会在地址栏加上锚点，故刷新时去除，第三方分享链接亦如此
			getOriginUrl: function(){
				if(this.$route.fullPath.indexOf("#anchor-comment") > -1){
					this.fullPath = this.$route.fullPath.substring(0,this.$route.fullPath.indexOf("#"))
				}else{
					this.fullPath = this.$route.fullPath
				}
			},
			love: function(aid,_id){
				if(this.lovedArr.indexOf(_id) === -1){
					this.loveArticle({
						articleId: aid,
						num: 1,
						title: document.title
					}).then((data) => {
						if(data.code === 200){
							this.lovedArr.push(_id)
							localStorage.setItem("articleLoved",JSON.stringify(this.lovedArr))
						}
					})
					
				}else{
					this.loveArticle({
						articleId: aid,
						num: -1,
						title: document.title
					}).then((data) => {
						if(data.code === 200){
							this.lovedArr.splice(this.lovedArr.indexOf(_id),1)
							localStorage.setItem("articleLoved",JSON.stringify(this.lovedArr))
						}
						
					})
				}
			},
			jumpPn: function(item){
				if(item.tag[0] === "life"){
					this.$router.push({name: 'lifeShow',params : {id: item.articleId}})
				}else{
					this.$router.push({name: 'articleShow',params : {articleList: item.tag[0],id: item.articleId}})
				}
			},
			share: function(type,url){
				let	title = document.title + " Tecnical bolg from 7Ethan",
					el = document.createElement("a"),
					_href,
					_url
				if(window.location.href.indexOf("#anchor-comment") > -1){
					_url = window.location.href.substring(0,window.location.href.indexOf("#"))
				}else{
					_url = window.location.href
				}
				el.target = "_blank"
				switch (type){
					case "QQ" : 
					_href = url + "?title=" + title +"&url=" + _url + "&desc=我分享了一篇文章，快来看看哦 😄 " + "&site=7Ethan"
					break
					case "qzone" : 
					_href = url + "?title=" + title + "&url=" + _url + "&desc=我分享了一篇文章，快来看看哦 😄  " + "&site=7Ethan" + "summary="
					break
					case "sina" : 
					_href = url + "?title=" + title + "&url=" + _url
					break
					case "weixin" : 
					_href = url + "&url=" + _url
					break
					case "douban" : 
					_href = url + "?name=" + title + "&href=" + _url

				}
				el.href = _href
				el.click()
			},
			//微信二维码生成器
			qrcode: function(){
				if(this.qrShow === false){
					this.qrShow = true
					let _url = window.location.href
					new QRCode(document.getElementById("qrcode"),{
					 	text: _url,
					 	width: 160,
					 	height: 160,
					 	colorDark : "#000000",
						colorLight : "#ffffff",
					 	correctLevel : QRCode.CorrectLevel.H
					})
				}	
			},
			//关闭微信二维码
			exitQrcode: function(){
				this.qrShow = false
				document.getElementById("qrcode").innerHTML = ''
			}
		},
		
		/*
		directives: {
			compiledMarkdown: {
				bind: function(el){
					marked.setOptions({
						renderer: new marked.Renderer(),
						gfm: true,
						tables: true,
						breaks: false,
						pedantic: false,
						sanitize: false,
						smartLists: true,
						smartypants: false,
						highlight: function (code) {
							return highlight.highlightAuto(code).value;
						}
					})
					el.innerHTML = marked(el.innerText);
					var preList = el.querySelectorAll('pre');
					var imgList = el.querySelectorAll('img');
					var strongList = el.querySelectorAll('strong');
					var pList = el.querySelectorAll('p');
					var aList = el.querySelectorAll('a');
					var codeList = el.querySelectorAll('code');
					codeList.forEach(function(item){
						if(item.parentNode.tagName !== 'PRE'){
							item.style.padding = '2px 4px';
							item.style.color = '#c7254e';
							item.style.backgroundColor = '#f9f2f4';
							item.style.borderRadius = '3px';
						}
					})
					for (let i=0; i<aList.length; i++){
						aList[i].style.color = '#32D3C3'
						aList[i].style.textDecoration = 'none'
						aList[i].setAttribute('target', '_blank')
					}
					for (let i=0; i<pList.length; i++){
						pList[i].style.color = '#3E495E'
						pList[i].style.margin = '1.5em 0'
						pList[i].style.lineHeight = '1.6'
					}
					for (let i=0; i<strongList.length; i++){
						strongList[i].style.color = '#32D3C3'
					}
					for(let i=0; i<imgList.length; i++){
						imgList[i].style.width = 100 + '%';
					}
					for(let i=0; i<preList.length; i++){
						preList[i].style.overflowX = 'scroll';
						preList[i].style.backgroundColor = '#e8e8e8'
						preList[i].style.padding = '1rem'
						preList[i].style.lineHeight = '1.45'
						preList[i].style.backgroundSize = '30px,30px'
						preList[i].style.background = 'url(../../src/assets/blueprint.png) #F6F6F6'
						preList[i].style.borderRadius = '3px'
					} 
					var blockquoteList = el.querySelectorAll('blockquote')
					blockquoteList.forEach((item) => {
						item.style.borderLeft = '3px solid #32d3c3';
						item.style.backgroundColor = '#F6F6F6';
						item.style.color = '#555';
						item.style.fontSize = '1em';
						item.style.margin = '1.5em 0';
						item.style.padding = '1px 20px'
						let p = item.querySelector('p')
						p.style.color = '#555'
						p.style.margin = '0.5em 0px';
					})
				}
			},	
		}
		*/
	}
</script> 
<style lang = "less">
	/* #mdContent {
        text-align: left;
        padding: 1rem 0;
        color: #666;
        max-height: 3.7rem;
        line-height: 1.2rem;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 4;
        -webkit-box-orient: vertical;
	} */
	/* @media screen and (max-width: 768px){
		.detail-header{
			margin: 0 0rem 0 0rem!important;
		}
		.detail-body{
			margin: 0 0rem 0 0rem!important;
		}
		.detail-footer{
			margin: 0 0rem 0 0rem!important;
		}
	}


	#articlesDetails {
		height: 100vh;
		overflow: scroll;
		text-align: center;
		padding: 0 1rem;
		font-family: Avenir,Helvetica,Arial,sans-serif;
		-webkit-font-smoothing: antialiased;
		background-color: #fff;
	}
	.detail-body{
		padding: 1rem 0;
		text-align: left;
		border-bottom: 1px dashed #999999;
		margin: 0 7rem 0 4rem; 
	} */
	

	.article-show-content{
		margin-top: 10px;
		/*background: #F7EDED;*/
		background: #FAF7F7;
		color: #404040;
		font-size: 14px;
		line-height: 1.8;
		padding: 15px;
		border: 5px 5px 0 0;
		border-radius: 3px;
		hr{
			margin: 15px 0;
			height: 0;
			border: 0;
			border-top: 1px solid #ccc;
		}
		img{
			max-width: 100%
		}
	}
	.article-title{
		padding: 5px 0;
		color: #16a085;
	}
	.article-body li{
		margin-left: 15px;
	}
	.article-details{
		font-size: 12px;
		line-height: 24px;
		color: #404040;
	}
	.article-details-tag{
		display: flex;
		align-items: center;
	}
	.each-tag{
		margin-right: 8px;
	}
	.icon-tag-stroke,.icon-eye,.icon-clock{
		margin-top: 2px;
	}
	.article-details-other{
		display: flex;
		/*align-items: center;*/
		justify-content: space-between;
		flex-wrap: wrap;
	}
	.i-p{
		margin: 0 5px;
	}
	.article-like{
		background: url("/img/love-before.png") no-repeat;
		width: 50px;
		height: 50px;
		margin: 15px auto;
		cursor: pointer;
		text-align: center;
		transition: all ease 0.5s;
	}
	.love-text{
		display: inline-block;
		user-select: none;
		color: #F7EDED;
		margin-top: 7px;
	}
	.article-like-after{
		transform: rotateY(360deg);
		background: url("/img/love-after.png") no-repeat;
	}
	.article-like-after:hover,.article-like:hover{
		animation: move 1.5s;
	}
	@keyframes move{
		0% {
			transform: scale(1);
		}
		25% {
			transform: scale(1.2);
		}
		50%{
			transform: scale(1);
		}
		75%{
			transform: scale(1.2);
		}
		100%{
			transform: scale(1);
		}
	}
	.article-line{
		height: 2px;
		margin-top: 10px;
		background: #ccc;
	}
	.share a{
		display: inline-block;
		width: 32px;
		height: 32px;
		padding: 1px;
		margin: 0 5px;
		transition: all ease 0.5s;
	}
	.share a:hover{
		opacity: 0.8;
		transform: rotate(360deg);
	}
	.share .design-bg-qq{
		margin: 0 5px 0 0;
		background: url("/img/share.png") 0 0 no-repeat!important;
	}
	.design-bg-qzone{	
		background: url("/img/share.png") -57px 0 no-repeat!important;
	}
	.design-bg-sina{
		background: url("/img/share.png") -118px -71px no-repeat!important;
	}
	.design-bg-douban{
		background: url("/img/share.png") -118px -138px no-repeat!important;
	}
	.design-bg-weixin{
		background: url("/img/share.png") 0 -71px no-repeat!important;
	}
	.qrcode-box{
	 	position: fixed;
	 	z-index: 2000;
		padding: 0 15px 15px 15px;
		border-radius: 15px;
	 	-webkit-transform: translate(-50%, -50%);
    	transform: translate(-50%, -50%);
    	top: 50%;
    	left: 50%;
		background: #ccc;
		
	}
	.qrcode-box span:nth-child(1){
			font-size: 12px;
		};
	#qrcode img{
		margin: 0 auto;
	}
	.exit-qrcode{
		float: right;
		margin-right: 2px;
		cursor: pointer;
	}
	.article-warning{
		h6{
			line-height: 1.2;
			padding: 1px 0 0 5px ;
			display: inline-block;
			border-left: 5px solid orange;
		}
		a{
			display: inline-block;
			color: #404040;
		}
		a:hover{
			text-decoration: underline;
			color: #16a085;
		}
	}
	.pre-next{
		margin-top: 10px;
		h6{
			display: inline-block;

		}
		a{
			color: #404040;

		}
		a:hover{
			color: #16a085;
			text-decoration: underline;
		}
	}
</style>
