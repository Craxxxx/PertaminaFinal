from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from var_dump import var_dump
from .models import User,CCTV,UserCCTV
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_required, current_user
import json
from sqlalchemy import select
from sqlalchemy.orm import Session

#render_template function is a function used to render the html templating

# Register blueprints on innit.py
views = Blueprint('views', __name__)
wincamss = []
engine = db.create_engine('mysql://root:@localhost:3306/pertamina')
# Register blueprints on innit.py

meta_data = db.MetaData(bind=engine)
db.MetaData.reflect(meta_data)

cctv_table = meta_data.tables['cctv']
ids = []


#MAIN CCTV ROUTES

#USER ROUTES
@views.route('/cctvAccess',methods=['GET'])
@login_required
def access():
    user_cctv = current_user
    print(user_cctv)
    # print(user_cctv)
    # print(user.cctvs)
    # exit()
    

    return render_template("User/cctvAccess.html", user_cctv = current_user, user = current_user)


@views.route('/User4x4',methods=['GET', 'POST'])
@login_required
def Userhome4x4():
    user = current_user
    # check if user is Admin
    if user.permission == "Admin":
         return render_template("Admin/4x4.html",user_cctv = user.cctvs, user=current_user, jinja1 = [1,2,3,4,5,6,7,8], jinja2 = [1,2], jinja3 = [1,2,3,4,5,6,7,8,9]) 
    # print(user.permission)
    # exit()
    index = 0
    # jinja = [1,2,3,4]
    # IF REFRESH BUTTON IS PRESSED
    try:
        print(wincamss)
        if request.method == "POST":
            # print(index)
            user_cctv = user.cctvs

            array_len = len(user_cctv)
            while index < array_len :
                wincamss[index] = request.form.get('wincam'+ str(index+1))
                index = index + 1

                                                    # passed in the relations
            print(wincamss)
            return render_template("User/4x4.html",user_cctv = user.cctvs, user=current_user, jinja1 = [1,2,3,4,5,6,7,8], jinja2 = [1,2], jinja3 = [1,2,3,4,5,6,7,8,9])
        # IF REFRESH BUTTON IS PRESSED

        elif request.method == "GET":
            user_cctv = user.cctvs
            
            array_len = len(user_cctv)
            print(wincamss)
            
            index = 0
            while(index < 9):

                wincamss.append(r"C:\Users\Raditya\Desktop\UNSRI\Pertamina\PertaminaProjects\PertaminaFinal\website\static\no-signal.mp4")
                # print("wincam" + str(1+index))
                index = index + 1
          
            return render_template("User/4x4.html",user_cctv = user.cctvs , user=current_user, jinja1 = [1,2,3,4,5,6,7,8], jinja2 = [1,2], jinja3 = 0)
    except IndexError:
        user_cctv = user.cctvs
        array_len = len(user_cctv)  
        index = 0
        while(index < 9):
            wincamss.append(r"C:\Users\Raditya\Desktop\UNSRI\Pertamina\PertaminaProjects\PertaminaFinal\website\static\no-signal.mp4")
            index = index + 1
        return render_template("User/4x4.html",user_cctv = user.cctvs , user=current_user, wincams = wincamss, jinja1 = [1,2,3,4,5,6,7,8], jinja2 = [1,2], jinja3 = [1,2,3,4,5,6,7,8,9])

