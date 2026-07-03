from flask import Flask, render_template, request, flash, redirect, url_for, session, send_from_directory
from database import get_db, init_db
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
app = Flask(__name__)
app.secret_key='linkkiwi2026' #needed for flashing message

@app.route('/IMAGES/<path:filename>')
def images(filename):
    return send_from_directory(os.path.join(app.root_path, 'IMAGES'), filename)

QUESTIONS = [
    {
        "q": "Q1. What does HTML stand for?",
        "options": [
            "Hyper Text Markup Language",
            "High Text Machine Language",
            "Hyper Transfer Markup Language",
            "Home Tool Markup Language"
        ],
        "answer": "Hyper Text Markup Language"
    },
    {
        "q": "Q2. Which HTML tag is used to create a hyperlink?",
        "options": ["<a>", "<link>", "<href>", "<url>"],
        "answer": "<a>"
    }
]

QUESTIONS1 = [
    {
        "q": "Q1. What does AI stand for?",
        "options": [
            "Artificial Intelligence",
            "Automatic Intelligence",
            "Advanced Internet",
            "Artificial Internet"
        ],
        "answer": "Artificial Intelligence"
    },
    {
        "q": "Q2. Which of the following is a branch of AI?",
        "options": [
            "Machine Learning",
            "Web Hosting",
            "Networking",
            "Cloud Storage"
        ],
        "answer": "Machine Learning"
    }
]

QUESTIONS2 = [
    {
        "q": "Q1. What is Data Science?",
        "options": [
            "Study of data to gain insights",
            "Web Development",
            "Computer Networking",
            "Operating System"
        ],
        "answer": "Study of data to gain insights"
    },
    {
        "q": "Q2. Which language is most popular in Data Science?",
        "options": [
            "Python",
            "HTML",
            "CSS",
            "PHP"
        ],
        "answer": "Python"
    }
]

QUESTIONS3 = [
    {
        "q": "Q1. What is Cloud Computing?",
        "options": [
            "Delivering computing services over the Internet",
            "Building websites",
            "Creating databases",
            "Computer repair"
        ],
        "answer": "Delivering computing services over the Internet"
    },
    {
        "q": "Q2. Which of the following is a Cloud Service Provider?",
        "options": [
            "AWS",
            "HTML",
            "CSS",
            "Bootstrap"
        ],
        "answer": "AWS"
    }
]

QUESTIONS4 = [
    {
        "q": "Q1. What is Cyber Security?",
        "options": [
            "Protecting systems and data from cyber attacks",
            "Creating websites",
            "Building databases",
            "Computer manufacturing"
        ],
        "answer": "Protecting systems and data from cyber attacks"
    },
    {
        "q": "Q2. What is a Virus?",
        "options": [
            "A malicious software",
            "A programming language",
            "A web browser",
            "A database"
        ],
        "answer": "A malicious software"
    }
]

QUESTIONS5 = [
    {
        "q": "Q1. What is Mobile App Development?",
        "options": [
            "Creating applications for mobile devices",
            "Building computer hardware",
            "Managing databases",
            "Creating networks"
        ],
        "answer": "Creating applications for mobile devices"
    },
    {
        "q": "Q2. Which operating system is used by Android devices?",
        "options": [
            "Android",
            "iOS",
            "Windows",
            "Linux"
        ],
        "answer": "Android"
    }
]

QUESTIONS_C = [
    {
        "q": "Q1. Who is known as the father of C language?",
        "options": [
            "Dennis Ritchie",
            "Bjarne Stroustrup",
            "James Gosling",
            "Guido van Rossum"
        ],
        "answer": "Dennis Ritchie"
    },
    {
        "q": "Q2. In which year was C language developed?",
        "options": [
            "1972",
            "1985",
            "1995",
            "2000"
        ],
        "answer": "1972"
    }
]

QUESTIONS_CPP = [
    {
        "q": "Q1. Who developed C++ language?",
        "options": [
            "Bjarne Stroustrup",
            "Dennis Ritchie",
            "James Gosling",
            "Guido van Rossum"
        ],
        "answer": "Bjarne Stroustrup"
    },
    {
        "q": "Q2. C++ is an extension of which language?",
        "options": [
            "C",
            "Java",
            "Python",
            "Assembly"
        ],
        "answer": "C"
    }
]

