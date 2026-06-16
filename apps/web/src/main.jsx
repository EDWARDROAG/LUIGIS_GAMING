import React from 'react'
import ReactDOM from 'react-dom/client'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import App from './App.jsx'
import { applyPublicAssetCssVars } from './utils/assets.js'
import './index.css'

applyPublicAssetCssVars()

const queryClient = new QueryClient()

ReactDOM.createRoot(document.getElementById('root')).render(
<React.StrictMode>
<QueryClientProvider client={queryClient}>
<App />
</QueryClientProvider>
</React.StrictMode>
)
