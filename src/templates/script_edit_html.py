# Autogenerated file
def render(info, script):
    yield """
<form name = 'frmselect' method = 'post'>
    <table cellpadding='4' border='1' frame='box' rules='all'>
       <TH>Name
       <TR>
            <TD>
            """
    if script['operation'] == 'edit':
        yield """ 
                <B>"""
        yield str(script['filename'])
        yield """</B>
                <input type='hidden' name='filename' maxlength='26' value='"""
        yield str(script['filename'])
        yield """'>
            """
    else:
        yield """
                Filename: <input type='text' name='filename' maxlength='26' value=''>
            """
    yield """
       <TR>
          <TD><textarea name='content' rows='15' cols='80' wrap='off'>"""
    yield str(script['content'])
    yield """</textarea>
       <TR>
          <TD>Current size: """
    yield str(script['size'])
    yield """ characters
       <TR>
          <TD>
            <hr>
       <TR>
          <TD><a class=\"button link\" href=\"scripts\">Close</a><input class=\"button link\" type='submit' value='Submit'>
   </table>
</form>
"""
