import React, {
  Component
} from 'react';
import {
  Graph
} from './graph';
import './App.css';

// Define the size of the random graph
const xCount = 4;
const yCount = 3;
const boxSize = 150;
const probability = 0.6;
const radius = boxSize / 8;

//TODO: Figure out the canvas size

//The canvas size should be set to numbers not the random graph variables
const canvasWidth = 850;
const canvasHeight = 600;
// const radius = boxSize / 8; //This should be moved up with the global variables

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
  //TODO: Draw verts should have been drawn after edges?
  drawVerts(vertexes, color = 'blue', clear = true) {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    //TODO: Need to remove console.log


    // Clear it
    if (clear) {
      ctx.fillStyle = 'white';
      ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    }



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
    ctx.fillStyle = '#77f';

    for (let v of vertexes) {
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
      ctx.fill();
      ctx.stroke();

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
    return ( <
      canvas ref = "canvas"
      width = {
        canvasHeight
      }
      height = {
        canvasHeight
      } > {
        ' '
      } <
      /canvas>
    );
  }
}

/**
 * App
 */
class App extends Component {
  //TODO: Get button to be functional COMPLETED!
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
    //The GraphView and the Button need to be refactored
    return ( <
      div className = "App" >
      <
      GraphView graph = {
        this.state.graph
      }
      /> <
      button onClick = {
        this.onButton
      } > Random < /button>< /
      div >
    );

  }
}

export default App;