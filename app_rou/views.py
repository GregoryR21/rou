import re
from django.shortcuts import render, redirect
from .models import *
from datetime import datetime



def index(request):
    game = Game.objects.get(id=1)
    counter = game.counter
    red = game.red
    black = game.black
    green = game.green
    even = game.even_steve
    odd = game.odd_todd
    _112 = game._112
    _212 = game._212
    _312 = game._312
    _118 = game._118
    _1936 = game._1936
    _col1 = game._col1
    _col2 = game._col2
    _col3 = game._col3
    _left = game._left
    _right = game._right
    _q1 = game._q1
    _q2 = game._q2
    _q3 = game._q3
    _q4 = game._q4
    _36 = game._36
    _35 = game._35
    _34 = game._34
    _33 = game._33
    _32 = game._32
    _31 = game._31
    _30 = game._30
    _29 = game._29
    _28 = game._28
    _27 = game._27
    _26 = game._26
    _25 = game._25
    _24 = game._24
    _23 = game._23
    _22 = game._22
    _21 = game._21
    _20 = game._20
    _19 = game._19
    _18 = game._18
    _17 = game._17
    _16 = game._16
    _15 = game._15
    _14 = game._14
    _13 = game._13
    _12 = game._12
    _11 = game._11
    _10 = game._10
    _9 = game._9
    _8 = game._8
    _7 = game._7
    _6 = game._6
    _5 = game._5
    _4 = game._4
    _3 = game._3
    _2 = game._2
    _1 = game._1
    _0 = game._0
    _00 = game._00
    context = { 
        "counter": counter,
        "red": red,
        "black": black,
        "green": green,
        "even": even,
        "odd": odd,
        "x112": _112,
        "x212": _212,
        "x312": _312,
        "x118": _118,
        "x1936": _1936,
        "col1": _col1,
        "col2": _col2,
        "col3": _col3,
        "left": _left,
        "right": _right,
        "q1": _q1,
        "q2": _q2,
        "q3": _q3,
        "q4": _q4,
        "x36": _36,
        "x35": _35,
        "x34": _34,
        "x33": _33,
        "x32": _32,
        "x31": _31,
        "x30": _30,
        "x29": _29,
        "x28": _28,
        "x27": _27,
        "x26": _26,
        "x25": _25,
        "x24": _24,
        "x23": _23,
        "x22": _22,
        "x21": _21,
        "x20": _20,
        "x19": _19,
        "x18": _18,
        "x17": _17,
        "x16": _16,
        "x15": _15,
        "x14": _14,
        "x13": _13,
        "x12": _12,
        "x11": _11,
        "x10": _10,
        "x9": _9,
        "x8": _8,
        "x7": _7,
        "x6": _6,
        "x5": _5,
        "x4": _4,
        "x3": _3,
        "x2": _2,
        "x1": _1,
        "x0": _0,
        "x00": _00,

    }
    return render(request, 'index.html', context)

def start(request):    
    if request.POST: 
        Game.objects.create( 
            counter = 0,
        )
        return redirect('/')

