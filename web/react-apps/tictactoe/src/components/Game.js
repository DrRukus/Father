import React, { Component } from 'react'

import Board from './Board'
import InfoPanel from './InfoPanel'

class Game extends Component {
  constructor(props) {
    super(props)
    this.state = {
      history: [{
        squares: Array(9).fill(null),
        coords: ''
      }],
      stepNumber: 0,
      xIsNext: true,
    }
  }

  handleBoardClick(i) {
    const history = this.state.history.slice(0, this.state.stepNumber + 1)
    const current = history[history.length - 1]
    const squares = current.squares.slice()
    const coords = this.indexToCoords(i)
    if (calculateWinner(squares) || squares[i]) {
      return
    }
    squares[i] = this.state.xIsNext ? 'X' : 'O'
    this.setState({
      history: history.concat([{
        squares: squares,
        coords: coords
      }]),
      stepNumber: history.length,
      xIsNext: !this.state.xIsNext,
    })
  }

  indexToCoords(index) {
    let coords = [Math.floor(index / 3), index % 3]
    return '(' + coords[0] + ',' + coords[1] + ')'
  }

  jumpTo(step) {
    this.setState({
      stepNumber: step,
      xIsNext: (step % 2) === 0,
    })
  }

  menuOrder() {
    return this.state.ascending
  }

  render() {
    const history = this.state.history
    const current = history[this.state.stepNumber]
    const winner = calculateWinner(current.squares)
    const moves = history.map((step, move) => {
      let desc, label
      if (move) {
        label = `Go to move # ${move} - ${step.coords}`
        desc = (move === this.state.stepNumber) ?
               (<b>{label}</b>) : label
      } else {
        desc = 'Go to game start'
      }
      return (
        <li key={move}>
          <b><button onClick={() => this.jumpTo(move)}>{desc}</button></b>
        </li>
      )
    })

    let status, winLine
    if (winner) {
      winLine = winner.slice(0,winner.length - 1)
      status = 'Winner: ' + winner[winner.length - 1]
    } else {
      status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O')
    }

    return (
      <div className="game">
        <div className="game-board">
          <Board
            winLine={winLine}
            squares={current.squares}
            onClick={(i) => this.handleBoardClick(i)}
          />
        </div>
        <div className="game-info">
          <InfoPanel
            moves={moves}
            status={status}
            onClick={() => this.handleMenuOrderClick()}
          />
        </div>
      </div>
    )
  }
}

function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ]
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i]
    if (squares[a] && squares[a] === squares[b] &&
      squares[a] === squares[c]) {
        const payload = lines[i].concat([squares[a]])
        return payload
      }
  }
  return null
}

export default Game
