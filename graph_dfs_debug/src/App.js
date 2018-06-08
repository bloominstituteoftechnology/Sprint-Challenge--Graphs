import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// Define the size of the random graph
const xCount = 4;
const yCount = 3;
const boxSize = 150;
const probability = 0.6;

// Figure out the canvas size
// I'm not sure what the reasoning is for tying the canvas width and height to the box size,
// but the graph is getting cut off because the canvas isn't big enough, so I made it bigger and now it's
// not getting cut off
const canvasWidth = boxSize * xCount + 500;
const canvasHeight = boxSize * yCount + 200;
const radius = boxSize / 8;

/**
 * GraphView
 */
class GraphView extends Component {
  /**
   * On mount
   */
  componentDidMount() {
    this.updateCanvasConnectedComponents();
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    this.updateCanvasConnectedComponents();
  }

  /**
   * Draw the given verts
   */
  drawVerts(vertexes, color='blue', clear=true) {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    if (clear) {
      ctx.fillStyle = 'white';
      ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    }

    // Draw the edges
    ctx.lineWidth = 2;
    ctx.strokeStyle = color;

    for (let v of vertexes) { // From this vert
      for (let e of v.edges) { // To all these verts
        const v2 = e.destination;
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(v2.pos.x, v2.pos.y);
        ctx.stroke();
      }
    }

    // Draw the verts on top
    //the color was hardcoded in instead of using the randomly generated color
    ctx.fillStyle = color; 

    for (let v of vertexes) {
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
      ctx.stroke();
      ctx.fill();
    }

    // Draw the vert names
    ctx.font = '10px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillStyle = 'white';

    for (let v of vertexes) {
      ctx.fillText(v.value, v.pos.x, v.pos.y + 4);
    }
  }
  
  /**
   * Draw the entire graph
   */
  updateCanvasEntireGraph() {
    const g = this.props.graph;
    this.drawVerts(g.vertexes);
    //g.dump();
  }

  /**
   * Draw the connected components
   */
  updateCanvasConnectedComponents() {
    function randomHexColor() {
      let color = ((Math.random() * 240)|0).toString(16);

      if (color.length === 1) {
        color = '0' + color; // leading zero for values less than 0x10
      }

      return color;
    }

    const g = this.props.graph;
    const connectedComponents = g.getConnectedComponents();

    let clear = true;

    for (let component of connectedComponents) {
      // Color just like in CSS
      const curColor = '#' + randomHexColor() + randomHexColor() + randomHexColor();

      this.drawVerts(component, curColor, clear);
      clear = false;
    }
  }

  /**
   * Render
   */
  render() {
    return <canvas ref="canvas" width={canvasHeight} height={canvasHeight}></canvas>;
  }
}


/**
 * App
 */
class App extends Component {
  constructor(props) {
    super(props);
    this.onButton = this.onButton.bind(this);

    this.state = {
      graph: new Graph()
    };

    this.state.graph.randomize(xCount, yCount, boxSize, probability);
  }

  /**
   * Handle the button press
   */
  onButton() {
    const state = {
      graph: new Graph()
    };
    state.graph.randomize(xCount, yCount, boxSize, probability);
    console.log(state);
    this.setState(state);
  }

  render() {
    return (
      <div className="App">
        {/*the onclick wasn't calling the correct function*/}
        <button onClick={()=>this.onButton()}>Random</button>
        <GraphView graph={this.state.graph}></GraphView>
      </div>
    );
  }
}

export default App;
