from flask import render_template, url_for
from app import app
import os
from .models.experience import Experience
from .models.education import Education
from .models.hobbies import Hobbies
from .models.about import About
from .static.sample_data.data import data
    
@app.route('/')
def index():
    return render_template('layout.html',
                           title="MLH Fellow",
                           photoUrl=data['John Doe']['photourl'],
                           url=os.getenv("URL")
                           )

@app.route('/<name>')
def about(name):
    aboutme = []
    for about in data[name]['about']:
        aboutme.append(About(about['email'],
                                about['twitter'],
                                about['linkedin'],
                                about['description']
                                )
                            )
    return render_template('main.html', 
                           title="MLH Fellow",
                           name=name,
                           photoUrl=data[name]['photourl'],
                           url=os.getenv("URL"),
                           type='About', 
                           elements=aboutme)

@app.route('/experience/<name>')
def experience(name):
    experiences = []
    for experience in data[name]['experience']:
        experiences.append(Experience(experience['company'], 
                                    experience['position'], 
                                    experience['duration'], 
                                    experience['description']
                                    )
                            )
    return render_template('main.html', 
                           title="MLH Fellow",
                           name=name,
                           photoUrl=data[name]['photourl'],
                           url=os.getenv("URL"),
                           type='Experience', 
                           elements=experiences)

@app.route('/education/<name>')
def education(name):
    educations = []
    for education in data[name]['education']:
        educations.append(Education(education['institution'], 
                                    education['degree'], 
                                    education['tenure'], 
                                    education['description']
                                    )
                            )
    return render_template('main.html', 
                           title="MLH Fellow",
                           name=name,
                           photoUrl=data[name]['photourl'],
                           url=os.getenv("URL"),
                           type='Education', 
                           elements=educations)

@app.route('/hobbies/<name>')
def hobbie(name):
    hobbies = []
    for hobbie in data[name]['hobbies']:
        hobbies.append(Hobbies(hobbie['name'],
                            hobbie['description'],
                            hobbie['url'],
                            hobbie['alt'],
                            hobbie['textcolor']
                                )
                    )
    return render_template('main.html', 
                           title="MLH Fellow",
                           name=name,
                           photoUrl=data[name]['photourl'],
                           url=os.getenv("URL"),
                           type='Hobbies', 
                           elements=hobbies)