webpackJsonp([12],{sqie:function(t,n,e){"use strict";Object.defineProperty(n,"__esModule",{value:!0});var i=e("mvHQ"),o=e.n(i),a=e("PHrY"),u={data:function(){return{auth2:null}},methods:{startApp:function(){var t=this;window.gapi.load("auth2",function(){t.auth2=window.gapi.auth2.init({client_id:"728616517590-om5s9j1llfcbaru8t5al706r2tu5faqo.apps.googleusercontent.com",cookiepolicy:"single_host_origin",scope:"profile"}),t.attachSignin()})},attachSignin:function(){var t=this;this.auth2.attachClickHandler(this.$refs.customBtn,{},function(){var n=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};document.getElementById("name").innerHTML="Signed in: "+n.getBasicProfile().getName();var e=t.auth2.currentUser.get().getBasicProfile(),i={email:e.getEmail(),name:e.getName(),avatar:e.getImageUrl(),token:n.getAuthResponse().id_token};Object(a.g)(i).then(function(t){t.data&&console.log(t.data)})},function(t){console.log(o()(t,void 0,2))})},signOut:function(){window.gapi.auth2.getAuthInstance().signOut().then(function(){console.log("Uer signed out.")})}},mounted:function(){this.startApp()}},s={render:function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("div",{staticClass:"google"},[e("button",{ref:"customBtn",attrs:{type:"button"}},[t._v("Google登录")]),t._v(" "),e("div",{attrs:{id:"name"}}),t._v(" "),e("button",{attrs:{type:"button"},on:{click:function(n){t.signOut()}}},[t._v("Sign out")])])},staticRenderFns:[]},c=e("VU/8")(u,s,!1,null,null,null);n.default=c.exports}});