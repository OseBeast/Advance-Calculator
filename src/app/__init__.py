import os #New
import pkgutil
import importlib
import sys
from app.commands import CommandHandler, Command
from dotenv import load_dotenv #New
import logging #New
import logging.config #New


class App:
    def __init__(self): # Constructor
        os.makedirs('logs', exist_ok=True)#New
        self.configure_logging()#New
        load_dotenv() #New
        self.settings = self.load_environment_variables() #New
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION') #New
        logging.basicConfig(level=os.environ.get('LOGLEVEL', 'DEBUG')) #sets environnment level using environment var
        self.command_handler = CommandHandler()

    def configure_logging(self): #New
        logging_conf_path = 'logging.conf' #New
        if os.path.exists(logging_conf_path): #New
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False) #New
        else: #New
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') #New
        logging.info("Logging configured.")   #New

    def load_environment_variables(self): #New
        settings = {key: value for key, value in os.environ.items()} #New
        logging.info("Environment variables loaded.") #New
        return settings #New
    

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'): #New
        return self.settings.get(env_var, None) #New

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                            self.register_plugin_commands(plugin_module, plugin_name)
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                # Command names are now explicitly set to the plugin's folder name
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def start(self):
        # Register commands here
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        try:
            while True:  #REPL Read, Evaluate, Print, Loop
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    logging.info("User Exited Application.")
                if cmd_input.lower() == 'add':
                    logging.info("User Selected Add.")
                if cmd_input.lower() == 'subtract':
                    logging.info("User Selected Subtract.")
                if cmd_input.lower() == 'multiply':
                    logging.info("User Selected Multiply.")
                if cmd_input.lower() == 'divide':
                    logging.info("User Selected Divide.")
                self.command_handler.execute_command(cmd_input)           
        except KeyboardInterrupt:
            logging.warn("Program Terminated.")
            sys.exit(0)   # Assuming a KeyboardInterrupt should also result in a clean exit.
        finally:
            logging.info("Application shutdown.")

if __name__ == "__main__":
    app = App()
    app.start()