@views.route('/User3x3',methods=['GET', 'POST'])
@login_required
def Userhome3x3():
    user = current_user
    index = 0
    # check if user is Admin
    if user.permission == "Admin" :
         return render_template("Admin/3x3.html",user_cctv = user.cctvs, user=current_user, jinja1 = [1,2,3], jinja2 = [1,2,3], jinja3 = [1,2,3,4,5,6,7,8,9])
    # jinja = [1,2,3,4]
    # IF REFRESH BUTTON IS PRESSED
    try:
        print(wincamss)
        if request.method == "POST":
            # print(index)
            user_cctv = user.cctvs

            array_len = len(user_cctv)
            while index < array_len :
                wincamss[index] = request.form.get('wincam'+ str(index+1))
                index = index + 1

                                                    # passed in the relations
            print(wincamss)
            return render_template("User/3x3.html",user_cctv = user.cctvs, user=current_user, jinja1 = [1,2,3], jinja2 = [1,2,3], jinja3 = [1,2,3,4,5,6,7,8,9])
        # IF REFRESH BUTTON IS PRESSED

        elif request.method == "GET":
            user_cctv = user.cctvs

            array_len = len(user_cctv)
            print(array_len)
            
            index = 0
            while(index < 9):

                wincamss.append(r"C:\Users\Raditya\Desktop\UNSRI\Pertamina\PertaminaProjects\PertaminaFinal\website\static\no-signal.mp4")
                # print("wincam" + str(1+index))
                index = index + 1
          
            return render_template("User/3x3.html",user_cctv = user.cctvs , user=current_user, jinja1 = [1,2,3], jinja2 = [1,2,3], jinja3 = 0)
    except IndexError:
        user_cctv = user.cctvs
        array_len = len(user_cctv)  
        index = 0
        while(index < 9):
            wincamss.append(r"C:\Users\Raditya\Desktop\UNSRI\Pertamina\PertaminaProjects\PertaminaFinal\website\static\no-signal.mp4")
            index = index + 1
        return render_template("User/3x3.html",user_cctv = user.cctvs , user=current_user, wincams = wincamss, jinja1 = [1,2,3], jinja2 = [1,2,3], jinja3 = [1,2,3,4,5,6,7,8,9])


@views.route('/User2x2',methods=['GET', 'POST'])
@login_required
def Userhome2x2():
    user = current_user
    if user.permission == "Admin" :
        return render_template("Admin/2x2.html",user_cctv = user.cctvs , user=current_user, wincams = wincamss, jinja = [1,2,3,4])
    index = 0
    jinja = [1,2,3,4]
    # IF REFRESH BUTTON IS PRESSED
    try:
        print(wincamss)
        if request.method == "POST":
            print(index)
            user_cctv = user.cctvs

            array_len = len(user_cctv)
            while index < array_len :
                wincamss[index] = request.form.get('wincam'+ str(index+1))
                index = index + 1

                                                    # passed in the relations
            return render_template("User/2x2.html",user_cctv = user.cctvs, user=current_user, jinja = [1,2,3,4])
        # IF REFRESH BUTTON IS PRESSED

        elif request.method == "GET":
            user_cctv = user.cctvs

            array_len = len(user_cctv)
            
            
            index = 0
            while(index < array_len):

                wincamss.append(r"C:\Users\Raditya\Desktop\UNSRI\Pertamina\PertaminaProjects\PertaminaFinal\website\static\no-signal.mp4")
                # print("wincam" + str(1+index))
                index = index + 1



            # print(wincam1)
            return render_template("User/2x2.html",user_cctv = user.cctvs , user=current_user, jinja = [1,2,3,4])
    except IndexError:
        user_cctv = user.cctvs
        array_len = len(user_cctv)
            
            
        index = 0
        while(index < array_len):
            wincamss.append(r"C:\Users\Raditya\Desktop\UNSRI\Pertamina\PertaminaProjects\PertaminaFinal\website\static\no-signal.mp4")
            index = index + 1
        return render_template("User/2x2.html",user_cctv = user.cctvs , user=current_user, wincams = wincamss, jinja = [1,2,3,4])

#USER ROUTES



