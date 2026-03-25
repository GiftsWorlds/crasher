const express = require('express');
const cors = require('cors');
const fetch = require('node-fetch');

const app = express();
app.use(cors());

const API_TOKEN = 'ВАШ_ТОКЕН_СЮДА'; // Вставь свой токен с developer.brawlstars.com

app.get('/v1/*', async (req, res) => {
  const url = `https://api.brawlstars.com${req.url}`;
  try {
    const response = await fetch(url, {
      headers: {
        'Authorization': `Bearer ${API_TOKEN}`,
        'Accept': 'application/json'
      }
    });
    const data = await response.json();
    res.json(data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.listen(process.env.PORT || 3000, () => {
  console.log('BS Proxy запущен!');
});
