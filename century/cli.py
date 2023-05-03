import typer
import os
import shutil
from importlib.util import spec_from_file_location
from dotenv import load_dotenv
from century import century_conf_loader, settings
from rich import print


app = typer.Typer(
    name="century",
    help="Century CLI",
    short_help="Century CLI",
    add_completion=False,
    # invoke_without_command=False,
    # no_args_is_help=True,
    context_settings={"help_option_names": ["-h", "--help"]},

)


@app.command(
    help="Initialize Century",
    short_help="Initialize Century",
)
def init(project_name: str):
    typer.echo("Initializing Century Project: "+ project_name)
    path = os.path.join(os.getcwd(), project_name)
    if os.path.exists(path):
        typer.echo("Project already exists")
        return
    else:
        # Copy the default structures to the project folder
        shutil.copytree(
            os.path.join(os.path.dirname(__file__), "_default_stuctures"),
            path
        )
        typer.echo("Project stuctures created successfully")

        # Rename the app folder to the project name
        os.rename(
            os.path.join(path, "app"),
            os.path.join(path, project_name)
        )
        
        # Change directory to the project folder
        os.chdir(path)
        typer.echo("Changing directory to: "+ path)

        # Update the settings configs
        _conf = century_conf_loader()
        _conf_app = _conf.get_all()

        _conf_app['APP'] = {
            "NAME": project_name,
            "PATH": path,
            "SETTINGS": os.path.join(path, project_name, "settings.py"),
        }
        # Update the century.json file
        _conf.update("APP", _conf_app['APP'])

        # Update the main.py file
        with open(os.path.join(path, "main.py"), "w") as _main:
            _main.write(f"from {project_name} import app as application")
        
        # Update .env file
        load_dotenv()
        os.environ['APP_NAME'] = project_name
        os.environ['APP_PATH'] = f'{project_name} Slogan'
        os.environ['DESCRIPTION'] = f'{project_name} Description'
        
        typer.echo("Project created successfully")


@app.command(
    help="Create a new model",
    short_help="Create a new model",
)
def create():
    typer.echo("Creating a new model")


@app.command(
    help="Create a new migration",
    short_help="Create a new migration",
)
def migrate():
    typer.echo("Creating a new migration")


@app.command(
    help="Run migrations",
    short_help="Run migrations",
)
def migrate():
    typer.echo("Running migrations")


@app.command(
    help="Run the project",
    short_help="Run the project",
)
def run():
    if not os.path.exists("main.py"):
        print("[bold red]Error: [/bold red]main.py file not found")
        return
    
    # _application = import_module("main").application
    # typer.echo("Running the flask development server")
    # _application.run()

     # Import the Flask application instance from the specified module
    # module = import_module("main")

    __get_app_path = century_conf_loader().get("APP").get("PATH")
        
    __main = spec_from_file_location(
        "main", os.path.join(__get_app_path, "main.py")
    ).loader.load_module()

    application = getattr(__main, "application", None)
    if application is None:
        print("[bold red]Error: [/bold red]Flask application instance not found")
        return
    
    # Start the development server
    typer.echo("Running the Flask development server")
    application.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG,
    )


if __name__ == "__main__":
    app()
