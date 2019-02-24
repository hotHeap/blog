<template>
	<div class = "search-abstract">
		<loading v-if = "articles.all.length == 0&&code === 404"></loading>
		<div class = "search-tips">
			<h3>{{ searchTips }}</h3>
		</div>
		<article-list :articleList = "articles.search"></article-list>
	</div>
</template>
<script>
	import { mapActions,mapState,mapMutations } from "vuex"
	import articleList from "@/components/article/articleList"
	import loading from "@/components/base/loading"
	export default {
		components: {
			articleList,
			loading
		},
		data(){
			return{
				searchTips: "",
				code: 404
			}
		},
		metaInfo(){
			return {
				title: "Search -for your interst"
			}
		},
		created(){
			this.startSearch()
		},
		computed: {
			...mapState(["articles"])
		},
		watch: {
			$route(){
				this.startSearch()
			}
		},
		methods: {
			...mapActions(["search","getArticlesCount"]),
			...mapMutations(["clear"]),
			startSearch: function(){
				let that = this	
				this.search({
					publish: true,
					page: 1,
					key: this.$route.params.searchKey,
					according: "key"
				}).then((data) => {
					if(data.length){
						that.searchTips = "The following is the content of the search："
						that.code = 200
					}else{
						that.searchTips = "Oh sorry,that's nothing to show 🤔 "
						that.code = 200
					}
				})
				this.getArticlesCount({
					publish: true,
					key : this.$route.params.searchKey,
				})
			}
		}
	}
</script>
<style lang = "less" scoped>
	img{
		border: 5px solid red;
		width: 20px;
	}
	.fade-enter-active, .fade-leave-active {
 		transition: opacity .5s
	}
	.fade-enter, .fade-leave-to {
 		opacity: 0
	}
	.search-tips{
		margin-top: 10px;
		padding: 10px;
		/*background: #F7EDED;*/
		background: #FAF7F7;
	}
</style>

