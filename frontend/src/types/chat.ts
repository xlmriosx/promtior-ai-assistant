export interface Message {
  id: string;
  content: string;
  isUser: boolean;
  timestamp: Date;
  sources?: string[];
}

export interface ChatRequest {
  message: string;
}

export interface ChatResponse {
  response: string;
  sources: string[];
}