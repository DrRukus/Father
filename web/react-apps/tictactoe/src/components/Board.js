import React, { Component } from 'react'

import Square from './Square'

const board_styles = {
  border: '2px solid black',
  borderRadius: '5px',
  backgroundColor: '#546E7A',
  width: '250px',
  height: 'auto'
}

const inner_board = {
  margin: '20px'
}

class Board extends Component {

  renderSquare(i) {
    return (
      <Square
        winLine={this.props.winLine}
        key={i}
        index={i}
        value={this.props.squares[i]}
        onClick={() => this.props.onClick(i)}
      />
    )
  }

  renderRow(rowNum) {
    let row = []
    const start = rowNum * 3
    for (let i = start; i < start + 3; i++) {
      row.push(this.renderSquare(i))
    }
    return (
      <div key={rowNum} className="board-row">
        {row}
      </div>
    )
  }

  renderBoard() {
    let rows = []
    for (let i = 0; i < 3; i++) {
      rows.push(this.renderRow(i))
    }
    return rows
  }

  render() {
    return (
      <div style={board_styles}>
        <div style={inner_board}>
          {this.renderBoard()}
        </div>
      </div>
    )
  }
}

export default Board
