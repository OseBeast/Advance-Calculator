import os 
import pkgutil
import importlib
import sys
from app.commands import CommandHandler, Command
from dotenv import load_dotenv 
import logging 
import logging.config 

#This is the main class that holds all of the architecture of the code
class App:
    #initializes the settings of the commands, logging and environment variables
    def __init__(self): # Constructor
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv() 
        self.settings = self.load_environment_variables() 
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION') 
        self.command_handler = CommandHandler()

    #This configures the logging class so that is can log into app.log
    def configure_logging(self): 
        logging_conf_path = 'logging.conf' 
        if os.path.exists(logging_conf_path): 
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False) #sets environnment level using environment var
        else: 
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') 
        logging.info("Logging configured.")   
    
    def load_environment_variables(self): 
        settings = {key: value for key, value in os.environ.items()} 
        logging.info("Environment variables loaded.") 
        return settings 
    

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'): 
        return self.settings.get(env_var, None) 

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
    #Main menu display
    def menu(self):

        menuStr = '''Type the command to select the following:
                add: Adds two numbers
                subtract: Subtracts two numbers
                multiply: Multiplies two numbers
                divide: Divides two numbers
                load: Load history from a csv file which will add to the current history
                save: Save the current history
                delete: Deletes the history
                clear: Clears the history from display 
                exit: Exits out of the program   
        '''
        print(menuStr)

    #Used to pair commands with the plugins
    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                # Command names are now explicitly set to the plugin's folder name
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    #The beginning of the program
    def start(self):
        # Register commands here
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        try:
            #Main program loop for user interaction
            while True:  #REPL Read, Evaluate, Print, Loop
                self.menu()
                self.command_handler.execute_command("show_history")
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
