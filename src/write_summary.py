def write_summary(arguments) :
    print(f'''
###########
# Summary #
###########

          Project : {arguments['project']}

         Run Mode : {arguments['run_mode']}

        Read Mode : {arguments['read_mode']}
Forward Read (R1) : {arguments['r1']}
Reverse Read (R2) : {arguments['r2']}

   Alignment Mode : {arguments['alignment_mode']}
    Preset Option : {arguments['preset']}

 Alignment Output : {arguments['alignment']}
      CPU Threads : {arguments['nt']}

    ''')