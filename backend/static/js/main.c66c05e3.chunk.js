(this["webpackJsonptezos-flame-defi"]=this["webpackJsonptezos-flame-defi"]||[]).push([[0],{196:function(e,t,c){},198:function(e,t,c){},216:function(e,t,c){},217:function(e,t,c){},287:function(e,t,c){},291:function(e,t,c){},292:function(e,t,c){},304:function(e,t,c){},309:function(e,t,c){"use strict";c.r(t);var a=c(0),l=c.n(a),n=c(40),i=c.n(n),s=c(25),r=(c(196),c(7)),o=function(){return Object(r.jsxs)("div",{className:"header",children:[Object(r.jsx)("div",{className:"header__logo"}),Object(r.jsx)("div",{className:"header__label",children:"\u041f\u043e\u0438\u0441\u043a \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432"})]})},d=(c(198),function(){return Object(r.jsxs)("div",{className:"base-layout",children:[Object(r.jsx)(o,{}),Object(r.jsx)("div",{className:"base-layout__main",children:Object(r.jsx)(s.a,{})})]})}),u=c(6),j=c(3),b=c(5),O=c(177),p=c.n(O).a.create({baseURL:"/api",timeout:6e5});var h={get:p.get,delete:p.delete,post:p.post,put:p.put,patch:p.patch,request:p.request};function v(){return h.get("/items")}function x(e){var t=e.search;return h.get("/item",{params:{search:t}})}function m(e){var t=e.id;return h.get("/suppliers",{params:{item:t}}).then((function(e){return{data:e.data.reduce((function(e,t){return e.find((function(e){return e.inn===t.inn}))?e:[].concat(Object(u.a)(e),[t])}),[])}}))}function f(){return h.get("/statistics")}var _=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},c=arguments.length>2&&void 0!==arguments[2]&&arguments[2],l=Object(a.useState)(t),n=Object(b.a)(l,2),i=n[0],s=n[1],r=Object(a.useState)(!1),o=Object(b.a)(r,2),d=o[0],u=o[1],O=Object(a.useState)(),p=Object(b.a)(O,2),h=p[0],v=p[1],x=Object(a.useState)(!1),m=Object(b.a)(x,2),f=m[0],_=m[1],g=Object(a.useState)(!1),C=Object(b.a)(g,2),N=C[0],S=C[1],y=Object(a.useState)(""),k=Object(b.a)(y,2),w=k[0],I=k[1],E=Object(a.useState)(0),L=Object(b.a)(E,2),A=L[0],z=L[1],M=function(){return z((function(e){return e+1}))},R=Object(a.useCallback)((function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};return u(!0),e(Object(j.a)(Object(j.a)({},i),t)).then((function(e){return 200===e.status?v(e.data):(_(!0),I(e.data)),e.data})).catch((function(e){_(!0),I(null===e||void 0===e?void 0:e.message)})).finally((function(){u(!1),S(!0)}))}),[u,e,i,v,_,I]);return Object(a.useEffect)((function(){c&&R()}),[R,c,A]),{fetch:R,data:h,isLoading:d,isDone:N,hasError:f,errorMessage:w,updateParams:s,refetch:M}},g=c(321),C=c(43),N=c(311),S=c(189),y=c(323),k=c(324),w=(c(216),c(310)),I=c(188),E=(c(217),function(e){var t=e.onAdd,c=e.onSelect,l=e.options,n=e.loading,i=void 0!==n&&n,s=Object(a.useState)([]),o=Object(b.a)(s,2),d=o[0],O=o[1],p=Object(a.useState)(""),h=Object(b.a)(p,2),v=h[0],x=h[1];Object(a.useEffect)((function(){var e=l.reduce((function(e,t){var c,a=t.items.map((function(e){e.id;var t,c,a=e.label,l=e.activeSuppliers;return Object(j.a)({},(c=l,{value:t=a,label:Object(r.jsxs)("div",{style:{display:"flex",justifyContent:"space-between"},children:[t,c&&Object(r.jsxs)("span",{children:["\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432 ",c]})]})}))})),l={value:t.title,title:t.title,label:(c=t.title,Object(r.jsx)("span",{children:c})),options:a};return[].concat(Object(u.a)(e),[l])}),[]);O(e)}),[l,O]);var m=Object(a.useCallback)((function(e){c(e)}),[c]),f=Object(a.useCallback)((function(){c("")}),[c]),_=Object(a.useCallback)((function(e){x(e)}),[x]),g=Object(a.useCallback)((function(){t(v)}),[t,v]),N=Object(a.useMemo)((function(){return Object(r.jsxs)("div",{className:"add-item-form__empty",children:[Object(r.jsx)("span",{className:"add-item-form__empty-text",children:"\u041d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u043e"}),Object(r.jsx)(C.a,{icon:Object(r.jsx)(I.a,{}),onClick:g,className:"add-item-form__button",loading:i,children:"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0443"})]})}),[g,i]);return Object(r.jsx)("div",{className:"add-item-form",children:Object(r.jsx)(w.a,{className:"add-item-form__search",dropdownClassName:"add-item-form__search-dropdown",options:d,onClear:f,onSelect:m,onSearch:_,filterOption:function(e,t){return t.value.toLowerCase().includes(e.toLowerCase())},notFoundContent:N,placeholder:"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e \u043d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u044b",allowClear:!0})})}),L=c(8),A=c(68),z=c(319),M=c(180),R=c(89),P=c(69),T=c(320),D=(c(287),["name","inn","contacts","status","capitalization","created_at","debet","credit"]),U=A.a.Option,F=Object(a.memo)((function(e){var t=e.onClose,c=e.visible,l=e.suppliers,n=e.loading,i=Object(a.useState)(""),s=Object(b.a)(i,2),o=s[0],d=s[1],O=Object(a.useState)(""),p=Object(b.a)(O,2),h=p[0],v=p[1],x=Object(a.useMemo)((function(){return l.reduce((function(e,t){return e.find((function(e){return e.inn===t.inn}))?e:[].concat(Object(u.a)(e),[t])}),[])}),[l]),m=Object(a.useMemo)((function(){return x}),[x,o,h]),f=Object(a.useCallback)((function(e){d(e)}),[d]),_=Object(a.useCallback)((function(e){v(e.target.checked?"direct":"")}),[v]);return Object(r.jsxs)(z.a,{title:"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0438",placement:"right",onClose:t,visible:c,width:"30vw",children:[n&&Object(r.jsx)(M.a,{}),Object(r.jsxs)("div",{className:"suppliers-list__filter",children:[Object(r.jsxs)("div",{className:"suppliers-list__row",children:[Object(r.jsxs)(A.a,{placeholder:"\u0423\u0447\u0440\u0435\u0434\u0438\u0442\u0435\u043b\u044c..",className:"suppliers-list__select",allowClear:!0,children:[Object(r.jsx)(U,{value:"rus",children:"\u0420\u043e\u0441\u0441\u0438\u0439\u0441\u043a\u0438\u0439"}),Object(r.jsx)(U,{value:"out",children:"\u0417\u0430\u0440\u0443\u0431\u0435\u0436\u043d\u044b\u0439"})]}),Object(r.jsx)(A.a,{onChange:f,placeholder:"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e..",className:"suppliers-list__select",allowClear:!0,children:Object(r.jsx)(U,{value:"reliability",children:"\u0421\u043f\u0435\u0440\u0432\u0430 \u043d\u0430\u0434\u0435\u0436\u043d\u044b\u0435"})})]}),Object(r.jsx)(R.a,{onChange:_,children:"\u0422\u043e\u043b\u044c\u043a\u043e \u043f\u0440\u044f\u043c\u044b\u0435 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0438"})]}),!n&&Object(r.jsxs)(r.Fragment,{children:[!l.length&&Object(r.jsx)(P.a,{image:P.a.PRESENTED_IMAGE_SIMPLE}),m.map((function(e,t){return Object(a.createElement)(q,Object(j.a)(Object(j.a)({},e),{},{key:t}))}))]})]})})),q=function(e){var t=e.name,c=e.inn,l=e.contacts,n=e.status,i=e.capitalization,s=e.created_at,o=e.debet,d=e.credit,u=Object(L.a)(e,D),j=Object(a.useMemo)((function(){return new Date(parseInt(s)).toLocaleDateString()}),[s]);console.log(u);var b=Object(a.useCallback)((function(){var e="".concat(t," \u0418\u041d\u041d ").concat(c," \u043e\u0442\u0437\u044b\u0432\u044b");window.open("https://yandex.ru/search/?text=".concat(e),"_blank")}),[]);return Object(r.jsxs)("div",{className:"supplier",children:[Object(r.jsxs)("div",{className:"supplier__status",children:["ACTIVE"===n&&Object(r.jsx)(T.a,{color:"green",children:"\u0414\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0430\u044f"}),"LIQUIDATING"===n&&Object(r.jsx)(T.a,{color:"volcano",children:"\u041b\u0438\u043a\u0432\u0438\u0434\u0438\u0440\u0443\u0435\u0442\u0441\u044f"}),"LIQUIDATED"===n&&Object(r.jsx)(T.a,{color:"volcano",children:"\u041b\u0438\u043a\u0432\u0438\u0434\u0438\u0440\u043e\u0432\u0430\u043d\u0430"}),"BANKRUPT"===n&&Object(r.jsx)(T.a,{color:"volcano",children:"\u0411\u0430\u043d\u043a\u0440\u043e\u0442\u0441\u0442\u0432\u043e"}),"REORGANIZING"===n&&Object(r.jsx)(T.a,{color:"volcano",children:"\u0420\u0435\u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f"})]}),t&&Object(r.jsx)("div",{className:"supplier__name",children:t}),c&&Object(r.jsxs)("div",{className:"supplier__row",children:[Object(r.jsx)("div",{className:"supplier__label",children:"\u0418\u041d\u041d:"}),Object(r.jsx)("div",{className:"supplier__value",children:c})]}),s&&Object(r.jsxs)("div",{className:"supplier__row",children:[Object(r.jsx)("div",{className:"supplier__label",children:"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f:"}),Object(r.jsx)("div",{className:"supplier__value",children:j})]}),l&&Object(r.jsxs)("div",{className:"supplier__row",children:[Object(r.jsx)("div",{className:"supplier__label",children:"\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b:"}),Object(r.jsx)("div",{className:"supplier__value",children:l})]}),i&&Object(r.jsxs)("div",{className:"supplier__row",children:[Object(r.jsx)("div",{className:"supplier__label",children:"\u041a\u0430\u043f\u0438\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f:"}),Object(r.jsx)("div",{className:"supplier__value",children:i})]}),o&&Object(r.jsxs)("div",{className:"supplier__row",children:[Object(r.jsx)("div",{className:"supplier__label",children:"\u0414\u0435\u0431\u0438\u0442\u043e\u0440\u0441\u043a\u0430\u044f \u0437\u0430\u0434\u043e\u043b\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u044c:"}),Object(r.jsx)("div",{className:"supplier__value",children:o})]}),d&&Object(r.jsxs)("div",{className:"supplier__row",children:[Object(r.jsx)("div",{className:"supplier__label",children:"\u041a\u0440\u0435\u0434\u0438\u0442\u043e\u0440\u0441\u043a\u0430\u044f \u0437\u0430\u0434\u043e\u043b\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u044c:"}),Object(r.jsx)("div",{className:"supplier__value",children:d})]}),Object(r.jsx)(C.a,{type:"link",size:"small",onClick:b,className:"supplier__reviews",children:"\u0421\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043e\u0442\u0437\u044b\u0432\u044b"})]})},G=c(318),K=c(314),B=c(185),V=c(316),J=c(317),Q=c(312),W=c(322),Z=(c(291),G.a.Panel),H=Object(a.memo)((function(e){var t=e.search,c=e.visible,l=e.onClose,n=e.onSubmit,i=Object(a.useState)(t),s=Object(b.a)(i,2),o=s[0],d=s[1];Object(a.useEffect)((function(){d(t)}),[t,d]);var u=function(){l&&l()},j=Object(a.useMemo)((function(){return Object(r.jsxs)(r.Fragment,{children:[Object(r.jsx)(K.a.Item,{label:"\u0410\u0434\u0440\u0435\u0441 \u043e\u0431\u044a\u0435\u043a\u0442\u0430",tooltip:"\u0418\u0441\u043a\u0430\u0442\u044c \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432 \u0434\u043b\u044f \u043e\u0431\u044a\u0435\u043a\u0442\u0430 \u043f\u043e \u0430\u0434\u0440\u0435\u0441\u0443",wrapperCol:{span:10},children:Object(r.jsx)(B.a,{})}),Object(r.jsx)(K.a.Item,{label:"\u041c\u0438\u043d. \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",tooltip:"\u0412\u043b\u0438\u044f\u0435\u0442 \u043d\u0430 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043f\u043e\u0438\u0441\u043a\u0430",labelCol:{span:17},children:Object(r.jsx)(V.a,{min:0})}),Object(r.jsx)(K.a.Item,{label:"\u041c\u0438\u043d. \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \xab\u043d\u0430\u0434\u0451\u0436\u043d\u044b\u0445\xbb \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",tooltip:"\u0412\u043b\u0438\u044f\u0435\u0442 \u043d\u0430 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043f\u043e\u0438\u0441\u043a\u0430",labelCol:{span:17},children:Object(r.jsx)(V.a,{min:0})}),Object(r.jsx)(K.a.Item,{valuePropName:"checked",children:Object(r.jsx)(R.a,{children:"\u0418\u0441\u043a\u0430\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0445 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432"})}),Object(r.jsx)(K.a.Item,{valuePropName:"checked",className:"settings__checkbox",children:Object(r.jsx)(R.a,{children:"\u0418\u0441\u043a\u0430\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439"})})]})}),[]),O=Object(a.useMemo)((function(){return Object(r.jsxs)(r.Fragment,{children:[Object(r.jsx)(K.a.Item,{label:"\u0423\u0441\u0442\u0430\u0432\u043d\u043e\u0439 \u043a\u0430\u043f\u0438\u0442\u0430\u043b, \u043d\u0435 \u043c\u0435\u043d\u0435\u0435",labelCol:{span:12},children:Object(r.jsx)(V.a,{min:0})}),Object(r.jsx)(K.a.Item,{label:"\u041b\u0435\u0442 \u0440\u0430\u0431\u043e\u0442\u044b, \u043d\u0435 \u043c\u0435\u043d\u0435\u0435",labelCol:{span:12},children:Object(r.jsx)(V.a,{min:0})})]})}),[]);return Object(r.jsx)(J.a,{title:"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0438\u0441\u043a\u0430 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",visible:c,onCancel:u,footer:null,children:Object(r.jsxs)(K.a,{onFinish:function(){o&&(n&&n(o),u())},layout:"horizontal",labelWrap:!0,size:"small",labelAlign:"left",requiredMark:!1,children:[Object(r.jsx)(K.a.Item,{label:"\u041d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0430",name:"search",required:!0,children:Object(r.jsxs)(g.b,{direction:"vertical",style:{width:"100%"},children:[Object(r.jsx)(B.a,{placeholder:"\u041d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0430 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430",name:"search",value:o,onInput:function(e){return d(e.target.value)}}),Object(r.jsxs)(Q.a,{accept:".xsl,.xlsx,.csv",children:["\u0438\u043b\u0438 ",Object(r.jsx)(C.a,{icon:Object(r.jsx)(W.a,{}),children:"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 xls, csv"})]})]})}),Object(r.jsxs)(G.a,{ghost:!0,className:"settings",expandIconPosition:"left",defaultActiveKey:["1","2"],children:[Object(r.jsx)(Z,{header:"\u041c\u043e\u0434\u0443\u043b\u044c \u043f\u043e\u0438\u0441\u043a\u0430",children:j},"1"),Object(r.jsx)(Z,{header:"\u041c\u043e\u0434\u0443\u043b\u044c \u0441\u043a\u043e\u0440\u0438\u043d\u0433\u0430 \xab\u043d\u0430\u0434\u0451\u0436\u043d\u043e\u0433\u043e\xbb \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0430",children:O},"2")]}),Object(r.jsx)(K.a.Item,{noStyle:!0,children:Object(r.jsxs)(g.b,{className:"settings__footer",children:[Object(r.jsx)(C.a,{size:"middle",onClick:function(){l&&l()},type:"ghost",htmlType:"reset",children:"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c"}),Object(r.jsx)(C.a,{size:"middle",type:"primary",htmlType:"submit",children:"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c"})]})})]})})})),X=c(90),Y=c(57),$=c(313),ee=c(315),te=c(183),ce=(c(292),function(e){var t=e.visible,c=e.onCLose,l=_(f),n=Object(a.useState)({}),i=Object(b.a)(n,2),s=i[0],o=i[1];Object(a.useEffect)((function(){t&&l.fetch().then((function(e){console.log(e),o(e)}))}),[t]);return Object(r.jsx)(J.a,{title:"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u0432\u0441\u0435\u043c \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f\u043c",visible:t,onCancel:c,footer:null,width:"50vw",className:"statistic",children:Object(r.jsxs)(g.b,{direction:"vertical",size:12,children:[Object(r.jsxs)(X.a,{gutter:12,children:[Object(r.jsx)(Y.a,{span:12,children:Object(r.jsx)($.a,{children:Object(r.jsx)(ee.a,{title:"\u041d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u043d\u044b\u0445 \u043f\u043e\u0437\u0438\u0446\u0438\u0439 \u0432 \u0431\u0430\u0437\u0435",loading:l.isLoading,value:(null===s||void 0===s?void 0:s.items_count)||"-",valueStyle:{color:"#389e0d"}})})}),Object(r.jsx)(Y.a,{span:12,children:Object(r.jsx)($.a,{children:Object(r.jsx)(ee.a,{title:"\u041d\u0430\u0439\u0434\u0435\u043d\u043e URL \u043f\u043e \u043d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0430\u043c",loading:l.isLoading,value:(null===s||void 0===s?void 0:s.urls_count)||"-"})})})]}),Object(r.jsxs)(X.a,{gutter:12,children:[Object(r.jsx)(Y.a,{span:8,children:Object(r.jsx)($.a,{children:Object(r.jsx)(ee.a,{title:"\u0421\u0430\u0439\u0442\u043e\u0432 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",loading:l.isLoading,value:(null===s||void 0===s?void 0:s.direct_suppliers)||"-"})})}),Object(r.jsx)(Y.a,{span:8,children:Object(r.jsx)($.a,{children:Object(r.jsx)(ee.a,{title:"\u041f\u043b\u043e\u0449\u0430\u0434\u043e\u043a / \u043c\u0430\u0440\u043a\u0435\u0442\u043f\u043b\u0435\u0439\u0441\u043e\u0432",loading:l.isLoading,value:(null===s||void 0===s?void 0:s.markeplaces)||"-"})})}),Object(r.jsx)(Y.a,{span:8,children:Object(r.jsx)($.a,{children:Object(r.jsx)(ee.a,{title:"\u041d\u0435\u0440\u0435\u043b\u0435\u0432\u0430\u043d\u0442\u043d\u044b\u0445 \u0441\u0430\u0439\u0442\u043e\u0432",loading:l.isLoading,value:(null===s||void 0===s?void 0:s.trash_urls)||"-",valueStyle:{color:"#cf1322"}})})})]}),Object(r.jsxs)(X.a,{gutter:12,children:[Object(r.jsx)(Y.a,{span:8,children:Object(r.jsx)($.a,{children:Object(r.jsx)(ee.a,{title:"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432 \u043d\u0430\u0439\u0434\u0435\u043d\u043e",loading:l.isLoading,value:(null===s||void 0===s?void 0:s.suppliers)||"-",valueStyle:{color:"#389e0d"}})})}),Object(r.jsx)(Y.a,{span:8,children:Object(r.jsx)($.a,{children:Object(r.jsx)(ee.a,{title:"\u041d\u0430\u0434\u0435\u0436\u043d\u044b\u0445 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",loading:l.isLoading,value:(null===s||void 0===s?void 0:s.suppliers_active)||"-",valueStyle:{color:"#389e0d"}})})})]}),Object(r.jsxs)("div",{className:"statistic__chart",children:[Object(r.jsx)(te.PieChart,{data:[{title:"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",value:(null===s||void 0===s?void 0:s.suppliers_active)||0,color:"#E38627"},{title:"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435 \u043b\u0438\u043a\u0432\u0438\u0434\u0430\u0446\u0438\u0438 / \u043b\u0438\u043a\u0432\u0438\u0434\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435",value:(null===s||void 0===s?void 0:s.suppliers)-(null===s||void 0===s?void 0:s.suppliers_active)||0,color:"#C13C37"}]}),Object(r.jsxs)("div",{children:[Object(r.jsxs)("div",{className:"statistic__chart-legend",children:[Object(r.jsx)("div",{className:"statistic__round",style:{backgroundColor:"#E38627"}}),"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432"]}),Object(r.jsxs)("div",{className:"statistic__chart-legend",children:[Object(r.jsx)("div",{className:"statistic__round",style:{backgroundColor:"#C13C37"}}),"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435 \u043b\u0438\u043a\u0432\u0438\u0434\u0430\u0446\u0438\u0438 / \u043b\u0438\u043a\u0432\u0438\u0434\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435"]})]})]}),Object(r.jsx)("div",{className:"statistic__table-header",children:"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0441 \u043d\u0438\u0437\u043a\u043e\u0439 \u0434\u043e\u043b\u0435\u0439 \xab\u043d\u0430\u0434\u0451\u0436\u043d\u044b\u0445\xbb \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432"}),Object(r.jsx)(N.a,{columns:[{title:"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f",dataIndex:"title"},{title:"\u041d\u0430\u0434\u0435\u0436\u043d\u044b\u0445 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",dataIndex:"suppliers",width:"10%",align:"center"}],dataSource:[{key:1,title:"\u0411\u043e\u043b\u0442\u044b",suppliers:1},{key:2,title:"\u041c\u0430\u043d\u0436\u0435\u0442\u044b",suppliers:3}],pagination:{position:[]},bordered:!0,loading:l.isLoading})]})})}),ae=Object(r.jsx)("span",{className:"dashboard__empty-cell",children:"\u0412 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0435..."}),le=[{title:"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f",dataIndex:"category",key:"category",width:"18%",className:"dashboard__column--bold"},{title:"\u041d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0430",dataIndex:"label",key:"label",className:"dashboard__column--bold"},{title:"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",dataIndex:"activeSuppliers",key:"activeSuppliers",width:"12%",align:"right",className:"dashboard__column--bold",render:function(e,t){return t.label&&(null!==e&&void 0!==e?e:ae)}},{title:"\u041d\u0430\u0434\u0435\u0436\u043d\u044b\u0445 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",dataIndex:"reliableSuppliers",key:"reliableSuppliers",width:"12%",align:"right",className:"dashboard__column--bold",render:function(e,t){return t.label&&(null!==e&&void 0!==e?e:ae)}},{title:"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432 \u0431\u0435\u0437 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438",dataIndex:"unverifiedSuppliers",key:"unverifiedSuppliers",width:"12%",align:"right",render:function(e,t){return t.label&&(null!==e&&void 0!==e?e:ae)}},{title:"\u041d\u0435\u043d\u0430\u0434\u0435\u0436\u043d\u044b\u0445 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",dataIndex:"unreliableSupplier",key:"unreliableSupplier",width:"12%",align:"right",render:function(e,t){return t.label&&(null!==e&&void 0!==e?e:ae)}}];var ne=function(){var e=_(v),t=_(x),c=_(m),l=Object(a.useState)([]),n=Object(b.a)(l,2),i=n[0],s=n[1],o=Object(a.useState)(""),d=Object(b.a)(o,2),O=d[0],p=d[1],h=Object(a.useState)(""),f=Object(b.a)(h,2),w=f[0],I=f[1],L=Object(a.useState)([]),A=Object(b.a)(L,2),z=A[0],M=A[1],R=Object(a.useState)([]),P=Object(b.a)(R,2),T=P[0],D=P[1],U=Object(a.useState)(!1),q=Object(b.a)(U,2),G=q[0],K=q[1],B=Object(a.useState)(!1),V=Object(b.a)(B,2),J=V[0],Q=V[1],W=Object(a.useState)(!1),Z=Object(b.a)(W,2),X=Z[0],Y=Z[1],$=Object(a.useState)([]),ee=Object(b.a)($,2),te=ee[0],ae=ee[1],ne=Object(a.useState)([]),ie=Object(b.a)(ne,2),se=ie[0],re=ie[1],oe=Object(a.useCallback)((function(e){if(!e||!e.categories)return M([]),void s([]);var t=e.categories,c=t.reduce((function(e,t){var c=t.items.map((function(e){return Object(j.a)(Object(j.a)({},e),{},{key:e.id,category:t.title})})),a={key:"".concat(t.id,"-category"),label:"",category:t.title,children:c};return e.push(a),e}),[]);s(t),M(c),de(c)}),[M,s]);Object(a.useEffect)((function(){e.fetch().then(oe)}),[]);var de=function(e){try{var t=e.reduce((function(e,t){var c=t.children;return[].concat(Object(u.a)(e),Object(u.a)(c.map((function(e){return e.id}))))}),[]);if(0===t.length)return;var c=0,a=setInterval((function(){var e=t[c++];void 0!==e?m({id:e}).then((function(t){var c=t.data.reduce((function(e,t){return"ACTIVE"===t.status?Object(j.a)(Object(j.a)({},e),{},{activeSuppliers:(e.activeSuppliers||0)+1}):"ACTIVE"!==t.status?Object(j.a)(Object(j.a)({},e),{},{unreliableSupplier:(e.unreliableSupplier||0)+1}):void 0}),{activeSuppliers:null,reliableSuppliers:null,unverifiedSuppliers:0,unreliableSupplier:null});null===c.reliableSuppliers&&null!==c.activeSuppliers&&null!==c.unreliableSupplier&&(c.reliableSuppliers=c.activeSuppliers-c.unreliableSupplier),M((function(t){return t.reduce((function(t,a){var l=a.children.reduce((function(t,a){return a.id===e?[].concat(Object(u.a)(t),[Object(j.a)(Object(j.a)({},a),c)]):[].concat(Object(u.a)(t),[a])}),[]);return[].concat(Object(u.a)(t),[Object(j.a)(Object(j.a)({},a),{},{children:l})])}),[])}))})):clearInterval(a)}),500)}catch(l){console.log("some error"),console.log(l)}},ue=Object(a.useCallback)((function(e){K(!0),c.fetch({id:e}).then((function(e){D(e)}))}),[D,c]),je=Object(a.useCallback)((function(){K(!1)}),[K]),be=Object(a.useCallback)((function(e){e&&t.fetch({search:e}).then((function(e){oe(e)}))}),[t,oe]),Oe=Object(a.useCallback)((function(e){p(e||"")}),[p]),pe=Object(a.useCallback)((function(){Q(!0)}),[Q]),he=Object(a.useCallback)((function(){Q(!1)}),[Q]),ve=Object(a.useMemo)((function(){return O?[z.find((function(e){return e.children.find((function(e){return e.label===O}))}))]:z}),[O,z]),xe=Object(a.useCallback)((function(e){I(e),pe()}),[I,pe]),me=Object(a.useCallback)((function(e){ae(e)}),[ae]),fe=Object(a.useCallback)((function(){!function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"",c=document.createElement("a");c.setAttribute("href","data:text/plain;charset=utf-8,"+encodeURIComponent(t)),c.setAttribute("download",e),c.style.display="none",document.body.appendChild(c),c.click(),document.body.removeChild(c)}("data.xlsx")}),[]),_e=Object(a.useCallback)((function(){Y(!0)}),[Y]),ge=Object(a.useCallback)((function(){Y(!1)}),[Y]),Ce=Object(a.useCallback)((function(){return Object(r.jsxs)(g.b,{children:[Object(r.jsx)("div",{children:"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0430\u043c"}),Object(r.jsx)(C.a,{size:"middle",type:"primary",icon:Object(r.jsx)(S.a,{}),onClick:fe,children:"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c"})]})}),[fe]),Ne=Object(a.useCallback)((function(e,t){var c=t.key,a=e?[].concat(Object(u.a)(se),[c]):se.filter((function(e){return e!==c}));re(a)}),[re,se]);return Object(a.useEffect)((function(){re(ve.map((function(e){return e.key})))}),[ve]),Object(r.jsxs)("div",{className:"dashboard",children:[Object(r.jsxs)("div",{className:"dashboard__form-wrapper",children:[Object(r.jsx)(E,{onAdd:xe,onSelect:Oe,options:i,loading:t.isLoading}),Object(r.jsx)(C.a,{className:"dashboard__settings-button",type:"primary",icon:Object(r.jsx)(y.a,{}),onClick:pe,children:"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438"}),Object(r.jsx)(C.a,{className:"dashboard__settings-button",type:"primary",icon:Object(r.jsx)(k.a,{}),onClick:_e,children:"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430"})]}),Object(r.jsx)(H,{visible:J,onClose:he,onSubmit:be,search:w}),Object(r.jsx)(ce,{visible:X,onCLose:ge}),Object(r.jsx)(N.a,{columns:le,dataSource:ve,pagination:!1,scroll:{y:"75vh"},bordered:!0,size:"small",loading:e.isLoading||t.isLoading,rowClassName:function(e){return e.label?"":"dashboard__row--category"},onRow:function(e,t){return{onClick:function(){e.label&&ue(e.id)}}},expandable:{expandRowByClick:!0,expandedRowKeys:se,rowExpandable:function(e){return!e.label},onExpand:Ne},rowSelection:{selectedRowKeys:te,onChange:me,checkStrictly:!1},footer:te.length?Ce:void 0,className:"dashboard__table"}),Object(r.jsx)(F,{visible:G,onClose:je,suppliers:T,loading:c.isLoading})]})},ie=function(){return Object(r.jsx)(s.d,{children:Object(r.jsx)(s.b,{path:"/",element:Object(r.jsx)(d,{}),children:Object(r.jsx)(s.b,{index:!0,element:Object(r.jsx)(ne,{})})})})},se=c(109),re=c(18),oe=c(184),de=c.n(oe);c(304);i.a.render(Object(r.jsx)(l.a.StrictMode,{children:Object(r.jsx)(se.a,{children:Object(r.jsx)(re.a,{locale:de.a,children:Object(r.jsx)(ie,{})})})}),document.getElementById("root"))}},[[309,1,2]]]);
//# sourceMappingURL=main.c66c05e3.chunk.js.map