#ADMIN ROUTES 
@views.route('/',methods=['GET', 'POST'])
@login_required
def home4x4():
    user = current_user
    # print(user.permission)
    # exit()
    index = 0
    # jinja = [1,2,3,4]
    # IF REFRESH BUTTON IS PRESSED
    try:
        print(wincamss)
        if request.method == "POST":
            # print(index)
            user_cctv = user.cctvs

            array_len = len(user_cctv)
            while index < array_len :
                wincamss[index] = request.form.get('wincam'+ str(index+1))
                index = index + 1

                                                    # passed in the relations
            print(wincamss)
            return render_template("Admin/4x4.html",user_cctv = user.cctvs, user=current_user, jinja1 = [1,2,3,4,5,6,7,8], jinja2 = [1,2], jinja3 = [1,2,3,4,5,6,7,8,9])
        # IF REFRESH BUTTON IS PRESSED

        elif request.method == "GET":
            user_cctv = user.cctvs

            array_len = len(user_cctv)
            print(array_len)
            
            index = 0
            while(index < 9):

                wincamss.append(r"C:\Users\Raditya\Desktop\UNSRI\Pertamina\PertaminaProjects\PertaminaFinal\website\static\no-signal.mp4")
                # print("wincam" + str(1+index))
                index = index + 1
          
            return render_template("Admin/4x4.html",user_cctv = user.cctvs , user=current_user, jinja1 = [1,2,3,4,5,6,7,8], jinja2 = [1,2], jinja3 = 0)
    except IndexError:
        user_cctv = user.cctvs
        array_len = len(user_cctv)  
        index = 0
        while(index < 9):
            wincamss.append(r"C:\Users\Raditya\Desktop\UNSRI\Pertamina\PertaminaProjects\PertaminaFinal\website\static\no-signal.mp4")
            index = index + 1
        return render_template("Admin/4x4.html",user_cctv = user.cctvs , user=current_user, wincams = wincamss, jinja1 = [1,2,3,4,5,6,7,8], jinja2 = [1,2], jinja3 = [1,2,3,4,5,6,7,8,9])


@views.route('/3x3',methods=['GET', 'POST'])
@login_required
def home3x3():
    user = current_user
    index = 0
    # jinja = [1,2,3,4]
    # IF REFRESH BUTTON IS PRESSED
    try:
        print(wincamss)
        if request.method == "POST":
            # print(index)
            user_cctv = user.cctvs

            array_len = len(user_cctv)
            while index < array_len :
                wincamss[index] = request.form.get('wincam'+ str(index+1))
                index = index + 1

                                                    # passed in the relations
            print(wincamss)
            return render_template("Admin/3x3.html",user_cctv = user.cctvs, user=current_user, jinja1 = [1,2,3], jinja2 = [1,2,3], jinja3 = [1,2,3,4,5,6,7,8,9])
        # IF REFRESH BUTTON IS PRESSED

        elif request.method == "GET":
            user_cctv = user.cctvs

            array_len = len(user_cctv)
            print(array_len)
            
            index = 0
            while(index < 9):

                wincamss.append(r"C:\Users\Raditya\Desktop\UNSRI\Pertamina\PertaminaProjects\PertaminaFinal\website\static\no-signal.mp4")
                # print("wincam" + str(1+index))
                index = index + 1
          
            return render_template("Admin/3x3.html",user_cctv = user.cctvs , user=current_user, jinja1 = [1,2,3], jinja2 = [1,2,3], jinja3 = 0)
    except IndexError:
        user_cctv = user.cctvs
        array_len = len(user_cctv)  
        index = 0
        while(index < 9):
            wincamss.append(r"C:\Users\Raditya\Desktop\UNSRI\Pertamina\PertaminaProjects\PertaminaFinal\website\static\no-signal.mp4")
            index = index + 1
        return render_template("Admin/3x3.html",user_cctv = user.cctvs , user=current_user, wincams = wincamss, jinja1 = [1,2,3], jinja2 = [1,2,3], jinja3 = [1,2,3,4,5,6,7,8,9])


@views.route('/2x2',methods=['GET', 'POST'])
@login_required
def home2x2():
    user = current_user
    index = 0
    jinja = [1,2,3,4]
    # IF REFRESH BUTTON IS PRESSED
    try:
        print(wincamss)
        if request.method == "POST":
            print(index)
            user_cctv = user.cctvs

            array_len = len(user_cctv)
            while index < array_len :
                wincamss[index] = request.form.get('wincam'+ str(index+1))
                index = index + 1

                                                    # passed in the relations
            return render_template("Admin/2x2.html",user_cctv = user.cctvs, user=current_user, jinja = [1,2,3,4])
        # IF REFRESH BUTTON IS PRESSED

        elif request.method == "GET":
            user_cctv = user.cctvs

            array_len = len(user_cctv)
            
            
            index = 0
            while(index < array_len):

                wincamss.append(r"C:\Users\Raditya\Desktop\UNSRI\Pertamina\PertaminaProjects\PertaminaFinal\website\static\no-signal.mp4")
                # print("wincam" + str(1+index))
                index = index + 1



            # print(wincam1)
            return render_template("Admin/2x2.html",user_cctv = user.cctvs , user=current_user, jinja = [1,2,3,4])
    except IndexError:
        user_cctv = user.cctvs
        array_len = len(user_cctv)
            
            
        index = 0
        while(index < array_len):
            wincamss.append(r"C:\Users\Raditya\Desktop\UNSRI\Pertamina\PertaminaProjects\PertaminaFinal\website\static\no-signal.mp4")
            index = index + 1
        return render_template("Admin/2x2.html",user_cctv = user.cctvs , user=current_user, wincams = wincamss, jinja = [1,2,3,4])


