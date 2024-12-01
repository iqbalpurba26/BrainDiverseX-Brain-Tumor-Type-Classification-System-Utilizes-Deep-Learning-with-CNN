# GET STARTED
To learn more, you can check out the project documentation [[HERE]](https://github.com/iqbalpurba26/BrainDiverseX-api/blob/main/ABOUT%20PROJECT.md). Before starting this project, make sure you understand the following points:

- This repository consists of 2 main folders: API and WEBSITE. These folders run separately.
- The API folder contains the API to connect the model with the Website. - The Website folder contains simple HTML and CSS files as the project's interface.
- Open both folders in two different IDE windows.
- Ensure you have cloned the repository.


Now let's get started running the project
## Running the API
- Open the API folder in your IDE
- Prepare the environment
    ```
    python -m venv env

    env\Scripts\activate.bat

    pip install -r requirements.txt    
    ```
- Run the API
    ```
    uvicorn endpoint:app --reload
    ```
- (Optional) Hit the API using Postman to confirm availability. Then go to Body > Form Data > fill the key with "image" > change type to file > upload file


## Running the Website
- Open the WEBSITE folder in different window
- Ensure the API is running at http://127.0.0.1:8000
- If different, please replace the URL in the Website's JavaScript section
- Launch the website
- Try uploading an image