QUESTIONS_JAVA = [
    {
        "q": "Q1. Who developed Java programming language?",
        "options": [
            "James Gosling",
            "Dennis Ritchie",
            "Bjarne Stroustrup",
            "Guido van Rossum"
        ],
        "answer": "James Gosling"
    },
    {
        "q": "Q2. Java was developed at which company?",
        "options": [
            "Sun Microsystems",
            "Microsoft",
            "Google",
            "Apple"
        ],
        "answer": "Sun Microsystems"
    }
]

QUESTIONS_PYTHON = [
    {
        "q": "Q1. Who developed Python language?",
        "options": [
            "Guido van Rossum",
            "Dennis Ritchie",
            "James Gosling",
            "Bjarne Stroustrup"
        ],
        "answer": "Guido van Rossum"
    },
    {
        "q": "Q2. Python is which type of language?",
        "options": [
            "Interpreted language",
            "Compiled language",
            "Machine language",
            "Assembly language"
        ],
        "answer": "Interpreted language"
    }

]

QUESTIONS_OS = [
    {
        "q": "Q1. What is an Operating System?",
        "options": [
            "System software that manages hardware and software",
            "A programming language",
            "A web browser",
            "A database system"
        ],
        "answer": "System software that manages hardware and software"
    },
    {
        "q": "Q2. Which of the following is an Operating System?",
        "options": [
            "Windows",
            "Java",
            "HTML",
            "MySQL"
        ],
        "answer": "Windows"
    }
]

QUESTIONS_DBMS = [
    {
        "q": "Q1. What is DBMS?",
        "options": [
            "Software to manage and store data",
            "Programming language",
            "Operating system",
            "Web browser"
        ],
        "answer": "Software to manage and store data"
    },
    {
        "q": "Q2. Which of the following is a DBMS?",
        "options": [
            "MySQL",
            "Java",
            "Linux",
            "HTML"
        ],
        "answer": "MySQL"
    }
]

QUESTIONS_CN = [
    {
        "q": "Q1. What is a computer network?",
        "options": [
            "A system of connected computers to share data",
            "A type of software",
            "A programming language",
            "A database system"
        ],
        "answer": "A system of connected computers to share data"
    },
    {
        "q": "Q2. What does LAN stand for?",
        "options": [
            "Local Area Network",
            "Large Area Network",
            "Light Access Network",
            "Logical Area Network"
        ],
        "answer": "Local Area Network"
    }
]

QUESTIONS_DS = [
    {
        "q": "Q1. What is a data structure?",
        "options": [
            "A way to organize and store data",
            "A programming language",
            "An operating system",
            "A database software"
        ],
        "answer": "A way to organize and store data"
    },
    {
        "q": "Q2. Which data structure follows LIFO principle?",
        "options": [
            "Stack",
            "Queue",
            "Array",
            "Tree"
        ],
        "answer": "Stack"
    }
]

stud = [
    {
        'Sr_no':1,
        'Name':'John Doe',
        'username':'John',
        'email':'John@gmail.com',
        'password':'John@1234'
    },
    {
        'Sr_no':2,
        'Name':'Jane smith',
        'username':'Jone',
        'email':'Jane@gmail.com',
        'password':'Jone@1234'
    }
]

@app.route('/')
def Home():
        return render_template('Home.html',students=stud)
    
    
    



@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        conn = get_db()

        user = conn.execute(
            "SELECT * FROM SCORE WHERE Username = ?",
            (username,)
        ).fetchone()

        conn.close()

        if user and check_password_hash(user['Password'], password):

            session['username'] = user['Username']
            
            session['student_name'] = user['Student_name']
            session['role']=user['role']
            flash('Login Successful!', 'success')
            return redirect(url_for('technology'))

        else:
            flash('Invalid Username or Password!', 'danger')

    return render_template('login.html')



