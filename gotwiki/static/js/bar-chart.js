
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
