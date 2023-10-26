from flask import Flask, render_template
app=Flask(__name__,template_folder='template')
@app.route("/")
def home():
  return render_template('Home.html')
@app.route('/dashboard')
def dashboard():
  return render_template('Dashboard.html')
@app.route('/story')
def story():
  return render_template('Story.html')
@app.route('/report')
def report():
  return render_template('Report.html')
if __name__=="__main__":
  app.run()
