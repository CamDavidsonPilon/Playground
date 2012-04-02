

import glob
import time
import sys
import re

def compiler(ending, name="All"):
    """

    This fuction will put all text from files with extension "ending" in the current directory into a new text file.

        ending:  a string that encodes a type of file, i.e. 'm', 'py', 'tex'.
        name: the name of the output file. If none is specified, will output 'All'+ending.
    """
    DIVIDER = "\n"+"%"*50 + "\n"
    
    p = re.search("""['"]{0,1}\.{1}([a-zA-Z]+)['"]{0,1}""",ending)
    if not p:
        print "I think you put a wrong ending in. It must be only letters."
        sys.exit()
    else: 
        ending = p.group(1)
    
    
    if name=="All":
        name = "Alldot"+ending + "Files.txt"
    
        
    files = glob.glob('*.'+ending)
    print
    print "Found %d files with extension .%s"%(len(files), ending)
    print "Creating %s file."%name
    
    try: 
        output = open( name, 'w')
        
        #insert time into the doc
        output.write(time.strftime("%d %b %Y %H:%M:%S", time.localtime() ) )
        
        for file in files:
        
            fh = open(file, 'r')
            
            output.write("\n")
            output.write(DIVIDER)
            output.write( file )
            output.write(DIVIDER)
            output.write("\n")
            
            output.write( fh.read() )
            
            fh.close()
        
        output.close()
        print "..."
        print "File %s created."%name
    except:
        print "There was an error."
        print sys.exc_info()[0]
        
        
    print "Goodbye"
    
    
    
if __name__ == '__main__':
    """attach the extension of the file and an optional name of the output file"""
    if len(sys.argv)<2:
        print "have atleast a extension, and an optional name."
    else:
        try:
            compiler( sys.argv[1], sys.argv[2] )
        except:
            compiler( sys.argv[1] )
    