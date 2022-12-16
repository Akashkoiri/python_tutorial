# def people(request):        
#     if request.method == 'GET':
#         if type(request.data) != list:
#             if request.data:
#                 if 'id' in request.data:
#                     try:
#                         person = Person.objects.get(id=request.data['id'])
#                         serialized = PersonSerial(person)
#                     except Exception:
#                         msg = "Person dosen't exist"
#                 else:
#                     msg = "Please provide an id"

#             else:
#                 people = Person.objects.all()
#                 serialized = PersonSerial(people, many=True)
#             return Response(serialized.data)
#         msg = "Please provide a right format"
#         return Response({'message': f"{msg}"})


def people(request):        
    if request.method == 'GET':
        if type(request.data) == list:
            msg = "Please provide a right format"

        if request.data:
            if 'id' not in request.data:
                msg = "Please provide an id"
            try:
                person = Person.objects.get(id=request.data['id'])
                serialized = PersonSerial(person)
            except Exception:
                msg = "Person dosen't exist"

        people = Person.objects.all()
        serialized = PersonSerial(people, many=True)
        return Response(serialized.data)