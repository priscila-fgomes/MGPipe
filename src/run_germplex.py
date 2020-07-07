def run_germplex(arguments) :
    """
    This is an automatic run for GermPLEX pannels.
    """

    # Step 1/3 - Setup and run alignment ----------------------------
    from src.run_bowtie2     import set_bowtie2,run_bowtie2

    ## Default parameters for auto mode
    arguments['alignment_mode'] = 'end-to-end'
    arguments['preset']         = 'sensitive'
    
    ## Run
    arguments = set_bowtie2(arguments)
    run_bowtie2(arguments)


    # Step 2/3 - Analyse alignment ----------------------------------
    from src.menu_sam   import menu_sam
    from src.run_sam    import run_sam,report_sam

    arguments['sam']='alignment.sam'

    if not arguments['sam'] :
        arguments['sam'] = menu_sam()

    run_sam(arguments)
    report_sam(arguments)


    # Step 3/3 - MultiQC report -------------------------------------
    from src.run_multiqc     import run_multiqc
    run_multiqc(arguments)

    # Summary
    summary_germplex(arguments)



def summary_germplex(arguments) :
    '''
    Summary for automatic mode
    '''

    bam = arguments['sam'].split('.sam')[0]+'.bam'
    bam_sorted=arguments['sam'].split('.sam')[0]+'_sorted.bam'   

    print(f'''

###########################################################
#    MGPipe   -   GermPLEX automatic run   -   Summary    #
###########################################################

                    Run options
-----------------------------------------------------------
          Project : {arguments['project']}
         Run Mode : {arguments['run_mode']}
        Read Mode : {arguments['read_mode']}
Forward Read (R1) : {arguments['r1']}
Reverse Read (R2) : {arguments['r2']}
   Alignment Mode : {arguments['alignment_mode']}
    Preset Option : {arguments['preset']}

                Alignment Outputs
-----------------------------------------------------------
              SAM : {arguments['sam']}
         SAM->BAM : {bam}
       Sorted BAM : {bam_sorted}
        BAM index : {bam_sorted}.bai
 Alignment Report : {arguments['project']}/species.html
     Genes Report : {arguments['project']}/genes.csv

                Additional Outputs
-----------------------------------------------------------
 Alignment Report : {arguments['project']}/raw_data/report.idxstat
  Alignment Depth : {arguments['project']}/raw_data/depth.tsv
    Alignment Log : {arguments['project']}/log/alignment.log



Open Species report with:
firefox ./{arguments['project']}/species.html

Open MultiQC report with:
firefox ./{arguments['project']}/multiqc_report.html

''')