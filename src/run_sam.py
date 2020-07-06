def run_sam(arguments): 
    import os
    import subprocess   
    from time import time
    from src.colors import bcolors

    start_time = time()
    # Write summary
    if arguments['run_mode'] != 'auto':
        summary_sam(arguments)


    print(f'''{bcolors.BLUE}[ Running ]{bcolors.ENDC} Alignment analysis (Samtools)''',end='')

    # Update alignment path
    arguments.update({'sam': os.path.join(arguments['project'],arguments['sam'])})

    # Convert .sam to .bam
    bam = arguments['sam'].split('.sam')[0]+'.bam'
    cmd=['samtools','view','-bS',arguments['sam'],'-o',bam]
    subprocess.call(cmd)

    # Sort .bam file.
    bam_sorted=arguments['sam'].split('.sam')[0]+'_sorted.bam'   
    cmd=['samtools','sort',bam,'-o',bam_sorted]
    subprocess.call(cmd)

    # Index the sorted .bam file.
    cmd=['samtools','index',bam_sorted]
    subprocess.call(cmd)

    # Run sam report
    cmd=['samtools','idxstats', bam_sorted]
    with open(os.path.join(arguments['project'],"raw_data","report.idxstat"), "w") as file:
        file.write('Reference gene\tReference sequence length\tMapped read count\tUnmapped read count\n')

    with open(os.path.join(arguments['project'],"raw_data","report.idxstat"), "a") as file:
        subprocess.run(cmd, stdout=file)

    # Optional arguments
    if arguments['stats'] : 
        cmd=['samtools','flagstat',bam_sorted]
        with open(os.path.join(arguments['project'],"log","alignment.log"), "w") as file:
            subprocess.run(cmd, stdout=file)

    if arguments['depth'] :    
        cmd=['samtools','depth', bam_sorted]
        with open(os.path.join(arguments['project'],"raw_data","depth.tsv"), "w") as file:
            subprocess.run(cmd, stdout=file)

    end_time = time()
    elapsed_time = end_time - start_time
    
#    print(f'''{bcolors.GREEN}[  Done   ]{bcolors.ENDC} in {elapsed_time/60:5.2f} minutes\n''')
    # Lots of TABS to align [ Done ]
    print(f'''{bcolors.GREEN}\t[ Done ]{bcolors.ENDC}''')


def summary_sam(arguments) :

    bam = arguments['sam'].split('.sam')[0]+'.bam'
    bam_sorted=arguments['sam'].split('.sam')[0]+'_sorted.bam'   

    print(f'''
        ####################
        # Samtools Summary #
        ####################

          Project : {arguments['project']}
         Run Mode : {arguments['run_mode']}
  Input Alignment : {arguments['project']}/{arguments['sam']}

Alignment Outputs
-----------------------------------------------------------
         SAM->BAM : {arguments['project']}/{bam}
       Sorted BAM : {arguments['project']}/{bam_sorted}
        BAM index : {arguments['project']}/{bam_sorted}.bai
 Alignment Report : {arguments['project']}/species.html
     Genes Report : {arguments['project']}/genes.csv

Additional Outputs
-----------------------------------------------------------
 Alignment Report : {arguments['project']}/raw_data/report.idxstat
  Alignment Depth : {arguments['project']}/raw_data/depth.tsv
    Alignment Log : {arguments['project']}/log/alignment.log

''')


def report_sam(arguments):
    import os
    import sys
    import pandas  as pd
    from matplotlib import pyplot as plt
    import plotly.express as px
    import plotly.graph_objects as go

    df = pd.read_table(os.path.join(arguments['project'],'raw_data','report.idxstat'))
    df2 = pd.read_csv(os.path.join(os.path.dirname(sys.argv[0]),'Index','Organism_genes.csv'))

    df3 = pd.merge(df,df2)
    df3['Percentage of Mapped reads']=(df3['Mapped read count']*100)/df3['Mapped read count'].sum()
    df3 = df3[df3['Mapped read count'] > 0]
    df3.to_csv(os.path.join(arguments['project'],'genes.csv'),index=False)
    df4 = df3.groupby('Organism').sum()
    df4.reset_index(inplace=True)

    df_toplot=df4[df4['Mapped read count'] > 0]
    common_props = dict(labels=df_toplot['Organism'],
                    values=df_toplot['Mapped read count'])
    fig = go.Figure(data=[go.Pie(common_props,
                                textposition='outside')])
    fig.update_traces(marker=dict(line=dict(color='white', width=2)))
    fig.update_layout(title="Percentage of mapped reads")

    #fig.write_image(os.path.join(arguments['project'],'species.pdf'))
    fig.write_html(os.path.join(arguments['project'],'species.html'))
