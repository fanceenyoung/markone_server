webpackJsonp([1],{"+6Bu":function(t,e,n){"use strict";e.__esModule=!0,e.default=function(t,e){var n={};for(var i in t)e.indexOf(i)>=0||Object.prototype.hasOwnProperty.call(t,i)&&(n[i]=t[i]);return n}},"+E39":function(t,e,n){t.exports=!n("S82l")(function(){return 7!=Object.defineProperty({},"a",{get:function(){return 7}}).a})},"+ZMJ":function(t,e,n){var i=n("lOnJ");t.exports=function(t,e,n){if(i(t),void 0===e)return t;switch(n){case 1:return function(n){return t.call(e,n)};case 2:return function(n,i){return t.call(e,n,i)};case 3:return function(n,i,o){return t.call(e,n,i,o)}}return function(){return t.apply(e,arguments)}}},"1kS7":function(t,e){e.f=Object.getOwnPropertySymbols},"3Eo+":function(t,e){var n=0,i=Math.random();t.exports=function(t){return"Symbol(".concat(void 0===t?"":t,")_",(++n+i).toString(36))}},"52gC":function(t,e){t.exports=function(t){if(void 0==t)throw TypeError("Can't call method on  "+t);return t}},"77Pl":function(t,e,n){var i=n("EqjI");t.exports=function(t){if(!i(t))throw TypeError(t+" is not an object!");return t}},"7KvD":function(t,e){var n=t.exports="undefined"!=typeof window&&window.Math==Math?window:"undefined"!=typeof self&&self.Math==Math?self:Function("return this")();"number"==typeof __g&&(__g=n)},"D+19":function(t,e){},D2L2:function(t,e){var n={}.hasOwnProperty;t.exports=function(t,e){return n.call(t,e)}},Dd8w:function(t,e,n){"use strict";e.__esModule=!0;var i,o=n("woOf"),r=(i=o)&&i.__esModule?i:{default:i};e.default=r.default||function(t){for(var e=1;e<arguments.length;e++){var n=arguments[e];for(var i in n)Object.prototype.hasOwnProperty.call(n,i)&&(t[i]=n[i])}return t}},EqjI:function(t,e){t.exports=function(t){return"object"==typeof t?null!==t:"function"==typeof t}},GKmE:function(t,e,n){"use strict";n.d(e,"b",function(){return i}),n.d(e,"a",function(){return o});var i=function(t){if(!t)return"";var e=new Date(t).toString().split(" ");return e[1]+" "+e[2]+", "+e[3]},o={bind:function(t,e,n){function i(n){if(t.contains(n.target))return!1;e.expression&&e.value(n)}t.__vueClickOutside__=i,document.addEventListener("click",i)},unbind:function(t,e){document.removeEventListener("click",t.__vueClickOutside__),delete t.__vueClickOutside__}}},HVxx:function(t,e){},Ibhu:function(t,e,n){var i=n("D2L2"),o=n("TcQ7"),r=n("vFc/")(!1),s=n("ax3d")("IE_PROTO");t.exports=function(t,e){var n,a=o(t),c=0,u=[];for(n in a)n!=s&&i(a,n)&&u.push(n);for(;e.length>c;)i(a,n=e[c++])&&(~r(u,n)||u.push(n));return u}},MU5D:function(t,e,n){var i=n("R9M2");t.exports=Object("z").propertyIsEnumerable(0)?Object:function(t){return"String"==i(t)?t.split(""):Object(t)}},MmMw:function(t,e,n){var i=n("EqjI");t.exports=function(t,e){if(!i(t))return t;var n,o;if(e&&"function"==typeof(n=t.toString)&&!i(o=n.call(t)))return o;if("function"==typeof(n=t.valueOf)&&!i(o=n.call(t)))return o;if(!e&&"function"==typeof(n=t.toString)&&!i(o=n.call(t)))return o;throw TypeError("Can't convert object to primitive value")}},NpIQ:function(t,e){e.f={}.propertyIsEnumerable},O4g8:function(t,e){t.exports=!0},ON07:function(t,e,n){var i=n("EqjI"),o=n("7KvD").document,r=i(o)&&i(o.createElement);t.exports=function(t){return r?o.createElement(t):{}}},QRG4:function(t,e,n){var i=n("UuGF"),o=Math.min;t.exports=function(t){return t>0?o(i(t),9007199254740991):0}},R4wc:function(t,e,n){var i=n("kM2E");i(i.S+i.F,"Object",{assign:n("To3L")})},R9M2:function(t,e){var n={}.toString;t.exports=function(t){return n.call(t).slice(8,-1)}},S82l:function(t,e){t.exports=function(t){try{return!!t()}catch(t){return!0}}},SfB7:function(t,e,n){t.exports=!n("+E39")&&!n("S82l")(function(){return 7!=Object.defineProperty(n("ON07")("div"),"a",{get:function(){return 7}}).a})},TcQ7:function(t,e,n){var i=n("MU5D"),o=n("52gC");t.exports=function(t){return i(o(t))}},To3L:function(t,e,n){"use strict";var i=n("lktj"),o=n("1kS7"),r=n("NpIQ"),s=n("sB3e"),a=n("MU5D"),c=Object.assign;t.exports=!c||n("S82l")(function(){var t={},e={},n=Symbol(),i="abcdefghijklmnopqrst";return t[n]=7,i.split("").forEach(function(t){e[t]=t}),7!=c({},t)[n]||Object.keys(c({},e)).join("")!=i})?function(t,e){for(var n=s(t),c=arguments.length,u=1,l=o.f,d=r.f;c>u;)for(var f,h=a(arguments[u++]),g=l?i(h).concat(l(h)):i(h),p=g.length,v=0;p>v;)d.call(h,f=g[v++])&&(n[f]=h[f]);return n}:c},UuGF:function(t,e){var n=Math.ceil,i=Math.floor;t.exports=function(t){return isNaN(t=+t)?0:(t>0?i:n)(t)}},V3tA:function(t,e,n){n("R4wc"),t.exports=n("FeBl").Object.assign},X8DO:function(t,e){t.exports=function(t,e){return{enumerable:!(1&t),configurable:!(2&t),writable:!(4&t),value:e}}},ax3d:function(t,e,n){var i=n("e8AB")("keys"),o=n("3Eo+");t.exports=function(t){return i[t]||(i[t]=o(t))}},e8AB:function(t,e,n){var i=n("FeBl"),o=n("7KvD"),r=o["__core-js_shared__"]||(o["__core-js_shared__"]={});(t.exports=function(t,e){return r[t]||(r[t]=void 0!==e?e:{})})("versions",[]).push({version:i.version,mode:n("O4g8")?"pure":"global",copyright:"© 2018 Denis Pushkarev (zloirock.ru)"})},evD5:function(t,e,n){var i=n("77Pl"),o=n("SfB7"),r=n("MmMw"),s=Object.defineProperty;e.f=n("+E39")?Object.defineProperty:function(t,e,n){if(i(t),e=r(e,!0),i(n),o)try{return s(t,e,n)}catch(t){}if("get"in n||"set"in n)throw TypeError("Accessors not supported!");return"value"in n&&(t[e]=n.value),t}},fU5E:function(t,e){},fkB2:function(t,e,n){var i=n("UuGF"),o=Math.max,r=Math.min;t.exports=function(t,e){return(t=i(t))<0?o(t+e,0):r(t,e)}},hJx8:function(t,e,n){var i=n("evD5"),o=n("X8DO");t.exports=n("+E39")?function(t,e,n){return i.f(t,e,o(1,n))}:function(t,e,n){return t[e]=n,t}},kM2E:function(t,e,n){var i=n("7KvD"),o=n("FeBl"),r=n("+ZMJ"),s=n("hJx8"),a=n("D2L2"),c=function(t,e,n){var u,l,d,f=t&c.F,h=t&c.G,g=t&c.S,p=t&c.P,v=t&c.B,m=t&c.W,_=h?o:o[e]||(o[e]={}),y=_.prototype,b=h?i:g?i[e]:(i[e]||{}).prototype;for(u in h&&(n=e),n)(l=!f&&b&&void 0!==b[u])&&a(_,u)||(d=l?b[u]:n[u],_[u]=h&&"function"!=typeof b[u]?n[u]:v&&l?r(d,i):m&&b[u]==d?function(t){var e=function(e,n,i){if(this instanceof t){switch(arguments.length){case 0:return new t;case 1:return new t(e);case 2:return new t(e,n)}return new t(e,n,i)}return t.apply(this,arguments)};return e.prototype=t.prototype,e}(d):p&&"function"==typeof d?r(Function.call,d):d,p&&((_.virtual||(_.virtual={}))[u]=d,t&c.R&&y&&!y[u]&&s(y,u,d)))};c.F=1,c.G=2,c.S=4,c.P=8,c.B=16,c.W=32,c.U=64,c.R=128,t.exports=c},lOnJ:function(t,e){t.exports=function(t){if("function"!=typeof t)throw TypeError(t+" is not a function!");return t}},lktj:function(t,e,n){var i=n("Ibhu"),o=n("xnc9");t.exports=Object.keys||function(t){return i(t,o)}},mnWG:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i=n("Dd8w"),o=n.n(i),r=n("+6Bu"),s=n.n(r),a={render:function(){var t=this.$createElement;return(this._self._c||t)("ul",{staticClass:"list"},[this._t("default")],2)},staticRenderFns:[]};var c=n("VU/8")({},a,!1,function(t){n("HVxx")},null,null).exports,u=n("PHrY"),l={render:function(){var t=this,e=t.$createElement;return(t._self._c||e)("div",{directives:[{name:"focus",rawName:"v-focus"}],attrs:{contenteditable:"true"},on:{input:t.update,blur:function(e){t.$emit("edited")},keyup:function(e){if(!("button"in e)&&t._k(e.keyCode,"esc",27,e.key,"Escape"))return null;t.$emit("cancel")}}})},staticRenderFns:[]},d={data:function(){return{editing:!1,content:null}},props:["item","isHighlight","img","isVideo","origin","startTime","isTrash","notesUuid","itemUuid"],components:{EditAble:n("VU/8")({props:["content"],methods:{update:function(t){this.$emit("update",t.target.innerText)}},mounted:function(){this.$el.innerText=this.content},directives:{focus:{inserted:function(t){t.focus()}}}},l,!1,null,null,null).exports},methods:{highlight:function(){this.$emit("tohighlight")},edit:function(){this.content=this.item,this.editing=!0},edited:function(){var t=this;if(this.editing=!1,this.content!==this.item){var e={user:this.$store.getters.uuid,notes:this.notesUuid,remark:this.content};Object(u.l)(this.itemUuid,e).then(function(t){t.status}).catch(function(){t.content=t.item})}},cancel:function(){this.editing=!1,this.content=this.item}},computed:{jumpLink:function(){return-1!==this.origin.indexOf("youtu")?"https://youtu.be/"+this.origin.split("=")[1]+"?t="+Math.floor(this.startTime):this.origin}},mounted:function(){this.content=this.item}},f={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return t.isTrash?t._e():n("li",{class:{"list-item":!0,"has-left-radius":t.isHighlight,"border-left-radius":t.isHighlight,editing:t.editing}},[t.editing?n("edit-able",{staticClass:"list-item-edit",attrs:{content:t.content},on:{update:function(e){t.content=e},edited:t.edited,cancel:t.cancel}}):t._e(),t._v(" "),t.img&&!t.editing?n("div",{class:{"list-item-img-box":!0,"border-box-radius":t.isHighlight}},[n("img",{staticClass:"list-item-img",attrs:{src:t.img,alt:"Markone"},on:{click:function(e){t.$emit("clickShowImg")}}})]):t._e(),t._v(" "),t.img||t.editing?t._e():n("p",{staticClass:"list-item-text",on:{dblclick:t.edit}},[t._v(t._s(t.content))]),t._v(" "),t.editing?t._e():n("div",{staticClass:"list-item-delete",attrs:{title:"Move to trash"},on:{click:function(e){t.$emit("toTrash")}}},[n("span",[t._v("×")])]),t._v(" "),t.editing?t._e():n("div",{staticClass:"list-item-box"},[n("span",{staticClass:"list-item-box-icon",attrs:{title:t.isHighlight?"Unmark":"Mark"},on:{click:t.highlight}},[n("icon-svg",{attrs:{"icon-class":t.isHighlight?"highlighted":"highlight"}})],1),t._v(" "),n("span",{class:{"list-item-box-icon":!0,ban:!t.isVideo},attrs:{title:"Return to video"}},[t.isVideo?n("a",{staticClass:"list-item-box-icon-link",attrs:{href:t.jumpLink,target:"_blank"}}):t._e(),t._v(" "),n("icon-svg",{attrs:{"icon-class":"back-to-video"}})],1)])],1)},staticRenderFns:[]};var h=n("VU/8")(d,f,!1,function(t){n("D+19")},"data-v-716a62a4",null).exports,g="0.3s height ease-in-out, 0.3s padding-top ease-in-out, 0.3s padding-bottom ease-in-out",p={"before-enter":function(t){t.style.transition=g,t.dataset||(t.dataset={}),t.dataset.oldPaddingTop=t.style.paddingTop,t.dataset.oldPaddingBottom=t.style.paddingBottom,t.style.height=0,t.style.paddingTop=0,t.style.paddingBottom=0},enter:function(t){t.dataset.oldOverflow=t.style.overflow,0!==t.scrollHeight?(t.style.height=t.scrollHeight+"px",t.style.paddingTop=t.dataset.oldPaddingTop,t.style.paddingBottom=t.dataset.oldPaddingBottom):(t.style.height="",t.style.paddingTop=t.dataset.oldPaddingTop,t.style.paddingBottom=t.dataset.oldPaddingBottom),t.style.overflow="hidden"},"after-enter":function(t){t.style.transition="",t.style.height="",t.style.overflow=t.dataset.oldOverflow},"before-leave":function(t){t.dataset||(t.dataset={}),t.dataset.oldPaddingTop=t.style.paddingTop,t.dataset.oldPaddingBottom=t.style.paddingBottom,t.dataset.oldOverflow=t.style.overflow,t.style.height=t.scrollHeight+"px",t.style.overflow="hidden"},leave:function(t){0!==t.scrollHeight&&(t.style.transition=g,t.style.height=0,t.style.paddingTop=0,t.style.paddingBottom=0)},"after-leave":function(t){t.style.transition="",t.style.height="",t.style.overflow=t.dataset.oldOverflow,t.style.paddingTop=t.dataset.oldPaddingTop,t.style.paddingBottom=t.dataset.oldPaddingBottom}},v={name:"collapseTransition",functional:!0,render:function(t,e){var n=e.children;return t("transition",{on:p},n)}},m=n("VU/8")(v,null,!1,null,null,null).exports,_=n("I+qJ"),y=n("zXoH"),b=n("GKmE"),x={data:function(){return{notes:[],loading:!1,showImg:!1,imgSrc:"",copyList:[],next:null,previous:null,current:1,loadingmore:!1,nomoredata:!1}},components:{SortableList:c,SortableItem:h,CollapseTransition:m,NoData:_.a,BigImg:y.a},watch:{$route:function(){this.notes=[],this.getdata()}},methods:{getdata:function(){var t=this;this.loading=!0,this.$route.params.uuid?Object(u.e)(this.$route.params.uuid).then(function(e){if(200===e.status){var n=e.data,i=n.sections,r=s()(n,["sections"]);t.notes.push(o()({show:i},r)),t.loading=!1}}).catch(function(){t.loading=!1}):Object(u.d)({page:this.current}).then(function(e){e.data&&(t.next=e.data.next,t.previous=e.data.previous,e.data.next&&t.next>=2&&(t.current=t.next-1),e.data.results.forEach(function(e){var n=e.sections,i=s()(e,["sections"]),r={show:[],fold:[]};if(e.sections.length<=3)for(var a=0,c=e.sections.length;a<c;a++)r.show.push(e.sections[a]);else{for(var u=0;u<3;u++)r.show.push(e.sections[u]);for(var l=3,d=e.sections.length;l<d;l++)r.fold.push(e.sections[l])}n.length&&t.notes.push(o()({},i,r,{noteVisible:!1,sections:n}))}),t.loading=!1)}).catch(function(){t.nomoredata=!0,t.loading=!1})},highLight:function(t,e,n){var i=this,o={highlight:!n,notes:t,user:this.$store.getters.uuid};Object(u.l)(e,o).then(function(t){200===t.status&&(i.notes=[],i.getdata())})},totrash:function(t,e){var n=this,i={trash:!0,notes:t,user:this.$store.getters.uuid};Object(u.l)(e,i).then(function(t){200===t.status&&(n.notes=[],n.getdata(),n.$toast("Moved to Trash",1500))})},clickImg:function(t){t&&(this.imgSrc=t,this.showImg=!0)},viewImg:function(){this.showImg=!1},copyAll:function(t){var e=this;this.copyList=t.sections,setTimeout(function(){var t=document.createRange();t.selectNode(document.getElementById("section"));var n=window.getSelection();n.rangeCount>0&&n.removeAllRanges(),n.addRange(t),document.execCommand("copy")&&e.$toast("Copied")},500)},loadMore:function(){this.loadingmore=!0,this.current++,this.getdata()},scrollToTop:function(t){document.getElementById(t).scrollIntoView({block:"start",behavior:"smooth"})}},mounted:function(){this.getdata()},filters:{formatDate:b.b}},w={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"notes",attrs:{id:"scroll"}},[t.$route.params.uuid?n("div",{staticClass:"back-to-notes",on:{click:function(e){t.$router.push("/notes")}}},[n("span",{staticClass:"back-to-notes-icon"},[n("icon-svg",{attrs:{"icon-class":"down"}})],1),t._v(" "),n("span",[t._v("Back to notes")])]):t._e(),t._v(" "),t._l(t.notes,function(e){return n("div",{key:e.id,staticClass:"note-list"},[n("div",{class:{"note-list-header":!0,"params-header":t.$route.params.title}},[t._m(0,!0),t._v(" "),n("span",{staticClass:"note-list-header-icon",on:{click:function(n){t.copyAll(e)}}},[t._v("Copy all")]),t._v(" "),n("h4",{attrs:{id:e.title},on:{click:function(n){t.scrollToTop(e.title)}}},[t._v(t._s(e.title))])]),t._v(" "),n("sortable-list",[t._l(e.show,function(i,o){return n("sortable-item",{key:i.uuid,attrs:{index:o,item:i.remark,isHighlight:i.highlight,img:i.image,notesUuid:e.uuid,isVideo:i.is_video,origin:e.origin,itemUuid:i.uuid,startTime:i.start_time,isTrash:i.trash},on:{clickShowImg:function(e){t.clickImg(i.image)},tohighlight:function(n){t.highLight(e.uuid,i.uuid,i.highlight)},toTrash:function(n){t.totrash(e.uuid,i.uuid)}}})}),t._v(" "),n("collapse-transition",[n("div",{directives:[{name:"show",rawName:"v-show",value:e.noteVisible,expression:"note.noteVisible"}],staticClass:"collapse"},t._l(e.fold,function(i,o){return n("sortable-item",{key:i.uuid,attrs:{index:o,item:i.remark,isHighlight:i.highlight,img:i.image,isVideo:i.is_video,origin:e.origin,startTime:i.start_time,isTrash:i.trash},on:{clickShowImg:function(e){t.clickImg(i.image)},tohighlight:function(n){t.highLight(e.uuid,i.uuid,i.highlight)},toTrash:function(n){t.totrash(e.uuid,i.uuid)}}})}))])],2),t._v(" "),n("div",{staticClass:"note-list-footer"},[e.fold&&e.fold.length?n("p",{staticClass:"note-list-footer-box",on:{click:function(t){e.noteVisible=!e.noteVisible}}},[t._v("\n        "+t._s(e.noteVisible?"Fold":"More")+" \n        "),n("span",{class:{"note-list-footer-box-icon":!0,rotate:!e.noteVisible}},[n("icon-svg",{attrs:{"icon-class":"down"}})],1)]):t._e(),t._v(" "),n("p",{staticClass:"note-list-footer-time"},[t._v("Edited: "+t._s(t._f("formatDate")(e.updated_at)))]),t._v(" "),n("p",{staticClass:"note-list-footer-link"},[t._v("  From: "),n("a",{attrs:{href:e.origin,target:"_blank"}},[n("span",[t._v(t._s(e.origin))])])])])],1)}),t._v(" "),t.loading||!t.notes.length||t.next?n("no-data",{attrs:{loading:t.loading,nodata:!t.loading&&!t.notes.length,next:t.next,loadingmore:t.loadingmore,nomoredata:t.nomoredata},on:{loadMore:t.loadMore}}):t._e(),t._v(" "),t.showImg?n("big-img",{attrs:{imgSrc:t.imgSrc},on:{clickit:t.viewImg}}):t._e(),t._v(" "),n("div",{staticClass:"copy-bord"},[n("div",{ref:"copyBord",attrs:{id:"section"}},t._l(t.copyList,function(e){return"null"!==e.remark?n("p",{key:e.uuid},[t._v(t._s(e.remark))]):t._e()}))])],2)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("span",{staticClass:"note-list-header-title"},[e("span")])}]};var k=n("VU/8")(x,w,!1,function(t){n("fU5E")},"data-v-ec1f0638",null);e.default=k.exports},sB3e:function(t,e,n){var i=n("52gC");t.exports=function(t){return Object(i(t))}},"vFc/":function(t,e,n){var i=n("TcQ7"),o=n("QRG4"),r=n("fkB2");t.exports=function(t){return function(e,n,s){var a,c=i(e),u=o(c.length),l=r(s,u);if(t&&n!=n){for(;u>l;)if((a=c[l++])!=a)return!0}else for(;u>l;l++)if((t||l in c)&&c[l]===n)return t||l||0;return!t&&-1}}},woOf:function(t,e,n){t.exports={default:n("V3tA"),__esModule:!0}},xnc9:function(t,e){t.exports="constructor,hasOwnProperty,isPrototypeOf,propertyIsEnumerable,toLocaleString,toString,valueOf".split(",")}});