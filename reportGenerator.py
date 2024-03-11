#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:59:53 2023

@author: jon
"""
"""
    This program is used to read a file and use the file in order to generate 
    a report which displays the columns the user requests.
    
    This program uses pandas functions
    
    This is done by using the createFrame definition which addresses what the 
    program does. Then asks the user to input the file name. Then the program 
    asks the user to input the separator for the different columns the customer
    can select. After defining the separator, the program repeats the file name
    as well as the separator. Then the program reads the file name with the 
    separators. 
    
    Definition selectColumns now begins. The program instructs the user to
    select columns for the report. As well as lists the available column names
    with the separator. The program then instructs the user to type the column
    names in the order the user wishes they would appear. Also gives the user 
    the choice to enter 'All' in order to print all available columns. Also 
    asks the user to separate all requested columns with commas. Now the 
    program will repeat what columns will appear in the correct order. 
    
    Definition generateReport now begins. The program states that it is 
    generating the report and clarifies that this is the requested report which
    includes 100 rows of data. The program then locks the column length to 100
    rows. Finally the program prints 100 rows of data from the columns 
    requested.
"""

#Pandas is used in ALL THREE FUNCTIONS, so we will import it only ONCE...
import pandas as pd

def createFrame( ) -> pd.DataFrame: #defining createFrame
    
    '''
        1. Prompt user for file name
        2. Prompt user for separator character/char sequence
             If no separator offered, default to comma
        3. "Mirror" input back to user
        4. Create DataFrame object based on input file
    '''
    
    print( "Select File and File format for Processing." ) #Message
    
    #1
    fileName = input( "Enter the name of the input file with extension: " )
    
    #Ask user about separator value...
    separator = input( "Enter the separator character(s): " )
    
    #Just in case the user did not enter a separator...
    if( len( separator ) == 0 ): #check separator
        separator = ',' #separator
    #End function
    
    #mirror inputback to user
    print( "The file you have selected for reporting is: \t%s" % fileName )
    print( "You have indicated that the separator is: \t%s" % separator ) 
    
    #create the DataFrame
    outFrame = pd.read_csv( fileName, 
                            sep    = separator, 
                            engine = 'python')
    
    #return the DataFrame to the caller
    return outFrame

#End of FUNCTION createFrame

#=============================================================================

def selectColumns( inFrame: pd.DataFrame ) -> list:
    print( )
    print( "Select columns for reporting." )
    
    #Retrieve list of COLUMN NAMES
    colList = inFrame.columns
    
    print( "These are the available COLUMN NAMES: " )
    print( colList )
    
    #Promput user for column names
    print( "\nType in the column names in the order you wish them to appear." )
    print( "Or, if you want all columns, type 'All'. " )
    
    selection = input( "Please separate names with commas: \n" )
    
    #Mirror input to the user
    print( )
    print( "The following columns will appear in this order: " )
    print( selection )
    
    
    if ( selection == "All" ): #checks if selection is all
        outList = colList
    else: #uses regex to check which columns to display 
        import re
        regEx = ", |,|\n"
        outList = re.split( regEx,
                            selection)
    #end selection
    
    return outList

#end function createSelection

#=============================================================================

def generateReport( inFrame: pd.DataFrame, #define generateReport
                    inList : list ):  #No Return
    
    print( )
    print( "Generating your report..." )
    print( "\n\n" )
    print( "\t\tRequested Report, 100 Rows of Data" )
    print( "\t\t----------------------------------" )
    
    # We are using the 100 Row Limit for OUR convenience.
    # It would be better to ASK the USER how much data they want...
    rptView = inFrame.loc[ : 99, inList ]
    
    with pd.option_context( 'display.max_rows',    None,
                            'display.max_columns', None ):
        print( rptView )
    #end CONTEXT
    
#end function generateReport

#=============================================================================
#                            CODE TO TEST FUNCTION

myFrame = createFrame()

selection = selectColumns( myFrame )

#The last function DOES NOT RETURN A VALUE, so we don't need to 'catch' 
generateReport( myFrame, 
                selection )
