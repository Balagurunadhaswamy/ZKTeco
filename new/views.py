from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def string_comp(request):
    return render(request, 'index.html')

@csrf_exempt
def save(request):
    '''
    Had to add 2 more alphabets to the given list to keep the index in range. 
    The function takes in a string and returns the desired output
    Eg:-
        Input = AAabbbE
        Output = A2ab3E

        'A' occurs twice, 'a' and 'E' occurs once and 'b' occurs thrice.

    The extra alphabets are removed at the end for the desired result.
    '''
    new = request.POST['your_name'] + "mn"

    input_string = [*new]
    output_string = ''
    counter = 1
    for index, elem in enumerate(input_string):
        if index == len(input_string) -1:
            break
        if elem == input_string[index+1]:
            counter += 1 
        else:
            output_string = output_string + str(elem+str(counter))
            counter = 1
            

    output_string = output_string[:len(output_string)-2]
    new_output = output_string.replace('1', '')
    
    return HttpResponse(new_output)