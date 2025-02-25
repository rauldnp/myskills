from datetime import datetime
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    try:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.on('console', lambda msg: print(f'Console log: {msg.text}'))  # Capturar logs do console
        page.goto('https://rauldnp.github.io/myskills/')
        
        # Esperar explicitamente pelo carregamento do gráfico
        page.wait_for_selector('#mynetwork', timeout=60000)  # Aumentando o timeout para 60 segundos
        
        # Tirar um screenshot após o carregamento do gráfico
        page.screenshot(path='scripts/myskills_screenshot.png')
        
        # Capturar o texto exibido na página após o carregamento
        page_text = page.inner_text('body')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('scripts/myskills_page_text.log', 'a', encoding='utf-8') as f:
            f.write(f'[{timestamp}]\n{page_text}\n\n')
    except Exception as e:
        print(f'Error occurred: {e}')
    finally:
        browser.close()