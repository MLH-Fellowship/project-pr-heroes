from flask import render_template
from app import app
import os
from .models.experience import Experience
from .models.education import Education
from .static.sample_data.data import data

experiences = []
for experience in data['experience']:
    experiences.append(Experience(experience['company'], 
                                  experience['position'], 
                                  experience['duration'], 
                                  experience['description']
                                  )
                        )
educations = []
for education in data['education']:
    educations.append(Education(education['institution'], 
                                  education['degree'], 
                                  education['tenure'], 
                                  education['description']
                                  )
                        )

@app.route('/')
def index():
    return render_template('main.html', 
                           title="MLH Fellow", 
                           url=os.getenv("URL"),
                           type='Education', 
                           elements=educations)