import React, { useState } from 'react';

const WordCount = () => {
  const [word, setWord] = useState('');

  const changeWord = e => {
    setWord(e.target.value);
  };

  return (
    <>
      <div>
        <input onChange={changeWord} value={word} />
      </div>
      <div>wordCount is {word.length}</div>
    </>
  );
};

export default WordCount;
