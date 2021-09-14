import React, { useState } from 'react';

const ChangeColor = () => {
  const [color, setColor] = useState('white');

  const changeColor = e => {
    setColor(e.target.value);
  };

  return (
    <div style={{ backgroundColor: color, padding: '10px' }}>
      <button value="black" onClick={changeColor} style={{ color: 'grey' }}>
        검정
      </button>
      <button value="white" onClick={changeColor} style={{ color: 'grey' }}>
        하양
      </button>
    </div>
  );
};

export default ChangeColor;
