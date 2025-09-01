from django.contrib import messages
from django.shortcuts import render,redirect
from ad_min.models import wind_turbine,blade
from django.core.mail import send_mail

# Create your views here.

# homepage.......

def home(request):
    return render(request, 'home_page/home_page.html')

# admin login & logout

def adminlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email == "admin@gmail.com" and password == "admin":
            messages.info(request,"Admin Login Successful")
            return redirect("/adminhome/")
        else:
            messages.error(request,"wrong credentials")
            return render(request, 'ad_min/admin_login.html')

    else:
        return render(request, 'ad_min/admin_login.html')


def logout(request):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        try:
            del request.session['user_id']
            messages.info(request, 'Admin Logout Successful')
            return redirect('/')
        except blade.DoesNotExist:
            messages.error(request, 'User not found')
            return redirect('/')
    messages.info(request, 'Admin Logout Successful')
    return redirect('/')

# admin home...............

def adminhome(request):
    return render(request, 'ad_min/admin_home.html')

# admin requirements

def requirements(request):
    if request.method == 'POST':
        blade_length = request.POST.get('length')
        blade_width = request.POST.get('width')
        blade_weight = request.POST.get('weight')
        blade_circumference = request.POST.get('circumference')
        

        p=random.randint(1000,9999)
        project_id=f"Project:{p}"

        blade(blade_length=blade_length, blade_width=blade_width, blade_weight=blade_weight,
             blade_circumference=blade_circumference,project_id=project_id).save()
        messages.info(request, f"{project_id} :: Requirements Uploaded successfully.")
        return redirect('/adminhome/')  # Redirect to chief home after successful submission
    return render(request, 'ad_min/requirements.html')





#  approve & reject..........

import random
def approve(request,id):
    data=wind_turbine.objects.get(id=id)
    password=random.randint(1000,9999)
    print(password)
    data.password=password
    data.rh_id=f"SG:{password}"
    data.save()

    send_mail(
        '{0}:Username and Password'.format(data.department),
        'Hello {0},\n Your {1} profile has been Approved.\n Your Username is "{2}" and Password is "{3}".\n Make sure you use this Username and Password while your logging in to the portal of {1}.\n Thank You '.format(
            data.name,data.department, data.email,data.password),
        'anvi.aadiv@gmail.com',
        [data.email],
        fail_silently=False,
    )

    data.approve=True
    data.reject=False
    data.save()
    messages.info(request,f"{data.rh_id} : {data.department} Approval Successful")
    return redirect("/adminhome/")



def reject(request,id):
    data = wind_turbine.objects.get(id=id)
    data.approve=False
    data.reject=True
    data.save()

    subject = 'Client Rejection'
    plain_message = f"Hi {data.name},\nYour registration was rejected due to some reasons.try this later!"
    send_mail(subject, plain_message, 'kramesh.suryainfo@gmail.com', [data.email], fail_silently=False)

    # data.delete()
    messages.info(request, "Rejection Mail Sent to Client")
    return redirect("/adminhome/")


# approve & reject..........

def solvoapprove(request):
    data = wind_turbine.objects.filter(department='SOLVOLYSIS')
    return render(request, 'ad_min/solvo_approve.html',{'data': data})

def recapprove(request):
    data = wind_turbine.objects.filter(department='RECLAMATION')
    return render(request, 'ad_min/rec_approve.html',{'data': data})

def fabricapprove(request):
    data = wind_turbine.objects.filter(department='FABRICATION')
    return render(request, 'ad_min/fabric_approve.html',{'data': data})

def assessapprove(request):
    data = wind_turbine.objects.filter(department='ASSESSMENT')
    return render(request, 'ad_min/assess_approve.html',{'data': data})


# manage reports..........

def solvomanage(request):
    data = blade.objects.all()
    return render(request, 'ad_min/solvo_manage.html',{'data': data})

def recmanage(request):
    data = blade.objects.all()
    return render(request, 'ad_min/rec_manage.html',{'data': data})

def fabricmanage(request):
    data = blade.objects.all()
    return render(request, 'ad_min/fabric_manage.html',{'data': data})

def assessmanage(request):
    data = blade.objects.all()
    return render(request, 'ad_min/assess_manage.html',{'data': data})



# MANAGE STATUS

