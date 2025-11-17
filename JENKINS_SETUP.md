# Configuration Jenkins pour le Projet Python

## Problème
Jenkins sur Windows ne trouve pas Python car il n'est pas dans le PATH du service Jenkins.

## Solution

### Option 1: Configurer le PATH dans Jenkins (Recommandé)

1. Accédez à **Manage Jenkins → System Configuration** (ou **Manage Jenkins → Configure System**)
2. Allez à la section **Global properties** → **Environment variables**
3. Ajoutez une nouvelle variable:
   - **Nom**: `PYTHON_HOME`
   - **Valeur**: `C:\Users\oualid\AppData\Local\Programs\Python\Python311` (adaptez à votre version Python)
4. Redémarrez Jenkins

Ensuite, modifiez le Jenkinsfile pour utiliser:
```groovy
bat '''
    %PYTHON_HOME%\python.exe --version
    %PYTHON_HOME%\python.exe -m pip install --upgrade pip
    %PYTHON_HOME%\python.exe -m pytest ...
'''
```

### Option 2: Installer Jenkins avec Python dans le PATH

1. Exécutez `setup_jenkins.bat` pour trouver l'emplacement de Python
2. Lancez le service Jenkins en tant qu'administrateur
3. Modifiez le service Jenkins pour inclure Python dans son PATH

### Option 3: Utiliser le Jenkinsfile actuel (Recherche automatique)

Le Jenkinsfile actuel recherche automatiquement Python. S'il ne le trouve pas, c'est que:
- Python n'est pas installé
- Python n'est pas ajouté au PATH système
- Le service Jenkins s'exécute avec des permissions insuffisantes

## Vérification

Pour vérifier que Python est accessible au service Jenkins:

1. Ouvrez PowerShell en tant qu'administrateur
2. Exécutez: `Get-Service Jenkins | Select-Object -Property StartName`
3. Notez le compte utilisateur (par exemple: `.\Jenkins`)
4. Exécutez: `whoami` pour obtenir l'utilisateur actuel
5. Comparez les chemins Python accessibles par chaque utilisateur

## Test rapide

Pour tester si le Jenkinsfile fonctionne, vous pouvez aussi:

1. Créer une version locale du script
2. L'exécuter manuellement sur la machine Jenkins
3. Adapter le Jenkinsfile selon le résultat

## Ressources

- [Configuring Jenkins System Configuration](https://www.jenkins.io/doc/book/managing/system-configuration/)
- [Jenkins on Windows Service](https://www.jenkins.io/doc/book/installing/windows/)
