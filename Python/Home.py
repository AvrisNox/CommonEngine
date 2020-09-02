

class Home:
    @staticmethod
    def home():
        statics = {
            "stop": quit,
            "quit": quit,
            "exit": quit,
            "q": quit,
            "!": Home.bang_quit,
            "!!": Home.double_bang_quit,
            ":q": quit,
            ":q!": quit
        }

        active = True
        while active:
            cmd = input("Please enter a command: ")

            if cmd.lower() in statics:
                statics[cmd.lower()]()

            else:
                if cmd is not None and len(cmd) > 0:
                    params = cmd.split(" ")
                    cmd = "Python.src." + params[0]
                    p_args, p_kwargs = Home.get_args_kwargs(params)
                else:
                    p_args = []
                    p_kwargs = {}
                    cmd = "Python.src"
                import importlib
                try:
                    modl = importlib.import_module(cmd)
                    try:
                        modl.run(*p_args, **p_kwargs)
                    except AttributeError:
                        print("The module you wanted to import cannot \"run\" - try adding a run function at top level.")
                except ModuleNotFoundError:
                    print("The requested module does not exists - check spelling and try again.")

    @staticmethod
    def get_args_kwargs(input_list):
        args = []
        kwargs = {}

        for obj in input_list:
            if "=" not in obj:
                args.append(obj)
            else:
                bits = obj.split("=")
                kwargs[bits[0]] = bits[1]

        return args, kwargs

    @staticmethod
    def bang_quit():
        print("Bang quit")
        quit()

    @staticmethod
    def double_bang_quit():
        print("Double bang quit")
        quit()
