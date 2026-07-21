
from flask import Flask, request
import random
import os
import sqlite3  # NEW
app = Flask(__name__)
# Create database and table
def init_db():
    conn = sqlite3.connect('applicants.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS applicants
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  app_num TEXT, name TEXT, email TEXT, phone TEXT, dob TEXT,
                  gender TEXT, marital TEXT, religion TEXT, state TEXT, lga TEXT,
                  country TEXT, id_type TEXT, work TEXT, passport TEXT)''')
    conn.commit()
    conn.close()

init_db()  # run it when app starts

UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <style>
                body {background-color: #1a1a2e; color: #ffffff; font-family: Arial; text-align: center; padding-top: 50px;}
                h1 { color: #00ff88; font-size: 40px; }
                button {background-color: #00ff88; color: #1a1a2e; border: none; padding: 15px 30px; font-size: 18px; border-radius: 10px; cursor: pointer; margin-top: 10px;}
                button:hover { background-color: #ff00ff; }
                a {color: #00ff88; text-decoration: none; font-size: 20px;}
                img {border-radius: 20px; margin: 20px; max-width: 80%;}
                input, textarea {width: 60%; padding: 10px; margin: 10px; border-radius: 8px; border: none; font-size: 16px;}
                .form-box {background-color: #0f3460; padding: 20px; border-radius: 15px; width: 70%; margin: 30px auto;}
            </style>
        </head>
        <body>
            <h1> SEN. NATASHA SUPPORTERS NETWORK 🎉</h1>
            <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600" alt="Coding">
            <p>Built with Flask + Python</p>
            <button onclick="alert('You clicked the button!')">PROJECTS</button>
            <br><br>
<a href="/">Home</a> | 
<a href="/about">About</a> | 
<a href="/services">Services</a> | 
<a href="/portfolio">Portfolio</a> | 
<a href="/blog">Blog</a> | 
<a href="/testimonials">Testimonials</a> | 
<a href="/signup">Sign Up</a> | 
<a href="/profile">Profile</a> | 
<a href="/contact">Contact</a>

            <div class="form-box">
                <h2>Contact Me</h2>
                <input type="text" placeholder="Your Name">
                <br>
                <textarea rows="4" placeholder="Your Message"></textarea>
                <br>
                <button onclick="alert('Thanks for your message!')">Send</button>
            </div>
        </body>
    </html>
    """

@app.route("/about")
def about():
    return """
    <html>
        <head>
            <style>
                body {background-color: #16213e; color: #ffffff; font-family: Arial; text-align: center; padding-top: 100px;}
                h1 { color: #ff00ff; font-size: 40px; }
                a {color: #00ff88; text-decoration: none; font-size: 20px;}
            </style>
        </head>
        <body>
            <h1>About Me</h1>
            <p>This is my first Flask website built!</p>
            <a href="/">← Back to Home</a>
        </body>
    </html>
    """
@app.route("/services")
def services():
    return """
    <html>
        <head>
            <style>
                body {background-color: #0f3460; color: #ffffff; font-family: Arial; text-align: center; padding-top: 100px;}
                h1 { color: #00ff88; font-size: 40px; }
                a {color: #00ff88; text-decoration: none; font-size: 20px; margin: 15px;}
            </style>
        </head>
        <body>
            <h1>My Services</h1>
            <p>I build websites with Flask + Python</p>
            <p>1. Web Design</p>
            <p>2. Python Apps</p>
            <p>3. Business Websites</p>
            <br>
            <a href="/">← Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
        </body>
    </html>
    """

@app.route("/contact")
def contact():
    return """
    <html>
        <head>
            <style>
                body {background-color: #16213e; color: #ffffff; font-family: Arial; text-align: center; padding-top: 100px;}
                h1 { color: #ff00ff; font-size: 40px; }
                a {color: #00ff88; text-decoration: none; font-size: 20px; margin: 15px;}
            </style>
        </head>
        <body>
            <h1>Contact Me</h1>
            <p>Email: youremail@gmail.com</p>
            <p>Location: Onitsha, Nigeria</p>
            <br>
            <a href="/">← Home</a>
            <a href="/about">About</a>
            <a href="/services">Services</a>
        </body>
    </html>
    """
@app.route("/profile")
def profile():
    app_num = request.args.get('app', '')
    
    if not app_num:
        return "<h1>No Application Found</h1><a href='/signup'>Register First</a>"
    
    # Get data from database
    conn = sqlite3.connect('applicants.db')
    c = conn.cursor()
    c.execute("SELECT * FROM applicants WHERE app_num = ?", (app_num,))
    data = c.fetchone()
    conn.close()
    
    if not data:
        return f"<h1>Application {app_num} Not Found</h1><a href='/signup'>Register</a>"
    
    # data order: id, app_num, name, email, phone, dob, gender, marital, religion, state, lga, country, id_type, work, passport
    _, app_num, name, email, phone, dob, gender, marital, religion, state, lga, country, id_type, work, passport = data
    
    return f"""
    <html>
        <head>
            <style>
                body {{background-color: #16213e; color: #ffffff; font-family: Arial; text-align: center; padding: 0; margin: 0;}}
                .navbar {{background-color: #0f3460; padding: 15px; text-align: center;}}
                .navbar a {{color: #00ff88; text-decoration: none; font-size: 16px; margin: 0 10px;}}
                h1 {{ color: #ff00ff; font-size: 40px; margin-top: 40px; }}
                .app-number {{background-color: #00ff88; color: #1a1a2e; padding: 10px 20px; border-radius: 10px; font-size: 20px; font-weight: bold; display: inline-block; margin-bottom: 20px;}}
                .profile-card {{background-color: #1a1a2e; padding: 40px; border-radius: 15px; width: 600px; margin: 30px auto; text-align: left;}}
                img {{border-radius: 50%; width: 120px; height: 120px; border: 4px solid #00ff88; margin-bottom: 20px; object-fit: cover; display: block; margin: 0 auto;}}
                .info {{font-size: 18px; line-height: 2;}}
                .info b {{color: #00ff88;}}
            </style>
        </head>
        <body>
            <div class="navbar">
                <a href="/">Home</a> | <a href="/signup">Sign Up</a> | <a href="/profile">Profile</a>
            </div>

            <h1>Applicant Dashboard</h1>
            <div class="profile-card">
                <p style="text-align: center;">Application Number:</p>
                <div class="app-number">{app_num}</div>
                
                <img src="/static/uploads/{passport}" alt="Passport">
                <h2 style="text-align: center;">Welcome, {name}!</h2>
                
                <div class="info">
                    <p><b>Email:</b> {email}</p>
                    <p><b>Phone:</b> {phone}</p>
                    <p><b>Date of Birth:</b> {dob}</p>
                    <p><b>Gender:</b> {gender}</p>
                    <p><b>Marital Status:</b> {marital}</p>
                    <p><b>Religion:</b> {religion}</p>
                    <p><b>State:</b> {state}</p>
                    <p><b>LGA:</b> {lga}</p>
                    <p><b>Country:</b> {country}</p>
                    <p><b>Mode of ID:</b> {id_type}</p>
                    <p><b>Nature of Work:</b> {work}</p>
                    <p><b>Status:</b> Active</p>
                </div>
            </div>
        </body>
    </html>
    """
@app.route("/blog")
def blog():
    return """
    <html>
        <head>
            <style>
                body {background-color: #16213e; color: #ffffff; font-family: Arial; text-align: center; padding-top: 80px;}
                h1 { color: #ff00ff; font-size: 40px; }
                .post {background-color: #1a1a2e; margin: 20px auto; padding: 20px; border-radius: 15px; width: 70%; text-align: left;}
                a {color: #00ff88; text-decoration: none; font-size: 18px; margin: 15px;}
            </style>
        </head>
        <body>
            <h1>My Blog</h1>
            <div class="post">
                <h2>Post 1: How I Built My First Website in Onitsha</h2>
                <p>Today I learned Flask. It was easier than I thought...</p>
            </div>
            <div class="post">
                <h2>Post 2: Python Tips for Beginners</h2>
                <p>Coming soon...</p>
            </div>
            <br>
            <a href="/">Home</a> | <a href="/about">About</a> | <a href="/services">Services</a> | <a href="/portfolio">Portfolio</a> | <a href="/testimonials">Testimonials</a> | <a href="/contact">Contact</a>
        </body>
    </html>
    """

@app.route("/testimonials")
def testimonials():
    return """
    <html>
        <head>
            <style>
                body {background-color: #0f3460; color: #ffffff; font-family: Arial; text-align: center; padding-top: 80px;}
                h1 { color: #00ff88; font-size: 40px; }
                .testimonial {background-color: #16213e; margin: 20px auto; padding: 20px; border-radius: 15px; width: 70%; font-style: italic;}
                a {color: #00ff88; text-decoration: none; font-size: 18px; margin: 15px;}
            </style>
        </head>
        <body>
            <h1>What People Say</h1>
            <div class="testimonial">
                <p>"Amazing work! Built my site so fast."</p>
                <p>- Client A, Ismail</p>
            </div>
            <div class="testimonial">
                <p>"Professional and clean design."</p>
                <p>- Client B</p>
            </div>
            <br>
            <a href="/">Home</a> | <a href="/about">About</a> | <a href="/services">Services</a> | <a href="/portfolio">Portfolio</a> | <a href="/blog">Blog</a> | <a href="/contact">Contact</a>
        </body>
    </html>
    """
import random  # add this at the very top of app.py with your other imports

import os  # add with your other imports at top

# Create a folder to store uploads
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

states_lga = {
    "Abia": ["Aba North", "Aba South", "Arochukwu", "Bende", "Ikwuano", "Isiala Ngwa North", "Isiala Ngwa South", "Isuikwuato", "Obi Ngwa", "Ohafia", "Osisioma", "Ugwunagbo", "Ukwa East", "Ukwa West", "Umuahia North", "Umuahia South", "Umunneochi"],
    "Adamawa": ["Demsa", "Fufure", "Ganye", "Gayuk", "Gombi", "Grie", "Hong", "Jada", "Lamurde", "Madagali", "Maiha", "Mayo Belwa", "Michika", "Mubi North", "Mubi South", "Numan", "Shelleng", "Song", "Toungo", "Yola North", "Yola South"],
    "Akwa Ibom": ["Abak", "Eastern Obolo", "Eket", "Esit Eket", "Essien Udim", "Etim Ekpo", "Etinan", "Ibeno", "Ibesikpo Asutan", "Ibiono-Ibom", "Ika", "Ikono", "Ikot Abasi", "Ikot Ekpene", "Ini", "Itu", "Mbo", "Mkpat-Enin", "Nsit-Atai", "Nsit-Ibom", "Nsit-Ubium", "Obot Akara", "Okobo", "Onna", "Oron", "Udung-Uko", "Ukanafun", "Uruan", "Urue-Offong/Oruko", "Uyo"],
    "Anambra": ["Aguata", "Anambra East", "Anambra West", "Anaocha", "Awka North", "Awka South", "Ayamelum", "Dunukofia", "Ekwusigo", "Idemili North", "Idemili South", "Ihiala", "Njikoka", "Nnewi North", "Nnewi South", "Ogbaru", "Onitsha North", "Onitsha South", "Orumba North", "Orumba South", "Oyi"],
    "Bauchi": ["Alkaleri", "Bauchi", "Bogoro", "Damban", "Darazo", "Dass", "Gamawa", "Ganjuwa", "Giade", "Itas/Gadau", "Jama'are", "Katagum", "Kirfi", "Misau", "Ningi", "Shira", "Tafawa Balewa", "Toro", "Warji", "Zaki"],
    "Bayelsa": ["Brass", "Ekeremor", "Kolokuma/Opokuma", "Nembe", "Ogbia", "Sagbama", "Southern Ijaw", "Yenagoa"],
    "Benue": ["Agatu", "Apa", "Ado", "Buruku", "Gboko", "Guma", "Gwer East", "Gwer West", "Katsina-Ala", "Konshisha", "Kwande", "Logo", "Makurdi", "Obi", "Ogbadibo", "Ohimini", "Oju", "Okpokwu", "Oturkpo", "Tarka", "Ukum", "Ushongo", "Vandeikya"],
    "Borno": ["Abadam", "Askira/Uba", "Bama", "Bayo", "Biu", "Chibok", "Damboa", "Dikwa", "Gubio", "Guzamala", "Gwoza", "Hawul", "Jere", "Kaga", "Kala/Balge", "Konduga", "Kukawa", "Kwaya Kusar", "Mafa", "Magumeri", "Maiduguri", "Marte", "Mobbar", "Monguno", "Ngala", "Nganzai", "Shani"],
    "Cross River": ["Abi", "Akamkpa", "Akpabuyo", "Bakassi", "Bekwarra", "Biase", "Boki", "Calabar Municipal", "Calabar South", "Etung", "Ikom", "Obanliku", "Obubra", "Obudu", "Odukpani", "Ogoja", "Yakuur", "Yala"],
    "Delta": ["Aniocha North", "Aniocha South", "Bomadi", "Burutu", "Ethiope East", "Ethiope West", "Ika North East", "Ika South", "Isoko North", "Isoko South", "Ndokwa East", "Ndokwa West", "Okpe", "Oshimili North", "Oshimili South", "Patani", "Sapele", "Udu", "Ughelli North", "Ughelli South", "Ukwuani", "Uvwie", "Warri North", "Warri South", "Warri South West"],
    "Ebonyi": ["Abakaliki", "Afikpo North", "Afikpo South", "Ebonyi", "Ezza North", "Ezza South", "Ikwo", "Ishielu", "Ivo", "Izzi", "Ohaozara", "Ohaukwu", "Onicha"],
    "Edo": ["Akoko-Edo", "Egor", "Esan Central", "Esan North-East", "Esan South-East", "Esan West", "Etsako Central", "Etsako East", "Etsako West", "Igueben", "Ikpoba Okha", "Orhionmwon", "Oredo", "Ovia North-East", "Ovia South-West", "Owan East", "Owan West", "Uhunmwonde"],
    "Ekiti": ["Ado Ekiti", "Efon", "Ekiti East", "Ekiti South-West", "Ekiti West", "Emure", "Gbonyin", "Ido Osi", "Ijero", "Ikere", "Ikole", "Ilejemeje", "Irepodun/Ifelodun", "Ise/Orun", "Moba", "Oye"],
    "Enugu": ["Aninri", "Awgu", "Enugu East", "Enugu North", "Enugu South", "Ezeagu", "Igbo Etiti", "Igbo Eze North", "Igbo Eze South", "Isi Uzo", "Nkanu East", "Nkanu West", "Nsukka", "Oji River", "Udenu", "Udi", "Uzo Uwani"],
    "FCT": ["Abaji", "Bwari", "Gwagwalada", "Kuje", "Kwali", "Municipal Area Council"],
    "Gombe": ["Akko", "Balanga", "Billiri", "Dukku", "Funakaye", "Gombe", "Kaltungo", "Kwami", "Nafada", "Shongom", "Yamaltu/Deba"],
    "Imo": ["Aboh Mbaise", "Ahiazu Mbaise", "Ehime Mbano", "Ezinihitte", "Ideato North", "Ideato South", "Ihitte/Uboma", "Ikeduru", "Isiala Mbano", "Isu", "Mbaitoli", "Ngor Okpala", "Njaba", "Nkwerre", "Nwangele", "Obowo", "Oguta", "Ohaji/Egbema", "Okigwe", "Orlu", "Orsu", "Oru East", "Oru West", "Owerri Municipal", "Owerri North", "Owerri West"],
    "Jigawa": ["Auyo", "Babura", "Biriniwa", "Birnin Kudu", "Buji", "Dutse", "Gagarawa", "Garki", "Gumel", "Guri", "Gwaram", "Gwiwa", "Hadejia", "Jahun", "Kafin Hausa", "Kaugama", "Kazaure", "Kiri Kasama", "Kiyawa", "Maigatari", "Malam Madori", "Miga", "Ringim", "Roni", "Sule Tankarkar", "Taura", "Yankwashi"],
    "Kaduna": ["Birnin Gwari", "Chikun", "Giwa", "Igabi", "Ikara", "Jaba", "Jema'a", "Kachia", "Kaduna North", "Kaduna South", "Kagarko", "Kajuru", "Kaura", "Kauru", "Kubau", "Kudan", "Lere", "Makarfi", "Sabon Gari", "Sanga", "Soba", "Zangon Kataf", "Zaria"],
    "Kano": ["Ajingi", "Albasu", "Bagwai", "Bebeji", "Bichi", "Bunkure", "Dala", "Dambatta", "Dawakin Kudu", "Dawakin Tofa", "Doguwa", "Fagge", "Gabasawa", "Garko", "Garun Mallam", "Gaya", "Gezawa", "Gwale", "Gwarzo", "Kabo", "Kano Municipal", "Karaye", "Kibiya", "Kiru", "Kumbotso", "Kunchi", "Kura", "Madobi", "Makoda", "Minjibir", "Nasarawa", "Rano", "Rimin Gado", "Rogo", "Shanono", "Sumaila", "Takai", "Tarauni", "Tofa", "Tsanyawa", "Tudun Wada", "Ungogo", "Warawa", "Wudil"],
    "Katsina": ["Bakori", "Batagarawa", "Batsari", "Baure", "Bindawa", "Charanchi", "Dandume", "Danja", "Dan Musa", "Daura", "Dutsi", "Dutsin Ma", "Faskari", "Funtua", "Ingawa", "Jibia", "Kafur", "Kaita", "Kankara", "Kankia", "Katsina", "Kurfi", "Kusada", "Mai'Adua", "Malumfashi", "Mani", "Mashi", "Matazu", "Musawa", "Rimi", "Sabuwa", "Safana", "Sandamu", "Zango"],
    "Kebbi": ["Aleiro", "Arewa Dandi", "Argungu", "Augie", "Bagudo", "Birnin Kebbi", "Bunza", "Dandi", "Fakai", "Gwandu", "Jega", "Kalgo", "Koko/Besse", "Maiyama", "Ngaski", "Sakaba", "Shanga", "Suru", "Wasagu/Danko", "Yauri", "Zuru"],
    "Kogi": ["Adavi", "Ajaokuta", "Ankpa", "Bassa", "Dekina", "Ibaji", "Idah", "Igalamela Odolu", "Ijumu", "Kabba/Bunu", "Kogi", "Lokoja", "Mopa Muro", "Ofu", "Ogori/Magongo", "Okehi", "Okene", "Olamaboro", "Omala", "Yagba East", "Yagba West"],
    "Kwara": ["Asa", "Baruten", "Edu", "Ekiti", "Ifelodun", "Ilorin East", "Ilorin South", "Ilorin West", "Irepodun", "Isin", "Kaiama", "Moro", "Offa", "Oke Ero", "Oyun", "Pategi"],
    "Lagos": ["Agege", "Ajeromi-Ifelodun", "Alimosho", "Amuwo-Odofin", "Apapa", "Badagry", "Epe", "Eti Osa", "Ibeju-Lekki", "Ifako-Ijaiye", "Ikeja", "Ikorodu", "Kosofe", "Lagos Island", "Lagos Mainland", "Mushin", "Ojo", "Oshodi-Isolo", "Shomolu", "Surulere"],
    "Nasarawa": ["Akwanga", "Awe", "Doma", "Karu", "Keana", "Keffi", "Kokona", "Lafia", "Nasarawa", "Nasarawa Egon", "Obi", "Toto", "Wamba"],
    "Niger": ["Agaie", "Agwara", "Bida", "Borgu", "Bosso", "Chanchaga", "Edati", "Gbako", "Gurara", "Katcha", "Kontagora", "Lapai", "Lavun", "Magama", "Mariga", "Mashegu", "Mokwa", "Moya", "Paikoro", "Rafi", "Rijau", "Shiroro", "Suleja", "Tafa", "Wushishi"],
    "Ogun": ["Abeokuta North", "Abeokuta South", "Ado-Odo/Ota", "Egbado North", "Egbado South", "Ewekoro", "Ifo", "Ijebu East", "Ijebu North", "Ijebu North East", "Ijebu Ode", "Ikenne", "Imeko Afon", "Ipokia", "Obafemi Owode", "Odeda", "Odogbolu", "Ogun Waterside", "Remo North", "Shagamu"],
    "Ondo": ["Akoko North-East", "Akoko North-West", "Akoko South-East", "Akoko South-West", "Akure North", "Akure South", "Ese Odo", "Idanre", "Ifedore", "Ilaje", "Ile Oluji/Okeigbo", "Irele", "Odigbo", "Okitipupa", "Ondo East", "Ondo West", "Ose", "Owo"],
    "Osun": ["Atakunmosa East", "Atakunmosa West", "Aiyedaade", "Aiyedire", "Boluwaduro", "Boripe", "Ede North", "Ede South", "Ife Central", "Ife East", "Ife North", "Ife South", "Ifedayo", "Ifelodun", "Ila", "Ilesa East", "Ilesa West", "Irepodun", "Irewole", "Isokan", "Iwo", "Obokun", "Odo Otin", "Ola Oluwa", "Olorunda", "Oriade", "Orolu", "Osogbo"],
    "Oyo": ["Afijio", "Akinyele", "Atiba", "Atisbo", "Egbeda", "Ibadan North", "Ibadan North-East", "Ibadan North-West", "Ibadan South-East", "Ibadan South-West", "Ibarapa Central", "Ibarapa East", "Ibarapa North", "Ido", "Irepo", "Iseyin", "Itesiwaju", "Iwajowa", "Kajola", "Lagelu", "Ogbomosho North", "Ogbomosho South", "Ogo Oluwa", "Olorunsogo", "Oluyole", "Ona Ara", "Orelope", "Ori Ire", "Oyo", "Oyo East", "Saki East", "Saki West", "Surulere"],
    "Plateau": ["Barkin Ladi", "Bassa", "Bokkos", "Jos East", "Jos North", "Jos South", "Kanam", "Kanke", "Langtang North", "Langtang South", "Mangu", "Mikang", "Pankshin", "Qua'an Pan", "Riyom", "Shendam", "Wase"],
    "Rivers": ["Abua/Odual", "Ahoada East", "Ahoada West", "Akuku-Toru", "Andoni", "Asari-Toru", "Bonny", "Degema", "Eleme", "Emohua", "Etche", "Gokana", "Ikwerre", "Khana", "Obio-Akpor", "Ogba/Egbema/Ndoni", "Ogu/Bolo", "Okrika", "Omuma", "Opobo/Nkoro", "Port Harcourt", "Tai"],
    "Sokoto": ["Binji", "Bodinga", "Dange Shuni", "Gada", "Goronyo", "Gudu", "Gwadabawa", "Illela", "Isa", "Kebbe", "Kware", "Rabah", "Sabon Birni", "Shagari", "Silame", "Sokoto North", "Sokoto South", "Tambuwal", "Tangaza", "Tureta", "Wamako", "Wurno", "Yabo"],
    "Taraba": ["Ardo Kola", "Bali", "Donga", "Gashaka", "Gassol", "Ibi", "Jalingo", "Karim Lamido", "Kumi", "Lau", "Sardauna", "Takum", "Ussa", "Wukari", "Yorro", "Zing"],
    "Yobe": ["Bade", "Bursari", "Damaturu", "Fika", "Fune", "Geidam", "Gujba", "Gulani", "Jakusko", "Karasuwa", "Machina", "Nangere", "Nguru", "Potiskum", "Tarmuwa", "Yunusari", "Yusufari"],
    "Zamfara": ["Anka", "Bakura", "Birnin Magaji/Kiyaw", "Bukkuyum", "Bungudu", "Gummi", "Gusau", "Kaura Namoda", "Maradun", "Maru", "Shinkafi", "Talata Mafara", "Chafe", "Zurmi"]
}

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    app_num = "SNSN-MEM-26-" + str(random.randint(001, 2999))
    
    if request.method == 'POST':
        # Get all data
        data = (
            app_num, request.form['name'], request.form['email'], request.form['phone'],
            request.form['dob'], request.form['gender'], request.form['marital'],
            request.form['religion'], request.form['state'], request.form['lga'],
            request.form['country'], request.form['id_type'], request.form['work'],
            app_num + ".jpg"
        )
        
        # Save passport
        file = request.files['passport']
        if file:
            file.save(os.path.join(UPLOAD_FOLDER, app_num + ".jpg"))
        
        # Save to database
        conn = sqlite3.connect('applicants.db')
        c = conn.cursor()
        c.execute("INSERT INTO applicants VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
        conn.commit()
        conn.close()
        
        return f'<script>window.location.href="/profile?app={app_num}"</script>'
    
    # Generate dropdown options for states
    state_options = "".join([f'<option value="{s}">{s}</option>' for s in states_lga.keys()])
    
    return f"""
    <html>
        <head>
            <style>
                body {{background-color: #1a1a2e; color: #ffffff; font-family: Arial; text-align: center; padding: 0; margin: 0;}}
                .navbar {{background-color: #0f3460; padding: 15px; text-align: center;}}
                .navbar a {{color: #00ff88; text-decoration: none; font-size: 16px; margin: 0 10px;}}
                h1 {{ color: #00ff88; font-size: 40px; margin-top: 40px; }}
                .app-number {{background-color: #ff00ff; padding: 10px 20px; border-radius: 10px; font-size: 20px; font-weight: bold; display: inline-block; margin-bottom: 20px;}}
                input, select {{width: 80%; padding: 12px; margin: 8px 0; border-radius: 8px; border: none; font-size: 16px;}}
                label {{display: block; text-align: left; margin-left: 10%; margin-top: 10px; font-weight: bold; color: #00ff88;}}
                button {{background-color: #00ff88; color: #1a1a2e; border: none; padding: 15px 30px; font-size: 18px; border-radius: 10px; cursor: pointer; margin-top: 20px; font-weight: bold;}}
                .form-box {{background-color: #0f3460; padding: 40px; border-radius: 15px; width: 500px; margin: 30px auto;}}
            </style>
        </head>
        <body>
            <div class="navbar">
                <a href="/">Home</a> | <a href="/signup">Sign Up</a> | <a href="/profile">Profile</a>
            </div>

            <h1>Registration Form</h1>
            <form method="POST" enctype="multipart/form-data" class="form-box">
                <p>Your Application Number:</p>
                <div class="app-number">{app_num}</div>
                
                <label>Full Name</label>
                <input type="text" name="name" required>
                
                <label>Email Address</label>
                <input type="email" name="email" required>
                
                <label>Phone Number</label>
                <input type="tel" name="phone" required>
                
                <label>Date of Birth</label>
                <input type="date" name="dob" required>
                
                <label>Gender</label>
                <select name="gender" required>
                    <option value="">Select Gender</option>
                    <option>Male</option><option>Female</option><option>Other</option>
                </select>
                
                <label>Marital Status</label>
                <select name="marital" required>
                    <option value="">Select</option>
                    <option>Single</option><option>Married</option><option>Divorced</option><option>Widowed</option>
                </select>
                
                <label>Religion</label>
                <select name="religion" required>
                    <option value="">Select</option>
                    <option>Christianity</option><option>Islam</option><option>Traditional</option><option>Other</option>
                </select>
                
                <label>State</label>
                <select name="state" id="state" required>
                    <option value="">Select State</option>
                    {state_options}
                </select>
                
                <label>LGA</label>
                <select name="lga" id="lga" required>
                    <option value="">Select LGA</option>
                </select>
                
                <label>Country</label>
                <select name="country" required>
                    <option value="">Select Country</option>
                    <option>Nigeria</option><option>Ghana</option><option>Kenya</option><option>USA</option><option>UK</option>
                </select>
                
                <label>Mode of Identification</label>
                <select name="id_type" required>
                    <option value="">Select ID</option>
                    <option>NIN</option><option>PVC</option><option>Driver License</option><option>International Passport</option>
                </select>
                
                <label>Nature of Work</label>
                <input type="text" name="work" required>
                
                <label>Upload Passport Photograph</label>
                <input type="file" name="passport" accept="image/*" required>
                
                <button type="submit">Submit Registration</button>
            </form>
            
            <script>
                // Simple JS to change LGA based on State
                const states = {str(states_lga).replace("'", '"')};
                document.getElementById('state').onchange = function() {{
                    const lga = document.getElementById('lga');
                    lga.innerHTML = '<option value="">Select LGA</option>';
                    states[this.value].forEach(x => {{
                        lga.innerHTML += `<option value="${{x}}">${{x}}</option>`;
                    }})
                }}
            </script>
        </body>
    </html>
    """
@app.route("/login")
def login():
    return """
    <html>
        <head>
            <style>
                body {background-color: #16213e; color: #ffffff; font-family: Arial; text-align: center; padding: 0; margin: 0;}
                .navbar {background-color: #0f3460; padding: 15px; text-align: center;}
                .navbar a {color: #00ff88; text-decoration: none; font-size: 16px; margin: 0 10px;}
                .navbar a:hover {color: #ff00ff;}
                h1 { color: #ff00ff; font-size: 40px; margin-top: 40px; }
                input {width: 80%; padding: 12px; margin: 10px 0; border-radius: 8px; border: none; font-size: 16px;}
                button {background-color: #ff00ff; color: #ffffff; border: none; padding: 15px 30px; font-size: 18px; border-radius: 10px; cursor: pointer; margin-top: 15px; font-weight: bold;}
                button:hover { background-color: #00ff88; color: #1a1a2e; }
                .form-box {background-color: #1a1a2e; padding: 40px; border-radius: 15px; width: 400px; margin: 30px auto; box-shadow: 0 0 20px rgba(255,0,255,0.3);}
                .link {color: #00ff88; margin-top: 20px; display: block;}
            </style>
        </head>
        <body>
            <div class="navbar">
                <a href="/">Home</a> | 
                <a href="/about">About</a> | 
                <a href="/services">Services</a> | 
                <a href="/portfolio">Portfolio</a> | 
                <a href="/blog">Blog</a> | 
                <a href="/testimonials">Testimonials</a> | 
                <a href="/signup">Sign Up</a> | 
                <a href="/login">Login</a> | 
                <a href="/profile">Profile</a> | 
                <a href="/contact">Contact</a>
            </div>

            <h1>Login</h1>
            <div class="form-box">
                <input type="email" placeholder="Email Address">
                <br>
                <input type="password" placeholder="Password">
                <br>
                <a href="/profile"><button>Login</button></a>
                <a href="/signup" class="link">Don't have an account? Sign Up</a>
            </div>
        </body>
    </html>
    """
from flask import request  # add this with other imports

@app.route("/profile")
def profile():
    # Get all data from URL
    name = request.args.get('name', 'User')
    email = request.args.get('email', 'user@email.com')
    phone = request.args.get('phone', '08000000000')
    state = request.args.get('state', 'Lagos')
    country = request.args.get('country', 'Nigeria')
    gender = request.args.get('gender', 'Male')
    religion = request.args.get('religion', 'Christianity')
    marital = request.args.get('marital', 'Single')
    id_type = request.args.get('id', 'NIN')
    work = request.args.get('work', 'Business')
    dob = request.args.get('dob', '01-01-2000')
    app_num = request.args.get('app', 'APP00000')
    img = request.args.get('img', '149071.png')
    
    return f"""
    <html>
        <head>
            <style>
                body {{background-color: #16213e; color: #ffffff; font-family: Arial; text-align: center; padding: 0; margin: 0;}}
                .navbar {{background-color: #0f3460; padding: 15px; text-align: center;}}
                .navbar a {{color: #00ff88; text-decoration: none; font-size: 16px; margin: 0 10px;}}
                h1 {{ color: #ff00ff; font-size: 40px; margin-top: 40px; }}
                .app-number {{background-color: #00ff88; color: #1a1a2e; padding: 10px 20px; border-radius: 10px; font-size: 20px; font-weight: bold; display: inline-block; margin-bottom: 20px;}}
                .profile-card {{background-color: #1a1a2e; padding: 40px; border-radius: 15px; width: 600px; margin: 30px auto; text-align: left;}}
                img {{border-radius: 50%; width: 120px; height: 120px; border: 4px solid #00ff88; margin-bottom: 20px; object-fit: cover; display: block; margin: 0 auto;}}
                .info {{font-size: 18px; line-height: 2;}}
                .info b {{color: #00ff88;}}
                .logout-btn {{background-color: #ff0044; color: #ffffff; border: none; padding: 12px 25px; font-size: 16px; border-radius: 10px; cursor: pointer; margin-top: 20px; display: block; margin: 20px auto 0;}}
            </style>
        </head>
        <body>
            <div class="navbar">
                <a href="/">Home</a> | <a href="/signup">Sign Up</a> | <a href="/profile">Profile</a>
            </div>

            <h1>Applicant Dashboard</h1>
            <div class="profile-card">
                <p style="text-align: center;">Application Number:</p>
                <div class="app-number" style="margin: 0 auto 20px; display: block; width: fit-content;">{app_num}</div>
                
                <img src="/static/uploads/{img}" alt="Passport">
                <h2 style="text-align: center;">Welcome, {name}!</h2>
                
                <div class="info">
                    <p><b>Email:</b> {email}</p>
                    <p><b>Phone:</b> {phone}</p>
                    <p><b>Date of Birth:</b> {dob}</p>
                    <p><b>Gender:</b> {gender}</p>
                    <p><b>Marital Status:</b> {marital}</p>
                    <p><b>Religion:</b> {religion}</p>
                    <p><b>State:</b> {state}</p>
                    <p><b>Country:</b> {country}</p>
                    <p><b>Mode of ID:</b> {id_type}</p>
                    <p><b>Nature of Work:</b> {work}</p>
                    <p><b>Status:</b> Active</p>
                </div>
                
                <a href="/"><button class="logout-btn">Log Out</button></a>
            </div>
        </body>
    </html>
    """
    import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
app.run(debug=True)
