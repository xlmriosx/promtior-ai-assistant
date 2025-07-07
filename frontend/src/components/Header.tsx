import React from 'react';

const Header: React.FC = () => (
  <header className="w-full bg-white shadow-sm border-b p-4 flex items-center gap-3 justify-center">
    <img src="/logo.png" alt="Promtior Logo" className="h-10 w-10 rounded-full" />
    <div>
      <h1 className="text-xl font-semibold text-gray-800">Promtior Assistant</h1>
      <p className="text-sm text-gray-600">Chatbot RAG con información sobre Promtior</p>
    </div>
  </header>
);

export default Header;