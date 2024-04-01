import requests
#from requests_html import HTMLSession
import pandas


def main():
    #1. Attempt to web scrap/pull down the contents of `https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/`
    url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'


    def save_html(html, path):
        with open(path, 'wb') as f:
            f.write(html)
        
    #r = requests.get(url)
    #save_html(r.content, 'ncei_filelist')
        
    #2. Analyze it's structure, determine how to find the corresponding file to `2022-02-07 14:03` (Anne: Updated to '2024-01-19 10:06') using Python.
    date = '2024-01-19' # 10:06'
    
    with open('ncei_filelist', 'r') as file:
    matched_lines = [line for line in my_string.split('\n') if "substring" in line]
    
    
    with open('ncei_filelist', 'r') as file:
        # read all lines in a list
        lines = file.readline()
        for line in lines:
            # check if string present on a current line
            if line.find(date) != -1:
                print(date, 'File for this date found at')
                print('Line Number:', lines.index(line))
                print('Line:', line)
                
    #3. Build the `URL` required to download this file, and write the file locally.
    
    
    #4. Open the file with `Pandas` and find the records with the highest `HourlyDryBulbTemperature`.
    #5. Print this to stdout/command line/terminal.
    pass


if __name__ == "__main__":
    main()
