d3.json("data/academic_words_mapping.json").then(function(graph) {
    // Create a new directed graph
    var g = new dagreD3.graphlib.Graph().setGraph({});

    // Add nodes to the graph
    graph.nodes.forEach(function(node) {
        g.setNode(node.id, { label: node.id });
    });

    // Add edges to the graph
    graph.links.forEach(function(link) {
        g.setEdge(link.source, link.target);
    });

    // Create a new D3 renderer
    var render = new dagreD3.render();

    // Create an SVG element
    var svg = d3.select("body").append("svg"),
        svgGroup = svg.append("g");

    // Run the renderer
    render(svgGroup, g);

    // Center the graph
    var xCenterOffset = (svg.attr("width") - g.graph().width) / 2;
    svgGroup.attr("transform", "translate(" + xCenterOffset + ", 20)");
    svg.attr("height", g.graph().height + 40);
});
