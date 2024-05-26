from flask import Flask, render_template, request,session
import os
import schedule

app = Flask(__name__)

app.secret_key="Pawan's secret key"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/design/')
def design():
    return render_template('design.html')

@app.route('/form/<string:design>', methods=['POST','GET'])
def form(design):
    session["design_session"] = design
    return render_template('form.html')

@app.route('/update', methods=["GET", "POST"])
def update():
    if request.method == 'POST':
        name = request.form.get('First_name')
        lastname = request.form.get('Last_name')
        schoolname = request.form.get('School_name')
        collegename = request.form.get('College_name')
        mobilenumber = request.form.get('Mobile_number')
        email = request.form.get('Email_address')
        about = request.form.get('about')
        skills = request.form.getlist('skills[]')
        insta=request.form.get('instagram')
        git=request.form.get('git')
        #Image Uploading methods
        profile = request.files['image']   
        profile.save(f"static/images/{profile.filename}")
        design_upload=session.get("design_session")   
        if design_upload == "design1":        
            return render_template('design1.html', 
                                dname=name,
                                dlname=lastname,
                                dsch=schoolname,
                                dcol=collegename,
                                dph=mobilenumber,
                                demail=email,
                                dabout=about,
                                dskills=skills,
                                img=profile.filename,
                                dinsta=insta,
                                dgit=git)
        elif design_upload== "design2":
            return render_template('design2.html', 
                                dname=name,
                                dlname=lastname,
                                dsch=schoolname,
                                dcol=collegename,
                                dph=mobilenumber,
                                demail=email,
                                dabout=about,
                                dskills=skills,
                                img=profile.filename,
                                dinsta=insta,
                                dgit=git)
        elif design_upload== "design3":
            return render_template('design3.html', 
                                dname=name,
                                dlname=lastname,
                                dsch=schoolname,
                                dcol=collegename,
                                dph=mobilenumber,
                                demail=email,
                                dabout=about,
                                dskills=skills,
                                img=profile.filename,
                                dinsta=insta,
                                dgit=git)
        elif design_upload== "design4":
            return render_template('design4.html', 
                                dname=name,
                                dlname=lastname,
                                dsch=schoolname,
                                dcol=collegename,
                                dph=mobilenumber,
                                demail=email,
                                dabout=about,
                                dskills=skills,
                                img=profile.filename,
                                dinsta=insta,
                                dgit=git)
            
    else:
        return render_template('form.html')
    
def delete():
    file = os.listdir("static/images")
    for f in file:
        os.remove(f"static/images/{f}") 

if __name__ == '__main__':
    schedule.every().day.at("23:59").do(delete)
    app.run(host='0.0.0.0', port=8000, debug=True)