#ADDUSER
@views.route("/addUser", methods=['GET', 'POST'])
@login_required
def UserAdd():
    # if posting a data
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        permission = request.form.get('permission')

        user = User.query.filter_by(username=username).first()
        # if user already exist flash error 
        if user:
            flash('Username already exists.', category='error')
        else:
            new_user = User(email=email, username=username, password=password, permission=permission)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            
    #if requesting a data

    return render_template("Admin/AddUser.html", user=current_user, Users = User.query.all())
#ADD USER

#ADD CCTV
@views.route("/addcctv", methods=['GET', 'POST'])
@login_required
def addCCTV():
    
    if request.method == "POST":
        hostname = request.form.get('cctv_name')
        description = request.form.get('description')
        cctv_link = request.form.get('cctv_link')
        cctv_brand = request.form.get('cctv_brand')

        cctv = CCTV.query.filter_by(link_cctv=cctv_link).first()
        # print(cctv)
        # exit()
        # if cctv link already exist flash error
        if cctv:
            flash('CCTV link already exist!', category='error')
        else:
            new_cctv = CCTV(hostname=hostname, name_cctv=description, link_cctv=cctv_link, brand_cctv=cctv_brand)
            db.session.add(new_cctv)
            db.session.commit()
            flash('CCTV data inserted!', category='succsess')
    

    return render_template('Admin/AddCCTV.html', user=current_user, cctv=CCTV.query.all())
#ADD CCTV

#UPDATE CCTV
@views.route("/updatecctv/<int:id>", methods=['GET', 'POST'])
@login_required
def CCTVUpdate(id):

    Update = CCTV.query.get_or_404(id)
    

    if request.method == "POST":
        hostname = request.form.get('cctv_name')
        description = request.form.get('description')
        cctv_link = request.form.get('cctv_link')
        cctv_brand = request.form.get('cctv_brand')
        

        Update.hostname = hostname
        Update.name_cctv = description
        Update.link_cctv = cctv_link
        Update.brand_cctv = cctv_brand
        db.session.commit()
        flash("CCTV Updated!", category="success")
        return redirect(url_for('views.addCCTV'))
    return render_template("Admin/AddCCTV.html", cctv_to_update = CCTV.query.get_or_404(id), cctv = CCTV.query.all(), user = current_user)
#UPDATE CCTV

#UPDATE USER
@views.route("/updateUser/<int:id>", methods=['GET', 'POST'])
@login_required
def UserUpdate(id):
    #name_to_update is filled the related object
    # print(name_to_update)
    # exit()

    # ambil semua data user yang akan diubah
    Update = User.query.get_or_404(id)
    usr = current_user

    #if the form is sent
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        permission = request.form.get('permission')

        Update.username = username
        Update.email = email
        Update.password = password
        Update.permission = permission
        db.session.commit()
        flash("User Updated!", category="Success")
        return redirect(url_for('views.UserAdd',user = usr))
    #if the form is sent

    return render_template("Admin/AddUser.html", name_to_update=User.query.get_or_404(id), Users=User.query.all(), user = current_user)
#UPDATE USER

# DELETE USER
@views.route("/deleteUser/<int:id>", methods=['GET', 'POST'])
@login_required
def deleteUser(id):
    deleteUser = User.query.get_or_404(id)
    db.session.delete(deleteUser)
    db.session.commit()
    flash("User Berhasil Dihapus!", category="success")
    return redirect(url_for('views.UserAdd',user = current_user))
# DELETE USER