@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():

    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')
        new_password = request.form.get('new_password')

        conn = get_db()

        user = conn.execute(
            "SELECT * FROM SCORE WHERE Username=? AND Email=?",
            (username, email)
        ).fetchone()

        if user:

            hashed_password = generate_password_hash(new_password)

            conn.execute(
                "UPDATE SCORE SET Password=? WHERE Username=?",
                (hashed_password, username)
            )

            conn.commit()

            flash('Password Updated Successfully!', 'success')

            conn.close()

            return redirect(url_for('Login'))

        else:

            conn.close()

            flash('Invalid Username or Email!', 'danger')

            return redirect(url_for('forgot_password'))

    return render_template('forgot_password.html')

@app.route('/explore_technology')
def explore_technology():

    if 'sr_no' in session:
        return redirect(url_for('technology'))

    flash('Please Login or Register First!')
    return redirect(url_for('login'))


@app.route('/technology')
def technology():
    return render_template('technology.html')

@app.route('/web_development/<int:qno>', methods=['GET', 'POST'])
def web_development(qno):

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM QUESTIONS WHERE subject=?",
        ("Web Development",)
    ).fetchall()

    conn.close()

    all_questions = QUESTIONS.copy()

    for row in rows:
        all_questions.append({
            "q": row["question"],
            "options": [
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            ],
            "answer": row["answer"]
        })

    if len(all_questions) == 0:
        return "<h2>No Web Development Questions Found!</h2>"

    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":

        selected = request.form.get("answer")
        session[f"q{qno}"] = selected

        if "next" in request.form and qno < len(all_questions) - 1:
            return redirect(url_for("web_development", qno=qno + 1))

        if "prev" in request.form and qno > 0:
            return redirect(url_for("web_development", qno=qno - 1))

        if "submit" in request.form:

            score = 0

            for i in range(len(all_questions)):
                if session.get(f"q{i}") == all_questions[i]["answer"]:
                    score += 1

            session["score"] = score

            return redirect(url_for("Result"))

    return render_template(
        "web_development.html",
        question=all_questions[qno],
        qno=qno,
        total=len(all_questions)
    )


@app.route('/Artificial_Intelligence/<int:qno>', methods=['GET', 'POST'])
def Artificial_Intelligence(qno):

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM QUESTIONS WHERE subject=?",
        ("Artificial Intelligence",)
    ).fetchall()

    conn.close()

    all_questions = QUESTIONS1.copy()

    for row in rows:
        all_questions.append({
            "q": row["question"],
            "options": [
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            ],
            "answer": row["answer"]
        })

    if len(all_questions) == 0:
        return "<h2>No Artificial Intelligence Questions Found!</h2>"

    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":

        selected = request.form.get("answer")
        session[f"q{qno}"] = selected

        if "next" in request.form and qno < len(all_questions) - 1:
            return redirect(url_for("Artificial_Intelligence", qno=qno + 1))

        if "prev" in request.form and qno > 0:
            return redirect(url_for("Artificial_Intelligence", qno=qno - 1))

        if "submit" in request.form:

            score = 0

            for i in range(len(all_questions)):
                if session.get(f"q{i}") == all_questions[i]["answer"]:
                    score += 1

            session["score"] = score

            return redirect(url_for("Result"))

    return render_template(
        "Artificial_Intelligence.html",
        question=all_questions[qno],
        qno=qno,
        total=len(all_questions)
    )

@app.route('/data_science/<int:qno>', methods=['GET', 'POST'])
def data_science(qno):

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM QUESTIONS WHERE subject=?",
        ("Data Science",)
    ).fetchall()

    conn.close()

    all_questions = QUESTIONS2.copy()

    for row in rows:
        all_questions.append({
            "q": row["question"],
            "options": [
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            ],
            "answer": row["answer"]
        })

    if len(all_questions) == 0:
        return "<h2>No Data Science Questions Found!</h2>"

    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":

        selected = request.form.get("answer")
        session[f"q{qno}"] = selected

        if "next" in request.form and qno < len(all_questions) - 1:
            return redirect(url_for("data_science", qno=qno + 1))

        if "prev" in request.form and qno > 0:
            return redirect(url_for("data_science", qno=qno - 1))

        if "submit" in request.form:

            score = 0

            for i in range(len(all_questions)):
                if session.get(f"q{i}") == all_questions[i]["answer"]:
                    score += 1

            session["score"] = score

            return redirect(url_for("Result"))

    return render_template(
        "data_science.html",
        question=all_questions[qno],
        qno=qno,
        total=len(all_questions)
    )

