graphsInPage = []

// Bar chart made with plotly
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
      height: containerHeight,
      font: {size: 16}
    };

    Plotly.newPlot(elementName, data, layout);

    graphsInPage.push(elementName)
}

// Pie chart made with plotly
function pie_chart(elementName, pieValues, pieLabels, pieTitle){
  var containerWidth = $("#"+elementName).width();
  var containerHeight = $("#"+elementName).height();

  var data = [{
    values: pieValues[0].x,
    labels: pieLabels,
    type: 'pie'
  }];

  var layout = {
    font: {size: 16},
    title: pieTitle,
    width: containerWidth,  
    height: containerHeight
  };
  
  Plotly.newPlot(elementName, data, layout);
  graphsInPage.push(elementName)
}

// Table chart made with plotly
function plotly_table(elementName, tableValues, tableHeaders, tableTitle){
  var containerWidth = $("#"+elementName).width();
  var containerHeight = $("#"+elementName).height();

  var data = [{
    type: 'table',
    header: {
      values: tableHeaders,
      align: "center",
      line: {width: 1, color: 'black'},
      fill: {color: "grey"},
      font: {family: "Arial", size: 20, color: "white"}
    },
    cells: {
      values: tableValues,
      align: "center",
      line: {color: "black", width: 1},
      font: {family: "Arial", size: 16, color: ["black"]}
    }
  }]

  var layout = {
    title: tableTitle,
    width: containerWidth,  
    height: containerHeight
  }

  Plotly.plot(elementName, data, layout);
  graphsInPage.push(elementName)
}

// Bubble chart made with plotly
function bubble_chart(elementName, xValues, yValues, bubblesText, colors, bubblesSize, chartTitle){
  var containerWidth = $("#"+elementName).width();
  var containerHeight = $("#"+elementName).height();

  var trace1 = {
    x: xValues,
    y: yValues,
    text: bubblesText,
    mode: 'markers',
    marker: {
      color: colors,
      size: bubblesSize
    }
  };
  
  var data = [trace1];
  
  var layout = {
    title: chartTitle,
    height: containerHeight,
    width: containerWidth,
    font: {size: 16}
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