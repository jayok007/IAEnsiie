# IAEnsiie

## Prerequisites

You need to have a firestore database. Therefore you need to specify GOOGLE_APPLICATION_CREDENTIAL this way :

```bash
    export GOOGLE_APPLICATION_CREDENTIALS=$(pwd)/cred.json
```

And you need to install TreeTagger on your machine.

[Tutorial on how to install TreeTagger](https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/)

TIPS for TreeTagger installation :
 - Install it close to your python repository (I created a repository besides the git repository)
 - Install french corpus