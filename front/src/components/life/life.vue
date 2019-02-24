<template>
	<div class = "life-module">
		<loading v-if = "code === 404"></loading>
		<h3 v-if = "articles.life.length == 0&&code === 200" class = "none-article">Coming soon 😄···</h3>
		<article-list :articleList = "articles.life"></article-list>
	</div>	
</template>
<script>
 	import { mapActions,mapMutations,mapState } from "vuex"
	import articleList from "@/components/article/articleList"
	import loading from "@/components/base/loading"
	export default {
		components: {
			articleList,
			loading
		},
		metaInfo(){
			return {
				title: "ヽ(･ω･´ﾒ)-7Ethan",
				meta: [{vmid: "description",name: "description",content: "ヽ(･ω･´ﾒ) -7Ethan"}]
			}
		},	
		asyncData({store,route}){
			return Promise.all([
				store.dispatch("getArticles",{
					publish: true,
					page: 1,
					tag: "life",
					cache: true
				}),
				store.dispatch("getArticlesCount",{
					publish: true,
					page: 1,
					tag: "life",
					cache: true
				})
			]).then(()=>{
				store.commit("changeCode",200)
			})
		},
		beforeRouteLeave(to,from,next){
			this.clear()
			next()
		},
		computed: {
			...mapState(["articles","code"])
		},
		methods: {
			...mapMutations(["clear"]),
			...mapActions(["getArticles","getArticlesCount"])
		}
	}
</script>
<style lang="less" scoped>
	.none-article{
		padding: 20px;
		// background: #F7EDED;
		background: #FAF7F7;
		margin-top: 10px;
	}
</style>