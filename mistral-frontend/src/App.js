import React from 'react';
import './App.css';
import Chat from './chatbot/chatbot';


function App() {
  return (
    <div className="App">
      <div className='Sider'>
      <img className='VhLogo' src='Icons\Logo White.png'>
      </img>
      </div>
     <Chat/>
    </div>
  );
}

export default App;
