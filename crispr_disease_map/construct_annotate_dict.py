import json
import os.path

import pandas as pd

from glob import glob
from pprint import pprint

annotation_data_folder = 'data/external/'
counts_data_folder = 'data/processed_counts_external/'
annotate_dict_output_folder = 'data/dict_annotation/'


if __name__ == "__main__":
    print(annotation_data_folder + '*.tsv')

    replicate_to_sample = {}
    replicate_to_filename = {}
    sample_to_annotation = {}
    for file in glob(annotation_data_folder + '*.xlsx'):
        print(file)
        df = pd.read_excel(file, 'Sample details')
        
        for replicate, sample, treatment, dose, days_grown, cell_line, ko in \
            zip(df['Replicate'], df['Sample'], df['Treatment'], df['Dose'], df['Days grown'], df['Cell line'], df['KO']):
            
            replicate_to_sample[replicate] = sample

            filename = os.path.basename(file).replace('.xlsx', '.counts.tsv')
            assert(os.path.isfile(counts_data_folder + filename))
            replicate_to_filename[replicate] = filename
            
            sample_to_annotation[sample] = {'Replicate': replicate,
                                            'Sample': sample,
                                            'Treatment': treatment,
                                            'Dose': dose,
                                            'Days grown': days_grown,
                                            'Cell line': cell_line,
                                            'KO': ko}

    # pprint(replicate_to_sample)
    # pprint(sample_to_annotation)

    with open(annotate_dict_output_folder + 'replicate_to_sample.json', "w") as outfile:
        outfile.write(json.dumps(replicate_to_sample, indent=4))

    with open(annotate_dict_output_folder + 'sample_to_annotation.json', "w") as outfile:
        outfile.write(json.dumps(sample_to_annotation, indent=4))

    with open(annotate_dict_output_folder + 'replicate_to_filename.json', "w") as outfile:
        outfile.write(json.dumps(replicate_to_filename, indent=4))