@app.route('/cloud_computing/<int:qno>', methods=['GET', 'POST'])
def cloud_computing(qno):

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM QUESTIONS WHERE subject=?",
        ("Cloud Computing",)
    ).fetchall()

    conn.close()

    all_questions = QUESTIONS3.copy()

    for row in rows:
        all_questions.append({
            "q": row["question"],
            "options": [
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            ],
            "answer": row["answer"]
        })

    if len(all_questions) == 0:
        return "<h2>No Cloud Computing Questions Found!</h2>"

    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":

        selected = request.form.get("answer")
        session[f"q{qno}"] = selected

        if "next" in request.form and qno < len(all_questions) - 1:
            return redirect(url_for("cloud_computing", qno=qno + 1))

        if "prev" in request.form and qno > 0:
            return redirect(url_for("cloud_computing", qno=qno - 1))

        if "submit" in request.form:

            score = 0

            for i in range(len(all_questions)):
                if session.get(f"q{i}") == all_questions[i]["answer"]:
                    score += 1

            session["score"] = score

            return redirect(url_for("Result"))

    return render_template(
        "cloud_computing.html",
        question=all_questions[qno],
        qno=qno,
        total=len(all_questions)
    )

@app.route('/cyber_security/<int:qno>', methods=['GET', 'POST'])
def cyber_security(qno):

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM QUESTIONS WHERE subject=?",
        ("Cyber Security",)
    ).fetchall()

    conn.close()

    all_questions = QUESTIONS4.copy()

    for row in rows:
        all_questions.append({
            "q": row["question"],
            "options": [
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            ],
            "answer": row["answer"]
        })

    if len(all_questions) == 0:
        return "<h2>No Cyber Security Questions Found!</h2>"

    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":

        selected = request.form.get("answer")
        session[f"q{qno}"] = selected

        if "next" in request.form and qno < len(all_questions) - 1:
            return redirect(url_for("cyber_security", qno=qno + 1))

        if "prev" in request.form and qno > 0:
            return redirect(url_for("cyber_security", qno=qno - 1))

        if "submit" in request.form:

            score = 0

            for i in range(len(all_questions)):
                if session.get(f"q{i}") == all_questions[i]["answer"]:
                    score += 1

            session["score"] = score

            return redirect(url_for("Result"))

    return render_template(
        "cyber_security.html",
        question=all_questions[qno],
        qno=qno,
        total=len(all_questions)
    )

@app.route('/mobile_app_development/<int:qno>', methods=['GET', 'POST'])
def Mobile_App_Development(qno):

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM QUESTIONS WHERE subject=?",
        ("Mobile_App_Development",)
    ).fetchall()

    conn.close()

    all_questions = QUESTIONS5.copy()

    for row in rows:
        all_questions.append({
            "q": row["question"],
            "options": [
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            ],
            "answer": row["answer"]
        })

    if len(all_questions) == 0:
        return "<h2>No Mobile App Development Questions Found!</h2>"

    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":

        selected = request.form.get("answer")

        session[f"q{qno}"] = selected

        # NEXT
        if "next" in request.form and qno < len(all_questions) - 1:
            return redirect(url_for("Mobile_App_Development", qno=qno + 1))

        # PREVIOUS
        if "prev" in request.form and qno > 0:
            return redirect(url_for("Mobile_App_Development", qno=qno - 1))

        # SUBMIT
        if "submit" in request.form:

            score = 0

            for i in range(len(all_questions)):
                if session.get(f"q{i}") == all_questions[i]["answer"]:
                    score += 1

            session["score"] = score

            return redirect(url_for("Result"))

    return render_template(
        "mobile_app_development.html",
        question=all_questions[qno],
        qno=qno,
        total=len(all_questions)
    )




@app.route('/explore_programing_lang')
def explore_programing_lang():

    if 'sr_no' in session:
        return redirect(url_for('programing_lang'))

    flash('Please Login or Register First!')
    return redirect(url_for('login'))

@app.route('/programing_lang')
def programing_lang():
    return render_template('programing_lang.html')


