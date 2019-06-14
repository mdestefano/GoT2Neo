$(document).ready(function () {
    var query_title = $("#query_title").attr("data-query_title");
    try {
        if (query_title === "getDeathCountPerKillCategory") {
            getDeathCountPerKillCategory();
        }
        if (query_title === "getKillCountPerCharacter") {
            getKillCountPerCharacter();
        }
        if (query_title === "getMurdersByCharacter") {
            getMurdersByCharacter();
        }
        if (query_title === "getSuicides") {
            getSuicides();
        }
    } catch (e) {
        alert(e);
    }
});

function getDeathCountPerKillCategory() {
    var dataElement = $("#data");
    var dataJson = dataElement.attr("data-json");
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

function getMurdersByCharacter() {
    var dataElement = $("#data");
    var dataJson = dataElement.attr("data-json");
    var dataObj = JSON.parse(dataJson);
    for (var i in dataObj) {
        var dead = dataObj[i].dead;
        var killings = dataObj[i].killings;
        var count = dataObj[i].count;
        var when;
        if (count === 1) {
            when = killings[0].season + "x" + killings[0].episode;
        } else {
            when = "Variuous occasions"
        }
        var htmlContent = "<div class=\"row mb-5\">\n" +
            "                <div class=\"col-sm-12 col-md-9 col-lg-9 col-xl-9\">\n" +
            "                    <table class=\"table\">\n" +
            "                        <tr>\n" +
            "                            <td scope=\"row\">Name</td>\n" +
            "                            <td>" + dead.name + "<td>\n" +
            "                        </tr>\n" +
            "                        <tr>\n" +
            "                            <td scope=\"row\">Nickname</td>\n" +
            "                            <td>" + dead.nickname + "</td>\n" +
            "                        </tr>\n" +
            "                        <tr>\n" +
            "                            <td scope=\"row\">Actor name</td>\n" +
            "                            <td>" + dead.actor + "</td>\n" +
            "                        </tr>\n" +
            "                        <tr>\n" +
            "                            <td scope=\"row\">Times</td>\n" +
            "                            <td>" + count + "</td>\n" +
            "                        </tr>\n" +
            "                        <tr>\n" +
            "                            <td scope=\"row\">When</td>\n" +
            "                            <td>" + when + "</td>\n" +
            "                        </tr>\n" +
            "                    </table>\n" +
            "                </div>\n" +
            "                <div class=\"col\">\n" +
            "                    <img src=\"" + dead.imageFull + "\" alt='N/A'/>\n" +
            "                </div>\n" +
            "            </div>";
        dataElement.append(htmlContent);
    }
}

function getSuicides() {
    var dataElement = $("#data");
    var dataJson = dataElement.attr("data-json");
    var dataObj = JSON.parse(dataJson);
    dataElement.append("<div class=\"container\">");
    for (var i in dataObj) {
        var character = dataObj[i].character;
        var name = character.name;
        var nickname = character.nickname;
        var actor = character.actor;
        var imageFull = character.imageFull;
        var htmlContent = "<div class=\"row mb-5\">\n" +
            "                <div class=\"col-sm-12 col-md-9 col-lg-9 col-xl-9\">\n" +
            "                    <table class=\"table\">\n" +
            "                        <tr>\n" +
            "                            <td scope=\"row\">Name</td>\n" +
            "                            <td>" + name + "<td>\n" +
            "                        </tr>\n" +
            "                        <tr>\n" +
            "                            <td scope=\"row\">Nickname</td>\n" +
            "                            <td>" + nickname + "</td>\n" +
            "                        </tr>\n" +
            "                        <tr>\n" +
            "                            <td scope=\"row\">Actor name</td>\n" +
            "                            <td>" + actor + "</td>\n" +
            "                        </tr>\n" +
            "                    </table>\n" +
            "                </div>\n" +
            "                <div class=\"col\">\n" +
            "                    <img src=\"" + imageFull + "\"/>\n" +
            "                </div>\n" +
            "            </div>";
        dataElement.append(htmlContent);
    }
    dataElement.append("</div>");
    /*
    <div class="row">
        <div class="col-sm-12 col-md-9 col-lg-9 col-xl-9">
            <table class="table">
                <tr>
                    <td scope="row">Name</td>
                    <td><td>
                </tr>
                <tr>
                    <td scope="row">Nickname</td>
                    <td></td>
                </tr>
                <tr>
                    <td scope="row">Actor name</td>
                    <td></td>
                </tr>
            </table>
        </div>
        <div class="col">
            <img src="" />
        </div>
    </div>
    */
}