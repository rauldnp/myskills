# Linguagens de Programação

## Python

### Automação Web

#### Selenium

Biblioteca Python robusta para automação de navegadores web. Essencial para interagir com elementos dinâmicos de páginas web, simular ações humanas complexas e automatizar fluxos de trabalho completos, como extração de dados, preenchimento de formulários e geração de relatórios.

##### WebDriverManager

Biblioteca para gerenciamento automatizado de drivers de navegadores (ChromeDriver, GeckoDriver, etc.). Simplifica a configuração do ambiente Selenium, garantindo a compatibilidade entre o navegador e o driver, e facilitando a execução de scripts em diferentes ambientes.

##### WebDriverWait

Utilização da espera explícita (`WebDriverWait`) do Selenium para garantir que os elementos web estejam totalmente carregados e interativos antes de executar ações sobre eles. Isso torna a automação mais resiliente a variações de tempo de carregamento da página e evita erros.

##### ChromeOptions

Configuração avançada do navegador Chrome (`ChromeOptions`) para otimizar a automação, definindo o diretório de download padrão, desabilitando funcionalidades desnecessárias e personalizando o comportamento do navegador para o contexto da automação.

#### python-telegram-bot

Biblioteca Python para criar bots do Telegram. Permite interagir com a API do Telegram de forma programática.

### AI

#### google.generativeai

### Dados

#### pandas

Utilizada para manipulação e análise de dados, especialmente para trabalhar com os arquivos Excel (leitura, transformação e escrita).

#### openpyxl

Mecanismo (engine) que o *pandas* usa para interagir com arquivos Excel no formato `.xlsx`.  É uma dependência do *pandas*.

#### requests

Utilizada para realizar requisições HTTP,  fundamental para interagir com APIs web e baixar arquivos de servidores (como no projeto ASC).

#### xlsxwriter

Biblioteca para criar e modificar arquivos Excel (.xlsx) de forma eficiente,  ideal para gerar relatórios e exportar dados.

#### chardet

Biblioteca para detecção de encoding de arquivos, importante para lidar com diferentes formatos de texto.

#### docling

Biblioteca para conversão de documentos, com foco em conversão de PDF para Markdown.

#### PyPDF2

Biblioteca para manipulação de arquivos PDF.

### Uso geral

#### logging

Biblioteca para registrar eventos e mensagens de erro/debug, essencial para monitorar a execução de scripts e diagnosticar problemas.

#### regex (re)

Utilizo expressões regulares para tarefas de manipulação de texto, como extração de padrões e validação de dados.

#### Asyncio

Biblioteca para programação assíncrona, essencial para bots que precisam lidar com múltiplas requisições simultaneamente.

#### Threading (threading)

Implementação de multithreading com a biblioteca `threading` para executar tarefas de monitoramento de downloads em paralelo, sem bloquear o fluxo principal do script. Isso melhora a performance e a responsividade da automação.

#### Watchdog

Biblioteca Python eficiente para monitoramento do sistema de arquivos em tempo real. Utilizada para detectar a conclusão de downloads de arquivos de forma confiável, reagindo a eventos de criação e movimentação de arquivos na pasta de download, garantindo que o script processe apenas arquivos totalmente baixados.

#### Queue (queue)

Emprego de filas thread-safe (`queue.Queue`) para comunicação segura entre threads, permitindo que a thread de monitoramento (`watchdog`) envie o caminho do arquivo baixado para a thread principal de forma sincronizada e sem riscos de race conditions.

### Web

#### streamlit

#### BeautifulSoup

### APIs

#### RESTful

## Delphi

## C#

## ASP.NET
