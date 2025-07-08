import axios from 'axios';
import { ChatRequest, ChatResponse } from '../types/chat';
import { loadRuntimeConfig, RuntimeConfig } from '../config/runtime-config';

let config: RuntimeConfig | null = null;
let configPromise: Promise<RuntimeConfig> | null = null;

const getConfig = async (): Promise<RuntimeConfig> => {
  if (config) {
    return config;
  }
  
  if (!configPromise) {
    configPromise = loadRuntimeConfig();
  }
  
  config = await configPromise;
  return config;
};

const api = axios.create({
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use(async (requestConfig) => {
  const runtimeConfig = await getConfig();
  requestConfig.baseURL = runtimeConfig.REACT_APP_API_URL;
  return requestConfig;
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

  getConfig: () => getConfig(),
};

export default api;