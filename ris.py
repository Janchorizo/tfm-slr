from __future__ import annotations
from typing import Dict, List, Callable
from functools import reduce
import os
import re

class Article:
    required: List[str] = ['T1', 'A1', 'Y1', 'DO', 'N2']
    csv_fields: List[str] = ['T1', 'A1', 'Y1']
    csv_header: str = 'T1\tA1\tY1\tDO'

    def __init__(self, info: Dict[str,str]):
        if not all(map(lambda key: key in info, info)):
            raise Exception('Not all data available')
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
        articles = iter(self.articles)
        with open(self.file_path+'.filtered', 'w') as f:
            for entry in ris_csv.included_referencies():
                for article in articles:
                    occurencies: List[bool] = \
                        [entry[i] == article.info[csv_fields[i]] for i in range(len(csv_fields))]
                    if sum(occurencies) == len(csv_fields):
                        f.write(article.info['raw'])
                        break

class RIScsv:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def included_referencies(self):
        is_inclusion_criteria_field: Callable[[str], bool] = \
            lambda x: re.search('I\d+$',x) is not None

        with open(self.file_path, 'r') as f:
            header: str = next(f)
            inclusion_field_count: int = \
                reduce(lambda ac,dc: ac + is_inclusion_criteria_field(dc), header.split('\t'), 0)
            for line in f:
                entry = line.split('\t')
                if all(map(lambda x: x=='y', entry[:inclusion_field_count])):
                    yield entry[-4:]

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
        self._inclusion_criteria: List[str] = []
        self._exclusion_criteria: List[str] = []

    def add_inclusion_criteria(self, criteria: str):
        self._inclusion_criteria.append(criteria)

    def add_exclusion_criteria(self, criteria: str):
        self._exclusion_criteria.append(criteria)

    @property
    def criteria_count(self):
        return len(self._inclusion_criteria) + len(self._exclusion_criteria)

    def __str__(self):
        string: str = ''
        string += '\n'.join([f'I{i} - {self._inclusion_criteria[i]}' for i \
            in range(len(self._inclusion_criteria))])
        string += '\n'
        string += '\n'.join([f'E{i} - {self._exclusion_criteria[i]}' for i \
            in range(len(self._inclusion_criteria))])

        return string

    @property
    def input_banner(self):
        numbers: Callable[[int], str] = lambda n: ''.join(map(lambda x:str(x),range(1,n+1)))
        string: str = ''
        string += 'I'*len(self._inclusion_criteria) + 'E'*len(self._exclusion_criteria)
        string += '\n'
        string += numbers(len(self._inclusion_criteria)) + numbers(len(self._exclusion_criteria))

        return string

    @property
    def csv_header(self):
        header: List[str] = [f'I{i}' for i in range(len(self._inclusion_criteria))]
        header.extend([f'E{i}' for i in range(len(self._exclusion_criteria))])

        return '\t'.join(header)

if __name__ == '__main__':
    ris_file_path = './without_duplicates.ris'
    criteria = Criteria()

    criteria.add_inclusion_criteria('The paper addresses a (RnaSeq OR WES) process AND')
    criteria.add_inclusion_criteria('The paper proposes a software based solution (model, tool, framework, service, infrastructure, system, technique, application) AND')
    criteria.add_inclusion_criteria('The proposed solution allows for the solution to be replicated AND')
    criteria.add_inclusion_criteria('The proposed solution allows to replicate the environment in which the process would take place AND')

    criteria.add_exclusion_criteria('The paper does not address a RnaSeq OR WES process OR')
    criteria.add_exclusion_criteria('The paper does not propose a software based solution (model, tool, framework, service, infrastructure, system, technique, application) OR')
    criteria.add_exclusion_criteria('The proposed solution does not allow for the solution to be replicated OR')
    criteria.add_exclusion_criteria('The proposed solution does not allow to replicate the environment in which the process would take place OR')
    criteria.add_exclusion_criteria('The paper addresses one monolithic process')
    criteria.add_exclusion_criteria('The paper proposes a solution for just a specific step of the bioinformatic process')

    ris_csv = RIScsv('./evaluated.csv')

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
                    for x in articles:
                        f.write(x.info['raw'])
                break
            elif options == 'p':
                continue
            else:
                ris_csv.write_entry(article.to_csv(), list(options))

