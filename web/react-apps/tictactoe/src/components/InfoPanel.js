import React, { Component } from 'react'

class InfoPanel extends Component {
  constructor(props) {
    super(props)
    this.state = {
      ascending: true,
    }
  }

  handleMenuOrderClick() {
    this.setState({
      ascending: !this.state.ascending,
    })
  }

  menuList() {
    if (this.state.ascending) {
      return <ol >{this.props.moves}</ol>
    } else {
      let reversedMoves = []
      for (let i = this.props.moves.length; i >= 0; i--) {
        reversedMoves.push(this.props.moves[i])
      }
      return <ol reversed>{reversedMoves}</ol>
    }
  }

  render() {
    return (
      <div>
        <div>{this.props.status}</div>
        <button onClick={() => this.handleMenuOrderClick()} >
          List order
        </button>
        {this.menuList()}
      </div>
    )
  }
}

export default InfoPanel
