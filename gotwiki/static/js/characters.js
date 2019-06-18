$(document).ready(function () {
    var query_title = $("#query_title").attr("data-query_title");
    try {
        if (query_title === "getDeathCountPerKillCategory") {
            getDeathCountPerKillCategory();
        }
        if (query_title === "getKillCountPerCharacter") {
            getKillCountPerCharacter();
        }
    } catch (e) {
        alert(e);
    }
});

function getDeathCountPerKillCategory() {
    var dataElement = $("#data");
    var dataJson = dataElement.attr("data-data");
    var dataObj = JSON.parse(dataJson);
    // margins
    var margin = {top: 20, right: 30, bottom: 40, left: 90},
        width = 530 - margin.left - margin.right,
        height = 520 - margin.top - margin.bottom;

    // append the svg object to data div
    var svg = d3.select("#data")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    // Add X axis
    var x = d3.scaleLinear()
        .domain([0, dataObj[0].count])
        .range([0, width]);
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x))
        .selectAll("text")
        .attr("transform", "translate(-10,0)rotate(-45)")
        .style("text-anchor", "end");

    // Y axis
    var y = d3.scaleBand()
        .range([0, height])
        .domain(dataObj.map(function (d) {
            return d.methodCat;
        }))
        .padding(.1);
    svg.append("g")
        .call(d3.axisLeft(y));

    //Bars
    svg.selectAll("myRect")
        .data(dataObj)
        .enter()
        .append("rect")
        .attr("x", x(0))
        .attr("y", function (d) {
            return y(d.methodCat);
        })
        .attr("width", function (d) {
            return x(d.count);
        })
        .attr("height", y.bandwidth())
        .attr("fill", "#b33e0f")
}

function getKillCountPerCharacter() {

}