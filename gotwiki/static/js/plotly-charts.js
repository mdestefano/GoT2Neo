graphsInPage = []

function bar_chart(elementName, data, title, xTitle, yTitle){
  var containerWidth = $("#"+elementName).width();
  var containerHeight = $("#"+elementName).height();

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
      },
      width: containerWidth,  
      height: containerHeight 
    };

    Plotly.plot(elementName, data, layout);

    graphsInPage.push(elementName)
}

function pie_chart(elementName, pieValues, pieLabels, pieTitle){
  var containerWidth = $("#"+elementName).width();
  var containerHeight = $("#"+elementName).height();

  var data = [{
    values: pieValues[0].x,
    labels: pieLabels,
    type: 'pie'
  }];

  var layout = {
    font: {size: 18},
    title: pieTitle,
    width: containerWidth,  
    height: containerHeight
  };
  
  Plotly.newPlot(elementName, data, layout);
  graphsInPage.push(elementName)
}

window.onresize = function() {
  graphsInPage.forEach(function(elementName) {
    var containerWidth = $("#"+elementName).width();
    var containerHeight = $("#"+elementName).height();

    var update = {
      width: containerWidth,  
      height: containerHeight
    };
    Plotly.relayout(elementName, update);
  });
};