# Generator for NoDaLiDa 2023 Proceedings 

This package allows to generate NoDaLiDa 2023 proceedings from OpenReview submissions (with some manual work).

It is based on https://github.com/rycolab/aclpub2 with some modifications. Most of the useful information is there and won't be repeated here.

## Steps

* Go to https://aclanthology.org/info/contrib/ and read it. Basically you have to open a Github issue (an ingestion request) 2 week before the submission.

* Modify `conference_details.yml` and all other YAML files.

* Install required Python packages (see `requirements.txt`)

* Generate the list of reviewers (`program_committee.yml`)

```    
python scripts/or2program_committee.py USER PASSWORD NoDaLiDa/2023/Conference
```
   
* Go through `program_committee.yml` and modify, if needed.

* Generate `papers.yml` along with `papers/` subdirectory

```   
python scripts/or2papers.py --all --pdfs USER PASSWORD NoDaLiDa/2023/Conference
```

* Go through `papars.yml` and update author names for those that do not have their OpenReview aprofile properly configured

* Generate the ACL ingestion package

```
PYTHONPATH=. ./bin/generate  --proceedings --overwrite .
```
 
* Tar the output directory

```
tar zcvf nodalida2023main_aclpub2.tgz output/
```
 
* Upload it to Google Drive or whatever and add the link to the Github issue that you opened in Step 1.
