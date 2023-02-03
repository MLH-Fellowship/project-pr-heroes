import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from .models.experience import Experience
from .static.sample_data.data import data

load_dotenv()
app = Flask(__name__)


experiences = []
for experience in data['experience']:
    experiences.append(Experience(experience['company'], 
                                  experience['position'], 
                                  experience['duration'], 
                                  experience['description']
                                  )
                        )

@app.route('/')
def index():
    return render_template('components/experience.html', title="MLH Fellow", url=os.getenv("URL"), experiences=experiences)