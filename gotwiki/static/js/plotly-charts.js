
function bar_chart(elementName, data, title, xTitle, yTitle){
    var layout = {
        title: title,
        xaxis: {
          title: xTitle,
          showgrid: false,
          zeroline: false
        },
        yaxis: {
          title: yTitle,
          showline: false
        }
      };
  
      Plotly.plot(elementName, data, layout);
  }
  
  function pie_chart(elementName, pieValues, pieLabels, pieTitle){
  
    pageWidth = window.innerWidth || document.body.clientWidth
    pageHeight = window.innerHeight || document.body.clientHeight
  
    console.log(pieLabels)
    var data = [{
      values: pieValues[0].x,
      labels: pieLabels,
      type: 'pie'
    }];
  
    var layout = {
      font: {size: 18},
      title: pieTitle,
      height: pageHeight/1.8,
      width: pageWidth/1.3
    };
    
    Plotly.newPlot(elementName, data, layout);
  }