@app.route('/c_lang/<int:qno>', methods=['GET', 'POST'])
def c_lang(qno):

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM QUESTIONS WHERE subject=?",
        ("C",)
    ).fetchall()

    conn.close()

    all_questions = QUESTIONS_C.copy()

    for row in rows:
        all_questions.append({
            "q": row["question"],
            "options": [
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            ],
            "answer": row["answer"]
        })

    if len(all_questions) == 0:
        return "<h2>No C Questions Found!</h2>"

    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":

        selected = request.form.get("answer")
        session[f"q{qno}"] = selected

        if "next" in request.form and qno < len(all_questions) - 1:
            return redirect(url_for("c_lang", qno=qno + 1))

        if "prev" in request.form and qno > 0:
            return redirect(url_for("c_lang", qno=qno - 1))

        if "submit" in request.form:

            score = 0

            for i in range(len(all_questions)):
                if session.get(f"q{i}") == all_questions[i]["answer"]:
                    score += 1

            session["score"] = score

            return redirect(url_for("Result"))

    return render_template(
        "c_lang.html",
        question=all_questions[qno],
        qno=qno,
        total=len(all_questions)
    )


@app.route('/cpp_lang/<int:qno>', methods=['GET', 'POST'])
def cpp_lang(qno):

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM QUESTIONS WHERE subject=?",
        ("C++",)
    ).fetchall()

    conn.close()

    all_questions = QUESTIONS_CPP.copy()

    for row in rows:
        all_questions.append({
            "q": row["question"],
            "options": [
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            ],
            "answer": row["answer"]
        })

    if len(all_questions) == 0:
        return "<h2>No C++ Questions Found!</h2>"

    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":

        selected = request.form.get("answer")
        session[f"q{qno}"] = selected

        if "next" in request.form and qno < len(all_questions) - 1:
            return redirect(url_for("cpp_lang", qno=qno + 1))

        if "prev" in request.form and qno > 0:
            return redirect(url_for("cpp_lang", qno=qno - 1))

        if "submit" in request.form:

            score = 0

            for i in range(len(all_questions)):
                if session.get(f"q{i}") == all_questions[i]["answer"]:
                    score += 1

            session["score"] = score

            return redirect(url_for("Result"))

    return render_template(
        "cpp_lang.html",
        question=all_questions[qno],
        qno=qno,
        total=len(all_questions)
    )

@app.route('/java_lang/<int:qno>', methods=['GET', 'POST'])
def java_lang(qno):

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM QUESTIONS WHERE subject=?",
        ("Java",)
    ).fetchall()

    conn.close()

    all_questions = QUESTIONS_JAVA.copy()

    for row in rows:
        all_questions.append({
            "q": row["question"],
            "options": [
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            ],
            "answer": row["answer"]
        })

    if len(all_questions) == 0:
        return "<h2>No Java Questions Found!</h2>"

    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":

        selected = request.form.get("answer")
        session[f"q{qno}"] = selected

        if "next" in request.form and qno < len(all_questions) - 1:
            return redirect(url_for("java_lang", qno=qno + 1))

        if "prev" in request.form and qno > 0:
            return redirect(url_for("java_lang", qno=qno - 1))

        if "submit" in request.form:

            score = 0

            for i in range(len(all_questions)):
                if session.get(f"q{i}") == all_questions[i]["answer"]:
                    score += 1

            session["score"] = score

            return redirect(url_for("Result"))

    return render_template(
        "java_lang.html",
        question=all_questions[qno],
        qno=qno,
        total=len(all_questions)
    )

