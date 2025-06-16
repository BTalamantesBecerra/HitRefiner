import sys, getopt
import os

def main(argv):
    
    #Variables
    
    a_BLAST_input_path_and_file = ""
    b_output_path_ = ""
    c_output_file_name = "_filtered"

    #filtering parameters

    d_percentage_overlap = ""
    e_bitscore = ""
    f_subQueryOverlapThreshold = ""
    g_min_pident = ""
    

    try:
        opts, args = getopt.getopt(argv, "a:b:c:d:e:f:g:", [
                                                    "a_BLAST_input_path_and_file=",
                                                    "b_output_path_=",
                                                    "c_output_file_name=",
                                                    "d_percentage_overlap=",
                                                    "e_bitscore=",
                                                    "f_subQueryOverlapThreshold=",
                                                    "g_min_pident ="])

    except getopt.GetoptError:
        
        print("ERROR:")
        print("CHECK INPUT HANDLES")
        print("filtering_MT1H2.py -a <a_BLAST_input_path_and_file> -c <c_output_file_name> -d <d_percentage_overlap> -e <e_bitscore> -f <f_subQueryOverlapThreshold> -g <g_min_pident>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h'):
            print ("HELP")
            print ("Use this commandline => filtering_MT1H.py -a <a_BLAST_input_path_and_file>  -c <c_output_file_name> -d <d_percentage_overlap> -e <e_bitscore> -f <f_subQueryOverlapThreshold> -g <g_min_pident>")
            sys.exit()

        elif opt in ("-a", "--a_BLAST_input_path_and_file"):
            a_BLAST_input_path_and_file = arg
            
        elif opt in ("-b", "--b_output_path_"):
            b_output_path_ = arg
            
        elif opt in ("-c", "--c_output_file_name"):
            c_output_file_name = arg
            
        elif opt in ("-d", "d_percentage_overlap"):
            d_percentage_overlap = float(arg)
            
        elif opt in ("-e", "e_bitscore"):
            e_bitscore = int(arg)
            
        elif opt in ("-f", "f_subQueryOverlapThreshold"):
            f_subQueryOverlapThreshold = float(arg)
         
        elif opt in ("-g", "--g_min_pident"):
            g_min_pident = float(arg)



    print('\n')
    print("Input file : " + a_BLAST_input_path_and_file)
    print("Output file path : " + b_output_path_)
    print("Output File name : " + c_output_file_name)
    print("Pergentage overlap : " + str(d_percentage_overlap))
    print("BitScore : " + str(e_bitscore))
    print("SubQueryOverlapThreshold : " + str(f_subQueryOverlapThreshold))
    print("PercentageIdentity : " + str(g_min_pident))

    print('\n')

    #Adding indexes to each BLAST column

    qseqid = 0
    sacc = 1
    stitle = 2
    qseq = 3
    sseq = 4
    nident = 5
    mismatch = 6
    pident = 7
    length = 8
    evalue = 9
    bitscore = 10
    qstart = 11
    qend = 12
    sstart = 13
    send = 14
    gapopen = 15
    gaps = 16
    qlen = 17
    slen = 18
    PercentageOverlapINT = 19
    SubQseqID = 20
    qseq_subQseq  = 21


    #Opening a new file

    BLAST_OUTPUT_FILE_NAME = a_BLAST_input_path_and_file

    Input_BLAST_file = open(BLAST_OUTPUT_FILE_NAME, 'r')
    filtered_file = os.path.join(b_output_path_, c_output_file_name + "_filtered_by_PercOverlap_BitScore.txt")
    filtered_files_to_write = open(filtered_file, "w+")


    #Write headers into the new file

    AllHeadersToWriteIntoTheFile = ""
    AllHeadersToWriteIntoTheFile = ( "qseqid" + '\t' + "sacc" + '\t' + "stitle" + '\t' +
                                   "qseq" + '\t' + "sseq" + '\t' + "nident" + '\t' + "mismatch"+ '\t' +
                                   "pident" + '\t' + "length" + '\t' + "evalue"+ '\t' +
                                   "bitscore" + '\t' + "qstart" + '\t' + "qend" + '\t' + "sstart" + '\t' +
                                   "send" + '\t' + "gapopen" + '\t' + "gaps" + '\t' +
                                   "qlen"+ '\t' + "slen" + '\t' + "PercentageOverlap" + '\n')

    filtered_files_to_write.write(AllHeadersToWriteIntoTheFile)

    #Reading BLAST files

    tempstring = "temp"
    while tempstring:
        tempstring = Input_BLAST_file.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist=x.split('\t')

        BLAST_columns_to_read = (rowlist[qseqid] + '\t' + rowlist[sacc] + '\t' + rowlist[stitle]+ '\t' +
                   rowlist[qseq]+ '\t' + rowlist[sseq]+ '\t'  + rowlist[nident]+ '\t' + rowlist[mismatch]+ '\t' +
                   rowlist[pident] + '\t' + rowlist[length] + '\t' + rowlist[evalue]+ '\t' +
                   rowlist[bitscore]+ '\t' + rowlist[qstart]+ '\t' + rowlist[qend]+ '\t' + rowlist[sstart]+ '\t' +
                   rowlist[send] + '\t' + rowlist[gapopen] + '\t' + rowlist[gaps]+ '\t' +
                   rowlist[qlen]  + '\t' + rowlist[slen] + '\t')
        

        #Calculation of the Percentage Overlap

        Query_length = int(rowlist[qlen])
        Length = int(rowlist[length])
        SubjectLength = int(rowlist[slen])
        min_length = min(Query_length, SubjectLength)
        perc_overlap = (Length / min_length)

        

        #Appending Percentage overlap to the last column of the output file

        rowlist.append(str(perc_overlap))
        

        BLAST_columns_to_read += rowlist[PercentageOverlapINT] + '\n' 

    
        #Filter by and write output by Percentage overlap and bitscore

        if float(rowlist[PercentageOverlapINT]) >= d_percentage_overlap:
            if float(rowlist[bitscore]) >= e_bitscore:
                if float(rowlist[pident]) >= g_min_pident:
                    filtered_files_to_write.write(BLAST_columns_to_read)




    #Close files
    Input_BLAST_file.close()
    filtered_files_to_write.close()


    #################################################
    filtered_file_1_reopen = open(filtered_file, 'r')
    filtered_file_2 = os.path.join(b_output_path_, c_output_file_name + "_filtered_by_SQseqID.txt")
    filtered_files_by_alingments = open(filtered_file_2, "w")

    #Write headers to the second file adding subseq ID
    
    AllHeadersToWriteIntoTheFile2 = ""
    AllHeadersToWriteIntoTheFile2 = ( "qseqid" + '\t' + "sacc" + '\t' + "stitle" + '\t' +
                                   "qseq" + '\t' + "sseq" + '\t' + "nident" + '\t' + "mismatch"+ '\t' +
                                   "pident" + '\t' + "length" + '\t' + "evalue"+ '\t' +
                                   "bitscore" + '\t' + "qstart" + '\t' + "qend" + '\t' + "sstart" + '\t' +
                                   "send" + '\t' + "gapopen" + '\t' + "gaps" + '\t' +
                                   "qlen"+ '\t' + "slen" + '\t' + "PercentageOverlap" + '\t' + "subqseqid" + '\t' + "qseq_subqseq" +'\n')


    filtered_files_by_alingments.write(AllHeadersToWriteIntoTheFile2)

    
    #SORTING AND READING ALINGMENT FILES

    lst_lst = []
    counter = 0
    

    tempstring = "temp"
    while tempstring:
        tempstring = filtered_file_1_reopen.readline()
        if tempstring == "":
            break
        if counter != 0:
            templine = tempstring.splitlines()
            x = templine[0]
            rowlist_SQseqID = x.split('\t')
            lst_lst.append(rowlist_SQseqID)

        counter += 1
        




    #reading the list of lists
        #SORTING BY QUERY SEQ ID AND QUERY START
     
    list.sort(lst_lst, key = lambda DataRow_1: (DataRow_1[qstart]), reverse=False)
    list.sort(lst_lst, key = lambda DataRow_0: (DataRow_0[qseqid]), reverse=False)

    #create an index for the subquery Seq ID

    subIndex = 0
    temp_qseqID = ""
    temp_qstart = 0
    temp_qend = 0
    temp_slen = 0



    
    #Create a loop to read through lst_lst

    length_of_list = len(lst_lst)
    for p in range(length_of_list):
        temp_rowlist1 = lst_lst[p]
        temporary_rowlist1_length = len(temp_rowlist1)
        if temporary_rowlist1_length !=20:
            continue


        current_QSEQ_ID = temp_rowlist1[qseqid]
        if temp_qseqID == current_QSEQ_ID:
            current_qstart = temp_rowlist1[qstart]
            current_qend = temp_rowlist1[qend]
            current_slen = temp_rowlist1[slen]
            
            x = range(int(temp_qstart), int(temp_qend))
            y = range(int(current_qstart), int(current_qend))
            
            z = list(set(x) & set(y))
            w = min(set(x), set(y))

            min_slen = min(current_slen, temp_slen)
            
            #print(w)
            overlap_length = len(z)
                        
            #Calculation of overlap proportion and sub index threshold

            overlap_proportion = 0

            if int(min_slen) != 0:
                overlap_proportion = (int(overlap_length) / int(min_slen) )

            if float(overlap_proportion) < f_subQueryOverlapThreshold:
                subIndex += 1                

            temp_rowlist1.append(str(subIndex))
            temp_rowlist1.append(str(current_QSEQ_ID) + "_" + str(subIndex)) 
            temp_qstart = temp_rowlist1[qstart]
            temp_qend = temp_rowlist1[qend]
            temp_slen = temp_rowlist1[slen]
            
        
        else:
            subIndex = 0
            temp_qseqID = current_QSEQ_ID
            temp_qstart = temp_rowlist1[qstart]
            temp_qend = temp_rowlist1[qend]
            temp_slen = temp_rowlist1[slen]
            temp_rowlist1.append(str(subIndex))
            temp_rowlist1.append(str(current_QSEQ_ID) + "_" + str(subIndex))


            
    #Sorting by pident, percentage overlap, bitscore and QseqID_subIndex
            

    list.sort(lst_lst, key = lambda DataRow_2: float(DataRow_2[pident]), reverse=True)
    list.sort(lst_lst, key = lambda DataRow_3: float(DataRow_3[PercentageOverlapINT]), reverse=True) 
    list.sort(lst_lst, key = lambda DataRow_4: float(DataRow_4[bitscore]), reverse=True)
    list.sort(lst_lst, key = lambda DataRow_5: DataRow_5[qseq_subQseq])

    dictionary_lst_lst = {}
   
    #loop through lst_lst and build each output string and write it to the output file

    length = len(lst_lst)
    for i in range(length):
        temp_rowlist = lst_lst[i]
        temp_rowlist_length = len(temp_rowlist)
        if float(temp_rowlist[pident]) < g_min_pident:
            continue

        
        #Note, the number of columns is hardcoded for 22 this needs to be bundled with BLASTn
        if temp_rowlist_length != 22:
            print("length of the tem_row_list_is:")
            print(temp_rowlist_length)
            continue

        row_string_for_output = ""
        
        Variable_qseqid_subindex = temp_rowlist[qseq_subQseq] 

        try:
            for j in range(temp_rowlist_length -1):
                temp_string = temp_rowlist[j]
                row_string_for_output += (temp_string + "\t")

            row_string_for_output += temp_rowlist[(temp_rowlist_length) - 1]
            row_string_for_output += "\n"

        except IndexError:
            print ("Exception thrown")

        Tuple_rowlist = (Variable_qseqid_subindex, row_string_for_output)

        if Variable_qseqid_subindex in dictionary_lst_lst:
            pass

        else:
            dictionary_lst_lst[Variable_qseqid_subindex] = row_string_for_output
            filtered_files_by_alingments.write(row_string_for_output)


    #Close files
    filtered_file_1_reopen.close()
    filtered_files_by_alingments.close()

    # ==============================
    # Step 3: Remove qseq and sseq from final filtered output
    # ==============================

    def remove_qseq_sseq(input_file, output_file):
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            header = infile.readline().strip().split('\t')
            
            # Identify the indices of qseq and sseq
            qseq_index = header.index("qseq")
            sseq_index = header.index("sseq")

            # Create a new header excluding qseq and sseq
            new_header = [col for i, col in enumerate(header) if i not in (qseq_index, sseq_index)]
            outfile.write('\t'.join(new_header) + '\n')

            for line in infile:
                parts = line.strip().split('\t')
                new_parts = [val for i, val in enumerate(parts) if i not in (qseq_index, sseq_index)]
                outfile.write('\t'.join(new_parts) + '\n')

    # Define output file for the version without sequences
    filtered_file_3 = os.path.join(b_output_path_, c_output_file_name + "_filtered_by_SQseqID_without_sequences.txt")

    # Run the sequence-stripping step
    remove_qseq_sseq(filtered_file_2, filtered_file_3)

    print(f"Final file without sequences written to:\n{filtered_file_3}")



if __name__ == "__main__":
    main(sys.argv[1:])

