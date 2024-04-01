import requests
import os
import zipfile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def main():
    # Create folder for download
    target_path = os.getcwd() + '\\downloads'
    print(target_path)
    
    if os.path.exists(target_path) == False:
        os.mkdir(target_path)
    
    # Download
    '''
    for u in download_uris:
        filename = u.split(sep = '/')[-1]
        try:
            r = requests.get(u)
            with open(target_path + '\\' + filename, 'wb') as f:
                f.write(r.content)
        except:
            print(u + ' could not be downloaded.')
        exit

    print('Download completed.')
    '''
    
    # Unzip
                
    for dirpath, dirnames, files in os.walk(target_path):
        for f in files:
            if f.split('.')[-1] == 'zip':
                try:
                    with zipfile.ZipFile(dirpath + '\\' + f, 'r') as zip_ref:
                        zip_ref.extractall(dirpath)
                    print(f)      
                    os.remove(dirpath + '\\' + f)   
                    print(f + ' extracted and removed.')                   
                except:
                    print(f + ' could not be extracted. Possibly invalid file.')    
                '''
                try:
                    os.remove(dirpath + '\\' + f)    
                except:
                    print(f + ' could not be deleted. Possibly permission missing.')  
                ''' 
    print('Unzipping completed.')    
    
'''
    files = os.walk(target_path)
    print(files)
    
    for f in files:
        filepath = os.path.join(target_path, files)
        if filepath.split('.')[-1] == 'zip':
                with zipfile.ZipFile(filepath, 'r') as zip_ref:
                    zip_ref.extractall(dirpath)
                    os.remove(filepath)
    '''

if __name__ == "__main__":
    main()
