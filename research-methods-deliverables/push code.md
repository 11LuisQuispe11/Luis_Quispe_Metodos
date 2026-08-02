# Copy and push

1. Extract `Luis_Quispe_Metodos_Donna_Structure.zip`.
2. Copy the contents inside the extracted folder to the root of your repository.
3. Do not create another nested outer folder.

```bash
cd /e/Luis/Luis_Quispe_Metodos

git remote set-url origin https://github.com/11LuisQuispe11/Luis_Quispe_Metodos.git

git add .
git status
git commit -m "Align repository with complete UNMSM course structure"
git push origin main
```

Before committing, verify that no real operational data, coordinates, credentials, or source-system names were added.
