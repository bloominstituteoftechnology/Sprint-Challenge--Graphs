import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// Define the size of the random graph
const xCount = 4;
const yCount = 3;
const boxSize = 150;
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
  drawVerts(vertexes, color = 'blue', clear = true) {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // Clear it
    if (clear) {
      ctx.fillStyle = 'white';
      // 1. debug - set to visible color (e.g. pink) to see where canvas is cutting off
      // Observation - canvas didn't seem to draw the right dimensions
      // Search - cmd f 'width' to see if canvasWidth is implemented incorrectly in file
      ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    }

    ctx.lineWidth = 2;
    ctx.strokeStyle = color;
    console.log('color: ', color);
    // 3. debug - see what manually set color does (e.g. green)
    // Observation - all edges are same color, some are drawn before their vertexes and show up on top
    // It's odd that everything is working without errors, but only some edges are drawn incorrectly
    // Search - Problem may be in graph.js where vertex/edge relationship is built (dfs)

    // Draw the edges
    for (let v of vertexes) {
      // From this vert
      for (let e of v.edges) {
        // To all these verts
        const v2 = e.destination;
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(v2.pos.x, v2.pos.y);
        ctx.stroke();
      }
    }

    // Draw the verts on top
    ctx.fillStyle = color; // '#77f';
    // 6. debug - should be same color as edges
    // edge color is determined first, so set vertex fill to edge strokeStyle

    for (let v of vertexes) {
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
      ctx.stroke();
      ctx.strokeStyle = color; // '#77f';
      // 7. debug - must set strokeStyle again like above
      //
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
    // g.dump();
  }

  /**
   * Draw the connected components
   */
  updateCanvasConnectedComponents() {
    function randomHexColor() {
      let color = ((Math.random() * 240) | 0).toString(16);

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
      const curColor =
        '#' + randomHexColor() + randomHexColor() + randomHexColor();

      this.drawVerts(component, curColor, clear);
      clear = false;
    }
  }

  /**
   * Render
   */
  render() {
    // 2. debug -  canvasHeight was used where canvasWidth should be
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />;
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
      graph: new Graph(),
    };

    this.state.graph.randomize(xCount, yCount, boxSize, probability);
  }

  /**
   * Handle the button press
   */
  onButton() {
    const state = {
      graph: new Graph(),
    };

    state.graph.randomize(xCount, yCount, boxSize, probability);

    this.setState(state);
  }

  render() {
    return (
      <div className="App">
        <button onClick={this.Button}>Random</button>
        <GraphView graph={this.state.graph} />
      </div>
    );
  }
}

export default App;
