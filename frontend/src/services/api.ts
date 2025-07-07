import axios from 'axios';
import { ChatRequest, ChatResponse } from '../types/chat';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const chatService = {
  sendMessage: async (message: string): Promise<ChatResponse> => {
    const request: ChatRequest = { message };
    const response = await api.post<ChatResponse>('/chat', request);
    return response.data;
  },

  checkHealth: async (): Promise<{ status: string }> => {
    const response = await api.get('/health');
    return response.data;
  },
};

export default api;