<template>
	<!-- 给图片加遮罩层 -->
	<div class = "banner" ref = "banner">
		<ul>
			<!-- 此处transition有bug,离开当前标签，再次返回后，图片会消失，直到轮播到下一张图片 -->
			<!-- <transition-group name = "slider-fade" tag = "div"> -->
				<!-- transition-group中v-for若有index，则必须绑定key值，否则报错 -->
				<li v-for = "(item,index) in bannerData"  v-bind:key = "index" :class = "{'show-opacity': index === currentIndex}"  @touchmove.stop = "touchMove($event,index)" @touchstart.stop = "touchStart($event)" @touchend.stop = "touchEnd($event)">
					<img :data-src= item.url alt="" src = "/img/pic-loading.gif" ref = "img">
					<div class = "img-shadow">
						<div class="wellknown">
							<div>{{ item.word }}</div>
							<br>
							<div>👉 {{ item.person }}</div>
						</div>
					</div>
				</li>
			<!-- </transition-group> -->
		</ul>
		<div class = "circle">
			<div v-for = "(item,_index) in bannerData">
				<span :class = "{'current-circle': _index === currentIndex}" @click = "chosePic(_index)" @mouseover = "stopSlider_cpt" @mouseleave = "startSlider" @touchstart = "stopSlider" @touchend = "startSlider"></span>
			</div>
		</div>
	</div>
</template>
<script>
	export default{
		data(){
			return{
				currentIndex: 0,
				startPos: {x: "",y: "",date: ""},
				move: {x: "",y: ""},
				bannerData: [
					{
						url: "/img/banner/one.jpeg",
						word:"Success is not final, failure is not fatal. It is the courage to continue that counts.",
						person: "Winston Churchill"},
					{
						url: "/img/banner/two.jpeg",
						word: "或许是疯子的世界观与常人不一样，所以是疯子。我也无法说服自己那些疯狂的想法，念头。",
						person: "7Ethan"
					},
					{
						url: "/img/banner/three.jpeg",
						word: "有人朝九晚五是对的，有人四海为家是对的，有人仗剑走天涯也是对的，不要有什么绝对的对与错。",
						person: "佚名"
					},
					{
						url: "/img/banner/four.jpeg",
						word: "一个人可以被毁灭，但不能被打败。",
						person: "海明威"
					},
					{
						url: "/img/banner/five.jpeg",
						word: " JUST DO IT",
						person: "Simple words are not simple"
					}
				]
			}
		},
		mounted(){
			this.lazyLoad()
		},
		methods: {
			//实现图片懒加载
			lazyLoad: function(){
				this.$refs.img.forEach((item,index,arr) =>{	
					if(index === this.currentIndex){
						//清除定时器，防止图片还没加载完成就轮播到下一张
						clearInterval(this.timer)
						let img = new Image()
						img.src = item.dataset.src
						img.onload = () =>{
							item.src = img.src
							this.slider()
						}
					}
				})
			},
      		slider: function(index){
      			let that = this
      			this.timer = setInterval(() => {
      				if(that.currentIndex < that.bannerData.length - 1){
      					that.currentIndex++
      					this.lazyLoad()
      				}else{
      					that.currentIndex = 0
      					this.lazyLoad()
      				}
      			},8000)
      		},
      		chosePic: function(index){
      			this.currentIndex = index
      			this.lazyLoad()
      		},
      		startSlider: function(){
      			this.lazyLoad()
      		},
      		stopSlider: function(){
      			clearInterval(this.timer)
      		},
      		//移动端也会触发mouseover事件（奇怪--），所以做一下判断，否则手动切换图片会消除定时器
      		stopSlider_cpt: function(){
      			if (!/(iPhone|iPad|iPod|iOS|Android)/i.test(navigator.userAgent)) { //移动端
				    clearInterval(this.timer)
				}
      		},
      		//移动端滑动
      		touchStart(event){
      			clearInterval(this.timer)
      			let touch = event.targetTouches[0] //touches数组对象获得屏幕上所有的touch，取第一个touch
			　　this.startPos = {x: touch.pageX,y: touch.pageY,date: +new Date} //取第一个touch的坐标值
      		},
      		touchMove: function(event,index){
      			//防止滚屏
      			event.preventDefault()
				if(event.targetTouches.length > 1 || event.scale && event.scale !== 1) return
		　      let touch = event.targetTouches[0]
				this.move.x = touch.pageX - this.startPos.x
				this.move.y = touch.pageY - this.startPos.y
      		},
      		touchEnd(event){
      			let ted = event.targetTouches[0],//touches数组对象获得屏幕上所有的touch，取第一个touch
      			moveDate = +new Date() - this.startPos.date
      			if(Math.abs(this.move.x) > Math.abs(this.move.y)&&moveDate<1000&&this.move.x < -150){
					if(this.currentIndex < this.bannerData.length - 1){
						this.currentIndex++
						this.move = {x: 0,y: 0,date: ""}
					}else{
						this.currentIndex = 0
						this.move = {x: 0,y: 0,date: ""}
					}
				}
				if(Math.abs(this.move.x) > Math.abs(this.move.y)&&moveDate<1000&&this.move.x > 150){
					if(this.currentIndex > 0){
						this.currentIndex--
						this.move = {x: 0,y: 0,date: ""}
					}else{
						this.currentIndex = this.bannerData.length-1
						this.move = {x: 0,y: 0,date: ""}
					}
				}
				this.lazyLoad()
      		}
    	}
	}
</script>
<style lang="less">
	.banner{
		transition: all ease .5s;
		position: relative;
		margin-top: 10px;
		height: 250px;
		ul,ul>div{
			width: 100%;
			height: 100%;
		}
		li{
			transition: all ease 1s;
			opacity: 0;
			list-style: none;
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
		}
		img{
			width: 100%;
			height: 100%;
		}
	}
	.img-shadow{
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background: rgba(0,0,0,0.3);
	}
	.wellknown{
		box-sizing: border-box;
		line-height: 1.5;
		color: #eee;
		text-align: center;
		position: absolute;
		top: 50%;
		left: 0;
		padding: 0 25px;
		transform: translateY(-50%);
		width: 100%;
	}
	.headerHeight{
		height: 0!important
	}
	.show-opacity{
		opacity: 1!important
	}
	.slider-fade-enter,.slider-fade-leave-to{
		opacity: 0
	}
	.slider-fade-enter-active,.slider-fade-leave-active{
		transition: all ease 0.5s
	}
	.current-relative{
		position: relative!important
	}
	.circle{
		position: absolute;
		bottom: 0;
		left: 50%;
		margin-left: -60px;
		z-index: 250;
		div{
			display: inline-block;
			width: 20px;
			height: 20px;
			text-align: center;
		}
		span{
			display: inline-block;
			transition: all ease-in .5s;
			width: 8px;
			height: 8px;
			border-radius: 4px;
			background: #eee;
			cursor: pointer;
		}
	}
	.banner .circle .current-circle{
		width: 20px;
		height: 8px;
		border-radius: 4px;
		background: orange
	}
	@media screen and (max-width: 768px){
		.banner{
			margin-top: -50px;
		}
	}
</style>