def run_sam(arguments): 
    import os
    import subprocess   
    from time import time
    from src.colors import bcolors


    start_time = time()
    
    print(f'''[ Running ] Samtools''',end=' ')

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
    with open(os.path.join(arguments['project'],"report.idxstat"), "w") as file:
        file.write('Reference gene\tReference sequence length\tMapped read count\tUnmapped read count\n')
    with open(os.path.join(arguments['project'],"report.idxstat"), "a") as file:
        subprocess.run(cmd, stdout=file)

    # Optional arguments
    if arguments['stats'] : 
        cmd=['samtools','flagstat',bam_sorted]
        with open(os.path.join(arguments['project'],"alignment.log"), "w") as file:
            subprocess.run(cmd, stdout=file)

    if arguments['depth'] :    
        cmd=['samtools','depth', bam_sorted]
        with open(os.path.join(arguments['project'],"depth.tsv"), "w") as file:
            subprocess.run(cmd, stdout=file)

    end_time = time()
    elapsed_time = end_time - start_time
    
#    print(f'''{bcolors.GREEN}[  Done   ]{bcolors.ENDC} in {elapsed_time/60:5.2f} minutes\n''')
    # Lots of TABS to align [ Done ]
    print(f'''{bcolors.GREEN}\t\t\t[ Done ]{bcolors.ENDC}\n''')


def write_summary_sam(arguments) :

    bam = arguments['sam'].split('.sam')[0]+'.bam'
    bam_sorted=arguments['sam'].split('.sam')[0]+'_sorted.bam'   

    print(f'''
        ####################
        # Samtools Summary #
        ####################

          Project : {arguments['project']}
         Run Mode : {arguments['run_mode']}
  Input Alignment : {arguments['sam']}

Alignment Outputs
-----------------------------------------------------------
         SAM->BAM : {bam}
       Sorted BAM : {bam_sorted}
        BAM index : {bam_sorted}.bai
 Alignment Report : {arguments['project']}/report.idxstat
 Alignment Report : {arguments['project']}/report.html
  Alignment Depth : {arguments['project']}/depth.tsv
    Alignment Log : {arguments['project']}/alignment.log

''')


def report_sam(arguments):
    import os
    import pandas  as pd
#    import seaborn as sns
#    from matplotlib import pyplot as plt
    import plotly.express as px
    import plotly.graph_objects as go

    df = pd.read_table(os.path.join(arguments['project'],'report.idxstat'))
#    df =  pd.read_table(os.path.join(arguments['project'],'report.idxstat'),header=None)
#    df.columns=['Reference gene','Reference sequence length','Mapped read count','Unmapped read count']

    df.apply(pd.to_numeric, errors='ignore')

    df['Percentage of Mapped reads']=(df['Mapped read count']*100)/df['Mapped read count'].sum()  

    df_toplot=df[df['Percentage of Mapped reads'] > arguments['sam_report_cutoff']]

    px.pie(df_toplot, 
        values='Percentage of Mapped reads', 
        names='Reference gene', 
        title='Percentage of mapped reads')

    common_props = dict(labels=df_toplot['Reference gene'],
                        values=df_toplot['Percentage of Mapped reads'])
    fig = go.Figure(data=[go.Pie(common_props,
                                textposition='outside')])

    fig.update_traces(marker=dict(line=dict(color='white', width=2)))

    #    fig.show()
    fig.write_image(os.path.join(arguments['project'],'report.pdf'))
    fig.write_html( os.path.join(arguments['project'],'report.html'))