@app.route('/python_lang/<int:qno>', methods=['GET', 'POST'])
def python_lang(qno):

    # Database madhun Python questions ghya
    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM QUESTIONS WHERE subject=?",
        ("Python",)
    ).fetchall()

    conn.close()

    # Pahile dictionary madhle questions
    all_questions = QUESTIONS_PYTHON.copy()

    # Database madhle questions add kara
    for row in rows:
        all_questions.append({
            "q": row["question"],
            "options": [
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            ],
            "answer": row["answer"]
        })

    # Questions nasel tar
    if len(all_questions) == 0:
        return "<h2>No Python Questions Found!</h2>"

    if "score" not in session:
        session["score"] = 0

    # POST Request
    if request.method == "POST":

        selected = request.form.get("answer")

        # User answer save kara
        session[f"q{qno}"] = selected

        # Next button
        if "next" in request.form and qno < len(all_questions) - 1:
            return redirect(url_for("python_lang", qno=qno + 1))

        # Previous button
        if "prev" in request.form and qno > 0:
            return redirect(url_for("python_lang", qno=qno - 1))

        # Submit button
        if "submit" in request.form:

            score = 0

            for i in range(len(all_questions)):
                if session.get(f"q{i}") == all_questions[i]["answer"]:
                    score += 1

            session["score"] = score

            return redirect(url_for("Result"))

    return render_template(
        "python_lang.html",
        question=all_questions[qno],
        qno=qno,
        total=len(all_questions)
    )


@app.route('/explore_computer_science')
def explore_computer_science():

    if 'sr_no' in session:
        return redirect(url_for('computer_science'))

    flash('Please Login or Register First!')
    return redirect(url_for('login'))

@app.route('/computer_science')
def computer_science():
    return render_template('Computer_seience.html')


@app.route('/operating_system/<int:qno>', methods=['GET', 'POST'])
def operating_system(qno):

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM QUESTIONS WHERE subject=?",
        ("Operating System",)
    ).fetchall()

    conn.close()

    all_questions = QUESTIONS_OS.copy()

    for row in rows:
        all_questions.append({
            "q": row["question"],
            "options": [
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            ],
            "answer": row["answer"]
        })

    if len(all_questions) == 0:
        return "<h2>No Operating System Questions Found!</h2>"

    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":

        selected = request.form.get("answer")
        session[f"q{qno}"] = selected

        if "next" in request.form and qno < len(all_questions) - 1:
            return redirect(url_for("operating_system", qno=qno + 1))

        if "prev" in request.form and qno > 0:
            return redirect(url_for("operating_system", qno=qno - 1))

        if "submit" in request.form:

            score = 0

            for i in range(len(all_questions)):
                if session.get(f"q{i}") == all_questions[i]["answer"]:
                    score += 1

            session["score"] = score

            return redirect(url_for("Result"))

    return render_template(
        "operating_system.html",
        question=all_questions[qno],
        qno=qno,
        total=len(all_questions)
    )


@app.route('/dbms_lang/<int:qno>', methods=['GET', 'POST'])
def dbms_lang(qno):

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM QUESTIONS WHERE subject=?",
        ("DBMS",)
    ).fetchall()

    conn.close()

    all_questions = QUESTIONS_DBMS.copy()

    for row in rows:
        all_questions.append({
            "q": row["question"],
            "options": [
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            ],
            "answer": row["answer"]
        })

    if len(all_questions) == 0:
        return "<h2>No DBMS Questions Found!</h2>"

    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":

        selected = request.form.get("answer")
        session[f"q{qno}"] = selected

        if "next" in request.form and qno < len(all_questions) - 1:
            return redirect(url_for("dbms_lang", qno=qno + 1))

        if "prev" in request.form and qno > 0:
            return redirect(url_for("dbms_lang", qno=qno - 1))

        if "submit" in request.form:

            score = 0

            for i in range(len(all_questions)):
                if session.get(f"q{i}") == all_questions[i]["answer"]:
                    score += 1

            session["score"] = score

            return redirect(url_for("Result"))

    return render_template(
        "dbms_lang.html",
        question=all_questions[qno],
        qno=qno,
        total=len(all_questions)
    )

@app.route('/computer_network/<int:qno>', methods=['GET', 'POST'])
def computer_network(qno):

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM QUESTIONS WHERE subject=?",
        ("Computer Network",)
    ).fetchall()

    conn.close()

    all_questions = QUESTIONS_CN.copy()

    for row in rows:
        all_questions.append({
            "q": row["question"],
            "options": [
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            ],
            "answer": row["answer"]
        })

    if len(all_questions) == 0:
        return "<h2>No Computer Network Questions Found!</h2>"

    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":

        selected = request.form.get("answer")
        session[f"q{qno}"] = selected

        if "next" in request.form and qno < len(all_questions) - 1:
            return redirect(url_for("computer_network", qno=qno + 1))

        if "prev" in request.form and qno > 0:
            return redirect(url_for("computer_network", qno=qno - 1))

        if "submit" in request.form:

            score = 0

            for i in range(len(all_questions)):
                if session.get(f"q{i}") == all_questions[i]["answer"]:
                    score += 1

            session["score"] = score

            return redirect(url_for("Result"))

    return render_template(
        "computer_network.html",
        question=all_questions[qno],
        qno=qno,
        total=len(all_questions)
    )