# DELETE CCTV
@views.route("/deletecctv/<int:id>", methods=['GET', 'POST'])
@login_required
def deleteCCTV(id):
    deleteCCTV = CCTV.query.get_or_404(id)
    db.session.delete(deleteCCTV)
    db.session.commit()
    flash("CCTV Berhasil Dihapus!", category="success")
    return redirect(url_for('views.addCCTV'))
# DELETE CCTV

#ADMIN ROUTES

#MANAGE USER ACCESS
@views.route("/manageCCTV/<int:id>", methods=['GET','POST'])
@login_required
def manageCCTV(id):
    test = User.query.filter_by(id=id).first()
    # print(test.cctv_association[5].id)
    # exit()
    cctv      = CCTV.query.all()
    # print(id)
    # if user press submit button
    if(request.method == "POST"):
        # DATAS IS AN array of cctv id from checked check box 
        datas = request.form.getlist('relation') #CCTV ID
        # cctv_data = CCTV.query.filter_by(id=datas[0]).first()
        # print(cctv_data)
        #TAKE ALL CCTV DATAS
        
        #TAKE ALL CCTV DATAS
        # DATAS IS AN ARRAY

        # USER IS AN OBJECT
        user   = User.query.filter_by(id=id).first() #USER EDITED DATA
        userid = user.id
        # USER IS AN OBJECT

        #INITIATION FOR A LOOP
        array_length = len(datas) #CALCULATE THE ARRAY LENGTH
        index = 0
        #INITIATION FOR A LOOP


        # loop success it needs a return value for the form to not loop three times
        # loop to administer the user relation with the associate cctv
        while index < array_length:
            cctv_data = CCTV.query.filter_by(id=datas[index]).first()
            new_relation = UserCCTV(user=user,cctv=cctv_data) # CREATE OBJECT FOR NEW RELATION
            db.session.add(new_relation)
            db.session.commit()
            index = index + 1
        return render_template('Admin/manageCCTV.html', user=current_user, user_cctv = User.query.filter_by(id=id).first(), cctv_view = CCTV.query.all(), check_cctv = filter_cctv(test), delete = test.cctv_association)
        # loop to administer the user relation with the associate cctv
    elif request.method == "GET":
        test = User.query.filter_by(id=id).first()
       

        return render_template('Admin/manageCCTV.html', user=current_user, user_cctv = User.query.filter_by(id=id).first(), cctv_view = CCTV.query.all() , check_cctv = filter_cctv(test), delete = test.cctv_association)
#MANAGE USER ACCESS

#FILTER DATA
def filter_cctv(Current_user):
    listcctv = []
        # print(listcctv)
    array_length = len(Current_user.cctvs)
    # print(array_length)
    index = 0
    while index < array_length:
        listcctv.append(Current_user.cctvs[index].id)
        index = index + 1
        # print(listcctv)
          
        # subq = db.session.query(UserCCTV).join(CCTV).filter(UserCCTV.user_id == 1).all()
        # subqs = []

        # print(subq)
    query = db.select([CCTV.id]).where(CCTV.id.not_in(listcctv))
    result = engine.execute(query).fetchall()
    # print(result)

    array2_length = len(result)
    # print(array2_length)
    cctvObject = []
    index2 = 0
    while index2 < array2_length:
        id = result[index2][0]
        print(id)
        cctvObject.append(CCTV.query.filter_by(id=id).first())
        # print("loop")
        index2 = index2 +1

    # print(cctvObject)


    # if cctv sudah di ceklis semua
    if len(cctvObject) == 0:
        return "sudah di ceklis"
    #if cctv belum ada yg di ceklis
    elif len(result) == 0: 
        return "belum ada yang di ceklis"
    else:
        return cctvObject
#FILTER DATA

#DELETE RELATION
@views.route("/deleterelation/<int:id>", methods=['GET', 'POST'])
@login_required
def deleteRelation(id):
    deleteRelation = UserCCTV.query.get_or_404(id)
    ids = deleteRelation.user_id
    db.session.delete(deleteRelation)
    db.session.commit()
    flash("Izin berhasil dihapus!", category="success")
    return redirect(url_for('views.manageCCTV',id = ids))


    # exit()
    # return 0
#DELETE RELATION





