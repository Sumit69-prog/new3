import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(
    page_title="QUANTITATIVE FINANCIAL COMMAND CENTER",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit Default UI Elements
st.markdown("""
<style>
    header { visibility: hidden; }
    footer { visibility: hidden; }
    #MainMenu { visibility: hidden; }
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }
    body {
        background-color: #05070a;
    }
</style>
""", unsafe_allowed_html=True)

# Cyberpunk Dashboard HTML/CSS/JS Engine
cyberpunk_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600;800&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        :root {
            --bg-base: #05070a;
            --panel-bg: rgba(10, 15, 24, 0.85);
            --border-glow: rgba(0, 243, 255, 0.25);
            --text-main: #e2f1f8;
            --text-dim: #5c7080;
            --accent-green: #00ff66;
            --accent-cyan: #00f3ff;
            --accent-amber: #ffb700;
            --font-mono: 'JetBrains Mono', monospace;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }

        body {
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-mono);
            font-size: 11px;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 50% 50%, rgba(0, 243, 255, 0.05) 0%, transparent 80%),
                linear-gradient(rgba(0, 243, 255, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 243, 255, 0.03) 1px, transparent 1px);
            background-size: 100% 100%, 30px 30px, 30px 30px;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 16px;
            border-bottom: 1px solid var(--border-glow);
            background: rgba(5, 7, 10, 0.95);
        }

        .sys-id {
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 800;
            color: var(--accent-cyan);
        }

        .status-badge {
            background: rgba(0, 255, 102, 0.15);
            color: var(--accent-green);
            border: 1px solid var(--accent-green);
            padding: 2px 6px;
            font-size: 9px;
            border-radius: 2px;
        }

        .sys-telemetry { display: flex; gap: 20px; color: var(--text-dim); }
        .sys-telemetry span strong { color: var(--text-main); }

        .ticker-bar {
            background: rgba(0, 243, 255, 0.05);
            border-bottom: 1px solid var(--border-glow);
            padding: 4px 0;
            overflow: hidden;
            white-space: nowrap;
            font-size: 10px;
            color: var(--accent-cyan);
        }

        .ticker-content {
            display: inline-block;
            animation: ticker 35s linear infinite;
        }

        @keyframes ticker {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }

        .dashboard-grid {
            display: grid;
            grid-template-columns: 310px 1fr 330px;
            gap: 12px;
            padding: 12px;
            min-height: calc(100vh - 70px);
        }

        .panel {
            background: var(--panel-bg);
            border: 1px solid var(--border-glow);
            border-radius: 4px;
            padding: 12px;
            display: flex;
            flex-direction: column;
        }

        .panel-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            padding-bottom: 6px;
            border-bottom: 1px dashed var(--border-glow);
            font-weight: 600;
            color: var(--accent-cyan);
        }

        .stat-card {
            background: rgba(0, 0, 0, 0.4);
            border-left: 3px solid var(--accent-cyan);
            padding: 8px 10px;
            margin-bottom: 8px;
        }

        .stat-card.green { border-color: var(--accent-green); }
        .stat-card.amber { border-color: var(--accent-amber); }

        .stat-label { color: var(--text-dim); font-size: 9px; margin-bottom: 2px; }
        .stat-val { font-size: 18px; font-weight: 800; }
        .stat-sub { font-size: 9px; color: var(--accent-green); }

        .center-stage {
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 420px;
        }

        #torus-canvas {
            width: 100%;
            height: 100%;
            position: absolute;
            top: 0; left: 0;
        }

        .stage-overlay {
            position: absolute;
            z-index: 2;
            pointer-events: none;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 12px;
        }

        .data-table { width: 100%; border-collapse: collapse; font-size: 10px; }
        .data-table th { text-align: left; color: var(--text-dim); padding: 4px; border-bottom: 1px solid var(--border-glow); }
        .data-table td { padding: 4px; border-bottom: 1px solid rgba(255, 255, 255, 0.03); }

        .text-right { text-align: right; }
        .text-green { color: var(--accent-green); }
        .text-cyan { color: var(--accent-cyan); }
        .text-amber { color: var(--accent-amber); }

        .bottom-panel { grid-column: 1 / -1; }
        .log-stream {
            font-size: 10px;
            height: 100px;
            overflow-y: auto;
            background: rgba(0, 0, 0, 0.5);
            padding: 8px;
            border: 1px solid rgba(0, 243, 255, 0.1);
        }
        .log-entry { margin-bottom: 3px; display: flex; gap: 10px; }
    </style>
