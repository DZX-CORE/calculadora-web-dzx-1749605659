from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def calculadora():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>Calculadora DZX-CORE</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
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
            margin: 10px;
            font-size: 18px;
            border: 2px solid #ddd;
            border-radius: 8px;
            width: 150px;
        }
        button {
            background: #4CAF50;
            color: white;
            cursor: pointer;
            border: none;
            transition: all 0.3s;
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
            font-size: 22px;
            font-weight: bold;
            color: #2c3e50;
            border-left: 5px solid #4CAF50;
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
            <button onclick="calcRaiz()">√ Raiz Quadrada</button>
        </div>
        
        <div id="resultado">Digite os números e escolha a operação</div>
    </div>
    
    <script>
        function calc(op) {
            let a = parseFloat(document.getElementById('a').value);
            let b = parseFloat(document.getElementById('b').value);
            
            if (isNaN(a) || isNaN(b)) {
                document.getElementById('resultado').innerHTML = '⚠️ Digite números válidos';
                return;
            }
            
            let r;
            let opName;
            
            if (op == '+') {
                r = a + b;
                opName = 'Soma';
            } else if (op == '-') {
                r = a - b;
                opName = 'Subtração';
            } else if (op == '*') {
                r = a * b;
                opName = 'Multiplicação';
            } else if (op == '/') {
                if (b == 0) {
                    document.getElementById('resultado').innerHTML = '❌ Erro: Divisão por zero';
                    return;
                }
                r = a / b;
                opName = 'Divisão';
            }
            
            document.getElementById('resultado').innerHTML = 
                `✅ ${opName}: ${a} ${op} ${b} = ${r}`;
        }
        
        function calcPotencia() {
            let a = parseFloat(document.getElementById('a').value);
            let b = parseFloat(document.getElementById('b').value);
            
            if (isNaN(a) || isNaN(b)) {
                document.getElementById('resultado').innerHTML = '⚠️ Digite números válidos';
                return;
            }
            
            let r = Math.pow(a, b);
            document.getElementById('resultado').innerHTML = 
                `✅ Potência: ${a}^${b} = ${r}`;
        }
        
        function calcRaiz() {
            let a = parseFloat(document.getElementById('a').value);
            
            if (isNaN(a)) {
                document.getElementById('resultado').innerHTML = '⚠️ Digite um número válido';
                return;
            }
            
            if (a < 0) {
                document.getElementById('resultado').innerHTML = '❌ Erro: Raiz de número negativo';
                return;
            }
            
            let r = Math.sqrt(a);
            document.getElementById('resultado').innerHTML = 
                `✅ Raiz Quadrada: √${a} = ${r}`;
        }
    </script>
</body>
</html>
""")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
