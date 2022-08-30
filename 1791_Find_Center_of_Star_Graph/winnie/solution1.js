var findCenter = function (edges) {
    const graphMap = buildGraph(edges);
    return centerNeighborCount(graphMap)
};

const buildGraph = (edgesMap) => {
    const graphMap = {};

    for (let singleEdge of edgesMap) {
        const [a, b] = singleEdge;

        if (!(a in graphMap)) graphMap[a] = [];
        if (!(b in graphMap)) graphMap[b] = [];

        graphMap[a].push(b);
        graphMap[b].push(a);
    }

    return graphMap;
}

const centerNeighborCount = (graphMap) => {
    let center = 1;
    while (true) {
        if (graphMap[center].length > 1) return center
        center += 1
    }
}

console.log(findCenter(edges = [[1,2],[2,3],[4,2]]))