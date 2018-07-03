import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';


const xCount = 5;
const yCount = 4;
const boxSize = 150;
const probability = 0.6;


const canvasWidth = boxSize * xCount;
const canvasHeight = boxSize * yCount;
const radius = boxSize / 10;

/**
 * GraphView
 */
class GraphView extends Component {
  /**
   * On mount
   */
  componentDidMount() {
    this.updateCanvasConnectedComponents();
    console.log(this.props.graph.getConnectedComponents());
    console.log(this.props.graph.dump());
  }

  
  componentDidUpdate() {
    this.updateCanvasConnectedComponents();
  }

  
  drawVerts(vertexes, color = 'blue', clear = true) {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // Clear it
    if (clear) {
      ctx.fillStyle = 'green';
      ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    }

    
    ctx.lineWidth = 2;
    ctx.strokeStyle = color;

    for (let v of vertexes) {
      // From this vert
      for (let e of v.edges) {
        // To all these verts
        const v2 = e.destination;
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y);
        console.log(color);
        ctx.lineTo(v2.pos.x, v2.pos.y);
        ctx.stroke();
      }
    }

    
    ctx.fillStyle = '#78f';

    for (let v of vertexes) {
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();
    }

  
    ctx.font = '10px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillStyle = 'white';

    for (let v of vertexes) {
      ctx.fillText(v.value, v.pos.x, v.pos.y + 4);
    }
  }

  
  updateCanvasEntireGraph() {
    const g = this.props.graph;
    this.drawVerts(g.vertexes);
   
  }

  
  updateCanvasConnectedComponents() {
    function randomHexColor() {
      let color = ((Math.random() * 240) | 0).toString(16);

      if (color.length === 1) {
        color = '0' + color; 
      }

      return color;
    }

    const g = this.props.graph;
    const connectedComponents = g.getConnectedComponents();

    let clear = true;
    console.log(connectedComponents);
   

    for (let component of connectedComponents) {
     
      const curColor =
        '#' + randomHexColor() + randomHexColor() + randomHexColor();

      this.drawVerts(component, curColor, clear);
      clear = false;
    }
  }

 
  render() {
    
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />;
  }
}


class App extends Component {
  constructor(props) {
    super(props);
    this.onButton = this.onButton.bind(this);

    this.state = {
      graph: new Graph(),
    };

    this.state.graph.randomize(xCount, yCount, boxSize, probability);
  }

  
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
        <button onClick={this.onButton}>Random</button>
        <GraphView graph={this.state.graph} />
      </div>
    );
  }
}

export default App;