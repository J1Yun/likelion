import React, { useState } from 'react';

const UserInfo = () => {
  const [name, setName] = useState('');
  const [nickname, setNickname] = useState('');

  const changeName = e => {
    setName(e.target.value);
  };

  const changeNickname = e => {
    setNickname(e.target.value);
  };

  return (
    <div>
      <div>
        <input onChange={changeName} value={name} />
        <input onChange={changeNickname} value={nickname} />
      </div>
      <div>
        <p>이름: {name}</p>
        <p>닉네임: {nickname}</p>
      </div>
    </div>
  );
};

export default UserInfo;
