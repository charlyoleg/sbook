sbook
=====

Inline phone directory.  
This idea is to get a tool similar to 'grep' but working on paragraph instead of line.  
Write the information you want to access quickly in simple text files and grab them with a simple inline command.


Examples
--------

* Who are my friends called robert?  
  
        $ sbook.sh charli  
          
        1:  
        charli oleg  
        12/05/1955  
        06 55 54 44 55  
        2 rue des champs elysee  
        Paris  
        friend/pianist  
          
        Found entries: 1  

* Who are my friends who have their birthday in december?   
           
        $ sbook.sh /12/   
            
        1:  
        robert guillot  
        05/12/1960  
        3 rue du chemin vert  
        63000 trifouilly  
        friend  
          
        Found entries: 1  

Setup sbook
-----------

1. Write the text files containing your data.  
   One paragraph per entry. You can add comment with '#'
2. Edit the bash file sbook.sh  
   Adapt the text file paths.
3. Make sure sbook.sh is in your $PATH directories
4. Use sbook.sh

Use sbook
---------
Which paragraphs contain robert ?  
      
    $ sbook.sh robert

Which paragraphs contain robert AND thierry ?
      
    $ sbook.sh robert thierry

Which paragraphs contain rob OR rol ?
      
    $ sbook.sh rob\|rol

Which paragraphs contain (rob OR rol) AND thierry ?
      
    $ sbook.sh rob\|rol thierry

The arguments of -g have the same meaning of the script arguments.
      
    $ sbook.sh -g rob\|rol -g thierry

Which paragraphs contain (rob OR rol) but NOT thierry ?
      
    $ sbook.sh -g rob\|rol -v thierry

Add the data file name to know where data come from.
      
    $ sbook.sh -g rob\|rol -v thierry -a

Non-regression-test
-------------------

    $ ./check_sbook.sh

License
-------
GLP v3

