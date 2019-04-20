# tfm-slr
Repository for bibliographic references used in the make of a SLR for bioinformatic pipelines.


# SLR
## Motivation : research questions  
RQ1: What frameworks have been used to model and automate RNSEQ experiments?

RQ2: What approaches to automatic bio-pipelines allow for customization?

RQ3: Which are the most common configuration parameters for bio-pipelines, and what is the 
most common format for defining them?

RQ4: What are the needs covered by automatic reports in regards to replicability of the 
experiment?

## Article acceptance : inclusion and exclusion criteria
### Inclusion criteria
IC1: The paper addresses a (RnaSeq OR WES) (process OR worflow or pipeline) AND

IC2: The paper proposes a software based solution (model, tool, framework, service, 
infrastructure, system, technique, application) AND

IC3: The proposed solution allows for the solution to be replicated AND

IC4: The proposed solution allows to replicate the environment in which the process would 
take place

### Exclusion criteria
EC1: The paper does not address a (RnaSeq OR WES) (process OR worflow or pipeline) OR

EC2: The paper does not propose a software based solution (model, tool, framework, service, 
infrastructure, system, technique, application) OR

EC3: The proposed solution does not allow for the solution to be replicated OR

EC4: The proposed solution does not allow to replicate the environment in which the process 
would take place OR

EC5: The paper addresses one monolithic process

EC6: The paper proposes a solution for just a specific step of the bioinformatic process

## Sources
WoS and Scopus were used for retrieving the results

## Research queries
The following terms were taken into account when writing the queries:

+ pipeline
+ process
+ rna-seq
+ wes
+ automate
+ framework
+ tool
+ sotware
+ schema

### Queries
The queries aim at retrieving software based projects that focus on autamation and reproducibility of bioinformatic experiments regarding rnaseq or wes (whole exome sequence). Either by the proposal of a framework, a pipeline or some software solution.

Only articles are revised, excluding those earlier to 2017 and from different fields to the one mentioned.

The queries were executed on April 19th, 2019.

_Reference query_
((rna-seq OR rnaseq OR “rna seq*”) OR ”whole exome sequenc*”) AND (“pipeline” OR “schem*” OR ("framework" AND "software") OR "automate" OR ("experiment" AND "reproducibility"))

#### WoS (635)
TOPIC: (( ( ( rna-seq OR rnaseq OR "rna seq*" ) OR "whole exome sequenc*" ) AND ( "pipeline" OR “schem*” OR ("framework" AND "software") OR "automate" OR ("experiment" AND "reproducibility") ) ))
Refined by: RESEARCH DOMAINS: ( SCIENCE TECHNOLOGY ) AND RESEARCH DOMAINS: ( SCIENCE TECHNOLOGY ) AND DOCUMENT TYPES: ( ARTICLE ) AND Databases: ( WOS OR MEDLINE )
Timespan: 2017-2019. Databases:  WOS, CCC, DIIDW, KJD, MEDLINE, RSCI, SCIELO.
Search language=Auto  

#### Scopus (575)
TITLE-ABS-KEY ( ( ( rna-seq OR rnaseq OR "rna seq*" ) OR "whole exome sequenc*" ) 
AND ( "pipeline" OR “schem*”
    OR ("framework" AND "software") 
OR "automate" 
OR ("experiment" AND "reproducibility") ) ) 
AND ( LIMIT-TO ( SUBJAREA,"BIOC" ) 
OR LIMIT-TO ( SUBJAREA,"COMP" ) ) 
AND ( LIMIT-TO ( PUBYEAR,2019) 
OR LIMIT-TO ( PUBYEAR,2018) 
OR LIMIT-TO ( PUBYEAR,2017) )
AND  ( LIMIT-TO ( DOCTYPE ,  "ar" ) ) 

## Duplicate removal
Duplicate entries for articles were detected and deleted with the desktop Mendeley application (v1.19.4).

After duplicate removal __869__ different articles were obtained, and which will be processed by applying the inclusion/acceptance and 
exclusion/rejection criteria previously defined. 

## Applying the inclusion and exclusion criteria
The file format used for the referencies is .ris (). This file will be used in conjuction with the
ris.py Python program writen for this task.

The program allows to go through each of the articles in the initial .ris file and write the values
for each of the criteria specified, additionally:
* A csv is generated with a header indicating the filed's related information and a row entry for
	each of the references analyzed; each of them with the values applied.
* When the users stops the analysis of the bibliography by pressing 'q', a .temp file is created
	in the same directory for the process to be continued at any time.
* When the user selects the filter option, the csv created will be used to create a .ris file with
	the same base name as the initial with a '.filtered' extension appended, containing all the
	references from the original that have met all the inclusion criteria defined in the csv.

