import React, { Component } from 'react';
import { Graph } from './graph';
import { NewGraph } from './utils';
import { colors } from './colors';
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
      //ctx.fillStyle = 'white';
      ctx.fillStyle = color.hex;
      ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    }

    // Draw the edges
    ctx.lineWidth = 2;
    ctx.strokeStyle = color.hex;

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
    //ctx.fillStyle = '#77f';
    ctx.fillStyle = color.hex;

    for (let v of vertexes) {
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
      ctx.stroke();
      ctx.fill();
    }

    // Draw the vert names
    ctx.font = '10px sans-serif';
    ctx.textAlign = 'center';
    //ctx.fillStyle = 'white';
    let compColor = color.complimentary[0];

    if (color.complimentary.includes('White')) {
      const index = color.complimentary.indexOf('White');
      compColor = color.complimentary[index];
    } else if (color.complimentary.includes('Black')) {
      const index = color.complimentary.indexOf('Black');
      compColor = color.complimentary[index];
    }
    ctx.fillStyle = compColor;

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
    // I will re-write this
    /*
    function randomHexColor() {
      let color = ((Math.random() * 240) | 0).toString(16);

      if (color.length === 1) {
        color = '0' + color; // leading zero for values less than 0x10
      }

      return color;
    }
    */

    const g = this.props.graph;
    const connectedComponents = g.getConnectedComponents();

    let clear = true;

    for (let component of connectedComponents) {
      // Color just like in CSS
      //const curColor = '#' + randomHexColor() + randomHexColor() + randomHexColor();
      // my way of randomizing color
      const curColor = colors[Math.floor(Math.random() * colors.length)];
      this.drawVerts(component, curColor, clear);
      clear = false;
    }
  }

  /**
   * Render
   */
  render() {
    return <canvas ref="canvas" width={canvasHeight} height={canvasHeight} />;
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
        <GraphView graph={this.state.graph} />
        <NewGraph onClick={this.onButton}>Random</NewGraph>
      </div>
    );
  }
}

export default App;
