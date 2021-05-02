# -*- coding: utf-8 -*-
import os, sys, time
import base64

def getBase64EncodedString(input_string):
    urlSafeEncodedBytes = base64.urlsafe_b64encode(input_string.encode('utf-8'))
    return str(urlSafeEncodedBytes, 'utf-8')

def getBase64DecodedString(input_string):
    decodedBytes = base64.urlsafe_b64decode(input_string)
    return str(decodedBytes, 'utf-8')

def doesPathExist(path):
    return os.path.exists(path)

def getFileListFromDir(path):
    for root, dirs, files in os.walk(path):
        return files
    return None

def doPathsContainSameFiles(path1, path2):
    files1 = getFileListFromDir(path1)
    files2 = getFileListFromDir(path2)
    return doHashesContainSameObjects(files1, files2)

def getItemsInPath(input_path, itemType='files'):
    if doesPathExist(input_path):
        for root, dirs, files in os.walk(input_path):
            if itemType == 'files':
                return files
            elif itemType == 'dirs':
                return dirs
            else:
                return root
    return None

def getFilesInDirectory(input_path):
    return getItemsInPath(input_path)

def getDirsInDirectory(input_path):
    return getItemsInPath(input_path, 'dirs')

def readFileAsOneString(input_file, replaceNewLines=True):
    if doesPathExist(input_file):
        with open(input_file, 'r') as file:
            data = file.read()
            if replaceNewLines:
                data = data.replace('\n', '')
        file.close()
        return data
    return None

def splitInputFileIntoMultipleFiles(infile, out_dir, batch_size):
    t = time.time()
    reader = open(infile, 'r')
    record_number = 1;
    print("BEGIN Splitting")
    batch_number = 1
    writer = open(out_dir + '/' + str(batch_number), 'w')
    for line in reader.readlines():
        writer.write(line)
        record_number += 1;
        if record_number % batch_size == 0:
            writer.close()
            batch_number += 1
            writer = open(out_dir + '/' + str(batch_number), 'w')
            print("DONE Writing %s records", str(record_number))
            print("\n Time Taken: %.3f sec" % (time.time() - t))
    writer.close()
    end_t = time.time()
    print("\n Time Taken: %.3f sec" % (end_t - t))
    print("DONE Splitting")
    return

