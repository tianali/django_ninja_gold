from django.shortcuts import render, redirect
import random
from datetime import datetime
# Create your views here.
def index(request):
    if not 'gold' in request.session: 
        request.session['gold'] = 0
        request.session['result'] = []
    return render(request, 'index.html')

def process_money(request):
    building = request.POST['place']
    original_gold = request.session['gold']
    if building == 'farm':
        request.session['gold'] += random.randint(10,21)
    elif building == 'cave':
        request.session['gold'] += random.randint(5, 11)
    elif building == 'home':
        request.session['gold'] += random.randint(2, 6)
    else:
        request.session['gold'] += random.randint(-50, 51)

    time = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    if request.session['gold'] < original_gold: 
        gold_lost = abs(original_gold - request.session['gold'])
        message = f"({time}): Entered a casino and lost {gold_lost} golds... Ouch.."
    else:
        message = f"({time}): Earned {abs(original_gold - request.session['gold'])} golds from the {building}!"
    request.session['result'].append(message)
    return redirect('/')
