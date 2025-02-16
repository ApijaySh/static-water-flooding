from app.console.greet import Greeter
from app.tools.args import ArgParserTool

def app():
    greeter,parser = Greeter(),ArgParserTool()
    greeter.welcome()
    parser.parser.print_help()

if __name__ == '__main__':
    app()