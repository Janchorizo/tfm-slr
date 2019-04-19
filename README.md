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
IC1: The paper addresses a RnaSeq OR WES process AND
IC2: The paper proposes a software based solution (model, tool, framework, service, 
infrastructure, system, technique, application) AND
IC3: The proposed solution allows for the solution to be replicated AND
IC4: The proposed solution allows to replicate the environment in which the process would 
take place AND
IC5: The paper was published in the year 2017 or later

### Exclusion criteria
EC1: The paper does not address a RnaSeq OR WES process OR
EC2: The paper does not propose a software based solution (model, tool, framework, service, 
infrastructure, system, technique, application) OR
EC3: The proposed solution does not allow for the solution to be replicated OR
EC4: The proposed solution does not allow to replicate the environment in which the process 
would take place OR
EC5: The paper was not published in the year 2017 or later

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

After duplicate removal __892__ different articles were obtained, and which will be processed by applying the inclusion/acceptance and 
exclusion/rejection criteria previously defined. 
