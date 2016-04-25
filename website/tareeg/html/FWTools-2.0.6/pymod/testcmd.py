
import gvcommand
import string
import sys

class EchoCommand(gvcommand.CommandBase):

    def __init__(self):
        self.Name = 'echo'
        self.Usage = 'Echo [/noeval] <quoted text or a python expression>'
        self.HelpURL = ''

        self.Args = [
            gvcommand.ArgDef( name = 'noeval', type = 'switch',
                              required = 0, ),
            gvcommand.ArgDef( name = 'text', type = 'string_chunk',
                              required = 1 )
            ]
            
                           
    def execute( self, args, line, interpreter ):
        if args[0]:
            interpreter.showText( args[1], 'result' )
            return

        try:
            result = str(eval(args[1]))
            interpreter.showText( result, 'result' )
        except:
            junk, exception = sys.exc_info()[:2]
            interpreter.showText( str(exception), 'error' )
            
class QuitCommand(gvcommand.CommandBase):

    def __init__(self):
        self.Name = 'quit'
        self.Usage = 'QUIT'
        self.HelpURL = ''

        self.Args = []				
                           
    def execute( self, args, line, interpreter ):
        import sys
        sys.exit( 0 )

class DefineCommand(gvcommand.CommandBase):

    def __init__(self):
        self.Name = 'define'
        self.Usage = 'DEFINE <var> {type} {initial value}'
        self.HelpURL = ''

        self.Args = [
            gvcommand.ArgDef( name = 'analyse_var', type = 'string_token',
                              validate_method = self.validate_analysis_var ),
            gvcommand.ArgDef( name = 'grouping_var', type = 'string_token',
                              validate_method = self.validate_grouping_var ),
            gvcommand.ArgDef( name = 'n', type = 'switch', required = 0, ),
            ]

    def validate_analysis_var( self, text ):
        print 'Trying to validate(analysis): '+ text
        return None
            
    def validate_grouping_var( self, text ):
        print 'Trying to validate(grouping): '+ text
        return None
            
    def execute( self, args, line, interpreter ):

        print 'analysis var = ' + args[0]
        print 'grouping var = ' + args[1]
        print 'n_switch = ' + str(args[2])
            

if __name__ == '__main__':

    import pyshell
    import GtkExtra
    import gtk

    commands = [ EchoCommand(), QuitCommand(), DefineCommand() ]

    app = pyshell.Shell()
    for cmd in commands:
        app.add_command( cmd )
    app.show_all()
    
    GtkExtra.debug_main_quit()
    gtk.mainloop()