def add_number(request):
    if request.POST['number'] == "00": 
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update green number
        current_green = game_to_update.green 
        game_to_update.green = current_green + 1
        # update 00 number
        current_00 = game_to_update._00 
        game_to_update._00 = current_00 + 1
        test = Game.objects.all()
        print(test) 
        game_to_update.save()     
        return redirect('/')
    elif request.POST['number'] == "0":  
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update green number
        current_green = game_to_update.green 
        game_to_update.green = current_green + 1
        # update 0 number
        current_0 = game_to_update._0 
        game_to_update._0 = current_0 + 1
        test = Game.objects.all()
        print(test) 
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "1":
        print("inside of 1")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 1 number
        current_1 = game_to_update._1 
        game_to_update._1 = current_1 + 1
        # update 112 
        current_112 = game_to_update._112 
        game_to_update._112 = current_112 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col1 
        current_col1 = game_to_update._col1 
        game_to_update._col1 = current_col1 + 1
        # update odd 
        current_odd_todd = game_to_update.odd_todd 
        game_to_update.odd_todd = current_odd_todd + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q4 
        current_q4 = game_to_update._q4
        game_to_update._q4 = current_q4 + 1
        print("last line")
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "2":
        print("inside of 2")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 2 number
        current_2 = game_to_update._2 
        game_to_update._2 = current_2 + 1
        # update 112 
        current_112 = game_to_update._112 
        game_to_update._112 = current_112 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col2 
        current_col2 = game_to_update._col2 
        game_to_update._col2 = current_col2 + 1
        # update even 
        current_even_steve = game_to_update.even_steve 
        game_to_update.even_steve = current_even_steve + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q2 
        current_q2 = game_to_update._q2
        game_to_update._q2 = current_q2 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "3":
        print("inside of 3")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 3 number
        current_3 = game_to_update._3 
        game_to_update._3 = current_3 + 1
        # update 112 
        current_112 = game_to_update._112 
        game_to_update._112 = current_112 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col3 
        current_col3 = game_to_update._col3 
        game_to_update._col3 = current_col3 + 1
        # update odd 
        current_odd_todd = game_to_update.odd_todd 
        game_to_update.odd_todd = current_odd_todd + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q4 
        current_q4 = game_to_update._q4
        game_to_update._q4 = current_q4 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "4":
        print("inside of 4")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 4 number
        current_4 = game_to_update._4 
        game_to_update._4 = current_4 + 1
        # update 112 
        current_112 = game_to_update._112 
        game_to_update._112 = current_112 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col1 
        current_col1 = game_to_update._col1 
        game_to_update._col1 = current_col1 + 1
        # update even 
        current_even_steve = game_to_update.even_steve 
        game_to_update.even_steve = current_even_steve + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q2 
        current_q2 = game_to_update._q2
        game_to_update._q2 = current_q2 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "5":
        print("inside of 5")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 5 number
        current_5 = game_to_update._5 
        game_to_update._5 = current_5 + 1
        # update 112 
        current_112 = game_to_update._112 
        game_to_update._112 = current_112 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col2 
        current_col2 = game_to_update._col2 
        game_to_update._col2 = current_col2 + 1
        # update odd 
        current_odd_todd = game_to_update.odd_todd 
        game_to_update.odd_todd = current_odd_todd + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q4
        current_q4 = game_to_update._q4
        game_to_update._q4 = current_q4 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "6":
        print("inside of 6")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 6 number
        current_6 = game_to_update._6 
        game_to_update._6 = current_6 + 1
        # update 112 
        current_112 = game_to_update._112 
        game_to_update._112 = current_112 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col3
        current_col3 = game_to_update._col3 
        game_to_update._col3 = current_col3 + 1
        # update even 
        current_even_steve = game_to_update.even_steve 
        game_to_update.even_steve = current_even_steve + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q1
        current_q1 = game_to_update._q1
        game_to_update._q1 = current_q1 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "7":
        print("inside of 7")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 7 number
        current_7 = game_to_update._7 
        game_to_update._7 = current_7 + 1
        # update 112 
        current_112 = game_to_update._112 
        game_to_update._112 = current_112 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col1
        current_col1 = game_to_update._col1 
        game_to_update._col1 = current_col1 + 1
        # update odd 
        current_odd_todd = game_to_update.odd_todd
        game_to_update.odd_todd = current_odd_todd + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q3
        current_q3 = game_to_update._q3
        game_to_update._q3 = current_q3 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "8":
        print("inside of 8")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 8 number
        current_8 = game_to_update._8 
        game_to_update._8 = current_8 + 1
        # update 112 
        current_112 = game_to_update._112 
        game_to_update._112 = current_112 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col2
        current_col2 = game_to_update._col2
        game_to_update._col2 = current_col2 + 1
        # update even
        current_even_steve = game_to_update.even_steve
        game_to_update.even_steve = current_even_steve + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q1
        current_q1 = game_to_update._q1
        game_to_update._q1 = current_q1 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "9":
        print("inside of 9")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 9 number
        current_9 = game_to_update._9 
        game_to_update._9 = current_9 + 1
        # update 112 
        current_112 = game_to_update._112 
        game_to_update._112 = current_112 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col3
        current_col3 = game_to_update._col3
        game_to_update._col3 = current_col3 + 1
        # update odd
        current_odd_todd = game_to_update.odd_todd
        game_to_update.odd_todd = current_odd_todd + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q3
        current_q3 = game_to_update._q3
        game_to_update._q3 = current_q3 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "10":
        print("inside of 10")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 10 number
        current_10 = game_to_update._10 
        game_to_update._10 = current_10 + 1
        # update 112 
        current_112 = game_to_update._112 
        game_to_update._112 = current_112 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col1
        current_col1 = game_to_update._col1
        game_to_update._col1 = current_col1 + 1
        # update even
        current_even_steve = game_to_update.even_steve
        game_to_update.even_steve = current_even_steve + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q1
        current_q1 = game_to_update._q1
        game_to_update._q1 = current_q1 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "11":
        print("inside of 11")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 11 number
        current_11 = game_to_update._11 
        game_to_update._11 = current_11 + 1
        # update 112 
        current_112 = game_to_update._112 
        game_to_update._112 = current_112 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col2
        current_col2 = game_to_update._col2
        game_to_update._col2 = current_col2 + 1
        # update odd
        current_odd_todd = game_to_update.odd_todd
        game_to_update.odd_todd = current_odd_todd + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q3
        current_q3 = game_to_update._q3
        game_to_update._q3 = current_q3 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "12":
        print("inside of 12")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 12 number
        current_12 = game_to_update._12 
        game_to_update._12 = current_12 + 1
        # update 112 
        current_112 = game_to_update._112 
        game_to_update._112 = current_112 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col3
        current_col3 = game_to_update._col3
        game_to_update._col3 = current_col3 + 1
        # update even
        current_even_steve = game_to_update.even_steve
        game_to_update.even_steve = current_even_steve + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q1
        current_q1 = game_to_update._q1
        game_to_update._q1 = current_q1 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "13":
        print("inside of 13")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 13 number
        current_13 = game_to_update._13 
        game_to_update._13 = current_13 + 1
        # update 212 
        current_212 = game_to_update._212 
        game_to_update._212 = current_212 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col1
        current_col1 = game_to_update._col1
        game_to_update._col1 = current_col1 + 1
        # update odd
        current_odd_todd = game_to_update.odd_todd
        game_to_update.odd_todd = current_odd_todd + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q4
        current_q4 = game_to_update._q4
        game_to_update._q4 = current_q4 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "14":
        print("inside of 14")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 14 number
        current_14 = game_to_update._14 
        game_to_update._14 = current_14 + 1
        # update 212 
        current_212 = game_to_update._212 
        game_to_update._212 = current_212 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col2
        current_col2 = game_to_update._col2
        game_to_update._col2 = current_col2 + 1
        # update even
        current_even_steve = game_to_update.even_steve
        game_to_update.even_steve = current_even_steve + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q2
        current_q2 = game_to_update._q2
        game_to_update._q2 = current_q2 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "15":
        print("inside of 15")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 15 number
        current_15 = game_to_update._15 
        game_to_update._15 = current_15 + 1
        # update 212 
        current_212 = game_to_update._212 
        game_to_update._212 = current_212 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col3
        current_col3 = game_to_update._col3
        game_to_update._col3 = current_col3 + 1
        # update odd
        current_odd_todd = game_to_update.odd_todd
        game_to_update.odd_todd = current_odd_todd + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q4
        current_q4 = game_to_update._q4
        game_to_update._q4 = current_q4 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "16":
        print("inside of 16")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 16 number
        current_16 = game_to_update._16 
        game_to_update._16 = current_16 + 1
        # update 212 
        current_212 = game_to_update._212 
        game_to_update._212 = current_212 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col1
        current_col1 = game_to_update._col1
        game_to_update._col1 = current_col1 + 1
        # update even
        current_even_steve = game_to_update.even_steve
        game_to_update.even_steve = current_even_steve + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q2
        current_q2 = game_to_update._q2
        game_to_update._q2 = current_q2 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "17":
        print("inside of 17")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 17 number
        current_17 = game_to_update._17 
        game_to_update._17 = current_17 + 1
        # update 212 
        current_212 = game_to_update._212 
        game_to_update._212 = current_212 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col2
        current_col2 = game_to_update._col2
        game_to_update._col2 = current_col2 + 1
        # update odd
        current_odd_todd = game_to_update.odd_todd
        game_to_update.odd_todd = current_odd_todd + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q3
        current_q3 = game_to_update._q3
        game_to_update._q3 = current_q3 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "18":
        print("inside of 18")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 18 number
        current_18 = game_to_update._18 
        game_to_update._18 = current_18 + 1
        # update 212 
        current_212 = game_to_update._212 
        game_to_update._212 = current_212 + 1
        # update 118 
        current_118 = game_to_update._118 
        game_to_update._118 = current_118 + 1
        # update col3
        current_col3 = game_to_update._col3
        game_to_update._col3 = current_col3 + 1
        # update even
        current_even_steve = game_to_update.even_steve
        game_to_update.even_steve = current_even_steve + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q1
        current_q1 = game_to_update._q1
        game_to_update._q1 = current_q1 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "19":
        print("inside of 19")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 19 number
        current_19 = game_to_update._19 
        game_to_update._19 = current_19 + 1
        # update 212 
        current_212 = game_to_update._212 
        game_to_update._212 = current_212 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col1
        current_col1 = game_to_update._col1
        game_to_update._col1 = current_col1 + 1
        # update odd
        current_odd_todd = game_to_update.odd_todd
        game_to_update.odd_todd = current_odd_todd + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q1
        current_q1 = game_to_update._q1
        game_to_update._q1 = current_q1 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "20":
        print("inside of 20")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 20 number
        current_20 = game_to_update._20 
        game_to_update._20 = current_20 + 1
        # update 212 
        current_212 = game_to_update._212 
        game_to_update._212 = current_212 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col2
        current_col2 = game_to_update._col2
        game_to_update._col2 = current_col2 + 1
        # update even
        current_even_steve = game_to_update.even_steve
        game_to_update.even_steve = current_even_steve + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q3
        current_q3 = game_to_update._q3
        game_to_update._q3 = current_q3 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "21":
        print("inside of 21")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 21 number
        current_21 = game_to_update._21 
        game_to_update._21 = current_21 + 1
        # update 212 
        current_212 = game_to_update._212 
        game_to_update._212 = current_212 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col3
        current_col3 = game_to_update._col3
        game_to_update._col3 = current_col3 + 1
        # update odd
        current_odd_todd = game_to_update.odd_todd
        game_to_update.odd_todd = current_odd_todd + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q2
        current_q2 = game_to_update._q2
        game_to_update._q2 = current_q2 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "22":
        print("inside of 22")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 22 number
        current_22 = game_to_update._22 
        game_to_update._22 = current_22 + 1
        # update 212 
        current_212 = game_to_update._212 
        game_to_update._212 = current_212 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col1
        current_col1 = game_to_update._col1
        game_to_update._col1 = current_col1 + 1
        # update even
        current_even_steve = game_to_update.even_steve
        game_to_update.even_steve = current_even_steve + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q4
        current_q4 = game_to_update._q4
        game_to_update._q4 = current_q4 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "23":
        print("inside of 23")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 23 number
        current_23 = game_to_update._23 
        game_to_update._23 = current_23 + 1
        # update 212 
        current_212 = game_to_update._212 
        game_to_update._212 = current_212 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col2
        current_col2 = game_to_update._col2
        game_to_update._col2 = current_col2 + 1
        # update odd
        current_odd_todd = game_to_update.odd_todd
        game_to_update.odd_todd = current_odd_todd + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q2
        current_q2 = game_to_update._q2
        game_to_update._q2 = current_q2 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "24":
        print("inside of 24")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 24 number
        current_24 = game_to_update._24 
        game_to_update._24 = current_24 + 1
        # update 212 
        current_212 = game_to_update._212 
        game_to_update._212 = current_212 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col3
        current_col3 = game_to_update._col3
        game_to_update._col3 = current_col3 + 1
        # update even
        current_even_steve = game_to_update.even_steve
        game_to_update.even_steve = current_even_steve + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q4
        current_q4 = game_to_update._q4
        game_to_update._q4 = current_q4 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "25":
        print("inside of 25")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 25 number
        current_25 = game_to_update._25 
        game_to_update._25 = current_25 + 1
        # update 312 
        current_312 = game_to_update._312 
        game_to_update._312 = current_312 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col1
        current_col1 = game_to_update._col1
        game_to_update._col1 = current_col1 + 1
        # update odd
        current_odd_todd = game_to_update.odd_todd
        game_to_update.odd_todd = current_odd_todd + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q1
        current_q1 = game_to_update._q1
        game_to_update._q1 = current_q1 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "26":
        print("inside of 26")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 26 number
        current_26 = game_to_update._26 
        game_to_update._26 = current_26 + 1
        # update 312 
        current_312 = game_to_update._312 
        game_to_update._312 = current_312 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col2
        current_col2 = game_to_update._col2
        game_to_update._col2 = current_col2 + 1
        # update even
        current_even_steve = game_to_update.even_steve
        game_to_update.even_steve = current_even_steve + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q3
        current_q3 = game_to_update._q3
        game_to_update._q3 = current_q3 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "27":
        print("inside of 27")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 27 number
        current_27 = game_to_update._27 
        game_to_update._27 = current_27 + 1
        # update 312 
        current_312 = game_to_update._312 
        game_to_update._312 = current_312 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col3
        current_col3 = game_to_update._col3
        game_to_update._col3 = current_col3 + 1
        # update odd
        current_odd_todd = game_to_update.odd_todd
        game_to_update.odd_todd = current_odd_todd + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q1
        current_q1 = game_to_update._q1
        game_to_update._q1 = current_q1 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "28":
        print("inside of 28")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 28 number
        current_28 = game_to_update._28 
        game_to_update._28 = current_28 + 1
        # update 312 
        current_312 = game_to_update._312 
        game_to_update._312 = current_312 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col1
        current_col1 = game_to_update._col1
        game_to_update._col1 = current_col1 + 1
        # update even
        current_even_steve = game_to_update.even_steve
        game_to_update.even_steve = current_even_steve + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q3
        current_q3 = game_to_update._q3
        game_to_update._q3 = current_q3 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "29":
        print("inside of 29")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 29 number
        current_29 = game_to_update._29 
        game_to_update._29 = current_29 + 1
        # update 312 
        current_312 = game_to_update._312 
        game_to_update._312 = current_312 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col2
        current_col2 = game_to_update._col2
        game_to_update._col2 = current_col2 + 1
        # update odd
        current_odd_todd = game_to_update.odd_todd
        game_to_update.odd_todd = current_odd_todd + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q1
        current_q1 = game_to_update._q1
        game_to_update._q1 = current_q1 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "30":
        print("inside of 30")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 30 number
        current_30 = game_to_update._30 
        game_to_update._30 = current_30 + 1
        # update 312 
        current_312 = game_to_update._312 
        game_to_update._312 = current_312 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col3
        current_col3 = game_to_update._col3
        game_to_update._col3 = current_col3 + 1
        # update even
        current_even_steve = game_to_update.even_steve
        game_to_update.even_steve = current_even_steve + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q3
        current_q3 = game_to_update._q3
        game_to_update._q3 = current_q3 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "31":
        print("inside of 31")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 31 number
        current_31 = game_to_update._31 
        game_to_update._31 = current_31 + 1
        # update 312 
        current_312 = game_to_update._312 
        game_to_update._312 = current_312 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col1
        current_col1 = game_to_update._col1
        game_to_update._col1 = current_col1 + 1
        # update odd
        current_odd_todd = game_to_update.odd_todd
        game_to_update.odd_todd = current_odd_todd + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q1
        current_q1 = game_to_update._q1
        game_to_update._q1 = current_q1 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "32":
        print("inside of 32")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 32 number
        current_32 = game_to_update._32 
        game_to_update._32 = current_32 + 1
        # update 312 
        current_312 = game_to_update._312 
        game_to_update._312 = current_312 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col2
        current_col2 = game_to_update._col2
        game_to_update._col2 = current_col2 + 1
        # update even
        current_even_steve = game_to_update.even_steve
        game_to_update.even_steve = current_even_steve + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q3
        current_q3 = game_to_update._q3
        game_to_update._q3 = current_q3 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "33":
        print("inside of 33")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 33 number
        current_33 = game_to_update._33 
        game_to_update._33 = current_33 + 1
        # update 312 
        current_312 = game_to_update._312 
        game_to_update._312 = current_312 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col3
        current_col3 = game_to_update._col3
        game_to_update._col3 = current_col3 + 1
        # update odd
        current_odd_todd = game_to_update.odd_todd
        game_to_update.odd_todd = current_odd_todd + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q2
        current_q2 = game_to_update._q2
        game_to_update._q2 = current_q2 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "34":
        print("inside of 34")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 34 number
        current_34 = game_to_update._34 
        game_to_update._34 = current_34 + 1
        # update 312 
        current_312 = game_to_update._312 
        game_to_update._312 = current_312 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col1
        current_col1 = game_to_update._col1
        game_to_update._col1 = current_col1 + 1
        # update even
        current_even_steve = game_to_update.even_steve
        game_to_update.even_steve = current_even_steve + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q4
        current_q4 = game_to_update._q4
        game_to_update._q4 = current_q4 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "35":
        print("inside of 35")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update black number
        current_black = game_to_update.black 
        game_to_update.black = current_black + 1
        # update 35 number
        current_35 = game_to_update._35 
        game_to_update._35 = current_35 + 1
        # update 312 
        current_312 = game_to_update._312 
        game_to_update._312 = current_312 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col2
        current_col2 = game_to_update._col2
        game_to_update._col2 = current_col2 + 1
        # update odd
        current_odd_todd = game_to_update.odd_todd
        game_to_update.odd_todd = current_odd_todd + 1
        # update right 
        current_right = game_to_update._right
        game_to_update._right = current_right + 1
        # update q2
        current_q2 = game_to_update._q2
        game_to_update._q2 = current_q2 + 1
        game_to_update.save()
        return redirect('/')
    elif request.POST['number'] == "36":
        print("inside of 36")
        test = Game.objects.all()
        print(test)   
        game_to_update = Game.objects.get(id=1)
        current_counter = game_to_update.counter
        # update counter
        game_to_update.counter = current_counter + 1 
        # update red number
        current_red = game_to_update.red 
        game_to_update.red = current_red + 1
        # update 36 number
        current_36 = game_to_update._36 
        game_to_update._36 = current_36 + 1
        # update 312 
        current_312 = game_to_update._312 
        game_to_update._312 = current_312 + 1
        # update 1936 
        current_1936 = game_to_update._1936 
        game_to_update._1936 = current_1936 + 1
        # update col3
        current_col3 = game_to_update._col3
        game_to_update._col3 = current_col3 + 1
        # update even
        current_even_steve = game_to_update.even_steve
        game_to_update.even_steve = current_even_steve + 1
        # update left 
        current_left = game_to_update._left
        game_to_update._left = current_left + 1
        # update q4
        current_q4 = game_to_update._q4
        game_to_update._q4 = current_q4 + 1
        game_to_update.save()
        return redirect('/')
    else: 
        return redirect('/')
    
