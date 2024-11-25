
# Smart Horses Project

Este proyecto es una simulación de un juego en un tablero de ajedrez (8x8) con dos caballos, donde el objetivo es maximizar los puntos acumulados por cada caballo. Los jugadores pueden ser humanos o inteligencias artificiales (IA) controladas por algoritmos de minimax con poda alfa-beta.

## Requisitos

### Frontend (Angular)
- Node.js (v14 o superior)
- Angular CLI (`@angular/cli`)
- Angular Material

### Backend (Flask)
- Python (3.x)
- Flask
- Flask-CORS
- Tabulate
- Numpy

## Estructura del Proyecto

El proyecto está dividido en dos partes principales:
1. **Frontend (Angular)**: Gestiona la interfaz de usuario, mostrando el tablero y las puntuaciones de los caballos.
2. **Backend (Flask)**: Proporciona la API para ejecutar las jugadas, manejar la lógica del juego y realizar simulaciones IA vs IA.

## Instalación

### 1. Clonar el Repositorio

Clona el repositorio en tu máquina local:

```bash
git clone https://github.com/NathaMoraHSB/SmartHorsesProject
cd SmartHorsesProject
```

###  2. Configuración del Frontend (Angular)

#### Instalación de Dependencias
En la carpeta raíz del proyecto, accede al directorio `frontend` y ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
cd smart_horses_frontend
npm install
```

#### Ejecución del Frontend
Una vez que las dependencias estén instaladas, puedes iniciar el servidor de desarrollo de Angular:

```bash
ng serve
```

Esto iniciará la aplicación Angular en [http://localhost:4200/](http://localhost:4200/). Puedes acceder a la interfaz de usuario del proyecto desde un navegador web.

### 3. Configuración del Backend (Flask)

#### Instalación de Dependencias

En la raíz del proyecto, instala las dependencias de Python necesarias:

```bash
pip install -r requirements.txt
```

### 4. Iniciar el Backend

```bash
python app.py
```

El servidor se iniciará en [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Características

- **Modos de Juego**:
    - IA vs IA
    - IA vs Humano
- **Niveles de Dificultad**: Principiante, Intermedio y Avanzado.
- **Simulaciones**: Generación de reportes detallados para IA vs IA con estadísticas de victorias y empates.

## Autores

Nathalia Carolina Mora Arciniegas

**Código:** 2413217

Juan Camilo Valencia

**Código:** 2259459
