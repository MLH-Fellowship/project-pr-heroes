from flask import render_template
from app import app
import os
from .models.experience import Experience
from .static.sample_data.data import data

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
    return render_template('main.html', 
                           title="MLH Fellow", 
                           url=os.getenv("URL"),
                           type='Experience', 
                           elements=experiences)