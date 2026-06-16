/** @type {import('tailwindcss').Config} */
export default {
content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
theme: {
extend: {
colors: {
gaming: {
primary: '#7C3AED',
secondary: '#1E1B4B',
accent: '#F59E0B',
dark: '#0F0A1A',
card: '#1A1430',
text: '#E2E8F0',
'text-light': '#94A3B8',
}
},
fontFamily: {
'gaming': ['"Orbitron"', 'sans-serif'],
},
animation: {
'glow': 'glow 2s ease-in-out infinite alternate',
'float': 'float 3s ease-in-out infinite',
},
keyframes: {
glow: {
'0%': { textShadow: '0 0 10px #7C3AED, 0 0 20px #7C3AED' },
'100%': { textShadow: '0 0 20px #A78BFA, 0 0 40px #7C3AED, 0 0 60px #7C3AED' },
},
float: {
'0%, 100%': { transform: 'translateY(0px)' },
'50%': { transform: 'translateY(-10px)' },
},
},
},
},
plugins: [],
}
