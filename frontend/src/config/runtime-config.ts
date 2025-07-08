export interface RuntimeConfig {
  REACT_APP_API_URL: string;
}

// Función para cargar la configuración desde el archivo generado en runtime
export const loadRuntimeConfig = async (): Promise<RuntimeConfig> => {
  try {
    const script = document.createElement('script');
    script.src = '/config.js?' + Date.now(); // Cache busting
    
    return new Promise((resolve, reject) => {
      script.onload = () => {

        if (window.runtimeConfig) {
          resolve(window.runtimeConfig as RuntimeConfig);
        } else {
          reject(new Error('Runtime config not found'));
        }
      };
      
      script.onerror = () => {
        reject(new Error('Failed to load runtime config'));
      };
      
      document.head.appendChild(script);
    });
  } catch (error) {
    console.error('Error loading runtime config:', error);
    
    return {
      REACT_APP_API_URL: 'http://localhost:8000',
    };
  }
};

declare global {
  interface Window {
    runtimeConfig?: RuntimeConfig;
  }
}