@app.route('/data_structure/<int:qno>', methods=['GET', 'POST'])
def data_structure(qno):

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM QUESTIONS WHERE subject=?",
        ("Data Structure",)
    ).fetchall()

    conn.close()

    all_questions = QUESTIONS_DS.copy()

    for row in rows:
        all_questions.append({
            "q": row["question"],
            "options": [
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            ],
            "answer": row["answer"]
        })

    if len(all_questions) == 0:
        return "<h2>No Data Structure Questions Found!</h2>"

    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":

        selected = request.form.get("answer")
        session[f"q{qno}"] = selected

        if "next" in request.form and qno < len(all_questions) - 1:
            return redirect(url_for("data_structure", qno=qno + 1))

        if "prev" in request.form and qno > 0:
            return redirect(url_for("data_structure", qno=qno - 1))

        if "submit" in request.form:

            score = 0

            for i in range(len(all_questions)):
                if session.get(f"q{i}") == all_questions[i]["answer"]:
                    score += 1

            session["score"] = score

            return redirect(url_for("Result"))

    return render_template(
        "data_structure.html",
        question=all_questions[qno],
        qno=qno,
        total=len(all_questions)
    )


@app.route('/logout')
def logout():
    
    session.pop('username', None)
    session.pop('role', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('Home'))

@app.route('/subjects')
def subjects():
    conn=get_db()
    rows = conn.execute('''
                        SELECT subject AS subject_name, COUNT(*) AS student_count
                        FROM SCORE
                        GROUP BY subject
                        ORDER BY subject
                        ''').fetchall()
    conn.close()
    return render_template('subjects.html',rows=rows)



