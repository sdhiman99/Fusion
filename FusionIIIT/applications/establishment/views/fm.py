# FACULTY MANAGEMENT
from .utils import *


# TODO THIS
def handle_fm_admin(request):
    if 'fm_new_employee' in request.POST:
        # print (request.POST)
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'The given user ALREADY exists')
            return

        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            messages.error(request, 'The given passwords do not match.')
            return

        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email
        )
        user.set_password(password)
        user.save()
        
        title = request.POST.get('title')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        phone_no = request.POST.get('phone_no')
        dept = request.POST.get('department')
        department = DepartmentInfo.objects.filter(id=dept).first()
        # I'm using username as an id for Extra_info
        extra_info = ExtraInfo.objects.create(
            id = username,
            user = user,
            title = title,
            sex = gender,
            date_of_birth = dob,
            address = address,
            phone_no = phone_no,
            user_type = 'faculty',
            department = department,
        )
        faculty = Faculty.objects.create(
            id = extra_info
        )

        pf_number = request.POST.get('pf_number')
        date_of_joining = request.POST.get('date_of_joining')
        joining_payscale = request.POST.get('joining_payscale')
        isVac = request.POST.get('isVacational')
        if isVac == 'on':
            isVacational = True
        else:
            isVacational = False
        category = request.POST.get('category')
        desig = request.POST.get('designation')
        designation = Designation.objects.filter(id=desig).first()
        pan_number = request.POST.get('pan_number')
        aadhar_number = request.POST.get('aadhar_number')
        local_address = request.POST.get('local_address')
        marital_status = request.POST.get('marital_status')
        spouse_name = request.POST.get('spouse_name')
        children_info = request.POST.get('children_info')
        personal_email_id = request.POST.get('personal_email_id')

        faculty_info = Faculty_Info.objects.create(
            faculty_user = faculty,
            pf_number = pf_number,
            joining_date = date_of_joining,
            designation = designation,
            joining_payscale = joining_payscale,
            is_vacational = isVacational,
            category = category,
            pan_number = pan_number,
            aadhar_number = aadhar_number,
            local_address = local_address,
            marital_status = marital_status,
            spouse_name = spouse_name,
            children_info = children_info,
            personal_email_id = personal_email_id,
            is_archived = False
        )
        HoldsDesignation.objects.create(
            user = user,
            working = user,
            designation = designation,
            held_at = datetime.now()
        )
        establishment_notif(user, user, 'fm_new_faculty')
        messages.success(request, 'New Faculty user succesfully created')

    # elif 'fm_edit_faculty' in request.POST:

    # elif 'fm_delete_faculty' in request.POST:


# TODO THIS
def generate_fm_admin_lists(request):
    new_employee_form = Employee_Registration_Form()
    response = {
        'admin': True,
        'fm_add_employee_form' : new_employee_form
    }
    return response

