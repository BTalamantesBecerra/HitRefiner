# HitRefiner

HitRefiner is a Python-based tool developed to improve the identification of coding genes from BLAST results by resolving multiple non-overlapping hits along the same contig. This allows for a more comprehensive in-silico safety assessment in genomic datasets.

Features

Filters BLAST output using customizable thresholds:

    Percentage overlap

    Bit score

    Percentage identity

Resolves multiple non-overlapping hits per contig

Removes redundant overlapping alignments

Outputs:

    Filtered results

    Region-resolved hits

    Version without raw sequences


Input Requirements

The input BLAST file must be in tabular format (outfmt 6) with the following 19 columns in this exact order:

    qseqid  sacc  stitle  qseq  sseq  nident  mismatch  pident  length  evalue  bitscore  qstart  qend  sstart  send  gapopen  gaps  qlen  slen

This tool supports both nucleotide (BLASTn) and protein (BLASTx) alignments, as long as the input file follows this format.

Make sure to use the correct -outfmt specification in your BLAST command, for example:

    blastx -query input.fasta -db proteins.fasta \
        -out results/sampleBLAST.txt \
        -outfmt '6 qseqid sacc stitle qseq sseq nident mismatch pident length evalue bitscore qstart qend sstart send gapopen gaps qlen slen'


Usage

    python3 blast_hit_refiner.py \
      -a <input_file> \
      -b <output_directory> \
      -c <output_file_prefix> \
      -d <percentage_overlap> \
      -e <bit_score> \
      -f <subquery_overlap_threshold> \
      -g <percentage_identity>

Example:

    python3 blast_hit_refiner.py \
      -a results/sampleBLAST.txt \
      -b results/ \
      -c refined_sample \
      -d 0.7 -e 50 -f 0.7 -g 90

Dependencies

Python 3.x




