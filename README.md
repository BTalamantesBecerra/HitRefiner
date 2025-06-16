# HitRefiner

HitRefiner is a Python-based tool developed to improve the identification of coding genes from BLAST results by resolving multiple non-overlapping hits along the same contig. This allows for a more comprehensive in-silico safety assessment in genomic datasets.

<br>

##**Features**

Filters BLAST output using customizable thresholds: Percentage overlap, Bit score and Percentage identity

Resolves multiple non-overlapping hits per contig

Removes redundant overlapping alignments

Outputs: Filtered results, Region-resolved hits, Version without raw sequences

<br>

Input Requirements

The input BLAST file must be in tabular format (outfmt 6) with the following 19 columns in this exact order:

    qseqid  sacc  stitle  qseq  sseq  nident  mismatch  pident  length  evalue  bitscore  qstart  qend  sstart  send  gapopen  gaps  qlen  slen

This tool supports both nucleotide (BLASTn) and protein (BLASTx) alignments, as long as the input file follows this format.

Make sure to use the correct -outfmt specification in your BLAST command, for example:

    blastx -query input.fasta -db proteins.fasta \
        -out results/sampleBLAST.txt \
        -outfmt '6 qseqid sacc stitle qseq sseq nident mismatch pident length evalue bitscore qstart qend sstart send gapopen gaps qlen slen'

<br>
**Usage**

    python3 HitRefiner.py \
      -a <input_file> \
      -b <output_directory> \
      -c <output_file_prefix> \
      -d <percentage_overlap> \
      -e <bit_score> \
      -f <subquery_overlap_threshold> \
      -g <percentage_identity>

Example:

    python3 HitRefiner.py \
      -a results/sampleBLAST.txt \
      -b results/ \
      -c refined_sample \
      -d 0.7 -e 50 -f 0.7 -g 90

<br>

##**Dependencies**

Python 3.x

<br>


**Dependencies**

    Python 3.x


🧪 Example Tutorial

To help you get started, this repository includes a sample input file:

example_input: dfvf_db_A-oryzae-1674BLAST.txt
This file contains BLASTx results comparing contigs from A. oryzae to the DFVF virulence factor database.
▶️ Step-by-Step

    Clone the repository:

git clone https://github.com/BTalamantesBecerra/HitRefiner.git
cd HitRefiner

Run the script:

    python3 HitRefiner.py \
      -a path_to_input_file/dfvf_db_A-oryzae-1674BLAST.txt \
      -b path_to_output_directory/ \
      -c dfvf_db_refined_A-oryzae-1674 \
      -d 0.7 -e 50 -f 0.7 -g 90

    Output Files:

        dfvf_db_refined_A-oryzae-1674_filtered_by_PercOverlap_BitScore.txt
        → Filtered by overlap, bitscore, and identity

        dfvf_db_refined_A-oryzae-1674_filtered_by_SQseqID.txt
        → Resolves non-overlapping regions per contig

        dfvf_db_refined_A-oryzae-1674_filtered_by_SQseqID_without_sequences.txt
        → Final filtered output (sequences removed)

📊 Parameters Summary
Parameter	Description	Example
-d	Minimum percentage overlap	0.7
-e	Minimum bitscore	50
-f	Sub-query overlap threshold	0.7
-g	Minimum percentage identity	90
