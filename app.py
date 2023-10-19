from flask import Flask, render_template, Response
import stream

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("landing.html")


@app.route('/landing2')
def landing2():
    return render_template("landing2.html")


@app.route('/landing3')
def landing3():
    return render_template("landing3.html")


@app.route('/doctor-login')
def doctor_login():
    return render_template("doctor-login.html")


@app.route('/doctor-register')
def doctor_register():
    return render_template("doctor-register.html")


@app.route('/contact')
def contact():
    return "contact는 준비중";

@app.route("/user-precheck")
def user_precheck():
    return render_template("user-precheck.html")


@app.route("/user-camera-check")
def user_camera_check():
    return Response(stream.GenerateFrames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run()
