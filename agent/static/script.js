
function xToLeft(x, scale=5){
    return 5*x
}
function yToTop(y, scale=5){
    return 500-(5*y)
}
function rad2deg(rad){
    return -57.295779513 * rad
}
// initialize 
graph = new fabric.Canvas('graph');
var agent = new Image();
agent.src = "/static/agent.png";
var light = new Image();
light.src = "/static/light.png"
agentObj = new fabric.Image(
    agent,
    {
        originX: "center",
        originY: "center"
    })
lightObj = new fabric.Image(
light,
{
    originX: "center",
    originY: "center",
    
})
agentObj.selectable = false
lightObj.selectable = false
// lightObj.scaleToWidth(50)
// lightObj.scaleToHeight(50)
graph.add(agentObj)
graph.add(lightObj)
fabric.Image.fromURL("/static/grid.png", imgObj => {
    graph.setBackgroundImage(imgObj, graph.renderAll.bind(graph), {
        scaleX: graph.width / imgObj.width,
        scaleY: graph.height / imgObj.height
})})


function renderAgent(x,y,rad){
    agentObj.set({
        'left':xToLeft(x), 
        'top':yToTop(y), 
        'angle':rad2deg(rad)
    })
    graph.renderAll()   
}

function renderLight(x,y){
    lightObj.set({
        'left': xToLeft(x),
        'top': yToTop(y)
    })
    graph.renderAll()
}

var sleep = time => new Promise(resolve => setTimeout(resolve, time))
var poll = (promiseFn, time) => promiseFn().then(
             sleep(time).then(() => poll(promiseFn, time)))


function render(url){
    fetch(url)
        .then(a=>a.json())
        .then(state=>{
            renderAgent(state.agent.positionX, state.agent.positionY, state.agent.angle);
            renderLight(state.light.positionX, state.light.positionY);
            document.getElementById("sensor").innerText =state.sensor 
            // console.log(state)
        })
}
document.addEventListener("DOMContentLoaded", function(event) {
    simNumber = window.location.pathname
    url = `/simulations${simNumber}`
    poll(() => new Promise(() => render(url)), 20)
});
            