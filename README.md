# external-sort-visualizer
Final project for the course of Data Management 2022/23 edition held at Sapienza University of Rome

## Demo requirements
To run the server you can choose one of the below strategies, after you cloned the repository and changed to the project root
1. Docker (Recommended)\
    &nbsp;&nbsp;&nbsp;&nbsp;1.1. Build the image: `docker build -t <name-you-prefer> .`\
    &nbsp;&nbsp;&nbsp;&nbsp;1.2. Run the container: `docker run -p 5000:5000 <name-you-prefer>`
2. Virtual Environment\
    &nbsp;&nbsp;&nbsp;&nbsp;2.1. Create and activate a Python3 virtual environment\
    &nbsp;&nbsp;&nbsp;&nbsp;2.2. Install the dependencies in the virtual environment `pip install -r requirements.txt` from the folder where requirements file is stored\
    &nbsp;&nbsp;&nbsp;&nbsp;2.3. Start the server `python main.py` it will listen on all interfaces at port 5000.\
Now you can use any browser and access the tool by navigating http://localhost:5000.

## Limits
Too large relations in terms of either rows or number of attributes can make the visualization look bad, because blocks will grow too wide. Try use the samples provided in the repository 


