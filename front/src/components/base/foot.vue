<template>
	<div class = "foot">
		<div class = "police">
			<img src ="/img/beian.png"/>
			<p>&nbsp 和谐社会，文明网络。</p>
		</div>
		<div class="link">
			<p>
				Power by 
				<span style="color:#000">  ¹</span>
				<a href="https://cn.vuejs.org/ " style="color:cyan;"><i>Vue</i></a>
				<span style="color:#000">  ²</span>
				<a href="https://github.com/labstack/echo" style="color:cyan;"><i>Echo</i></a>
				<span style="color:#000">  ³</span>
				<a href="https://www.docker.com" style="color:cyan;"><i>Docker</i></a>	
			</p>
		</div>
		<div class = "copyright">
			<div>Copyright © 2016 - 2018&nbsp <a href = "https://www.7Ethan.top">7Ethan &nbsp</a></div>
			<div>
				<a href="https://github.com/7Ethan" class="footer-github">
				<img src="/img/github.png" alt=""width="20px" height="20px"></a>
			</div>
			<div>
				<span style="color:#000">&nbsp|&nbsp</span>
				<span>link&nbsp</span>				
			</div>
			<div>
				<a href="https://rust.cc">Rust.cc</a>
			</div>
			<div>
				<span style="color:#000">&nbsp|&nbsp</span>
			</div>
			<div><a href = "https://www.7Ethan.top/login" target = "_blank">&nbspLogin</a></div>
		</div>
    </div>  
</template>
<script></script>
<style lang = "less">
	.foot{
		color: #ccc;
		/* background: #2e3033; */
		background: #186384;
		a{
			color: #ccc;
		}
		a:hover{
			color: #ffffff;
			text-decoration: underline;
		}
	}
	
	.police{
		display: flex;
		justify-content: center;
		/* padding: 20px; */
		padding-top: 10px;
	}
	.link {
		display: flex;
		justify-content: center;
		flex-wrap: wrap;
		/* padding-bottom: 20px; */
		padding: 5px;
	}
	.copyright{
		display: flex;
		justify-content: center;
		flex-wrap: wrap;
		padding-bottom: 10px;
		font-family: HeiTi;
	}
	@media screen and(max-width: 767px){
		.foot{
			font-size: 14px;
		}
		.police{
			padding: 15px;
		}
		.copyright span{
			display: none;
		}
	}
</style>
