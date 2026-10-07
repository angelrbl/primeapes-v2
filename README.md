# PrimeApes 🦍

Aplicación para **planificar y registrar tus entrenamientos**: base de ejercicios, series, historial y planificación por ciclos. Funciona **sin conexión**: tus datos se guardan en una base de datos SQLite dentro del propio dispositivo.

Esta es la reescritura de [primeapes-app](https://github.com/angelrbl/primeapes-app) (Streamlit), pensada desde cero para móvil.

## Tecnologías

| Área | Herramienta |
|---|---|
| Interfaz | [Flet](https://flet.dev) (Python) |
| Base de datos | SQLite + SQLAlchemy |
| Tests | pytest |


## Puesta en marcha

```powershell
git clone https://github.com/angelrbl/primeapes-v2.git
cd primeapes-v2
python -m venv .venv
.venv\Scripts\activate
pip install flet
pip install -r requirements-dev.txt
```

> Si PowerShell no deja activar el entorno virtual, ejecuta una vez
> `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`.

### Ejecutar la app

```powershell
flet run
```

### Modo desarrollo (ventana con tamaño de móvil y recarga automática)

```powershell
$env:PRIMEAPES_DEV=1; flet run -d -r
```

Con `PRIMEAPES_DEV` activo, la ventana se abre con proporciones de móvil (390×844) y la base de datos se guarda en `storage/data/`. Al empaquetar la app, usa la carpeta de almacenamiento que Flet reserva para ella.
También se puede añadir como variable de entorno en el archivo .env.

## Tests y calidad del código

```powershell
pytest
```

## Estructura del proyecto

```
src/
├── main.py          # Punto de entrada
├── core/            # Configuración y conexión a SQLite
├── models/          # Modelos SQLAlchemy
├── services/        # Lógica de negocio (sin dependencias de Flet)
├── views/           # Pantallas
└── components/      # Componentes de interfaz reutilizables
└── assets/          # Assets a usar en la app
tests/               # Tests de servicios y base de datos
storage/             # Datos locales de desarrollo (no se sube a Git)
```

## Flujo de trabajo

- `main` siempre está estable.
- Cada tarea parte de un issue y se desarrolla en su propia rama (`feat/…`, `fix/…`, `chore/…`).
- Los commits siguen [Conventional Commits](https://www.conventionalcommits.org/es/).

## Licencia

Pendiente de definir.