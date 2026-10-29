import terminalnexus
import subprocess
import sys
import os
from pprint import pprint
import multiprocessing
import warnings
from mpire import WorkerPool

def create_awesome_color_text(text,hexcode):
    results = terminalnexus.set(f"{hexcode}") + f"{text}" + terminalnexus.reset()
    return results

def create_awesome_color_texts(list_of_texts,hexcode,progress_bar):
    results = []
    for text in list_of_texts:
        my_dict = {
            "text":text,
            "hexcode":hexcode
        }
        results.append(my_dict)
    num_cores = max(multiprocessing.cpu_count()//2,1)
    with WorkerPool(n_jobs=num_cores,daemon=False) as pool:
        results = pool.map(create_awesome_color_text,results,progress_bar=progress_bar)
    return results

def print_results(results):
    NEWLINE = "\n"
    for result in results:
        print(result)
        print(NEWLINE)

if __name__=="__main__":
    
    list_of_texts = [
        "Hello"*100,
        "World"
    ]
    hexcode = "ff0000"
    progress_bar = True
    results = create_awesome_color_texts(list_of_texts,hexcode,progress_bar)
    print_results(results)

    list_of_texts = [
        "Hello",
        "World"*100
    ]
    hexcode = "00ff00"
    progress_bar = True
    results = create_awesome_color_texts(list_of_texts,hexcode,progress_bar)
    print_results(results)

    list_of_texts = [
        "Hello"*100,
        "World"*100
    ]
    hexcode = "000000"
    progress_bar = True
    results = create_awesome_color_texts(list_of_texts,hexcode,progress_bar)
    print_results(results)
