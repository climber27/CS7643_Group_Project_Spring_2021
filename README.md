# CS7643_Group_Project_Spring_2021

### Workflow

1) From local that is synced with Google Drive (see [Backup and Sync])
   - Develop on a separate branch from main. Preferably {your name}-{what you're doing}-{version}
      - Keep notebooks in `teams/{your name}/`
   - Write unit tests if it's anything that others can use (utils, custome loss functions, etc.)
      - See [PyTest]
2) Run experiements via Google Colab Notebooks or personal scripts from `teams/{your name}/` on a cloud provider
   - Google Colab instructions
     - Mount Drive
    ```py
        from google.colab import drive
        drive.mount('/content/gdrive')
    ```
    - `%cd gdrive/My Drive/{this repo}`
    - install packages
     ```py
        !pip install -r requirements.txt
    ```


[Backup and Sync]: https://www.google.com/drive/download/
[PyTest]: https://docs.pytest.org/en/6.2.x/getting-started.html