def managestatus(request):
    data = blade.objects.all()
    return render(request, "ad_min/manage_status.html", {'data': data})

# FINAL REPORT

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.shortcuts import redirect
from django.contrib import messages

def final_report(request, project_id):
    data = blade.objects.get(project_id=project_id)
    title = "LIFE CYCLE IMPACT OF BIO RESINS IN WIND TURBINES"

    # Create a BytesIO buffer to store PDF
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    def draw_title_and_project_id(c):
        c.setFont("Helvetica-Bold", 16)
        text_width = c.stringWidth(title)
        c.setFillColor(colors.blue)
        x_position = (c._pagesize[0] - text_width) / 2
        c.drawString(x_position, 800, title)

        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(colors.black)
        project_id_label = "Project ID:"
        text_width = c.stringWidth(project_id_label)
        x_position = (c._pagesize[0] - text_width - 100) / 2
        c.drawString(x_position, 780, project_id_label)

        c.setFillColor(colors.black)
        c.drawString(x_position + text_width + 5, 780, f"{data.project_id}")

    def draw_section(c, title, section_data, start_y):
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(colors.blue)
        c.drawString(50, start_y, title)
        start_y -= 10  # Reduced space between title and table

        table_data = [[f"{item[0]}", f"{item[1]}"] for item in section_data]
        table = Table(table_data, colWidths=[200, 250])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        table.wrapOn(c, 400, 400)
        table.drawOn(c, 50, start_y - len(section_data) * 20)

        return start_y - len(section_data) * 20 - 60

    draw_title_and_project_id(c)

    sections = [
        ("SOLVOLYSIS", [
            ["measurement of cut pieces (CM)", f"{data.measurement_of_cut_pieces}"],
            ["no of cut pieces", f"{data.no_of_cut_pieces}"],
            ["methanolysis heating time (Hours)", f"{data.methanolysis_heating_time}"],
            ["methanolysis heating temp (Fahrenheit)", f"{data.methanolysis_heating_temp}"],
        ]),
        ("RECLAMATION", [
            ["fibre glass (Kg)", f"{data.fibre_glass}"],
            ["carbon fibre (Kg)", f"{data.carbon_fibre}"],
            ["balsa wood (Kg)", f"{data.balsa_wood}"],
            ["polyol (Kg)", f"{data.polyol}"],
        ]),
        ("FABRICATION", [
            ["c_carbon fibre (Kg)", f"{data.c_carbon_fibre}"],
            ["f_fibre glass (Kg)", f"{data.f_fibre_glass}"],
            ["b_balsa wood (Kg)", f"{data.balsa_wood}"],
            ["pet foam (Kg)", f"{data.pet_foam}"],
            ["flax fibre (Kg)", f"{data.flax_fibre}"],
            ["basalt fibre (Kg)", f"{data.basalt_fibre}"],
            ["pecan resin (Kg)", f"{data.pecan_resin}"],
        ]),
        ("ASSESSMENT (FINAL REPORT)", [
            ["static testing (%)", f"{data.static_testing}"],
            ["fatigue testing (%)", f"{data.fatigue_testing}"],
            ["resonance testing (%)", f"{data.resonance_testing}"],
            ["environmental testing(%)", f"{data.environmental_testing}"],
            ["impact testing (%)", f"{data.impact_testing}"],
            ["aerodynamic testing (%)", f"{data.aerodynamic_testing}"],
            ["acoustic testing (%)", f"{data.acoustic_testing}"],
            ["lightning strike testing (%)", f"{data.lightning_strike_testing}"],
            ["non destructive testing (%)", f"{data.non_destructive_testing}"],
            ["full scale blade testing (%)", f"{data.full_scale_blade_testing}"],
        ])
    ]
    
    y_position = 750
    for section_title, section_data in sections:
        y_position = draw_section(c, section_title, section_data, y_position)

    if y_position < 150:
        c.showPage()
        y_position = 750

    c.save()

    pdf_data = buffer.getvalue()
    buffer.close()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{title}_{data.project_id}.pdf"'
    response.write(pdf_data)

    data.f_report.save(f"{title}_{data.project_id}.pdf", ContentFile(pdf_data))
    data.rep = False
    data.report = True
    data.save()

    messages.success(request, f"{data.project_id}, Report Generated successfully")
    return redirect('/managestatus/')
