webpackJsonp([6],{"P+Lm":function(t,i){},Uqhr:function(t,i,a){"use strict";Object.defineProperty(i,"__esModule",{value:!0});var n=a("dgVe"),e=a("PHrY"),s=a("I+qJ"),o=a("zXoH"),r={data:function(){return{data:[],loading:!1,showImg:!1,imgSrc:"",nodata:!0,next:null,previous:null,current:1,loadingmore:!1,nomoredata:!1}},methods:{getData:function(){var t=this;this.loading=!0,Object(e.f)({page:this.current}).then(function(i){i.data&&(t.next=i.data.next,t.previous=i.data.previous,i.data.next&&i.data.next>=2&&(t.current=t.next-1),t.data=i.data.results,t.data.every(function(i){i.sections.length?t.nodata=!1:t.nodata=!0}),t.loading=!1)}).catch(function(){t.nomoredata=!1,t.loading=!1})},loadMore:function(){this.loadingmore=!0,this.current++,this.getData()},clickImg:function(t){t&&(this.imgSrc=t,this.showImg=!0)},imgShow:function(){this.showImg=!1},highLight:function(t,i){var a=this,n={trash:!1,notes:t,user:this.$store.getters.uuid};Object(e.l)(i,n).then(function(t){200===t.status&&(a.data=[],a.getData())})}},components:{NoteList:n.a,NoData:s.a,BigImg:o.a},mounted:function(){this.getData()}},c={render:function(){var t=this,i=t.$createElement,a=t._self._c||i;return a("div",{staticClass:"highlight"},[t._l(t.data,function(i){return a("ul",{key:i.uuid,staticClass:"light"},t._l(i.sections,function(n){return a("note-list",{key:n.uuid,attrs:{context:n.remark,type:"trash",img:n.image,isHighlight:n.highlight,isTrash:n.trash},on:{clickShowImg:function(i){t.clickImg(n.image)},reduction:function(a){t.highLight(i.uuid,n.uuid)}}})}))}),t._v(" "),t.loading||t.nodata||t.next?a("no-data",{attrs:{loading:t.loading,nodata:!t.loading&&t.nodata,next:t.next,loadingmore:t.loadingmore,nomoredata:t.nomoredata},on:{loadMore:t.loadMore}}):t._e(),t._v(" "),t.showImg?a("big-img",{attrs:{imgSrc:t.imgSrc},on:{clickit:t.imgShow}}):t._e()],2)},staticRenderFns:[]};var l=a("VU/8")(r,c,!1,function(t){a("j/nA")},"data-v-5a0f481c",null);i.default=l.exports},dgVe:function(t,i,a){"use strict";var n={render:function(){var t=this,i=t.$createElement,a=t._self._c||i;return"highlight"===t.type&&!t.isTrash||"trash"===t.type?a("li",{class:{"light-list":!0,"has-left-radius":"highlight"===t.type,"no-left-radius":"trash"===t.type}},[t.img?a("div",{class:{"light-list-img-box":!0,"border-left-radius":t.isHighlight&&"highlight"===t.type}},[a("img",{staticClass:"list-item-img",attrs:{src:t.img,alt:"Markone"},on:{click:function(i){t.$emit("clickShowImg")}}})]):a("p",[t._v(t._s(t.context))]),t._v(" "),"highlight"===t.type?a("div",{staticClass:"light-list-delete",attrs:{title:"Move to trash"},on:{click:function(i){t.$emit("toTrash")}}},[a("span",[t._v("✖")])]):t._e(),t._v(" "),"highlight"===t.type?a("div",{staticClass:"light-list-box highlight"},[a("span",{staticClass:"light-list-box-icon",attrs:{title:"Unmark"},on:{click:function(i){t.$emit("tohighlight")}}},[a("icon-svg",{attrs:{"icon-class":"highlighted"}})],1),t._v(" "),a("span",{staticClass:"light-list-box-icon",attrs:{title:"Return notes"},on:{click:function(i){t.$router.push("/detail/"+t.uuid)}}},[a("icon-svg",{attrs:{"icon-class":"back-to-note"}})],1)]):t._e(),t._v(" "),"trash"===t.type?a("div",{staticClass:"light-list-box trash"},[a("span",{staticClass:"light-list-box-icon",attrs:{title:"Revert"},on:{click:function(i){t.$emit("reduction")}}},[a("icon-svg",{attrs:{"icon-class":"return-to-note"}})],1)]):t._e()]):t._e()},staticRenderFns:[]};var e=a("VU/8")({props:["context","type","img","isHighlight","isTrash","uuid"]},n,!1,function(t){a("P+Lm")},"data-v-ca5cd31a",null);i.a=e.exports},"j/nA":function(t,i){}});