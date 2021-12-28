from flask import Flask, request, render_template

from static.stories import Story

app = Flask(__name__)
app.config['SECRET KEY'] = 'secret'

@app.route('/')
def show_questions():
    return render_template ('index.html')

@app.route('/madlib')
def make_madlib():
    place = request.args.get('place')
    noun = request.args.get('noun')
    verb = request.args.get('verb')
    adjective = request.args.get('adjective')
    name = request.args.get('name')

    return render_template ('madlibs.html', place = place, noun = noun, verb = verb, adjective = adjective, name = name)


def create_new_story(place, noun, verb, adjective, plural_noun):
    story3 = Story([
    place, noun, verb, adjective,plural_noun
    ],
    '''{name} {verb} the {noun} so hard that it broke into pieces. So they went back to {place} and ate {adjective} snakes'''
    )
    return story3

app.jinja_env.globals.update(create_new_story=create_new_story)

def get_ans(story):
    ans = {'place': story.prompts[0], 'noun': story.prompts[1], 'verb': story.prompts[2], 'adjective': story.prompts[3], 'name': story.prompts[4] }

    return ans

app.jinja_env.globals.update(get_ans=get_ans)