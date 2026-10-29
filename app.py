import streamlit as st
import streamlit.components.v1 as components

# Page Configuration for Full Screen Dark Layout
st.set_page_config(
    page_title="QUANTITATIVE FINANCIAL COMMAND CENTER",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling to Hide Streamlit Elements & Force Dark Cyberpunk Theme
st.markdown("""
<style>
    /* Hide Streamlit Header, Footer, and Padding */
    header { visibility: hidden; }
    footer { visibility: hidden; }
    #MainMenu { visibility: hidden; }
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    body {
        background-color: #05070a;
    }
</style>
""", unsafe_allowed_html=True)

# Full Exact Cyberpunk HTML/CSS/JS Engine
cyberpunk_html = """
<!DOCTYPE html>
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
            background: rgba(0, 0
