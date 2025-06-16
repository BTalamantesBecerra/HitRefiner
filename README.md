# HitRefiner

HitRefiner is a Python-based tool developed to improve the identification of coding genes from BLAST results by resolving multiple non-overlapping hits along the same contig. This allows for a more comprehensive in-silico safety assessment in genomic datasets.

<br>

##**Features**

Filters BLAST output using customizable thresholds: Percentage overlap, Bit score and Percentage identity

Resolves multiple non-overlapping hits per contig

Removes redundant overlapping alignments

Outputs: Filtered results, Region-resolved hits, Version without raw sequences

<br>

__Input Requirements__

The input BLAST file must be in tabular format (outfmt 6) with the following 19 columns in this exact order:

    qseqid  sacc  stitle  qseq  sseq  nident  mismatch  pident  length  evalue  bitscore  qstart  qend  sstart  send  gapopen  gaps  qlen  slen

This tool supports both nucleotide (BLASTn) and protein (BLASTx) alignments, as long as the input file follows this format.

Make sure to use the correct -outfmt specification in your BLAST command, for example:

    blastx -query input.fasta -db proteins.fasta \
        -out results/sampleBLAST.txt \
        -outfmt '6 qseqid sacc stitle qseq sseq nident mismatch pident length evalue bitscore qstart qend sstart send gapopen gaps qlen slen'

<br>

__Usage__ 

    python3 HitRefiner.py \
      -a <input_file> \
      -b <output_directory> \
      -c <output_file_prefix> \
      -d <percentage_overlap> \
      -e <bit_score> \
      -f <subquery_overlap_threshold> \
      -g <percentage_identity>

__Example:__

    python3 HitRefiner.py \
      -a results/sampleBLAST.txt \
      -b results/ \
      -c refined_sample \
      -d 0.7 -e 50 -f 0.7 -g 90

<br>
<br>


__Example Tutorial__

To help you get started, this repository includes a sample input file:
<br>

example_input: dfvf_db_A-oryzae-1674BLAST.txt
This file contains BLASTx results comparing contigs from A. oryzae to the DFVF virulence factor database.

Clone the repository:

    git clone https://github.com/BTalamantesBecerra/HitRefiner.git
    cd HitRefiner

Run the script:

    python3 HitRefiner.py \
        -a path_to_input_file/dfvf_db_A-oryzae-1674BLAST.txt \
        -b path_to_output_directory/ \
        -c dfvf_db_refined_A-oryzae-1674 \
        -d 0.7 -e 50 -f 0.7 -g 90

<br>

__Output Files:__

__dfvf_db_refined_A-oryzae-1674_filtered_by_PercOverlap_BitScore.txt__ → Filtered by overlap, bitscore, and identity
<br>
<br>
__dfvf_db_refined_A-oryzae-1674_filtered_by_SQseqID.txt__ → Resolves non-overlapping regions per contig
<br>
<br>
__dfvf_db_refined_A-oryzae-1674_filtered_by_SQseqID_without_sequences.txt__ → Final filtered output (sequences removed)
<br>
<br>

__Suggested Parameters__
<br>
<br>
We recommend to use a pergentage overlap of 70%, minimum bitscore of 40, also keep a subquery thresshold of 70% and a percentage identity of 80% or 90%. These values will depend on how stringent you would like your filtering to be done. 
<br>
A more detailed version of the variables used in the script is shown here: 
<br>
<br>
Parameter	Description	
<br>
<br>
-d	Minimum percentage overlap	0.7
<br>
-e	Minimum bitscore	50
<br>
-f	Sub-query overlap threshold	0.7
<br>
-g	Minimum percentage identity	90

<br>
<br>

**Dependencies**
<br>

Python 3.x

<br>
