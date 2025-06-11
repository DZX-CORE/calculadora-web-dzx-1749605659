from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def calculadora():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>Calculadora DZX-CORE</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            margin: 0;
            min-height: 100vh;
        }
        .calc {
            background: rgba(255, 255, 255, 0.95);
            padding: 40px;
            border-radius: 15px;
            max-width: 450px;
            margin: 0 auto;
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
            color: #333;
        }
        input, button {
            padding: 15px;
            margin: 8px;
            font-size: 18px;
            border: 2px solid #ddd;
            border-radius: 8px;
            width: 140px;
        }
        button {
            background: #4CAF50;
            color: white;
            cursor: pointer;
            border: none;
            transition: all 0.3s;
            font-weight: bold;
        }
        button:hover {
            background: #45a049;
            transform: translateY(-2px);
        }
        #resultado {
            background: #e8f5e8;
            padding: 25px;
            margin: 25px 0;
            border-radius: 10px;
            font-size: 20px;
            font-weight: bold;
            color: #2c3e50;
            border-left: 5px solid #4CAF50;
            min-height: 50px;
        }
        .logo {
            font-size: 48px;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #666;
            margin-bottom: 30px;
            font-style: italic;
        }
        .footer {
            margin-top: 30px;
            color: #888;
            font-size: 14px;
        }
        @media (max-width: 600px) {
            .calc { padding: 20px; margin: 10px; }
            input, button { width: 120px; font-size: 16px; }
        }
    </style>
</head>
<body>
    <div class="calc">
        <div class="logo">🧮</div>
        <h1>Calculadora DZX-CORE</h1>
        <p class="subtitle">Criada pelo orquestrador inteligente</p>
        
        <div>
            <input type="number" id="a" placeholder="Primeiro número" step="any">
            <input type="number" id="b" placeholder="Segundo número" step="any">
        </div>
        
        <div>
            <button onclick="calc('+')">+ Somar</button>
            <button onclick="calc('-')">- Subtrair</button>
        </div>
        
        <div>
            <button onclick="calc('*')">× Multiplicar</button>
            <button onclick="calc('/')">÷ Dividir</button>
        </div>
        
        <div>
            <button onclick="calcPotencia()">^ Potência</button>
            <button onclick="calcRaiz()">√ Raiz</button>
        </div>
        
        <div>
            <button onclick="limpar()">Limpar</button>
            <button onclick="calcFatorial()">! Fatorial</button>
        </div>
        
        <div id="resultado">Digite os números e escolha a operação</div>
        
        <div class="footer">
            Desenvolvido com DZX-CORE
        </div>
    </div>
    
    <script>
        function calc(op) {
            let a = parseFloat(document.getElementById('a').value);
            let b = parseFloat(document.getElementById('b').value);
            
            if (isNaN(a) || isNaN(b)) {
                document.getElementById('resultado').innerHTML = 'Digite números válidos nos dois campos';
                return;
            }
            
            let r;
            let opName;
            
            switch(op) {
                case '+':
                    r = a + b;
                    opName = 'Soma';
                    break;
                case '-':
                    r = a - b;
                    opName = 'Subtração';
                    break;
                case '*':
                    r = a * b;
                    opName = 'Multiplicação';
                    break;
                case '/':
                    if (b == 0) {
                        document.getElementById('resultado').innerHTML = 'Erro: Divisão por zero';
                        return;
                    }
                    r = a / b;
                    opName = 'Divisão';
                    break;
            }
            
            document.getElementById('resultado').innerHTML = 
                opName + ': ' + a + ' ' + op + ' ' + b + ' = ' + r.toFixed(4).replace(/\.?0+$/, '');
        }
        
        function calcPotencia() {
            let a = parseFloat(document.getElementById('a').value);
            let b = parseFloat(document.getElementById('b').value);
            
            if (isNaN(a) || isNaN(b)) {
                document.getElementById('resultado').innerHTML = 'Digite números válidos nos dois campos';
                return;
            }
            
            let r = Math.pow(a, b);
            document.getElementById('resultado').innerHTML = 
                'Potência: ' + a + '^' + b + ' = ' + r.toFixed(4).replace(/\.?0+$/, '');
        }
        
        function calcRaiz() {
            let a = parseFloat(document.getElementById('a').value);
            
            if (isNaN(a)) {
                document.getElementById('resultado').innerHTML = 'Digite um número válido no primeiro campo';
                return;
            }
            
            if (a < 0) {
                document.getElementById('resultado').innerHTML = 'Erro: Raiz de número negativo';
                return;
            }
            
            let r = Math.sqrt(a);
            document.getElementById('resultado').innerHTML = 
                'Raiz Quadrada: √' + a + ' = ' + r.toFixed(4).replace(/\.?0+$/, '');
        }
        
        function calcFatorial() {
            let a = parseInt(document.getElementById('a').value);
            
            if (isNaN(a) || a < 0 || a > 20) {
                document.getElementById('resultado').innerHTML = 'Digite um número inteiro entre 0 e 20';
                return;
            }
            
            let r = 1;
            for (let i = 2; i <= a; i++) {
                r *= i;
            }
            
            document.getElementById('resultado').innerHTML = 
                'Fatorial: ' + a + '! = ' + r;
        }
        
        function limpar() {
            document.getElementById('a').value = '';
            document.getElementById('b').value = '';
            document.getElementById('resultado').innerHTML = 'Campos limpos! Digite novos números.';
        }
    </script>
</body>
</html>
""")

@app.route('/health')
def health():
    return {'status': 'ok', 'app': 'Calculadora DZX-CORE'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
