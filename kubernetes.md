# Turning ou kubectl autocomplete on GCP Cloud Shell

Similar to what documented on the official kubernetes docs, you have to do:  
`echo "source <(kubectl completion bash)" >> ~/.bash_profile`  
The only difference, `source` doesnt seem to work in `.bashrc`, but works fine in `.bash_profile`  
Official docs: https://kubernetes.io/docs/tasks/tools/install-kubectl/#enabling-shell-autocompletion
