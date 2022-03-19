(this["webpackJsonptezos-flame-defi"]=this["webpackJsonptezos-flame-defi"]||[]).push([[0],{172:function(e,t,a){},174:function(e,t,a){},192:function(e,t,a){},193:function(e,t,a){},263:function(e,t,a){},264:function(e,t,a){},270:function(e,t,a){},275:function(e,t,a){"use strict";a.r(t);var c=a(0),n=a.n(c),s=a(39),i=a.n(s),l=a(24),r=(a(172),a(10)),o=function(){return Object(r.jsxs)("div",{className:"header",children:[Object(r.jsx)("div",{className:"header__logo"}),Object(r.jsx)("div",{className:"header__label",children:"\u041f\u043e\u0438\u0441\u043a \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432"})]})},b=(a(174),function(){return Object(r.jsxs)("div",{className:"base-layout",children:[Object(r.jsx)(o,{}),Object(r.jsx)("div",{className:"base-layout__main",children:Object(r.jsx)(l.a,{})})]})}),j=a(3),u=a(5),d=a(158),O=a.n(d).a.create({baseURL:"/api",timeout:6e5});var h={get:O.get,delete:O.delete,post:O.post,put:O.put,patch:O.patch,request:O.request};function m(){return h.get("/items")}function f(e){var t=e.search;return h.get("/item",{params:{search:t}})}function p(e){var t=e.id;return h.get("/suppliers",{params:{item:t}})}var x=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},a=arguments.length>2&&void 0!==arguments[2]&&arguments[2],n=Object(c.useState)(t),s=Object(u.a)(n,2),i=s[0],l=s[1],r=Object(c.useState)(!1),o=Object(u.a)(r,2),b=o[0],d=o[1],O=Object(c.useState)(),h=Object(u.a)(O,2),m=h[0],f=h[1],p=Object(c.useState)(!1),x=Object(u.a)(p,2),v=x[0],g=x[1],y=Object(c.useState)(!1),C=Object(u.a)(y,2),S=C[0],_=C[1],k=Object(c.useState)(""),N=Object(u.a)(k,2),w=N[0],I=N[1],E=Object(c.useState)(0),z=Object(u.a)(E,2),L=z[0],M=z[1],A=function(){return M((function(e){return e+1}))},P=Object(c.useCallback)((function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};return d(!0),e(Object(j.a)(Object(j.a)({},i),t)).then((function(e){return 200===e.status?f(e.data):(g(!0),I(e.data)),e.data})).catch((function(e){g(!0),I(null===e||void 0===e?void 0:e.message)})).finally((function(){d(!1),_(!0)}))}),[d,e,i,f,g,I]);return Object(c.useEffect)((function(){a&&P()}),[P,a,L]),{fetch:P,data:m,isLoading:b,isDone:S,hasError:v,errorMessage:w,updateParams:l,refetch:A}},v=a(40),g=a(277),y=a(287),C=(a(192),a(6)),S=a(276),_=a(285),k=(a(193),function(e){var t=e.onAdd,a=e.onSelect,n=e.options,s=e.loading,i=void 0!==s&&s,l=Object(c.useState)([]),o=Object(u.a)(l,2),b=o[0],d=o[1],O=Object(c.useState)(""),h=Object(u.a)(O,2),m=h[0],f=h[1];Object(c.useEffect)((function(){var e=n.reduce((function(e,t){var a,c=t.items.map((function(e){e.id;var t,a,c=e.label,n=e.activeSuppliers;return Object(j.a)({},(a=n,{value:t=c,label:Object(r.jsxs)("div",{style:{display:"flex",justifyContent:"space-between"},children:[t,a&&Object(r.jsxs)("span",{children:["\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432 ",a]})]})}))})),n={value:t.title,title:t.title,label:(a=t.title,Object(r.jsx)("span",{children:a})),options:c};return[].concat(Object(C.a)(e),[n])}),[]);d(e)}),[n,d]);var p=Object(c.useCallback)((function(e){a(e)}),[a]),x=Object(c.useCallback)((function(e){f(e)}),[f]),g=Object(c.useCallback)((function(){t(m)}),[t,m]),y=Object(c.useMemo)((function(){return Object(r.jsxs)("div",{className:"add-item-form__empty",children:[Object(r.jsx)("span",{className:"add-item-form__empty-text",children:"\u041d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u043e"}),Object(r.jsx)(v.a,{icon:Object(r.jsx)(_.a,{}),onClick:g,className:"add-item-form__button",loading:i,children:"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0443"})]})}),[g,i]);return Object(r.jsx)("div",{className:"add-item-form",children:Object(r.jsx)(S.a,{className:"add-item-form__search",dropdownClassName:"add-item-form__search-dropdown",options:b,onSelect:p,onSearch:x,filterOption:function(e,t){return t.value.toLowerCase().includes(e.toLowerCase())},notFoundContent:y,placeholder:"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e \u043d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u044b",allowClear:!0})})}),N=a(283),w=(a(263),Object(c.memo)((function(e){var t=e.onClose,a=e.visible,c=e.suppliers;return Object(r.jsx)(N.a,{title:"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0438",placement:"right",onClose:t,visible:a,children:Object(r.jsx)("p",{children:JSON.stringify(c)})})}))),I=a(282),E=a(279),z=a(163),L=a(280),M=a(87),A=a(281),P=a(284),q=a(278),F=a(286),R=(a(264),I.a.Panel),J=Object(c.memo)((function(e){var t=e.search,a=e.visible,n=e.onClose,s=e.onSubmit,i=Object(c.useState)(t),l=Object(u.a)(i,2),o=l[0],b=l[1];Object(c.useEffect)((function(){b(t)}),[t,b]);var j=function(){n&&n()},d=Object(c.useMemo)((function(){return Object(r.jsxs)(r.Fragment,{children:[Object(r.jsx)(E.a.Item,{label:"\u0410\u0434\u0440\u0435\u0441 \u043e\u0431\u044a\u0435\u043a\u0442\u0430",tooltip:"\u0418\u0441\u043a\u0430\u0442\u044c \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432 \u0434\u043b\u044f \u043e\u0431\u044a\u0435\u043a\u0442\u0430 \u043f\u043e \u0430\u0434\u0440\u0435\u0441\u0443",wrapperCol:{span:10},children:Object(r.jsx)(z.a,{})}),Object(r.jsx)(E.a.Item,{label:"\u041c\u0438\u043d. \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",tooltip:"\u0412\u043b\u0438\u044f\u0435\u0442 \u043d\u0430 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043f\u043e\u0438\u0441\u043a\u0430",labelCol:{span:17},children:Object(r.jsx)(L.a,{min:0})}),Object(r.jsx)(E.a.Item,{label:"\u041c\u0438\u043d. \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \xab\u043d\u0430\u0434\u0451\u0436\u043d\u044b\u0445\xbb \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",tooltip:"\u0412\u043b\u0438\u044f\u0435\u0442 \u043d\u0430 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043f\u043e\u0438\u0441\u043a\u0430",labelCol:{span:17},children:Object(r.jsx)(L.a,{min:0})}),Object(r.jsx)(E.a.Item,{valuePropName:"checked",children:Object(r.jsx)(M.a,{children:"\u0418\u0441\u043a\u0430\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0445 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432"})}),Object(r.jsx)(E.a.Item,{valuePropName:"checked",className:"settings__checkbox",children:Object(r.jsx)(M.a,{children:"\u0418\u0441\u043a\u0430\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439"})})]})}),[]),O=Object(c.useMemo)((function(){return Object(r.jsxs)(r.Fragment,{children:[Object(r.jsx)(E.a.Item,{label:"\u0423\u0441\u0442\u0430\u0432\u043d\u043e\u0439 \u043a\u0430\u043f\u0438\u0442\u0430\u043b, \u043d\u0435 \u043c\u0435\u043d\u0435\u0435",labelCol:{span:12},children:Object(r.jsx)(L.a,{min:0})}),Object(r.jsx)(E.a.Item,{label:"\u041b\u0435\u0442 \u0440\u0430\u0431\u043e\u0442\u044b, \u043d\u0435 \u043c\u0435\u043d\u0435\u0435",labelCol:{span:12},children:Object(r.jsx)(L.a,{min:0})})]})}),[]);return Object(r.jsx)(A.a,{title:"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0438\u0441\u043a\u0430 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",visible:a,onCancel:j,footer:null,children:Object(r.jsxs)(E.a,{onFinish:function(){o&&(s&&s(o),j())},layout:"horizontal",labelWrap:!0,size:"small",labelAlign:"left",requiredMark:!1,children:[Object(r.jsx)(E.a.Item,{label:"\u041d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0430",name:"search",required:!0,children:Object(r.jsxs)(P.b,{direction:"vertical",style:{width:"100%"},children:[Object(r.jsx)(z.a,{placeholder:"\u041d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0430 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430",name:"search",value:o,onInput:function(e){return b(e.target.value)}}),Object(r.jsxs)(q.a,{accept:".xsl,.xlsx,.csv",children:["\u0438\u043b\u0438 ",Object(r.jsx)(v.a,{icon:Object(r.jsx)(F.a,{}),children:"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 xls, csv"})]})]})}),Object(r.jsxs)(I.a,{ghost:!0,className:"settings",expandIconPosition:"left",defaultActiveKey:["1","2"],children:[Object(r.jsx)(R,{header:"\u041c\u043e\u0434\u0443\u043b\u044c \u043f\u043e\u0438\u0441\u043a\u0430",children:d},"1"),Object(r.jsx)(R,{header:"\u041c\u043e\u0434\u0443\u043b\u044c \u0441\u043a\u043e\u0440\u0438\u043d\u0433\u0430 \xab\u043d\u0430\u0434\u0451\u0436\u043d\u043e\u0433\u043e\xbb \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0430",children:O},"2")]}),Object(r.jsx)(E.a.Item,{noStyle:!0,children:Object(r.jsxs)(P.b,{className:"settings__footer",children:[Object(r.jsx)(v.a,{size:"middle",onClick:function(){n&&n()},type:"ghost",htmlType:"reset",children:"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c"}),Object(r.jsx)(v.a,{size:"middle",type:"primary",htmlType:"submit",children:"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c"})]})})]})})})),B=[{title:"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f",dataIndex:"category",key:"category",width:"18%",className:"dashboard__column--bold"},{title:"\u041d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0430",dataIndex:"label",key:"label",className:"dashboard__column--bold"},{title:"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",dataIndex:"activeSuppliers",key:"activeSuppliers",width:"12%",align:"right",className:"dashboard__column--bold"},{title:"\u041d\u0430\u0434\u0435\u0436\u043d\u044b\u0445 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",dataIndex:"reliableSuppliers",key:"reliableSuppliers",width:"12%",align:"right",className:"dashboard__column--bold"},{title:"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432 \u0431\u0435\u0437 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438",dataIndex:"unverifiedSuppliers",key:"unverifiedSuppliers",width:"12%",align:"right"},{title:"\u041d\u0435\u043d\u0430\u0434\u0435\u0436\u043d\u044b\u0445 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432",dataIndex:"unreliableSupplier",key:"unreliableSupplier",width:"12%",align:"right"}],T=function(){var e=x(m),t=x(f),a=x(p),n=Object(c.useState)([]),s=Object(u.a)(n,2),i=s[0],l=s[1],o=Object(c.useState)(""),b=Object(u.a)(o,2),d=b[0],O=b[1],h=Object(c.useState)(""),C=Object(u.a)(h,2),S=C[0],_=C[1],N=Object(c.useState)([]),I=Object(u.a)(N,2),E=I[0],z=I[1],L=Object(c.useState)([]),M=Object(u.a)(L,2),A=M[0],P=M[1],q=Object(c.useState)(!1),F=Object(u.a)(q,2),R=F[0],T=F[1],D=Object(c.useState)(!1),K=Object(u.a)(D,2),U=K[0],W=K[1],G=Object(c.useCallback)((function(e){if(!e||!e.categories)return z([]),void l([]);var t=e.categories,a=t.reduce((function(e,t){var a=t.items.map((function(e){return Object(j.a)(Object(j.a)({},e),{},{key:e.id,category:t.title})})),c={key:"".concat(t.id,"-category"),label:"",category:t.title,children:a};return e.push(c),e}),[]);l(t),z(a)}),[z,l]);Object(c.useEffect)((function(){e.fetch().then(G)}),[]);var H=Object(c.useCallback)((function(e){T(!0),a.fetch({id:e}).then((function(e){P(e)}))}),[P,a]),Q=Object(c.useCallback)((function(){T(!1)}),[T]),V=Object(c.useCallback)((function(e){e&&t.fetch({search:e}).then((function(e){G(e)}))}),[t,G]),X=Object(c.useCallback)((function(e){O(e||"")}),[O]),Y=Object(c.useCallback)((function(){W(!0)}),[W]),Z=Object(c.useCallback)((function(){W(!1)}),[W]),$=Object(c.useMemo)((function(){return d?[E.find((function(e){return e.children.find((function(e){return e.label===d}))}))]:E}),[d,E]),ee=Object(c.useCallback)((function(e){_(e),Y()}),[_,Y]);return Object(r.jsxs)("div",{className:"dashboard",children:[Object(r.jsxs)("div",{className:"dashboard__form-wrapper",children:[Object(r.jsx)(k,{onAdd:ee,onSelect:X,options:i,loading:t.isLoading}),Object(r.jsx)(v.a,{className:"dashboard__settings-button",type:"primary",icon:Object(r.jsx)(y.a,{}),onClick:Y})]}),Object(r.jsx)(J,{visible:U,onClose:Z,onSubmit:V,search:S}),Object(r.jsx)(g.a,{columns:B,dataSource:$,pagination:{position:[]},scroll:{y:700},bordered:!0,size:"small",loading:e.isLoading||t.isLoading,rowClassName:function(e){return e.label?"":"dashboard__row--category"},onRow:function(e,t){return{onClick:function(){e.label&&H(e.id)}}},expandable:{defaultExpandAllRows:!0,showExpandColumn:!0,expandRowByClick:!0,rowExpandable:function(e){return!e.label}},className:"dashboard__table"}),Object(r.jsx)(w,{visible:R,onClose:Q,suppliers:A})]})},D=function(){return Object(r.jsx)(l.d,{children:Object(r.jsx)(l.b,{path:"/",element:Object(r.jsx)(b,{}),children:Object(r.jsx)(l.b,{index:!0,element:Object(r.jsx)(T,{})})})})},K=a(102),U=a(20),W=a(162),G=a.n(W);a(270);i.a.render(Object(r.jsx)(n.a.StrictMode,{children:Object(r.jsx)(K.a,{children:Object(r.jsx)(U.a,{locale:G.a,children:Object(r.jsx)(D,{})})})}),document.getElementById("root"))}},[[275,1,2]]]);
//# sourceMappingURL=main.6e967452.chunk.js.map