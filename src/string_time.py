'''Function takes a non negative number of seconds and returns 
   time in a readable format. This is a simple version of this function.
   Check ReadMe for more complex version of it.'''

def make_readable(s):
    
    hours = int(s/ 3600)
    minutes = int((s % 3600)/60)
    seconds = int((s % 216000)% 60)
    time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return time
        
        