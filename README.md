# tfm-slr
Repository for bibliographic references used in the make of a SLR for bioinformatic pipelines.
 SLR
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

IC3: The proposed solution allows for the (workflow/pipeline) to be reused or replicated AND

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

_Reference query_
((rna-seq OR rnaseq OR “rna seq*”) OR ”whole exome sequenc*”) AND (“pipeline” OR “schem*” OR ("framework" AND "software") OR "automate" OR ("experiment" AND "reproducibility"))

#### WoS 1 (635) [wos_1.ris](https://github.com/Janchorizo/tfm-slr/blob/revision/wos_1.ris)
TOPIC: (( ( ( rna-seq OR rnaseq OR "rna seq*" ) OR "whole exome sequenc*" ) AND ( "pipeline" OR “schem*” OR ("framework" AND "software") OR "automate" OR ("experiment" AND "reproducibility") ) ))
Refined by: RESEARCH DOMAINS: ( SCIENCE TECHNOLOGY ) AND RESEARCH DOMAINS: ( SCIENCE TECHNOLOGY ) AND DOCUMENT TYPES: ( ARTICLE ) AND Databases: ( WOS OR MEDLINE )
Timespan: 2017-2019. Databases:  WOS, CCC, DIIDW, KJD, MEDLINE, RSCI, SCIELO.
Search language=Auto  

#### Scopus 1 (575) [scopus_1.ris](https://github.com/Janchorizo/tfm-slr/blob/revision/scopus_1.ris)
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

#### WoS 2 (472) [wos_2.ris](https://github.com/Janchorizo/tfm-slr/blob/revision/wos_2.ris)
TOPIC: (( ( ( rna-seq OR rnaseq OR "rna seq*" ) OR "whole exome sequenc*" ) AND ( (("pipeline" OR “schem*”) AND "implement*") OR ("framework" AND "software") OR "automate" OR ("experiment" AND "reproducibility") ) ))
Refined by: RESEARCH DOMAINS: ( SCIENCE TECHNOLOGY ) AND RESEARCH DOMAINS: ( SCIENCE TECHNOLOGY ) AND DOCUMENT TYPES: ( ARTICLE ) AND Databases: ( WOS OR MEDLINE )
Search language=Auto  

#### Scopus 2 (513) [scopus_2.ris](https://github.com/Janchorizo/tfm-slr/blob/revision/scopus_2.ris)
TITLE-ABS-KEY ( ( ( rna-seq OR rnaseq OR "rna seq*" ) OR "whole exome sequenc*" ) 
AND ( (("pipeline" OR “schem*”) AND "implement*")
    OR ("framework" AND "software") 
OR "automate" 
OR ("experiment" AND "reproducibility") ) ) 
AND ( LIMIT-TO ( SUBJAREA,"BIOC" ) 
OR LIMIT-TO ( SUBJAREA,"COMP" ) ) 
AND  ( LIMIT-TO ( DOCTYPE ,  "ar" ) ) 

#### Query results merged [merged.ris](https://github.com/Janchorizo/tfm-slr/blob/revision/merged.ris)
The sum of references for all four searches is of **2195** total references.

## Duplicate removal [without_duplicates.ris](https://github.com/Janchorizo/tfm-slr/blob/revision/without_duplicates.ris)
Duplicate entries for articles were detected and deleted with the desktop Mendeley application (v1.19.4).

After duplicate removal __1398__ different articles were obtained, and which will be processed by applying the inclusion/acceptance and 
exclusion/rejection criteria previously defined.

## Applying the inclusion and exclusion criteria [without_duplicates.ris.filtered](https://github.com/Janchorizo/tfm-slr/blob/revision/without_duplicates.ris.filtered)
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

The result of applying the inclusion and exclusion crteria is a set of __133__ articles related to the questions firstly
proposed; framed in the design and implementation of bioinformatic workflows/pipelines in the context
of wes and rnaseq analysis.

## Excluding articles during data extraction [to_eval.ris.deleted](https://github.com/Janchorizo/tfm-slr/blob/revision/to_eval.ris.deleted)
While reapplying the inclusion and exclusion criteria, if an article shows to be not relevant to
the research questions, it is excluded from the list of articles to be used in the final revision.

There were a total of __69__ articles that were rejected while applying the quality criteria, 
because of unfulfillment of the inclusion criteria or irrelevance to the proposed research questions.

## Applying quality checks to the articles [to_eval.ris.filtered](https://github.com/Janchorizo/tfm-slr/blob/revision/to_eval.ris.filtered)

To ensure that the revised articles contribute in a suficient manner, and with a minimum of alignment
to the research questions proposed, a set of quality checks are applyed to each individual article.
Each of the questions contributes with a different value, adding up to a maximum of 7.

The minimum score of an article to be selected for analysis is 4. This is an arbitrary value
selected taking into account the articles that fulfil these.

The questions and scores are the following :
1. (1) Is the workflow/pipeline used/proposed documented well enough to be reproduced?
2. (1) Can the workflow/pipeline be automated?
3. (1) The solution makes use of well known models for describing the workflow/pipeline?
4. (1) Is the workflow/pipeline data agnostic?
5. (1) Is the workflow/pipeline able to be distributed?
6. (1) The workflow/pipeline provides a way to be extended?
7. (1) The research assesses reproducibility in bioinformatic experiments? 

After applying the quality criteria, there are total of __37__ articles that were included in the revision
of the literacy.
