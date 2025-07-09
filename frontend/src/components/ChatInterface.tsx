import React, { useState, useRef, useEffect } from 'react';
import { Message } from '../types/chat';
import { chatService } from '../services/api';
import MessageBubble from './MessageBubble';
import InputBox from './InputBox';
import { MessageCircle, AlertCircle } from 'lucide-react';

const ChatInterface: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    const welcomeMessage: Message = {
      id: '1',
      content: 'Hello! I am the Promtior Assistant. I can answer questions about our services, history, and more. How can I help you?',
      isUser: false,
      timestamp: new Date(),
    };
    setMessages([welcomeMessage]);
  }, []);

  const handleSendMessage = async (content: string) => {
    const userMessage: Message = {
      id: Date.now().toString(),
      content,
      isUser: true,
      timestamp: new Date(),
    };

    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);
    setError(null);

    try {
      const response = await chatService.sendMessage(content);
      
      const botMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: response.response,
        isUser: false,
        timestamp: new Date(),
        sources: response.sources,
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (err) {
      console.error('Error sending message:', err);
      setError('Error sending message. Please try again.');
      
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: 'Sorry, there was an error processing your message. Please try again.',
        isUser: false,
        timestamp: new Date(),
      };

      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

    return (
    <div className="w-full max-w-2xl flex flex-col bg-white rounded-lg shadow-2xl" style={{ minHeight: '70vh', maxHeight: '90vh', border: '50px' }}>
        {error && (
        <div className="bg-red-50 border-l-4 border-red-400 p-4 rounded-t-lg">
            <div className="flex items-center">
            <AlertCircle className="w-5 h-5 text-red-400 mr-2" />
            <p className="text-red-700">{error}</p>
            </div>
        </div>
        )}

        <div className="flex-1 overflow-y-auto p-4" style={{ height: '60vh' }}>
        {messages.map((message) => (
            <MessageBubble key={message.id} message={message} />
        ))}
        {isLoading && (
            <div className="flex justify-start mb-4">
            <div className="bg-gray-100 rounded-lg p-4">
                <div className="flex items-center gap-2">
                <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-blue-500"></div>
                <span className="text-gray-600">Writing...</span>
                </div>
            </div>
            </div>
        )}
        <div ref={messagesEndRef} />
        </div>

        <InputBox onSendMessage={handleSendMessage} isLoading={isLoading} />
    </div>
    );
};

export default ChatInterface;