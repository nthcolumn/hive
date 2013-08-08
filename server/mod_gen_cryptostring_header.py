#!/usr/local/bin/python
#    We may have to change the above line based upon the build platform
#       The previous line used to read "#!/usr/bin/env python"
#    Could simply use a script with sed command to change the first line of
#    each ./*.py file for now...
#
#  gen_string_header.py
#
#

import mod_hexify
import sys

def main():
    """ """
    file = open(sys.argv[1]) #in this case, file = crypto_strings.txt
    if len(sys.argv) > 2:
        projheaders = sys.argv[2]
    else:
        projheaders = "PROJHEADERS" #in our case, args !> 2 so use PROJHEADERS always
    headerfile = file.read() #reads project_strings_source.h, going to need to read 2 files OR call this script twice inside doheaders.sh . . .
    file.close()
    newheaderfile = "#ifndef _%s__\n#define _%s__\n\n" %(projheaders, projheaders)
    newheaderfilemain = "#ifndef _%smain__\n#define _%smain__\n\n" %(projheaders, projheaders) 
    newheaderfile += "// *********** DO NOT MODIFY - autogenerated ***\n"
    forfunc = "// ***********DO NOT MODIFY - autogenerated ****\n\nvoid\ninit_crypto_strings()\n{\n"
    formain = "// ******DO NOT MODIFY - autogenerated **** FOR MAIN \n\n"
    for line in headerfile.split('\n'): #project_strings.source.h
        #print("line: %s" %line)
        
        # line should be
        # #define DEFINENAME DEFINEVALUE
        if (line.startswith("#define")):
            #splitline = line.split(None, 2) # definevalue can have spaces so max of 2 splits., None defaults to whitespace
            splitline = line.split(None, 3) # definevalue can have spaces so max of 3 splits to accommodate flag 4/7/09, None defaults to whitespace
            #print(splitline)
            flag = splitline[1]
            definename = splitline[2] #used to be 1
            definevalue = ""
            if len(splitline) > 3: #used to be 2
                definevalue = splitline[3] #used to be 2
            newline = line
            formainline = line
            definevalue = definevalue.strip()
            #print("definedvalue = %s, len(xx) = %s"%(definevalue, len(definevalue)))
            if definevalue.startswith("\""): #if starts with quotes
                definevalue, defcount = mod_hexify.obfs( definevalue[1:len(definevalue) -1], flag ) #understood, what's up with the -1, should be -2 to take off quotes . . .
                #newline = "extern char %s[] = %s;" %(definename, definevalue) 
                newline = "extern unsigned char %s[%s];" %(definename, defcount) #understood
                formainline = "unsigned char %s[] = %s;" %(definename, definevalue); #understood, definevalue is now hexified *********************CHANGE TO CORRECT TYPE*****************
                forfunc += "\tcl_string(%s, %s);\n" %(definename, defcount) #understood
            #print newline
            newheaderfile += newline + "\n"
            formain += formainline + "\n"

    newheaderfile += "\n#endif\n\n"

    newheaderfilemain += formain
    newheaderfilemain += "void init_crypto_strings();"
    newheaderfilemain += "\n#endif\n\n"
    
    forfunc += "}\n"
 
    file = open("crypto_proj_strings.h", "w")
    file.write(newheaderfile)
    file.close()
    
    file = open("crypto_strings_main.h", "w")
    file.write(newheaderfilemain)
    file.close()
    
    file = open("init_crypto_strings.c", "w")
    file.write("#include \"string_utils.h\"\n")
    file.write("#include \"crypto_proj_strings.h\"\n")
    file.write(forfunc)
    file.close()

    

if __name__ == "__main__":
    main()
    
