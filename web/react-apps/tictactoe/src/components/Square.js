import React from 'react'

const button_style = {
  border: '2px solid green',
  width: '50px',
  height: '33px',
  fontSize: '25px',
  margin: '10px',
  backgroundColor: 'white',
  color: 'black',
  borderRadius: '5px',
}

function Square(props) {
  if (props.winLine) {

    for (let i = 0; i < props.winLine.length; i++)  {
      if (props.winLine[i] === props.index) {

        return (
          <button style={button_style} onClick={props.onClick}>
            <b>{props.value}</b>
          </button>
        )
      }
    }
  }

  return (
    <button style={button_style} onClick={props.onClick}>
      {props.value}
    </button>
  )
}

export default Square
