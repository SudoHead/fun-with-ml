FROM tensorflow/tensorflow:latest-gpu-jupyter

WORKDIR /tf

COPY ./requirements.txt .

# Install the required libraries and copy files
# RUN while IFS= read -r requirement; do conda install $requirement; done < requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Run a bash terminal when the containers is run
CMD bash