# Configuration de Jenkins pour Python sur Windows

## Problème actuel

Jenkins ne trouve pas Python même s'il est installé sur la machine. Cela se produit parce que:

1. **Le service Jenkins s'exécute sous un compte système** qui n'a pas le même PATH que votre compte utilisateur
2. **Python n'est pas dans le PATH du service Jenkins**
3. **Les variables d'environnement utilisateur ne sont pas hérédées par le service**

## Solution immédiate

### Ajouter Python au PATH système (Méthode 1 - Recommandée)

1. Trouvez l'emplacement exact de Python:
   ```powershell
   (Get-Command python).Source
   ```
   Exemple: `C:\Users\oualid\AppData\Local\Programs\Python\Python311\python.exe`

2. Copiez le répertoire parent: `C:\Users\oualid\AppData\Local\Programs\Python\Python311`

3. Allez à **Paramètres Système** → **Variables d'environnement**

4. Sous **Variables système**, trouvez ou créez `PATH`

5. Ajoutez le chemin Python au PATH système

6. **Redémarrez Jenkins:**
   ```powershell
   Restart-Service Jenkins
   ```

### Vérifier que c'est pris en compte

Après redémarrage, relancez le build Jenkins. Le stage "Verify Python" affichera:
- Le contenu du PATH
- Si Python est trouvé
- L'emplacement exact de Python

## Alternative: Configurer dans Jenkins UI

1. Allez à **Manage Jenkins** → **System** (ou **Configure System**)
2. Trouvez **Global properties**
3. Cochez **Environment variables**
4. Ajoutez une variable:
   - **Name**: `PATH`
   - **Value**: `C:\Users\oualid\AppData\Local\Programs\Python\Python311;${PATH}`

5. Cliquez **Save** et **Redémarrez Jenkins**

## Diagnostic

Pour vérifier quel utilisateur exécute Jenkins:

1. Ouvrez PowerShell en tant qu'administrateur
2. Exécutez:
   ```powershell
   $service = Get-Service Jenkins
   $service | Select-Object -Property StartName
   ```

3. Connectez-vous avec cet utilisateur et vérifiez si Python est disponible:
   ```powershell
   python --version
   where python
   ```

## Chemins Python courants

- **Installation utilisateur**: `C:\Users\<username>\AppData\Local\Programs\Python\Python311`
- **Installation système**: `C:\Python311`
- **Microsoft Store**: `C:\Users\<username>\AppData\Local\Microsoft\WindowsApps`

## Jenkinsfile amélioré

Le Jenkinsfile actuel cherche Python automatiquement dans:
1. Le PATH
2. Emplacements courants (C:\Python310, C:\Python311, etc.)
3. Dossier utilisateur (AppData\Local\Programs\Python)

Si aucun n'est trouvé, le build échoue avec un message explicite.

## Test manuel

Pour tester manuellement si Jenkins peut accéder à Python:

1. Exécutez cmd.exe en tant qu'administrateur
2. Exécutez: `python --version`
3. Si cela échoue, Python n'est pas dans le PATH système
4. Ajoutez-le selon la section "Solution immédiate"
