from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee, DeletedEmployee
from .serializers import EmployeeSerializer, DeletedEmployeeSerializer


# =========================
# CREATE + READ EMPLOYEES
# =========================
@api_view(['GET', 'POST'])
def employee_list(request):

    if request.method == 'GET':

        eid = request.GET.get('eid')
        name = request.GET.get('name')
        salary = request.GET.get('salary')
        department = request.GET.get('department')
        email = request.GET.get('email')

        if eid:
            employees = Employee.objects.filter(id=eid)

        elif name:
            employees = Employee.objects.filter(name__icontains=name)

        elif salary:
            employees = Employee.objects.filter(salary=salary)

        elif department:
            employees = Employee.objects.filter(department__icontains=department)

        elif email:
            employees = Employee.objects.filter(email__icontains=email)

        else:
            employees = Employee.objects.all()

        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':

        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


# =========================
# GET + UPDATE + DELETE
# =========================
@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, id):

    employee = get_object_or_404(Employee, id=id)

    # GET single employee
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    # UPDATE employee
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    # DELETE employee (with backup)
    elif request.method == 'DELETE':

        DeletedEmployee.objects.create(
            eid=employee.eid,
            name=employee.name,
            email=employee.email,
            department=employee.department,
            salary=employee.salary
        )

        employee.delete()

        return Response({
            "message": "Employee deleted successfully and saved in DeletedEmployee"
        })


# =========================
# GET DELETED EMPLOYEES
# =========================
@api_view(['GET'])
def deleted_employee_list(request):

    employees = DeletedEmployee.objects.all()
    serializer = DeletedEmployeeSerializer(employees, many=True)

    return Response(serializer.data)
from django.http import JsonResponse
from .models import Employee
def unique_employee_ids(request):
    ids = Employee.objects.values_list('eid', flat=True).distinct()
    return JsonResponse(list(ids), safe=False)
