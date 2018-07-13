import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// Define the size of the random graph
const xCount = 5;
const yCount = 5;
const boxSize = 135;
const probability = 0.6;

// Figure out the canvas size
const canvasWidth = boxSize * xCount;
const canvasHeight = boxSize * yCount;
const radius = boxSize / 8;

/**
 * GraphView
 */
class GraphView extends Component {
  /**
   * On mount
   */
  componentDidMount() {
    this.updateCanvasEntireGraph();
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    this.updateCanvasEntireGraph();
  }

  /**
   * Draw the given verts
   */
  drawVerts(vertexes, color='black', clear=true) {
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
    ctx.fillStyle = 'black'; 

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
    function getRandomColor() {
      let letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }
    const connectedComponents = this.props.graph.getConnectedComponents();
    let clear = true;
    for (let component of connectedComponents) {
      const curColor = getRandomColor();
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

    this.state = {
      graph: new Graph()
    };

    this.state.graph.randomize(xCount, yCount, boxSize, probability);
  }

  refreshPage() {
    window.location.reload();
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <input type="button" value="Random" onClick={ this.refreshPage} />
      </div>
    );
  }
}

export default App;
