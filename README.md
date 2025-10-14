# Django Channels + React + Celery + Redis: Real-Time Table (CoinMarketCap Clone)  

Educational project based on [this video](https://youtu.be/wos1uhnd3qM).  

This project is a real-time cryptocurrency prices table (CoinMarketCap clone) built with **Django Channels**, **Celery**, **Redis**, and **React**.  
It performs periodic data fetching from the **CoinGecko API** every 30 seconds and broadcasts updates to all connected clients via **WebSockets**.

- **Backend:** Django, Channels, Celery, Redis  
- **Frontend:** React (instead of Vue.js in the video)  
- **Data:** CoinGecko API, updated every 30 seconds via WebSockets  


