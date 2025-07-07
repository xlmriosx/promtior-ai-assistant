import React from 'react';
import Header from './components/Header';
import ChatInterface from './components/ChatInterface';

function App() {
  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      <Header />
      <div className="flex-1 flex items-center justify-center">
        <ChatInterface />
      </div>
    </div>
  );
}

export default App;