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

IC3: The proposed solution can be reused and replicated AND

IC4: The required environment is well defined and replicable 

### Exclusion criteria
EC1: The paper does not address a (RnaSeq OR WES) (process OR worflow or pipeline) OR

EC2: The paper does not propose a software based solution (model, tool, framework, service, 
infrastructure, system, technique, application) OR

EC3: The proposed solution does not allow for the (workflow/pipeline) to be reused or replicated OR

EC4: The requirement environment is not well defined and replicable OR

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

The queries were executed on April 24th, 2019.

_Reference query_
((rna-seq OR rnaseq OR “rna seq*”) OR ”whole exome sequenc*”) AND (((“pipeline” OR “schem*”) AND "implement*")OR ("framework" AND "software") OR "automate" OR ("experiment" AND "reproducibility"))

#### WoS (472)
TOPIC: (( ( ( rna-seq OR rnaseq OR "rna seq*" ) OR "whole exome sequenc*" ) AND ( (("pipeline" OR “schem*”) AND "implement*") OR ("framework" AND "software") OR "automate" OR ("experiment" AND "reproducibility") ) ))
Refined by: RESEARCH DOMAINS: ( SCIENCE TECHNOLOGY ) AND RESEARCH DOMAINS: ( SCIENCE TECHNOLOGY ) AND DOCUMENT TYPES: ( ARTICLE ) AND Databases: ( WOS OR MEDLINE )
Search language=Auto  

#### Scopus (513)
TITLE-ABS-KEY ( ( ( rna-seq OR rnaseq OR "rna seq*" ) OR "whole exome sequenc*" ) 
AND ( (("pipeline" OR “schem*”) AND "implement*")
    OR ("framework" AND "software") 
OR "automate" 
OR ("experiment" AND "reproducibility") ) ) 
AND ( LIMIT-TO ( SUBJAREA,"BIOC" ) 
OR LIMIT-TO ( SUBJAREA,"COMP" ) ) 
AND  ( LIMIT-TO ( DOCTYPE ,  "ar" ) ) 
