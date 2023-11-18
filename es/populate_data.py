import os
import json
from .es_utils import save_to_es
from .utils import time_the_process

# supposed json files are stored in /transcripts folder
transcripts_path = 'transcripts'

@time_the_process
def populate_transcripts():
    files = os.listdir(transcripts_path)
    failed_files = []
    for file in files:
        if file.endswith(".json") is False:
            continue
        [is_saved, file] = load_and_save_data(file)
        if is_saved is False:
            failed_files.append(file)
    
    print('Number of files: ', len(files))
    print('Number of failed files: ', len(failed_files))
    print('Failed files: ', failed_files)

    
def load_and_save_data(file):
    print('Processing file: ', file)
    is_saved = False
    with open(os.path.join(transcripts_path, file)) as f:
        file_name = file.split('.')[0]
        source_data = json.load(f)
        data = {
            'transcript': source_data['results']['transcripts'][0]['transcript'],
            'file_name': file_name,
        }
        try:
            save_to_es(data)
            is_saved = True
            print('{} .Data saved successfully'.format(file))
        except Exception as e:
            print(e)
            print('{} .Data was not saved'.format(file))
    return [is_saved, file]