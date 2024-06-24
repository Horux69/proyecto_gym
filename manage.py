from app import inicializador_app

app = inicializador_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)