</head>
<body>

    <header>
        <div class="sys-id">
            <span>// QUANT_HUB v4.0.8</span>
            <span class="status-badge">ONLINE</span>
            <span style="color: var(--text-dim); font-weight: normal;">DATASET: IT_PERFORMANCE_80K</span>
        </div>
        <div class="sys-telemetry">
            <span>LATENCY: <strong>14 ms</strong></span>
            <span>NODES: <strong>80,000 EMP</strong></span>
            <span>SYSTEM UTC: <strong id="clock">00:00:00 UTC</strong></span>
        </div>
    </header>

    <div class="ticker-bar">
        <div class="ticker-content">
            TOTAL REVENUE: $21,003,879,883.12 &nbsp;&nbsp;///&nbsp;&nbsp; TOTAL NET PROFIT: $10,292,147,209.95 &nbsp;&nbsp;///&nbsp;&nbsp; OVERALL MARGIN: 49.00% &nbsp;&nbsp;///&nbsp;&nbsp; DIRECT COST: $10,711,732,673.17 &nbsp;&nbsp;///&nbsp;&nbsp; TOP REGION: NORTH AMERICA ($2.07B PROFIT) &nbsp;&nbsp;///&nbsp;&nbsp; TOP CLIENT: VANGUARD MEDIA ($705.78M PROFIT)
        </div>
    </div>

    <div class="dashboard-grid">
        <div class="panel">
            <div class="panel-header"><span>[01] Financial Overview</span><span class="text-cyan">80K AGGREGATE</span></div>
            <div class="stat-card green"><div class="stat-label">GROSS CLIENT REVENUE</div><div class="stat-val text-green">$21.00B</div><div class="stat-sub">AVG / EMP: $262,548.50</div></div>
            <div class="stat-card"><div class="stat-label">TOTAL NET PROFIT</div><div class="stat-val text-cyan">$10.29B</div><div class="stat-sub">PROFIT MARGIN: 49.00%</div></div>
            <div class="stat-card amber"><div class="stat-label">TOTAL DIRECT COST</div><div class="stat-val text-amber">$10.71B</div><div class="stat-sub">SALARIES: $8.40B | OVERHEAD: $2.31B</div></div>
            <div class="panel-header" style="margin-top:10px;"><span>Department Yield</span></div>
            <table class="data-table">
                <thead><tr><th>DEPT</th><th class="text-right">PROFIT</th><th class="text-right">MARGIN</th></tr></thead>
                <tbody>
                    <tr><td class="text-cyan">Data & AI</td><td class="text-right">$2,077.0M</td><td class="text-right text-green">49.02%</td></tr>
                    <tr><td class="text-cyan">Engineering</td><td class="text-right">$2,066.1M</td><td class="text-right text-green">49.00%</td></tr>
                    <tr><td class="text-cyan">Quality Assurance</td><td class="text-right">$2,054.6M</td><td class="text-right text-green">49.01%</td></tr>
                    <tr><td class="text-cyan">Cloud & Infra</td><td class="text-right">$2,050.3M</td><td class="text-right text-green">49.01%</td></tr>
                    <tr><td class="text-cyan">Product & Design</td><td class="text-right">$2,044.2M</td><td class="text-right text-green">48.96%</td></tr>
                </tbody>
            </table>
        </div>

        <div class="panel center-stage">
            <canvas id="torus-canvas"></canvas>
            <div class="stage-overlay">
                <div style="display:flex; justify-content:space-between; font-size:10px; color:var(--accent-cyan);">
                    <span>MATRIX VISUALIZER // QUANTUM TORUS</span><span>ROTATION: ACTIVE</span>
                </div>
                <div style="display:flex; justify-content:space-between; font-size:9px; color:var(--text-dim);">
                    <span>NODE COUNT: 80,000</span><span style="color:var(--accent-green);">CORE STATUS: OPTIMAL</span>
                </div>
            </div>
        </div>

        <div class="panel">
            <div class="panel-header"><span>[02] Regional Matrix</span></div>
            <table class="data-table" style="margin-bottom:10px;">
                <thead><tr><th>REGION</th><th class="text-right">HEADCOUNT</th><th class="text-right">PROFIT</th></tr></thead>
                <tbody>
                    <tr><td>North America</td><td class="text-right">16,008</td><td class="text-right text-cyan">$2,071.1M</td></tr>
                    <tr><td>Europe</td><td class="text-right">16,074</td><td class="text-right text-cyan">$2,066.6M</td></tr>
                    <tr><td>Middle East</td><td class="text-right">16,102</td><td class="text-right text-cyan">$2,061.0M</td></tr>
                    <tr><td>Latin America</td><td class="text-right">15,934</td><td class="text-right text-cyan">$2,049.2M</td></tr>
                    <tr><td>Asia-Pacific</td><td class="text-right">15,882</td><td class="text-right text-cyan">$2,044.4M</td></tr>
                </tbody>
            </table>
            <div class="panel-header"><span>Top Enterprise Clients</span></div>
            <table class="data-table">
                <thead><tr><th>CLIENT</th><th class="text-right">REVENUE</th><th class="text-right">MARGIN</th></tr></thead>
                <tbody>
                    <tr><td>Vanguard Media</td><td class="text-right">$1,438.4M</td><td class="text-right text-green">49.07%</td></tr>
                    <tr><td>Nexus Logistics</td><td class="text-right">$1,433.3M</td><td class="text-right text-green">49.01%</td></tr>
                    <tr><td>Global Telco</td><td class="text-right">$1,432.5M</td><td class="text-right text-green">48.74%</td></tr>
                    <tr><td>Apex Healthcare</td><td class="text-right">$1,417.9M</td><td class="text-right text-green">49.28%</td></tr>
                    <tr><td>Quantum Analytics</td><td class="text-right">$1,412.1M</td><td class="text-right text-green">49.13%</td></tr>
                </tbody>
            </table>
        </div>

        <div class="panel bottom-panel">
            <div class="panel-header"><span>[03] Real-Time Execution Audit Stream</span></div>
            <div class="log-stream" id="log-container"></div>
        </div>
    </div>

    <script>
        function updateClock() {
            document.getElementById('clock').innerText = new Date().toISOString().substr(11, 8) + ' UTC';
        }
        setInterval(updateClock, 1000); updateClock();

        const canvas = document.getElementById('torus-canvas');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / canvas.clientHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
        renderer.setSize(canvas.clientWidth, canvas.clientHeight);

        const particleCount = 4000;
        const geometry = new THREE.BufferGeometry();
        const positions = new Float32Array(particleCount * 3);
        const colors = new Float32Array(particleCount * 3);
        const R = 3.2, r = 1.1;

        for (let i = 0; i < particleCount; i++) {
            const u = Math.random() * Math.PI * 2;
            const v = Math.random() * Math.PI * 2;
            positions[i * 3] = (R + r * Math.cos(v)) * Math.cos(u);
            positions[i * 3 + 1] = (R + r * Math.cos(v)) * Math.sin(u);
            positions[i * 3 + 2] = r * Math.sin(v);

            if (Math.random() > 0.3) {
                colors[i * 3] = 0; colors[i * 3 + 1] = 0.95; colors[i * 3 + 2] = 1;
            } else {
                colors[i * 3] = 0; colors[i * 3 + 1] = 1; colors[i * 3 + 2] = 0.4;
            }
        }
        geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

        const material = new THREE.PointsMaterial({ size: 0.035, vertexColors: true, transparent: true, opacity: 0.85 });
        const torus = new THREE.Points(geometry, material);
        scene.add(torus);
        camera.position.z = 6.8; camera.position.y = 1.5; camera.lookAt(0, 0, 0);

        function animate() {
            requestAnimationFrame(animate);
            torus.rotation.x += 0.003;
            torus.rotation.y += 0.005;
            renderer.render(scene, camera);
        }
        animate();

        const depts = ['Data & AI', 'Engineering', 'Quality Assurance', 'Cloud & Infra'];
        const roles = ['Data Scientist', 'Senior Software Engineer', 'DevOps Engineer', 'Cloud Architect'];
        const logContainer = document.getElementById('log-container');

        function generateLog() {
            const id = 'EMP-' + Math.floor(100000 + Math.random() * 80000);
            const dept = depts[Math.floor(Math.random() * depts.length)];
            const role = roles[Math.floor(Math.random() * roles.length)];
            const rev = (Math.random() * 150000 + 150000).toFixed(2);
            const time = new Date().toISOString().substr(11, 8);
            const logHTML = `
                <div class="log-entry">
                    <span style="color:var(--text-dim)">[${time}]</span>
                    <span style="color:var(--accent-cyan); width:120px;">${dept}</span>
                    <span>NODE: <strong style="color:var(--accent-cyan);">${id}</strong> | ROLE: ${role} | REVENUE: <span class="text-green">$${rev}</span></span>
                </div>
            `;
            logContainer.insertAdjacentHTML('afterbegin', logHTML);
            if (logContainer.children.length > 30) logContainer.removeChild(logContainer.lastChild);
        }
        setInterval(generateLog, 800);
    </script>
</body>
</html>"""

# Render Full Height Component
components.html(cyberpunk_html, height=880, scrolling=False)
