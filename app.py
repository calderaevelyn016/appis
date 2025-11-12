from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret.key = "tu_clave_secreta_aqui"
API = "https://pokeapi.co/api/v2/pokemon/"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search',['POST'])
def search_pokemon():
    pokemon_name = request.form.get('pokemon_name', '').strip().lower()
    
    if not pokemon_name():
        flash('Por favor, ingresa u nombre de Pokemon','error')
        return redirect(url_for('index'))
    
    try:
        resp = requests.get(f"{API}{pokemon_name}")
        if resp.status_code == 200:
            pokemon_data = resp.json()
            return render_template('pokemon.html', pokemon=pokemon_data)
        else:
            flask(f'Pokemon "{pokemon_name}" no encontrado', 'error')
            return redirect(url_for('index'))
    except requests.exceptions.RequestException as e:
        flash('Error')