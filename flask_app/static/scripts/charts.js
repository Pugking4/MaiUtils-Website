function drawPieChart(chartId, data, width, height) {
    var chartData = new google.visualization.DataTable();
    chartData.addColumn('string', 'Label');
    chartData.addColumn('number', 'Value');
    var rows = [];
    for (var label in data) {
        rows.push([label, data[label]]);
    }
    chartData.addRows(rows);
    
    var options = {
        'width': width,
        'height': height,
        'backgroundColor': 'transparent',
    };
    
    var chart = new google.visualization.PieChart(document.getElementById(chartId));
    chart.draw(chartData, options);
}
