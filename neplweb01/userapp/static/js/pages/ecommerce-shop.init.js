function getChartColorsArray(r){r=$(r).attr("data-colors");return(r=JSON.parse(r)).map(function(r){r=r.replace(" ","");if(-1==r.indexOf("--"))return r;r=getComputedStyle(document.documentElement).getPropertyValue(r);return r||void 0})}var vectormapColors=getChartColorsArray("#sales-by-locations");$("#sales-by-locations").vectorMap({map:"world_mill_en",normalizeFunction:"polynomial",hoverOpacity:.7,hoverColor:!1,regionStyle:{initial:{fill:"#e9e9ef"}},markerStyle:{initial:{r:9,fill:vectormapColors,"fill-opacity":.9,stroke:"#fff","stroke-width":7,"stroke-opacity":.4},hover:{stroke:"#fff","fill-opacity":1,"stroke-width":1.5}},backgroundColor:"transparent",markers:[{latLng:[41.9,12.45],name:"USA"},{latLng:[12.05,-61.75],name:"Russia"},{latLng:[1.3,103.8],name:"Australia"}]});