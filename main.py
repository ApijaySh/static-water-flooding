from app.console.greet import Greeter
from app.tools.args import ArgParserTool

def app():
    greeter,parser = Greeter(),ArgParserTool()
    greeter.welcome()
    arg_values = parser.parser.parse_args()
    print(arg_values)
    tdata = parser.parse_(arg_values.__dict__)
    print(tdata)

if __name__ == '__main__':
    app()