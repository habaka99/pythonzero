from flask import Flask ,render_template
skill_app=Flask(__name__)
my_skills=[("html",50),("css",60),("python",70)]
@skill_app.route("/")
def homepage():
    return render_template("hommepage.html",title="Home page",custom_css="homepage")
@skill_app.route("/about")
def aboutpage():
    return render_template("abouttpage.html",title="About page")
@skill_app.route("/add")
def add():
    return render_template("add.html",title="About page",custom_css="add")
@skill_app.route("/skill")
def skill():
    return render_template("skill.html",title="skill page",custom_css="skills",page_head="my skills",description="this is my skills page",skills=my_skills,
                          )
if __name__=="__main__":
    skill_app.run(debug=True,port=8000)