def restart(request):    
    if request.POST: 
        game_to_update = Game.objects.get(id=1) 
        game_to_update.counter = 0
        game_to_update.red = 0
        game_to_update.black = 0
        game_to_update.green = 0
        game_to_update.even_steve = 0
        game_to_update.odd_todd = 0
        game_to_update._112 = 0
        game_to_update._212 = 0
        game_to_update._312 = 0
        game_to_update._118 = 0
        game_to_update._1936 = 0
        game_to_update._col1 = 0
        game_to_update._col2 = 0
        game_to_update._col3 = 0
        game_to_update._00 = 0
        game_to_update._0 = 0
        game_to_update._1 = 0
        game_to_update._2 = 0
        game_to_update._3 = 0
        game_to_update._4 = 0
        game_to_update._5 = 0
        game_to_update._6 = 0
        game_to_update._7 = 0
        game_to_update._8 = 0
        game_to_update._9 = 0
        game_to_update._10 = 0
        game_to_update._11 = 0
        game_to_update._12 = 0
        game_to_update._13 = 0
        game_to_update._14 = 0
        game_to_update._15 = 0
        game_to_update._16 = 0
        game_to_update._17 = 0
        game_to_update._18 = 0
        game_to_update._19 = 0
        game_to_update._20 = 0
        game_to_update._21 = 0
        game_to_update._22 = 0
        game_to_update._23 = 0
        game_to_update._24 = 0
        game_to_update._25 = 0
        game_to_update._26 = 0
        game_to_update._27 = 0        
        game_to_update._28 = 0
        game_to_update._29 = 0
        game_to_update._30 = 0
        game_to_update._31 = 0
        game_to_update._32 = 0
        game_to_update._33 = 0
        game_to_update._34 = 0
        game_to_update._35 = 0
        game_to_update._36 = 0
        game_to_update._q1 = 0
        game_to_update._q2 = 0
        game_to_update._q3 = 0
        game_to_update._q4 = 0
        game_to_update.save()
        return redirect('/')