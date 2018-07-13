import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

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

  // Missing from Assignment

  //   ctx.font = "13px Arial";
  //   ctx.textAlign = "center";
  //   ctx.textBaseline = "middle";

  //   // set of all connected components
  //   const components = this.props.graph.getConnectedComponents();
  //   // loop pass each to drawV
  //   components.forEach((component) => {
  //     this.drawVertexes(ctx, component, this.generateRandomColor());
  //   });
  // }
  updateCanvas() {
    let canvas = this.refs.canvas;
    const ctx = canvas.getContext("2d");
  
    ctx.fillStyle = "grey";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = "10px sans-serif";
    ctx.textAlign = "center";
    ctx.fillStyle = "white";
  }

  /**
   * Draw the given verts
   */
  // defualt
  drawVerts(ctx, vertexes, color) {
    // Draw the edges
    ctx.lineWidth = 2;
    ctx.strokeStyle = color;

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
    for (let v of vertexes) {
      ctx.beginPath();
      ctx.fillStyle = color;
      ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    }
  }

  color() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
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
      let color = ((Math.random() * 240) | 0).toString(16);

      if (color.length === 1) {
        color = "0" + color; // leading zero for values less than 0x10
      }

      return color;
    }

    const g = this.props.graph;
    const connectedComponents = g.getConnectedComponents();

    let clear = true;

    for (let component of connectedComponents) {
      // Color just like in CSS
      const curColor =
        "#" + randomHexColor() + randomHexColor() + randomHexColor();

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