@app.route('/Register', methods=['GET', 'POST'])
def Register():
    #if session.get('role')!='admin':
    #    flash("Admin only! you do not have permission","danger")
    #    return redirect(url_for('Home'))
    
    if request.method == 'POST':

        student_name = request.form.get('student_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        subject = request.form.get('subject')

        if not student_name or not username or not email or not password or not subject:
            flash('Please provide all details!', 'danger')
            return redirect(url_for('Register'))

        # Password Hashing
        hashed_password = generate_password_hash(password)

        conn = get_db()

        conn.execute(
            '''
            INSERT INTO SCORE
            (Student_name, total_marks, Username, Email, Password, Subject)
            VALUES (?, ?, ?, ?, ?, ?)
            ''',
            (student_name, 0, username, email, hashed_password, subject)
        )

        conn.commit()
        conn.close()

        flash('Registration Successful!', 'success')
        return redirect(url_for('Register'))

    return render_template('Register.html')


@app.route('/search')
def search():
    q = request.args.get('q', '')
    conn = get_db()

    if q:
        students = conn.execute(
            '''SELECT * FROM SCORE
               WHERE Student_name LIKE ?
               OR Username LIKE ?''',
            (f'%{q}%', f'%{q}%')
        ).fetchall()
    else:
        students = conn.execute(
            'SELECT * FROM SCORE ORDER BY Sr_no ASC'
        ).fetchall()

    conn.close()

    return render_template(
        'search.html',
        students=students,
        query=q
    )



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Add_Question', methods=['GET', 'POST'])
def Add_Question():
    
    if request.method == "POST":

        subject = request.form.get('subject')
        question = request.form.get('question')
        option1 = request.form.get('option1')
        option2 = request.form.get('option2')
        option3 = request.form.get('option3')
        option4 = request.form.get('option4')
        answer = request.form.get('answer')

        if not subject or not question or not option1 or not option2 or not option3 or not option4 or not answer:
            flash('Please fill all fields!', 'danger')
            return render_template("Add_Question.html")

        conn = get_db()

        conn.execute(
            '''
            INSERT INTO QUESTIONS
            (subject,question, option1, option2, option3, option4, answer)
            VALUES (?,?, ?, ?, ?, ?, ?)
            ''',
            (subject,question, option1, option2, option3, option4, answer)
        )

        conn.commit()
        conn.close()

        flash("Question Added Successfully!", "success")

        return redirect(url_for('Add_Question'))

    return render_template('Add_Question.html')


@app.route("/students")
def students():
    if session.get('role')!='admin':
        flash("Admin only! you do not have permission","danger")
        return redirect(url_for('Home'))

    conn = get_db()
    db_students = conn.execute(
        'SELECT * FROM SCORE ORDER BY Sr_no ASC'
    ).fetchall()
    conn.close()

    combined_students = []

    # Database Data
    for s in db_students:
        combined_students.append({
        'Sr_no': s['Sr_no'],
        'Name': s['Student_name'],
        'username': s['Username'],
        'email': s['Email']
        #'password': s['Password']
    })

    return render_template(
        "students.html",
        students=combined_students
    )

@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    conn= get_db()
    subjects = conn.execute('SELECT * FROM subjects').fetchall()
    # subjects list - needed to populate the dropdown in the form
    if request.method == "POST":
        name = request.form['name'].strip()
        subject_id = request.form['subject_id']
        conn.execute('INSERT INTO students (name, subject_id) VALUES (?, ?)', (name, subject_id))
        conn.commit()
        conn.close()
        flash(f"Student '{name}' added successfully!")
        return redirect(url_for('students'))
    return render_template("add_student.html", subjects=subjects)
    
@app.route('/view_student/<int:Sr_no>')
def view_student(Sr_no):

    conn = get_db()

    student = conn.execute(
        "SELECT * FROM SCORE WHERE Sr_no=?",
        (Sr_no,)
    ).fetchone()

    conn.close()

    return render_template('view_student.html', students=student)


@app.route('/delete_candidate/<int:Sr_no>')
def delete_candidate(Sr_no):
        

    if session.get('role')!='admin':
        flash("Admin only! you do not have permission","danger")
        return redirect(url_for('Home'))

    conn = get_db()

    student = conn.execute(
            'SELECT * FROM SCORE WHERE Sr_no=?',
            (Sr_no,)
            ).fetchone()
    if student is None:
                flash("student not found","danger")
                conn.close()
            
    conn.execute(
            'DELETE FROM SCORE WHERE Sr_no=?',
            (Sr_no,)
            )
    conn.commit()
    conn.close()
    flash("candidate deleted successfully","success")
    return redirect(url_for('students'))

@app.route('/edit_student/<int:Sr_no>', methods=['GET', 'POST'])
def edit_student(Sr_no):
    if session.get('role')!='admin':
        flash("Admin only! you do not have permission","danger")
        return redirect(url_for('Home'))

    conn = get_db()

    if request.method == 'POST':

        Candidate_name = request.form['Candidate_name']

        conn.execute(
            "UPDATE SCORE SET student_name=? WHERE Sr_no=?",
            (Candidate_name, Sr_no)
        )

        conn.commit()
        conn.close()

        return redirect(url_for('students'))

    student = conn.execute(
        "SELECT * FROM SCORE WHERE Sr_no=?",
        (Sr_no,)
    ).fetchone()

    conn.close()

    return render_template('edit_student.html', student=student)


@app.route('/filter')
def filter():

    subject = request.args.get('subject')

    conn = get_db()

    if subject:
        students = conn.execute(
            "SELECT * FROM SCORE WHERE subject=?",
            (subject,)
        ).fetchall()
    else:
        students = conn.execute(
            "SELECT * FROM SCORE"
        ).fetchall()

    conn.close()

    return render_template(
        'filter_result.html',
        students=students
    )

@app.route('/Subject')
def Subject():
    return render_template('Subject.html')


@app.route('/Result')
def Result():
    score = session.get("score", 0)
    total = len(QUESTIONS)

    return render_template("result.html", score=score, total=total)
    

init_db()
if __name__ == '__main__':
    
    app.run(debug=True)