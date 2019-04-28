from __future__ import annotations
from typing import Dict, List, Callable
from functools import reduce
import os
import re

class Article:
    required: List[str] = ['T1', 'A1', 'Y1', 'N2']
    csv_fields: List[str] = ['T1', 'A1', 'Y1']
    csv_header: str = 'T1\tA1\tY1'

    def __init__(self, info: Dict[str,str]):
        if not all(list(map(lambda key: key in info, info))):
            raise Exception('Not all data available',info)
        self.info = info

    def to_csv(self):
        return '\t'.join([self.info[key] for key in self.csv_fields])

    def pretty_print(self):
        return '\n\n'.join([self.info[key] for key in self.required])

    def __str__(self):
        return self.pretty_print()

class RISfile:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.articles:List[Article] = []
        self.parse()

    def parse(self):
        with open(self.file_path, 'r') as f:
            fields: Dict[str, str] = {'raw': ''}

            for line in f:
                fields['raw'] += line
                if line.startswith('ER  -'):
                    try:
                        self.articles.append(Article(fields))
                    except:
                        print('Not all data available : '+', '.join(fields.keys()))
                    fields = {'raw': ''}
                elif '  - ' in line:
                    line_fields = line.split('  - ')
                    if line_fields[0] not in fields:
                        fields[line_fields[0]] = line_fields[1].strip()
                    else:
                        fields[line_fields[0]] += ';'+line_fields[1].strip()

    def filter(self, ris_csv: RIScsv, csv_fields: List[str]):
        included = 0
        with open(self.file_path+'.filtered', 'w') as f:
            for entry in ris_csv.included_referencies():
                for article in self.articles:
                    try:
                        occurencies: List[bool] = \
                            [entry[i].strip() == article.info[csv_fields[i]].strip() for i in range(len(csv_fields))]
                        if all(occurencies):
                            included += 1
                            f.write(article.info['raw'])
                            break
                    except Exception as e:
                        print(type(e), e)
        print(f'\nIncluded : {included}')

class RIScsv:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def included_referencies(self):
        with open(self.file_path, 'r') as f:
            header: str = next(f)
            score_index: int = header.count('\t') - len(Article.csv_fields)
            print(score_index)
            article_count_by_score: List[int] = []
            for field in range(score_index + 1):
                article_count_by_score.append(0)

            for line in f:
                score: int = int(line.split('\t')[score_index])
                print(score_index, line.split('\t')[:8], line.split('\t')[score_index])
                article_count_by_score[score] += 1

                if score >= 4:
                    yield line.split('\t')[-len(Article.csv_fields):]

        for score,count in enumerate(article_count_by_score):
            print(f'# of articles with a {score} total score : {count}')

    def write_entry(self, article:Article, extra_fields: List[str]):
        extra_fields.extend([article])
        entry = '\t'.join(extra_fields)
        with open(self.file_path, 'a+') as f:
            f.write(entry+'\n')

    def write_header(self, header):
        if os.path.isfile(self.file_path) == False:
            with open(self.file_path, 'w') as f:
                f.write(header+'\n')

class Criteria:
    def __init__(self):
        self._criteria: List[str] = []

    def add_criteria(self, criteria: str):
        self._criteria.append(criteria)

    @property
    def criteria_count(self):
        return len(self._criteria)

    def __str__(self):
        string: str = ''
        string += '\n'.join([f'Q{i+1} - {self._criteria[i]}' for i \
            in range(len(self._criteria))])

        return string

    @property
    def input_banner(self):
        numbers: Callable[[int], str] = lambda n: ''.join(map(lambda x:str(x),range(1,n+1)))
        string: str = ''
        string += 'Q'*len(self._criteria)
        string += '\n'
        string += numbers(len(self._criteria))

        return string

    @property
    def csv_header(self):
        header: List[str] = [f'I{i+1}' for i in range(len(self._criteria))]
        header.append('T')

        return '\t'.join(header)

if __name__ == '__main__':
    ris_file_path = './to_eval.ris'
    criteria = Criteria()

    criteria.add_criteria('Is the workflow/pipeline used/proposed documented well enough to be reproduced?')
    criteria.add_criteria('Can the workflow/pipeline be automated?')
    criteria.add_criteria('The solution makes use of well known models for describing the workflow/pipeline?')
    criteria.add_criteria('Is the workflow/pipeline data agnostic?')
    criteria.add_criteria('Is the workflow/pipeline able to be distributed?')
    criteria.add_criteria('The workflow/pipeline provides a way to be extended?')
    criteria.add_criteria('The research assesses reproducibility in bioinformatic experiments?')

    ris_csv = RIScsv('./to_eval.csv')

    analyze_articles = input('Do [y]ou want to process the articles, or filter usi[n]g the csv?')
    
    if analyze_articles.strip() == 'n':
        ris_file = RISfile(ris_file_path)
        ris_file.filter(ris_csv, csv_fields=Article.csv_fields)
    elif analyze_articles.strip() == 'y':
        if os.path.isfile(ris_file_path+'.temp'):
            ris_file = RISfile(ris_file_path+'.temp')
        else:
            ris_file = RISfile(ris_file_path)
        ris_csv.write_header(criteria.csv_header + '\t' + Article.csv_header)

        articles = iter(ris_file.articles)
        for article in articles:
            _ = os.system('clear')
            print(article)
            print('\n\n')
            print(criteria)
            options = ''
            while options not in ['q','p'] and len(options) != criteria.criteria_count:
                options = input('Introduce the values or [q]uit [p]ass\n'+criteria.input_banner+'\n')
            
            if options == 'q':
                with open(ris_file_path+'.temp', 'w') as f:
                    f.write(article.info['raw'])
                    left = 0
                    for x in articles:
                        f.write(x.info['raw'])
                        left += 1
                    print(f'{left} articles left for evaluation\n')
                break
            elif options == 'p':
                continue
            else:
                options = f'{options}{reduce(lambda x, a: x + int(a), options, 0)}'
                ris_csv.write_entry(article.to_csv(), list(options))

