import logo from './logo.svg';
import './App.css';
import Counter from './components/Counter/Counter';
import UserInfo from './components/UserInfo/UserInfo';
import Header from './components/Header/Header';
import ChangeColor from './components/ChangeColor/ChangeColor';
import WordCount from './components/WordCount/WordCount';

function App() {
  return (
    <div className="App">
      <Header />
      <Counter />
      <UserInfo />
      <ChangeColor />
      <WordCount />
    </div>
  );
}

export default App;
